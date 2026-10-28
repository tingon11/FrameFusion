# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Impostazioni salvate in config.json accanto al programma."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def app_dir() -> Path:
    """Cartella base dell'applicazione: accanto all'eseguibile se impacchettata con PyInstaller.

    In un bundle --onefile __file__ sta in una cartella temporanea che sparisce
    alla chiusura: config.json e tools/ devono invece restare accanto all'exe.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


APP_DIR = app_dir()
CONFIG_FILE = APP_DIR / "config.json"

DEFAULTS: dict[str, Any] = {
    "language": "",           # "" = non ancora scelta: all'avvio la si chiede (inglese finche' non si sceglie)
    "geometry": "",
    "last_video_dir": "",
    "preview_expanded": False,  # anteprima ingrandita, timeline nascosta
    # uscita
    "output_dir": "",
    "subfolder": True,
    "format": "PNG",
    "depth": "Auto",          # Auto = 16 bit per la fusione, la profondita' della sorgente per il singolo fotogramma
    "save_aligned": False,
    # pipeline (vedi fusion.Params)
    "subject": "plate",       # "plate" (targa), "text" (scritta) oppure "face" (volto)
    "motion": "homography",
    "keep": 75,
    "min_quality": 0.80,
    "track_min": 0.50,
    "scale": 2,
    "method": "robust-mean",
    "weight_sharpness": True,
    "equalize": True,
    "denoise": "off",
    "iterations": 20,
    "psf_sigma": 0.0,
    "regularization": "medium",
    "levels": True,
    "local_contrast": "off",
    "grayscale": False,
    # impostazioni salvate con nome: {nome: {chiave: valore, ...}} con le sole chiavi di PARAM_KEYS
    "presets": {},
    "preset": "",             # nome dell'ultima impostazione caricata
}
# le chiavi della pipeline: quelle che «Predefiniti» riporta ai valori di DEFAULTS (vedi defaults_for)
PARAM_KEYS = ("subject", "motion", "keep", "min_quality", "track_min", "scale", "method", "weight_sharpness",
              "equalize", "denoise", "iterations", "psf_sigma", "regularization", "levels", "local_contrast",
              "grayscale")
# cio' che cambia nei predefiniti con il tipo di soggetto: per i volti il modello di moto e' affine
# (su un volto di poche decine di pixel l'omografia si piega per far salire la correlazione: la
# prospettiva non e' un moto reale della testa) e il restauro e' piu' leggero (meno iterazioni,
# regolarizzazione forte, un po' di riduzione del rumore), perche' la deconvoluzione spinta produce
# aloni e un effetto «plastica» sulla pelle; CLAHE e scala di grigi restano spenti
SUBJECT_DEFAULTS: dict[str, dict[str, Any]] = {
    "plate": {},
    "text": {},
    "face": {"motion": "affine", "denoise": "light", "iterations": 10, "regularization": "strong"},
}


def _preset(subject: str, description: str, **changes: Any) -> dict[str, Any]:
    values = defaults_for(subject)
    values.update(changes)
    values["description"] = description
    return values


def builtin_presets() -> dict[str, dict[str, Any]]:
    """I preset di serie, sempre presenti e non modificabili: cinque per tipo di soggetto (targa, testo, volto).

    Ognuno parte dai predefiniti del suo tipo di soggetto e cambia solo cio' che
    serve al caso; i valori sono tra quelli dei menu. La descrizione e' un testo
    inglese, tradotto al momento dell'uso (N_ in i18n).
    """
    from .i18n import N_

    return {
        "Plate 01": _preset("plate", N_("Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate "
                                        "deconvolution. The starting point.")),
        "Plate 02": _preset("plate", N_("Plate at night or noisy: more frames, medium noise reduction, gentler "
                                        "deconvolution with strong regularization, light local contrast, grayscale."),
                            keep=90, denoise="medium", iterations=15, regularization="strong",
                            local_contrast="light", grayscale=True),
        "Plate 03": _preset("plate", N_("Distant, small plate filmed in many frames: ×3, shift-and-add, almost all "
                                        "frames, lower alignment threshold."),
                            scale=3, method="shift-and-add", keep=90, min_quality=0.70, denoise="light"),
        "Plate 04": _preset("plate", N_("Moving or approaching vehicle with motion blur: only the sharpest half of "
                                        "the frames, more tolerant subject search, stronger deconvolution."),
                            keep=50, track_min=0.40, iterations=30, regularization="medium"),
        "Plate 05": _preset("plate", N_("Plate in shadow or against the light: medium local contrast, grayscale, "
                                        "light noise reduction."),
                            local_contrast="medium", grayscale=True, denoise="light", iterations=15),
        "Text 01": _preset("text", N_("Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate "
                                      "deconvolution. The starting point.")),
        "Text 02": _preset("text", N_("Text at night or noisy: more frames, medium noise reduction, gentler "
                                      "deconvolution with strong regularization, light local contrast, grayscale."),
                           keep=90, denoise="medium", iterations=15, regularization="strong",
                           local_contrast="light", grayscale=True),
        "Text 03": _preset("text", N_("Distant, small text filmed in many frames: ×3, shift-and-add, almost all "
                                      "frames, lower alignment threshold."),
                           scale=3, method="shift-and-add", keep=90, min_quality=0.70, denoise="light"),
        "Text 04": _preset("text", N_("Text on a moving vehicle or filmed by a moving camera, with motion blur: only "
                                      "the sharpest half of the frames, more tolerant subject search, stronger "
                                      "deconvolution."),
                           keep=50, track_min=0.40, iterations=30, regularization="medium"),
        "Text 05": _preset("text", N_("Text in shadow or against the light: medium local contrast, grayscale, light "
                                      "noise reduction."),
                           local_contrast="medium", grayscale=True, denoise="light", iterations=15),
        "Face 01": _preset("face", N_("Face, standard: affine, local refinement, light noise reduction, gentle "
                                      "deconvolution with strong regularization. The starting point.")),
        "Face 02": _preset("face", N_("Face at night or noisy: more frames, medium noise reduction, very light "
                                      "deconvolution."),
                           keep=90, denoise="medium", iterations=5),
        "Face 03": _preset("face", N_("Face, minimal processing: fusion with auto levels only, no noise reduction "
                                      "and no deconvolution. The most conservative result."),
                           denoise="off", iterations=0),
        "Face 04": _preset("face", N_("Distant, small face: ×3, almost all frames, lower alignment threshold."),
                           scale=3, keep=90, min_quality=0.70),
        "Face 05": _preset("face", N_("Face in shadow or against the light: light local contrast, gentle "
                                      "deconvolution."),
                           local_contrast="light", iterations=5),
    }


def defaults_for(subject: str) -> dict[str, Any]:
    """I parametri predefiniti della pipeline per un tipo di soggetto (chiavi di PARAM_KEYS)."""
    if subject not in SUBJECT_DEFAULTS:
        subject = DEFAULTS["subject"]
    values = {key: DEFAULTS[key] for key in PARAM_KEYS}
    values.update(SUBJECT_DEFAULTS[subject])
    values["subject"] = subject
    return values


class Config:
    def __init__(self) -> None:
        self._data = dict(DEFAULTS)
        try:
            loaded = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                self._data.update({k: v for k, v in loaded.items() if k in DEFAULTS})
        except (OSError, ValueError):
            pass

    def get(self, key: str) -> Any:
        return self._data.get(key, DEFAULTS.get(key))

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def save(self) -> None:
        try:
            CONFIG_FILE.write_text(json.dumps(self._data, indent=2, ensure_ascii=False),
                                   encoding="utf-8")
        except OSError:
            pass
