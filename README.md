# IdentiFrame

**English** · [Italiano](README.it.md)

Improves the legibility of a small detail — a license plate, a face, a
sign — filmed in several frames of a video. IdentiFrame aligns those frames
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

IdentiFrame is the continuation, under a new name, of FrameFusion by the same
author, with a mode made for faces and the reading of plates and texts. The
interface is written in Python with **customtkinter**. Decoding is done by
**ffmpeg**, run as a separate program; image processing uses **OpenCV** and
**NumPy**.

## About the name

IdentiFrame was published until version 1.0.1 as **FrameFusion**. That name
is already used by a commercial product that does the same kind of work, so
to avoid any confusion the program continues as IdentiFrame, with a new name,
logo and icon. The code, the reports and the settings carry on from
FrameFusion 1.0.1; the old releases stay available on this repository, and
links to the old FrameFusion repository lead here.

## The pipeline

| Step | What happens |
| --- | --- |
| 1. Frame extraction | The selected range is decoded by ffmpeg, exact to the frame (a reduced grey pass to look for the subject, then a full-resolution pass that keeps only the area around it). 10-bit and deeper sources are read at 16 bits. |
| 2. Subject detection | The subject, framed on the **reference frame**, is followed frame by frame, forwards and backwards, by normalized cross-correlation with motion prediction. Frames where it is lost are discarded. |
| 3. Local alignment | Each frame is aligned to the reference with the **ECC** algorithm (Evangelidis & Psarakis, 2008) on smoothed, reduced images: translation, rotation, affine or **perspective** (homography) model, so a vehicle that approaches or turns is compensated. If the chosen model does not converge on a frame, or converges to a deformation that is not a possible motion of the subject (local scale, shear or perspective beyond the limits), a simpler one is tried (written in the report). With the subject type **Face**, after the rigid model every frame also receives a **local non-rigid refinement** (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) that follows expression and head movement, with a per-pixel confidence (forward-backward consistency of the flow and local correlation). |
| 4. Sub-pixel registration | ECC is refined at full resolution. The most useful frames are then chosen: reliable alignment (ECC coefficient) and greatest sharpness (Laplacian energy on the aligned area). With a face, frames whose local similarity to the reference is too low (pose or expression changed) are left out. |
| 5. Multi-frame fusion | The chosen frames are resampled on a grid 1–4 times finer than the reference and combined: **robust mean** (weighted, outliers rejected pixel by pixel: reflections, occlusions, compression artifacts), **median**, or **shift-and-add** of the single samples with normalized convolution. Weights follow alignment quality and sharpness, and with a face the local confidence of every sample; brightness can be equalized to the reference. |
| 6. Deconvolution and denoising | Auto levels first (black and white at the 0.5 and 99.5 percentiles of the luminance; 0.1 and 99.9 for a face), then, on the **luminance only** (in compressed video the color is at half resolution and carries noise, not detail: it is smoothed instead): optional bilateral filter and **Richardson-Lucy** deconvolution with a Gaussian PSF whose width is **measured on the edges of the fused image** (or chosen), a limited number of iterations and **total-variation regularization** (Dey et al., 2006), which holds the noise back. |
| 7. Single frame | Presentation (local contrast, grayscale — documented), the final image, the **ghost** (every frame used, superimposed at the position where it was found) and the reference frame enlarged with bicubic interpolation, for comparison. |

Steps 1–4 depend only on video, range, reference, area, motion model and
subject type: their outcome is kept, so changing the fusion and restoration
parameters re-runs only steps 5–7, in a fraction of a second.

## Requirements

- Windows 10/11 (on other systems it runs with the standard title bar)
- Python 3.10 or later (with Tkinter, included in the official installer)
- ffmpeg, as a **standalone** program: IdentiFrame downloads it into the
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
python IdentiFrame.py
```

Or double-click `Avvia.bat` (it starts without a console window and uses the
`.venv` virtualenv if present). The video to open can be passed as an
argument: `python IdentiFrame.py movie.mp4`.

## Usage

The interface has three pages, in the side bar (Ctrl+1 / 2 / 3).

At every start a notice explains the technique and asks to confirm that the
result is a reconstruction from the real pixels of the frames, in which
nothing is invented, while the character reading and the country are
estimates to be checked; on the very first start the language is asked
first.

1. **Configuration** — open the video (**Open video…**, Ctrl+O, or the icon
   in the VIDEO box at the top), choose the destination folder and the image
   format (PNG or TIFF, 16 bits per channel by default), download ffmpeg if
   it is missing, choose the language.
2. **Subject** — preview and timeline:
   - choose the **subject type** in the *Subject* box: *Plate*, *Text* or
     *Face* (see *Subject type* below);
   - move to a frame where the subject is as clear as possible and **frame
     it**: drag with the **right mouse button** on the preview, or press
     **Select area** and drag with the left one. That frame becomes the
     **reference** (marker **R** on the timeline) and the fusion **starts by
     itself**; drawing a new area while it runs restarts it;
   - choose the range with **In [I]** / **Out [O]** (or by dragging the I and
     O flags): the frames in which the subject is visible. Every time the
     area is drawn, the range is set to 30 seconds before and 30 after the
     reference (within the video), only as limits of the search: the fusion
     follows the subject outwards from the reference, stops in each direction
     after one second without it, and then closes In and Out on the frames
     where it was followed. A range moved by hand is left as it is.
     **Fuse frames →** (or F5) runs the pipeline again after changing the
     range.
3. **Fusion** — parameters on the left, comparison on the right: on the left
   the **ghost** of the frames used (all of them superimposed, at the position
   where each was found) or the reference frame enlarged with bicubic
   interpolation; on the right the result (or the fusion before restoration).
   Zoom with the wheel and pan by dragging: the two views move together.
   Below, the seven steps with their outcome and time. **Run fusion** repeats
   it with new parameters, **Save result** (Ctrl+S) writes images and report.

### Subject type

The menu next to **Select area**, on the **Subject** page, says what is being
enhanced.
**Plate** and **Text**: a flat, rigid subject, described by one motion model
per frame; they differ in the character reading (fast-plate-ocr for plates,
PaddleOCR for texts, see below). **Face**: a head turns and an expression changes between frames, so
after the rigid alignment every frame receives a local non-rigid refinement
that follows these movements within a few pixels; the parts that still
differ count less, frames with a different pose or expression are left out,
the restoration is lighter (10 iterations, strong regularization, light
noise reduction, to avoid halos and the "plastic" look on skin) and the auto
levels are gentler on skin and shadows. Changing the type loads its defaults
and runs the alignment again. The report writes which type was used, the
mean similarity and displacement of the refinement, a similarity column in
the frame table and a note on the size of the face in the video: below about
60 pixels of width the fusion can improve the overall appearance, not reveal
identifying features. Nothing generative is used: the refinement only moves
by a few pixels what the frames contain. For a face the motion model is
**affine** by default: on a face of a few dozen pixels a homography bends
itself to raise the correlation, and perspective is not a real motion of a
head. Outside the ellipse inscribed in the area the samples count little and
the result shows the reference frame, because the background moves
differently from the face.

### Saved settings

The menu always starts with five **built-in presets** for the subject type
chosen on the Subject page, which cannot be changed or deleted: **Plate 01**
standard, **02** night or noisy, **03** distant small plate (×3,
shift-and-add), **04** moving vehicle with motion blur, **05** shadow or
backlight; **Text 01–05** the same cases for texts; **Face 01** standard, **02** night or noisy, **03** minimal
processing (no noise reduction, no deconvolution), **04** distant small face
(×3), **05** shadow or backlight. A line under the menu describes the one
chosen. Your own settings follow.

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
| Subject type (Subject page) | Plate (default), Text or Face: see above. Changing it loads the defaults of that type. |
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

### Character reading (OCR)

With the OCR models downloaded (see *OCR models* below), after every fusion
of a *Plate* or a *Text* the **CHARACTERS** line of the *Pipeline* box shows
the characters read; **Read characters** repeats the reading. No single frame
of a small plate is readable by an OCR, so the reading is made on the result
and on **eight fusions of independent groups of frames** (alternate frames by
sharpness, each group fused and restored with the same parameters). The
readings are aligned to the most representative one and voted **character by
character**, weighted by the probability the model gives each character
(Quiala et al., 2023).

- **Plate**: [fast-plate-ocr](https://github.com/ankandrew/fast-plate-ocr)
  reads the whole plate (the area, or the light rectangle of the plate found
  inside it) and also estimates the **plate format**, the country, among 65:
  an estimate from the look of the plate, not a check.
- **Text**: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) PP-OCRv6
  finds the text lines in the result and reads each one, in many languages
  and alphabets; every line is voted on its own.

The line gives the agreement between the readings, the **model confidence**
(mean probability of the characters read: concordant readings with low
confidence are usually illegible text read the same way every time), the
*doubtful* positions (agreement below 70 %, or a similar shape as runner up)
and, on plates, the characters to **check by eye** (8/B, 0/D/O, 1/I, 5/S,
2/Z, 6/G: a model can misread them the same way in every reading, and the
vote cannot see it). The report gets a section with the reading, the vote by
position and the single readings.

The models always propose the most probable characters, even where nothing
can be read: a line is shown only from a model confidence of 60 %, otherwise
it is **illegible**, and a character with less than 50 % of the weighted
votes is shown as **«?»**. The country appears in yellow next to the
characters only on a legible reading with one country holding the majority
of the votes. Reading and country remain estimates: always compare with the
image.

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
sub-pixel shift, sharpness, perspective weight of the warp, weight, reason
for exclusion, alignment matrix in the JSON), noise estimates, sample density, sub-pixel phases covered and
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
- At most 3601 frames in the range; very large areas are processed on a
  reduced number of frames (written in the report).

## Single executable

```bash
.venv\Scripts\python.exe scripts\build_exe.py
```

installs PyInstaller into the virtualenv if it is missing, writes a spec file
in `build\` and builds `dist\IdentiFrame.exe` (one file, no console window,
"IF" icon and file properties). FFmpeg is deliberately left out of the bundle
in every form: the executable looks for `ffmpeg.exe` in `tools\ffmpeg\` next
to itself and offers to download it, and the FFmpeg library that the OpenCV
package ships (LGPL, used only by OpenCV's own video reading, which
IdentiFrame does not use) is removed from the build, which checks that it is
absent.

`--release` also writes `dist\IdentiFrame-<version>-windows-x64.zip` (exe,
LICENSE, NOTICE, README and a `licenses` folder with the license files of
Python and of the libraries inside the executable, taken from the virtualenv)
and `dist\release-notes-<version>.md`, with the changes from the most recent
section of `CHANGELOG.md`; `--publish` creates the GitHub release
`<version>` on the repository of the `origin` remote (token from
`GITHUB_TOKEN` or typed when asked, never saved). Before a new release, raise
`__version__` in `identiframe/__init__.py` and add a section to
`CHANGELOG.md`.

## OCR models

The character reading uses two neural network models in ONNX format, run by
OpenCV (already part of the program): they are optional, never included in
the executable, and downloaded on request by the **OCR models** box of the
**Configuration** page into `tools/ocr/`, about 37 MB in all. Without them
IdentiFrame works as usual: fusion, restoration and reports do not change,
only the character reading is missing.

| Folder | Model | License | Source |
| --- | --- | --- | --- |
| `tools/ocr/plate/` | fast-plate-ocr `cct-s-v2-global` with its configuration | MIT (code and weights, confirmed by the author in [issue 97](https://github.com/ankandrew/fast-plate-ocr/issues/97)) | [release arg-plates](https://github.com/ankandrew/fast-plate-ocr/releases/tag/arg-plates) |
| `tools/ocr/text/` | PaddleOCR PP-OCRv6 small, text detection and recognition, with the character list | Apache 2.0 (weights by Baidu / PaddleOCR; ONNX conversion by RapidOCR, Apache 2.0) | [RapidOCR 3.10.0 models](https://www.modelscope.cn/models/RapidAI/RapidOCR) |

Every file is checked against its SHA-256 fingerprint, written in
`identiframe/tools.py`, and every network is loaded once by OpenCV before it
is kept; the license texts and a `SOURCE.txt` with origin and fingerprints
are saved next to the models. OpenCV 5.0 computes Tanh through an
exponential that overflows for inputs above about 44: when loading,
IdentiFrame puts a Clip(-40, 40) in front of every Tanh of the network in
memory (tanh(±40) is already ±1 in single precision), so the outputs are the
same as onnxruntime's; the files on disk are left untouched.

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
Every language is a module in `identiframe/locales/` (English text →
translation); `scripts\check_i18n.py` checks that every text has its
translation in every language. The translations other than Italian were
produced with the help of a language model and have not been reviewed by
native speakers yet: corrections are welcome.

## Layout

| File | Content |
| --- | --- |
| `IdentiFrame.py` | entry point |
| `identiframe/app.py` | main window |
| `identiframe/fusion.py` | the pipeline: tracking, ECC registration, fusion, deconvolution |
| `identiframe/report.py`, `pdfreport.py` | saving of images and report (text, JSON, PDF) |
| `identiframe/preview.py` | zoomable preview with subject area and linked views |
| `identiframe/timeline.py` | timeline with thumbnails, zoom, markers and reference |
| `identiframe/ffmpeg.py` | video information, previews, raw frames |
| `identiframe/tools.py` | ffmpeg and OCR models lookup, download and update in `tools/` |
| `identiframe/i18n.py`, `locales/` | interface language and the translation catalogs (one module per language) |
| `identiframe/theme.py`, `widgets.py`, `shell.py`, `frameless.py` | dark theme, components, side bar, frameless window |
| `identiframe/tasks.py`, `procs.py` | background jobs; child processes tied to the application |
| `identiframe/config.py` | settings in `config.json` |
| `identiframe/ocr.py` | character reading: group fusions, fast-plate-ocr and PaddleOCR through OpenCV, vote by position |
| `scripts/build_exe.py` | builds `IdentiFrame.exe` (spec file without the OpenCV FFmpeg library); `--release` zip, licenses and notes; `--publish` GitHub release |
| `scripts/make_brand.py` | regenerates logo and icon (needs the Panchang font) |
| `scripts/check_i18n.py` | checks that every text has its translation in every language |

## License

GNU GPL v3 with additional author-attribution terms: see
[LICENSE](LICENSE) and [NOTICE](NOTICE). The line

    Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net

must be kept in the source files, in the interface (window footer and
Credits box) and in the documentation. The program also writes it in the
reports: modified versions may keep it there, but need not. The name
"IdentiFrame", the logo and the "IF" icon identify the original program: a
modified version distributed to others must use a different name and logo.

ffmpeg is a separate program under its own license (LGPL/GPL): see
<https://ffmpeg.org/legal.html>. Python and the libraries inside the
executable (CustomTkinter, Pillow, NumPy, OpenCV, fpdf2 and their dependencies)
remain under their own licenses: the release zip carries their license files
in the `licenses` folder. The OCR models are not part of the program either:
see *OCR models* above for their licenses and origin.

### Font

The logo and the icon are set in **Panchang**, a typeface by Indian Type
Foundry (ITF) distributed by [Fontshare](https://www.fontshare.com/fonts/panchang)
under the ITF Free Font License; ITF owns its trademarks and copyright. The
images of the logo and of the icon contain outlines and pixels only: the font
itself is not distributed with IdentiFrame, and `scripts/make_brand.py` needs
it installed to regenerate them.

### Test videos

The program was tested, and the screenshots of the user manual were made,
with three videos from Pexels, used under the
[Pexels license](https://www.pexels.com/license/):

| Subject | Video | Author |
| --- | --- | --- |
| Vehicles and plates | [Busy Highway Traffic at Sunset](https://www.pexels.com/it-it/video/traffico-autostradale-intenso-al-tramonto-31779728/) | [Şeyhmus Kino](https://www.pexels.com/@seyhmuskino/) |
| Texts | [Street traffic in Taipei, Taiwan](https://www.pexels.com/it-it/video/citta-auto-traffico-veicoli-13271103/) | [Levi Wedge](https://www.pexels.com/@levi-wedge-266970209/) |
| Face | [Charming European Street with Cyclist](https://www.pexels.com/it-it/video/affascinante-strada-europea-con-ciclista-33476096/) | [Tuba Din](https://www.pexels.com/@tubadinn/) |

The plates, the texts and the face visible in the documentation belong to
that footage.
