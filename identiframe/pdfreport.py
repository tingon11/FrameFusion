# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Rapporto in PDF: le stesse sezioni di report.txt, con le immagini, impaginate con fpdf2.

I caratteri vengono presi dal sistema (Segoe UI e Consolas su Windows, DejaVu
o Liberation altrove) e incorporati nel PDF come sottoinsieme: servono per i
simboli del rapporto (→ × σ λ ≥ « »). Se non se ne trova nessuno si usano i
caratteri di base del PDF (Helvetica, Courier) e i simboli vengono
traslitterati.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

import numpy as np
from fpdf import FPDF
from fpdf.enums import TableBordersLayout, XPos, YPos
from fpdf.fonts import FontFace
from PIL import Image

from . import APP_NAME, CREDITS
from .fusion import aligned_frame
from .i18n import tr, upper

PAGE_MARGIN = 15          # mm
IMAGE_MIN_WIDTH = 1200    # pixel: le immagini piccole vengono ingrandite (pixel interi) prima di incorporarle
THUMB_MIN_WIDTH = 240     # pixel: lo stesso per le miniature dei fotogrammi fusi
THUMB_COLUMNS = 6
COLORS = {"text": (30, 34, 40), "dim": (110, 118, 130), "accent": (74, 99, 181), "rule": (200, 205, 214)}

# (famiglia, file normale, file grassetto) nelle cartelle dei caratteri di sistema
UI_CANDIDATES = (("segoeui.ttf", "segoeuib.ttf"), ("arial.ttf", "arialbd.ttf"),
                 ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf"), ("LiberationSans-Regular.ttf", "LiberationSans-Bold.ttf"))
MONO_CANDIDATES = (("consola.ttf", "consolab.ttf"), ("CascadiaMono.ttf", "CascadiaMono.ttf"),
                   ("DejaVuSansMono.ttf", "DejaVuSansMono-Bold.ttf"),
                   ("LiberationMono-Regular.ttf", "LiberationMono-Bold.ttf"), ("cour.ttf", "courbd.ttf"))
# caratteri di riserva per le scritte lette in altri alfabeti (cinese, giapponese, coreano, indiano, thai...):
# caricati solo se il rapporto contiene caratteri che quelli principali non hanno
FALLBACK_CANDIDATES = ("msyh.ttc", "msjh.ttc", "YuGothR.ttc", "malgun.ttf", "Nirmala.ttc", "LeelawUI.ttf",
                       "ebrima.ttf", "seguisym.ttf", "NotoSansCJK-Regular.ttc", "DejaVuSans.ttf")
# fontTools segnala le tabelle che non sa ridurre (MERG di Segoe UI): non e' un problema
logging.getLogger("fontTools").setLevel(logging.ERROR)

ASCII = {"→": "->", "×": "x", "σ": "sigma", "λ": "lambda", "≥": ">=", "«": '"', "»": '"', "—": "-", "·": "-",
         "…": "...", "≈": "~", "°": " deg"}


def _font_dirs() -> list[Path]:
    dirs = []
    if sys.platform == "win32":
        dirs.append(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts")
        dirs.append(Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Windows" / "Fonts")
    dirs += [Path("/usr/share/fonts"), Path("/usr/local/share/fonts"), Path.home() / ".fonts",
             Path("/Library/Fonts"), Path("/System/Library/Fonts")]
    return [d for d in dirs if d.is_dir()]


def _find_font(candidates) -> tuple[Path, Path] | None:
    dirs = _font_dirs()
    for regular, bold in candidates:
        for folder in dirs:
            found = list(folder.rglob(regular))[:1]
            if found:
                bold_found = list(folder.rglob(bold))[:1]
                return found[0], bold_found[0] if bold_found else found[0]
    return None


class _Pdf(FPDF):
    """A4 con piede fisso: crediti dell'autore e numero di pagina."""

    def __init__(self) -> None:
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(PAGE_MARGIN, PAGE_MARGIN, PAGE_MARGIN)
        self.set_auto_page_break(auto=True, margin=PAGE_MARGIN + 4)
        self.ui, self.mono = "Helvetica", "Courier"
        self.unicode = False
        ui = _find_font(UI_CANDIDATES)
        mono = _find_font(MONO_CANDIDATES)
        if ui is not None and mono is not None:
            self.add_font("ui", "", str(ui[0]))
            self.add_font("ui", "B", str(ui[1]))
            self.add_font("mono", "", str(mono[0]))
            self.add_font("mono", "B", str(mono[1]))
            self.ui, self.mono, self.unicode = "ui", "mono", True
        self.set_text_shaping(False)
        self.alias_nb_pages()

    def cover(self, texts) -> None:
        """Aggiunge i caratteri di riserva che servono a scrivere `texts` (cinese, coreano...), se ce ne sono."""
        if not self.unicode:
            return
        known = set(self.fonts["ui"].cmap) & set(self.fonts["mono"].cmap)
        missing = {ord(c) for text in texts for c in str(text) if ord(c) > 0x7F and ord(c) not in known}
        found = []
        for name in FALLBACK_CANDIDATES:
            if not missing:
                break
            path = next((hit for folder in _font_dirs() for hit in list(folder.rglob(name))[:1]), None)
            if path is None:
                continue
            family = f"fallback{len(found)}"
            try:
                self.add_font(family, "", str(path))
            except Exception:  # noqa: BLE001 - un carattere illeggibile si salta
                continue
            covered = missing & set(self.fonts[family].cmap)
            if covered:
                found.append(family)
                missing -= covered
        if found:
            self.set_fallback_fonts(found, exact_match=False)

    def t(self, text: str) -> str:
        """Il testo come lo possono scrivere i caratteri in uso."""
        text = str(text)
        if self.unicode:
            return text
        for char, plain in ASCII.items():
            text = text.replace(char, plain)
        return text.encode("latin-1", "replace").decode("latin-1")

    def footer(self) -> None:
        self.set_y(-PAGE_MARGIN)
        self.set_font(self.mono, "", 7)
        self.set_text_color(*COLORS["dim"])
        self.cell(0, 5, self.t(f"{APP_NAME}  ·  {CREDITS}"), new_x=XPos.LMARGIN, new_y=YPos.TOP, align="L")
        self.cell(0, 5, self.t(tr("page {page} of {pages}").format(page=self.page_no(), pages="{nb}")), align="R")

    @property
    def usable(self) -> float:
        return self.w - self.l_margin - self.r_margin

    def heading(self, text: str) -> None:
        self.ln(3)
        self.set_font(self.mono, "B", 8)
        self.set_text_color(*COLORS["accent"])
        self.cell(0, 5, self.t(upper(text)), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(*COLORS["rule"])
        self.line(self.l_margin, self.get_y(), self.l_margin + self.usable, self.get_y())
        self.ln(1.5)
        self.set_text_color(*COLORS["text"])

    def paragraph(self, text: str, size: float = 9, family: str | None = None, dim: bool = False) -> None:
        self.set_font(family or self.ui, "", size)
        self.set_text_color(*(COLORS["dim"] if dim else COLORS["text"]))
        self.multi_cell(0, size * 0.5, self.t(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*COLORS["text"])

    def key_values(self, rows, label_width: float = 62, mono_values: bool = False) -> None:
        self.set_font(self.ui, "", 9)
        with self.table(col_widths=(label_width, self.usable - label_width), borders_layout=TableBordersLayout.NONE,
                        first_row_as_headings=False, line_height=4.6, padding=(0.6, 0, 0.6, 0)) as table:
            for label, value in rows:
                row = table.row()
                self.set_font(self.ui, "", 9)
                self.set_text_color(*COLORS["dim"])
                row.cell(self.t(label))
                self.set_font(self.mono if mono_values else self.ui, "", 8 if mono_values else 9)
                self.set_text_color(*COLORS["text"])
                row.cell(self.t(value))
        self.set_text_color(*COLORS["text"])


def _pil(array: np.ndarray, min_width: int = IMAGE_MIN_WIDTH) -> Image.Image:
    """Immagine a 8 bit, ingrandita a pixel interi finche' e' larga almeno `min_width`."""
    image = Image.fromarray((np.clip(array, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8))
    factor = max(1, int(np.ceil(min_width / max(1, image.width))))
    if factor > 1:
        image = image.resize((image.width * factor, image.height * factor), Image.NEAREST)
    return image


def _images(pdf: _Pdf, pairs: list[tuple[np.ndarray, str]], width: float) -> None:
    """Immagini affiancate (due per riga), con didascalia sotto."""
    gap = 4
    line = 3.2
    x0 = pdf.l_margin
    pdf.set_font(pdf.mono, "", 7)
    for start in range(0, len(pairs), 2):
        row = pairs[start:start + 2]
        heights, lines = [], []
        for array, caption in row:
            h, w = array.shape[:2]
            heights.append(width * h / w)
            lines.append(len(pdf.multi_cell(width, line, pdf.t(caption), dry_run=True, output="LINES")))
        row_height = max(h + 1 + n * line for h, n in zip(heights, lines))
        if pdf.get_y() + row_height + 6 > pdf.h - pdf.b_margin:
            pdf.add_page()
        y = pdf.get_y()
        for column, (array, caption) in enumerate(row):
            x = x0 + column * (width + gap)
            pdf.image(_pil(array), x=x, y=y, w=width)
            pdf.set_xy(x, y + heights[column] + 1)
            pdf.set_font(pdf.mono, "", 7)
            pdf.set_text_color(*COLORS["dim"])
            pdf.multi_cell(width, line, pdf.t(caption), align="L")
        pdf.set_xy(x0, y + row_height + 5)
        pdf.set_text_color(*COLORS["text"])


def _thumbs(pdf: _Pdf, result, frames: list[int]) -> None:
    """Miniature di tutti i fotogrammi fusi, allineati al riferimento come entrano nella fusione."""
    records = {r.index: r for r in result.alignment.frames}
    ref = result.alignment.request.ref
    gap, line = 2.5, 3.0
    width = (pdf.usable - gap * (THUMB_COLUMNS - 1)) / THUMB_COLUMNS
    for start in range(0, len(frames), THUMB_COLUMNS):
        row = [records[n] for n in frames[start:start + THUMB_COLUMNS]]
        images = [aligned_frame(result, record) for record in row]
        height = max(width * image.shape[0] / image.shape[1] for image in images)
        if pdf.get_y() + height + line + 3 > pdf.h - pdf.b_margin:
            pdf.add_page()
        y = pdf.get_y()
        for column, (record, image) in enumerate(zip(row, images)):
            x = pdf.l_margin + column * (width + gap)
            pdf.image(_pil(image, THUMB_MIN_WIDTH), x=x, y=y, w=width)
            pdf.set_xy(x, y + height + 0.6)
            pdf.set_font(pdf.mono, "", 6.3)
            pdf.set_text_color(*COLORS["dim"])
            label = f"f{record.index}  ·  {record.weight:.3f}" + ("  ·  R" if record.index == ref else "")
            pdf.cell(width, line, pdf.t(label), align="L")
        pdf.set_xy(pdf.l_margin, y + height + line + 2.5)
    pdf.set_text_color(*COLORS["text"])


def _strings(value):
    """Tutti i testi di una struttura di liste e tuple."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _strings(item)


def write(path: Path, document, result) -> None:
    """Scrive il rapporto `document` (vedi report.sections) con le immagini di `result` in `path`."""
    pdf = _Pdf()
    pdf.cover(_strings([document.title, document.credits, document.created]
                       + [[section.title, section.rows, section.head, section.extra] for section in document.sections]))
    pdf.set_title(pdf.t(document.title))
    pdf.set_author(pdf.t(CREDITS))
    pdf.set_creator(pdf.t(f"{APP_NAME}"))
    pdf.add_page()

    # intestazione
    pdf.set_font(pdf.ui, "B", 15)
    pdf.set_text_color(*COLORS["text"])
    pdf.cell(0, 8, pdf.t(document.title), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font(pdf.mono, "", 8)
    pdf.set_text_color(*COLORS["accent"])
    pdf.cell(0, 4.5, pdf.t(document.credits), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(*COLORS["dim"])
    pdf.cell(0, 4.5, pdf.t(document.created), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    # immagini: riferimento e risultato grandi, poi ghost e fusione
    half = (pdf.usable - 4) / 2
    ref = result.alignment.request.ref
    scale = result.final.shape[1] // result.alignment.request.roi[2]
    _images(pdf, [
        (result.reference, tr("Reference f{frame}  ·  bicubic ×{scale}").format(frame=ref, scale=scale)),
        (result.final, tr("Result  ·  {count} frames").format(count=len(result.used))),
    ], half)
    quarter = (pdf.usable - 4) / 2 * 0.62
    _images(pdf, [
        (result.ghost, tr("Ghost  ·  {count} frames, each at the position where it was found").format(
            count=len(result.used))),
        (result.fused, tr("Fusion before restoration")),
    ], quarter)

    for section in document.sections:
        pdf.heading(section.title)
        if section.kind == "kv":
            pdf.key_values(section.rows, mono_values=section.mono)
        elif section.kind == "steps":
            for number, (name, seconds, description) in enumerate(section.rows, start=1):
                pdf.set_font(pdf.ui, "B", 9)
                pdf.cell(0, 5, pdf.t(f"{number}. {name}  ({seconds:.2f} s)"), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.paragraph(description, size=8.5)
                pdf.ln(0.8)
            for note in section.extra:
                pdf.paragraph("· " + note, size=8.5, dim=True)
        elif section.kind == "table":
            widths = section.widths
            total = sum(widths)
            pdf.set_font(pdf.mono, "", 6.3)
            with pdf.table(col_widths=tuple(w * pdf.usable / total for w in widths),
                           borders_layout=TableBordersLayout.HORIZONTAL_LINES, line_height=3.4,
                           text_align=tuple(section.aligns), padding=(0.4, 0.6, 0.4, 0.6),
                           headings_style=FontFace(emphasis="BOLD", color=COLORS["dim"], fill_color=(240, 242, 246)),
                           repeat_headings=1) as table:
                head = table.row()
                for cell in section.head:
                    head.cell(pdf.t(cell))
                for cells in section.rows:
                    row = table.row()
                    for cell in cells:
                        row.cell(pdf.t(cell))
        elif section.kind == "thumbs":
            for line in section.extra:
                pdf.paragraph(line, size=8.5, dim=True)
            pdf.ln(1.5)
            _thumbs(pdf, result, section.rows)
        elif section.kind == "files":
            pdf.key_values(section.rows, label_width=40, mono_values=True)
            for line in section.extra:
                pdf.paragraph(line, size=8.5, dim=True)
        else:
            for text in section.rows:
                pdf.paragraph(text, size=9)
                pdf.ln(1)
    pdf.output(str(path))
