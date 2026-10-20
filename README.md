# FrameFusion

**English** · [Italiano](README.it.md)

Improves the legibility of a small detail — a license plate, a face, a
sign — filmed in several frames of a video. FrameFusion aligns those frames
with sub-pixel precision, fuses them on a finer grid, reduces noise and blur
and produces **one single image**, together with a report that documents
every parameter and every step.

**Author: Andrea Cumini — [www.osintinfo.net](https://www.osintinfo.net) — andrea@osintinfo.net**

**User manual, with screenshots:** [English](docs/manual/manual.en.md) · [Italiano](docs/manual/manual.it.md) · [Deutsch](docs/manual/manual.de.md) · [Français](docs/manual/manual.fr.md) · [Español](docs/manual/manual.es.md) · [Nederlands](docs/manual/manual.nl.md) · [Polski](docs/manual/manual.pl.md) · [Ελληνικά](docs/manual/manual.el.md) · [Shqip](docs/manual/manual.sq.md)

The technique is called **multi-frame super-resolution** (or multi-frame
image enhancement). Every frame samples the subject at a slightly different
position with respect to the pixel grid and carries independent noise:
combined after a precise alignment, the frames give a cleaner image with
more of the detail that was really recorded. Nothing is invented: the result
only contains what the frames support.

The interface is written in Python with **customtkinter**, in the same style
as AndrOsint, TagFaces and VideoSlicer (the Seity dark theme), from which
FrameFusion derives. Decoding is done by **ffmpeg**, run as a separate
program; image processing uses **OpenCV** and **NumPy**.

## The pipeline

| Step | What happens |
| --- | --- |
| 1. Frame extraction | The selected range is decoded by ffmpeg, exact to the frame (a reduced grey pass to look for the subject, then a full-resolution pass that keeps only the area around it). 10-bit and deeper sources are read at 16 bits. |
| 2. Subject detection | The subject, framed on the **reference frame**, is followed frame by frame, forwards and backwards, by normalized cross-correlation with motion prediction. Frames where it is lost are discarded. |
| 3. Local alignment | Each frame is aligned to the reference with the **ECC** algorithm (Evangelidis & Psarakis, 2008) on smoothed, reduced images: translation, rotation, affine or **perspective** (homography) model, so a vehicle that approaches or turns is compensated. If the chosen model does not converge on a frame, a simpler one is tried (written in the report). |
| 4. Sub-pixel registration | ECC is refined at full resolution. The most useful frames are then chosen: reliable alignment (ECC coefficient) and greatest sharpness (Laplacian energy on the aligned area). |
| 5. Multi-frame fusion | The chosen frames are resampled on a grid 1–4 times finer than the reference and combined: **robust mean** (weighted, outliers rejected pixel by pixel: reflections, occlusions, compression artifacts), **median**, or **shift-and-add** of the single samples with normalized convolution. Weights follow alignment quality and sharpness; brightness can be equalized to the reference. |
| 6. Deconvolution and denoising | Auto levels first (black and white at the 0.5 and 99.5 percentiles of the luminance), then, on the **luminance only** (in compressed video the color is at half resolution and carries noise, not detail: it is smoothed instead): optional bilateral filter and **Richardson-Lucy** deconvolution with a Gaussian PSF whose width is **measured on the edges of the fused image** (or chosen), a limited number of iterations and **total-variation regularization** (Dey et al., 2006), which holds the noise back. |
| 7. Single frame | Presentation (local contrast, grayscale — documented), the final image, the **ghost** (every frame used, superimposed at the position where it was found) and the reference frame enlarged with bicubic interpolation, for comparison. |

Steps 1–4 depend only on video, range, reference, area and motion model:
their outcome is kept, so changing the fusion and restoration parameters
re-runs only steps 5–7, in a fraction of a second.

## Requirements

- Windows 10/11 (on other systems it runs with the standard title bar)
- Python 3.10 or later (with Tkinter, included in the official installer)
- ffmpeg, as a **standalone** program: FrameFusion downloads it into the
  `tools/ffmpeg/` folder next to the program (see *FFmpeg* below); an
  ffmpeg already in the PATH is used too

Python dependencies (`requirements.txt`): `customtkinter`, `pillow`, `numpy`,
`opencv-python-headless` (4.8 or later; 5.x works too) and `fpdf2` (PDF
report).

```bash
python -m pip install -r requirements.txt
```

## Running

```bash
python FrameFusion.py
```

Or double-click `Avvia.bat` (it starts without a console window and uses the
`.venv` virtualenv if present). The video to open can be passed as an
argument: `python FrameFusion.py movie.mp4`.

## Usage

The interface has three pages, in the side bar (Ctrl+1 / 2 / 3).

1. **Configuration** — open the video (**Open video…**, Ctrl+O, or the icon
   in the VIDEO box at the top), choose the destination folder and the image
   format (PNG or TIFF, 16 bits per channel by default), download ffmpeg if
   it is missing, choose the language.
2. **Subject** — preview and timeline, as in VideoSlicer:
   - move to a frame where the subject is as clear as possible and **frame
     it**: drag with the **right mouse button** on the preview, or press
     **Select area** and drag with the left one. That frame becomes the
     **reference** (marker **R** on the timeline) and the fusion **starts by
     itself**; drawing a new area while it runs restarts it;
   - choose the range with **In [I]** / **Out [O]** (or by dragging the I and
     O flags): the frames in which the subject is visible. If the range is
     still the whole video, drawing the area sets it to 30 frames before and
     after the reference. **Fuse frames →** (or F5) runs the pipeline again
     after changing the range.
3. **Fusion** — parameters on the left, comparison on the right: on the left
   the **ghost** of the frames used (all of them superimposed, at the position
   where each was found) or the reference frame enlarged with bicubic
   interpolation; on the right the result (or the fusion before restoration).
   Zoom with the wheel and pan by dragging: the two views move together.
   Below, the seven steps with their outcome and time. **Run fusion** repeats
   it with new parameters, **Save result** (Ctrl+S) writes images and report.

### Saved settings

The *Saved settings* box at the top of the parameters column keeps named
sets of parameters: **Save…** asks for a name and writes the current
parameters into `config.json` at once; choosing a name in the menu loads
them; **Delete** removes the chosen set; **Defaults** puts every parameter
back to its default value. **From report…** loads the parameters written in
the `report.json` of a fusion saved earlier, so that an elaboration can be
repeated exactly. The parameters in use are also saved automatically when
the program closes.

### Parameters

| Parameter | Effect |
| --- | --- |
| Motion model | Translation, rotation + translation, affine, perspective (default). Perspective follows a subject that approaches, moves away or turns. |
| Subject search: minimum correlation | Below this score the subject counts as not found in a frame. |
| Minimum alignment quality (ECC) | Frames aligned with a lower coefficient are discarded (0.80 by default). |
| Sharpest frames kept | 75 % by default: the least sharp quarter (motion blur, frames far from the reference) is left out; 100 % keeps all the well aligned ones. |
| Scale | ×1 (noise reduction only) to ×4. ×2 or ×3 is usually the right choice: the gain depends on how many frames there are and how they are shifted. |
| Fusion method | Robust mean (default), shift-and-add with normalized convolution, median. |
| Weight by sharpness / Equalize brightness | Sharper frames count much more (fourth power of the relative sharpness); exposure changes are compensated. |
| Noise reduction | Off, light, medium, strong (bilateral filter, proportional to the estimated noise). |
| Deconvolution iterations / PSF σ | Richardson-Lucy: more iterations sharpen more but also amplify noise and halos. The automatic PSF is measured on the sharpest edges of the fused image (amplitude / maximum slope): about 0.8–1 px of the video on phone footage. Raise it if the characters stay soft, lower it if halos appear. |
| Regularization (total variation) | Off, light, medium (default), strong: holds the noise back during the deconvolution, so more iterations can be used. |
| Auto levels | Stretches the luminance so that the 0.5 and 99.5 percentiles become black and white (same line on every channel: colors do not change), before the deconvolution. On by default. |
| Local contrast (CLAHE) | Off, light, medium, strong: equalization by zones on the luminance. Useful on plates in shadow or against the light. |
| Grayscale | Drops the color: often cleaner for reading characters. |

## Output and report

**Save result** creates a new folder `fusion_f<reference>_<date-time>` in the
destination folder (in a subfolder named after the video, if chosen; next to
the video if no folder is set) with:

| File | Content |
| --- | --- |
| `result.png` | the final image |
| `fused.png` | the fusion before noise reduction and deconvolution |
| `ghost.png` | every frame used, superimposed at the position where it was found |
| `reference_x<k>.png` | the area of the reference frame enlarged with bicubic interpolation, for comparison |
| `reference_crop.png` | the same area at the video resolution |
| `aligned/` | on request, every frame used, aligned on the reference grid |
| `report.txt` | readable report, in the interface language |
| `report.pdf` | the same report laid out on A4 with the images (reference, result, ghost, fusion), the frame table and the SHA-256 fingerprints; fonts are taken from the system (Segoe UI and Consolas on Windows) |
| `report.json` | the same data in structured form, including the settings as the program uses them (**From report…** reloads them) |

The report contains the source (path, size, **SHA-256**, format), range,
reference frame, area, all parameters, the seven steps with the methods used
and their times, the table of the frames (tracking score, ECC coefficients,
sub-pixel shift, sharpness, weight, reason for exclusion, alignment matrix
in the JSON), noise estimates, sample density, sub-pixel phases covered and
the SHA-256 of every image written. Whoever reads it can repeat the
processing.

## Limits

- The result is an **enhancement** of the recorded frames, not a
  reconstruction of reality: it cannot recover what no frame contains. Fine
  details at the limit of the resolution, and characters that look alike
  (8/B, 0/D, 1/7), must be checked against the source frames.
- The gain is greatest with many frames, small shifts between them,
  independent noise and a sharp-enough reference. Motion blur within a
  single frame is not removed by the fusion.
- Strong compression (blocks, smearing) produces errors that are the same in
  consecutive frames: the fusion reduces them less than random noise.
- At most 300 frames per fusion; very large areas are processed on a
  reduced number of frames (written in the report).

## Single executable

```bash
.venv\Scripts\python.exe scripts\build_exe.py
```

installs PyInstaller into the virtualenv if it is missing and writes
`dist\FrameFusion.exe` (one file, no console window, "FF" icon and file
properties). ffmpeg is deliberately left out of the bundle: the executable
looks for it in `tools\ffmpeg\` next to itself and offers to download it.

`--release` also writes `dist\FrameFusion-<version>-windows-x64.zip` (exe,
LICENSE, NOTICE, README and a `licenses` folder with the license files of
Python and of the libraries inside the executable, taken from the virtualenv)
and `dist\release-notes-<version>.md`, with the changes from the most recent
section of `CHANGELOG.md`; `--publish` creates the GitHub release
`v<version>` on the repository of the `origin` remote (token from
`GITHUB_TOKEN` or typed when asked, never saved). Before a new release, raise
`__version__` in `framefusion/__init__.py` and add a section to
`CHANGELOG.md`.

## FFmpeg

ffmpeg is not included: it is a separate program under its own license. On
the first start, if no ffmpeg is found, the **Configuration** page opens on
the *FFmpeg* box: **Download / Update** takes the official Windows build
("release essentials") from <https://www.gyan.dev/ffmpeg/builds/>, the one
linked from the FFmpeg site, and keeps only `ffmpeg.exe`, `LICENSE` and
`README.txt` in `tools/ffmpeg/`. No installation, no change to the PATH.
**Check for updates** compares the installed release with the latest one.

## Language

The interface and the reports are in **English** (default), **Italian**,
**German**, **French**, **Spanish**, **Dutch**, **Polish**, **Greek** or
**Albanian**. Switch with the language buttons in the *Language* box of the
**Configuration** page: the change is immediate and saved in `config.json`.
Every language is a module in `framefusion/locales/` (English text →
translation); `scripts\check_i18n.py` checks that every text has its
translation in every language. The translations other than Italian were
produced with the help of a language model and have not been reviewed by
native speakers yet: corrections are welcome.

## Layout

| File | Content |
| --- | --- |
| `FrameFusion.py` | entry point |
| `framefusion/app.py` | main window |
| `framefusion/fusion.py` | the pipeline: tracking, ECC registration, fusion, deconvolution |
| `framefusion/report.py`, `pdfreport.py` | saving of images and report (text, JSON, PDF) |
| `framefusion/preview.py` | zoomable preview with subject area and linked views |
| `framefusion/timeline.py` | timeline with thumbnails, zoom, markers and reference |
| `framefusion/ffmpeg.py` | video information, previews, raw frames |
| `framefusion/tools.py` | ffmpeg lookup, download and update in `tools/` |
| `framefusion/i18n.py`, `locales/` | interface language and the translation catalogs (one module per language) |
| `framefusion/theme.py`, `widgets.py`, `shell.py`, `frameless.py` | dark theme, components, side bar, frameless window |
| `framefusion/tasks.py`, `procs.py` | background jobs; child processes tied to the application |
| `framefusion/config.py` | settings in `config.json` |
| `scripts/build_exe.py` | builds `FrameFusion.exe`; `--release` zip and notes; `--publish` GitHub release |
| `scripts/check_i18n.py` | checks the Italian translation |

## License

GNU GPL v3 with additional author-attribution terms: see
[LICENSE](LICENSE) and [NOTICE](NOTICE). The line

    Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net

must be kept in the source files, in the interface (window footer and
Credits box) and in the documentation. The program also writes it in the
reports: modified versions may keep it there, but need not. The name
"FrameFusion", the logo and the "FF" icon identify the original program: a
modified version distributed to others must use a different name and logo.

ffmpeg is a separate program under its own license (LGPL/GPL): see
<https://ffmpeg.org/legal.html>. Python and the libraries inside the
executable (CustomTkinter, Pillow, NumPy, OpenCV, fpdf2 and their dependencies)
remain under their own licenses: the release zip carries their license files
in the `licenses` folder.
