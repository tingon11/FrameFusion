# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Pipeline di fusione multi-frame (super-risoluzione da piu' fotogrammi).

Un dettaglio piccolo (una targa, un volto, una scritta) ripreso in piu'
fotogrammi cade ogni volta in una posizione leggermente diversa rispetto alla
griglia dei pixel: ogni fotogramma ne porta un campionamento diverso, con
rumore indipendente. Allineandoli con precisione sub-pixel e fondendoli su una
griglia piu' fine si riduce il rumore e si recupera parte del dettaglio.
Nulla viene inventato: il risultato contiene solo cio' che i fotogrammi
sostengono, e ogni passaggio e ogni parametro finisce nel rapporto.

I sette passaggi:

1. Estrazione - l'intervallo scelto viene decodificato (una passata ridotta in
   grigio per la ricerca del soggetto, una a piena risoluzione che ritaglia
   solo il suo intorno).
2. Rilevamento - il soggetto, indicato da un riquadro sul fotogramma di
   riferimento, viene cercato in ogni fotogramma per correlazione normalizzata,
   a partire dal riferimento in avanti e all'indietro.
3. Allineamento locale - per ogni fotogramma si stima con l'algoritmo ECC
   (Evangelidis & Psarakis, 2008) la trasformazione (traslazione, rotazione,
   affine o prospettica) che lo porta sul riferimento, prima su immagini ridotte.
4. Registrazione sub-pixel - la stessa stima viene raffinata a piena
   risoluzione; poi si scelgono i fotogrammi piu' utili: allineamento riuscito
   e affidabile, maggiore nitidezza.
5. Fusione - i fotogrammi scelti vengono ricampionati sulla griglia ingrandita
   del riferimento e combinati in modo robusto: media pesata con scarto dei
   valori anomali (predefinita), mediana, oppure somma con spostamento dei
   singoli campioni con convoluzione normalizzata.
6. Deconvoluzione e riduzione del rumore - sulla sola luminanza (il colore,
   che nel video compresso e' a meta' risoluzione e porta solo rumore, viene
   smussato): filtro bilaterale facoltativo, poi Richardson-Lucy con un nucleo
   gaussiano di ampiezza nota, poche iterazioni e regolarizzazione a
   variazione totale (Dey et al., 2006), che frena l'amplificazione del rumore.
   I livelli automatici (nero e bianco ai percentili della luminanza) si
   applicano alla fusione prima del restauro.
7. Fotogramma unico - presentazione (contrasto locale, scala di grigi, tutto
   documentato), immagine finale, «ghost» dei fotogrammi usati e riferimento
   ingrandito per il confronto, dati per il rapporto.

I passaggi 1-4 dipendono solo da video, intervallo, riferimento, riquadro e
modello di moto: il loro esito (Alignment) si conserva, e cambiando i soli
parametri di fusione e restauro si rifanno solo i passaggi 5-7.
"""

from __future__ import annotations

import math
import threading
import time
from dataclasses import dataclass, field
from typing import Callable

import cv2
import numpy as np

from . import ffmpeg
from .ffmpeg import Cancelled, VideoInfo
from .i18n import N_, tr

# nomi dei sette passaggi, nell'ordine (tradotti al momento dell'uso)
STEPS = (
    N_("Frame extraction"),
    N_("Subject detection"),
    N_("Local alignment"),
    N_("Sub-pixel registration"),
    N_("Multi-frame fusion"),
    N_("Deconvolution and denoising"),
    N_("Single frame"),
)

MOTIONS = {
    "translation": cv2.MOTION_TRANSLATION,
    "euclidean": cv2.MOTION_EUCLIDEAN,
    "affine": cv2.MOTION_AFFINE,
    "homography": cv2.MOTION_HOMOGRAPHY,
}
METHODS = ("robust-mean", "shift-and-add", "median")
DENOISE = {"off": 0.0, "light": 1.0, "medium": 2.0, "strong": 3.0}
REGULARIZATION = {"off": 0.0, "light": 0.002, "medium": 0.005, "strong": 0.01}   # lambda della TV
LOCAL_CONTRAST = {"off": 0.0, "light": 1.5, "medium": 2.5, "strong": 4.0}       # clip limit di CLAHE
LEVELS_PERCENTILES = (0.5, 99.5)       # livelli automatici: questi percentili della luminanza vanno a 0 e 1
SHARP_POWER = 4                        # peso per nitidezza = (nitidezza / massima) ** SHARP_POWER
# modello di moto di ripiego quando ECC non converge con quello scelto
FALLBACK = {"homography": "affine", "affine": "euclidean", "euclidean": "translation", "translation": None}

MAX_FRAMES = 301                    # fotogrammi analizzati al massimo: il riferimento e 150 per parte
TRACK_BUDGET = 512 * 1024 ** 2      # memoria per le immagini di ricerca (passata 1)
PATCH_BUDGET = 1024 * 1024 ** 2     # memoria per i ritagli a piena risoluzione (passata 2)
STACK_BUDGET = 384 * 1024 ** 2      # memoria per la pila di fotogrammi della fusione, a strisce
MAX_OUTPUT_PIXELS = 24_000_000      # pixel dell'immagine ingrandita
MIN_ROI = 12                        # lato minimo del riquadro, in pixel
SEARCH = 1.0                        # raggio di ricerca, in lati del riquadro
CLIP_KAPPA = 2.5                    # soglia degli scarti (in deviazioni robuste)
KERNEL_MIN = 0.45                   # nucleo minimo della convoluzione normalizzata (pixel della griglia fine)


class PipelineError(RuntimeError):
    """Dati insufficienti o parametri non validi: il messaggio e' per l'utente."""


# ------------------------------------------------------------------ parametri

@dataclass
class Params:
    motion: str = "homography"
    keep: int = 75              # percentuale dei fotogrammi piu' nitidi da tenere
    min_quality: float = 0.80   # coefficiente ECC minimo
    track_min: float = 0.50     # correlazione minima per dire "soggetto trovato"
    scale: int = 2              # fattore d'ingrandimento
    method: str = "robust-mean"
    weight_sharpness: bool = True
    equalize: bool = True
    denoise: str = "off"
    iterations: int = 20        # Richardson-Lucy; 0 = nessuna deconvoluzione
    psf_sigma: float = 0.0      # in pixel della griglia ingrandita; 0 = automatico
    regularization: str = "medium"  # variazione totale nella deconvoluzione
    levels: bool = True         # livelli automatici (presentazione)
    local_contrast: str = "off"     # CLAHE sulla luminanza (presentazione)
    grayscale: bool = False     # uscita in scala di grigi (presentazione)


@dataclass
class Request:
    """Cosa fondere: video, intervallo, riferimento e riquadro del soggetto (pixel del video)."""

    info: VideoInfo
    first: int
    last: int
    ref: int
    roi: tuple[int, int, int, int]   # x, y, larghezza, altezza sul fotogramma di riferimento

    def key(self, params: Params) -> tuple:
        """Cio' da cui dipendono i passaggi 1-4: se non cambia, l'allineamento si riusa."""
        return (str(self.info.path), self.first, self.last, self.ref, self.roi, params.motion, params.track_min)


@dataclass
class FrameRecord:
    """Un fotogramma dell'intervallo e cio' che la pipeline ha misurato su di lui."""

    index: int                    # numero del fotogramma nel video
    time: float                   # secondi
    track_score: float = float("nan")
    found: bool = False
    position: tuple[float, float] = (0.0, 0.0)   # angolo del soggetto trovato (pixel del video)
    origin: tuple[int, int] = (0, 0)              # angolo del ritaglio nel fotogramma
    patch: np.ndarray | None = None               # ritaglio a piena risoluzione (tipo nativo)
    warp: np.ndarray | None = None                # 3x3: coordinate del riquadro -> coordinate del ritaglio
    cc_coarse: float = float("nan")
    cc_fine: float = float("nan")
    shift: tuple[float, float] = (float("nan"), float("nan"))  # spostamento rispetto al riferimento
    sharpness: float = float("nan")
    gain: tuple[float, float] = (1.0, 0.0)        # luminosita': valore * a + b porta al riferimento
    model: str = ""                               # modello di moto con cui ECC e' riuscito
    used: bool = False
    reason: str = ""                              # perche' e' stato scartato (testo inglese, chiave di tr)
    weight: float = 0.0


@dataclass
class Alignment:
    """Esito dei passaggi 1-4, riusato finche' non cambiano video, intervallo, riquadro o moto."""

    request: Request
    motion: str
    frames: list[FrameRecord]
    max_value: float              # 255 o 65535: valore massimo dei ritagli
    track_scale: float
    stride: int                   # 1 = tutti i fotogrammi dell'intervallo
    timings: dict[int, float] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    @property
    def reference(self) -> FrameRecord:
        return next(f for f in self.frames if f.index == self.request.ref)


@dataclass
class Result:
    alignment: Alignment
    params: Params
    final: np.ndarray             # alto x largo x 3, float32 in [0, 1]
    fused: np.ndarray             # prima di riduzione del rumore e deconvoluzione
    ghost: np.ndarray             # sovrapposizione dei fotogrammi usati, alla posizione trovata, stessa griglia
    reference: np.ndarray         # riquadro del riferimento ingrandito (bicubica), stessa griglia
    reference_native: np.ndarray  # riquadro del riferimento alla risoluzione del video
    used: list[int]
    psf_sigma: float
    kernel_sigma: float
    noise: dict[str, float]       # deviazione del rumore stimata (scala 0-255)
    coverage: float               # campioni per pixel della griglia ingrandita
    subpixel: float               # frazione delle 16 fasi sub-pixel coperte
    levels: tuple[float, float]   # luminanza portata a 0 e 1 dai livelli automatici (0..1); (0, 1) se spenti
    timings: dict[int, float]
    notes: list[str] = field(default_factory=list)


Progress = Callable[[int, float, str], None]   # passaggio (0-6), avanzamento 0..1, messaggio


def _check(cancel: threading.Event | None) -> None:
    if cancel is not None and cancel.is_set():
        raise Cancelled()


# ------------------------------------------------------------- passaggi 1-4

def align(request: Request, params: Params, progress: Progress,
          cancel: threading.Event | None = None) -> Alignment:
    """Estrazione, rilevamento, allineamento locale e registrazione sub-pixel."""
    info = request.info
    motion = params.motion
    x, y, w, h = request.roi
    if w < MIN_ROI or h < MIN_ROI:
        raise PipelineError(tr("The subject area is too small: draw at least {size} × {size} pixels.").format(
            size=MIN_ROI))
    if not request.first <= request.ref <= request.last:
        raise PipelineError(tr("The reference frame must be inside the selected range."))
    first = request.first
    count = request.last - request.first + 1
    notes: list[str] = []
    if count > MAX_FRAMES:
        raise PipelineError(tr("The range has {count} frames: select at most {limit} around the "
                               "reference.").format(count=count, limit=MAX_FRAMES))
    timings: dict[int, float] = {}

    # ---- 1. estrazione: passata ridotta in grigio, per la ricerca del soggetto
    started = time.perf_counter()
    scale_t = min(1.0, math.sqrt(TRACK_BUDGET / max(1, count * info.width * info.height)))
    if scale_t < 1.0:
        size = (max(16, int(round(info.width * scale_t))), max(16, int(round(info.height * scale_t))))
        scale_t = size[0] / info.width
    else:
        size = None
    grays: list[np.ndarray] = []
    for number, frame in ffmpeg.stream_frames(info, first, count, "gray", size=size):
        _check(cancel)
        grays.append(frame[:, :, 0])
        progress(0, len(grays) / count, tr("{done} / {total} frames decoded").format(done=len(grays), total=count))
    if request.ref - first >= len(grays):
        raise PipelineError(tr("The video ended before the reference frame."))
    count = len(grays)
    timings[0] = time.perf_counter() - started
    progress(0, 1.0, tr("{count} frames decoded").format(count=count))
    if scale_t < 1.0:
        notes.append(tr("Subject search on frames reduced to {percent:.0f} % (memory limit).").format(
            percent=scale_t * 100))

    # ---- 2. rilevamento: il soggetto in ogni fotogramma
    started = time.perf_counter()
    records = [FrameRecord(index=first + i, time=(first + i) / info.fps) for i in range(count)]
    _track(grays, request, scale_t, params.track_min, records, progress, cancel)
    del grays

    # ritagli a piena risoluzione attorno al soggetto trovato (passata 2)
    margin = int(round(0.25 * max(w, h))) + 12
    patch_w, patch_h = min(info.width, w + 2 * margin), min(info.height, h + 2 * margin)
    deep = info.bit_depth > 8
    bytes_per = patch_w * patch_h * 3 * (2 if deep else 1)
    found = [r for r in records if r.found]
    stride = max(1, math.ceil(len(found) * bytes_per / PATCH_BUDGET))
    if stride > 1:
        ref_pos = request.ref - first
        for i, record in enumerate(records):
            if record.found and (i - ref_pos) % stride:
                record.found = False
                record.reason = N_("not sampled (memory limit)")
        notes.append(tr("One frame every {stride} kept (memory limit for large areas).").format(stride=stride))
    wanted = {r.index: r for r in records if r.found}
    for number, frame in ffmpeg.stream_frames(info, first, count, "rgb48le" if deep else "rgb24"):
        _check(cancel)
        record = wanted.get(number)
        if record is not None:
            px, py = record.position
            ox = int(round(px)) - margin
            oy = int(round(py)) - margin
            ox = max(0, min(info.width - patch_w, ox))
            oy = max(0, min(info.height - patch_h, oy))
            record.origin = (ox, oy)
            record.patch = frame[oy:oy + patch_h, ox:ox + patch_w].copy()
        progress(1, 0.5 + 0.5 * (number - first + 1) / count,
                 tr("{done} / {total} frames read at full resolution").format(done=number - first + 1, total=count))
    for record in records:
        if record.found and record.patch is None:
            record.found = False
            record.reason = N_("frame not decoded")
    ref_record = next(r for r in records if r.index == request.ref)
    if ref_record.patch is None:
        raise PipelineError(tr("The reference frame could not be read."))
    timings[1] = time.perf_counter() - started
    progress(1, 1.0, tr("subject found in {found} / {total} frames").format(
        found=sum(r.found for r in records), total=count))

    max_value = 65535.0 if deep else 255.0
    alignment = Alignment(request=request, motion=motion, frames=records, max_value=max_value,
                          track_scale=scale_t, stride=stride, timings=timings, notes=notes)

    # ---- 3 e 4. allineamento locale e registrazione sub-pixel (ECC)
    _register(alignment, progress, cancel)
    return alignment


def _track(grays: list[np.ndarray], request: Request, scale: float, track_min: float,
           records: list[FrameRecord], progress: Progress, cancel: threading.Event | None) -> None:
    """Cerca il soggetto fotogramma per fotogramma, dal riferimento verso i due estremi.

    Il modello cercato e' il soggetto trovato nel fotogramma precedente,
    mescolato con quello di prima: segue cambi lenti di scala e di luce senza
    perdere di vista l'originale. La posizione prevista tiene conto della
    velocita' del soggetto.
    """
    x, y, w, h = request.roi
    ref_i = request.ref - request.first
    gh, gw = grays[0].shape
    tw, th = max(6, int(round(w * scale))), max(6, int(round(h * scale)))
    rx = min(max(0, int(round(x * scale))), gw - tw)
    ry = min(max(0, int(round(y * scale))), gh - th)
    reference = grays[ref_i][ry:ry + th, rx:rx + tw].astype(np.float32)

    ref_record = records[ref_i]
    ref_record.found, ref_record.track_score, ref_record.position = True, 1.0, (float(x), float(y))
    total, done = len(records), 1
    radius = int(round(max(tw, th) * SEARCH)) + 6
    for direction in (1, -1):
        template = reference.copy()
        px, py = float(rx), float(ry)
        vx = vy = 0.0
        i = ref_i + direction
        while 0 <= i < total:
            _check(cancel)
            gray = grays[i]
            cx, cy = px + vx, py + vy
            x0 = int(max(0, min(gw - tw, round(cx) - radius)))
            y0 = int(max(0, min(gh - th, round(cy) - radius)))
            x1 = int(max(x0, min(gw - tw, round(cx) + radius)))
            y1 = int(max(y0, min(gh - th, round(cy) + radius)))
            window = gray[y0:y1 + th, x0:x1 + tw].astype(np.float32)
            score, loc = 0.0, (0, 0)
            if window.shape[0] >= th and window.shape[1] >= tw and float(template.std()) > 1e-3:
                result = cv2.matchTemplate(window, template, cv2.TM_CCOEFF_NORMED)
                result = np.nan_to_num(result, nan=-1.0, posinf=-1.0, neginf=-1.0)
                _lo, score, _lo_loc, loc = cv2.minMaxLoc(result)
            record = records[i]
            record.track_score = float(score)
            if score >= track_min:
                nx, ny = float(x0 + loc[0]), float(y0 + loc[1])
                vx, vy = 0.5 * vx + 0.5 * (nx - px), 0.5 * vy + 0.5 * (ny - py)
                px, py = nx, ny
                current = gray[int(py):int(py) + th, int(px):int(px) + tw].astype(np.float32)
                if current.shape == template.shape:
                    template = 0.6 * current + 0.4 * template
                record.found = True
                record.position = (px / scale, py / scale)
            else:
                # perso: si prosegue sulla posizione prevista, il modello resta quello
                px, py = cx, cy
                record.found = False
                record.reason = N_("subject not found")
            done += 1
            progress(1, 0.5 * done / total, tr("searching the subject: {done} / {total}").format(
                done=done, total=total))
            i += direction


def _gray(image: np.ndarray, max_value: float) -> np.ndarray:
    """Luminanza in virgola mobile, 0..1."""
    rgb = image.astype(np.float32) / max_value
    return rgb[:, :, 0] * 0.299 + rgb[:, :, 1] * 0.587 + rgb[:, :, 2] * 0.114


def _translation(dx: float, dy: float) -> np.ndarray:
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]], dtype=np.float64)


def _scale_matrix(k: float) -> np.ndarray:
    return np.array([[k, 0, 0], [0, k, 0], [0, 0, 1]], dtype=np.float64)


def _ecc(template: np.ndarray, image: np.ndarray, warp: np.ndarray, motion: str,
         iterations: int, eps: float, blur: int) -> tuple[np.ndarray, float]:
    """Una stima ECC; `warp` 3x3 porta le coordinate del modello in quelle dell'immagine."""
    mode = MOTIONS[motion]
    start = warp.astype(np.float32) if mode == cv2.MOTION_HOMOGRAPHY else warp[:2].astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, iterations, eps)
    cc, out = cv2.findTransformECC(template, image, start, mode, criteria, None, blur)
    full = np.eye(3, dtype=np.float64)
    if mode == cv2.MOTION_HOMOGRAPHY:
        full[:, :] = out
    else:
        full[:2, :] = out
    return full, float(cc)


def _register(alignment: Alignment, progress: Progress, cancel: threading.Event | None) -> None:
    """Passaggi 3 e 4: ECC grossolano (ridotto e sfocato), poi fine a piena risoluzione."""
    request, motion = alignment.request, alignment.motion
    x, y, w, h = request.roi
    ref = alignment.reference
    rox, roy = ref.origin
    template = _gray(ref.patch, alignment.max_value)[y - roy:y - roy + h, x - rox:x - rox + w].copy()
    ref.warp = _translation(x - rox, y - roy)
    ref.cc_coarse = ref.cc_fine = 1.0
    ref.shift = (0.0, 0.0)
    ref.sharpness = _sharpness(template)

    # piramide: il passo grossolano lavora a meta' risoluzione se il riquadro e' grande abbastanza
    half = min(w, h) >= 48
    k = 0.5 if half else 1.0
    small_template = cv2.resize(template, None, fx=k, fy=k, interpolation=cv2.INTER_AREA) if half else template
    candidates = [r for r in alignment.frames if r.found and r is not ref]

    started = time.perf_counter()
    for n, record in enumerate(candidates, start=1):
        _check(cancel)
        gray = _gray(record.patch, alignment.max_value)
        ox, oy = record.origin
        px, py = record.position
        start = _translation(px - ox, py - oy)
        image = cv2.resize(gray, None, fx=k, fy=k, interpolation=cv2.INTER_AREA) if half else gray
        s = _scale_matrix(k)
        warp0 = s @ start @ np.linalg.inv(s)
        # prima solo la traslazione, poi il modello scelto; se non converge, uno piu' semplice
        try:
            warp0, cc0 = _ecc(small_template, image, warp0, "translation", 60, 1e-4, 5)
        except cv2.error:
            record.warp = None
            record.reason = N_("alignment failed")
            continue
        model = motion
        while model is not None:
            try:
                if model == "translation":
                    warp, cc = warp0, cc0
                else:
                    warp, cc = _ecc(small_template, image, warp0, model, 100, 1e-5, 5)
                break
            except cv2.error:
                model = FALLBACK[model]
        if model is None:
            record.warp = None
            record.reason = N_("alignment failed")
            continue
        record.model = model
        record.warp = np.linalg.inv(s) @ warp @ s
        record.cc_coarse = cc
        progress(2, n / max(1, len(candidates)), tr("{done} / {total} frames aligned").format(
            done=n, total=len(candidates)))
    alignment.timings[2] = time.perf_counter() - started
    progress(2, 1.0, tr("motion model: {model}").format(model=tr(MOTION_LABELS[motion])))

    started = time.perf_counter()
    for n, record in enumerate(candidates, start=1):
        _check(cancel)
        if record.warp is None:
            continue
        gray = _gray(record.patch, alignment.max_value)
        model = record.model
        while model is not None:
            try:
                record.warp, record.cc_fine = _ecc(template, gray, record.warp, model, 200, 1e-7, 3)
                break
            except cv2.error:
                model = FALLBACK[model]
        if model is None:
            record.warp = None
            record.reason = N_("sub-pixel registration failed")
            continue
        record.model = model
        ox, oy = record.origin
        cx, cy = _apply(record.warp, (w - 1) / 2, (h - 1) / 2)
        record.shift = (cx + ox - (x + (w - 1) / 2), cy + oy - (y + (h - 1) / 2))
        aligned = cv2.warpPerspective(gray, record.warp, (w, h), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP,
                                      borderMode=cv2.BORDER_REFLECT)
        record.sharpness = _sharpness(aligned)
        # luminosita' e contrasto riportati a quelli del riferimento (esposizione automatica)
        std = float(aligned.std())
        a = float(template.std()) / std if std > 1e-6 else 1.0
        a = min(4.0, max(0.25, a))
        record.gain = (a, float(template.mean()) - a * float(aligned.mean()))
        progress(3, n / max(1, len(candidates)), tr("{done} / {total} frames registered").format(
            done=n, total=len(candidates)))
    alignment.timings[3] = time.perf_counter() - started
    registered = sum(1 for r in alignment.frames if r.warp is not None)
    simpler = sum(1 for r in candidates if r.warp is not None and r.model != motion)
    if simpler:
        alignment.notes.append(tr("{count} frames aligned with a simpler motion model, because the chosen one "
                                  "did not converge on them.").format(count=simpler))
    progress(3, 1.0, tr("{count} frames registered").format(count=registered))


def _apply(warp: np.ndarray, x: float, y: float) -> tuple[float, float]:
    vx, vy, vw = warp @ np.array([x, y, 1.0])
    return float(vx / vw), float(vy / vw)


def _sharpness(gray: np.ndarray) -> float:
    """Energia del laplaciano rispetto al contrasto: non dipende da luminosita' e contrasto."""
    lap = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    return float(lap.var() / (gray.var() + 1e-8))


# --------------------------------------------------------------- selezione

def select(alignment: Alignment, params: Params) -> list[FrameRecord]:
    """Sceglie i fotogrammi da fondere e ne calcola il peso; aggiorna used/reason/weight."""
    ref = alignment.reference
    good: list[FrameRecord] = []
    for record in alignment.frames:
        record.used, record.weight = False, 0.0
        if record is ref:
            continue
        if record.warp is None:
            if not record.reason:
                record.reason = N_("subject not found")
            continue
        if record.cc_fine < params.min_quality:
            record.reason = N_("low alignment quality")
            continue
        record.reason = ""
        good.append(record)
    good.sort(key=lambda r: r.sharpness, reverse=True)
    keep = max(0, math.ceil((len(good) + 1) * params.keep / 100) - 1)
    for record in good[keep:]:
        record.reason = N_("less sharp than the selected ones")
    chosen = [ref] + good[:keep]
    top = max(r.sharpness for r in chosen) or 1.0
    for record in chosen:
        record.used, record.reason = True, ""
        weight = record.cc_fine ** 2
        if params.weight_sharpness:
            weight *= max(0.02, (record.sharpness / top) ** SHARP_POWER)
        record.weight = float(weight)
    chosen.sort(key=lambda r: r.index)
    return chosen


# ------------------------------------------------------------- passaggi 5-7

def fuse(alignment: Alignment, params: Params, progress: Progress,
         cancel: threading.Event | None = None) -> Result:
    request = alignment.request
    x, y, w, h = request.roi
    notes = list(alignment.notes)
    s = int(params.scale)
    if w * h * s * s > MAX_OUTPUT_PIXELS:
        s_max = max(1, int(math.sqrt(MAX_OUTPUT_PIXELS / (w * h))))
        notes.append(tr("Scale reduced from ×{asked} to ×{used}: the area is too large.").format(
            asked=s, used=s_max))
        s = s_max
    chosen = select(alignment, params)
    if len(chosen) < 3:
        notes.append(tr("Only {count} usable frames: the result can be only slightly better than the "
                        "reference. Widen the range or lower the quality threshold.").format(count=len(chosen)))
    timings = dict(alignment.timings)
    W, H = w * s, h * s
    # coordinate della griglia ingrandita -> coordinate del riquadro (centri dei pixel)
    hr_to_roi = np.array([[1 / s, 0, 0.5 / s - 0.5], [0, 1 / s, 0.5 / s - 0.5], [0, 0, 1]], dtype=np.float64)
    weights = np.array([r.weight for r in chosen], dtype=np.float32)
    progress(4, 0.0, tr("{count} frames selected").format(count=len(chosen)))

    # ---- 5. fusione
    started = time.perf_counter()
    estimate = _robust_stack(alignment, chosen, weights, hr_to_roi, (W, H), params,
                             median=params.method == "median", progress=progress, cancel=cancel,
                             share=0.5 if params.method == "shift-and-add" else 1.0)
    kernel = 0.0
    coverage = len(chosen) / (s * s)
    if params.method == "shift-and-add":
        fused, kernel, coverage = _shift_and_add(alignment, chosen, weights, hr_to_roi, (W, H), params,
                                                 estimate, progress, cancel)
    else:
        fused = estimate
    timings[4] = time.perf_counter() - started
    progress(4, 1.0, tr("{count} frames fused on a ×{scale} grid").format(count=len(chosen), scale=s))

    # ---- 6. riduzione del rumore e deconvoluzione (sulla luminanza)
    started = time.perf_counter()
    ref = alignment.reference
    rox, roy = ref.origin
    native = ref.patch[y - roy:y - roy + h, x - rox:x - rox + w].astype(np.float32) / alignment.max_value
    reference = cv2.resize(native, (W, H), interpolation=cv2.INTER_CUBIC) if s > 1 else native.copy()
    reference = np.clip(reference, 0.0, 1.0)
    # tutte le stime sulla stessa strada: griglia fine riportata alla risoluzione del video
    noise = {"reference": _noise(cv2.resize(reference, (w, h), interpolation=cv2.INTER_AREA)),
             "fused": _noise(cv2.resize(fused, (w, h), interpolation=cv2.INTER_AREA))}
    psf = params.psf_sigma if params.psf_sigma > 0 else auto_psf(fused, s)
    # i livelli automatici vengono prima del restauro: con il nero a zero e il bianco a uno la
    # deconvoluzione lavora sul modello giusto e la regolarizzazione pesa quanto deve
    leveled, levels = _levels(np.clip(fused, 0.0, 1.0), params)
    restored = _restore(leveled, params, s, psf, progress, cancel)
    timings[5] = time.perf_counter() - started
    progress(5, 1.0, tr("PSF σ {sigma:.2f} px, {iterations} iterations").format(sigma=psf, iterations=params.iterations)
             if params.iterations > 0 else tr("no deconvolution"))

    # ---- 7. fotogramma unico: presentazione, ghost, dati
    started = time.perf_counter()
    final = _present(restored, params)
    ghost = _ghost(alignment, chosen, hr_to_roi, (W, H), params)
    noise["final"] = _noise(cv2.resize(final, (w, h), interpolation=cv2.INTER_AREA))
    phases = {(int(((r.shift[0] % 1) * 4)) % 4, int(((r.shift[1] % 1) * 4)) % 4) for r in chosen}
    timings[6] = time.perf_counter() - started
    result = Result(alignment=alignment, params=params, final=final, fused=np.clip(fused, 0, 1).astype(np.float32),
                    ghost=ghost, reference=reference.astype(np.float32), reference_native=np.clip(native, 0, 1),
                    used=[r.index for r in chosen], psf_sigma=float(psf), kernel_sigma=float(kernel),
                    noise=noise, coverage=float(coverage), subpixel=len(phases) / 16, levels=levels,
                    timings=timings, notes=notes)
    progress(6, 1.0, tr("{width} × {height} pixels").format(width=W, height=H))
    return result


def _luma(rgb: np.ndarray) -> np.ndarray:
    return rgb[:, :, 0] * 0.299 + rgb[:, :, 1] * 0.587 + rgb[:, :, 2] * 0.114


def _restore(fused: np.ndarray, params: Params, s: int, psf: float, progress: Progress,
             cancel: threading.Event | None) -> np.ndarray:
    """Passaggio 6: riduzione del rumore e deconvoluzione sulla luminanza; il colore viene solo smussato.

    Nel video compresso il colore e' a meta' risoluzione (4:2:0) e porta
    rumore, non dettaglio: deconvolverlo creerebbe frange colorate.
    """
    ycc = cv2.cvtColor(fused.astype(np.float32), cv2.COLOR_RGB2YCrCb)
    luma = np.ascontiguousarray(ycc[:, :, 0])
    chroma = cv2.GaussianBlur(ycc[:, :, 1:], (0, 0), max(0.8, 0.6 * s), borderType=cv2.BORDER_REFLECT)
    strength = DENOISE.get(params.denoise, 0.0)
    if strength > 0:
        sigma_n = max(1e-4, _noise(luma) / 255.0)
        luma = cv2.bilateralFilter(luma, d=-1, sigmaColor=float(strength * 2.0 * sigma_n),
                                   sigmaSpace=float(max(1.0, 0.75 * s)))
        progress(5, 0.3, tr("noise reduction ({level})").format(level=tr(DENOISE_LABELS[params.denoise])))
    if params.iterations > 0:
        luma = _richardson_lucy(luma, psf, params.iterations, REGULARIZATION.get(params.regularization, 0.0),
                                lambda n: progress(5, 0.3 + 0.7 * n / params.iterations,
                                                   tr("deconvolution: iteration {n} / {total}").format(
                                                       n=n, total=params.iterations)),
                                cancel)
    ycc = np.dstack([np.clip(luma, 0.0, 1.0), chroma]).astype(np.float32)
    return np.clip(cv2.cvtColor(ycc, cv2.COLOR_YCrCb2RGB), 0.0, 1.0)


def _levels(image: np.ndarray, params: Params) -> tuple[np.ndarray, tuple[float, float]]:
    """Livelli automatici: i percentili LEVELS_PERCENTILES della luminanza vanno a 0 e 1.

    La stessa retta sui tre canali: i colori non cambiano. Si applica alla
    fusione, prima del restauro.
    """
    if not params.levels:
        return image, (0.0, 1.0)
    lo, hi = (float(v) for v in np.percentile(_luma(image), LEVELS_PERCENTILES))
    if hi - lo <= 0.05:
        return image, (0.0, 1.0)
    return np.clip((image - lo) / (hi - lo), 0.0, 1.0).astype(np.float32), (lo, hi)


def _present(image: np.ndarray, params: Params) -> np.ndarray:
    """Passaggio 7: contrasto locale e scala di grigi; tutto nel rapporto."""
    out = image.astype(np.float32)
    clip = LOCAL_CONTRAST.get(params.local_contrast, 0.0)
    if clip > 0:
        ycc = cv2.cvtColor(out, cv2.COLOR_RGB2YCrCb)
        h, w = ycc.shape[:2]
        clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(max(2, w // 32), max(2, h // 32)))
        luma16 = clahe.apply(np.round(ycc[:, :, 0] * 65535.0).astype(np.uint16))
        ycc[:, :, 0] = luma16.astype(np.float32) / 65535.0
        out = np.clip(cv2.cvtColor(ycc, cv2.COLOR_YCrCb2RGB), 0.0, 1.0)
    if params.grayscale:
        out = np.repeat(_luma(out)[:, :, None], 3, axis=2)
    return np.ascontiguousarray(out, dtype=np.float32)


def _ghost(alignment: Alignment, chosen: list[FrameRecord], hr_to_roi: np.ndarray, size: tuple[int, int],
           params: Params) -> np.ndarray:
    """Sovrapposizione a pari peso dei fotogrammi usati, ciascuno alla posizione trovata dalla ricerca
    (al pixel intero, prima della registrazione): mostra cosa entra nella fusione e quanto si muove."""
    W, H = size
    total = np.zeros((H, W, 3), np.float32)
    for record in chosen:
        ox, oy = record.origin
        px, py = record.position
        shift = _translation(round(px) - ox, round(py) - oy)
        total += cv2.warpPerspective(_prepared(alignment, record, params), shift @ hr_to_roi, (W, H),
                                     flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REFLECT)
    return np.clip(total / max(1, len(chosen)), 0.0, 1.0)


def auto_psf(fused: np.ndarray, scale: int) -> float:
    """Ampiezza del nucleo di deconvoluzione stimata dai bordi dell'immagine fusa (pixel della griglia fine).

    Un gradino sfocato da una gaussiana di deviazione s ha pendenza massima
    A / (s * sqrt(2 pi)), con A l'ampiezza del gradino: sui bordi piu' netti
    si misura l'ampiezza locale (massimo meno minimo in un intorno) e la
    pendenza, e la mediana dei rapporti da' s. E' la sfocatura complessiva
    (ottica, sensore, codec, ricampionamento), quella che la deconvoluzione
    deve togliere. Il valore resta tra 0.5 e 1.6 pixel del video.
    """
    luma = _luma(fused).astype(np.float32)
    gy, gx = np.gradient(luma)
    slope = np.sqrt(gx * gx + gy * gy)
    radius = int(math.ceil(2.5 * scale))
    window = np.ones((2 * radius + 1, 2 * radius + 1), np.uint8)
    amplitude = cv2.dilate(luma, window) - cv2.erode(luma, window)
    strong = slope >= np.percentile(slope, 97)
    strong &= amplitude >= max(0.05, float(np.percentile(amplitude, 50)))
    low, high = 0.5 * scale, 1.6 * scale
    if strong.sum() < 20:
        return float(math.sqrt(low * high))
    sigma = amplitude[strong] / (slope[strong] * math.sqrt(2 * math.pi))
    return float(min(high, max(low, float(np.median(sigma)))))


def _prepared(alignment: Alignment, record: FrameRecord, params: Params) -> np.ndarray:
    patch = record.patch.astype(np.float32) / alignment.max_value
    if params.equalize and record is not alignment.reference:
        a, b = record.gain
        patch = patch * a + b
    return patch


def _robust_stack(alignment: Alignment, chosen: list[FrameRecord], weights: np.ndarray, hr_to_roi: np.ndarray,
                  size: tuple[int, int], params: Params, median: bool, progress: Progress,
                  cancel: threading.Event | None, share: float) -> np.ndarray:
    """Ogni fotogramma ricampionato sulla griglia ingrandita, poi mediana o media con scarto degli anomali.

    Si lavora a strisce orizzontali per non tenere in memoria l'intera pila.
    """
    W, H = size
    n = len(chosen)
    band = max(8, min(H, STACK_BUDGET // max(1, n * W * 3 * 4 * 5)))
    out = np.zeros((H, W, 3), np.float32)
    patches = [_prepared(alignment, r, params) for r in chosen]
    w = weights.reshape(n, 1, 1, 1)
    for top in range(0, H, band):
        _check(cancel)
        rows = min(band, H - top)
        shift = _translation(0, top)
        stack = np.empty((n, rows, W, 3), np.float32)
        valid = np.empty((n, rows, W, 1), np.float32)
        for i, (record, patch) in enumerate(zip(chosen, patches)):
            m = record.warp @ hr_to_roi @ shift
            stack[i] = cv2.warpPerspective(patch, m, (W, rows), flags=cv2.INTER_LANCZOS4 | cv2.WARP_INVERSE_MAP,
                                           borderMode=cv2.BORDER_REFLECT)
            ones = np.ones(patch.shape[:2], np.float32)
            valid[i, :, :, 0] = cv2.warpPerspective(ones, m, (W, rows), flags=cv2.INTER_NEAREST | cv2.WARP_INVERSE_MAP,
                                                    borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        if not median and n < 3:
            out[top:top + rows] = _weighted_mean(stack, valid * w)
            continue
        # i campioni fuori dal ritaglio non contano (succede solo vicino ai bordi del video)
        complete = bool(valid.all())
        masked = stack if complete else np.where(valid > 0, stack, np.nan)
        med = np.median(masked, axis=0) if complete else np.nan_to_num(np.nanmedian(masked, axis=0), nan=0.0)
        if median:
            out[top:top + rows] = med
        else:
            deviation = np.abs(masked - med)
            spread = 1.4826 * (np.median(deviation, axis=0) if complete else np.nanmedian(deviation, axis=0))
            spread = np.nan_to_num(spread, nan=0.0)
            del deviation
            # soglia: mai sotto il rumore tipico, per non scartare per caso i campioni buoni
            floor = max(1e-3, float(np.median(spread)))
            keep = (np.abs(stack - med) <= CLIP_KAPPA * np.maximum(spread, floor)) & (valid > 0)
            out[top:top + rows] = _weighted_mean(stack, keep.astype(np.float32) * w, fallback=med)
        progress(4, share * min(1.0, (top + rows) / H), tr("resampling on the fine grid: {percent:.0f} %").format(
            percent=100 * share * min(1.0, (top + rows) / H)))
    return out


def _weighted_mean(stack: np.ndarray, weights: np.ndarray, fallback: np.ndarray | None = None) -> np.ndarray:
    total = weights.sum(axis=0)
    mean = (stack * weights).sum(axis=0) / np.maximum(total, 1e-12)
    if fallback is not None:
        mean = np.where(total > 0, mean, np.nan_to_num(fallback, nan=0.0))
    return mean


def _shift_and_add(alignment: Alignment, chosen: list[FrameRecord], weights: np.ndarray, hr_to_roi: np.ndarray,
                   size: tuple[int, int], params: Params, estimate: np.ndarray, progress: Progress,
                   cancel: threading.Event | None) -> tuple[np.ndarray, float, float]:
    """Somma con spostamento e convoluzione normalizzata (Knutsson & Westin, 1993).

    Ogni pixel di ogni fotogramma e' un campione nella sua posizione esatta,
    sub-pixel, sulla griglia ingrandita: si distribuisce (bilineare) sui
    quattro nodi vicini, con il peso del fotogramma e un peso robusto che
    attenua i campioni lontani dalla stima di riferimento (riflessi, occlusioni,
    errori di allineamento). Numeratore e denominatore vengono poi smussati
    con lo stesso nucleo gaussiano e divisi: dove i campioni mancano decide la
    stima ricampionata.
    """
    W, H = size
    s = 1 / hr_to_roi[0, 0]
    roi_to_hr = np.linalg.inv(hr_to_roi)
    num = np.zeros((H * W, 3), np.float64)
    den = np.zeros(H * W, np.float64)
    luma_est = (estimate[:, :, 0] * 0.299 + estimate[:, :, 1] * 0.587 + estimate[:, :, 2] * 0.114).astype(np.float32)

    def samples(record: FrameRecord):
        """Posizione sulla griglia ingrandita, colore e scarto dalla stima di ogni pixel del ritaglio."""
        patch = _prepared(alignment, record, params)
        ph, pw = patch.shape[:2]
        ys, xs = np.mgrid[0:ph, 0:pw]
        pts = np.stack([xs.ravel(), ys.ravel(), np.ones(xs.size)]).astype(np.float64)
        hr = roi_to_hr @ np.linalg.inv(record.warp) @ pts
        u, v = hr[0] / hr[2], hr[1] / hr[2]
        inside = (u > -1) & (u < W) & (v > -1) & (v < H)
        u, v = u[inside], v[inside]
        values = patch.reshape(-1, 3)[inside].astype(np.float64)
        at = cv2.remap(luma_est, u.astype(np.float32).reshape(-1, 1), v.astype(np.float32).reshape(-1, 1),
                       cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT).ravel()
        luma = values[:, 0] * 0.299 + values[:, 1] * 0.587 + values[:, 2] * 0.114
        return u, v, values, np.abs(luma - at)

    # rumore tipico dei campioni rispetto alla stima (su un sottoinsieme): soglia del peso robusto
    rng = np.random.default_rng(0)
    residuals = []
    for record in chosen[:12]:
        resid = samples(record)[3]
        residuals.append(resid[rng.integers(0, resid.size, min(resid.size, 20000))] if resid.size else resid)
    sigma = 1.4826 * float(np.median(np.concatenate(residuals))) if residuals else 0.0
    threshold = max(1e-3, CLIP_KAPPA * sigma)

    count = 0
    total = len(chosen)
    for n, record in enumerate(chosen, start=1):
        _check(cancel)
        u, v, values, resid = samples(record)
        count += u.size
        robust = np.minimum(1.0, threshold / np.maximum(resid, 1e-9))   # peso di Huber
        base = float(weights[n - 1]) * robust
        u0, v0 = np.floor(u).astype(np.int64), np.floor(v).astype(np.int64)
        fu, fv = u - u0, v - v0
        for du, dv, wk in ((0, 0, (1 - fu) * (1 - fv)), (1, 0, fu * (1 - fv)),
                           (0, 1, (1 - fu) * fv), (1, 1, fu * fv)):
            uu, vv = u0 + du, v0 + dv
            ok = (uu >= 0) & (uu < W) & (vv >= 0) & (vv < H)
            idx = vv[ok] * W + uu[ok]
            wt = (base * wk)[ok]
            den += np.bincount(idx, weights=wt, minlength=H * W)
            for c in range(3):
                num[:, c] += np.bincount(idx, weights=wt * values[ok, c], minlength=H * W)
        progress(4, 0.5 + 0.5 * n / total, tr("shift-and-add: {done} / {total} frames").format(done=n, total=total))

    kernel = max(KERNEL_MIN, 0.6 * s / math.sqrt(max(1, total)))
    num_img = num.reshape(H, W, 3).astype(np.float32)
    den_img = den.reshape(H, W).astype(np.float32)
    num_g = cv2.GaussianBlur(num_img, (0, 0), kernel, borderType=cv2.BORDER_REFLECT)
    den_g = cv2.GaussianBlur(den_img, (0, 0), kernel, borderType=cv2.BORDER_REFLECT)
    certainty = den_g / max(1e-12, float(np.percentile(den_g, 95)))
    fused = num_g / np.maximum(den_g, 1e-12)[:, :, None]
    # dove i campioni sono pochi la stima ricampionata pesa di piu'
    blend = np.clip(certainty * 4.0, 0.0, 1.0)[:, :, None]
    fused = blend * fused + (1 - blend) * estimate
    return fused.astype(np.float32), float(kernel), count / float(H * W)


def _richardson_lucy(image: np.ndarray, sigma: float, iterations: int, lam: float,
                     step: Callable[[int], None], cancel: threading.Event | None) -> np.ndarray:
    """Deconvoluzione di Richardson-Lucy con nucleo gaussiano e regolarizzazione a variazione totale.

    Il nucleo e' simmetrico, quindi e' anche il proprio trasposto. Con `lam` > 0
    (Dey et al., 2006) ogni passo viene diviso per 1 - lam * div(grad f / |grad f|):
    le zone piatte restano piatte e il rumore non cresce a ogni iterazione.
    """
    observed = np.clip(image, 1e-6, None).astype(np.float32)
    estimate = observed.copy()
    for n in range(1, iterations + 1):
        _check(cancel)
        blurred = cv2.GaussianBlur(estimate, (0, 0), sigma, borderType=cv2.BORDER_REFLECT)
        ratio = observed / np.maximum(blurred, 1e-6)
        correction = cv2.GaussianBlur(ratio, (0, 0), sigma, borderType=cv2.BORDER_REFLECT)
        if lam > 0:
            gy, gx = np.gradient(estimate)
            norm = np.sqrt(gx * gx + gy * gy) + 1e-4
            div = np.gradient(gx / norm, axis=1) + np.gradient(gy / norm, axis=0)
            correction = correction / np.clip(1.0 - lam * div, 0.5, 1.5)
        estimate *= correction
        np.clip(estimate, 0.0, 1.5, out=estimate)
        step(n)
    return estimate


def _noise(image: np.ndarray) -> float:
    """Deviazione del rumore stimata (Immerkaer, 1996), sulla luminanza, in unita' 0-255."""
    if image.ndim == 3:
        image = image[:, :, 0] * 0.299 + image[:, :, 1] * 0.587 + image[:, :, 2] * 0.114
    h, w = image.shape
    if h < 3 or w < 3:
        return 0.0
    kernel = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]], np.float32)
    conv = cv2.filter2D(image.astype(np.float32), -1, kernel, borderType=cv2.BORDER_REFLECT)[1:-1, 1:-1]
    sigma = math.sqrt(math.pi / 2) * float(np.abs(conv).sum()) / (6 * (w - 2) * (h - 2))
    return sigma * 255.0


def aligned_frame(result: Result, record: FrameRecord) -> np.ndarray:
    """Il fotogramma `record` riportato sulla griglia ingrandita del riferimento (per documentazione)."""
    alignment = result.alignment
    x, y, w, h = alignment.request.roi
    H, W = result.final.shape[:2]
    s = W / w
    hr_to_roi = np.array([[1 / s, 0, 0.5 / s - 0.5], [0, 1 / s, 0.5 / s - 0.5], [0, 0, 1]], dtype=np.float64)
    patch = _prepared(alignment, record, result.params)
    out = cv2.warpPerspective(patch, record.warp @ hr_to_roi, (W, H),
                              flags=cv2.INTER_LANCZOS4 | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REFLECT)
    return np.clip(out, 0.0, 1.0)


# etichette dei valori dei menu (testi inglesi, tradotti al momento dell'uso)
MOTION_LABELS = {
    "translation": N_("Translation"),
    "euclidean": N_("Rotation + translation"),
    "affine": N_("Affine"),
    "homography": N_("Perspective (homography)"),
}
METHOD_LABELS = {
    "robust-mean": N_("Robust mean (outliers rejected)"),
    "shift-and-add": N_("Shift-and-add (normalized convolution)"),
    "median": N_("Median"),
}
DENOISE_LABELS = {"off": N_("Off"), "light": N_("Light"), "medium": N_("Medium"), "strong": N_("Strong")}
REGULARIZATION_LABELS = DENOISE_LABELS
LOCAL_CONTRAST_LABELS = DENOISE_LABELS
