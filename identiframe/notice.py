# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Avviso all'avvio: che cosa produce IdentiFrame, da accettare prima di usarlo.

Copre la finestra sotto l'intestazione finche' non si accetta. Se la lingua
non e' ancora stata scelta la chiede prima, con il nome di ogni lingua scritto
in quella lingua, e l'avviso compare nella lingua scelta. Il pulsante per
continuare si abilita solo dopo aver spuntato la dichiarazione: il risultato
e' una ricostruzione dai fotogrammi, in cui nulla e' inventato, mentre la
lettura dei caratteri e il paese sono stime.
"""

from __future__ import annotations

from typing import Callable

import customtkinter as ctk

from . import APP_NAME, theme
from .i18n import N_, tr, upper
from .locales import LANGUAGES, catalog

WIDTH = 760          # larghezza del riquadro dell'avviso
CHOOSE = N_("Choose the language")   # scritto in tutte le lingue insieme: la lingua non e' ancora nota


class StartNotice(ctk.CTkFrame):
    def __init__(self, master, fonts: theme.Fonts, ask_language: bool,
                 on_language: Callable[[str], None], on_accept: Callable[[], None],
                 on_exit: Callable[[], None]) -> None:
        super().__init__(master, fg_color=theme.BG, corner_radius=0)
        self.fonts = fonts
        self._on_language = on_language
        self._on_accept = on_accept
        self._on_exit = on_exit
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._page: ctk.CTkFrame | None = None
        if ask_language:
            self._show_languages()
        else:
            self._show_notice()

    def _card(self, accent: str) -> ctk.CTkFrame:
        if self._page is not None:
            self._page.destroy()
        page = self._page = ctk.CTkFrame(self, fg_color=theme.PANEL, border_width=1, border_color=theme.BORDER,
                                         corner_radius=4, width=WIDTH)
        page.grid(row=0, column=0, padx=24, pady=24)
        ctk.CTkFrame(page, height=2, corner_radius=0, border_width=0, fg_color=accent).pack(
            fill="x", padx=1, pady=(1, 0))
        return page

    def _show_languages(self) -> None:
        """La lingua non e' ancora nota: il titolo in tutte le lingue, un pulsante per lingua."""
        page = self._card(theme.ACCENT)
        titles = [catalog(code).get(CHOOSE, CHOOSE) for code in LANGUAGES]
        ctk.CTkLabel(page, text=APP_NAME.upper(), font=self.fonts.caption, text_color=theme.TEXT_DIM,
                     anchor="w").pack(fill="x", padx=24, pady=(18, 2))
        ctk.CTkLabel(page, text="  ·  ".join(titles), font=self.fonts.body, text_color=theme.TEXT_SOFT,
                     justify="left", anchor="w", wraplength=WIDTH - 48).pack(fill="x", padx=24, pady=(0, 14))
        grid = ctk.CTkFrame(page, fg_color="transparent", corner_radius=0)
        grid.pack(fill="x", padx=24, pady=(0, 22))
        for index, (code, name) in enumerate(LANGUAGES.items()):
            ctk.CTkButton(
                grid, text=f"{name}   {code.upper()}", width=(WIDTH - 48 - 16) // 3, height=34, corner_radius=4,
                font=self.fonts.bold, fg_color=theme.NEUTRAL, hover_color=theme.NEUTRAL_HOVER,
                text_color=theme.TEXT, anchor="w", command=lambda c=code: self._language_chosen(c),
            ).grid(row=index // 3, column=index % 3, padx=(0 if index % 3 == 0 else 8, 0), pady=(0, 8))

    def _language_chosen(self, code: str) -> None:
        self._on_language(code)
        self._show_notice()

    def _show_notice(self) -> None:
        page = self._card(theme.WARN)
        wrap = WIDTH - 48
        head = ctk.CTkFrame(page, fg_color="transparent", corner_radius=0)
        head.pack(fill="x", padx=24, pady=(18, 4))
        ctk.CTkLabel(head, text="●", font=(theme.mono_font(), 11), text_color=theme.WARN).pack(side="left")
        ctk.CTkLabel(head, text=upper(tr("Before you start")), font=self.fonts.caption,
                     text_color=theme.TEXT_DIM).pack(side="left", padx=(6, 0))
        ctk.CTkLabel(page, text=tr("What {app} produces").format(app=APP_NAME), font=self.fonts.page,
                     text_color=theme.TEXT, anchor="w").pack(fill="x", padx=24, pady=(0, 8))

        sections = (
            (tr("How the result is obtained"), theme.ACCENT,
             tr("{app} does not create images: it combines the information really present in many frames of the "
                "same video. It follows the area you draw from frame to frame, aligns each frame to the reference "
                "frame with sub-pixel precision, discards the frames that do not align reliably and fuses the "
                "others with a weighted average that resists outliers. Each frame records the subject with a "
                "slightly different shift and different noise: combined, the noise drops and details spread over "
                "several frames emerge (multi-frame super-resolution). The deconvolution and the contrast "
                "corrections that follow are deterministic operations, with all their parameters written in the "
                "report.").format(app=APP_NAME)),
            (tr("The result is a reconstruction"), theme.OK,
             tr("The image obtained is a reconstruction computed only from the real pixels of the frames used, "
                "each one listed in the report with its weight. No generative model or artificial intelligence "
                "adds, completes or imagines details: what is in none of the frames cannot appear in the result. "
                "A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, "
                "halos from the deconvolution) and is only as good as the source: always compare it with the "
                "original frames.")),
            (tr("Character reading and country are estimates"), theme.WARN,
             tr("The character reading (OCR) and the country of the plate are instead estimates of recognition "
                "models trained on examples, which always propose the most probable characters. The program "
                "combines several readings and marks as «?» or illegible what does not reach its thresholds, but "
                "even a reading shown in green can be wrong. They are an aid, not a proof: check every character "
                "by eye on the image.")),
        )
        for title, color, text in sections:
            row = ctk.CTkFrame(page, fg_color="transparent", corner_radius=0)
            row.pack(fill="x", padx=24, pady=(6, 0))
            ctk.CTkFrame(row, fg_color=color, width=2, height=11, corner_radius=0).pack(side="left", padx=(0, 7))
            ctk.CTkLabel(row, text=upper(title), font=self.fonts.title, text_color=color, anchor="w").pack(
                side="left")
            ctk.CTkLabel(page, text=text, font=self.fonts.body, text_color=theme.TEXT_SOFT, justify="left",
                         anchor="w", wraplength=wrap).pack(fill="x", padx=24, pady=(3, 0))

        self._understood = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            page, text=tr("I have understood that the result is a reconstruction from the frames of the video, in "
                          "which nothing is invented, while the character reading and the attribution of the "
                          "country are estimates to be checked."),
            variable=self._understood, command=self._toggle, font=self.fonts.bold, text_color=theme.TEXT,
            checkbox_width=18, checkbox_height=18,
        ).pack(fill="x", padx=24, pady=(16, 0))
        # il testo di CTkCheckBox non va a capo da solo
        page.after_idle(lambda: self._wrap_checkbox(page, wrap - 30))

        buttons = ctk.CTkFrame(page, fg_color="transparent", corner_radius=0)
        buttons.pack(fill="x", padx=24, pady=(16, 20))
        self._accept = ctk.CTkButton(buttons, text=tr("Accept and continue"), width=180, height=32,
                                     corner_radius=4, font=self.fonts.button, state="disabled",
                                     command=self._on_accept)
        self._accept.pack(side="right")
        ctk.CTkButton(buttons, text=tr("Exit"), width=96, height=32, corner_radius=4, font=self.fonts.button,
                      fg_color="transparent", hover_color=theme.HOVER, border_width=1,
                      border_color=theme.BORDER_STRONG, text_color=theme.TEXT,
                      command=self._on_exit).pack(side="right", padx=(0, 8))

    @staticmethod
    def _wrap_checkbox(page, width: int) -> None:
        for child in page.winfo_children():
            if isinstance(child, ctk.CTkCheckBox):
                # _text_label e' un tk.Label: la larghezza va in pixel reali
                child._text_label.configure(wraplength=int(width * theme.scaling(child)), justify="left")

    def _toggle(self) -> None:
        self._accept.configure(state="normal" if self._understood.get() else "disabled")
