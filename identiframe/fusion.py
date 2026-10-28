# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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

Tipo di soggetto. Una targa o una scritta e' piana e rigida: un solo modello di
moto per fotogramma la descrive. Un volto no: la testa ruota, bocca e palpebre
si muovono. Con il soggetto «volto», dopo l'ECC ogni fotogramma riceve un
raffinamento locale non rigido (flusso ottico di Farneback tra riferimento e
fotogramma allineato, lisciato e limitato in ampiezza) con una confidenza per
pixel (coerenza avanti-indietro del flusso e correlazione locale): la fusione
pesa ogni campione con quella confidenza, i fotogrammi la cui posa o
espressione si discosta dal riferimento vengono esclusi, e i livelli
automatici sono piu' prudenti. Il campo e' lisciato e limitato proprio per non
inventare: sposta al massimo di pochi pixel cio' che i fotogrammi contengono.

I passaggi 1-4 dipendono solo da video, intervallo, riferimento, riquadro,
modello di moto e tipo di soggetto: il loro esito (Alignment) si conserva, e
cambiando i soli parametri di fusione e restauro si rifanno solo i passaggi 5-7.
"""

from __future__ import annotations

import math
import threading
import time
from dataclasses import dataclass, field
from typing import Callable, Iterator

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
LEVELS_PERCENTILES_FACE = (0.1, 99.9)  # per i volti: pelle chiara e ombre non vanno bruciate
SHARP_POWER = 4                        # peso per nitidezza = (nitidezza / massima) ** SHARP_POWER
SUBJECTS = ("plate", "text", "face")
# volti: raffinamento locale non rigido dopo l'ECC (misure in lati del riquadro, lato minore)
FLOW_MIN_SIDE = 24                  # sotto questo lato il campo locale non si stima: resta il solo modello rigido
FLOW_SMOOTH = 0.06                  # lisciamento del campo di spostamenti (sigma gaussiana)
FLOW_MAX = 0.08                     # ampiezza massima dello spostamento locale (almeno 1.5 px)
FLOW_WINDOW = 0.15                  # finestra di Farneback (almeno 9 px)
FLOW_TOLERANCE = 1.0                # errore avanti-indietro (px) oltre cui la confidenza scende
FLOW_TEXTURE = 0.10                 # varianza locale / globale sotto cui una zona conta come piatta
FACE_CORE = 0.8                     # nucleo pieno della finestra ellittica (frazione dell'ellisse inscritta)
FACE_EDGE_WEIGHT = 0.05             # peso dei campioni fuori dall'ellisse: lo sfondo si muove diversamente dal volto
# plausibilita' del warp al centro del riquadro: scala locale minima e massima, anisotropia massima, peso
# prospettico massimo (variazione del denominatore proiettivo sul lato del riquadro). Un warp oltre questi
# limiti e' un modello che si piega per far salire la correlazione, non un moto reale: si ricade su uno piu' semplice
PLAUSIBLE = {"plate": (0.4, 2.5, 2.5, 0.8), "text": (0.4, 2.5, 2.5, 0.8), "face": (0.5, 2.0, 1.5, 0.3)}
FACE_MIN_SIMILARITY = 0.45          # somiglianza locale minima assoluta per usare un fotogramma
FACE_SIMILARITY_TOLERANCE = 0.05    # scarto dalla mediana dei fotogrammi oltre cui la posa conta come diversa
#   la soglia effettiva e' adattiva: mediana - max(tolleranza, 3 deviazioni robuste), mai sotto il minimo
#   assoluto; cosi' la stessa regola vale per riprese nitide (somiglianze alte, vicine) e rumorose (basse, sparse)
# modello di moto di ripiego quando ECC non converge con quello scelto
FALLBACK = {"homography": "affine", "affine": "euclidean", "euclidean": "translation", "translation": None}

MAX_FRAMES = 3601                   # fotogrammi dell'intervallo al massimo: i limiti entro cui si cerca il soggetto
LOST_SECONDS = 1.0                  # soggetto assente per piu' di cosi': la ricerca in quel verso si ferma
LOST_MIN = 5                        # ... ma mai prima di questi fotogrammi
HOLD_CC = 0.6                       # registrazione fine che conferma il soggetto (vedi _keep_sequence)
TRACK_CHUNK = 60                    # fotogrammi decodificati per volta andando all'indietro
TRACK_BUDGET = 512 * 1024 ** 2      # memoria per un blocco di immagini di ricerca (passata 1)
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
    subject: str = "plate"      # "plate" (targa) e "text" (scritta): rigidi; "face": raffinamento locale non rigido
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
        return (str(self.info.path), self.first, self.last, self.ref, self.roi, params.motion, params.track_min,
                params.subject)


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
    implausible: bool = False                     # il modello scelto dava una deformazione non plausibile
    scale: float = float("nan")                   # geometria del warp al centro del riquadro (vedi _geometry)
    anisotropy: float = float("nan")
    perspective: float = float("nan")
    used: bool = False
    reason: str = ""                              # perche' e' stato scartato (testo inglese, chiave di tr)
    weight: float = 0.0
    # solo per i volti: raffinamento locale dopo l'ECC, sulla griglia del riquadro (pixel del video)
    flow: np.ndarray | None = None                # h x w x 2: spostamento da sommare al punto prima del warp
    confidence: np.ndarray | None = None          # h x w, 0..1: quanto il contenuto locale coincide col riferimento
    similarity: float = float("nan")              # confidenza media sulle zone con tessitura
    residual: float = float("nan")                # ampiezza media dello spostamento locale (px del video)


@dataclass
class Alignment:
    """Esito dei passaggi 1-4, riusato finche' non cambiano video, intervallo, riquadro, moto o soggetto."""

    request: Request
    motion: str
    frames: list[FrameRecord]
    max_value: float              # 255 o 65535: valore massimo dei ritagli
    track_scale: float
    stride: int                   # 1 = tutti i fotogrammi dell'intervallo
    subject: str = "plate"
    similarity_floor: float = float("nan")   # volti: soglia di somiglianza usata dalla selezione (vedi select)
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
    notes: list[str] = []
    if request.last - request.first + 1 > MAX_FRAMES:
        raise PipelineError(tr("The range has {count} frames: select at most {limit} around the "
                               "reference.").format(count=request.last - request.first + 1, limit=MAX_FRAMES))
    timings: dict[int, float] = {}

    # ---- 1. estrazione, insieme alla ricerca del soggetto: passata in grigio dal riferimento verso
    # i due estremi, che si ferma dove il soggetto non si vede piu' (l'intervallo e' solo il limite)
    started = time.perf_counter()
    scale_t = min(1.0, math.sqrt(TRACK_BUDGET / max(1, TRACK_CHUNK * info.width * info.height)))
    if scale_t < 1.0:
        size = (max(16, int(round(info.width * scale_t))), max(16, int(round(info.height * scale_t))))
        scale_t = size[0] / info.width
    else:
        size = None
    records = _track(request, size, scale_t, params.track_min, progress, cancel)
    first, count = records[0].index, len(records)
    timings[0] = time.perf_counter() - started
    progress(0, 1.0, tr("{count} frames decoded").format(count=count))
    if scale_t < 1.0:
        notes.append(tr("Subject search on frames reduced to {percent:.0f} % (memory limit).").format(
            percent=scale_t * 100))

    # ---- 2. rilevamento: ritagli dei fotogrammi in cui il soggetto e' stato trovato
    started = time.perf_counter()

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
    low, high = min(wanted), max(wanted)   # si decodifica solo il tratto in cui il soggetto c'e'
    span = high - low + 1
    for number, frame in ffmpeg.stream_frames(info, low, span, "rgb48le" if deep else "rgb24"):
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
        progress(1, (number - low + 1) / span,
                 tr("{done} / {total} frames read at full resolution").format(done=number - low + 1, total=span))
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
                          track_scale=scale_t, stride=stride, subject=params.subject, timings=timings, notes=notes)

    # ---- 3 e 4. allineamento locale e registrazione sub-pixel (ECC)
    _register(alignment, progress, cancel)
    frames = alignment.frames
    if frames[0].index > request.first or frames[-1].index < request.last:
        notes.append(tr("Subject followed from f{first} to f{last}: beyond that it is missing, or not "
                        "confirmed, for more than {seconds:g} s.").format(first=frames[0].index, last=frames[-1].index,
                                                       seconds=LOST_SECONDS))
    return alignment


def _lost_max(info: VideoInfo) -> int:
    """Fotogrammi consecutivi senza il soggetto dopo cui lo si considera perso."""
    return max(LOST_MIN, int(round(info.fps * LOST_SECONDS)))


def _keep_sequence(alignment: Alignment) -> int:
    """Tiene i fotogrammi collegati al riferimento senza buchi di registrazione piu' lunghi di LOST_SECONDS.

    La ricerca puo' continuare a lungo con punteggi alti anche quando il
    soggetto non e' piu' confermabile: coperto (il traffico davanti a un
    cartello, e allora il modello che si adatta aggancia altro) o diventato
    troppo piccolo (un veicolo che si allontana: la ricerca lo segue, ma la
    targa non ha piu' dettaglio da allineare). La registrazione fine su quei
    fotogrammi non riesce: oltre un buco senza una registrazione buona, il
    resto non si usa. Restituisce quanti fotogrammi in cui la ricerca aveva
    trovato qualcosa sono stati tolti.
    """
    frames = alignment.frames
    lost_max = _lost_max(alignment.request.info)
    ref_pos = next(i for i, r in enumerate(frames) if r.index == alignment.request.ref)
    good = [r.warp is not None and r.cc_fine >= HOLD_CC for r in frames]
    ends = []
    for direction in (1, -1):
        i, last_good = ref_pos + direction, ref_pos
        while 0 <= i < len(frames) and abs(i - last_good) <= lost_max:
            if good[i]:
                last_good = i
            i += direction
        # dopo l'ultimo buono restano i fotogrammi del buco: senza soggetto, come quelli dopo l'arresto della ricerca
        ends.append(min(len(frames) - 1, last_good + lost_max + 1) if direction > 0 else max(0, last_good - lost_max - 1))
    high, low = ends
    removed = frames[:low] + frames[high + 1:]
    alignment.frames = frames[low:high + 1]
    return sum(r.found for r in removed)


def _track(request: Request, size: tuple[int, int] | None, scale: float, track_min: float,
           progress: Progress, cancel: threading.Event | None) -> list[FrameRecord]:
    """Cerca il soggetto fotogramma per fotogramma, dal riferimento verso i due estremi dell'intervallo.

    I fotogrammi si decodificano man mano (all'indietro a blocchi di
    TRACK_CHUNK). In ogni verso la ricerca si ferma quando il soggetto manca
    da piu' di LOST_SECONDS: oltre, un riscontro sarebbe con ogni probabilita'
    un'altra cosa simile (un'altra targa, un riflesso), non il soggetto
    seguito. I fotogrammi esaminati, in ordine, sono il risultato.

    Il modello cercato e' il soggetto trovato nel fotogramma precedente,
    mescolato con quello di prima: segue cambi lenti di scala e di luce senza
    perdere di vista l'originale. La posizione prevista tiene conto della
    velocita' del soggetto.
    """
    info = request.info
    x, y, w, h = request.roi
    lost_max = max(LOST_MIN, int(round(info.fps * LOST_SECONDS)))
    total = request.last - request.first + 1

    def gray_frames(start: int, count: int) -> Iterator[tuple[int, np.ndarray]]:
        frames = ffmpeg.stream_frames(info, start, count, "gray", size=size)
        try:
            for number, frame in frames:
                _check(cancel)
                yield number, frame[:, :, 0]
        finally:
            frames.close()   # fermarsi prima della fine ferma anche ffmpeg

    def backward() -> Iterator[tuple[int, np.ndarray]]:
        end = request.ref - 1
        while end >= request.first:
            start = max(request.first, end - TRACK_CHUNK + 1)
            yield from reversed(list(gray_frames(start, end - start + 1)))
            end = start - 1

    forward = gray_frames(request.ref, request.last - request.ref + 1)
    reference_frame = next(forward, None)
    if reference_frame is None or reference_frame[0] != request.ref:
        forward.close()
        raise PipelineError(tr("The video ended before the reference frame."))
    gh, gw = reference_frame[1].shape
    tw, th = max(6, int(round(w * scale))), max(6, int(round(h * scale)))
    rx = min(max(0, int(round(x * scale))), gw - tw)
    ry = min(max(0, int(round(y * scale))), gh - th)
    reference = reference_frame[1][ry:ry + th, rx:rx + tw].astype(np.float32)

    ref_record = FrameRecord(index=request.ref, time=request.ref / info.fps)
    ref_record.found, ref_record.track_score, ref_record.position = True, 1.0, (float(x), float(y))
    records = [ref_record]
    radius = int(round(max(tw, th) * SEARCH)) + 6
    for frames in (forward, backward()):
        template = reference.copy()
        px, py = float(rx), float(ry)
        vx = vy = 0.0
        missing = 0
        for number, gray in frames:
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
            record = FrameRecord(index=number, time=number / info.fps)
            records.append(record)
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
                missing = 0
            else:
                # perso: si prosegue sulla posizione prevista, il modello resta quello
                px, py = cx, cy
                record.found = False
                record.reason = N_("subject not found")
                missing += 1
            progress(0, len(records) / total, tr("searching the subject: {done} / {total}").format(
                done=len(records), total=total))
            if missing > lost_max:
                break
        frames.close()
    records.sort(key=lambda r: r.index)
    return records


def _gray(image: np.ndarray, max_value: float) -> np.ndarray:
    """Luminanza in virgola mobile, 0..1."""
    rgb = image.astype(np.float32) / max_value
    return rgb[:, :, 0] * 0.299 + rgb[:, :, 1] * 0.587 + rgb[:, :, 2] * 0.114


def _translation(dx: float, dy: float) -> np.ndarray:
    return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]], dtype=np.float64)


def _scale_matrix(k: float) -> np.ndarray:
    return np.array([[k, 0, 0], [0, k, 0], [0, 0, 1]], dtype=np.float64)


def _geometry(warp: np.ndarray, w: int, h: int) -> tuple[float, float, float]:
    """Scala locale, anisotropia e peso prospettico del warp al centro del riquadro w x h.

    Dallo jacobiano al centro: scala = radice del determinante, anisotropia =
    rapporto dei valori singolari (stiramento o taglio). Il peso prospettico e'
    quanto la riga proiettiva fa variare il denominatore lungo il lato del
    riquadro: 0 per un'affinita', oltre 1 la linea di fuga taglia il riquadro.
    """
    cx, cy = (w - 1) / 2, (h - 1) / 2

    def at(x: float, y: float) -> np.ndarray:
        v = warp @ np.array([x, y, 1.0])
        return v[:2] / v[2]

    jacobian = np.column_stack([(at(cx + 1, cy) - at(cx - 1, cy)) / 2, (at(cx, cy + 1) - at(cx, cy - 1)) / 2])
    singular = np.linalg.svd(jacobian, compute_uv=False)
    scale = float(math.sqrt(max(0.0, singular[0] * singular[1])))
    anisotropy = float(singular[0] / max(singular[1], 1e-9))
    perspective = float(math.hypot(warp[2, 0], warp[2, 1]) * max(w, h))
    return scale, anisotropy, perspective


def _plausible(warp: np.ndarray, w: int, h: int, subject: str) -> bool:
    """Il warp descrive un moto possibile del soggetto (limiti in PLAUSIBLE)?"""
    low, high, anisotropy_max, perspective_max = PLAUSIBLE.get(subject, PLAUSIBLE["plate"])
    scale, anisotropy, perspective = _geometry(warp, w, h)
    return (all(math.isfinite(v) for v in (scale, anisotropy, perspective))
            and low <= scale <= high and anisotropy <= anisotropy_max and perspective <= perspective_max)


def _face_window(w: int, h: int) -> np.ndarray:
    """Finestra ellittica sul riquadro (volti): 1 nel nucleo, scende a 0 sull'ellisse inscritta e fuori."""
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    radius = np.sqrt(((xs - (w - 1) / 2) / (w / 2)) ** 2 + ((ys - (h - 1) / 2) / (h / 2)) ** 2)
    t = np.clip((radius - FACE_CORE) / (1.0 - FACE_CORE), 0.0, 1.0)
    return (1.0 - t * t * (3.0 - 2.0 * t)).astype(np.float32)


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
    ref.similarity, ref.residual = 1.0, 0.0
    face = alignment.subject == "face"

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
            except cv2.error:
                model = FALLBACK[model]
                continue
            # convergenza raggiunta: ma la deformazione deve essere un moto possibile del soggetto
            if model == "translation" or _plausible(np.linalg.inv(s) @ warp @ s, w, h, alignment.subject):
                break
            record.implausible = True
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
        start = record.warp
        while model is not None:
            try:
                warp, cc = _ecc(template, gray, start, model, 200, 1e-7, 3)
            except cv2.error:
                model = FALLBACK[model]
                continue
            if model == "translation" or _plausible(warp, w, h, alignment.subject):
                record.warp, record.cc_fine = warp, cc
                break
            record.implausible = True
            model = FALLBACK[model]
        if model is None:
            record.warp = None
            record.reason = N_("sub-pixel registration failed")
            continue
        record.model = model
        record.scale, record.anisotropy, record.perspective = _geometry(record.warp, w, h)
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
        if face:
            # volto: cio' che il modello rigido non spiega (espressione, rotazione della testa)
            record.flow, record.confidence, record.residual, record.similarity = _local_flow(template, aligned)
        progress(3, n / max(1, len(candidates)), tr("{done} / {total} frames registered").format(
            done=n, total=len(candidates)))
    alignment.timings[3] = time.perf_counter() - started
    # prima si tolgono i fotogrammi staccati dalla sequenza del riferimento: le note e i conteggi
    # devono parlare degli stessi fotogrammi della tabella del rapporto
    cut = _keep_sequence(alignment)
    if cut:
        alignment.notes.append(tr("{count} frames left out because they come after more than {seconds:g} s without "
                                  "a good alignment: from there the subject is no longer confirmed (covered, too "
                                  "small or out of the frame).").format(count=cut, seconds=LOST_SECONDS))
    kept = {id(r) for r in alignment.frames}
    candidates = [r for r in candidates if id(r) in kept]
    registered = sum(1 for r in alignment.frames if r.warp is not None)
    forced = sum(1 for r in candidates if r.warp is not None and r.implausible)
    simpler = sum(1 for r in candidates if r.warp is not None and r.model != motion and not r.implausible)
    if simpler:
        alignment.notes.append(tr("{count} frames aligned with a simpler motion model, because the chosen one "
                                  "did not converge on them.").format(count=simpler))
    if forced:
        alignment.notes.append(tr("{count} frames aligned with a simpler motion model, because the chosen one gave "
                                  "an implausible deformation (scale, shear or perspective beyond the limits)."
                                  ).format(count=forced))
    if face:
        refined = [r for r in candidates if r.flow is not None]
        if refined:
            alignment.notes.append(tr("Face: local non-rigid refinement after ECC on {count} frames, mean "
                                      "displacement {residual:.2f} px of the video.").format(
                count=len(refined), residual=sum(r.residual for r in refined) / len(refined)))
        else:
            alignment.notes.append(tr("Face: the area is too small for the local refinement ({size} px at least): "
                                      "rigid alignment only.").format(size=FLOW_MIN_SIDE))
    progress(3, 1.0, tr("{count} frames registered").format(count=registered))


def _to8(gray: np.ndarray) -> np.ndarray:
    """Luminanza standardizzata (media 128, deviazione 40) in 8 bit: riferimento e fotogramma sulla stessa scala."""
    std = float(gray.std())
    z = (gray - float(gray.mean())) / (std if std > 1e-6 else 1.0)
    return np.clip(z * 40.0 + 128.0, 0, 255).astype(np.uint8)


def _local_zncc(a: np.ndarray, b: np.ndarray, sigma: float) -> tuple[np.ndarray, np.ndarray]:
    """Correlazione normalizzata in finestre gaussiane e tessitura locale del riferimento (0 piatto, 1 ricco)."""
    def blur(image: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(image, (0, 0), sigma, borderType=cv2.BORDER_REFLECT)
    ma, mb = blur(a), blur(b)
    va = np.maximum(blur(a * a) - ma * ma, 0.0)
    vb = np.maximum(blur(b * b) - mb * mb, 0.0)
    cov = blur(a * b) - ma * mb
    zncc = cov / np.sqrt(np.maximum(va * vb, 1e-12))
    texture = np.clip(va / (FLOW_TEXTURE * (float(a.var()) + 1e-8)), 0.0, 1.0)
    return zncc, texture


def _local_flow(template: np.ndarray, aligned: np.ndarray
                ) -> tuple[np.ndarray | None, np.ndarray | None, float, float]:
    """Raffinamento locale per i volti: campo di spostamenti, confidenza per pixel, ampiezza media, somiglianza.

    Il flusso ottico di Farneback tra il riferimento e il fotogramma gia'
    allineato col modello rigido dice dove ogni dettaglio si e' spostato
    (espressione, rotazione della testa). Il campo viene lisciato e limitato in
    ampiezza, cosi' non puo' inventare nulla: sposta di pochi pixel cio' che il
    fotogramma contiene. La confidenza unisce la coerenza avanti-indietro del
    flusso e la correlazione locale tra riferimento e fotogramma riportato; le
    zone piatte, dove non c'e' nulla da allineare, contano come affidabili. La
    somiglianza e' la correlazione media sulle zone con tessitura: bassa quando
    posa o espressione sono cambiate davvero.
    """
    h, w = template.shape
    side = min(w, h)
    if side < FLOW_MIN_SIDE:
        zncc, texture = _local_zncc(template, aligned, max(2.0, 0.08 * side))
        weight = texture.sum()
        similarity = float((texture * np.clip(zncc, 0.0, 1.0)).sum() / weight) if weight > 0 else 1.0
        return None, None, 0.0, similarity
    a, b = _to8(template), _to8(aligned)
    window = int(max(9, round(FLOW_WINDOW * side))) | 1
    levels = max(1, min(3, int(math.log2(side / 16))))
    args = dict(pyr_scale=0.5, levels=levels, winsize=window, iterations=3, poly_n=5, poly_sigma=1.1, flags=0)
    try:
        forward = cv2.calcOpticalFlowFarneback(a, b, None, **args)
        backward = cv2.calcOpticalFlowFarneback(b, a, None, **args)
    except cv2.error:
        return None, None, 0.0, 1.0
    smooth = max(1.0, FLOW_SMOOTH * side)
    forward = cv2.GaussianBlur(forward, (0, 0), smooth, borderType=cv2.BORDER_REFLECT)
    backward = cv2.GaussianBlur(backward, (0, 0), smooth, borderType=cv2.BORDER_REFLECT)
    limit = max(1.5, FLOW_MAX * side)
    for flow in (forward, backward):
        magnitude = np.sqrt(flow[:, :, 0] ** 2 + flow[:, :, 1] ** 2)
        flow *= np.minimum(1.0, limit / np.maximum(magnitude, 1e-6))[:, :, None]
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    px, py = xs + forward[:, :, 0], ys + forward[:, :, 1]
    # coerenza: il flusso inverso, letto nel punto d'arrivo, deve riportare al punto di partenza
    back_x = cv2.remap(backward[:, :, 0], px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    back_y = cv2.remap(backward[:, :, 1], px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    error = np.sqrt((forward[:, :, 0] + back_x) ** 2 + (forward[:, :, 1] + back_y) ** 2)
    consistency = 1.0 / (1.0 + (error / FLOW_TOLERANCE) ** 2)
    warped = cv2.remap(aligned, px, py, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    zncc, texture = _local_zncc(template, warped, max(2.0, 0.08 * side))
    agreement = np.clip(zncc, 0.0, 1.0) * consistency
    confidence = (1.0 - texture * (1.0 - agreement)).astype(np.float32)
    # lo sfondo attorno al volto si muove in modo diverso: fuori dall'ellisse inscritta i campioni contano poco
    confidence *= np.maximum(FACE_EDGE_WEIGHT, _face_window(w, h))
    weight = texture.sum()
    similarity = float((texture * np.clip(zncc, 0.0, 1.0)).sum() / weight) if weight > 0 else 1.0
    residual = float(np.sqrt(forward[:, :, 0] ** 2 + forward[:, :, 1] ** 2).mean())
    return forward.astype(np.float32), confidence, residual, similarity


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
    face = alignment.subject == "face"
    floor = FACE_MIN_SIMILARITY
    if face:
        # soglia adattiva: i fotogrammi con la stessa posa hanno somiglianze vicine tra loro, quelli con posa o
        # espressione diverse se ne staccano verso il basso, qualunque sia il livello assoluto (rumore, nitidezza)
        sims = np.array([r.similarity for r in alignment.frames
                         if r is not ref and r.warp is not None and math.isfinite(r.similarity)])
        if sims.size >= 3:
            median = float(np.median(sims))
            spread = 3 * 1.4826 * float(np.median(np.abs(sims - median)))
            floor = max(FACE_MIN_SIMILARITY, median - max(FACE_SIMILARITY_TOLERANCE, spread))
        alignment.similarity_floor = floor
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
        if face and record.similarity < floor:
            record.reason = N_("pose or expression differs from the reference")
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
        if face and math.isfinite(record.similarity):
            weight *= max(0.05, record.similarity)   # un volto piu' simile al riferimento conta di piu'
        record.weight = float(weight)
    chosen.sort(key=lambda r: r.index)
    return chosen


# ------------------------------------------------------------- passaggi 5-7

def fuse(alignment: Alignment, params: Params, progress: Progress,
         cancel: threading.Event | None = None, frames: list[FrameRecord] | None = None) -> Result:
    """Passaggi 5-7. Con `frames` si fonde solo quel sottoinsieme, gia' scelto e pesato da una fusione
    precedente (select non viene richiamata, used/weight dei fotogrammi non cambiano): serve alla
    lettura dei caratteri (ocr.py), che confronta fusioni di gruppi di fotogrammi indipendenti."""
    request = alignment.request
    x, y, w, h = request.roi
    notes = list(alignment.notes)
    s = int(params.scale)
    if w * h * s * s > MAX_OUTPUT_PIXELS:
        s_max = max(1, int(math.sqrt(MAX_OUTPUT_PIXELS / (w * h))))
        notes.append(tr("Scale reduced from ×{asked} to ×{used}: the area is too large.").format(
            asked=s, used=s_max))
        s = s_max
    chosen = select(alignment, params) if frames is None else sorted(frames, key=lambda r: r.index)
    if frames is None and len(chosen) < 3:
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
    ref = alignment.reference
    rox, roy = ref.origin
    native = ref.patch[y - roy:y - roy + h, x - rox:x - rox + w].astype(np.float32) / alignment.max_value
    reference = cv2.resize(native, (W, H), interpolation=cv2.INTER_CUBIC) if s > 1 else native.copy()
    reference = np.clip(reference, 0.0, 1.0)
    if alignment.subject == "face":
        # fuori dall'ellisse inscritta nel riquadro resta il riferimento: lo sfondo non e' il soggetto
        window = cv2.resize(_face_window(w, h), (W, H), interpolation=cv2.INTER_LINEAR)[:, :, None]
        fused = window * fused + (1.0 - window) * reference
    timings[4] = time.perf_counter() - started
    progress(4, 1.0, tr("{count} frames fused on a ×{scale} grid").format(count=len(chosen), scale=s))

    # ---- 6. riduzione del rumore e deconvoluzione (sulla luminanza)
    started = time.perf_counter()
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
    fusione, prima del restauro. Per i volti i percentili sono piu' esterni:
    pelle chiara e ombre profonde non vanno portate a bianco e nero pieni.
    """
    if not params.levels:
        return image, (0.0, 1.0)
    percentiles = LEVELS_PERCENTILES_FACE if params.subject == "face" else LEVELS_PERCENTILES
    lo, hi = (float(v) for v in np.percentile(_luma(image), percentiles))
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


def _resample(patch: np.ndarray, record: FrameRecord, hr_to_roi: np.ndarray, width: int, top: int, rows: int,
              interpolation: int) -> tuple[np.ndarray, np.ndarray, np.ndarray | None]:
    """Il ritaglio portato sulle righe top..top+rows della griglia ingrandita.

    Restituisce immagine, maschera dei campioni dentro al ritaglio e, se il
    fotogramma ha il campo locale (volti), la confidenza per pixel; altrimenti None.
    Senza campo basta l'omografia (warpPerspective). Con il campo, per ogni
    pixel della griglia si calcola il punto del riquadro, vi si somma lo
    spostamento locale e si applica l'omografia: un solo remap.
    """
    shift = _translation(0, top)
    if record.flow is None:
        m = record.warp @ hr_to_roi @ shift
        image = cv2.warpPerspective(patch, m, (width, rows), flags=interpolation | cv2.WARP_INVERSE_MAP,
                                    borderMode=cv2.BORDER_REFLECT)
        ones = np.ones(patch.shape[:2], np.float32)
        valid = cv2.warpPerspective(ones, m, (width, rows), flags=cv2.INTER_NEAREST | cv2.WARP_INVERSE_MAP,
                                    borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        return image, valid, None
    grid = hr_to_roi @ shift
    xs, ys = np.meshgrid(np.arange(width, dtype=np.float32), np.arange(rows, dtype=np.float32))
    rx = (grid[0, 0] * xs + grid[0, 2]).astype(np.float32)
    ry = (grid[1, 1] * ys + grid[1, 2]).astype(np.float32)
    fx = cv2.remap(record.flow[:, :, 0], rx, ry, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    fy = cv2.remap(record.flow[:, :, 1], rx, ry, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    confidence = cv2.remap(record.confidence, rx, ry, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    qx, qy = rx + fx, ry + fy
    m = record.warp
    den = m[2, 0] * qx + m[2, 1] * qy + m[2, 2]
    mx = ((m[0, 0] * qx + m[0, 1] * qy + m[0, 2]) / den).astype(np.float32)
    my = ((m[1, 0] * qx + m[1, 1] * qy + m[1, 2]) / den).astype(np.float32)
    image = cv2.remap(patch, mx, my, interpolation, borderMode=cv2.BORDER_REFLECT)
    ph, pw = patch.shape[:2]
    valid = ((mx >= 0) & (mx <= pw - 1) & (my >= 0) & (my <= ph - 1)).astype(np.float32)
    return image, valid, confidence


def _robust_stack(alignment: Alignment, chosen: list[FrameRecord], weights: np.ndarray, hr_to_roi: np.ndarray,
                  size: tuple[int, int], params: Params, median: bool, progress: Progress,
                  cancel: threading.Event | None, share: float) -> np.ndarray:
    """Ogni fotogramma ricampionato sulla griglia ingrandita, poi mediana o media con scarto degli anomali.

    Si lavora a strisce orizzontali per non tenere in memoria l'intera pila.
    Per i volti ogni campione pesa anche per la confidenza locale del suo fotogramma.
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
        stack = np.empty((n, rows, W, 3), np.float32)
        valid = np.empty((n, rows, W, 1), np.float32)
        local = np.ones((n, rows, W, 1), np.float32)
        for i, (record, patch) in enumerate(zip(chosen, patches)):
            stack[i], valid[i, :, :, 0], confidence = _resample(patch, record, hr_to_roi, W, top, rows,
                                                                cv2.INTER_LANCZOS4)
            if confidence is not None:
                local[i, :, :, 0] = confidence
        if not median and n < 3:
            out[top:top + rows] = _weighted_mean(stack, valid * local * w)
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
            out[top:top + rows] = _weighted_mean(stack, keep.astype(np.float32) * local * w, fallback=med)
        progress(4, share * min(1.0, (top + rows) / H), tr("resampling on the fine grid: {percent:.0f} %").format(
            percent=100 * share * min(1.0, (top + rows) / H)))
    return out


def _weighted_mean(stack: np.ndarray, weights: np.ndarray, fallback: np.ndarray | None = None) -> np.ndarray:
    total = weights.sum(axis=0)
    mean = (stack * weights).sum(axis=0) / np.maximum(total, 1e-12)
    if fallback is not None:
        mean = np.where(total > 0, mean, np.nan_to_num(fallback, nan=0.0))
    return mean


SAMPLE_COLUMNS = 4096   # larghezza della mappa di _sample_points: OpenCV vuole righe e colonne sotto 32767


def _sample_points(image: np.ndarray, x: np.ndarray, y: np.ndarray, border: int) -> np.ndarray:
    """Valori di `image` (un canale) nei punti (x, y), con interpolazione bilineare.

    cv2.remap accetta mappe con meno di 32767 righe e colonne: i punti non vanno
    passati come una colonna sola (un ritaglio grande ne ha centinaia di
    migliaia), ma disposti in righe di SAMPLE_COLUMNS, completando l'ultima.
    """
    n = x.size
    if n == 0:
        return np.zeros(0, np.float32)
    rows = -(-n // SAMPLE_COLUMNS)
    pad = rows * SAMPLE_COLUMNS - n
    mx = np.pad(x.astype(np.float32), (0, pad)).reshape(rows, SAMPLE_COLUMNS)
    my = np.pad(y.astype(np.float32), (0, pad)).reshape(rows, SAMPLE_COLUMNS)
    return cv2.remap(image, mx, my, cv2.INTER_LINEAR, borderMode=border).ravel()[:n]


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
        """Posizione sulla griglia ingrandita, colore, scarto dalla stima e confidenza di ogni pixel del ritaglio."""
        patch = _prepared(alignment, record, params)
        ph, pw = patch.shape[:2]
        ys, xs = np.mgrid[0:ph, 0:pw]
        pts = np.stack([xs.ravel(), ys.ravel(), np.ones(xs.size)]).astype(np.float64)
        roi = np.linalg.inv(record.warp) @ pts
        rx, ry = roi[0] / roi[2], roi[1] / roi[2]
        local = np.ones(rx.size, np.float64)
        if record.flow is not None:
            # il campo locale e' definito sui punti del riquadro: inverso al primo ordine (campo liscio e piccolo)
            fx = _sample_points(record.flow[:, :, 0], rx, ry, cv2.BORDER_REPLICATE)
            fy = _sample_points(record.flow[:, :, 1], rx, ry, cv2.BORDER_REPLICATE)
            local = _sample_points(record.confidence, rx, ry, cv2.BORDER_REPLICATE).astype(np.float64)
            rx, ry = rx - fx, ry - fy
        u = roi_to_hr[0, 0] * rx + roi_to_hr[0, 2]
        v = roi_to_hr[1, 1] * ry + roi_to_hr[1, 2]
        inside = (u > -1) & (u < W) & (v > -1) & (v < H)
        u, v, local = u[inside], v[inside], local[inside]
        values = patch.reshape(-1, 3)[inside].astype(np.float64)
        at = _sample_points(luma_est, u, v, cv2.BORDER_REFLECT)
        luma = values[:, 0] * 0.299 + values[:, 1] * 0.587 + values[:, 2] * 0.114
        return u, v, values, np.abs(luma - at), local

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
        u, v, values, resid, local = samples(record)
        count += u.size
        robust = np.minimum(1.0, threshold / np.maximum(resid, 1e-9))   # peso di Huber
        base = float(weights[n - 1]) * robust * local
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
    out, _valid, _confidence = _resample(patch, record, hr_to_roi, W, 0, H, cv2.INTER_LANCZOS4)
    return np.clip(out, 0.0, 1.0)


# etichette dei valori dei menu (testi inglesi, tradotti al momento dell'uso)
SUBJECT_LABELS = {
    "plate": N_("Plate"),
    "text": N_("Text"),
    "face": N_("Face"),
}
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
