# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Salvataggio del risultato con il rapporto che lo documenta.

Per ogni fusione salvata nasce una cartella con:

- result.<ext>           immagine finale
- fused.<ext>            la fusione prima di riduzione del rumore e deconvoluzione
- ghost.<ext>            i fotogrammi usati sovrapposti alla posizione in cui sono stati trovati
- reference_x<k>.<ext>   il riquadro del fotogramma di riferimento ingrandito (bicubica), per confronto
- reference_crop.<ext>   lo stesso riquadro alla risoluzione del video
- aligned/               a richiesta, ogni fotogramma usato riportato sulla griglia del riferimento
- report.txt             rapporto leggibile (nella lingua dell'interfaccia)
- report.pdf             lo stesso rapporto impaginato, con le immagini (pdfreport.py)
- report.json            gli stessi dati, in forma strutturata

Il rapporto elenca sorgente (con impronta SHA-256), intervallo, riferimento,
riquadro, parametri, i sette passaggi con i metodi usati, la tabella dei
fotogrammi (punteggi, spostamenti, pesi, motivo dell'esclusione) e le impronte
dei file prodotti: chi lo legge puo' ripetere l'elaborazione.
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import hashlib
import json
import math
import platform
from pathlib import Path
from typing import Callable

import cv2
import numpy as np

from . import APP_NAME, CREDITS, __version__, pdfreport
from .fusion import (DENOISE_LABELS, LOCAL_CONTRAST, LOCAL_CONTRAST_LABELS, METHOD_LABELS, MOTION_LABELS,
                     REGULARIZATION, REGULARIZATION_LABELS, STEPS, FrameRecord, Result, aligned_frame)
from .i18n import tr, upper
from .timeline import format_time

EXTENSIONS = {"PNG": "png", "TIFF": "tif"}


def settings_from_report(path: Path) -> dict:
    """Le impostazioni della pipeline scritte in un report.json (anche di una versione senza «settings»)."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "parameters" not in data:
        raise ValueError(tr("{name} is not a FrameFusion report.").format(name=Path(path).name))
    settings = data.get("settings")
    if isinstance(settings, dict):
        return settings
    p = data["parameters"]
    return {
        "motion": p.get("motion_model"), "track_min": p.get("tracking_min_score"),
        "min_quality": p.get("min_alignment_quality"), "keep": p.get("keep_sharpest_percent"),
        "scale": p.get("scale"), "method": p.get("method"), "weight_sharpness": p.get("weight_by_sharpness"),
        "equalize": p.get("equalize_brightness"), "denoise": p.get("denoise"),
        "iterations": p.get("deconvolution_iterations"),
        "psf_sigma": 0.0 if p.get("psf_sigma_auto", True) else p.get("psf_sigma_px"),
        "regularization": p.get("regularization"), "levels": p.get("auto_levels"),
        "local_contrast": p.get("local_contrast"), "grayscale": p.get("grayscale"),
    }


def folder_name(result: Result, when: dt.datetime) -> str:
    return f"fusion_f{result.alignment.request.ref:06d}_{when:%Y%m%d-%H%M%S}"


def sha256(path: Path, cancel: Callable[[], bool] | None = None) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            if cancel is not None and cancel():
                raise InterruptedError
            digest.update(block)
    return digest.hexdigest()


def write_image(path: Path, image: np.ndarray, fmt: str, bits: int) -> None:
    """Immagine RGB in virgola mobile (0..1) in PNG o TIFF a 8 o 16 bit per canale, senza perdita.

    cv2.imwrite non accetta percorsi con caratteri non ASCII su Windows: si
    codifica in memoria e si scrive il file con Python.
    """
    top = 65535.0 if bits == 16 else 255.0
    data = np.round(np.clip(image, 0.0, 1.0) * top).astype(np.uint16 if bits == 16 else np.uint8)
    bgr = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
    ok, encoded = cv2.imencode("." + EXTENSIONS[fmt], bgr)
    if not ok:
        raise OSError(tr("Cannot encode {name}.").format(name=path.name))
    path.write_bytes(encoded.tobytes())


def save(result: Result, base: Path, fmt: str, bits: int, save_aligned: bool,
         progress: Callable[[str], None]) -> Path:
    """Scrive la cartella della fusione e restituisce il suo percorso."""
    when = dt.datetime.now()
    folder = base / folder_name(result, when)
    folder.mkdir(parents=True, exist_ok=False)
    ext = EXTENSIONS[fmt]
    s = result.final.shape[1] // result.alignment.request.roi[2]
    files: dict[str, Path] = {
        "result": folder / f"result.{ext}",
        "fused": folder / f"fused.{ext}",
        "ghost": folder / f"ghost.{ext}",
        "reference": folder / f"reference_x{s}.{ext}",
        "reference_crop": folder / f"reference_crop.{ext}",
    }
    progress(tr("Writing the images…"))
    write_image(files["result"], result.final, fmt, bits)
    write_image(files["fused"], result.fused, fmt, bits)
    write_image(files["ghost"], result.ghost, fmt, bits)
    write_image(files["reference"], result.reference, fmt, bits)
    write_image(files["reference_crop"], result.reference_native, fmt, bits)
    aligned: list[Path] = []
    if save_aligned:
        (folder / "aligned").mkdir()
        used = [r for r in result.alignment.frames if r.used]
        for n, record in enumerate(used, start=1):
            progress(tr("Writing the aligned frames: {done} / {total}").format(done=n, total=len(used)))
            path = folder / "aligned" / f"f{record.index:06d}.{ext}"
            write_image(path, aligned_frame(result, record), fmt, bits)
            aligned.append(path)

    progress(tr("Computing the SHA-256 fingerprints…"))
    video = result.alignment.request.info.path
    hashes = {"source": sha256(video)}
    for key, path in files.items():
        hashes[key] = sha256(path)
    data = _data(result, when, folder, files, hashes, fmt, bits, aligned)
    (folder / "report.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    document = sections(result, data)
    (folder / "report.txt").write_text(_text(document), encoding="utf-8")
    progress(tr("Writing the PDF report…"))
    pdfreport.write(folder / "report.pdf", document, result)
    return folder


# ------------------------------------------------------------------- dati

def _num(value: float, digits: int = 4) -> float | None:
    return None if value is None or not math.isfinite(value) else round(float(value), digits)


def _frame_row(record: FrameRecord) -> dict:
    return {
        "frame": record.index,
        "time_s": round(record.time, 6),
        "tracking_score": _num(record.track_score),
        "subject_found": record.found,
        "ecc_coarse": _num(record.cc_coarse),
        "ecc_fine": _num(record.cc_fine),
        "shift_x_px": _num(record.shift[0], 3),
        "shift_y_px": _num(record.shift[1], 3),
        "sharpness": _num(record.sharpness),
        "gain": [_num(record.gain[0]), _num(record.gain[1])],
        "motion_model": record.model or None,
        "warp": None if record.warp is None else [[round(float(v), 6) for v in row] for row in record.warp],
        "used": record.used,
        "weight": _num(record.weight),
        "excluded_because": record.reason or None,
    }


def _data(result: Result, when: dt.datetime, folder: Path, files: dict[str, Path], hashes: dict[str, str],
          fmt: str, bits: int, aligned: list[Path]) -> dict:
    alignment = result.alignment
    request = alignment.request
    info = request.info
    params = result.params
    x, y, w, h = request.roi
    H, W = result.final.shape[:2]
    return {
        "software": {"name": APP_NAME, "version": __version__, "credits": CREDITS,
                     "python": platform.python_version(), "opencv": cv2.__version__, "numpy": np.__version__},
        "created": when.isoformat(timespec="seconds"),
        "source": {
            "file": str(info.path), "size_bytes": info.path.stat().st_size, "sha256": hashes["source"],
            "width": info.width, "height": info.height, "fps": info.fps, "duration_s": info.duration,
            "codec": info.codec, "pix_fmt": info.pix_fmt, "bit_depth": info.bit_depth, "rotation": info.rotation,
        },
        "range": {"first": request.first, "last": request.last, "reference": request.ref,
                  "frames": request.last - request.first + 1},
        "subject_area": {"x": x, "y": y, "width": w, "height": h},
        # le impostazioni cosi' come le usa il programma: si ricaricano con «Da rapporto…»
        "settings": dataclasses.asdict(params),
        "parameters": {
            "motion_model": params.motion, "tracking_min_score": params.track_min,
            "min_alignment_quality": params.min_quality, "keep_sharpest_percent": params.keep,
            "scale": W // w, "method": params.method, "weight_by_sharpness": params.weight_sharpness,
            "equalize_brightness": params.equalize, "denoise": params.denoise,
            "deconvolution_iterations": params.iterations,
            "psf_sigma_px": round(result.psf_sigma, 4), "psf_sigma_auto": params.psf_sigma <= 0,
            "fusion_kernel_sigma_px": round(result.kernel_sigma, 4) if params.method == "shift-and-add" else None,
            "regularization": params.regularization,
            "regularization_lambda": REGULARIZATION.get(params.regularization, 0.0),
            "auto_levels": params.levels,
            "auto_levels_black_white": [round(v, 4) for v in result.levels] if params.levels else None,
            "local_contrast": params.local_contrast,
            "local_contrast_clip_limit": LOCAL_CONTRAST.get(params.local_contrast, 0.0),
            "grayscale": params.grayscale,
        },
        "steps": [{"step": i + 1, "name": STEPS[i], "seconds": round(result.timings.get(i, 0.0), 3)}
                  for i in range(len(STEPS))],
        "notes": [str(note) for note in result.notes],
        "frames": [_frame_row(r) for r in alignment.frames],
        "result": {
            "width": W, "height": H, "frames_used": len(result.used), "frames_used_list": result.used,
            "noise_sigma_0_255": {k: round(v, 3) for k, v in result.noise.items()},
            "samples_per_output_pixel": round(result.coverage, 3),
            "subpixel_phases_covered": round(result.subpixel, 3),
        },
        "output": {
            "folder": str(folder), "format": fmt, "bits_per_channel": bits,
            "files": {key: {"name": path.name, "sha256": hashes[key]} for key, path in files.items()},
            "aligned_frames": [p.name for p in aligned],
        },
    }


# --------------------------------------------------------------- sezioni

@dataclasses.dataclass
class Section:
    """Una sezione del rapporto, resa in testo e in PDF.

    kind: "kv" (coppie etichetta/valore), "steps" (nome, secondi, descrizione),
    "table" (head + righe di celle), "files" (nome, SHA-256), "paragraphs".
    """

    title: str
    kind: str
    rows: list = dataclasses.field(default_factory=list)
    extra: list[str] = dataclasses.field(default_factory=list)   # righe in coda (note, conteggi)
    head: tuple[str, ...] = ()
    widths: tuple[float, ...] = ()        # larghezze relative delle colonne (tabelle)
    aligns: tuple[str, ...] = ()
    mono: bool = False                    # valori a spaziatura fissa (impronte)


@dataclasses.dataclass
class Document:
    title: str
    credits: str
    created: str
    sections: list[Section]


def sections(result: Result, data: dict) -> Document:
    """Il rapporto come struttura: la stessa per report.txt e report.pdf."""
    alignment = result.alignment
    request = alignment.request
    info = request.info
    params = result.params
    src = data["source"]
    res = data["result"]
    par = data["parameters"]
    hours = info.duration >= 3600
    when = dt.datetime.fromisoformat(data["created"])
    count = request.last - request.first + 1
    out: list[Section] = []

    out.append(Section(tr("Source"), "kv", [
        (tr("File"), src["file"]),
        (tr("Size"), tr("{size} bytes").format(size=f"{src['size_bytes']:,}".replace(",", "."))),
        ("SHA-256", src["sha256"]),
        (tr("Video"), tr("{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}").format(
            width=info.width, height=info.height, fps=f"{info.fps:g}", codec=info.codec, pix_fmt=info.pix_fmt,
            bits=info.bit_depth, duration=format_time(info.duration, hours=hours))),
    ]))

    x, y, w, h = request.roi
    out.append(Section(tr("Range and subject"), "kv", [
        (tr("Frames"), tr("f{first} → f{last} ({count} frames, {start} → {end})").format(
            first=request.first, last=request.last, count=count,
            start=format_time(request.first / info.fps, hours=hours),
            end=format_time(request.last / info.fps, hours=hours))),
        (tr("Reference frame"), f"f{request.ref} ({format_time(request.ref / info.fps, hours=hours)})"),
        (tr("Subject area on the reference frame"), tr("x {x}, y {y}, {width} × {height} pixels").format(
            x=x, y=y, width=w, height=h)),
    ]))

    out.append(Section(tr("Parameters"), "kv", [
        (tr("Motion model"), tr(MOTION_LABELS[params.motion])),
        (tr("Subject search: minimum correlation"), f"{params.track_min:.2f}"),
        (tr("Minimum alignment quality (ECC)"), f"{params.min_quality:.2f}"),
        (tr("Sharpest frames kept"), f"{params.keep} %"),
        (tr("Scale"), f"×{par['scale']}"),
        (tr("Fusion method"), tr(METHOD_LABELS[params.method])),
        (tr("Weight by sharpness"), tr("yes") if params.weight_sharpness else tr("no")),
        (tr("Equalize brightness"), tr("yes") if params.equalize else tr("no")),
        (tr("Noise reduction"), tr(DENOISE_LABELS[params.denoise])),
        (tr("Deconvolution"), tr("{iterations} Richardson-Lucy iterations").format(iterations=params.iterations)
         if params.iterations > 0 else tr("not applied")),
        (tr("PSF σ"), tr("{sigma:.2f} px of the output ({mode})").format(
            sigma=result.psf_sigma,
            mode=tr("automatic: measured on the edges of the fused image") if params.psf_sigma <= 0 else tr("manual"))),
        (tr("Regularization (total variation)"), tr(REGULARIZATION_LABELS[params.regularization])),
        (tr("Auto levels"), tr("yes") if params.levels else tr("no")),
        (tr("Local contrast (CLAHE)"), tr(LOCAL_CONTRAST_LABELS[params.local_contrast])),
        (tr("Grayscale"), tr("yes") if params.grayscale else tr("no")),
    ]))

    used = len(result.used)
    found = sum(r.found for r in alignment.frames)
    registered = sum(1 for r in alignment.frames if r.warp is not None)
    descriptions = [
        tr("{count} frames decoded by FFmpeg, exact to the frame; {scale}.").format(
            count=count, scale=tr("subject search at full resolution") if alignment.track_scale >= 1 else
            tr("subject search at {percent:.0f} % of the resolution").format(percent=alignment.track_scale * 100)),
        tr("Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
           "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
           "resolution around it.").format(found=found, count=count),
        tr("Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
           "2008), model: {model}, on smoothed images."
           ).format(model=tr(MOTION_LABELS[params.motion])),
        tr("ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
           "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.").format(
            registered=registered, quality=params.min_quality, keep=params.keep, used=used),
        tr("{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
           "quality{sharp}{equal}.").format(
            method=tr(METHOD_LABELS[params.method]), scale=par["scale"],
            sharp=tr(" and sharpness") if params.weight_sharpness else "",
            equal=tr(", brightness equalized to the reference") if params.equalize else ""),
        tr("{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, "
           "not detail). Noise reduction: {denoise}. Deconvolution: {deconv}.").format(
            levels=tr("Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every "
                      "channel").format(black=result.levels[0], white=result.levels[1])
            if params.levels else tr("No auto levels"),
            denoise=tr(DENOISE_LABELS[params.denoise]) + (tr(" (bilateral filter)") if params.denoise != "off" else ""),
            deconv=tr("Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation "
                      "regularization {reg} (λ = {lam})").format(
                sigma=result.psf_sigma, iterations=params.iterations,
                reg=tr(REGULARIZATION_LABELS[params.regularization]),
                lam=f"{REGULARIZATION.get(params.regularization, 0.0):g}")
            if params.iterations > 0 else tr("not applied")),
        tr("Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.").format(
            clahe=tr(LOCAL_CONTRAST_LABELS[params.local_contrast]).lower() + (
                tr(" (CLAHE, clip limit {clip:g})").format(clip=LOCAL_CONTRAST[params.local_contrast])
                if params.local_contrast != "off" else ""),
            gray=tr("grayscale") if params.grayscale else tr("color"),
            width=res["width"], height=res["height"]),
    ]
    out.append(Section(tr("Steps"), "steps",
                       [(tr(STEPS[i]), result.timings.get(i, 0.0), text) for i, text in enumerate(descriptions)],
                       extra=[str(note) for note in result.notes]))

    noise = res["noise_sigma_0_255"]
    out.append(Section(tr("Result"), "kv", [
        (tr("Frames used"), tr("{used} of {count}").format(used=used, count=count)),
        (tr("Estimated noise σ"), tr("Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused "
                                     "{fused:.2f} → final {final:.2f}. Deconvolution raises fine detail and noise "
                                     "together, so the last value is not a noise measure alone.").format(
            ref=noise["reference"], fused=noise["fused"], final=noise["final"])),
        (tr("Samples per output pixel"), f"{res['samples_per_output_pixel']:.2f}"),
        (tr("Sub-pixel phases covered (4 × 4 grid)"), f"{res['subpixel_phases_covered'] * 100:.0f} %"),
    ]))

    rows = []
    for row in data["frames"]:
        note = tr(row["excluded_because"]) if row["excluded_because"] else ""
        if row["frame"] == request.ref:
            note = (note + "  " if note else "") + tr("(reference)")
        rows.append([
            f"f{row['frame']}", format_time(row["time_s"], hours=hours),
            _fmt(row["tracking_score"], 3), _fmt(row["ecc_coarse"], 4), _fmt(row["ecc_fine"], 4),
            _fmt(row["shift_x_px"], 3), _fmt(row["shift_y_px"], 3), _fmt(row["sharpness"], 3),
            _fmt(row["weight"], 3) if row["used"] else "",
            tr("yes") if row["used"] else tr("no"),
            MODEL_SHORT.get(row["motion_model"] or "", "—"),
            note,
        ])
    out.append(Section(tr("Frames"), "table", rows,
                       head=(tr("frame"), tr("time"), tr("search"), "ECC 1", "ECC 2", "dx", "dy", tr("sharp."),
                             tr("weight"), tr("used"), tr("model"), tr("note")),
                       widths=(7, 10, 7, 7, 7, 8, 8, 7, 7, 5, 8, 24),
                       aligns=("R", "R", "R", "R", "R", "R", "R", "R", "R", "C", "L", "L")))

    files = [(item["name"], item["sha256"]) for item in data["output"]["files"].values()]
    extra = []
    if data["output"]["aligned_frames"]:
        extra.append(tr("aligned/: {count} aligned frames").format(count=len(data["output"]["aligned_frames"])))
    extra.append("report.json, report.txt, report.pdf")
    out.append(Section(tr("Files"), "files", files, extra=extra, mono=True))

    out.append(Section(tr("Note"), "paragraphs", [
        tr("The result is an enhancement of the frames listed above: it combines information that is present "
           "in them and does not add details. Fine details at the limit of the resolution, and characters that "
           "look alike, must be checked against the source frames before drawing conclusions."),
        tr("Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.").format(
            app=APP_NAME, version=__version__, python=data["software"]["python"],
            opencv=data["software"]["opencv"], numpy=data["software"]["numpy"]),
    ]))

    return Document(
        title=tr("{app} {version} — multi-frame fusion report").format(app=APP_NAME, version=__version__),
        credits=CREDITS, created=tr("Created: {when}").format(when=f"{when:%Y-%m-%d %H:%M:%S}"),
        sections=out)


# ------------------------------------------------------------------ testo

def _text(document: Document) -> str:
    lines: list[str] = [document.title, document.credits, document.created]
    add = lines.append
    for section in document.sections:
        add("")
        add(upper(section.title))
        add("-" * len(section.title))
        if section.kind == "kv":
            width = max(len(label) for label, _v in section.rows)
            for label, value in section.rows:
                add(f"  {label.ljust(width)}  {value}")
        elif section.kind == "steps":
            for number, (name, seconds, description) in enumerate(section.rows, start=1):
                add(f"  {number}. {name}  ({seconds:.2f} s)")
                add(f"     {description}")
            for note in section.extra:
                add(f"  · {note}")
        elif section.kind == "table":
            add("  " + "  ".join(f"{cell:>9}" for cell in section.head[:-1]))
            for cells in section.rows:
                line = "  " + "  ".join(f"{cell:>9}" for cell in cells[:-1])
                if cells[-1]:
                    line += "  " + cells[-1]
                add(line)
        elif section.kind == "files":
            for name, digest in section.rows:
                add(f"  {name}")
                add(f"     SHA-256 {digest}")
            for line in section.extra:
                add(f"  {line}")
        else:
            for text in section.rows:
                add(f"  {text}")
    return "\n".join(lines) + "\n"


MODEL_SHORT = {"translation": "transl.", "euclidean": "eucl.", "affine": "affine", "homography": "homogr."}


def _fmt(value, digits: int) -> str:
    return "—" if value is None else f"{value:.{digits}f}"
