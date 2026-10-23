# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Compila FrameFusion in un unico eseguibile Windows e, a richiesta, prepara e pubblica la release.

    .venv\\Scripts\\python.exe scripts\\build_exe.py              solo dist/FrameFusion.exe
    .venv\\Scripts\\python.exe scripts\\build_exe.py --release    + zip e note di rilascio in dist/
    .venv\\Scripts\\python.exe scripts\\build_exe.py --publish    + release su GitHub con lo zip allegato

L'eseguibile e' un solo file, senza finestra console, con l'icona «FF» e le
proprieta' del file (versione, autore) compilate. Dentro ci sono Python, le
librerie (NumPy, OpenCV), il logo e l'icona; ffmpeg no: l'eseguibile lo cerca nella cartella
tools/ accanto a se' e, se manca, propone di scaricarlo. Il pacchetto
imageio-ffmpeg, se e' installato nel virtualenv, viene escluso di proposito.

--release produce dist/FrameFusion-<versione>-windows-x64.zip (exe, LICENSE,
NOTICE, README e la cartella licenses/ con i file di licenza di Python e delle
librerie dentro l'eseguibile, presi dal virtualenv: PyInstaller non li include)
e dist/release-notes-<versione>.md, con le novita' prese dalla sezione piu'
recente di CHANGELOG.md, l'elenco delle librerie e l'impronta SHA-256 dello zip.

--publish (che include --release) crea su GitHub la release «v<versione>» con
quelle note e vi allega lo zip. Il repository e' quello del remote «origin»;
serve un token con permesso di scrittura sui contenuti, letto dalla variabile
d'ambiente GITHUB_TOKEN oppure chiesto al momento (non viene salvato). La tag
viene creata da GitHub sul commit corrente del ramo, che quindi deve essere
gia' stato inviato con git push. Se una release con la stessa tag esiste gia',
lo script si ferma: alza la versione in framefusion/__init__.py.
"""

from __future__ import annotations

import getpass
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import platform
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from framefusion import APP_NAME, AUTHOR, AUTHOR_EMAIL, AUTHOR_URL, COPYRIGHT, __version__  # noqa: E402

ASSETS = ROOT / "framefusion" / "assets"
ICON = ASSETS / "framefusion.ico"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
CHANGELOG = ROOT / "CHANGELOG.md"
EXE = DIST / f"{APP_NAME}.exe"
ZIP = DIST / f"{APP_NAME}-{__version__}-windows-x64.zip"
NOTES = DIST / f"release-notes-{__version__}.md"
TAG = f"v{__version__}"
ZIP_FILES = ("LICENSE", "NOTICE", "README.md", "README.it.md")
# Librerie che PyInstaller mette nell'eseguibile senza i loro file di licenza:
# nome della distribuzione e licenza (quella scritta nel file di licenza del
# pacchetto). I file vengono copiati dal virtualenv in licenses/ dentro lo zip.
BUNDLED = (
    ("customtkinter", "MIT"),
    ("pillow", "MIT-CMU"),
    ("numpy", "BSD-3-Clause (bundled components under 0BSD, MIT, Zlib and CC0-1.0)"),
    ("opencv-python-headless", "Apache-2.0; the FFmpeg library it ships (opencv_videoio_ffmpeg*.dll) "
                               "is under the LGPL-2.1: see LICENSE-3RD-PARTY.txt"),
    ("darkdetect", "BSD-3-Clause"),
    ("packaging", "Apache-2.0 OR BSD-2-Clause"),
    ("fpdf2", "LGPL-3.0-only"),
    ("fonttools", "MIT"),
    ("defusedxml", "PSF-2.0"),
)
PYTHON_LICENSE = "PSF-2.0"

# Proprieta' del file mostrate da Esplora risorse (lingua 0x0409 = inglese).
VERSION_INFO = """\
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={numbers}, prodvers={numbers},
    mask=0x3f, flags=0x0, OS=0x40004, fileType=0x1, subtype=0x0, date=(0, 0),
  ),
  kids=[
    StringFileInfo([StringTable('040904B0', [
      StringStruct('CompanyName', {author!r}),
      StringStruct('FileDescription', {description!r}),
      StringStruct('FileVersion', {version!r}),
      StringStruct('InternalName', {name!r}),
      StringStruct('LegalCopyright', {copyright!r}),
      StringStruct('OriginalFilename', {exe!r}),
      StringStruct('ProductName', {name!r}),
      StringStruct('ProductVersion', {version!r}),
    ])]),
    VarFileInfo([VarStruct('Translation', [0x0409, 1200])]),
  ],
)
"""

RELEASE_NOTES = """\
{intro}

## What's new in {version}

{changes}

## Download

**{zip}** is the standalone program for Windows 10/11 (64-bit). Python is
not needed: unzip it anywhere and run `{exe}`.

Updating from a previous version: replace `{exe}` with the new one. Your
`tools` folder (ffmpeg) and `config.json` stay as they are.

## First start

- The interface starts in English; switch language (English, Italian, German,
  French, Spanish, Dutch, Polish, Greek, Albanian) in the *Language* box of the
  Configuration page.
- User manual with screenshots, in every language:
  [docs/manual](https://github.com/tingon11/FrameFusion/tree/main/docs/manual).
- ffmpeg is not included: at first start the program offers to download the
  official Windows build into a `tools` folder next to the executable.
- The executable is not signed, so Windows SmartScreen may show a warning the
  first time it runs.

## Verify the download

SHA-256 of `{zip}`:

```
{sha256}
```

## Bundled software

`{exe}` contains the Python interpreter and these libraries, each under
its own license; their license files are in the `licenses` folder of the zip:

{bundled}

## License

Free software under the GNU General Public License version 3 with additional
terms (author attribution): see `LICENSE` and `NOTICE`, included in the zip
together with the `licenses` folder (third-party license files).

Author: {author} — [{url}](https://{url}) — {email}
"""

LICENSES_README = """\
THIRD-PARTY SOFTWARE IN {exe}
{underline}

{exe}, built with PyInstaller, contains the Python interpreter and
the libraries listed below. Each of them remains under its own license. The
license files, copied from the installed packages, are in the subfolder named
after each one.

{entries}

FFmpeg itself (ffmpeg.exe) is not part of {exe}: see NOTICE.
{name} is free software under the GNU GPL v3 with additional terms: see
LICENSE and NOTICE next to the executable.
"""


# ------------------------------------------------------------------- build

def ensure_icon() -> None:
    if not ICON.is_file():
        sys.exit(f"Icona assente: {ICON}")


def ensure_pyinstaller() -> None:
    if importlib.util.find_spec("PyInstaller") is None:
        print("PyInstaller non presente: lo installo nel virtualenv…")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def version_file() -> Path:
    parts = [int(p) for p in __version__.split(".") if p.isdigit()][:4]
    numbers = tuple(parts + [0] * (4 - len(parts)))
    target = BUILD / "version_info.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        VERSION_INFO.format(
            numbers=numbers, author=AUTHOR, name=APP_NAME, version=__version__,
            description=f"{APP_NAME} - multi-frame video enhancement",
            copyright=COPYRIGHT, exe=EXE.name,
        ),
        encoding="utf-8",
    )
    return target


def build() -> None:
    ensure_icon()
    ensure_pyinstaller()
    argv = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean",
        "--onefile", "--windowed",
        "--name", APP_NAME,
        "--icon", str(ICON),
        "--version-file", str(version_file()),
        # logo e icona: il programma li cerca accanto a theme.py
        "--add-data", f"{ASSETS}{os.pathsep}framefusion/assets",
        # temi e caratteri di customtkinter sono file di dati, non moduli
        "--collect-data", "customtkinter",
        # i cataloghi delle lingue (framefusion/locales/*.py) sono importati per nome
        "--collect-submodules", "framefusion.locales",
        "--hidden-import", "PIL._tkinter_finder",
        # ffmpeg resta fuori: sta in tools/ accanto all'exe, non nel bundle
        "--exclude-module", "imageio_ffmpeg",
        "--exclude-module", "imageio",
        "--distpath", str(DIST),
        "--workpath", str(BUILD),
        "--specpath", str(BUILD),
        str(ROOT / "FrameFusion.py"),
    ]
    code = subprocess.call(argv, cwd=ROOT)
    if code != 0:
        sys.exit(code)
    print(f"\n{EXE}  ({EXE.stat().st_size / 1024 / 1024:.1f} MB)")


# ----------------------------------------------------------------- release

def changelog_section() -> tuple[str, str]:
    """Introduzione e novita' della versione corrente da CHANGELOG.md.

    Il file ha una sezione «## <versione>» per release; la prima riga di testo
    sotto il titolo fa da introduzione, il resto (elenco puntato) da novita'.
    """
    if not CHANGELOG.is_file():
        sys.exit(f"Manca {CHANGELOG.name}: scrivi la sezione «## {__version__}» con le novita'.")
    text = CHANGELOG.read_text(encoding="utf-8")
    match = re.search(rf"^## {re.escape(__version__)}\b[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if match is None:
        sys.exit(f"{CHANGELOG.name} non ha la sezione «## {__version__}»: aggiungila con le novita'.")
    lines = [line.rstrip() for line in match.group(1).strip().splitlines()]
    intro = lines[0] if lines and not lines[0].startswith(("-", "*")) else f"{APP_NAME} {__version__}."
    body = lines[1:] if intro == lines[0] else lines
    changes = "\n".join(body).strip() or "- Maintenance release."
    return intro, changes


class Bundled(NamedTuple):
    """Un componente dentro l'eseguibile, con i suoi file di licenza (percorso, nome relativo nello zip)."""
    name: str
    version: str
    license: str
    files: list[tuple[Path, str]]

    @property
    def folder(self) -> str:
        return f"{self.name}-{self.version}"


def dist_info_dir(dist: importlib.metadata.Distribution) -> Path:
    """Cartella <nome>-<versione>.dist-info di una distribuzione installata, trovata dai suoi file."""
    for file in dist.files or ():
        if file.name == "METADATA" and file.parent.name.endswith(".dist-info"):
            return Path(dist.locate_file(file.parent))
    sys.exit(f"Non trovo la cartella dist-info di {dist.metadata['Name']} {dist.version} nel virtualenv.")


def license_files(dist: importlib.metadata.Distribution) -> list[tuple[Path, str]]:
    """File di licenza di un pacchetto installato: (percorso, nome relativo da usare nello zip).

    Sono quelli che il wheel dichiara nel campo License-File dei metadati: i
    wheel recenti li mettono in <dist-info>/licenses/, quelli vecchi
    direttamente in <dist-info>/. Senza quel campo valgono i file LICENSE* e
    COPYING* presenti nella cartella dist-info. Se un file manca ci si ferma.
    """
    folder = dist_info_dir(dist)
    label = f"{dist.metadata['Name']} {dist.version}"
    names = dist.metadata.get_all("License-File") or []
    if not names:
        names = sorted(p.name for p in folder.iterdir()
                       if p.is_file() and p.name.upper().startswith(("LICENSE", "LICENCE", "COPYING")))
    if not names:
        sys.exit(f"{label} non dichiara file di licenza in {folder}: controlla il pacchetto a mano.")
    found = []
    for name in names:
        for candidate in (folder / "licenses" / name, folder / name):
            if candidate.is_file():
                found.append((candidate, name.replace("\\", "/")))
                break
        else:
            sys.exit(f"Manca il file di licenza {name} di {label} in {folder}.")
    return found


def bundled_software() -> list[Bundled]:
    """Python e ogni libreria in BUNDLED, con versione e file di licenza presi dal virtualenv."""
    items = []
    for name, license_name in BUNDLED:
        try:
            dist = importlib.metadata.distribution(name)
        except importlib.metadata.PackageNotFoundError:
            sys.exit(f"{name} non e' installato nel virtualenv: pip install -r requirements.txt")
        items.append(Bundled(dist.metadata["Name"], dist.version, license_name, license_files(dist)))
    python_license = Path(sys.base_prefix) / "LICENSE.txt"
    if not python_license.is_file():
        sys.exit(f"Manca la licenza di Python: {python_license}")
    items.append(Bundled("Python", platform.python_version(), PYTHON_LICENSE, [(python_license, "LICENSE.txt")]))
    return items


def licenses_readme(bundled: list[Bundled]) -> str:
    title = f"THIRD-PARTY SOFTWARE IN {EXE.name}"
    entries = "\n\n".join(f"{b.name} {b.version}\n  License: {b.license}\n  Files:   {b.folder}/" for b in bundled)
    return LICENSES_README.format(exe=EXE.name, underline="=" * len(title), entries=entries, name=APP_NAME)


def package() -> None:
    if not EXE.is_file():
        sys.exit(f"Manca {EXE}: esegui prima il build.")
    bundled = bundled_software()  # prima dello zip: se manca una licenza ci si ferma senza scrivere nulla
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(EXE, EXE.name)
        for name in ZIP_FILES:
            zf.write(ROOT / name, name)
        zf.writestr("licenses/README.txt", licenses_readme(bundled))
        for item in bundled:
            for path, relative in item.files:
                zf.write(path, f"licenses/{item.folder}/{relative}")
    sha256 = hashlib.sha256(ZIP.read_bytes()).hexdigest()
    intro, changes = changelog_section()
    # nelle note (Markdown) l'asterisco di opencv_videoio_ffmpeg*.dll va protetto
    listing = "\n".join(f"- {b.name} {b.version}: {b.license}".replace("*", "\\*") for b in bundled)
    NOTES.write_text(
        RELEASE_NOTES.format(intro=intro, version=__version__, changes=changes, zip=ZIP.name, exe=EXE.name,
                             sha256=sha256, bundled=listing, author=AUTHOR, url=AUTHOR_URL, email=AUTHOR_EMAIL),
        encoding="utf-8",
    )
    print(f"{ZIP}  ({ZIP.stat().st_size / 1024 / 1024:.1f} MB)\n{NOTES}\nSHA-256 {sha256}")


# ------------------------------------------------------------------ GitHub

def github_repo() -> tuple[str, str]:
    """(utente, repository) dal remote origin: https://github.com/u/r.git oppure git@github.com:u/r.git."""
    try:
        url = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        sys.exit("Nessun remote «origin»: collega prima il repository GitHub (git remote add origin …).")
    match = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?/?$", url)
    if match is None:
        sys.exit(f"Il remote origin non e' su GitHub: {url}")
    return match.group(1), match.group(2)


def github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("Serve un token GitHub con permesso di scrittura sui contenuti del repository")
        print("(Settings → Developer settings → Personal access tokens). Non viene salvato.")
        token = getpass.getpass("GITHUB_TOKEN: ").strip()
    if not token:
        sys.exit("Token assente.")
    return token


def github_call(method: str, url: str, token: str, data: bytes | None = None,
                content_type: str = "application/json") -> dict:
    request = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": f"{APP_NAME}-build/{__version__}",
        "Content-Type": content_type,
    })
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            body = response.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:400]
        sys.exit(f"GitHub ha risposto {exc.code} a {method} {url}:\n{detail}")
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        sys.exit(f"GitHub non raggiungibile: {exc}")


def publish() -> None:
    owner, repo = github_repo()
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip() or "main"
    if subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip():
        print("Attenzione: ci sono modifiche non ancora inviate con commit/push; la tag va sul commit corrente.")
    token = github_token()
    api = f"https://api.github.com/repos/{owner}/{repo}"

    # una release con questa tag non deve esistere: la versione va alzata
    request = urllib.request.Request(f"{api}/releases/tags/{TAG}", headers={
        "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
        "User-Agent": f"{APP_NAME}-build/{__version__}"})
    try:
        with urllib.request.urlopen(request, timeout=30):
            sys.exit(f"La release {TAG} esiste gia' su GitHub: alza __version__ in framefusion/__init__.py.")
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            sys.exit(f"GitHub ha risposto {exc.code} controllando la release {TAG}.")

    release = github_call("POST", f"{api}/releases", token, json.dumps({
        "tag_name": TAG, "target_commitish": branch, "name": f"{APP_NAME} {__version__}",
        "body": NOTES.read_text(encoding="utf-8"), "draft": False, "prerelease": False,
    }).encode("utf-8"))
    upload_url = release["upload_url"].split("{")[0] + "?" + urllib.parse.urlencode({"name": ZIP.name})
    github_call("POST", upload_url, token, ZIP.read_bytes(), content_type="application/zip")
    print(f"\nRelease pubblicata: {release['html_url']}")


def main() -> int:
    if sys.platform != "win32":
        sys.exit(f"{APP_NAME} si compila solo su Windows.")
    args = set(sys.argv[1:])
    unknown = args - {"--release", "--publish", "--no-build"}
    if unknown:
        sys.exit(f"Opzione sconosciuta: {' '.join(sorted(unknown))}. Vedi l'intestazione dello script.")
    if "--no-build" not in args:
        build()
    if "--release" in args or "--publish" in args:
        package()
    if "--publish" in args:
        publish()
    elif "--release" in args:
        print(f"Per pubblicare: rileggi {NOTES.name}, poi scripts\\build_exe.py --publish --no-build")
    else:
        print("Per distribuire l'exe usa --release: lo zip aggiunge LICENSE, NOTICE e le licenze delle librerie;"
              " ffmpeg lo scarica l'utente in tools/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
