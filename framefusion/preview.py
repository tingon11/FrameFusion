# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Vista dell'anteprima: fotogramma adattato al riquadro, zoom con la rotellina e trascinamento.

Le coordinate interne sono in pixel del video sorgente: l'immagine ricevuta
puo' essere ridotta (per velocita') e la vista lo sa, cosi' quando si
ingrandisce oltre la sua risoluzione chiede il fotogramma a piena
risoluzione. Si disegna solo la porzione visibile, ritagliata e riscalata:
anche un 4K ingrandito 20 volte resta fluido.

Sull'anteprima si disegna il riquadro del soggetto: trascinando con il tasto
destro, oppure con il sinistro quando draw_mode e' attivo. Due viste possono
essere collegate (on_view + set_view): zoom e spostamento dell'una si
ripetono sull'altra, per confrontare due immagini della stessa misura.
"""

from __future__ import annotations

import tkinter as tk
from typing import Callable

from PIL import Image, ImageTk

from . import theme
from .i18n import tr

MAX_ZOOM = 32.0        # ingrandimento massimo, in pixel schermo per pixel del video
WHEEL_STEP = 1.25      # fattore per ogni scatto di rotellina


class PreviewView(tk.Canvas):
    def __init__(
        self,
        master,
        on_step: Callable[[int], None] | None,
        on_zoom: Callable[[], None],
        on_roi: Callable[[tuple[int, int, int, int]], None] | None = None,
        on_view: Callable[[], None] | None = None,
        placeholder: str = "",
    ) -> None:
        super().__init__(master, bg=theme.PANEL_2, highlightthickness=0, bd=0, cursor="crosshair")
        self._on_step = on_step
        self._on_zoom = on_zoom
        self._on_roi = on_roi
        self._on_view = on_view
        self._image: Image.Image | None = None
        self._source = (1, 1)       # dimensioni del video sorgente
        self._scale = 1.0           # pixel schermo per pixel sorgente
        self._cx = 0.0              # centro della vista, in pixel sorgente
        self._cy = 0.0
        self._fit = True
        self._photo: ImageTk.PhotoImage | None = None
        self._drag: tuple[int, int] | None = None
        self._job: str | None = None
        self.placeholder = placeholder or tr("Open a video to see the preview")
        self.roi: tuple[int, int, int, int] | None = None   # riquadro del soggetto, pixel sorgente
        self.roi_label = ""
        self.draw_mode = False                              # il tasto sinistro disegna il riquadro
        self._roi_drag: tuple[float, float, float, float] | None = None

        self.bind("<Configure>", lambda _e: self._schedule())
        self.bind("<MouseWheel>", self._wheel)
        self.bind("<Control-MouseWheel>", self._wheel)
        self.bind("<Shift-MouseWheel>", self._wheel)
        self.bind("<ButtonPress-1>", self._press)
        self.bind("<B1-Motion>", self._motion)
        self.bind("<ButtonRelease-1>", self._release)
        self.bind("<Double-Button-1>", lambda _e: self.reset())
        if on_roi is not None:
            self.bind("<ButtonPress-3>", self._roi_press)
            self.bind("<B3-Motion>", self._roi_motion)
            self.bind("<ButtonRelease-3>", self._roi_release)

    # ----------------------------------------------------------------- stato

    def set_image(self, image: Image.Image | None, source: tuple[int, int] | None = None) -> None:
        """Nuovo fotogramma; `source` e' la misura reale del video (l'immagine puo' essere ridotta)."""
        self._image = image
        if image is not None:
            self._source = source or image.size
            if self._fit:
                self._fit_now()
        self._schedule()

    def clear(self) -> None:
        self._image = None
        self._fit = True
        self._schedule()

    def set_roi(self, roi: tuple[int, int, int, int] | None, label: str = "") -> None:
        self.roi, self.roi_label = roi, label
        self._schedule()

    @property
    def zoom(self) -> float:
        """Ingrandimento rispetto ai pixel del video (1.0 = un pixel per pixel)."""
        return self._scale

    @property
    def fitted(self) -> bool:
        return self._fit

    def wants_full(self) -> bool:
        """True se l'ingrandimento supera la risoluzione dell'immagine ricevuta."""
        if self._image is None or self._fit:
            return False
        shown = self._image.width / self._source[0]  # frazione della risoluzione reale
        return self._scale > shown

    def reset(self) -> None:
        """Torna al fotogramma intero adattato al riquadro."""
        self._fit = True
        self._fit_now()
        self._schedule()
        self._on_zoom()
        self._view_changed()

    def view(self) -> tuple[float, float, float, bool]:
        """Ingrandimento e centro della vista, per ripeterli su una vista collegata."""
        return self._scale, self._cx, self._cy, self._fit

    def set_view(self, view: tuple[float, float, float, bool]) -> None:
        scale, cx, cy, fit = view
        if fit:
            self._fit = True
        else:
            self._fit, self._scale, self._cx, self._cy = False, scale, cx, cy
            self._clamp()
        self._schedule()

    def _view_changed(self) -> None:
        if self._on_view is not None:
            self._on_view()

    def _fit_now(self) -> None:
        w, h = max(1, self.winfo_width()), max(1, self.winfo_height())
        sw, sh = self._source
        self._scale = min((w - 8) / sw, (h - 8) / sh)
        self._cx, self._cy = sw / 2, sh / 2

    # ---------------------------------------------------------------- eventi

    def _wheel(self, event) -> None:
        if not event.delta:
            return
        ticks = int(event.delta / 120)
        if event.state & 0x0001:  # Shift: scorre i fotogrammi
            if self._on_step is not None:
                self._on_step(-ticks * 10 if event.state & 0x0004 else -ticks)
            return
        if self._image is None:
            return
        self.zoom_at(WHEEL_STEP ** ticks, event.x, event.y)

    def zoom_at(self, factor: float, x: float, y: float) -> None:
        """Ingrandisce di `factor` tenendo fermo il punto dello schermo (x, y)."""
        if self._fit:
            self._fit_now()
        fit_scale = self._fit_scale()
        new = max(fit_scale, min(MAX_ZOOM, self._scale * factor))
        if abs(new - self._scale) < 1e-9:
            return
        # punto sorgente sotto il mouse, da tenere fermo
        sx, sy = self.to_source(x, y)
        w, h = self.winfo_width(), self.winfo_height()
        self._scale = new
        self._cx = sx - (x - w / 2) / new
        self._cy = sy - (y - h / 2) / new
        self._fit = new <= fit_scale + 1e-9
        if self._fit:
            self._fit_now()
        else:
            self._clamp()
        self._schedule()
        self._on_zoom()
        self._view_changed()

    def _fit_scale(self) -> float:
        w, h = max(1, self.winfo_width()), max(1, self.winfo_height())
        sw, sh = self._source
        return min((w - 8) / sw, (h - 8) / sh)

    def _clamp(self) -> None:
        """Il centro resta dentro l'immagine; se la vista e' piu' grande, l'immagine sta al centro."""
        w, h = self.winfo_width(), self.winfo_height()
        sw, sh = self._source
        half_w, half_h = w / 2 / self._scale, h / 2 / self._scale
        if sw <= 2 * half_w:
            self._cx = sw / 2
        else:
            self._cx = min(max(self._cx, half_w), sw - half_w)
        if sh <= 2 * half_h:
            self._cy = sh / 2
        else:
            self._cy = min(max(self._cy, half_h), sh - half_h)

    def _press(self, event) -> None:
        self.focus_set()
        if self.draw_mode and self._on_roi is not None:
            self._roi_press(event)
            return
        if self._image is not None and not self._fit:
            self._drag = (event.x, event.y)
            self.configure(cursor="fleur")

    def _motion(self, event) -> None:
        if self._roi_drag is not None:
            self._roi_motion(event)
            return
        if self._drag is None:
            return
        dx, dy = event.x - self._drag[0], event.y - self._drag[1]
        self._drag = (event.x, event.y)
        self._cx -= dx / self._scale
        self._cy -= dy / self._scale
        self._clamp()
        self._schedule()
        self._view_changed()

    def _release(self, event) -> None:
        if self._roi_drag is not None:
            self._roi_release(event)
            return
        self._drag = None
        self.configure(cursor="crosshair")

    # ------------------------------------------------------- riquadro soggetto

    def to_source(self, x: float, y: float) -> tuple[float, float]:
        """Punto dello schermo -> pixel sorgente."""
        w, h = self.winfo_width(), self.winfo_height()
        return self._cx + (x - w / 2) / self._scale, self._cy + (y - h / 2) / self._scale

    def to_screen(self, sx: float, sy: float) -> tuple[float, float]:
        w, h = self.winfo_width(), self.winfo_height()
        return w / 2 + (sx - self._cx) * self._scale, h / 2 + (sy - self._cy) * self._scale

    def _roi_press(self, event) -> None:
        if self._image is None or self._on_roi is None:
            return
        self.focus_set()
        if self._fit:
            self._fit_now()
        sx, sy = self.to_source(event.x, event.y)
        self._roi_drag = (sx, sy, sx, sy)
        self._schedule()

    def _roi_motion(self, event) -> None:
        if self._roi_drag is None:
            return
        sx, sy = self.to_source(event.x, event.y)
        self._roi_drag = (self._roi_drag[0], self._roi_drag[1], sx, sy)
        self._schedule()

    def _roi_release(self, event) -> None:
        if self._roi_drag is None:
            return
        self._roi_motion(event)
        x0, y0, x1, y1 = self._roi_drag
        self._roi_drag = None
        sw, sh = self._source
        left, right = sorted((max(0.0, min(sw, x0)), max(0.0, min(sw, x1))))
        top, bottom = sorted((max(0.0, min(sh, y0)), max(0.0, min(sh, y1))))
        roi = (int(round(left)), int(round(top)), int(round(right - left)), int(round(bottom - top)))
        self._schedule()
        if roi[2] >= 2 and roi[3] >= 2 and self._on_roi is not None:
            self._on_roi(roi)

    # ---------------------------------------------------------------- disegno

    def _schedule(self) -> None:
        if self._job is None:
            self._job = self.after_idle(self._paint)

    def _paint(self) -> None:
        self._job = None
        self.delete("all")
        w, h = max(1, self.winfo_width()), max(1, self.winfo_height())
        image = self._image
        if image is None:
            self.create_text(w / 2, h / 2, text=self.placeholder, fill=theme.TEXT_FAINT,
                             font=(theme.ui_font(), 11), width=max(120, w - 40), justify="center")
            return
        if self._fit:
            self._fit_now()
        else:
            self._clamp()
        sw, sh = self._source
        k = image.width / sw  # pixel immagine per pixel sorgente (1 se a piena risoluzione)
        # regione visibile in coordinate sorgente, ritagliata all'immagine
        left = max(0.0, self._cx - w / 2 / self._scale)
        top = max(0.0, self._cy - h / 2 / self._scale)
        right = min(float(sw), self._cx + w / 2 / self._scale)
        bottom = min(float(sh), self._cy + h / 2 / self._scale)
        if right <= left or bottom <= top:
            return
        box = (int(left * k), int(top * k), max(int(left * k) + 1, int(right * k + 0.999)),
               max(int(top * k) + 1, int(bottom * k + 0.999)))
        crop = image.crop(box)
        # misura a schermo della porzione ritagliata
        out_w = max(1, int(round((box[2] - box[0]) / k * self._scale)))
        out_h = max(1, int(round((box[3] - box[1]) / k * self._scale)))
        shown = self._scale / k  # fattore tra immagine ricevuta e schermo
        if shown < 1:
            method = Image.LANCZOS
        elif shown <= 3:
            method = Image.BILINEAR
        else:
            method = Image.NEAREST  # oltre 3x si vedono i pixel veri
        if (out_w, out_h) != crop.size:
            crop = crop.resize((out_w, out_h), method)
        self._photo = ImageTk.PhotoImage(crop)
        x = w / 2 + (box[0] / k - self._cx) * self._scale
        y = h / 2 + (box[1] / k - self._cy) * self._scale
        self.create_image(x, y, anchor="nw", image=self._photo)
        self._paint_roi()

    def _paint_roi(self) -> None:
        """Riquadro del soggetto (o quello in corso di disegno), sopra l'immagine."""
        if self._roi_drag is not None:
            x0, y0, x1, y1 = self._roi_drag
            dash, label = (4, 3), ""
        elif self.roi is not None:
            x0, y0 = self.roi[0], self.roi[1]
            x1, y1 = x0 + self.roi[2], y0 + self.roi[3]
            dash, label = (), self.roi_label
        else:
            return
        a, b = self.to_screen(x0, y0)
        c, d = self.to_screen(x1, y1)
        self.create_rectangle(a, b, c, d, outline=theme.BG, width=3)
        self.create_rectangle(a, b, c, d, outline=theme.ROI, width=1, dash=dash)
        if label:
            self.create_text(min(a, c) + 1, min(b, d) - 3, text=label, anchor="sw", fill=theme.ROI,
                             font=(theme.mono_font(), 9, "bold"))
