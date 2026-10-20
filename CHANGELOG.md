# Changelog

The most recent section is used by `scripts/build_exe.py --release` as the
release notes: first a one-line introduction, then the list of changes.

## 1.0.0

First public release: fuses several frames of a video into one enhanced image of a small detail (plate, face, sign), with a report that documents every step.

- **Seven-step pipeline**: frame extraction, subject detection, local alignment, sub-pixel registration, multi-frame fusion, deconvolution and denoising, single frame.
- **Subject area** drawn on the reference frame (right-drag, or Select area): the fusion starts by itself; the subject is followed through the range by normalized cross-correlation.
- **ECC registration** with translation, rotation, affine or perspective model (simpler models as fallback), refined to sub-pixel precision; frames chosen by alignment quality and sharpness.
- **Fusion** on a ×1–×4 grid: robust mean with outlier rejection, median, or shift-and-add with normalized convolution; brightness equalization and sharpness weights.
- **Restoration** on the luminance only: optional bilateral denoising, Richardson-Lucy deconvolution with total-variation regularization and a PSF measured on the edges of the fused image (or chosen); auto levels, local contrast (CLAHE) and grayscale.
- **Linked before/after comparison** (ghost of the frames used, or the reference frame, next to the result) with zoom down to the single pixel; changing only fusion or restoration parameters re-runs the last steps in a fraction of a second.
- **Saved settings**: named parameter sets in `config.json`, defaults with one button, parameters reloaded from the `report.json` of an earlier fusion.
- **Report** in text, JSON and PDF (with the images): source SHA-256, range, reference, area, parameters, steps, per-frame table, noise estimates and SHA-256 of every image written; optional aligned frames.
- Preview, zoomable timeline and ffmpeg downloader inherited from VideoSlicer; interface and reports in English, Italian, German, French, Spanish, Dutch, Polish, Greek and Albanian, switchable at any time.
