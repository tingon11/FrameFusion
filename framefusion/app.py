# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Finestra principale di FrameFusion.

Tre pagine: Configurazione (sorgente, uscita, ffmpeg, lingua, crediti),
Soggetto (anteprima, timeline, riquadro del soggetto sul fotogramma di
riferimento) e Fusione (parametri, confronto prima/dopo, i sette passaggi
della pipeline, salvataggio con rapporto).

I testi dell'interfaccia sono in inglese nel codice e passano da tr(): la
traduzioni stanno nei moduli di locales/ e si applicano a programma aperto.
"""

from __future__ import annotations

import datetime as dt
import os
import threading
import time
import tkinter as tk
import webbrowser
from collections import OrderedDict
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk
import numpy as np
from PIL import Image

from . import APP_NAME, CREDITS, __version__, ffmpeg, frameless, fusion, i18n, procs, report, shell, theme, tools
from .config import DEFAULTS, PARAM_KEYS, Config
from .ffmpeg import Cancelled, VideoInfo
from .i18n import N_, tr
from .preview import PreviewView
from .tasks import Tasks
from .timeline import Thumbnails, Timeline, format_time, parse_time
from .widgets import (Card, Choice, LanguageSwitch, Tooltip, askstring, button, caption, follow_width, icon_button,
                      link, messagebox, note, retranslate_all, rule)

DEFAULT_SIZE = "1360x920"
MIN_SIZE = (1100, 780)
PAGE_HEADER_ABOVE = 880   # altezza finestra sopra cui si mostra il titolo della pagina
LOG_ABOVE = 960           # altezza finestra sopra cui si mostra il registro
NAME_MAX = 36             # caratteri del nome del video nell'intestazione
PREVIEW_MAX_WIDTH = 1600   # larghezza massima dell'anteprima chiesta a ffmpeg
PREVIEW_DELAY_MS = 40      # attesa prima di chiedere l'anteprima, mentre si trascina
PREVIEW_LOOKAHEAD = 8      # fotogrammi decodificati in un colpo quando si avanza di uno alla volta
PREVIEW_CACHE_BYTES = 192 * 1024 * 1024   # memoria per i fotogrammi gia' decodificati
LOG_MAX = 400
COLLAPSE_BELOW = 1220     # larghezza finestra sotto cui la barra laterale si comprime
AUTO_RANGE = 30           # fotogrammi per parte attorno al riferimento, se l'intervallo e' tutto il video
PROGRESS_EVERY = 0.06     # secondi tra due aggiornamenti dell'avanzamento della pipeline

# chiave, etichetta, glifo (Segoe Fluent Icons), titolo della pagina
PAGES: tuple[tuple[str, str, str, str], ...] = (
    ("setup", N_("Configuration"), "", ""),
    ("work", N_("Subject"), "", N_("Frames, subject and reference")),
    ("result", N_("Fusion"), "", N_("Multi-frame fusion and result")),
)

# glifi di Segoe Fluent Icons / MDL2
GLYPH_MINIMIZE = ""
GLYPH_MAXIMIZE = ""
GLYPH_RESTORE = ""
GLYPH_CLOSE = ""
GLYPH_FIRST = ""
GLYPH_LAST = ""
GLYPH_PREV = ""
GLYPH_NEXT = ""
GLYPH_ZOOM_IN = ""
GLYPH_ZOOM_OUT = ""
GLYPH_FOLDER = ""

# voci dei menu dei parametri: chiave -> etichetta
KEEP = {str(v): f"{v} %" for v in (100, 90, 75, 50, 25)}
QUALITY = {f"{v:.2f}": f"{v:.2f}" for v in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95)}
TRACK = {f"{v:.2f}": f"{v:.2f}" for v in (0.3, 0.4, 0.5, 0.6, 0.7)}
SCALES = {str(v): f"× {v}" for v in (1, 2, 3, 4)}
ITERATIONS = {str(v): str(v) if v else N_("0 (none)") for v in (0, 5, 10, 15, 20, 30, 50)}
PSF = {"0": N_("Automatic"), **{f"{v:.1f}": f"{v:.1f} px" for v in (0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0)}}
VIEWS = {"final": N_("Final"), "fused": N_("Fusion only")}
LEFT_VIEWS = {"ghost": N_("Ghost of the frames"), "reference": N_("Reference frame")}
NO_PRESET = N_("(none saved)")   # voce del menu delle impostazioni salvate quando non ce ne sono

# stato dei passaggi della pipeline: colore del pallino
STEP_COLORS = {"pending": theme.TEXT_FAINT, "running": theme.ACCENT, "done": theme.OK,
               "reused": theme.TEXT_DIM, "error": theme.ERR}


class App(ctk.CTk):
    """Finestra unica: intestazione, barra laterale e tre pagine."""

    def __init__(self, video: str | None = None) -> None:
        self.config_store = Config()
        i18n.set_language(self.config_store.get("language"))
        theme.apply()
        super().__init__()

        self.title(APP_NAME)
        self.minsize(*MIN_SIZE)
        try:
            self.geometry(str(self.config_store.get("geometry")) or DEFAULT_SIZE)
        except tk.TclError:
            self.geometry(DEFAULT_SIZE)
        theme.set_icon(self)
        # senza barra del titolo di sistema: l'intestazione fa da barra
        self.frameless = frameless.make_frameless(self, border_color=theme.BORDER)

        self.fonts = theme.Fonts()
        self.tasks = Tasks(self, on_crash=lambda exc: self.error(tr("Operation failed"), exc),
                           on_bug=self._bug)
        self.thumbs = Thumbnails(post=lambda fn: self.tasks.post(fn))

        self.info: VideoInfo | None = None
        self.log_lines: list[str] = []
        self._installing: threading.Event | None = None
        self._pending_video: Path | None = None   # video da aprire appena ffmpeg e' disponibile
        self._preview_image = None      # PIL, fotogramma mostrato
        self._preview_frame = -1
        self._preview_wanted = 0
        self._preview_gen = 0
        self._preview_job: str | None = None
        self._preview_full = False       # l'immagine mostrata e' a piena risoluzione
        self._preview_last = -1          # ultimo fotogramma chiesto: dice in che verso si naviga
        self._preview_dir = 0
        self._inflight: object | None = None   # marcatore del lotto in decodifica
        self._frames: OrderedDict[tuple[int, int], object] = OrderedDict()  # (fotogramma, larghezza) -> PIL
        self._frames_bytes = 0
        self._busy_shown = False
        self._layout_job: str | None = None
        self.pages: dict[str, ctk.CTkFrame] = {}
        self._page_key = ""

        # soggetto e pipeline
        self.roi: tuple[int, int, int, int] | None = None
        self.ref: int | None = None
        self._rerun = False              # un'area nuova e' stata disegnata mentre la fusione girava
        self._alignment: fusion.Alignment | None = None
        self._alignment_key: tuple | None = None
        self._result: fusion.Result | None = None
        self._running: threading.Event | None = None
        self._saving = False
        self._run_started = 0.0
        self._last_folder: Path | None = None
        self._step_state: list[str] = ["pending"] * len(fusion.STEPS)

        self._build()
        self._bind_keys()
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.bind("<Configure>", self._on_configure, add="+")
        self.after(150, self._busy_tick)
        self.after(60, lambda: self._startup(video))

    # ------------------------------------------------------------ costruzione

    def _build(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self._build_header()
        rule(self, horizontal=True).grid(row=1, column=0, sticky="ew")

        body = ctk.CTkFrame(self, fg_color=theme.BG, corner_radius=0)
        body.grid(row=2, column=0, sticky="nsew")
        body.grid_columnconfigure(2, weight=1)
        body.grid_rowconfigure(0, weight=1)

        self.rail = shell.NavRail(
            body, self.fonts, [(key, tr(label), glyph) for key, label, glyph, _t in PAGES],
            on_select=self.show_page,
        )
        self.rail.grid(row=0, column=0, sticky="ns")
        rule(body, horizontal=False).grid(row=0, column=1, sticky="ns")

        main = ctk.CTkFrame(body, fg_color=theme.BG, corner_radius=0)
        main.grid(row=0, column=2, sticky="nsew")
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(1, weight=1)

        head = self.page_head = ctk.CTkFrame(main, fg_color="transparent", corner_radius=0)
        head.grid(row=0, column=0, sticky="ew", padx=22, pady=(12, 0))
        self.crumb_label = ctk.CTkLabel(head, text="", anchor="w", font=self.fonts.caption,
                                        text_color=theme.TEXT_FAINT, height=14)
        self.crumb_label.pack(anchor="w")
        self.title_label = ctk.CTkLabel(head, text="", anchor="w", font=self.fonts.page,
                                        text_color=theme.TEXT)
        self.title_label.pack(anchor="w")

        content = ctk.CTkFrame(main, fg_color="transparent", corner_radius=0)
        content.grid(row=1, column=0, sticky="nsew", padx=14, pady=(10, 12))
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)

        # pagina Soggetto: anteprima (si allarga), timeline, riquadro del soggetto
        work = self.pages["work"] = ctk.CTkFrame(content, fg_color="transparent", corner_radius=0)
        work.grid(row=0, column=0, sticky="nsew")
        work.grid_columnconfigure(0, weight=1)
        work.grid_rowconfigure(0, weight=1)
        self._build_preview(work)
        self._build_timeline(work)
        self._build_subject(work)

        # pagina Fusione: parametri a sinistra, confronto e pipeline a destra
        result = self.pages["result"] = ctk.CTkFrame(content, fg_color="transparent", corner_radius=0)
        result.grid(row=0, column=0, sticky="nsew")
        result.grid_columnconfigure(1, weight=1)
        result.grid_rowconfigure(0, weight=1)
        self._build_parameters(result)
        right = ctk.CTkFrame(result, fg_color="transparent", corner_radius=0)
        right.grid(row=0, column=1, sticky="nsew", padx=(theme.GAP, 0))
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(0, weight=1)
        self._build_compare(right)
        self._build_pipeline(right)

        # pagina Configurazione: sorgente, uscita, ffmpeg, lingua, crediti
        setup = self.pages["setup"] = ctk.CTkFrame(content, fg_color="transparent", corner_radius=0)
        setup.grid(row=0, column=0, sticky="nsew")
        setup.grid_columnconfigure(0, weight=1)
        self._build_source(setup)
        self._build_output(setup)
        self._build_tools(setup)
        self._build_language(setup)
        self._build_credits(setup)
        work.grid_remove()
        result.grid_remove()

        rule(self, horizontal=True).grid(row=3, column=0, sticky="ew")
        self._build_footer()
        self.show_page(PAGES[0][0])

    def show_page(self, key: str) -> None:
        if key == self._page_key:
            return
        for page_key, page in self.pages.items():
            if page_key == key:
                page.grid()
            else:
                page.grid_remove()
        self.rail.select(key)
        self._page_key = key
        self._paint_page_head()
        self.focus_set()

    def _paint_page_head(self) -> None:
        index = next(i for i, entry in enumerate(PAGES, start=1) if entry[0] == self._page_key)
        self.crumb_label.configure(
            text=tr("{app}  /  PAGE {index:02d}").format(app=APP_NAME.upper(), index=index))
        title = PAGES[index - 1][3]
        if title:
            self.title_label.configure(text=tr(title))
            self.title_label.pack(anchor="w")
        else:
            self.title_label.pack_forget()

    def _build_header(self) -> None:
        """Intestazione: logo, video aperto, stato. Fa anche da barra del titolo."""
        header = ctk.CTkFrame(self, fg_color=theme.BG, corner_radius=0, height=50)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(2, weight=1)
        header.grid_rowconfigure(0, weight=1)

        brand = ctk.CTkFrame(header, fg_color="transparent")
        brand.grid(row=0, column=0, sticky="w", padx=(18, 0))
        logo = theme.logo(17)
        if logo is not None:
            name = ctk.CTkLabel(brand, text="", image=logo)
        else:
            name = ctk.CTkLabel(brand, text=APP_NAME.upper(), font=(theme.mono_font(), 15, "bold"))
        name.pack(side="left")
        version = ctk.CTkLabel(brand, text=f"   v{__version__}", font=(theme.mono_font(), 10),
                               text_color=theme.TEXT_DIM)
        version.pack(side="left", pady=(3, 0))
        subtitle = ctk.CTkLabel(brand, text="  ·  multi-frame fusion", font=(theme.mono_font(), 10),
                                text_color=theme.TEXT_FAINT)
        subtitle.pack(side="left", pady=(3, 0))

        chip = ctk.CTkFrame(header, fg_color=theme.PANEL, corner_radius=4, border_width=1,
                            border_color=theme.BORDER, height=32)
        chip.grid(row=0, column=1, sticky="w", padx=(20, 0))
        tag = ctk.CTkLabel(chip, text="VIDEO", font=self.fonts.caption, text_color=theme.TEXT_FAINT)
        tag.pack(side="left", padx=(10, 6), pady=2)
        self.video_label = ctk.CTkLabel(chip, text=tr("none"), font=self.fonts.bold,
                                        text_color=theme.TEXT_DIM, anchor="w", width=240)
        self.video_label.pack(side="left", padx=(0, 4), pady=3)
        open_button = ctk.CTkButton(
            chip, text=GLYPH_FOLDER if theme.icon_font() else "…", width=28, height=24, corner_radius=4,
            fg_color="transparent", hover_color=theme.HOVER, text_color=theme.TEXT_DIM,
            font=self.fonts.icon(12), command=self.open_video,
        )
        open_button.pack(side="left", padx=(0, 4))
        Tooltip(open_button, tr("Open video… (Ctrl+O)"), self.fonts)

        spacer = ctk.CTkFrame(header, fg_color="transparent", height=1)
        spacer.grid(row=0, column=2, sticky="ew")

        right = ctk.CTkFrame(header, fg_color="transparent")
        right.grid(row=0, column=3, sticky="e", padx=(0, 12))
        self.state_dot = ctk.CTkLabel(right, text="●", font=(theme.mono_font(), 12),
                                      text_color=theme.TEXT_FAINT)
        self.state_dot.pack(side="left", padx=(0, 6))
        self.state_label = ctk.CTkLabel(right, text=tr("No video"), font=self.fonts.bold,
                                        text_color=theme.TEXT_SOFT)
        self.state_label.pack(side="left")

        if self.frameless:
            self._window_buttons(header).grid(row=0, column=4, sticky="ne", padx=(4, 0))
            for widget in (header, brand, name, version, subtitle, spacer, right, tag, chip,
                           self.video_label, self.state_dot, self.state_label):
                frameless.enable_drag(self, widget)

    def _window_buttons(self, master) -> ctk.CTkFrame:
        """Riduci / massimizza / chiudi, disegnati nell'intestazione (finestra senza barra)."""
        family = theme.icon_font()
        glyphs = (GLYPH_MINIMIZE, GLYPH_MAXIMIZE, GLYPH_CLOSE) if family else ("—", "□", "✕")
        restore = GLYPH_RESTORE if family else "❐"
        font = ctk.CTkFont(family=family or theme.ui_font(), size=10 if family else 13)
        box = ctk.CTkFrame(master, fg_color="transparent", corner_radius=0)
        buttons = []
        for glyph, command, hover in (
            (glyphs[0], self.iconify, theme.HOVER),
            (glyphs[1], lambda: frameless.toggle_maximize(self), theme.HOVER),
            (glyphs[2], self._on_close, theme.CLOSE_HOVER),
        ):
            item = ctk.CTkButton(
                box, text=glyph, command=command, width=46, height=34, corner_radius=0,
                fg_color="transparent", hover_color=hover, text_color=theme.TEXT_DIM, font=font,
            )
            item.pack(side="left")
            buttons.append(item)

        def sync(event=None) -> None:
            if event is not None and event.widget is not self:
                return
            try:
                glyph = restore if self.state() == "zoomed" else glyphs[1]
                if buttons[1].winfo_exists() and buttons[1].cget("text") != glyph:
                    buttons[1].configure(text=glyph)
            except tk.TclError:
                pass

        self.bind("<Configure>", sync, add="+")
        sync()
        return box

    # ------------------------------------------------------- pagina Soggetto

    def _build_preview(self, parent) -> None:
        card = Card(parent, tr("Preview"), self.fonts)
        card.grid(row=0, column=0, sticky="nsew")
        self.preview_info = ctk.CTkLabel(card.head_right, text="", font=self.fonts.tiny,
                                         text_color=theme.TEXT_FAINT)
        self.preview_info.pack(side="right")
        ctk.CTkLabel(card.head_right,
                     text=tr("right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit"),
                     font=self.fonts.tiny, text_color=theme.TEXT_FAINT).pack(side="right", padx=(0, 16))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        body.grid_rowconfigure(0, weight=1)

        self.preview = PreviewView(body, on_step=self.step, on_zoom=self._on_zoom, on_roi=self._roi_drawn)
        self.preview.configure(width=480, height=270)
        self.preview.grid(row=0, column=0, sticky="nsew")

        bar = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        bar.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        bar.grid_columnconfigure(2, weight=1)

        nav = ctk.CTkFrame(bar, fg_color="transparent", corner_radius=0)
        nav.grid(row=0, column=0, sticky="w")
        f = self.fonts
        for column, (glyph, fallback, delta, tip) in enumerate((
            (GLYPH_FIRST, "|◀", "first", N_("First frame (Home)")),
            ("", "-10", -10, N_("Back 10 frames (Shift+←)")),
            (GLYPH_PREV, "◀", -1, N_("Previous frame (←)")),
            (GLYPH_NEXT, "▶", 1, N_("Next frame (→)")),
            ("", "+10", 10, N_("Forward 10 frames (Shift+→)")),
            (GLYPH_LAST, "▶|", "last", N_("Last frame (End)")),
        )):
            if delta == "first":
                command = lambda: self.goto(0)
            elif delta == "last":
                command = lambda: self.goto(self.info.frames - 1 if self.info else 0)
            else:
                command = lambda d=delta: self.step(d)
            if glyph:
                item = icon_button(nav, glyph, fallback, command, f, width=36, tooltip=tr(tip))
            else:
                item = button(nav, fallback, command, width=40, font=f.mono)
                Tooltip(item, tr(tip), f)
            item.grid(row=0, column=column, padx=(0, 3))

        clock = ctk.CTkFrame(bar, fg_color="transparent", corner_radius=0)
        clock.grid(row=0, column=1, sticky="w", padx=(14, 0))
        self.time_label = ctk.CTkLabel(clock, text="00:00.000", font=f.mono_big,
                                       text_color=theme.ACCENT, anchor="w")
        self.time_label.pack(side="left")
        self.frame_label = ctk.CTkLabel(clock, text="", font=f.tiny, text_color=theme.TEXT_DIM,
                                        anchor="w")
        self.frame_label.pack(side="left", padx=(8, 0), pady=(4, 0))

        self.save_button = button(bar, tr("Save frame"), self.save_frame, width=140)
        self.save_button.grid(row=0, column=3, sticky="e")
        Tooltip(self.save_button, tr("Save the shown frame at full resolution, lossless (Ctrl+S)"), f)

    def _build_timeline(self, parent) -> None:
        card = Card(parent, "Timeline", self.fonts)
        card.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        ctk.CTkLabel(card.head_right,
                     text=tr("Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  "
                             "double-click the ruler: all"),
                     font=self.fonts.tiny, text_color=theme.TEXT_FAINT).pack(side="right")
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        f = self.fonts

        bar = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        bar.grid(row=0, column=0, sticky="ew", pady=(0, theme.GAP))
        bar.grid_columnconfigure(3, weight=1)

        self.in_button = button(bar, tr("In  [I]"), lambda: self.mark("in"), width=92,
                                fg_color=theme.NEUTRAL, text_color=theme.MARK_IN)
        self.in_button.grid(row=0, column=0, padx=(0, 3))
        Tooltip(self.in_button, tr("Sets the start of the selection at the cursor (key I)"), f)
        self.out_button = button(bar, tr("Out  [O]"), lambda: self.mark("out"), width=92,
                                 fg_color=theme.NEUTRAL, text_color=theme.MARK_OUT)
        self.out_button.grid(row=0, column=1, padx=(0, 14))
        Tooltip(self.out_button, tr("Sets the end of the selection at the cursor (key O)"), f)

        fields = ctk.CTkFrame(bar, fg_color="transparent", corner_radius=0)
        fields.grid(row=0, column=2, sticky="w")
        ctk.CTkLabel(fields, text="IN", font=f.caption, text_color=theme.MARK_IN).pack(side="left", padx=(0, 6))
        self.in_entry = ctk.CTkEntry(fields, width=100, height=28, font=f.mono)
        self.in_entry.pack(side="left")
        self._bind_time_entry(self.in_entry, lambda frame: self.timeline.set_in(frame))
        in_go = button(fields, "→", lambda: self.goto(self.timeline.in_f), width=28, height=28)
        in_go.pack(side="left", padx=(3, 12))
        Tooltip(in_go, tr("Moves the cursor to the start of the selection"), f)
        ctk.CTkLabel(fields, text="OUT", font=f.caption, text_color=theme.MARK_OUT).pack(side="left", padx=(0, 6))
        self.out_entry = ctk.CTkEntry(fields, width=100, height=28, font=f.mono)
        self.out_entry.pack(side="left")
        self._bind_time_entry(self.out_entry, lambda frame: self.timeline.set_out(frame))
        out_go = button(fields, "→", lambda: self.goto(self.timeline.out_f), width=28, height=28)
        out_go.pack(side="left", padx=(3, 12))
        Tooltip(out_go, tr("Moves the cursor to the end of the selection"), f)
        ctk.CTkLabel(fields, text=tr("CURSOR"), font=f.caption, text_color=theme.ACCENT).pack(
            side="left", padx=(0, 6))
        self.cursor_entry = ctk.CTkEntry(fields, width=100, height=28, font=f.mono)
        self.cursor_entry.pack(side="left")
        self._bind_time_entry(self.cursor_entry, self.goto)
        Tooltip(self.cursor_entry, tr("Time (1:23.456, 83.4) or frame (f2000), then Enter"), f)

        zoom = ctk.CTkFrame(bar, fg_color="transparent", corner_radius=0)
        zoom.grid(row=0, column=4, sticky="e")
        icon_button(zoom, GLYPH_ZOOM_OUT, "−", lambda: self.timeline.zoom(1 / 1.6), f,
                    tooltip=tr("Zoom out (−)")).pack(side="left", padx=(0, 3))
        icon_button(zoom, GLYPH_ZOOM_IN, "+", lambda: self.timeline.zoom(1.6), f,
                    tooltip=tr("Zoom in (+)")).pack(side="left", padx=(0, 3))
        button(zoom, tr("All"), lambda: self.timeline.zoom_fit(), width=56).pack(side="left", padx=(0, 3))
        button(zoom, tr("Selection"), lambda: self.timeline.zoom_selection(), width=76).pack(side="left")

        self.timeline = Timeline(body, f, self.thumbs, on_playhead=self._on_playhead,
                                 on_range=self._on_range, on_view=self._on_view)
        self.timeline.grid(row=1, column=0, sticky="ew")
        foot = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        foot.grid(row=2, column=0, sticky="ew", pady=(4, 0))
        foot.grid_columnconfigure(0, weight=1)
        self.selection_label = ctk.CTkLabel(foot, text="", font=f.small, text_color=theme.TEXT_DIM,
                                            anchor="w")
        self.selection_label.grid(row=0, column=0, sticky="ew")
        self.view_label = ctk.CTkLabel(foot, text="", font=f.tiny, text_color=theme.TEXT_FAINT, anchor="e")
        self.view_label.grid(row=0, column=1, sticky="e")

    def _build_subject(self, parent) -> None:
        """Riquadro del soggetto sul fotogramma di riferimento e avvio della fusione."""
        card = Card(parent, tr("Subject"), self.fonts)
        card.grid(row=2, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(5, weight=1)
        f = self.fonts

        self.draw_button = button(body, tr("Select area"), self._toggle_draw, width=120)
        self.draw_button.grid(row=0, column=0, padx=(0, 3))
        Tooltip(self.draw_button, tr("Then drag on the preview to frame the subject (or right-drag at any time); "
                                     "the fusion starts by itself"), f)
        go_ref = button(body, "→ R", lambda: self.goto(self.ref) if self.ref is not None else None, width=44)
        go_ref.grid(row=0, column=3, padx=(0, 3))
        Tooltip(go_ref, tr("Moves the cursor to the reference frame"), f)
        clear = button(body, tr("Clear"), self.clear_subject, width=70)
        clear.grid(row=0, column=4, padx=(0, 12))

        self.subject_label = ctk.CTkLabel(body, text=tr("Frame the subject on a clear frame: that frame becomes "
                                                        "the reference and the fusion starts."),
                                          font=f.small, text_color=theme.TEXT_DIM, anchor="w", justify="left")
        self.subject_label.grid(row=0, column=5, sticky="ew")
        follow_width(self.subject_label, body, margin=640)

        self.fuse_button = button(body, tr("Fuse frames  →"), self.run_fusion, primary=True, width=160)
        self.fuse_button.grid(row=0, column=6, padx=(theme.GAP, 0))
        Tooltip(self.fuse_button, tr("Runs the multi-frame fusion on the selected range (F5)"), f)

    # -------------------------------------------------------- pagina Fusione

    def _build_parameters(self, parent) -> None:
        """Colonna dei parametri, divisa per passaggi: allineamento, fusione, restauro, presentazione."""
        config = self.config_store
        f = self.fonts
        column = ctk.CTkScrollableFrame(parent, fg_color="transparent", corner_radius=0, width=290)
        column.grid(row=0, column=0, sticky="nsw")
        column.grid_columnconfigure(0, weight=1)
        self.params_column = column

        def field(body, row: int, title: str, widget) -> None:
            caption(body, tr(title), f).grid(row=row * 2, column=0, sticky="w", pady=(0 if row == 0 else theme.GAP, 2))
            widget.grid(row=row * 2 + 1, column=0, sticky="ew")

        # ---- impostazioni salvate con nome
        card = Card(column, tr("Saved settings"), f)
        card.grid(row=0, column=0, sticky="ew")
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        self.preset_menu = Choice(body, {"": NO_PRESET}, "", f, command=self.load_preset)
        self.preset_menu.grid(row=0, column=0, columnspan=2, sticky="ew")
        self._fill_presets(str(config.get("preset")))
        self.preset_save_button = button(body, tr("Save…"), self.save_preset, width=100)
        self.preset_save_button.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0), padx=(0, 3))
        Tooltip(self.preset_save_button, tr("Saves the current parameters under a name (in config.json)"), f)
        self.preset_delete_button = button(body, tr("Delete"), self.delete_preset, width=100, danger=True)
        self.preset_delete_button.grid(row=1, column=1, sticky="ew", pady=(theme.GAP, 0), padx=(3, 0))
        report_button = button(body, tr("From report…"), self.load_from_report, width=100)
        report_button.grid(row=2, column=0, sticky="ew", pady=(6, 0), padx=(0, 3))
        Tooltip(report_button, tr("Loads the parameters written in the report.json of a saved fusion"), f)
        self.reset_button = button(body, tr("Defaults"), self.reset_params, width=100)
        self.reset_button.grid(row=2, column=1, sticky="ew", pady=(6, 0), padx=(3, 0))
        Tooltip(self.reset_button, tr("Puts every parameter of the pipeline back to its default value"), f)

        # ---- passaggi 1-4
        card = Card(column, tr("Frames and alignment"), f)
        card.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        self.motion_menu = Choice(body, fusion.MOTION_LABELS, str(config.get("motion")), f)
        field(body, 0, N_("Motion model"), self.motion_menu)
        self.track_menu = Choice(body, TRACK, f"{float(config.get('track_min')):.2f}", f)
        field(body, 1, N_("Subject search: minimum correlation"), self.track_menu)
        self.quality_menu = Choice(body, QUALITY, f"{float(config.get('min_quality')):.2f}", f)
        field(body, 2, N_("Minimum alignment quality (ECC)"), self.quality_menu)
        self.keep_menu = Choice(body, KEEP, str(config.get("keep")), f)
        field(body, 3, N_("Sharpest frames kept"), self.keep_menu)

        # ---- passaggio 5
        card = Card(column, tr("Fusion"), f)
        card.grid(row=2, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        self.scale_menu = Choice(body, SCALES, str(config.get("scale")), f)
        field(body, 0, N_("Scale"), self.scale_menu)
        self.method_menu = Choice(body, fusion.METHOD_LABELS, str(config.get("method")), f)
        field(body, 1, N_("Fusion method"), self.method_menu)
        self.sharp_var = ctk.BooleanVar(value=bool(config.get("weight_sharpness")))
        ctk.CTkCheckBox(body, text=tr("Weight by sharpness"), variable=self.sharp_var, font=f.small,
                        checkbox_width=18, checkbox_height=18).grid(row=4, column=0, sticky="w", pady=(theme.GAP, 0))
        self.equalize_var = ctk.BooleanVar(value=bool(config.get("equalize")))
        ctk.CTkCheckBox(body, text=tr("Equalize brightness"), variable=self.equalize_var, font=f.small,
                        checkbox_width=18, checkbox_height=18).grid(row=5, column=0, sticky="w", pady=(6, 0))

        # ---- passaggio 6
        card = Card(column, tr("Restoration"), f)
        card.grid(row=3, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        self.denoise_menu = Choice(body, fusion.DENOISE_LABELS, str(config.get("denoise")), f)
        field(body, 0, N_("Noise reduction"), self.denoise_menu)
        self.iterations_menu = Choice(body, ITERATIONS, str(config.get("iterations")), f)
        field(body, 1, N_("Deconvolution iterations"), self.iterations_menu)
        psf = float(config.get("psf_sigma") or 0)
        self.psf_menu = Choice(body, PSF, f"{psf:.1f}" if psf > 0 else "0", f)
        field(body, 2, N_("PSF σ (output pixels)"), self.psf_menu)
        self.regularization_menu = Choice(body, fusion.REGULARIZATION_LABELS, str(config.get("regularization")), f)
        field(body, 3, N_("Regularization (total variation)"), self.regularization_menu)
        hint = note(body, tr("More iterations sharpen more but also amplify noise and halos; the regularization "
                             "holds the noise back. Change a little at a time and compare."), f, wraplength=250)
        hint.grid(row=8, column=0, sticky="ew", pady=(theme.GAP, 0))

        # ---- passaggio 7: presentazione
        card = Card(column, tr("Presentation"), f)
        card.grid(row=4, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        self.levels_var = ctk.BooleanVar(value=bool(config.get("levels")))
        ctk.CTkCheckBox(body, text=tr("Auto levels"), variable=self.levels_var, font=f.small,
                        checkbox_width=18, checkbox_height=18).grid(row=0, column=0, sticky="w")
        self.local_contrast_menu = Choice(body, fusion.LOCAL_CONTRAST_LABELS, str(config.get("local_contrast")), f)
        field(body, 1, N_("Local contrast (CLAHE)"), self.local_contrast_menu)
        self.grayscale_var = ctk.BooleanVar(value=bool(config.get("grayscale")))
        ctk.CTkCheckBox(body, text=tr("Grayscale"), variable=self.grayscale_var, font=f.small,
                        checkbox_width=18, checkbox_height=18).grid(row=4, column=0, sticky="w", pady=(theme.GAP, 0))
        hint = note(body, tr("The levels are a straight line applied before the deconvolution (black and white "
                             "at the 0.5 and 99.5 percentiles); the local contrast an equalization by zones. All "
                             "written in the report."), f, wraplength=250)
        hint.grid(row=5, column=0, sticky="ew", pady=(theme.GAP, 0))

    def _build_compare(self, parent) -> None:
        card = Card(parent, tr("Comparison"), self.fonts)
        card.grid(row=0, column=0, sticky="nsew")
        self.summary_label = ctk.CTkLabel(card.head_right, text="", font=self.fonts.tiny,
                                          text_color=theme.TEXT_FAINT)
        self.summary_label.pack(side="right")
        body = card.body
        body.grid_columnconfigure((0, 1), weight=1, uniform="cmp")
        body.grid_rowconfigure(1, weight=1)
        f = self.fonts

        top_left = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        top_left.grid(row=0, column=0, sticky="ew")
        top_left.grid_columnconfigure(0, weight=1)
        self.left_caption = ctk.CTkLabel(top_left, text=tr("FRAMES"), font=f.caption, text_color=theme.TEXT_DIM,
                                         anchor="w", height=26)
        self.left_caption.grid(row=0, column=0, sticky="ew")
        self.left_menu = Choice(top_left, LEFT_VIEWS, "ghost", f, command=lambda _k: self._show_result(),
                                width=160, height=26)
        self.left_menu.grid(row=0, column=1, sticky="e", padx=(0, theme.GAP))
        top_right = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        top_right.grid(row=0, column=1, sticky="ew", padx=(theme.GAP, 0))
        top_right.grid_columnconfigure(0, weight=1)
        self.right_caption = ctk.CTkLabel(top_right, text=tr("RESULT"), font=f.caption, text_color=theme.ACCENT,
                                          anchor="w", height=26)
        self.right_caption.grid(row=0, column=0, sticky="ew")
        self.view_menu = Choice(top_right, VIEWS, "final", f, command=lambda _k: self._show_result(),
                                width=140, height=26)
        self.view_menu.grid(row=0, column=1, sticky="e")

        placeholder = tr("Draw the subject area on the Subject page, then run the fusion")
        self.before_view = PreviewView(body, on_step=None, on_zoom=lambda: self._zoom_label(),
                                       on_view=lambda: self._link(self.before_view, self.after_view),
                                       placeholder=placeholder)
        self.before_view.configure(width=300, height=200)
        self.before_view.grid(row=1, column=0, sticky="nsew", pady=(4, 0))
        self.after_view = PreviewView(body, on_step=None, on_zoom=lambda: self._zoom_label(),
                                      on_view=lambda: self._link(self.after_view, self.before_view),
                                      placeholder=placeholder)
        self.after_view.configure(width=300, height=200)
        self.after_view.grid(row=1, column=1, sticky="nsew", padx=(theme.GAP, 0), pady=(4, 0))
        hint = note(body, tr("wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  "
                             "ghost: every frame used, superimposed at the position where it was found"), f)
        hint.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(4, 0))
        follow_width(hint, body)

    def _build_pipeline(self, parent) -> None:
        """I sette passaggi con il loro esito, avanzamento, pulsanti e registro."""
        card = Card(parent, tr("Pipeline"), self.fonts)
        card.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        f = self.fonts

        steps = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        steps.grid(row=0, column=0, sticky="ew")
        steps.grid_columnconfigure((0, 1), weight=1, uniform="steps")
        self.step_rows: list[tuple[ctk.CTkLabel, ctk.CTkLabel]] = []
        for index, name in enumerate(fusion.STEPS):
            column, row = (0, index) if index < 4 else (1, index - 4)
            cell = ctk.CTkFrame(steps, fg_color="transparent", corner_radius=0)
            cell.grid(row=row, column=column, sticky="ew", padx=(0 if column == 0 else theme.PAD, 0))
            cell.grid_columnconfigure(3, weight=1)
            ctk.CTkLabel(cell, text=f"{index + 1}", font=f.caption, text_color=theme.TEXT_FAINT,
                         width=14, height=20).grid(row=0, column=0)
            dot = ctk.CTkLabel(cell, text="●", font=(theme.mono_font(), 10), text_color=STEP_COLORS["pending"],
                               width=14, height=20)
            dot.grid(row=0, column=1, padx=(2, 4))
            ctk.CTkLabel(cell, text=tr(name), font=f.small, text_color=theme.TEXT_SOFT, anchor="w",
                         height=20).grid(row=0, column=2, sticky="w")
            detail = ctk.CTkLabel(cell, text="", font=f.tiny, text_color=theme.TEXT_DIM, anchor="w", height=20)
            detail.grid(row=0, column=3, sticky="ew", padx=(8, 0))
            self.step_rows.append((dot, detail))

        self.run_label = ctk.CTkLabel(body, text=tr("Ready."), font=f.small, text_color=theme.TEXT_DIM, anchor="w")
        self.run_label.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        row = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        row.grid(row=2, column=0, sticky="ew", pady=(4, 0))
        row.grid_columnconfigure(1, weight=1)
        self.progress = ctk.CTkProgressBar(row, height=8, width=180)
        self.progress.grid(row=0, column=1, sticky="ew")
        self.progress.set(0)
        self.progress_label = ctk.CTkLabel(row, text="0 %", font=f.mono, text_color=theme.TEXT_DIM,
                                           width=52, anchor="e")
        self.progress_label.grid(row=0, column=2, padx=(6, theme.GAP))
        self.open_folder_button = button(row, tr("Open folder"), self._open_folder, width=110)
        self.open_folder_button.grid(row=0, column=3, padx=(theme.GAP, 0))
        self.cancel_button = button(row, tr("Cancel"), self._cancel, width=90, danger=True)
        self.cancel_button.grid(row=0, column=4, padx=(theme.GAP, 0))
        self.cancel_button.configure(state="disabled")
        self.save_result_button = button(row, tr("Save result"), self.save_result, width=120)
        self.save_result_button.grid(row=0, column=5, padx=(theme.GAP, 0))
        self.save_result_button.configure(state="disabled")
        Tooltip(self.save_result_button, tr("Saves images and report in a new folder (Ctrl+S)"), f)
        self.run_button = button(row, tr("Run fusion"), self.run_fusion, primary=True, width=130)
        self.run_button.grid(row=0, column=6, padx=(theme.GAP, 0))
        Tooltip(self.run_button, tr("Runs the pipeline again with these parameters (F5)"), f)

        self.log_box = ctk.CTkTextbox(body, height=64, font=f.tiny, text_color=theme.TEXT_DIM,
                                      state="disabled", wrap="none")
        self.log_box.grid(row=3, column=0, sticky="ew", pady=(theme.GAP, 0))

    # -------------------------------------------------- pagina Configurazione

    def _build_source(self, parent) -> None:
        card = Card(parent, tr("Source"), self.fonts)
        card.grid(row=0, column=0, sticky="new")
        body = card.body
        body.grid_columnconfigure(1, weight=1)

        self.video_entry = ctk.CTkEntry(body, height=30, state="readonly", font=self.fonts.body)
        self.video_entry.grid(row=0, column=0, columnspan=2, sticky="ew")
        button(body, tr("Open video…"), self.open_video, primary=True, width=100).grid(
            row=0, column=2, padx=(theme.GAP, 0))

        self.info_labels: dict[str, ctk.CTkLabel] = {}
        fields = ((N_("Duration"), "duration"), (N_("Frames"), "frames"),
                  (N_("Resolution"), "size"), (N_("Codec"), "codec"))
        for index, (title, key) in enumerate(fields):
            row, column = 1 + index // 2, (index % 2) * 2
            box = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
            box.grid(row=row, column=column, columnspan=1 if column == 0 else 2, sticky="ew",
                     pady=(theme.GAP, 0), padx=(0, theme.GAP) if column == 0 else 0)
            caption(box, tr(title), self.fonts).pack(anchor="w")
            label = ctk.CTkLabel(box, text="—", font=self.fonts.body, text_color=theme.TEXT_SOFT,
                                 anchor="w")
            label.pack(anchor="w")
            self.info_labels[key] = label
        body.grid_columnconfigure(0, weight=1, uniform="info")
        body.grid_columnconfigure(2, weight=1, uniform="info")

    def _build_output(self, parent) -> None:
        config = self.config_store
        card = Card(parent, tr("Output"), self.fonts)
        card.grid(row=1, column=0, sticky="new", pady=(theme.GAP, 0))
        body = card.body
        f = self.fonts
        for column in range(6):
            body.grid_columnconfigure(column, weight=1, uniform="out")

        caption(body, tr("Destination folder"), f).grid(row=0, column=0, columnspan=4, sticky="w")
        self.subfolder_var = ctk.BooleanVar(value=bool(config.get("subfolder")))
        ctk.CTkCheckBox(body, text=tr("Subfolder named after the video"), variable=self.subfolder_var,
                        font=f.small, checkbox_width=18, checkbox_height=18,
                        command=self._refresh_example).grid(row=0, column=4, columnspan=2, sticky="e")
        self.out_var = ctk.StringVar(value=str(config.get("output_dir")))
        self.out_var.trace_add("write", lambda *_a: self._refresh_example())
        ctk.CTkEntry(body, textvariable=self.out_var, height=30, font=f.body).grid(
            row=1, column=0, columnspan=5, sticky="ew", pady=(2, 0))
        button(body, tr("Browse…"), self._choose_output, width=90).grid(
            row=1, column=5, sticky="ew", padx=(theme.GAP, 0), pady=(2, 0))

        for column, title in enumerate((N_("Format"), N_("Color depth"))):
            caption(body, tr(title), f).grid(row=2, column=column, sticky="w", pady=(theme.GAP, 0),
                                             padx=(0 if column == 0 else theme.GAP, 0))
        fmt = str(config.get("format"))
        self.format_var = ctk.StringVar(value=fmt if fmt in ffmpeg.FORMATS else "PNG")
        ctk.CTkOptionMenu(body, values=list(ffmpeg.FORMATS), variable=self.format_var, height=30, width=60,
                          dynamic_resizing=False, font=f.body, dropdown_font=f.body,
                          command=lambda _v: self._refresh_example()).grid(row=3, column=0, sticky="ew")
        depth = str(config.get("depth"))
        self.depth_var = ctk.StringVar(value=depth if depth in ffmpeg.DEPTHS else "Auto")
        ctk.CTkOptionMenu(body, values=list(ffmpeg.DEPTHS), variable=self.depth_var, height=30, width=60,
                          dynamic_resizing=False, font=f.body, dropdown_font=f.body,
                          command=lambda _v: self._refresh_example()).grid(
            row=3, column=1, sticky="ew", padx=(theme.GAP, 0))
        self.aligned_var = ctk.BooleanVar(value=bool(config.get("save_aligned")))
        ctk.CTkCheckBox(body, text=tr("Also save every aligned frame (aligned/ folder)"), variable=self.aligned_var,
                        font=f.small, checkbox_width=18, checkbox_height=18).grid(
            row=3, column=2, columnspan=4, sticky="w", padx=(theme.PAD, 0))

        self.example_label = note(body, "", f)
        self.example_label.grid(row=4, column=0, columnspan=6, sticky="ew", pady=(theme.GAP, 0))
        follow_width(self.example_label, body)
        self._refresh_example()

    def _build_tools(self, parent) -> None:
        """Riquadro FFmpeg: dove sta, che versione e', download e aggiornamento in tools/."""
        card = Card(parent, "FFmpeg", self.fonts)
        card.grid(row=2, column=0, sticky="new", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(0, weight=1)
        f = self.fonts

        top = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        top.grid(row=0, column=0, sticky="ew")
        top.grid_columnconfigure(0, weight=1)
        self.tool_label = ctk.CTkLabel(top, text=tr("Checking…"), font=f.body, text_color=theme.TEXT_SOFT,
                                       anchor="w")
        self.tool_label.grid(row=0, column=0, sticky="ew")
        self.tool_check_button = button(top, tr("Check"), self.refresh_tools, width=80)
        self.tool_check_button.grid(row=0, column=1, padx=(theme.GAP, 0))
        self.tool_update_button = button(top, tr("Check for updates"), self.check_tool_updates, width=140)
        self.tool_update_button.grid(row=0, column=2, padx=(theme.GAP, 0))
        self.tool_cancel_button = button(top, tr("Cancel"), self._cancel_install, width=90, danger=True)
        self.tool_cancel_button.grid(row=0, column=3, padx=(theme.GAP, 0))
        self.tool_cancel_button.configure(state="disabled")
        self.tool_install_button = button(top, tr("Download / Update"), self.install_tools, primary=True,
                                          width=150)
        self.tool_install_button.grid(row=0, column=4, padx=(theme.GAP, 0))

        self.tool_progress = ctk.CTkProgressBar(body, height=8)
        self.tool_progress.grid(row=1, column=0, sticky="ew", pady=(theme.GAP, 0))
        self.tool_progress.set(0)
        hint = note(body, tr("ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
                             "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
                             "folder next to the program: no installation, no changes to the PATH.").format(
            url=tools.FFMPEG_PAGE), f)
        hint.grid(row=2, column=0, sticky="ew", pady=(theme.GAP, 0))
        follow_width(hint, body)

    def _build_language(self, parent) -> None:
        card = Card(parent, tr("Language"), self.fonts)
        card.grid(row=3, column=0, sticky="new", pady=(theme.GAP, 0))
        body = card.body
        body.grid_columnconfigure(1, weight=1)
        self.language_switch = LanguageSwitch(
            body, self.fonts, list(i18n.LANGUAGES), i18n.language(), self.set_language)
        self.language_switch.grid(row=0, column=0, sticky="w")
        note(body, tr("Interface language. The change is immediate and is saved for the next start."),
             self.fonts).grid(row=0, column=1, sticky="w", padx=(theme.PAD, 0))

    def _build_credits(self, parent) -> None:
        """Crediti dell'autore (vedi NOTICE), sotto la lingua."""
        credits = Card(parent, tr("Credits"), self.fonts)
        credits.grid(row=4, column=0, sticky="new", pady=(theme.GAP, 0))
        body = credits.body
        body.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(body, text=CREDITS, font=self.fonts.mono, text_color=theme.ACCENT, anchor="w").grid(
            row=1, column=0, sticky="w")
        about = note(body, tr("Free software under the GNU GPL v3 with author attribution: see the LICENSE and "
                              "NOTICE files. Video decoding by FFmpeg, a separate program under its own license; "
                              "image processing with OpenCV and NumPy."),
                     self.fonts)
        about.grid(row=2, column=0, sticky="ew", pady=(4, 0))
        follow_width(about, body)
        links = ctk.CTkFrame(body, fg_color="transparent", corner_radius=0)
        links.grid(row=3, column=0, sticky="w", pady=(4, 0))
        link(links, "ffmpeg.org", lambda: webbrowser.open("https://ffmpeg.org")).pack(side="left")
        link(links, "opencv.org", lambda: webbrowser.open("https://opencv.org")).pack(side="left", padx=(8, 0))

    def _build_footer(self) -> None:
        footer = ctk.CTkFrame(self, fg_color=theme.BG, corner_radius=0, height=26)
        footer.grid(row=4, column=0, sticky="ew")
        footer.grid_propagate(False)
        footer.grid_columnconfigure(0, weight=1)
        footer.grid_rowconfigure(0, weight=1)
        self.status_label = ctk.CTkLabel(footer, text=tr("Ready."), font=self.fonts.small,
                                         text_color=theme.TEXT_SOFT, anchor="w")
        self.status_label.grid(row=0, column=0, sticky="ew", padx=(16, 8))
        self.busy_bar = ctk.CTkProgressBar(footer, mode="indeterminate", width=90, height=4)
        self.busy_bar.grid(row=0, column=1, padx=(0, 14))
        self.busy_bar.grid_remove()
        self.engine_label = ctk.CTkLabel(footer, text="", font=self.fonts.tiny, text_color=theme.TEXT_DIM)
        self.engine_label.grid(row=0, column=2, sticky="e", padx=(0, 16))
        ctk.CTkLabel(footer, text=tr("Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   "
                                     "Ctrl+S  save"),
                     font=self.fonts.tiny, text_color=theme.TEXT_FAINT).grid(
            row=0, column=3, sticky="e", padx=(0, 16))
        # Dicitura di paternita' (vedi NOTICE): sempre visibile.
        ctk.CTkLabel(footer, text=CREDITS, font=self.fonts.tiny, text_color=theme.TEXT_DIM).grid(
            row=0, column=4, sticky="e", padx=(0, 16))

    # ---------------------------------------------------------------- lingua

    def set_language(self, code: str) -> None:
        """Cambia lingua a programma aperto: i testi a schermo vengono ritradotti subito."""
        if code == i18n.language():
            return
        code = i18n.set_language(code)
        self.config_store.set("language", code)
        self.config_store.save()
        self.language_switch.select(code)
        retranslate_all(self)
        self._paint_page_head()
        self.preview.placeholder = tr("Open a video to see the preview")
        self.preview.set_roi(self.preview.roi, self.preview.roi_label)
        for view in (self.before_view, self.after_view):
            view.placeholder = tr("Draw the subject area on the Subject page, then run the fusion")
            view.set_roi(None)   # ridisegna il segnaposto nella nuova lingua
        self._paint_subject()
        self._refresh_example()
        self._fill_presets(self.preset_menu.key)

    # ---------------------------------------------------------------- tastiera

    def _bind_keys(self) -> None:
        self.bind("<Key>", self._key)
        self.bind("<Control-o>", lambda _e: self.open_video())
        for index, (key, _label, _glyph, _title) in enumerate(PAGES, start=1):
            self.bind(f"<Control-Key-{index}>", lambda _e, k=key: self.show_page(k))
        self.bind("<Control-s>", lambda _e: self.save_result() if self._page_key == "result" else self.save_frame())
        self.bind("<F5>", lambda _e: self.run_fusion())

    def _typing(self) -> bool:
        return isinstance(self.focus_get(), (tk.Entry, tk.Text))

    def _key(self, event) -> None:
        if self.info is None or self._typing() or self._page_key != "work":
            return
        shift = bool(event.state & 0x0001)
        key = event.keysym
        if key == "Left":
            self.step(-10 if shift else -1)
        elif key == "Right":
            self.step(10 if shift else 1)
        elif key == "Home":
            self.goto(0)
        elif key == "End":
            self.goto(self.info.frames - 1)
        elif key in ("i", "I"):
            self.mark("in")
        elif key in ("o", "O"):
            self.mark("out")
        elif key in ("plus", "equal", "KP_Add"):
            self.timeline.zoom(1.6)
        elif key in ("minus", "KP_Subtract"):
            self.timeline.zoom(1 / 1.6)
        elif key in ("f", "F"):
            self.timeline.zoom_fit()
        elif key == "Escape":
            self._set_draw(False)
            self.focus_set()

    def _bind_time_entry(self, entry: ctk.CTkEntry, apply) -> None:
        def commit(_event=None) -> None:
            if self.info is None:
                return
            frame = parse_time(entry.get(), self.info.fps)
            if frame is None:
                self.status(tr("Time not recognized: use mm:ss.mmm, seconds or f<number>."))
                return
            apply(min(frame, self.info.frames - 1))
            self.focus_set()

        entry.bind("<Return>", commit)
        entry.bind("<KP_Enter>", commit)
        entry.bind("<Escape>", lambda _e: self.focus_set())

    # ---------------------------------------------------------------- avvio

    def _startup(self, video: str | None) -> None:
        # il video passato da riga di comando si apre solo quando si sa che ffmpeg c'e'
        self._pending_video = Path(video) if video else None
        self.refresh_tools(first=True)

    # ---------------------------------------------------------------- ffmpeg

    def refresh_tools(self, first: bool = False) -> None:
        """Rilegge dove sta ffmpeg e la sua versione (in background: avvia un processo)."""
        ffmpeg.reset()
        self.tasks.run(tools.status, on_ok=lambda state: self._show_tools(state, first),
                       on_error=lambda exc: self.error(tr("ffmpeg check failed"), exc))

    def _show_tools(self, state: tools.Status, first: bool = False) -> None:
        sources = {"tools": tr("tools folder"), "path": tr("system PATH"), "package": tr("Python package")}
        if state.present and state.path is not None:
            try:
                shown = state.path.relative_to(tools.APP_DIR)
            except ValueError:
                shown = state.path
            version = state.version or "?"
            self.tool_label.configure(
                text=tr("OK  ·  ffmpeg {version}  ·  {source}  ·  {path}").format(
                    version=version, source=sources.get(state.source, state.source), path=shown),
                text_color=theme.OK)
            self.engine_label.configure(text=f"ffmpeg {version}", text_color=theme.TEXT_DIM)
            self.log(tr("Engine: ffmpeg {version} ({path})").format(version=version, path=state.path))
            self.tool_update_button.configure(state="normal" if state.source == "tools" else "disabled")
            pending, self._pending_video = self._pending_video, None
            if pending is not None:
                self.load(pending)
        else:
            self.tool_label.configure(text=tr("Missing: download it with the button on the right."),
                                      text_color=theme.ERR)
            self.engine_label.configure(text=tr("ffmpeg missing"), text_color=theme.ERR)
            self.tool_update_button.configure(state="disabled")
            self.log(tr("ffmpeg not found: download it from the FFmpeg box of the Configuration page."))
            if first or self._pending_video is not None:
                self.show_page("setup")
                self.status(tr("ffmpeg missing: download it from the FFmpeg box."))

    def check_tool_updates(self) -> None:
        """Confronta la release scritta all'ultimo download con l'ultima pubblicata."""
        if self._installing is not None:
            return
        self.status(tr("Checking the latest ffmpeg version…"))

        def done(latest: str) -> None:
            installed = tools.installed_release()
            if installed and installed == latest:
                self.status(tr("ffmpeg {version} is up to date.").format(version=latest))
                messagebox.showinfo("FFmpeg", tr("ffmpeg {version} is up to date.").format(version=latest),
                                    parent=self)
                return
            text = tr("Latest release: {latest}. Installed: {installed}. Download it now?").format(
                latest=latest, installed=installed or "?")
            self.status(text)
            if messagebox.askyesno("FFmpeg", text, parent=self):
                self.install_tools()

        self.tasks.run(tools.latest_release, on_ok=done,
                       on_error=lambda exc: self.error(tr("Update check failed"), exc))

    def install_tools(self) -> None:
        """Scarica (o aggiorna) ffmpeg in tools/ffmpeg/ con avanzamento e annullamento."""
        if self._installing is not None:
            return
        if self._running is not None:
            messagebox.showwarning("FFmpeg", tr("Wait for the running fusion, then try again."), parent=self)
            return
        cancel = self._installing = threading.Event()
        self.tool_install_button.configure(state="disabled")
        self.tool_check_button.configure(state="disabled")
        self.tool_update_button.configure(state="disabled")
        self.tool_cancel_button.configure(state="normal")
        self.tool_progress.set(0)
        self.status(tr("Downloading ffmpeg…"))
        self.log(tr("Downloading ffmpeg from {url}").format(url=tools.FFMPEG_URL))
        last = [-1]

        def progress(label: str, done: int, total: int) -> None:
            percent = done * 100 // total if total > 0 else -1
            if percent != last[0] or total <= 0:
                last[0] = percent
                self.tasks.post(self._tools_progress, label, done, total)

        def finish() -> None:
            self._installing = None
            self.tool_install_button.configure(state="normal")
            self.tool_check_button.configure(state="normal")
            self.tool_cancel_button.configure(state="disabled")

        def ok(path) -> None:
            finish()
            self.tool_progress.set(1)
            self.status(tr("ffmpeg downloaded into {path}").format(path=path))
            self.log(tr("ffmpeg downloaded into {path}").format(path=path))
            self.refresh_tools()
            self._preview_frame = -1
            if self.info is not None:
                self._request_preview(self.timeline.play_f)

        def failed(exc: BaseException) -> None:
            finish()
            self.tool_progress.set(0)
            if isinstance(exc, tools.Cancelled):
                self.status(tr("Download cancelled."))
                self.log(tr("Download cancelled."))
                return
            self.error(tr("ffmpeg download failed"), exc)
            self.refresh_tools()

        self.tasks.run(lambda: tools.install(progress, cancel), on_ok=ok, on_error=failed, lane="tools")

    def _tools_progress(self, label: str, done: int, total: int) -> None:
        if total > 0:
            self.tool_progress.set(done / total)
            self.status(f"{label}  ·  {done / 1_048_576:.1f} / {total / 1_048_576:.1f} MB")
        else:
            self.status(label)

    def _cancel_install(self) -> None:
        if self._installing is not None:
            self._installing.set()

    # ------------------------------------------------------------- sorgente

    def open_video(self) -> None:
        if self._running is not None:
            return
        initial = str(self.config_store.get("last_video_dir")) or str(Path.home())
        path = filedialog.askopenfilename(
            parent=self, title=tr("Open video"), initialdir=initial,
            filetypes=[(tr("Videos"), ffmpeg.VIDEO_EXTENSIONS), (tr("All files"), "*.*")],
        )
        if path:
            self.load(Path(path))

    def load(self, path: Path) -> None:
        self.status(tr("Reading {name}…").format(name=path.name))
        self._set_state(tr("Reading…"), theme.WARN)
        self.tasks.run(lambda: ffmpeg.probe(path), on_ok=self._loaded,
                       on_error=lambda exc: (self._set_state(tr("Error"), theme.ERR),
                                             self.error(tr("Cannot open the video"), exc)))

    def _loaded(self, info: VideoInfo) -> None:
        self.info = info
        self.config_store.set("last_video_dir", str(info.path.parent))
        self.video_entry.configure(state="normal")
        self.video_entry.delete(0, "end")
        self.video_entry.insert(0, str(info.path))
        self.video_entry.configure(state="readonly")
        name = info.path.name
        if len(name) > NAME_MAX:
            name = name[:NAME_MAX - 1] + "…"
        self.video_label.configure(text=name, text_color=theme.TEXT)
        hours = info.duration >= 3600
        duration = format_time(info.duration, hours=hours)
        self.info_labels["duration"].configure(text=duration)
        self.info_labels["frames"].configure(text=f"{info.frames}  ·  {info.fps:g} fps")
        rotated = tr("  (rotated {degrees}°)").format(degrees=info.rotation) if info.rotation else ""
        self.info_labels["size"].configure(text=f"{info.width} × {info.height}{rotated}")
        self.info_labels["codec"].configure(text=f"{info.codec}  ·  {info.pix_fmt}  ·  {info.bit_depth} bit")
        self._preview_frame = -1
        self._preview_image = None
        self._preview_full = False
        self._preview_last = -1
        self._preview_dir = 0
        self._inflight = None
        self._frames.clear()
        self._frames_bytes = 0
        self.preview.clear()
        self.timeline.set_video(info)
        self._forget_subject()
        # il risultato del video precedente non vale piu' (e i suoi ritagli occupano memoria)
        self._alignment = self._alignment_key = self._result = None
        self._last_folder = None
        self.before_view.clear()
        self.after_view.clear()
        self.save_result_button.configure(state="disabled")
        self.summary_label.configure(text="")
        self.left_caption.configure(text=tr("FRAMES"))
        self.right_caption.configure(text=tr("RESULT"))
        self.run_label.configure(text=tr("Ready."), text_color=theme.TEXT_DIM)
        self.progress.set(0)
        self.progress_label.configure(text="0 %")
        for dot, detail in self.step_rows:
            dot.configure(text_color=STEP_COLORS["pending"])
            detail.configure(text="")
        self._on_zoom()
        self._on_range(0, info.frames - 1)
        self._on_playhead(0)
        self._on_view()
        self._refresh_example()
        self._set_state(tr("Ready"), theme.OK)
        self.status(tr("{name}: {frames} frames, {duration}.").format(
            name=info.path.name, frames=info.frames, duration=duration))
        self.log(tr("Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}")
                 .format(path=info.path, width=info.width, height=info.height, fps=f"{info.fps:g}",
                         codec=info.codec, pix_fmt=info.pix_fmt, bits=info.bit_depth, duration=duration))
        self.show_page("work")
        self.focus_set()

    # ------------------------------------------------------------ navigazione

    def goto(self, frame: int) -> None:
        if self.info is not None:
            self.timeline.set_playhead(frame)

    def step(self, frames: int) -> None:
        if self.info is not None:
            self.timeline.step(frames)

    def mark(self, which: str) -> None:
        if self.info is None:
            return
        if which == "in":
            self.timeline.set_in(self.timeline.play_f)
        else:
            self.timeline.set_out(self.timeline.play_f)

    def _on_playhead(self, frame: int) -> None:
        if self.info is None:
            return
        t = frame / self.info.fps
        text = format_time(t, hours=self.info.duration >= 3600)
        self.time_label.configure(text=text)
        reference = "  ·  R" if frame == self.ref else ""
        self.frame_label.configure(text=f"f {frame} / {self.info.frames - 1}{reference}")
        if self.focus_get() is not self.cursor_entry._entry:
            self._set_entry(self.cursor_entry, text)
        self._request_preview(frame)

    def _on_range(self, in_f: int, out_f: int) -> None:
        if self.info is None:
            return
        fps = self.info.fps
        hours = self.info.duration >= 3600
        self._set_entry(self.in_entry, format_time(in_f / fps, hours=hours))
        self._set_entry(self.out_entry, format_time(out_f / fps, hours=hours))
        count = out_f - in_f + 1
        self.selection_label.configure(
            text=tr("Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s").format(
                first=in_f, last=out_f, count=count, seconds=count / fps))
        self._paint_subject()

    def _on_view(self) -> None:
        if self.info is None:
            self.view_label.configure(text="")
            return
        tl = self.timeline
        hours = self.info.duration >= 3600
        self.view_label.configure(
            text=tr("View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)").format(
                start=format_time(tl.v0, hours=hours), end=format_time(tl.v1, hours=hours),
                seconds=tl.span, frames=tl.span * self.info.fps))

    @staticmethod
    def _set_entry(entry: ctk.CTkEntry, text: str) -> None:
        if entry.get() != text:
            entry.delete(0, "end")
            entry.insert(0, text)

    # -------------------------------------------------------------- anteprima

    def _request_preview(self, frame: int) -> None:
        self._preview_wanted = frame
        if self._preview_job is None:
            self._preview_job = self.after(PREVIEW_DELAY_MS, self._fire_preview)

    def _fire_preview(self) -> None:
        self._preview_job = None
        info, frame = self.info, self._preview_wanted
        if info is None:
            return
        # a piena risoluzione solo quando lo zoom lo richiede; se l'abbiamo gia', non si rifa'
        need_full = self.preview.wants_full()
        if frame == self._preview_frame and (self._preview_full or not need_full):
            return
        self._preview_gen += 1
        generation = self._preview_gen
        width = info.width if need_full else min(info.width, PREVIEW_MAX_WIDTH)
        # verso di marcia: se lo stesso fotogramma viene richiesto di nuovo (lotto appena
        # finito, zoom cambiato) resta quello di prima, cosi' il lotto seguente parte giusto
        # (un salto di pochi fotogrammi conta come un passo: il ritardo anti-rimbalzo fonde le pressioni)
        if frame != self._preview_last:
            delta = frame - self._preview_last
            self._preview_dir = (1 if 0 < delta <= PREVIEW_LOOKAHEAD
                                 else -1 if -PREVIEW_LOOKAHEAD <= delta < 0 else 0)
            self._preview_last = frame
        direction = self._preview_dir

        cached = self._frames.get((frame, width))
        if cached is not None:
            self._frames.move_to_end((frame, width))
            self._show_preview(generation, frame, cached)
            # si sta avanzando di un fotogramma alla volta: il prossimo lotto si prepara gia'
            nxt = frame + direction
            if (direction and self._inflight is None and 0 <= nxt < info.frames
                    and (nxt, width) not in self._frames):
                self._fetch_frames(info, nxt, width, direction, generation=None)
            return
        if self._inflight is not None:
            return  # un lotto e' in decodifica: al suo termine _show_wanted mostra o richiede il fotogramma
        self._fetch_frames(info, frame, width, direction, generation=generation)

    def _fetch_frames(self, info: VideoInfo, frame: int, width: int, direction: int,
                      generation: int | None) -> None:
        """Decodifica `frame` e, se si naviga di un passo alla volta, anche i vicini nel verso di marcia.

        Un lotto costa quasi quanto un fotogramma solo (la decodifica dal keyframe
        e' la stessa): i successivi tasti freccia escono dalla cache all'istante.
        Alla fine mostra il fotogramma che serve in quel momento, non quello
        chiesto all'inizio: se nel frattempo l'utente e' andato avanti, si vede
        l'ultimo e, se e' oltre il lotto, parte il lotto seguente.
        """
        frame_bytes = width * int(info.height * width / info.width) * 3
        count = max(1, min(PREVIEW_LOOKAHEAD, (48 * 1024 * 1024) // max(1, frame_bytes)))
        if direction > 0:
            first, count = frame, min(count, info.frames - frame)
        elif direction < 0:
            first = max(0, frame - count + 1)
            count = frame - first + 1
        else:
            first, count = frame, 1
        job = object()  # identita' di questo lotto: finish() azzera solo il proprio marcatore
        self._inflight = job

        def work():
            if generation is not None and generation != self._preview_gen:
                return None  # superata da una richiesta piu' recente
            if count == 1:
                return {frame: ffmpeg.grab(info.path, ffmpeg.seek_time(info, frame), width=width)}
            images = ffmpeg.grab_run(info, first, count, width=width)
            return {first + index: image for index, image in enumerate(images)}

        def finish() -> None:
            if self._inflight == job:
                self._inflight = None

        def done(images) -> None:
            finish()
            if self.info is not info:
                return
            for f, image in (images or {}).items():
                self._cache_frame(f, width, image)
            self._show_wanted()

        def failed(exc: BaseException) -> None:
            finish()
            self.status(tr("Preview unavailable: {error}").format(error=exc))

        self.tasks.run(work, on_ok=done, on_error=failed, lane="preview")

    def _show_wanted(self) -> None:
        """Mostra il fotogramma corrente se e' in cache, altrimenti lo chiede."""
        if self.info is None:
            return
        frame = self._preview_wanted
        need_full = self.preview.wants_full()
        if frame == self._preview_frame and (self._preview_full or not need_full):
            return
        width = self.info.width if need_full else min(self.info.width, PREVIEW_MAX_WIDTH)
        image = self._frames.get((frame, width))
        if image is not None:
            self._frames.move_to_end((frame, width))
            self._preview_gen += 1
            self._show_preview(self._preview_gen, frame, image)
        else:
            self._request_preview(frame)

    def _cache_frame(self, frame: int, width: int, image) -> None:
        key = (frame, width)
        size = image.width * image.height * 3
        if key in self._frames:
            self._frames.move_to_end(key)
            return
        self._frames[key] = image
        self._frames_bytes += size
        while self._frames_bytes > PREVIEW_CACHE_BYTES and len(self._frames) > 1:
            _old_key, old = self._frames.popitem(last=False)
            self._frames_bytes -= old.width * old.height * 3

    def _show_preview(self, generation: int, frame: int, image) -> None:
        if image is None or generation != self._preview_gen or self.info is None:
            return
        self._preview_image = image
        self._preview_frame = frame
        self._preview_full = image.width >= self.info.width
        self.preview.set_image(image, (self.info.width, self.info.height))
        self._on_zoom()

    def _on_zoom(self) -> None:
        """Lo zoom e' cambiato: aggiorna l'indicatore e, se serve, chiede il fotogramma intero."""
        if self.info is None:
            self.preview_info.configure(text="")
            return
        self.preview_info.configure(
            text=f"{self.info.width} × {self.info.height}  ·  {self.preview.zoom * 100:.0f} %")
        if self.preview.wants_full() and not self._preview_full:
            self._request_preview(self.timeline.play_f)

    def save_frame(self) -> None:
        """Salva il fotogramma mostrato a piena risoluzione, senza perdita."""
        info = self.info
        if info is None:
            return
        frame = self.timeline.play_f
        fmt = self.format_var.get()
        ext = ffmpeg.FORMATS[fmt][0]
        initial_dir = self.out_var.get().strip() or str(info.path.parent)
        target = filedialog.asksaveasfilename(
            parent=self, title=tr("Save frame"), initialdir=initial_dir,
            initialfile=f"{info.path.stem}_f{frame:06d}.{ext}", defaultextension=f".{ext}",
            filetypes=[(tr("{format} (lossless)").format(format=fmt), f"*.{ext}"), (tr("All files"), "*.*")],
        )
        if not target:
            return
        depth = self.depth_var.get()
        self.status(tr("Saving frame {frame}…").format(frame=frame))
        self.tasks.run(
            lambda: ffmpeg.save_frame(info, frame, target, fmt, depth),
            on_ok=lambda path: (self.status(tr("Saved {path}").format(path=path)),
                                self.log(tr("Frame f{frame} saved to {path} ({pix_fmt})").format(
                                    frame=frame, path=path, pix_fmt=ffmpeg.choose_pix_fmt(info, fmt, depth)))),
            on_error=lambda exc: self.error(tr("Save failed"), exc),
        )

    # -------------------------------------------------------------- soggetto

    def _toggle_draw(self) -> None:
        self._set_draw(not self.preview.draw_mode)

    def _set_draw(self, on: bool) -> None:
        self.preview.draw_mode = on and self.info is not None
        if self.preview.draw_mode:
            self.draw_button.configure(fg_color=theme.ACCENT_BG, text_color=theme.ACCENT)
            self.status(tr("Drag on the preview to frame the subject (Esc to stop)."))
        else:
            self.draw_button.configure(fg_color=theme.NEUTRAL, text_color=theme.TEXT)

    def _roi_drawn(self, roi: tuple[int, int, int, int]) -> None:
        """Riquadro disegnato (o proposto): il fotogramma mostrato diventa il riferimento."""
        self._set_draw(False)
        if self.info is None:
            return
        if roi[2] < fusion.MIN_ROI or roi[3] < fusion.MIN_ROI:
            self.status(tr("The subject area is too small: draw at least {size} × {size} pixels.").format(
                size=fusion.MIN_ROI))
            self._paint_subject()
            return
        self.roi = roi
        self.ref = self.timeline.play_f
        self.timeline.set_reference(self.ref)
        tl = self.timeline
        # intervallo ancora sull'intero video: si propone un intorno del riferimento
        if tl.in_f == 0 and tl.out_f == self.info.frames - 1 and self.info.frames > 2 * AUTO_RANGE + 1:
            tl.set_in(max(0, self.ref - AUTO_RANGE), notify=False)
            tl.set_out(min(self.info.frames - 1, self.ref + AUTO_RANGE), notify=False)
            self._on_range(tl.in_f, tl.out_f)
            self.log(tr("Range set around the reference: f{first} → f{last}. Move I / O to change it.").format(
                first=tl.in_f, last=tl.out_f))
        self._paint_subject()
        self.log(tr("Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}").format(
            width=roi[2], height=roi[3], x=roi[0], y=roi[1], frame=self.ref))
        # la fusione parte da sola; se una e' in corso, si interrompe e si rifa' con l'area nuova
        if self._running is not None:
            self._rerun = True
            self._running.set()
        else:
            self.run_fusion()

    def clear_subject(self) -> None:
        self._forget_subject()
        self.status(tr("Subject area cleared."))

    def _forget_subject(self) -> None:
        self.roi = None
        self.ref = None
        self.timeline.set_reference(None)
        self._set_draw(False)
        self._paint_subject()

    def _paint_subject(self) -> None:
        """Riquadro sull'anteprima e riepilogo nel riquadro Soggetto."""
        if self.roi is None or self.ref is None or self.info is None:
            self.preview.set_roi(None)
            self.subject_label.configure(
                text=tr("Frame the subject on a clear frame: that frame becomes the reference and the fusion starts."),
                text_color=theme.TEXT_DIM)
            return
        x, y, w, h = self.roi
        self.preview.set_roi(self.roi, f"R  f{self.ref}")
        tl = self.timeline
        count = tl.out_f - tl.in_f + 1
        if not tl.in_f <= self.ref <= tl.out_f:
            text, color = tr("Reference f{frame} is outside the range f{first} → f{last}: move I / O.").format(
                frame=self.ref, first=tl.in_f, last=tl.out_f), theme.WARN
        elif count > fusion.MAX_FRAMES:
            text, color = tr("{count} frames in the range: select at most {limit}.").format(
                count=count, limit=fusion.MAX_FRAMES), theme.WARN
        else:
            text, color = tr("Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  "
                             "{count} frames f{first} → f{last}").format(
                width=w, height=h, x=x, y=y, frame=self.ref, count=count, first=tl.in_f, last=tl.out_f), theme.TEXT_SOFT
        self.subject_label.configure(text=text, text_color=color)

    # -------------------------------------------------------------- pipeline

    def _read_params(self) -> fusion.Params:
        return fusion.Params(
            motion=self.motion_menu.key,
            keep=int(self.keep_menu.key),
            min_quality=float(self.quality_menu.key),
            track_min=float(self.track_menu.key),
            scale=int(self.scale_menu.key),
            method=self.method_menu.key,
            weight_sharpness=bool(self.sharp_var.get()),
            equalize=bool(self.equalize_var.get()),
            denoise=self.denoise_menu.key,
            iterations=int(self.iterations_menu.key),
            psf_sigma=float(self.psf_menu.key),
            regularization=self.regularization_menu.key,
            levels=bool(self.levels_var.get()),
            local_contrast=self.local_contrast_menu.key,
            grayscale=bool(self.grayscale_var.get()),
        )

    def reset_params(self) -> None:
        """Riporta tutti i parametri della pipeline ai valori predefiniti (config.DEFAULTS)."""
        self._apply_params(DEFAULTS)
        self.preset_menu.select("")
        self.config_store.set("preset", "")
        self.status(tr("Parameters back to their defaults."))
        self.log(tr("Parameters back to their defaults."))

    def _apply_params(self, values: dict) -> None:
        """Porta nei controlli i valori di `values` (chiavi di PARAM_KEYS); quelle assenti restano come sono."""
        d = {key: values[key] for key in PARAM_KEYS if key in values and values[key] is not None}
        current = self._read_params()
        for key in PARAM_KEYS:
            d.setdefault(key, getattr(current, key))
        self.motion_menu.select(str(d["motion"]))
        self.track_menu.select(f"{float(d['track_min']):.2f}")
        self.quality_menu.select(f"{float(d['min_quality']):.2f}")
        self.keep_menu.select(str(d["keep"]))
        self.scale_menu.select(str(d["scale"]))
        self.method_menu.select(str(d["method"]))
        self.sharp_var.set(bool(d["weight_sharpness"]))
        self.equalize_var.set(bool(d["equalize"]))
        self.denoise_menu.select(str(d["denoise"]))
        self.iterations_menu.select(str(d["iterations"]))
        self.psf_menu.select("0" if float(d["psf_sigma"]) <= 0 else f"{float(d['psf_sigma']):.1f}")
        self.regularization_menu.select(str(d["regularization"]))
        self.levels_var.set(bool(d["levels"]))
        self.local_contrast_menu.select(str(d["local_contrast"]))
        self.grayscale_var.set(bool(d["grayscale"]))

    # ------------------------------------------------------ impostazioni salvate

    def _presets(self) -> dict[str, dict]:
        presets = self.config_store.get("presets")
        return presets if isinstance(presets, dict) else {}

    def _fill_presets(self, current: str) -> None:
        names = sorted(self._presets(), key=str.lower)
        options = {name: name for name in names} if names else {"": NO_PRESET}
        self.preset_menu.set_options(options, current if current in options else next(iter(options)))

    def load_preset(self, name: str) -> None:
        values = self._presets().get(name)
        if not name or values is None:
            return
        self._apply_params(values)
        self.config_store.set("preset", name)
        self.status(tr("Settings «{name}» loaded.").format(name=name))
        self.log(tr("Settings «{name}» loaded.").format(name=name))

    def save_preset(self) -> None:
        """Salva i parametri correnti con un nome in config.json (subito, non solo alla chiusura)."""
        initial = self.preset_menu.key or ""
        name = askstring(tr("Save settings"), tr("Name of these settings:"), initial, parent=self)
        if not name:
            return
        presets = dict(self._presets())
        if name in presets and not messagebox.askyesno(
                tr("Save settings"), tr("Settings «{name}» already exist. Replace them?").format(name=name),
                parent=self):
            return
        presets[name] = {key: getattr(self._read_params(), key) for key in PARAM_KEYS}
        self.config_store.set("presets", presets)
        self.config_store.set("preset", name)
        self.config_store.save()
        self._fill_presets(name)
        self.status(tr("Settings «{name}» saved.").format(name=name))
        self.log(tr("Settings «{name}» saved.").format(name=name))

    def delete_preset(self) -> None:
        name = self.preset_menu.key
        presets = dict(self._presets())
        if not name or name not in presets:
            return
        if not messagebox.askyesno(tr("Delete settings"), tr("Delete the settings «{name}»?").format(name=name),
                                   parent=self):
            return
        del presets[name]
        self.config_store.set("presets", presets)
        self.config_store.set("preset", "")
        self.config_store.save()
        self._fill_presets("")
        self.status(tr("Settings «{name}» deleted.").format(name=name))

    def load_from_report(self) -> None:
        """Carica i parametri dal report.json di una fusione salvata: per ripetere quell'elaborazione."""
        initial = str(self._last_folder or self._output_dir() or (self.info.path.parent if self.info else Path.home()))
        path = filedialog.askopenfilename(parent=self, title=tr("Load parameters from a report"), initialdir=initial,
                                          filetypes=[("report.json", "report.json"), ("JSON", "*.json")])
        if not path:
            return
        try:
            values = report.settings_from_report(Path(path))
        except (OSError, ValueError) as exc:
            self.error(tr("Cannot read the report"), exc)
            return
        self._apply_params(values)
        self.preset_menu.select("")
        self.config_store.set("preset", "")
        self.status(tr("Parameters loaded from {path}").format(path=path))
        self.log(tr("Parameters loaded from {path}").format(path=path))

    def run_fusion(self) -> None:
        """Avvia la pipeline; i passaggi 1-4 si riusano se video, intervallo, riquadro e moto non cambiano."""
        if self._running is not None or self._saving:
            return
        info = self.info
        if info is None:
            messagebox.showinfo(tr("No video"), tr("Open a video first."), parent=self)
            return
        if self.roi is None or self.ref is None:
            self.show_page("work")
            messagebox.showinfo(tr("Subject"), tr("Select the area of the subject (plate, face, object) on a clear "
                                                  "frame first: right-drag on the preview, or use Select area."),
                                parent=self)
            return
        tl = self.timeline
        if not tl.in_f <= self.ref <= tl.out_f:
            self.show_page("work")
            messagebox.showwarning(tr("Subject"), tr("The reference frame must be inside the selected range."),
                                   parent=self)
            return
        if tl.out_f - tl.in_f + 1 > fusion.MAX_FRAMES:
            self.show_page("work")
            messagebox.showwarning(tr("Subject"), tr("The range has {count} frames: select at most {limit} around "
                                                     "the reference.").format(count=tl.out_f - tl.in_f + 1,
                                                                              limit=fusion.MAX_FRAMES), parent=self)
            return
        params = self._read_params()
        request = fusion.Request(info=info, first=tl.in_f, last=tl.out_f, ref=self.ref, roi=self.roi)
        key = request.key(params)
        cached = self._alignment if (self._alignment is not None and self._alignment_key == key) else None

        cancel = self._running = threading.Event()
        self.show_page("result")
        self._run_started = time.perf_counter()
        self._step_state = ["reused" if (cached is not None and i < 4) else "pending" for i in range(len(fusion.STEPS))]
        for index, (dot, detail) in enumerate(self.step_rows):
            dot.configure(text_color=STEP_COLORS[self._step_state[index]])
            detail.configure(text=tr("reused") if self._step_state[index] == "reused" else "")
        self.progress.set(0)
        self.progress_label.configure(text="0 %")
        self.run_button.configure(state="disabled")
        self.fuse_button.configure(state="disabled")
        self.save_result_button.configure(state="disabled")
        self.cancel_button.configure(state="normal")
        self._set_state(tr("Fusing…"), theme.WARN)
        self.run_label.configure(text=tr("Fusion in progress…"), text_color=theme.TEXT_SOFT)
        self.status(tr("Fusion in progress…"))
        self.log(tr("Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), "
                    "×{scale}, {method}").format(first=request.first, last=request.last, ref=request.ref,
                                                 width=request.roi[2], height=request.roi[3], x=request.roi[0],
                                                 y=request.roi[1], scale=params.scale,
                                                 method=tr(fusion.METHOD_LABELS[params.method])))
        last_post = [0.0, -1]

        def progress(step: int, fraction: float, message: str) -> None:
            now = time.perf_counter()
            if fraction >= 1.0 or step != last_post[1] or now - last_post[0] >= PROGRESS_EVERY:
                last_post[0], last_post[1] = now, step
                self.tasks.post(self._pipeline_progress, step, fraction, message)

        def work():
            alignment = cached if cached is not None else fusion.align(request, params, progress, cancel)
            return alignment, fusion.fuse(alignment, params, progress, cancel)

        def ok(outcome) -> None:
            alignment, result = outcome
            self._running = None
            self._alignment, self._alignment_key = alignment, key
            self._result = result
            self._last_folder = None
            self._end_run()
            for index in range(len(fusion.STEPS)):
                if self._step_state[index] != "reused":
                    self._mark_step(index, "done")
                seconds = result.timings.get(index, 0.0)
                dot, detail = self.step_rows[index]
                if self._step_state[index] != "reused" and detail.cget("text"):
                    detail.configure(text=tr("{seconds:.2f} s  ·  {detail}").format(detail=detail.cget("text"),
                                                                                     seconds=seconds))
            self.progress.set(1)
            self.progress_label.configure(text="100 %")
            elapsed = time.perf_counter() - self._run_started
            noise = result.noise
            summary = tr("{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the "
                         "fusion  ·  {seconds:.1f} s").format(used=len(result.used), count=len(alignment.frames),
                                                             scale=result.final.shape[1] // alignment.request.roi[2],
                                                             ref=noise["reference"], fused=noise["fused"],
                                                             seconds=elapsed)
            self.run_label.configure(text=summary, text_color=theme.TEXT_SOFT)
            self.summary_label.configure(text=f"{result.final.shape[1]} × {result.final.shape[0]} px")
            self._set_state(tr("Fused"), theme.OK)
            self.status(tr("Fusion done: {summary}").format(summary=summary))
            self.log(tr("Fusion done: {summary}").format(summary=summary))
            for item in result.notes:
                self.log("  · " + str(item))
            excluded = [r for r in alignment.frames if not r.used]
            if excluded:
                reasons: dict[str, int] = {}
                for record in excluded:
                    reasons[record.reason] = reasons.get(record.reason, 0) + 1
                self.log("  " + tr("Excluded: {list}").format(
                    list=", ".join(f"{count} {tr(reason) if reason else '?'}" for reason, count in reasons.items())))
            self.save_result_button.configure(state="normal")
            self.before_view.reset()
            self._show_result()

        def failed(exc: BaseException) -> None:
            self._running = None
            self._end_run()
            running = next((i for i, state in enumerate(self._step_state) if state == "running"), None)
            if running is not None:
                self._mark_step(running, "error")
            if isinstance(exc, Cancelled):
                if self._rerun:
                    self._rerun = False
                    self.run_fusion()   # l'area e' cambiata mentre girava: si riparte con quella nuova
                    return
                self.run_label.configure(text=tr("Fusion cancelled."), text_color=theme.TEXT_DIM)
                self._set_state(tr("Ready"), theme.OK)
                self.status(tr("Fusion cancelled."))
                self.log(tr("Fusion cancelled by the user"))
                return
            self._set_state(tr("Error"), theme.ERR)
            self.run_label.configure(text=tr("Fusion failed: see the log."), text_color=theme.ERR)
            if isinstance(exc, fusion.PipelineError):
                self.log(tr("ERROR - {title}: {message}").format(title=tr("Fusion"), message=exc))
                self.status(str(exc))
                messagebox.showwarning(tr("Fusion"), str(exc), parent=self)
            else:
                self.error(tr("Fusion failed"), exc)

        self.tasks.run(work, on_ok=ok, on_error=failed, lane="fusion")

    def _end_run(self) -> None:
        self.run_button.configure(state="normal")
        self.fuse_button.configure(state="normal")
        self.cancel_button.configure(state="disabled")

    def _mark_step(self, index: int, state: str) -> None:
        self._step_state[index] = state
        self.step_rows[index][0].configure(text_color=STEP_COLORS[state])

    def _pipeline_progress(self, step: int, fraction: float, message: str) -> None:
        if self._running is None:
            return
        for index in range(step):
            if self._step_state[index] == "running":
                self._mark_step(index, "done")
        if self._step_state[step] != "running":
            self._mark_step(step, "running")
        self.step_rows[step][1].configure(text=message)
        overall = (step + max(0.0, min(1.0, fraction))) / len(fusion.STEPS)
        self.progress.set(overall)
        self.progress_label.configure(text=f"{int(overall * 100)} %")
        self.run_label.configure(text=f"{step + 1}. {tr(fusion.STEPS[step])}  ·  {message}", text_color=theme.TEXT_SOFT)

    def _cancel(self) -> None:
        if self._running is not None:
            self._running.set()

    # -------------------------------------------------------------- risultato

    @staticmethod
    def _to_image(array: np.ndarray) -> Image.Image:
        return Image.fromarray((np.clip(array, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8))

    def _show_result(self) -> None:
        result = self._result
        if result is None:
            return
        scale = result.final.shape[1] // result.alignment.request.roi[2]
        shown = result.final if self.view_menu.key == "final" else result.fused
        size = (result.final.shape[1], result.final.shape[0])
        if self.left_menu.key == "ghost":
            left, caption_text = result.ghost, tr("GHOST  ·  {count} FRAMES  ·  ×{scale}").format(
                count=len(result.used), scale=scale)
        else:
            left, caption_text = result.reference, tr("REFERENCE f{frame}  ·  BICUBIC ×{scale}").format(
                frame=result.alignment.request.ref, scale=scale)
        self.before_view.set_image(self._to_image(left), size)
        self.after_view.set_image(self._to_image(shown), size)
        self.after_view.set_view(self.before_view.view())
        self.left_caption.configure(text=caption_text)
        label = tr("RESULT  ·  {count} FRAMES").format(count=len(result.used))
        self.right_caption.configure(text=label)
        self._zoom_label()

    def _link(self, source: PreviewView, other: PreviewView) -> None:
        other.set_view(source.view())
        self._zoom_label()

    def _zoom_label(self) -> None:
        if self._result is None:
            return
        H, W = self._result.final.shape[:2]
        self.summary_label.configure(text=f"{W} × {H} px  ·  {self.before_view.zoom * 100:.0f} %")

    def save_result(self) -> None:
        """Scrive immagini e rapporto della fusione mostrata in una cartella nuova."""
        result = self._result
        if result is None or self._saving or self._running is not None:
            return
        base = self._output_dir()
        if base is None:
            base = result.alignment.request.info.path.parent
            if self.subfolder_var.get():
                base = base / result.alignment.request.info.path.stem
        fmt = self.format_var.get()
        bits = 8 if self.depth_var.get() == "8 bit" else 16
        save_aligned = bool(self.aligned_var.get())
        self._saving = True
        self.save_result_button.configure(state="disabled")
        self.run_button.configure(state="disabled")
        self.status(tr("Saving the result…"))

        def ok(folder: Path) -> None:
            self._saving = False
            self._last_folder = folder
            self.save_result_button.configure(state="normal")
            self.run_button.configure(state="normal")
            self.run_label.configure(text=tr("Saved in «{folder}».").format(folder=folder.name), text_color=theme.OK)
            self.status(tr("Saved in {folder}").format(folder=folder))
            self.log(tr("Result, comparison images and report saved in {folder}").format(folder=folder))

        def failed(exc: BaseException) -> None:
            self._saving = False
            self.save_result_button.configure(state="normal")
            self.run_button.configure(state="normal")
            self.error(tr("Save failed"), exc)

        self.tasks.run(lambda: report.save(result, base, fmt, bits, save_aligned,
                                           lambda message: self.tasks.post(self.status, message)),
                       on_ok=ok, on_error=failed, lane="save")

    # -------------------------------------------------------------- uscita

    def _choose_output(self) -> None:
        initial = self.out_var.get().strip() or str(Path.home())
        path = filedialog.askdirectory(parent=self, title=tr("Destination folder"), initialdir=initial)
        if path:
            self.out_var.set(path)
            self._refresh_example()

    def _output_dir(self) -> Path | None:
        base = self.out_var.get().strip()
        if not base:
            return None
        folder = Path(base)
        if self.subfolder_var.get() and self.info is not None:
            folder = folder / self.info.path.stem
        return folder

    def _refresh_example(self, *_args) -> None:
        if not hasattr(self, "example_label"):
            return
        folder = self._output_dir()
        if folder is None:
            where = tr("next to the video") + (tr(", in a subfolder named after it") if self.subfolder_var.get() else "")
        else:
            where = str(folder)
        ext = report.EXTENSIONS.get(self.format_var.get(), "png")
        bits = "8" if self.depth_var.get() == "8 bit" else "16"
        self.example_label.configure(text=tr(
            "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
            "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
            "SHA-256). Images at {bits} bits per channel.").format(where=where, ext=ext, bits=bits))

    def _open_folder(self) -> None:
        folder = self._last_folder or self._output_dir()
        if folder is None and self.info is not None:
            folder = self.info.path.parent
        if folder is None:
            return
        if not folder.is_dir():
            folder = folder.parent if folder.parent.is_dir() else None
        if folder is None:
            self.status(tr("The folder does not exist yet."))
            return
        try:
            os.startfile(str(folder))  # type: ignore[attr-defined]
        except (AttributeError, OSError) as exc:
            self.error(tr("Cannot open the folder"), exc)

    # -------------------------------------------------------------- helper UI

    def _set_state(self, text: str, color: str) -> None:
        self.state_dot.configure(text_color=color)
        self.state_label.configure(text=text)

    def status(self, message: str) -> None:
        self.status_label.configure(text=message)

    def log(self, message: str) -> None:
        line = f"[{dt.datetime.now():%H:%M:%S}] {message}"
        self.log_lines.append(line)
        del self.log_lines[:-LOG_MAX]
        self.log_box.configure(state="normal")
        self.log_box.insert("end", line + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def error(self, title: str, exc: BaseException | str) -> None:
        message = str(exc) or exc.__class__.__name__
        self.log(tr("ERROR - {title}: {message}").format(title=title, message=message))
        self.status(tr("Error: {title}").format(title=title))
        messagebox.showerror(title, message, parent=self)

    def _bug(self, trace: str) -> None:
        self.log(tr("INTERNAL ERROR") + "\n" + trace.rstrip())
        self.status(tr("Internal error: details in the log."))

    def _on_configure(self, event) -> None:
        if event.widget is self:
            if self._layout_job is not None:
                self.after_cancel(self._layout_job)
            self._layout_job = self.after(120, self._apply_layout)

    def _apply_layout(self) -> None:
        """Sulle finestre basse spariscono titolo della pagina e registro: lo spazio va alle immagini."""
        self._layout_job = None
        scale = theme.window_scaling(self)
        width, height = self.winfo_width() / scale, self.winfo_height() / scale
        if self.rail.user_choice is None:
            self.rail.set_collapsed(width < COLLAPSE_BELOW)
        if height >= PAGE_HEADER_ABOVE:
            self.page_head.grid()
        else:
            self.page_head.grid_remove()
        if height >= LOG_ABOVE:
            self.log_box.grid()
        else:
            self.log_box.grid_remove()

    def _busy_tick(self) -> None:
        busy = self.tasks.busy
        if busy != self._busy_shown:
            self._busy_shown = busy
            if busy:
                self.busy_bar.grid()
                self.busy_bar.start()
            else:
                self.busy_bar.stop()
                self.busy_bar.grid_remove()
        self.after(150, self._busy_tick)

    def _on_close(self) -> None:
        if self._running is not None:
            if not messagebox.askyesno(tr("Fusion in progress"), tr("The fusion is still running. Stop it and close?"),
                                       parent=self):
                return
            self._running.set()
        config = self.config_store
        params = self._read_params()
        config.set("output_dir", self.out_var.get().strip())
        config.set("subfolder", bool(self.subfolder_var.get()))
        config.set("format", self.format_var.get())
        config.set("depth", self.depth_var.get())
        config.set("save_aligned", bool(self.aligned_var.get()))
        for key in PARAM_KEYS:
            config.set(key, getattr(params, key))
        try:
            if self.state() == "normal":
                config.set("geometry", self.geometry())
        except tk.TclError:
            pass
        config.save()
        self.tasks.close()
        procs.kill_all()  # ffmpeg ancora in corso (anteprime, miniature, pipeline, download): via tutto
        self.destroy()


def run(video: str | None = None) -> None:
    App(video).mainloop()
