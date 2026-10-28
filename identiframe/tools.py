# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Ricerca, download e aggiornamento di ffmpeg e dei modelli OCR nella cartella tools/.

ffmpeg e' un programma separato: viene cercato, nell'ordine, in
tools/ffmpeg/ffmpeg.exe accanto al programma, nel PATH di sistema e, se c'e',
nel pacchetto Python imageio-ffmpeg. Il download prende il build Windows
"release essentials" di gyan.dev, quello indicato dal sito ufficiale di FFmpeg
(https://ffmpeg.org/download.html#build-windows): dallo zip si tengono solo
ffmpeg.exe, LICENSE e README. Nessuna installazione globale, nessuna modifica
al PATH, nessun privilegio amministrativo: tutto resta dentro tools/.

I modelli OCR (facoltativi, per leggere targhe e scritte) seguono la stessa
idea: vedi la sezione «modelli OCR» piu' sotto.
"""

from __future__ import annotations

import datetime
import hashlib
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from . import __version__, procs
from .config import APP_DIR
from .i18n import tr

TOOLS_DIR = APP_DIR / "tools"
FFMPEG_DIR = TOOLS_DIR / "ffmpeg"
FFMPEG_EXE = FFMPEG_DIR / ("ffmpeg.exe" if sys.platform == "win32" else "ffmpeg")
VERSION_FILE = FFMPEG_DIR / "VERSION"

FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
FFMPEG_VERSION_URL = "https://www.gyan.dev/ffmpeg/builds/release-version"
FFMPEG_PAGE = "https://www.gyan.dev/ffmpeg/builds/"
KEEP_FILES = ("LICENSE", "README.txt")

USER_AGENT = f"IdentiFrame/{__version__}"
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

ProgressCb = Callable[[str, int, int], None]


class ToolsError(RuntimeError):
    """Errore durante la verifica o il download di ffmpeg."""


class Cancelled(Exception):
    """Download interrotto dall'utente."""


@dataclass
class Status:
    path: Path | None
    source: str = ""      # "tools", "path", "package" o ""
    version: str = ""

    @property
    def present(self) -> bool:
        return self.path is not None


def find() -> tuple[Path | None, str]:
    """Percorso di ffmpeg e da dove viene: tools/, PATH o pacchetto imageio-ffmpeg."""
    if FFMPEG_EXE.is_file():
        return FFMPEG_EXE, "tools"
    found = shutil.which("ffmpeg")
    if found:
        return Path(found), "path"
    try:
        import imageio_ffmpeg  # dipendenza facoltativa

        return Path(imageio_ffmpeg.get_ffmpeg_exe()), "package"
    except Exception:  # noqa: BLE001 - pacchetto assente o binario non disponibile
        return None, ""


def version_of(exe: Path) -> str:
    """Versione stampata da `ffmpeg -version` (es. "7.1-essentials_build-www.gyan.dev")."""
    try:
        result = procs.run([str(exe), "-version"], timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return ""
    first = result.stdout.decode("utf-8", "replace").splitlines()[:1]
    if not first or not first[0].startswith("ffmpeg version "):
        return ""
    return first[0].split()[2]


def status() -> Status:
    """Stato corrente: dove sta ffmpeg e che versione e' (la lettura avvia un processo)."""
    path, source = find()
    if path is None:
        return Status(None)
    return Status(path, source, version_of(path))


def installed_release() -> str:
    """Versione di release scritta in tools/ffmpeg/VERSION dall'ultimo download ("" se non c'e')."""
    try:
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


# ----------------------------------------------------------------- download

def _open(url: str, timeout: float = 30.0):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(request, timeout=timeout)


def latest_release() -> str:
    """Ultima versione di release pubblicata da gyan.dev (es. "7.1")."""
    try:
        with _open(FFMPEG_VERSION_URL) as response:
            text = response.read(200).decode("utf-8", "replace").strip()
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        raise ToolsError(tr("Cannot check the latest ffmpeg version: {error}").format(error=exc)) from exc
    if not text or len(text) > 40 or "\n" in text:
        raise ToolsError(tr("Unexpected answer from the ffmpeg download site."))
    return text


def _download(url: str, target: Path, label: str, progress: ProgressCb | None,
              cancel: threading.Event | None) -> None:
    """Scarica un file mostrando l'avanzamento; si ferma se `cancel` viene impostato."""
    try:
        with _open(url, timeout=60) as response:
            total = int(response.headers.get("Content-Length") or 0)
            done = 0
            with target.open("wb") as handle:
                while True:
                    if cancel is not None and cancel.is_set():
                        raise Cancelled()
                    block = response.read(256 * 1024)
                    if not block:
                        break
                    handle.write(block)
                    done += len(block)
                    if progress:
                        progress(tr("Downloading {label}").format(label=label), done, total)
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        raise ToolsError(tr("Download of {label} failed: {error}").format(label=label, error=exc)) from exc


def _extract_wanted(archive: Path, destination: Path) -> None:
    """Prende dallo zip solo ffmpeg.exe, LICENSE e README, rifiutando percorsi sospetti."""
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    wanted = {FFMPEG_EXE.name: "bin/" + FFMPEG_EXE.name}
    for name in KEEP_FILES:
        wanted[name] = name
    found: set[str] = set()
    try:
        with zipfile.ZipFile(archive) as zf:
            for member in zf.namelist():
                if not (root / member).resolve().is_relative_to(root):
                    raise ToolsError(tr("Invalid archive: suspicious path '{member}'.").format(member=member))
                parts = member.replace("\\", "/").split("/")
                for out_name, tail in wanted.items():
                    if "/".join(parts[-tail.count("/") - 1:]) == tail and out_name not in found:
                        with zf.open(member) as src, (destination / out_name).open("wb") as dst:
                            shutil.copyfileobj(src, dst, 1024 * 1024)
                        found.add(out_name)
    except zipfile.BadZipFile as exc:
        raise ToolsError(tr("The downloaded file is not a valid zip archive.")) from exc
    if FFMPEG_EXE.name not in found:
        raise ToolsError(tr("The downloaded package does not contain {name}.").format(name=FFMPEG_EXE.name))


def _replace_dir(source: Path, target: Path) -> None:
    """Sostituisce la cartella di destinazione con il contenuto scaricato."""
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        backup = target.with_name(target.name + ".old")
        shutil.rmtree(backup, ignore_errors=True)
        try:
            target.rename(backup)
        except OSError as exc:
            raise ToolsError(
                tr("Cannot update '{name}': files in use. Wait for the running fusion and try again.")
                .format(name=target.name)
            ) from exc
        shutil.rmtree(backup, ignore_errors=True)
    shutil.move(str(source), str(target))


def install(progress: ProgressCb | None = None, cancel: threading.Event | None = None) -> Path:
    """Scarica il build ufficiale e lascia ffmpeg.exe in tools/ffmpeg/. Restituisce l'eseguibile."""
    if sys.platform != "win32":
        raise ToolsError(tr("Automatic download is available on Windows only: install ffmpeg with the "
                            "system package manager."))
    release = ""
    try:
        release = latest_release()
    except ToolsError:
        pass  # la versione serve solo per i controlli futuri: il download puo' procedere lo stesso
    with tempfile.TemporaryDirectory(prefix="identiframe-") as tmp:
        tmp_dir = Path(tmp)
        archive = tmp_dir / "ffmpeg.zip"
        _download(FFMPEG_URL, archive, "ffmpeg", progress, cancel)
        if progress:
            progress(tr("Extracting ffmpeg"), 0, 0)
        out = tmp_dir / "ffmpeg"
        _extract_wanted(archive, out)
        if not version_of(out / FFMPEG_EXE.name):
            raise ToolsError(tr("The downloaded ffmpeg does not run on this PC."))
        if release:
            (out / VERSION_FILE.name).write_text(release + "\n", encoding="utf-8")
        _replace_dir(out, FFMPEG_DIR)
    if not FFMPEG_EXE.is_file():
        raise ToolsError(tr("{name} is missing after extraction.").format(name=FFMPEG_EXE.name))
    return FFMPEG_EXE


# ============================================================== modelli OCR
#
# La lettura dei caratteri (ocr.py) usa due modelli ONNX eseguiti dal modulo
# DNN di OpenCV, gia' nel programma: nessun eseguibile o libreria in piu', solo
# i file dei modelli, scaricati a richiesta in tools/ocr/ come ffmpeg e mai
# inclusi nell'exe.
#
# - targhe: fast-plate-ocr di ankandrew (MIT, codice e pesi), modello
#   cct-s-v2-global con la sua configurazione, dalla release «arg-plates»
#   del repository; la licenza MIT dei pesi, anche per l'uso commerciale, e'
#   confermata dall'autore in github.com/ankandrew/fast-plate-ocr/issues/97;
# - testo: PaddleOCR PP-OCRv6 small (Apache-2.0, pesi di Baidu / PaddleOCR)
#   nella conversione ONNX di RapidOCR 3.10.0 (Apache-2.0): rilevamento e
#   lettura delle righe, piu' l'elenco dei caratteri.
#
# Ogni file ha l'impronta SHA-256 fissata qui: un file diverso viene rifiutato.
# Accanto ai modelli si scaricano i testi di licenza e si scrive SOURCE.txt
# con provenienza, licenza e impronte.

OCR_DIR = TOOLS_DIR / "ocr"
_PLATE_URL = "https://github.com/ankandrew/fast-plate-ocr/releases/download/arg-plates/"
_RAPID_URL = "https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/v3.10.0/"


@dataclass(frozen=True)
class Download:
    name: str
    url: str
    sha256: str = ""      # vuota per i testi di licenza, che possono cambiare solo nella forma


@dataclass(frozen=True)
class OcrModel:
    key: str              # "plate" o "text": cartella in tools/ocr/
    title: str
    license: str
    page: str
    files: tuple[Download, ...]
    licenses: tuple[Download, ...]
    note: str = ""

    @property
    def folder(self) -> Path:
        return OCR_DIR / self.key

    def path(self, name: str) -> Path:
        return self.folder / name

    @property
    def present(self) -> bool:
        return all(self.path(item.name).is_file() for item in self.files)


PLATE_MODEL = OcrModel(
    "plate", "fast-plate-ocr cct-s-v2-global", "MIT", "https://github.com/ankandrew/fast-plate-ocr",
    files=(Download("cct_s_v2_global.onnx", _PLATE_URL + "cct_s_v2_global.onnx",
                    "384bbbd2cea3ef54761d3df70822ef3a349ee1a112aeafddbe0e3ba06bc6e47b"),
           Download("cct_s_v2_global_plate_config.yaml", _PLATE_URL + "cct_s_v2_global_plate_config.yaml",
                    "0335c74a305173bb6f393efed0fde03cadeaa0b649ed8e19f431016d8232d0a6")),
    licenses=(Download("LICENSE.txt", "https://raw.githubusercontent.com/ankandrew/fast-plate-ocr/master/LICENSE"),),
    note="Code and pretrained weights are MIT licensed: the author confirms it for the published .keras/.onnx "
         "models, commercial use included, in https://github.com/ankandrew/fast-plate-ocr/issues/97")
TEXT_MODEL = OcrModel(
    "text", "PaddleOCR PP-OCRv6 small (RapidOCR ONNX)", "Apache-2.0", "https://github.com/PaddlePaddle/PaddleOCR",
    files=(Download("PP-OCRv6_det_small.onnx", _RAPID_URL + "onnx/PP-OCRv6/det/PP-OCRv6_det_small.onnx",
                    "090f04abcd9d9a7498bc4ebf677e4cb9bdce1fe4197ddb7e529f1ef44e1ff94f"),
           Download("PP-OCRv6_rec_small.onnx", _RAPID_URL + "onnx/PP-OCRv6/rec/PP-OCRv6_rec_small.onnx",
                    "6f327246b50388f3c176ae304bd95767ea6dc0c9ae92153ef8cbe210b3c14884"),
           Download("ppocrv6_dict.txt", _RAPID_URL + "paddle/PP-OCRv6/rec/PP-OCRv6_rec_small/ppocrv6_dict.txt",
                    "b5f2bfe2bdd9448429e3e82b51c789775d9b42f2403d082b00662eb77e401c5d")),
    licenses=(Download("LICENSE-PaddleOCR.txt",
                       "https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/LICENSE"),
              Download("LICENSE-RapidOCR.txt", "https://raw.githubusercontent.com/RapidAI/RapidOCR/main/LICENSE"),
              Download("MODEL_LICENSES-RapidOCR.md",
                       "https://raw.githubusercontent.com/RapidAI/RapidOCR/main/python/MODEL_LICENSES.md")),
    note="Model weights copyright Baidu and/or the PaddleOCR rights holders, Apache-2.0; ONNX conversion by "
         "RapidOCR 3.10.0 (https://github.com/RapidAI/RapidOCR), Apache-2.0.")
OCR_MODELS = (PLATE_MODEL, TEXT_MODEL)


@dataclass
class OcrStatus:
    plate: bool
    text: bool

    def ready_for(self, kind: str) -> bool:
        return self.text if kind == "text" else self.plate


def ocr_status() -> OcrStatus:
    return OcrStatus(PLATE_MODEL.present, TEXT_MODEL.present)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _intact(model: OcrModel) -> bool:
    """Il modello c'e' gia', con le impronte giuste e le licenze: non serve riscaricarlo."""
    return (all(model.path(item.name).is_file() for item in model.files + model.licenses)
            and all(_sha256(model.path(item.name)) == item.sha256 for item in model.files))


def _check_onnx(folder: Path) -> None:
    """OpenCV deve riuscire a caricare ogni rete scaricata (con la correzione di ocr.opencv_safe)."""
    import cv2
    import numpy as np

    from .ocr import opencv_safe

    for path in sorted(folder.glob("*.onnx")):
        try:
            cv2.dnn.readNetFromONNX(np.frombuffer(opencv_safe(path.read_bytes()), np.uint8))
        except (cv2.error, ValueError) as exc:
            raise ToolsError(tr("OpenCV cannot load the downloaded model {name}.").format(name=path.name)) from exc


def _source_note(model: OcrModel) -> str:
    lines = [model.title, f"License: {model.license}", f"Project: {model.page}", model.note, "",
             f"Downloaded by IdentiFrame {__version__} on {datetime.date.today().isoformat()}:"]
    for item in model.files:
        lines += [f"  {item.name}", f"    {item.url}", f"    SHA-256 {item.sha256}"]
    lines.append("License texts:")
    lines += [f"  {item.name}  <-  {item.url}" for item in model.licenses]
    return "\n".join(lines) + "\n"


def install_ocr(progress: ProgressCb | None = None, cancel: threading.Event | None = None) -> Path:
    """Scarica in tools/ocr/ i modelli che mancano o non corrispondono, con licenze e SOURCE.txt.

    Ogni file viene controllato con la sua impronta SHA-256 e ogni rete con un
    caricamento di prova in OpenCV prima di sostituire la cartella del modello.
    Restituisce la cartella dei modelli.
    """
    with tempfile.TemporaryDirectory(prefix="identiframe-") as tmp:
        for model in OCR_MODELS:
            if _intact(model):
                continue
            out = Path(tmp) / model.key
            out.mkdir()
            for item in model.files + model.licenses:
                _download(item.url, out / item.name, item.name, progress, cancel)
                if item.sha256 and _sha256(out / item.name) != item.sha256:
                    raise ToolsError(tr("{name}: the downloaded file is not the expected one (its SHA-256 "
                                        "fingerprint is different).").format(name=item.name))
            _check_onnx(out)
            (out / "SOURCE.txt").write_text(_source_note(model), encoding="utf-8")
            _replace_dir(out, model.folder)
    return OCR_DIR
