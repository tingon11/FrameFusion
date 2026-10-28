# Changelog

The most recent section is used by `scripts/build_exe.py --release` as the
release notes: first a one-line introduction, then the list of changes.

## 1.1.1

First release of IdentiFrame, the continuation of FrameFusion 1.0.1 under a new name (FrameFusion is already the name of a commercial product doing the same kind of work), with a mode made for faces and the reading of plates and texts.

- **New name**: FrameFusion becomes IdentiFrame, with its own logo and "IF" icon. Settings (`config.json`), saved reports and the `tools` folder with ffmpeg work as before.
- **Subject type**, on the Subject page: *Plate* and *Text* (one rigid alignment per frame, as before; they differ in the character reading) or *Face*. With a face, after the ECC model every frame receives a **local non-rigid refinement** (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) that follows expression and head movement; a **per-pixel confidence** (forward-backward consistency of the flow and local correlation) weights every sample in the fusion; frames whose **pose or expression differs** from the reference are left out; outside the ellipse inscribed in the area the samples count little and the result shows the reference frame; the auto levels are gentler on skin and shadows.
- **Plausible alignments only**: a motion model that converges to a deformation the subject cannot have (local scale, shear or perspective beyond the limits) is replaced by a simpler one, for every subject type; the report says on how many frames.
- **Defaults per subject type**: for faces the affine motion model, 10 deconvolution iterations, strong regularization and light noise reduction, to avoid bent faces, halos and the "plastic" look on skin. *Defaults* and the change of type load them.
- **Report**: subject type, the local refinement with mean similarity and displacement, perspective and similarity columns in the frame table, and a note on the limits of face enhancement and on the size of the face in the video.
- **Character reading (OCR)** after every fusion of a plate or a text: the result and eight fusions of independent groups of frames are read and voted character by character, weighted by the probability the model gives each character. Plates are read by **fast-plate-ocr** (MIT), which also shows the **possible country** of the plate among 65 (in yellow next to the characters when the model gives one country the majority of the votes on a reading it considers legible; otherwise, with its share, among the details); texts by **PaddleOCR PP-OCRv6** (Apache 2.0), which finds the text lines and reads them in many languages and alphabets. Since the models always propose some characters, even on an image where nothing can be read, a line below 60 % model confidence is shown as **illegible** and a character with less than 50 % of the weighted votes as **«?»**; both thresholds are written in the report. The Pipeline box shows the reading with its agreement, the model confidence, the doubtful positions and the look-alike characters to check by eye; the report gets the reading, the vote by position and the single readings, and the PDF uses the system fonts for other scripts (Chinese, Japanese, Korean...).
- **OCR models outside the program**: the two models (about 37 MB) are run by OpenCV, already in the program, and downloaded on request into `tools/ocr` from the *OCR models* box of the Configuration page, each file checked against its SHA-256 fingerprint, with licenses and origin saved next to them. Without them the program works as usual, without the character reading.
- **Built-in presets**: Plate 01–05, Text 01–05 and Face 01–05 in the Saved settings menu, shown for the subject type chosen, with a line describing each; they cannot be changed or deleted, and your own settings follow.
- **Notice at start**: every start opens with a notice, in the interface language, explaining the technique and that the result is a reconstruction from the real pixels of the frames, in which nothing is invented, while the character reading and the country are estimates; it must be accepted by ticking that this is understood. On the very first start the language is asked first.
- **Preview playback**: one play / pause button between the frame buttons of the Subject page (Space). A single ffmpeg process decodes ahead of the cursor at the size of the preview and a clock keeps the pace of the video, so playback is smooth also on 4K videos.
- **Result zoom**: the comparison views can be zoomed out below the fitted size, to see the result small; buttons −, +, 1:1 and Fit under the views, and the − + 0 keys on the Fusion page.
- **Larger preview**: a button next to *Save frame* (or F11) hides the timeline and gives its height to the preview, useful with vertical phone videos; the choice is remembered. The zoom shown above the preview now follows the size of the box.
- **Preview colours**: the reduced preview frames keep the accurate colour conversion (full-resolution chroma, exact rounding), as the saved frame and the fusion already did.
- **Executable without FFmpeg**: the FFmpeg library shipped inside the OpenCV package (LGPL) is left out of the build, which now goes through a generated spec file and checks the result; the release zip carries the license files of Python and of every bundled library in `licenses/`, listed in the release notes.
- **Automatic range**: drawing the area sets In and Out to 30 seconds before and after the reference, only as limits of the search; the subject is followed outwards from the reference while the frames are decoded, the search stops in each direction after one second without the subject, and In and Out then close on the frames where it was followed (a range moved by hand is left as it is). A subject visible for long, such as a parked vehicle, is no longer cut at 301 frames (now at most 3601 in the range), an isolated look-alike far from the tracked frames can no longer enter the fusion (and when the subject is covered and the search latches onto something else, the frames after more than one second without a good alignment are left out, with a note in the report), and with a moving vehicle the search is faster because the frames after it leaves are not decoded. The subject is now searched at full resolution in most videos (before, reduced to fit 301 frames in memory).
- **Report**: the frames actually examined next to the range set with I / O, the counts referred to them, and the exact list of the frames that make up the result (also in the frame table and in `report.json`); the PDF shows a thumbnail of every frame used, aligned as it enters the fusion, with its number and weight.
- **Large areas**: the shift-and-add fusion of a large area (more than about 32,000 pixels) no longer stops with an OpenCV error (`cv::remap`, `SHRT_MAX`).
- License texts (NOTICE, README) reviewed: attribution terms within GPLv3 section 7(b), third-party software and downloaded models listed completely, notes on the Panchang typeface and on the three test videos.

## FrameFusion 1.0.1

The range now follows the reference frame: every new selection places it 150 frames before and 150 after.

- **Automatic range**: every time the subject area is drawn, In and Out move to 150 frames before and 150 after the reference frame (within the video), also on a new selection; at most 301 frames per fusion (was 300).
- **Timeline ruler**: labels no longer overlap when zoomed in close to single frames.
- Release notes: language list and link to the user manual.

## FrameFusion 1.0.0

First public release: fuses several frames of a video into one enhanced image of a small detail (plate, face, sign), with a report that documents every step.

- **Seven-step pipeline**: frame extraction, subject detection, local alignment, sub-pixel registration, multi-frame fusion, deconvolution and denoising, single frame.
- **Subject area** drawn on the reference frame (right-drag, or Select area): the fusion starts by itself; the subject is followed through the range by normalized cross-correlation.
- **ECC registration** with translation, rotation, affine or perspective model (simpler models as fallback), refined to sub-pixel precision; frames chosen by alignment quality and sharpness.
- **Fusion** on a ×1–×4 grid: robust mean with outlier rejection, median, or shift-and-add with normalized convolution; brightness equalization and sharpness weights.
- **Restoration** on the luminance only: optional bilateral denoising, Richardson-Lucy deconvolution with total-variation regularization and a PSF measured on the edges of the fused image (or chosen); auto levels, local contrast (CLAHE) and grayscale.
- **Linked before/after comparison** (ghost of the frames used, or the reference frame, next to the result) with zoom down to the single pixel; changing only fusion or restoration parameters re-runs the last steps in a fraction of a second.
- **Saved settings**: named parameter sets in `config.json`, defaults with one button, parameters reloaded from the `report.json` of an earlier fusion.
- **Report** in text, JSON and PDF (with the images): source SHA-256, range, reference, area, parameters, steps, per-frame table, noise estimates and SHA-256 of every image written; optional aligned frames.
- Preview, zoomable timeline and ffmpeg downloader; interface and reports in English, Italian, German, French, Spanish, Dutch, Polish, Greek and Albanian, switchable at any time.
