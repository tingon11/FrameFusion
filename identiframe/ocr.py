# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Lettura dei caratteri di una targa o di una scritta (OCR) con voto carattere per carattere.

Su un soggetto piccolo nessun fotogramma da solo e' leggibile da un OCR: si
legge invece il risultato della fusione e, per sapere quanto ogni carattere e'
sicuro, le fusioni di GRUPPI indipendenti di fotogrammi. I fotogrammi usati
vengono divisi in gruppi alterni (ognuno con fotogrammi di tutto l'intervallo
e di nitidezza simile), ogni gruppo viene fuso e restaurato con gli stessi
parametri, e ogni immagine viene letta. Le letture vengono allineate a quella
piu' rappresentativa (Ratcliff/Obershelp, difflib) e per ogni posizione si
contano i voti, pesati per la probabilita' che il modello da' a ogni
carattere: il carattere scelto e la quota di accordo dicono quanto la lettura
e' sostenuta dai dati, e le alternative mostrano dove i fotogrammi lasciano il
dubbio. La combinazione per carattere segue Quiala et al., «Enhancing License
Plate Recognition in Videos through Character-Wise Temporal Combination» (2023).

Due motori, modelli ONNX eseguiti dal modulo DNN di OpenCV (gia' nel
programma) e scaricati a richiesta in tools/ocr (vedi tools.py):

- targa: fast-plate-ocr (MIT), modello cct-s-v2-global. Legge il riquadro
  della targa intero in 10 posizioni, con la probabilita' di ogni carattere, e
  riconosce il formato della targa (il paese) tra 65.
- testo: PaddleOCR PP-OCRv6 small (Apache-2.0, conversione ONNX di RapidOCR).
  Trova le righe di testo nel risultato (rete DB) e legge ogni riga (CTC), in
  molte lingue e alfabeti; ogni riga viene votata per conto suo.

E' una lettura automatica, da verificare sulle immagini: il rapporto lo dice.
"""

from __future__ import annotations

import difflib
import math
import re
import struct
import threading
from collections import defaultdict
from dataclasses import dataclass, field

import cv2
import numpy as np

from . import fusion, tools
from .i18n import tr

GROUPS = 8                   # fusioni indipendenti da leggere oltre al risultato
MIN_PER_GROUP = 3            # fotogrammi minimi per gruppo: con meno si fanno meno gruppi
RESULT_WEIGHT = 2.0          # peso della lettura del risultato completo rispetto a quella di un gruppo
# I modelli non hanno una risposta «non so»: anche su un'immagine senza caratteri riconoscibili danno sempre i
# caratteri piu' probabili. Sotto queste soglie la lettura non si mostra come tale.
LEGIBLE_CONFIDENCE = 0.6     # probabilita' media dei caratteri letti nel risultato: sotto, la riga e' illeggibile
CHAR_MIN_SUPPORT = 0.5       # sostegno minimo di un carattere (vedi Position.support): sotto, si mostra «?»
UNREADABLE = "?"
GAP = "–"                    # voto per «nessun carattere in questa posizione» (stampabile anche nel PDF)
# caratteri dalla forma simile: segnalati quando sono tra le prime alternative del voto e, sulle targhe, sempre
PLATE_CONFUSABLE = [set("8B"), set("0DO"), set("1I"), set("5S"), set("2Z"), set("6G")]
TEXT_CONFUSABLE = [set("8B"), set("0DOo"), set("1Il"), set("5Ss"), set("2Zz"), set("6G")]
# PP-OCR, come in PaddleOCR e RapidOCR: rilevamento sul lato corto portato ad almeno 736 pixel, soglie della
# mappa di probabilita' e allargamento delle righe trovate; lettura a 48 pixel di altezza, larghezza minima 320
DET_SIDE = 736
DET_THRESH, DET_BOX_THRESH, DET_UNCLIP = 0.3, 0.5, 1.6
REC_HEIGHT, REC_MIN_WIDTH = 48, 320
ARC = np.linspace(0.0, 2.0 * np.pi, 64, endpoint=False)


class OcrError(RuntimeError):
    """Modelli assenti o illeggibili: il messaggio e' per l'utente."""


def kind_for(subject: str) -> str:
    """Il motore per un tipo di soggetto: «text» per le scritte, «plate» per tutto il resto."""
    return "text" if subject == "text" else "plate"


@dataclass
class Reading:
    source: str                  # "result" o "group N"
    frames: list[int]            # fotogrammi della fusione letta
    text: str                    # caratteri letti
    confidence: float            # 0..100, media delle probabilita' dei caratteri
    weight: float
    char_conf: list[float] = field(default_factory=list)   # probabilita' di ogni carattere letto (0..1)


@dataclass
class Position:
    char: str                    # carattere scelto
    share: float                 # quota dei voti per il carattere scelto (0..1)
    alternatives: list[tuple[str, float]]   # altri candidati con la loro quota, in ordine
    confusable: bool             # il secondo candidato ha una forma simile (8/B, 0/D...)
    lookalikes: str = ""         # caratteri dalla forma simile a quello scelto («B» per un 8): da verificare a occhio
    # sostegno: voti del carattere scelto sul peso di tutte le letture (0..1); vale 1 solo se ogni lettura lo
    # legge in quella posizione con probabilita' 1. Unisce accordo e sicurezza del modello
    support: float = 1.0

    @property
    def shown(self) -> str:
        """Il carattere da mostrare: quello scelto, oppure «?» se il sostegno e' troppo basso."""
        return self.char if self.support >= CHAR_MIN_SUPPORT else UNREADABLE


@dataclass
class Line:
    """Una riga letta e votata: tutta la targa, o una riga di una scritta."""
    text: str
    agreement: float             # quota media di accordo sulle posizioni scelte (0..1)
    positions: list[Position]
    readings: list[Reading]
    box: tuple[int, int, int, int] | None = None   # riquadro letto nel risultato (x, y, w, h); None = tutta l'area

    @property
    def confidence(self) -> float:
        """Probabilita' media che il modello da' ai caratteri di questa riga letti nel risultato."""
        values = [c for r in self.readings if r.source == "result" for c in r.char_conf]
        return sum(values) / len(values) if values else 0.0

    @property
    def legible(self) -> bool:
        return self.confidence >= LEGIBLE_CONFIDENCE

    @property
    def shown(self) -> str:
        """La riga come va mostrata: vuota se illeggibile, «?» al posto dei caratteri senza sostegno."""
        return "".join(p.shown for p in self.positions) if self.legible else ""

    @property
    def unreadable(self) -> list[int]:
        """Posizioni mostrate come «?»."""
        return [i for i, p in enumerate(self.positions) if p.shown == UNREADABLE] if self.legible else []

    @property
    def uncertain(self) -> list[int]:
        """Indici delle posizioni dubbie: accordo sotto il 70 % o forma simile al secondo candidato."""
        return [i for i, p in enumerate(self.positions) if p.share < 0.7 or (p.confusable and p.share < 0.9)]

    @property
    def lookalike(self) -> list[int]:
        """Posizioni con un carattere dalla forma ambigua (8/B, 2/Z...): l'OCR puo' sbagliarle tutte allo stesso
        modo, e il voto non lo vede. Vanno sempre controllate sulle immagini."""
        return [i for i, p in enumerate(self.positions) if p.lookalikes]


@dataclass
class CharReading:
    kind: str                    # "plate" o "text"
    lines: list[Line]
    engine: str                  # motore e modello, per il rapporto
    license: str
    notes: list[str] = field(default_factory=list)
    region: str = ""             # formato della targa (paese) piu' votato; solo per le targhe
    region_share: float = 0.0

    @property
    def text(self) -> str:
        """Cio' che il modello propone, anche dove l'immagine non e' leggibile: e' un dato, non la lettura."""
        return "\n".join(line.text for line in self.lines)

    @property
    def legible(self) -> bool:
        """Almeno una riga che il modello legge con sicurezza sufficiente."""
        return any(line.legible for line in self.lines)

    @property
    def shown_text(self) -> str:
        """La lettura: le sole righe leggibili, con «?» al posto dei caratteri senza sostegno."""
        return "\n".join(line.shown for line in self.lines if line.legible)

    @property
    def agreement(self) -> float:
        shares = [p.share for line in self.lines for p in line.positions]
        return sum(shares) / len(shares) if shares else 0.0

    @property
    def confidence(self) -> float:
        """Probabilita' media che il modello da' ai caratteri letti nel risultato (0..1).

        L'accordo dice quanto le letture coincidono; la fiducia quanto il modello
        e' sicuro di cio' che legge: letture concordi ma a bassa fiducia sono
        spesso testo illeggibile interpretato sempre allo stesso modo.
        """
        values = [c for line in self.lines for r in line.readings if r.source == "result" for c in r.char_conf]
        return sum(values) / len(values) if values else 0.0

    @property
    def count(self) -> int:
        """Immagini lette (il risultato e le fusioni dei gruppi)."""
        return max((len(line.readings) for line in self.lines), default=0)

    def label(self, line: int, index: int) -> str:
        """Numero di una posizione per l'utente: «3», oppure «2.3» (riga 2, carattere 3) se le righe sono piu'."""
        return f"{line + 1}.{index + 1}" if len(self.lines) > 1 else f"{index + 1}"

    def shown(self) -> str:
        """La lettura su una riga: i caratteri della targa distanziati, le righe di una scritta separate da «|».

        Vuota se nessuna riga e' leggibile: i caratteri proposti dal modello non vanno presentati come lettura.
        """
        if self.kind == "plate":
            return " ".join(self.shown_text)
        return "  |  ".join(line.shown for line in self.lines if line.legible)


# ----------------------------------------------------------------- immagini

def _luma8(image: np.ndarray) -> np.ndarray:
    gray = image[:, :, 0] * 0.299 + image[:, :, 1] * 0.587 + image[:, :, 2] * 0.114
    return np.round(np.clip(gray, 0.0, 1.0) * 255.0).astype(np.uint8)


def _rgb8(image: np.ndarray) -> np.ndarray:
    return np.round(np.clip(image, 0.0, 1.0) * 255.0).astype(np.uint8)


def _crop(image: np.ndarray, box: tuple[int, int, int, int] | None) -> np.ndarray:
    if box is None:
        return image
    x, y, w, h = box
    return image[y:y + h, x:x + w]


def locate_text(image: np.ndarray) -> tuple[int, int, int, int] | None:
    """La fascia della targa (o della scritta) dentro l'area: (x, y, larghezza, altezza) sulla griglia del risultato.

    L'area disegnata contiene spesso il frontale dell'auto: griglia, logo e
    fari confondono un OCR che si aspetta la sola targa. I caratteri sono bordi
    verticali fitti e alternati: si prendono i bordi orizzontali di intensita'
    (Sobel x, soglia di Otsu), si uniscono in fasce con una chiusura
    morfologica orizzontale e si sceglie la fascia con proporzioni da targa,
    densita' di bordi e numero di alternanze chiaro/scuro lungo la sua riga
    centrale piu' alti. Il riquadro viene allargato di un margine. None se non
    c'e' una fascia convincente: allora si legge tutta l'area.
    """
    gray = _luma8(image)
    h, w = gray.shape
    smooth = cv2.GaussianBlur(gray, (0, 0), max(1.0, h / 150))
    gx = np.abs(cv2.Sobel(smooth.astype(np.float32), cv2.CV_32F, 1, 0, ksize=3))
    gx = (255 * gx / max(1e-6, float(gx.max()))).astype(np.uint8)
    _threshold, mask = cv2.threshold(gx, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kw, kh = max(3, int(w * 0.06)) | 1, max(3, int(h * 0.04)) | 1
    band = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (kw, kh)))
    band = cv2.morphologyEx(band, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (kw // 2 | 1, kh)))
    contours, _hierarchy = cv2.findContours(band, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best, best_score = None, 0.0
    for contour in contours:
        x, y, bw, bh = cv2.boundingRect(contour)
        aspect, fraction = bw / max(1, bh), bw * bh / float(w * h)
        if not (1.8 <= aspect <= 12 and 0.02 <= fraction <= 0.8 and bh >= 0.08 * h):
            continue
        density = float(mask[y:y + bh, x:x + bw].mean()) / 255
        row = gray[y + bh // 2, x:x + bw].astype(np.int16)
        alternations = np.count_nonzero(np.abs(np.diff(np.sign(row - row.mean()))) > 0) / max(1, bw) * 10
        score = density * min(alternations, 3.0) * math.sqrt(fraction)
        if score > best_score:
            best, best_score = (x, y, bw, bh), score
    if best is None or best_score < 0.01:
        return None
    x, y, bw, bh = best
    x, bw = _trim_sides(gray[y:y + bh], x, bw)
    # margine stretto ai lati (bordo della targa e banda blu verrebbero letti come caratteri), piu' largo sopra e sotto
    mx, my = int(round(0.02 * bw)) + 2, int(round(0.25 * bh)) + 2
    x0, y0 = max(0, x - mx), max(0, y - my)
    x1, y1 = min(w, x + bw + mx), min(h, y + bh + my)
    if (x1 - x0) * (y1 - y0) > 0.9 * w * h:
        return None   # e' praticamente tutta l'area: niente da ritagliare
    return x0, y0, x1 - x0, y1 - y0


def _trim_sides(rows: np.ndarray, x: int, bw: int) -> tuple[int, int]:
    """Toglie ai due lati della fascia le colonne uniformemente scure o chiare: banda blu europea, cornice.

    Una colonna di caratteri alterna chiaro e scuro (deviazione alta); la banda
    blu, in luminanza, e' un blocco scuro uniforme. Si stringe finche' si
    trovano colonne con poca variazione e lontane dal fondo della targa; mai
    piu' di un quarto per lato.
    """
    block = rows[:, x:x + bw].astype(np.float32)
    if block.size == 0:
        return x, bw
    background = float(np.percentile(block, 80))
    means, stds = block.mean(axis=0), block.std(axis=0)
    flat = (stds < 0.12 * max(background, 1.0)) & (np.abs(means - background) > 0.25 * max(background, 1.0))
    # piccolo lisciamento: una colonna isolata non basta
    flat = np.convolve(flat.astype(np.float32), np.ones(3) / 3, mode="same") > 0.6
    limit = bw // 4
    left = 0
    while left < limit and flat[left]:
        left += 1
    right = 0
    while right < limit and flat[bw - 1 - right]:
        right += 1
    return x + left, bw - left - right


def plate_rect(image: np.ndarray, box: tuple[int, int, int, int]) -> tuple[int, int, int, int] | None:
    """Dentro la fascia, il rettangolo chiaro della targa (fondo della targa senza carrozzeria attorno).

    Soglia di Otsu sulla luminanza della fascia, chiusura per riempire i
    caratteri, componente chiara piu' grande; None se e' troppo piccola (fascia
    gia' stretta, oppure testo chiaro su fondo scuro).
    """
    gray = _luma8(image)
    x, y, w, h = box
    sub = gray[y:y + h, x:x + w]
    _threshold, mask = cv2.threshold(sub, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (max(3, w // 12) | 1, max(3, h // 6) | 1))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    count, _labels, stats, _centroids = cv2.connectedComponentsWithStats(mask)
    if count < 2:
        return None
    i = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    bx, by, bw, bh = (int(v) for v in stats[i, :4])
    if bw * bh < 0.25 * w * h or (bw >= w - 2 and bh >= h - 2):
        return None
    return x + bx, y + by, bw, bh


def groups(result: fusion.Result) -> list[list[fusion.FrameRecord]]:
    """I fotogrammi usati divisi in gruppi alterni per nitidezza: ogni gruppo ha fotogrammi buoni e meno buoni."""
    used = sorted((r for r in result.alignment.frames if r.used), key=lambda r: r.sharpness, reverse=True)
    count = max(0, min(GROUPS, len(used) // MIN_PER_GROUP))
    if count < 2:
        return []
    return [used[i::count] for i in range(count)]


# ------------------------------------------------------------------ modelli

TANH_LIMIT = 40.0   # tanh(±40) e' gia' ±1 in float32: il Clip davanti al Tanh non cambia il risultato


def _varint(data: bytes, i: int) -> tuple[int, int]:
    shift = value = 0
    while True:
        b = data[i]
        i += 1
        value |= (b & 0x7F) << shift
        if b < 0x80:
            return value, i
        shift += 7


def _encode_varint(value: int) -> bytes:
    out = bytearray()
    while True:
        b, value = value & 0x7F, value >> 7
        out.append(b | 0x80 if value else b)
        if not value:
            return bytes(out)


def _fields(data: bytes) -> list[tuple[int, bytes]]:
    """I campi di un messaggio protobuf: (numero del campo, byte del campo con la sua chiave), in ordine."""
    out, i = [], 0
    while i < len(data):
        start = i
        key, i = _varint(data, i)
        wire = key & 7
        if wire == 0:
            _value, i = _varint(data, i)
        elif wire == 1:
            i += 8
        elif wire == 2:
            length, i = _varint(data, i)
            i += length
        elif wire == 5:
            i += 4
        else:
            raise ValueError(f"protobuf wire type {wire}")
        out.append((key >> 3, data[start:i]))
    return out


def _payload(raw: bytes) -> bytes:
    _key, i = _varint(raw, 0)
    length, i = _varint(raw, i)
    return raw[i:i + length]


def _message(field: int, payload: bytes) -> bytes:
    return _encode_varint(field << 3 | 2) + _encode_varint(len(payload)) + payload


def opencv_safe(model: bytes) -> bytes:
    """Il modello ONNX con un Clip(-40, 40) davanti a ogni Tanh, per il DNN di OpenCV.

    Il Tanh di OpenCV 5.0 passa per l'esponenziale e da' NaN quando l'ingresso
    supera circa 44 in valore assoluto (exp(89) va oltre il float32): con
    fast-plate-ocr succede sulle targhe molto contrastate, e con il modello
    cct-s-v2 su quasi tutte. Siccome tanh(±40) e' gia' ±1 in float32, limitare
    l'ingresso non cambia nulla: le uscite coincidono con onnxruntime. La
    modifica e' fatta in memoria sul protobuf (ModelProto.graph = 7,
    GraphProto.node = 1 e initializer = 5, NodeProto input = 1, output = 2,
    name = 3, op_type = 4; TensorProto data_type = 2, name = 8, raw_data = 9):
    il file scaricato resta quello originale, con la sua impronta.
    """
    out = bytearray()
    for field, raw in _fields(model):
        if field != 7:
            out += raw
            continue
        graph, patched = bytearray(), 0
        for g_field, g_raw in _fields(_payload(raw)):
            node = _fields(_payload(g_raw)) if g_field == 1 else []
            if not any(f == 4 and _payload(r) == b"Tanh" for f, r in node):
                graph += g_raw
                continue
            patched += 1
            source = next(_payload(r) for f, r in node if f == 1)
            clipped = source + b"__opencv_clip"
            graph += _message(1, _message(1, source) + _message(1, b"__opencv_clip_min")
                              + _message(1, b"__opencv_clip_max") + _message(2, clipped) + _message(3, clipped)
                              + _message(4, b"Clip"))
            first = next(i for i, (f, _r) in enumerate(node) if f == 1)
            graph += _message(1, b"".join(_message(1, clipped) if i == first else r for i, (_f, r) in enumerate(node)))
        if patched:
            for name, value in ((b"__opencv_clip_min", -TANH_LIMIT), (b"__opencv_clip_max", TANH_LIMIT)):
                graph += _message(5, _encode_varint(2 << 3) + _encode_varint(1) + _message(8, name)
                                  + _message(9, struct.pack("<f", value)))
        out += _message(7, bytes(graph))
    return bytes(out)


def _load(path) -> cv2.dnn.Net:
    try:
        return cv2.dnn.readNetFromONNX(np.frombuffer(opencv_safe(path.read_bytes()), np.uint8))
    except (cv2.error, OSError, ValueError, IndexError) as exc:
        raise OcrError(tr("Cannot load the OCR model {name}: {error}").format(name=path.name, error=exc)) from exc


def _plate_config(path) -> dict:
    """I campi della configurazione YAML del modello che servono (righe «chiave: valore» e la lista dei paesi)."""
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^\s*#.*$", "", text)

    def value(key: str) -> str:
        match = re.search(rf"(?m)^{key}:\s*(.+?)\s*$", text)
        if match is None:
            raise OcrError(tr("The OCR model configuration {name} is not valid.").format(name=path.name))
        return match.group(1).strip("'\"")

    regions = re.search(r"(?ms)^plate_regions:\s*\[(.*?)\]", text)
    return {"slots": int(value("max_plate_slots")), "alphabet": value("alphabet"), "pad": value("pad_char"),
            "height": int(value("img_height")), "width": int(value("img_width")),
            "gray": value("image_color_mode") == "grayscale",
            "regions": re.findall(r"'([^']*)'", regions.group(1)) if regions else []}


class _PlateNet:
    """fast-plate-ocr: la targa intera ridimensionata a 128 × 64 RGB, 10 posizioni con probabilita' e il paese."""

    def __init__(self) -> None:
        model = tools.PLATE_MODEL
        self.cfg = _plate_config(model.path("cct_s_v2_global_plate_config.yaml"))
        self.net = _load(model.path("cct_s_v2_global.onnx"))
        self.outputs = list(self.net.getUnconnectedOutLayersNames())

    def read(self, image: np.ndarray) -> tuple[str, list[float], np.ndarray | None]:
        """(testo, probabilita' per carattere, probabilita' dei paesi o None) di un'immagine RGB in [0, 1]."""
        cfg = self.cfg
        x = cv2.resize(_rgb8(image), (cfg["width"], cfg["height"]), interpolation=cv2.INTER_LINEAR)
        if cfg["gray"]:
            x = cv2.cvtColor(x, cv2.COLOR_RGB2GRAY)[:, :, None]
        self.net.setInput(x[None])
        outs = dict(zip(self.outputs, self.net.forward(self.outputs)))
        probs = np.asarray(outs.get("plate", next(iter(outs.values())))).reshape(cfg["slots"], len(cfg["alphabet"]))
        if not np.isfinite(probs).all():
            return "", [], None
        chars, conf = [], []
        for slot in probs:
            k = int(np.argmax(slot))
            if cfg["alphabet"][k] != cfg["pad"]:   # il riempimento delle posizioni libere non e' un carattere
                chars.append(cfg["alphabet"][k])
                conf.append(float(slot[k]))
        region = outs.get("region")
        region = None if region is None else np.asarray(region).reshape(-1)
        return "".join(chars), conf, region if region is not None and np.isfinite(region).all() else None


class _TextNets:
    """PP-OCRv6: rilevamento delle righe (mappa di probabilita' DB) e lettura di una riga (CTC), immagini BGR."""

    def __init__(self) -> None:
        model = tools.TEXT_MODEL
        self.det = _load(model.path("PP-OCRv6_det_small.onnx"))
        self.rec = _load(model.path("PP-OCRv6_rec_small.onnx"))
        lines = model.path("ppocrv6_dict.txt").read_bytes().decode("utf-8").split("\n")
        lines = [line.rstrip("\r") for line in lines]
        if lines and lines[-1] == "":
            lines.pop()
        self.characters = ["", *lines, " "]   # 0 = «nessun carattere» del CTC, in fondo lo spazio

    def detect(self, bgr: np.ndarray) -> list[np.ndarray]:
        """Le righe di testo: quadrilateri 4 × 2 (in alto a sinistra, poi in senso orario), dall'alto in basso."""
        h, w = bgr.shape[:2]
        ratio = DET_SIDE / min(h, w) if min(h, w) < DET_SIDE else 1.0
        rh, rw = max(32, int(round(int(h * ratio) / 32)) * 32), max(32, int(round(int(w * ratio) / 32)) * 32)
        img = cv2.resize(bgr, (rw, rh)).astype(np.float32) / 255.0
        self.det.setInput(((img - 0.5) / 0.5).transpose(2, 0, 1)[None])
        pred = np.nan_to_num(np.asarray(self.det.forward()).reshape(rh, rw))
        mask = cv2.dilate((pred > DET_THRESH).astype(np.uint8), np.ones((2, 2), np.uint8))
        contours, _hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        quads = []
        for contour in contours[:1000]:
            (cx, cy), (bw, bh), angle = cv2.minAreaRect(contour)
            if min(bw, bh) < 3:
                continue
            if _box_score(pred, cv2.boxPoints(((cx, cy), (bw, bh), angle))) < DET_BOX_THRESH:
                continue
            # la rete segna il nucleo della riga: si allarga di area × 1,6 / perimetro, come in PaddleOCR, che
            # lo fa con pyclipper in coordinate intere (vertici troncati, arrotondamento alla fine): qui con il
            # rettangolo minimo attorno a cerchi di quel raggio centrati nei vertici troncati
            grow = bw * bh * DET_UNCLIP / (2 * (bw + bh))
            corners = np.trunc(cv2.boxPoints(((cx, cy), (bw, bh), angle)))
            ring = np.stack([np.cos(ARC), np.sin(ARC)], axis=1) * grow
            grown = np.round((corners[:, None, :] + ring[None, :, :]).reshape(-1, 2)).astype(np.float32)
            (cx, cy), (bw, bh), angle = cv2.minAreaRect(grown)
            if min(bw, bh) < 5:
                continue
            quad = cv2.boxPoints(((cx, cy), (bw, bh), angle))
            # vertici in pixel interi dell'immagine, come in PaddleOCR: su righe di poche decine di pixel anche
            # un pixel di differenza nel ritaglio cambia la lettura
            quad = _order(quad)
            quad[:, 0] = np.clip(np.round(quad[:, 0] * w / rw), 0, w)
            quad[:, 1] = np.clip(np.round(quad[:, 1] * h / rh), 0, h)
            quads.append(quad)
        # dall'alto in basso; sulla stessa riga (meno di 10 pixel di differenza), da sinistra a destra
        quads.sort(key=lambda q: (q[0][1], q[0][0]))
        for i in range(len(quads) - 1):
            for j in range(i, -1, -1):
                if abs(quads[j + 1][0][1] - quads[j][0][1]) < 10 and quads[j + 1][0][0] < quads[j][0][0]:
                    quads[j], quads[j + 1] = quads[j + 1], quads[j]
                else:
                    break
        return quads

    def recognize(self, bgr: np.ndarray) -> tuple[str, list[float]]:
        """Testo di una riga e probabilita' di ogni carattere (decodifica CTC: ripetizioni e vuoti tolti)."""
        h, w = bgr.shape[:2]
        if h < 2 or w < 2:
            return "", []
        ratio = w / h
        width = max(REC_MIN_WIDTH, int(REC_HEIGHT * ratio))
        resized = min(width, int(math.ceil(REC_HEIGHT * ratio)))
        img = cv2.resize(bgr, (resized, REC_HEIGHT)).astype(np.float32) / 255.0
        blob = np.zeros((1, 3, REC_HEIGHT, width), np.float32)
        blob[0, :, :, :resized] = ((img - 0.5) / 0.5).transpose(2, 0, 1)
        self.rec.setInput(blob)
        out = np.asarray(self.rec.forward())[0]
        if not np.isfinite(out).all():
            return "", []
        index, prob = out.argmax(axis=1), out.max(axis=1)
        keep = index != 0
        keep[1:] &= index[1:] != index[:-1]
        chars = [self.characters[i] if i < len(self.characters) else "" for i in index[keep]]
        conf = [float(p) for p in prob[keep]]
        while chars and chars[0] == " ":
            chars.pop(0)
            conf.pop(0)
        while chars and chars[-1] == " ":
            chars.pop()
            conf.pop()
        return "".join(chars), conf


def _box_score(pred: np.ndarray, quad: np.ndarray) -> float:
    """Probabilita' media della mappa dentro il quadrilatero."""
    h, w = pred.shape
    x0, x1 = int(np.clip(np.floor(quad[:, 0].min()), 0, w - 1)), int(np.clip(np.ceil(quad[:, 0].max()), 0, w - 1))
    y0, y1 = int(np.clip(np.floor(quad[:, 1].min()), 0, h - 1)), int(np.clip(np.ceil(quad[:, 1].max()), 0, h - 1))
    mask = np.zeros((y1 - y0 + 1, x1 - x0 + 1), np.uint8)
    cv2.fillPoly(mask, [np.round(quad - [x0, y0]).astype(np.int32)], 1)
    return float(cv2.mean(pred[y0:y1 + 1, x0:x1 + 1], mask)[0])


def _order(quad: np.ndarray) -> np.ndarray:
    """Vertici in ordine: in alto a sinistra, in alto a destra, in basso a destra, in basso a sinistra."""
    pts = quad[np.argsort(quad[:, 0])]
    left, right = pts[:2][np.argsort(pts[:2, 1])], pts[2:][np.argsort(pts[2:, 1])]
    return np.array([left[0], right[0], right[1], left[1]], np.float32)


def _warp_line(bgr: np.ndarray, quad: np.ndarray) -> np.ndarray:
    """La riga raddrizzata (prospettiva sul quadrilatero); una riga verticale viene ruotata."""
    width = int(max(np.linalg.norm(quad[0] - quad[1]), np.linalg.norm(quad[2] - quad[3])))
    height = int(max(np.linalg.norm(quad[0] - quad[3]), np.linalg.norm(quad[1] - quad[2])))
    width, height = max(width, 2), max(height, 2)
    target = np.array([[0, 0], [width, 0], [width, height], [0, height]], np.float32)
    line = cv2.warpPerspective(bgr, cv2.getPerspectiveTransform(quad, target), (width, height),
                               flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    if height / width >= 1.5:
        line = np.rot90(line)
    return np.ascontiguousarray(line)


def _bounds(quad: np.ndarray) -> tuple[int, int, int, int]:
    x, y, w, h = cv2.boundingRect(np.round(quad).astype(np.int32))
    return int(x), int(y), int(w), int(h)


# -------------------------------------------------------------------- voto

def _distance(a: str, b: str) -> int:
    """Distanza di Levenshtein."""
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        current = [i]
        for j, cb in enumerate(b, start=1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def combine(readings: list[Reading], families: list[set[str]] = PLATE_CONFUSABLE,
            lookalikes: bool = True) -> tuple[str, float, list[Position]]:
    """Voto per carattere: allinea ogni lettura alla piu' rappresentativa e conta i voti per posizione.

    Ogni carattere vota con il peso della sua lettura per la probabilita' che il
    modello gli da'; un carattere mancante vota «nessun carattere» con la
    probabilita' media della lettura. Con `lookalikes` ogni carattere di una
    famiglia di forme simili viene segnalato (sulle targhe); senza, solo quando
    una forma simile e' il secondo candidato (sulle scritte, dove o, l e s sono
    ovunque).
    """
    valid = [r for r in readings if r.text]
    if not valid:
        return "", 0.0, []
    lengths = sorted(len(r.text) for r in valid)
    median = lengths[len(lengths) // 2]

    def cost(candidate: Reading) -> float:
        # la lettura piu' vicina a tutte le altre, penalizzata se ha una lunghezza diversa dalla tipica
        return (sum(r.weight * _distance(candidate.text, r.text) for r in valid)
                + 0.5 * abs(len(candidate.text) - median) * sum(r.weight for r in valid))

    anchor = min(valid, key=cost).text
    votes: list[dict[str, float]] = [defaultdict(float) for _ in anchor]
    weight_total = sum(r.weight for r in valid) or 1.0
    for reading in valid:
        mean = max(0.05, reading.confidence / 100.0)

        def strength(j: int) -> float:
            p = reading.char_conf[j] if j < len(reading.char_conf) else mean
            return reading.weight * max(0.05, p)

        matcher = difflib.SequenceMatcher(None, anchor, reading.text, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    votes[i1 + k][anchor[i1 + k]] += strength(j1 + k)
            elif tag == "replace":
                for k in range(i2 - i1):
                    j = j1 + k
                    if j < j2:
                        votes[i1 + k][reading.text[j]] += strength(j)
                    else:
                        votes[i1 + k][GAP] += reading.weight * mean
            elif tag == "delete":
                for k in range(i1, i2):
                    votes[k][GAP] += reading.weight * mean
            # "insert": caratteri in piu' rispetto all'ancora, non votano su nessuna posizione
    positions: list[Position] = []
    for box in votes:
        total = sum(box.values()) or 1.0
        ranked = sorted(box.items(), key=lambda kv: kv[1], reverse=True)
        char, top = ranked[0]
        alternatives = [(c, v / total) for c, v in ranked[1:4]]
        confusable = bool(alternatives) and any({char, alternatives[0][0]} <= pair for pair in families)
        similar = ("".join(sorted(set().union(*(pair - {char} for pair in families if char in pair))))
                   if lookalikes else "")
        positions.append(Position(char, top / total, alternatives, confusable, similar,
                                  support=min(1.0, top / weight_total)))
    kept = [p for p in positions if p.char != GAP]
    text = "".join(p.char for p in kept)
    agreement = sum(p.share for p in kept) / len(kept) if kept else 0.0
    return text, agreement, kept


# -------------------------------------------------------------------- lettura

def _sources(result: fusion.Result, cancel: threading.Event | None,
             notes: list[str]) -> list[tuple[str, list[int], np.ndarray, float]]:
    """Il risultato e le fusioni dei gruppi indipendenti: (origine, fotogrammi, immagine RGB, peso)."""
    alignment, params = result.alignment, result.params
    images = [("result", list(result.used), result.final, RESULT_WEIGHT)]
    split = groups(result)
    if not split:
        notes.append(tr("Too few frames for independent groups: only the result was read, without a vote."))
    for n, members in enumerate(split, start=1):
        if cancel is not None and cancel.is_set():
            raise fusion.Cancelled()
        part = fusion.fuse(alignment, params, lambda *_a: None, cancel, frames=members)
        images.append((f"group {n}", sorted(r.index for r in members), part.final, 1.0))
    return images


def _read_plate(images, notes: list[str]) -> CharReading:
    net = _PlateNet()
    final = images[0][2]
    # i ritagli possibili, gli stessi per tutte le immagini: l'area intera e, se si trova, il rettangolo chiaro
    # della targa; il modello vuole la targa intera con poco attorno. Di ogni immagine vale la lettura piu' sicura
    crops: list[tuple[int, int, int, int] | None] = [None]
    band = locate_text(final)
    rect = plate_rect(final, band) if band is not None else None
    if rect is not None:
        crops.append(rect)
    readings: list[Reading] = []
    regions = None
    chosen = None
    for source, frames, image, weight in images:
        options = [(crop, *net.read(_crop(image, crop))) for crop in crops]
        crop, text, conf, region = max(options, key=lambda o: (sum(o[2]) / max(1, len(o[2]))) * math.sqrt(len(o[2])))
        readings.append(Reading(source, frames, text, 100.0 * sum(conf) / max(1, len(conf)), weight, conf))
        if source == "result":
            chosen = crop
        if region is not None:
            regions = weight * region if regions is None else regions + weight * region
    text, agreement, positions = combine(readings, PLATE_CONFUSABLE, lookalikes=True)
    reading = CharReading("plate", [Line(text, agreement, positions, readings, chosen)] if text else [],
                          "fast-plate-ocr cct-s-v2-global", "MIT", notes)
    labels = net.cfg["regions"]
    if regions is not None and len(labels) == regions.size and regions.sum() > 0:
        k = int(np.argmax(regions))
        reading.region, reading.region_share = labels[k], float(regions[k] / regions.sum())
    return reading


def _read_text(images, notes: list[str]) -> CharReading:
    nets = _TextNets()
    pictures = [(source, frames, cv2.cvtColor(_rgb8(image), cv2.COLOR_RGB2BGR), weight)
                for source, frames, image, weight in images]
    quads: list[np.ndarray | None] = list(nets.detect(pictures[0][2]))
    if not quads:
        notes.append(tr("No text line found inside the area: the whole area was read as one line."))
        quads = [None]
    lines: list[Line] = []
    for quad in quads:
        readings = []
        for source, frames, picture, weight in pictures:
            text, conf = nets.recognize(picture if quad is None else _warp_line(picture, quad))
            readings.append(Reading(source, frames, text, 100.0 * sum(conf) / max(1, len(conf)), weight, conf))
        text, agreement, positions = combine(readings, TEXT_CONFUSABLE, lookalikes=False)
        if text:
            lines.append(Line(text, agreement, positions, readings, None if quad is None else _bounds(quad)))
    return CharReading("text", lines, "PaddleOCR PP-OCRv6 small (det + rec)", "Apache-2.0", notes)


def read(result: fusion.Result, cancel: threading.Event | None = None) -> CharReading:
    """Legge il risultato e le fusioni dei gruppi, poi vota carattere per carattere (una votazione per riga)."""
    kind = kind_for(result.params.subject)
    model = tools.TEXT_MODEL if kind == "text" else tools.PLATE_MODEL
    if not model.present:
        raise OcrError(tr("The OCR model for this subject type is missing: download it from the OCR models box of "
                          "the Configuration page."))
    notes: list[str] = []
    images = _sources(result, cancel, notes)
    reading = _read_plate(images, notes) if kind == "plate" else _read_text(images, notes)
    if not reading.lines:
        notes.append(tr("No characters found: draw the area tight around the plate or the text, and check the "
                        "scale and the restoration."))
    return reading
