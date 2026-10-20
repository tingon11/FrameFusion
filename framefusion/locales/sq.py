# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Shqip: përkthimi i teksteve të ndërfaqes dhe të raportit.

Çelësi është teksti anglisht ashtu siç shfaqet në kod (në tr() dhe N_()),
vlera është përkthimi i tij. Vendmbajtësit në kllapa gjarpërore mbeten të pandryshuar.
Çelësat e papërkthyer mbeten në anglisht. Pas çdo ndryshimi:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py
"""

from __future__ import annotations

NAME = "Shqip"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Ndërfaqja nuk mund të niset: {error}\n\n"
        "Instaloni varësitë me:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg nuk u gjet. Shkarkojeni nga kutia FFmpeg e faqes Konfigurimi, "
        "ose instalojeni dhe vendoseni në PATH.",
    "Cannot check the latest ffmpeg version: {error}": "Nuk mund të kontrollohet versioni më i fundit i ffmpeg: {error}",
    "Unexpected answer from the ffmpeg download site.": "Përgjigje e papritur nga faqja e shkarkimit të ffmpeg.",
    "Downloading {label}": "Po shkarkohet {label}",
    "Download of {label} failed: {error}": "Shkarkimi i {label} dështoi: {error}",
    "Invalid archive: suspicious path '{member}'.": "Arkiv i pavlefshëm: shteg i dyshimtë '{member}'.",
    "The downloaded file is not a valid zip archive.": "Skedari i shkarkuar nuk është një arkiv zip i vlefshëm.",
    "The downloaded package does not contain {name}.": "Paketa e shkarkuar nuk përmban {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Nuk mund të përditësohet '{name}': skedarët janë në përdorim. Prisni përfundimin e shkrirjes "
        "në vazhdim dhe provoni përsëri.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Shkarkimi automatik është i disponueshëm vetëm në Windows: instalojeni ffmpeg me "
        "menaxherin e paketave të sistemit.",
    "Extracting ffmpeg": "Po nxirret ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "Versioni i shkarkuar i ffmpeg nuk niset në këtë kompjuter.",
    "{name} is missing after extraction.": "{name} mungon pas nxjerrjes.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Po kontrollohet…",
    "Check": "Kontrollo",
    "Check for updates": "Kontrollo për përditësime",
    "Download / Update": "Shkarko / Përditëso",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg është një program i veçantë (LGPL/GPL). Shkarkimi merr versionin zyrtar për "
        "Windows nga {url} dhe mban vetëm ffmpeg.exe, LICENSE dhe README në dosjen tools\\ffmpeg "
        "pranë programit: pa instalim, pa ndryshime në PATH.",
    "ffmpeg check failed": "Kontrolli i ffmpeg dështoi",
    "tools folder": "dosja tools",
    "system PATH": "PATH i sistemit",
    "Python package": "paketë Python",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Motori: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Mungon: shkarkojeni me butonin në të djathtë.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg nuk u gjet: shkarkojeni nga kutia FFmpeg e faqes Konfigurimi.",
    "ffmpeg missing: download it from the FFmpeg box.": "ffmpeg mungon: shkarkojeni nga kutia FFmpeg.",
    "Checking the latest ffmpeg version…": "Po kontrollohet versioni më i fundit i ffmpeg…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} është i përditësuar.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Versioni i fundit: {latest}. I instaluar: {installed}. Dëshironi ta shkarkoni tani?",
    "Update check failed": "Kontrolli për përditësime dështoi",
    "Wait for the running fusion, then try again.": "Prisni përfundimin e shkrirjes në vazhdim, pastaj provoni përsëri.",
    "Downloading ffmpeg…": "Po shkarkohet ffmpeg…",
    "Downloading ffmpeg from {url}": "Po shkarkohet ffmpeg nga {url}",
    "ffmpeg downloaded into {path}": "ffmpeg u shkarkua në {path}",
    "Download cancelled.": "Shkarkimi u anulua.",
    "ffmpeg download failed": "Shkarkimi i ffmpeg dështoi",
    "ffmpeg: exit code {code}": "ffmpeg: kodi i daljes {code}",
    "File not found: {path}": "Skedari nuk u gjet: {path}",
    "The file has no recognizable video track.": "Skedari nuk ka asnjë gjurmë video të njohshme.",
    "Video size not recognized.": "Përmasat e videos nuk u njohën.",
    "Frame rate not recognized.": "Shpejtësia e kuadrove nuk u njoh.",
    "Invalid frame rate.": "Shpejtësi e pavlefshme e kuadrove.",
    "Unknown video duration (stream or damaged file).":
        "Kohëzgjatje e panjohur e videos (transmetim ose skedar i dëmtuar).",
    "Zero video duration.": "Kohëzgjatja e videos është zero.",
    "No frame at {seconds:.3f} s.": "Asnjë kuadër në {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg nuk e shkroi skedarin.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "KONFIRMIM",
    "WARNING": "KUJDES",
    "ERROR": "GABIM",
    "Yes": "Po",

    # ----------------------------------------------------------- navigazione
    "PAGES": "FAQET",
    "Configuration": "Konfigurimi",
    "Subject": "Subjekti",
    "Frames, subject and reference": "Kuadrot, subjekti dhe referenca",
    "Fusion": "Shkrirja",
    "Multi-frame fusion and result": "Shkrirja me shumë kuadro dhe rezultati",
    "{app}  /  PAGE {index:02d}": "{app}  /  FAQJA {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "asnjë",
    "Open video… (Ctrl+O)": "Hap video… (Ctrl+O)",
    "No video": "Asnjë video",
    "Reading…": "Po lexohet…",
    "Ready": "Gati",
    "Error": "Gabim",
    "Fusing…": "Po shkrihet…",
    "Fused": "E shkrirë",

    # ------------------------------------------------------------- anteprima
    "Preview": "Parapamja",
    "Open a video to see the preview": "Hapni një video për të parë parapamjen",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "zvarritje me të djathtën: zona e subjektit  ·  rrotulla: zmadhim  ·  zvarritje: lëvizje  ·  klik i dyfishtë: përshtatje",
    "First frame (Home)": "Kuadri i parë (Home)",
    "Back 10 frames (Shift+←)": "10 kuadro prapa (Shift+←)",
    "Previous frame (←)": "Kuadri i mëparshëm (←)",
    "Next frame (→)": "Kuadri tjetër (→)",
    "Forward 10 frames (Shift+→)": "10 kuadro përpara (Shift+→)",
    "Last frame (End)": "Kuadri i fundit (End)",
    "Save frame": "Ruaj kuadrin",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Ruan kuadrin e shfaqur me rezolucion të plotë, pa humbje (Ctrl+S)",
    "Preview unavailable: {error}": "Parapamja nuk është e disponueshme: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+rrotull: zmadhim  ·  rrotulla: rrëshqitje  ·  zvarritni I / O dhe kursorin  ·  klik i dyfishtë mbi vizore: e gjitha",
    "In  [I]": "Fillimi  [I]",
    "Out  [O]": "Fundi  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Vendos fillimin e përzgjedhjes te kursori (tasti I)",
    "Sets the end of the selection at the cursor (key O)":
        "Vendos fundin e përzgjedhjes te kursori (tasti O)",
    "Moves the cursor to the start of the selection": "Çon kursorin në fillim të përzgjedhjes",
    "Moves the cursor to the end of the selection": "Çon kursorin në fund të përzgjedhjes",
    "CURSOR": "KURSORI",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Koha (1:23.456, 83.4) ose kuadri (f2000), pastaj Enter",
    "Zoom out (−)": "Zvogëlo (−)",
    "Zoom in (+)": "Zmadho (+)",
    "All": "E gjitha",
    "Selection": "Përzgjedhja",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Përzgjedhja: f{first} → f{last}  ·  {count} kuadro  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Pamja: {start} → {end}  ({seconds:.3f} s, {frames:.1f} kuadro)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Koha nuk u njoh: përdorni mm:ss.mmm, sekonda ose f<numër>.",
    "Open a video to see the timeline": "Hapni një video për të parë vijën kohore",

    # -------------------------------------------------------------- soggetto
    "Select area": "Zgjidh zonën",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Pastaj zvarritni mbi parapamje për të rrethuar subjektin (ose zvarritni me të djathtën në çdo moment); "
        "shkrirja nis vetë",
    "Moves the cursor to the reference frame": "Çon kursorin te kuadri i referencës",
    "Clear": "Pastro",
    "Fuse frames  →": "Shkrij kuadrot  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Nis shkrirjen me shumë kuadro në intervalin e zgjedhur (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Rrethoni subjektin në një kuadër të qartë: ai kuadër bëhet referenca dhe shkrirja nis.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Zvarritni mbi parapamje për të rrethuar subjektin (Esc për të ndaluar).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "Zona e subjektit është shumë e vogël: vizatoni të paktën {size} × {size} piksel.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Intervali u vendos rreth referencës: f{first} → f{last}. Lëvizni I / O për ta ndryshuar.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Zona e subjektit {width} × {height} në ({x}, {y}) mbi kuadrin e referencës f{frame}",
    "Subject area cleared.": "Zona e subjektit u pastrua.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Referenca f{frame} është jashtë intervalit f{first} → f{last}: lëvizni I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} kuadro në interval: zgjidhni më së shumti {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Zona {width} × {height} px në ({x}, {y})  ·  referenca f{frame}  ·  {count} kuadro f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Zgjidhni fillimisht zonën e subjektit (targë, fytyrë, objekt) në një kuadër të qartë: zvarritni me të "
        "djathtën mbi parapamje, ose përdorni Zgjidh zonën.",
    "The reference frame must be inside the selected range.":
        "Kuadri i referencës duhet të jetë brenda intervalit të zgjedhur.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "Intervali ka {count} kuadro: zgjidhni më së shumti {limit} rreth referencës.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Kuadrot dhe rreshtimi",
    "Motion model": "Modeli i lëvizjes",
    "Translation": "Zhvendosje",
    "Rotation + translation": "Rrotullim + zhvendosje",
    "Affine": "Afin",
    "Perspective (homography)": "Perspektivë (homografi)",
    "Subject search: minimum correlation": "Kërkimi i subjektit: korrelacioni minimal",
    "Minimum alignment quality (ECC)": "Cilësia minimale e rreshtimit (ECC)",
    "Sharpest frames kept": "Kuadrot më të mprehta që mbahen",
    "Scale": "Zmadhimi",
    "Fusion method": "Metoda e shkrirjes",
    "Robust mean (outliers rejected)": "Mesatare e qëndrueshme (vlerat anomale përjashtohen)",
    "Shift-and-add (normalized convolution)": "Zhvendosje dhe mbledhje (konvolucion i normalizuar)",
    "Median": "Mediana",
    "Weight by sharpness": "Pesho sipas mprehtësisë",
    "Equalize brightness": "Barazo ndriçimin",
    "Restoration": "Restaurimi",
    "Noise reduction": "Reduktimi i zhurmës",
    "Off": "Asnjë",
    "Light": "E lehtë",
    "Medium": "Mesatare",
    "Strong": "E fortë",
    "Deconvolution iterations": "Iteracionet e dekonvolucionit",
    "0 (none)": "0 (asnjë)",
    "not applied": "nuk zbatohet",
    "PSF σ (output pixels)": "PSF σ (piksel të daljes)",
    "Automatic": "Automatike",
    "Regularization (total variation)": "Rregullarizimi (variacioni total)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Më shumë iteracione mprehin më shumë, por përforcojnë edhe zhurmën dhe aureolat; rregullarizimi e "
        "frenon zhurmën. Ndryshoni pak nga pak dhe krahasoni.",
    "Presentation": "Paraqitja",
    "Auto levels": "Nivele automatike",
    "Local contrast (CLAHE)": "Kontrast lokal (CLAHE)",
    "Grayscale": "Shkallë gri",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Nivelet janë një vijë e drejtë e zbatuar para dekonvolucionit (e zeza dhe e bardha në përqindëset "
        "0,5 dhe 99,5); kontrasti lokal një barazim sipas zonave. Gjithçka shkruhet në raport.",
    "Defaults": "Parazgjedhjet",
    "Puts every parameter of the pipeline back to its default value":
        "Kthen çdo parametër të pipeline-it në vlerën e tij të parazgjedhur",
    "Parameters back to their defaults.": "Parametrat u kthyen në vlerat e parazgjedhura.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Cilësime të ruajtura",
    "(none saved)": "(asnjë e ruajtur)",
    "Save…": "Ruaj…",
    "Saves the current parameters under a name (in config.json)":
        "Ruan parametrat aktualë me një emër (në config.json)",
    "Delete": "Fshi",
    "From report…": "Nga raporti…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Ngarkon parametrat e shkruar në report.json të një shkrirjeje të ruajtur",
    "Save settings": "Ruaj cilësimet",
    "Name of these settings:": "Emri i këtyre cilësimeve:",
    "Settings «{name}» already exist. Replace them?": "Cilësimet «{name}» ekzistojnë tashmë. Dëshironi t'i zëvendësoni?",
    "Settings «{name}» saved.": "Cilësimet «{name}» u ruajtën.",
    "Settings «{name}» loaded.": "Cilësimet «{name}» u ngarkuan.",
    "Delete settings": "Fshi cilësimet",
    "Delete the settings «{name}»?": "Të fshihen cilësimet «{name}»?",
    "Settings «{name}» deleted.": "Cilësimet «{name}» u fshinë.",
    "Load parameters from a report": "Ngarko parametrat nga një raport",
    "Cannot read the report": "Raporti nuk mund të lexohet",
    "{name} is not a FrameFusion report.": "{name} nuk është një raport i FrameFusion.",
    "Parameters loaded from {path}": "Parametrat u ngarkuan nga {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Krahasimi",
    "FRAMES": "KUADROT",
    "RESULT": "REZULTATI",
    "Ghost of the frames": "Fantazma e kuadrove",
    "Reference frame": "Kuadri i referencës",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "FANTAZMA  ·  {count} KUADRO  ·  ×{scale}",
    "Final": "Përfundimtar",
    "Fusion only": "Vetëm shkrirja",
    "Draw the subject area on the Subject page, then run the fusion":
        "Vizatoni zonën e subjektit në faqen Subjekti, pastaj nisni shkrirjen",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "rrotulla: zmadhim  ·  zvarritje: lëvizje  ·  klik i dyfishtë: përshtatje  ·  dy pamjet lëvizin bashkë  ·  "
        "fantazma: çdo kuadër i përdorur, i mbivendosur në pozicionin ku u gjet",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "REFERENCA f{frame}  ·  BIKUBIKE ×{scale}",
    "RESULT  ·  {count} FRAMES": "REZULTATI  ·  {count} KUADRO",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Nxjerrja e kuadrove",
    "Subject detection": "Zbulimi i subjektit",
    "Local alignment": "Rreshtimi lokal",
    "Sub-pixel registration": "Regjistrimi nënpiksel",
    "Multi-frame fusion": "Shkrirja me shumë kuadro",
    "Deconvolution and denoising": "Dekonvolucioni dhe reduktimi i zhurmës",
    "Single frame": "Kuadër i vetëm",
    "Save result": "Ruaj rezultatin",
    "Saves images and report in a new folder (Ctrl+S)": "Ruan imazhet dhe raportin në një dosje të re (Ctrl+S)",
    "Run fusion": "Nis shkrirjen",
    "Runs the pipeline again with these parameters (F5)": "Ekzekuton përsëri pipeline-in me këta parametra (F5)",
    "Open folder": "Hap dosjen",
    "Cancel": "Anulo",
    "reused": "i ripërdorur",
    "Fusion in progress…": "Shkrirja në vazhdim…",
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Shkrirja: f{first} → f{last}, referenca f{ref}, zona {width} × {height} në ({x}, {y}), ×{scale}, {method}",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} nga {count} kuadro  ·  ×{scale}  ·  zhurma σ {ref:.1f} → {fused:.1f} pas shkrirjes  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Shkrirja përfundoi: {summary}",
    "Excluded: {list}": "Të përjashtuara: {list}",
    "Fusion cancelled.": "Shkrirja u anulua.",
    "Fusion cancelled by the user": "Shkrirja u anulua nga përdoruesi",
    "Fusion failed: see the log.": "Shkrirja dështoi: shihni regjistrin.",
    "Fusion failed": "Shkrirja dështoi",
    "Fusion in progress": "Shkrirja në vazhdim",
    "The fusion is still running. Stop it and close?": "Shkrirja është ende në vazhdim. Dëshironi ta ndaloni dhe të mbyllni?",
    "Saving the result…": "Po ruhet rezultati…",
    "Saved in «{folder}».": "U ruajt në «{folder}».",
    "Saved in {folder}": "U ruajt në {folder}",
    "Result, comparison images and report saved in {folder}":
        "Rezultati, imazhet e krahasimit dhe raporti u ruajtën në {folder}",

    # messaggi dei passaggi (fusion.py)
    "{done} / {total} frames decoded": "{done} / {total} kuadro të dekoduara",
    "{count} frames decoded": "{count} kuadro të dekoduara",
    "The video ended before the reference frame.": "Videoja përfundoi para kuadrit të referencës.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Kërkimi i subjektit mbi kuadro të zvogëluara në {percent:.0f} % (kufi i memories).",
    "searching the subject: {done} / {total}": "po kërkohet subjekti: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "U mbajt një kuadër në çdo {stride} (kufi i memories për zona të mëdha).",
    "{done} / {total} frames read at full resolution": "{done} / {total} kuadro të lexuara me rezolucion të plotë",
    "The reference frame could not be read.": "Kuadri i referencës nuk mund të lexohej.",
    "subject found in {found} / {total} frames": "subjekti u gjet në {found} / {total} kuadro",
    "{done} / {total} frames aligned": "{done} / {total} kuadro të rreshtuara",
    "motion model: {model}": "modeli i lëvizjes: {model}",
    "{done} / {total} frames registered": "{done} / {total} kuadro të regjistruara",
    "{count} frames registered": "{count} kuadro të regjistruara",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} kuadro u rreshtuan me një model lëvizjeje më të thjeshtë, sepse modeli i zgjedhur nuk "
        "konvergonte mbi to.",
    "{count} frames selected": "{count} kuadro të zgjedhura",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Vetëm {count} kuadro të përdorshme: rezultati mund të jetë vetëm pak më i mirë se referenca. "
        "Zgjeroni intervalin ose ulni pragun e cilësisë.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Zmadhimi u ul nga ×{asked} në ×{used}: zona është shumë e madhe.",
    "resampling on the fine grid: {percent:.0f} %": "rikampionim në rrjetën e imët: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "zhvendosje dhe mbledhje: {done} / {total} kuadro",
    "{count} frames fused on a ×{scale} grid": "{count} kuadro të shkrira në një rrjetë ×{scale}",
    "noise reduction ({level})": "reduktim i zhurmës ({level})",
    "deconvolution: iteration {n} / {total}": "dekonvolucion: iteracioni {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} iteracione",
    "no deconvolution": "pa dekonvolucion",
    "{width} × {height} pixels": "{width} × {height} piksel",

    # motivi di esclusione di un fotogramma
    "subject not found": "subjekti nuk u gjet",
    "not sampled (memory limit)": "i pakampionuar (kufi i memories)",
    "frame not decoded": "kuadër i padekoduar",
    "alignment failed": "rreshtimi dështoi",
    "sub-pixel registration failed": "regjistrimi nënpiksel dështoi",
    "low alignment quality": "cilësi e ulët rreshtimi",
    "less sharp than the selected ones": "më pak i mprehtë se të zgjedhurat",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Burimi",
    "Open video…": "Hap video…",
    "Duration": "Kohëzgjatja",
    "Frames": "Kuadro",
    "Resolution": "Rezolucioni",
    "Codec": "Kodeku",
    "  (rotated {degrees}°)": "  (e rrotulluar {degrees}°)",
    "Open video": "Hap video",
    "Videos": "Video",
    "All files": "Të gjithë skedarët",
    "Reading {name}…": "Po lexohet {name}…",
    "Cannot open the video": "Videoja nuk mund të hapet",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} kuadro, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "U hap {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Output": "Dalja",
    "Destination folder": "Dosja e destinacionit",
    "Subfolder named after the video": "Nëndosje me emrin e videos",
    "Browse…": "Shfleto…",
    "Format": "Formati",
    "Color depth": "Thellësia e ngjyrës",
    "Also save every aligned frame (aligned/ folder)": "Ruaj edhe çdo kuadër të rreshtuar (dosja aligned/)",
    "next to the video": "pranë videos",
    ", in a subfolder named after it": ", në një nëndosje me emrin e saj",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Çdo shkrirje e ruajtur merr dosjen e vet ({where}) me result.{ext}, shkrirjen para restaurimit, "
        "kuadrin e referencës për krahasim, report.txt, report.pdf dhe report.json (parametrat, hapat, "
        "kuadrot e përdorura, SHA-256). Imazhe me {bits} bit për kanal.",
    "Language": "Gjuha",
    "Interface language. The change is immediate and is saved for the next start.":
        "Gjuha e ndërfaqes. Ndryshimi është i menjëhershëm dhe ruhet për nisjen e ardhshme.",
    "Credits": "Kredite",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Program i lirë nën GNU GPL v3 me atribuim të autorit: shihni skedarët LICENSE dhe NOTICE. Dekodimi "
        "i videos bëhet nga FFmpeg, program i veçantë me licencën e vet; përpunimi i imazheve me OpenCV "
        "dhe NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (pa humbje)",
    "Saving frame {frame}…": "Po ruhet kuadri {frame}…",
    "Saved {path}": "U ruajt {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Kuadri f{frame} u ruajt në {path} ({pix_fmt})",
    "Save failed": "Ruajtja dështoi",
    "The folder does not exist yet.": "Dosja nuk ekziston ende.",
    "Cannot open the folder": "Dosja nuk mund të hapet",
    "Open a video first.": "Hapni fillimisht një video.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "{name} nuk mund të kodohet.",
    "Writing the images…": "Po shkruhen imazhet…",
    "Writing the PDF report…": "Po shkruhet raporti PDF…",
    "page {page} of {pages}": "faqja {page} nga {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Referenca f{frame}  ·  bikubike ×{scale}",
    "Result  ·  {count} frames": "Rezultati  ·  {count} kuadro",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Fantazma  ·  {count} kuadro, secili në pozicionin ku u gjet",
    "Fusion before restoration": "Shkrirja para restaurimit",
    "Writing the aligned frames: {done} / {total}": "Po shkruhen kuadrot e rreshtuara: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Po llogariten gjurmët SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — raport i shkrirjes me shumë kuadro",
    "Created: {when}": "Krijuar: {when}",
    "File": "Skedari",
    "Size": "Madhësia",
    "{size} bytes": "{size} bajt",
    "Video": "Video",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Range and subject": "Intervali dhe subjekti",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} kuadro, {start} → {end})",
    "Subject area on the reference frame": "Zona e subjektit mbi kuadrin e referencës",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} piksel",
    "Parameters": "Parametrat",
    "yes": "po",
    "no": "jo",
    "Deconvolution": "Dekonvolucioni",
    "{iterations} Richardson-Lucy iterations": "{iterations} iteracione Richardson-Lucy",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px të daljes ({mode})",
    "automatic: measured on the edges of the fused image": "automatike: e matur në skajet e imazhit të shkrirë",
    "manual": "manuale",
    "Steps": "Hapat",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} kuadro të dekoduara nga FFmpeg, të sakta deri në kuadër; {scale}.",
    "subject search at full resolution": "kërkimi i subjektit me rezolucion të plotë",
    "subject search at {percent:.0f} % of the resolution": "kërkimi i subjektit në {percent:.0f} % të rezolucionit",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Subjekti u ndoq nga kuadri i referencës përpara dhe prapa me korrelacion të kryqëzuar të normalizuar "
        "(OpenCV matchTemplate, TM_CCOEFF_NORMED); u gjet në {found} / {count} kuadro, të prera me rezolucion "
        "të plotë rreth tij.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Rreshtim i përafërt i çdo kuadri me referencën me algoritmin ECC (Evangelidis & Psarakis, 2008), "
        "modeli: {model}, mbi imazhe të zbutura.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC i rafinuar me rezolucion të plotë (saktësi nënpiksel): {registered} kuadro të regjistruara. "
        "Përzgjedhja: ECC ≥ {quality:.2f}, {keep} % më të mprehtat (energjia e laplasianit): {used} kuadro të përdorura.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: kuadrot u rikampionuan në një rrjetë ×{scale} të referencës (Lanczos), të peshuara sipas "
        "cilësisë së rreshtimit{sharp}{equal}.",
    " and sharpness": " dhe mprehtësisë",
    ", brightness equalized to the reference": ", ndriçimi i barazuar me referencën",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Vetëm mbi luminancën (ngjyra zbutet: në videon e ngjeshur ajo mbart zhurmë, jo detaje). "
        "Reduktimi i zhurmës: {denoise}. Dekonvolucioni: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Fillimisht nivelet automatike: luminanca {black:.3f} → 0, {white:.3f} → 1, e njëjta vijë në çdo kanal",
    "No auto levels": "Pa nivele automatike",
    " (bilateral filter)": " (filtër bilateral)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, PSF gausiane σ {sigma:.2f} px, {iterations} iteracione, rregullarizim me variacion "
        "total {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Paraqitja: kontrast lokal {clahe}; {gray}. Kuadër i vetëm prej {width} × {height} piksel.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, kufi i prerjes {clip:g})",
    "grayscale": "shkallë gri",
    "color": "me ngjyra",
    "Result": "Rezultati",
    "Frames used": "Kuadro të përdorura",
    "{used} of {count}": "{used} nga {count}",
    "Estimated noise σ": "Zhurma σ e vlerësuar",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Metoda Immerkær, 0-255, me rezolucionin e videos: referenca {ref:.2f} → e shkrira {fused:.2f} → "
        "përfundimtare {final:.2f}. Dekonvolucioni ngre bashkë detajet e imëta dhe zhurmën, kështu që vlera "
        "e fundit nuk është vetëm një matje e zhurmës.",
    "Samples per output pixel": "Mostra për piksel të daljes",
    "Sub-pixel phases covered (4 × 4 grid)": "Faza nënpiksel të mbuluara (rrjetë 4 × 4)",
    "frame": "kuadër",
    "time": "koha",
    "search": "kërkim",
    "sharp.": "mpreht.",
    "weight": "pesha",
    "used": "përdorur",
    "model": "modeli",
    "note": "shënim",
    "(reference)": "(referenca)",
    "Files": "Skedarët",
    "aligned/: {count} aligned frames": "aligned/: {count} kuadro të rreshtuara",
    "Note": "Shënim",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Rezultati është një përmirësim i kuadrove të renditura më sipër: ai kombinon informacionin që gjendet "
        "në to dhe nuk shton detaje. Detajet e imëta në kufirin e rezolucionit, dhe shkronjat që ngjajnë me "
        "njëra-tjetrën, duhet të verifikohen mbi kuadrot burimore para se të nxirren përfundime.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Softueri: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Gati.",
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  faqja   ·   ← →  kuadri   ·   I / O  intervali   ·   F5  shkrij   ·   Ctrl+S  ruaj",
    "ffmpeg missing": "ffmpeg mungon",
    "Operation failed": "Veprimi dështoi",
    "ERROR - {title}: {message}": "GABIM - {title}: {message}",
    "Error: {title}": "Gabim: {title}",
    "INTERNAL ERROR": "GABIM I BRENDSHËM",
    "Internal error: details in the log.": "Gabim i brendshëm: detajet në regjistër.",
}
