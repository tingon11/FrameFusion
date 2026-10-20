# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Deutsch: Übersetzung der Texte der Oberfläche und des Berichts.

Der Schlüssel ist der englische Text, so wie er im Code steht (in tr() und N_()),
der Wert seine Übersetzung. Platzhalter in geschweiften Klammern bleiben unverändert.
Nicht übersetzte Schlüssel bleiben englisch. Nach jeder Änderung:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py de
"""

from __future__ import annotations

NAME = "Deutsch"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Die Oberfläche kann nicht gestartet werden: {error}\n\n"
        "Installieren Sie die Abhängigkeiten mit:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg nicht gefunden. Laden Sie es im FFmpeg-Feld der Seite Konfiguration herunter, "
        "oder installieren Sie es und nehmen Sie es in den PATH auf.",
    "Cannot check the latest ffmpeg version: {error}": "Die neueste ffmpeg-Version kann nicht geprüft werden: {error}",
    "Unexpected answer from the ffmpeg download site.": "Unerwartete Antwort der ffmpeg-Downloadseite.",
    "Downloading {label}": "{label} wird heruntergeladen",
    "Download of {label} failed: {error}": "Download von {label} fehlgeschlagen: {error}",
    "Invalid archive: suspicious path '{member}'.": "Ungültiges Archiv: verdächtiger Pfad '{member}'.",
    "The downloaded file is not a valid zip archive.": "Die heruntergeladene Datei ist kein gültiges Zip-Archiv.",
    "The downloaded package does not contain {name}.": "Das heruntergeladene Paket enthält {name} nicht.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "'{name}' kann nicht aktualisiert werden: Dateien in Benutzung. Warten Sie das Ende der laufenden "
        "Fusion ab und versuchen Sie es erneut.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Der automatische Download ist nur unter Windows verfügbar: Installieren Sie ffmpeg mit der "
        "Paketverwaltung des Systems.",
    "Extracting ffmpeg": "ffmpeg wird entpackt",
    "The downloaded ffmpeg does not run on this PC.": "Das heruntergeladene ffmpeg läuft auf diesem PC nicht.",
    "{name} is missing after extraction.": "{name} fehlt nach dem Entpacken.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Prüfung…",
    "Check": "Prüfen",
    "Check for updates": "Nach Updates suchen",
    "Download / Update": "Herunterladen / Aktualisieren",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg ist ein separates Programm (LGPL/GPL). Der Download holt den offiziellen Windows-Build "
        "von {url} und behält nur ffmpeg.exe, LICENSE und README im Ordner tools\\ffmpeg neben dem "
        "Programm: keine Installation, keine Änderung am PATH.",
    "ffmpeg check failed": "ffmpeg-Prüfung fehlgeschlagen",
    "tools folder": "Ordner tools",
    "system PATH": "System-PATH",
    "Python package": "Python-Paket",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Engine: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Fehlt: Laden Sie es mit der Schaltfläche rechts herunter.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg nicht gefunden: Laden Sie es im FFmpeg-Feld der Seite Konfiguration herunter.",
    "ffmpeg missing: download it from the FFmpeg box.": "ffmpeg fehlt: Laden Sie es im FFmpeg-Feld herunter.",
    "Checking the latest ffmpeg version…": "Neueste ffmpeg-Version wird geprüft…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} ist aktuell.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Neueste Version: {latest}. Installiert: {installed}. Jetzt herunterladen?",
    "Update check failed": "Update-Prüfung fehlgeschlagen",
    "Wait for the running fusion, then try again.": "Warten Sie das Ende der laufenden Fusion ab, dann versuchen Sie es erneut.",
    "Downloading ffmpeg…": "ffmpeg wird heruntergeladen…",
    "Downloading ffmpeg from {url}": "ffmpeg wird von {url} heruntergeladen",
    "ffmpeg downloaded into {path}": "ffmpeg heruntergeladen nach {path}",
    "Download cancelled.": "Download abgebrochen.",
    "ffmpeg download failed": "ffmpeg-Download fehlgeschlagen",
    "ffmpeg: exit code {code}": "ffmpeg: Exit-Code {code}",
    "File not found: {path}": "Datei nicht gefunden: {path}",
    "The file has no recognizable video track.": "Die Datei enthält keine erkennbare Videospur.",
    "Video size not recognized.": "Videogröße nicht erkannt.",
    "Frame rate not recognized.": "Bildrate nicht erkannt.",
    "Invalid frame rate.": "Ungültige Bildrate.",
    "Unknown video duration (stream or damaged file).":
        "Unbekannte Videodauer (Stream oder beschädigte Datei).",
    "Zero video duration.": "Videodauer null.",
    "No frame at {seconds:.3f} s.": "Kein Frame bei {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg hat die Datei nicht geschrieben.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "BESTÄTIGEN",
    "WARNING": "WARNUNG",
    "ERROR": "FEHLER",
    "Yes": "Ja",

    # ----------------------------------------------------------- navigazione
    "PAGES": "SEITEN",
    "Configuration": "Konfiguration",
    "Subject": "Motiv",
    "Frames, subject and reference": "Frames, Motiv und Referenz",
    "Fusion": "Fusion",
    "Multi-frame fusion and result": "Multi-Frame-Fusion und Ergebnis",
    "{app}  /  PAGE {index:02d}": "{app}  /  SEITE {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "keines",
    "Open video… (Ctrl+O)": "Video öffnen… (Strg+O)",
    "No video": "Kein Video",
    "Reading…": "Wird gelesen…",
    "Ready": "Bereit",
    "Error": "Fehler",
    "Fusing…": "Fusion läuft…",
    "Fused": "Fusioniert",

    # ------------------------------------------------------------- anteprima
    "Preview": "Vorschau",
    "Open a video to see the preview": "Öffnen Sie ein Video, um die Vorschau zu sehen",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "Ziehen mit rechter Maustaste: Motivausschnitt  ·  Mausrad: Zoom  ·  Ziehen: Verschieben  ·  Doppelklick: Einpassen",
    "First frame (Home)": "Erster Frame (Pos1)",
    "Back 10 frames (Shift+←)": "10 Frames zurück (Umschalt+←)",
    "Previous frame (←)": "Vorheriger Frame (←)",
    "Next frame (→)": "Nächster Frame (→)",
    "Forward 10 frames (Shift+→)": "10 Frames vor (Umschalt+→)",
    "Last frame (End)": "Letzter Frame (Ende)",
    "Save frame": "Frame speichern",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Speichert den angezeigten Frame in voller Auflösung, verlustfrei (Strg+S)",
    "Preview unavailable: {error}": "Vorschau nicht verfügbar: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Strg+Mausrad: Zoom  ·  Mausrad: Blättern  ·  I / O und Cursor ziehen  ·  Doppelklick auf das Lineal: Alles",
    "In  [I]": "In  [I]",
    "Out  [O]": "Out  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Setzt den Anfang der Auswahl auf den Cursor (Taste I)",
    "Sets the end of the selection at the cursor (key O)":
        "Setzt das Ende der Auswahl auf den Cursor (Taste O)",
    "Moves the cursor to the start of the selection": "Setzt den Cursor an den Anfang der Auswahl",
    "Moves the cursor to the end of the selection": "Setzt den Cursor an das Ende der Auswahl",
    "CURSOR": "CURSOR",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Zeit (1:23.456, 83.4) oder Frame (f2000), dann Eingabetaste",
    "Zoom out (−)": "Verkleinern (−)",
    "Zoom in (+)": "Vergrößern (+)",
    "All": "Alles",
    "Selection": "Auswahl",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Auswahl: f{first} → f{last}  ·  {count} Frames  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Ansicht: {start} → {end}  ({seconds:.3f} s, {frames:.1f} Frames)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Zeit nicht erkannt: Verwenden Sie mm:ss.mmm, Sekunden oder f<Zahl>.",
    "Open a video to see the timeline": "Öffnen Sie ein Video, um die Zeitleiste zu sehen",

    # -------------------------------------------------------------- soggetto
    "Select area": "Ausschnitt wählen",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Ziehen Sie dann in der Vorschau einen Rahmen um das Motiv (oder jederzeit mit der rechten Maustaste); "
        "die Fusion startet von selbst",
    "Moves the cursor to the reference frame": "Setzt den Cursor auf das Referenzbild",
    "Clear": "Aufheben",
    "Fuse frames  →": "Frames fusionieren  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Startet die Multi-Frame-Fusion auf dem gewählten Bereich (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Rahmen Sie das Motiv auf einem scharfen Frame ein: Dieser Frame wird zur Referenz, und die Fusion startet.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Ziehen Sie in der Vorschau einen Rahmen um das Motiv (Esc zum Abbrechen).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "Der Motivausschnitt ist zu klein: Zeichnen Sie mindestens {size} × {size} Pixel.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Bereich um die Referenz gesetzt: f{first} → f{last}. Verschieben Sie I / O, um ihn zu ändern.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Motivausschnitt {width} × {height} bei ({x}, {y}) auf dem Referenzbild f{frame}",
    "Subject area cleared.": "Motivausschnitt aufgehoben.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Die Referenz f{frame} liegt außerhalb des Bereichs f{first} → f{last}: Verschieben Sie I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} Frames im Bereich: Wählen Sie höchstens {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Ausschnitt {width} × {height} px bei ({x}, {y})  ·  Referenz f{frame}  ·  {count} Frames f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Wählen Sie zuerst den Ausschnitt des Motivs (Kennzeichen, Gesicht, Objekt) auf einem scharfen Frame: "
        "Ziehen Sie mit der rechten Maustaste in der Vorschau, oder verwenden Sie „Ausschnitt wählen“.",
    "The reference frame must be inside the selected range.":
        "Das Referenzbild muss innerhalb des gewählten Bereichs liegen.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "Der Bereich hat {count} Frames: Wählen Sie höchstens {limit} um die Referenz.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Frames und Ausrichtung",
    "Motion model": "Bewegungsmodell",
    "Translation": "Translation",
    "Rotation + translation": "Rotation + Translation",
    "Affine": "Affin",
    "Perspective (homography)": "Perspektivisch (Homographie)",
    "Subject search: minimum correlation": "Motivsuche: minimale Korrelation",
    "Minimum alignment quality (ECC)": "Minimale Ausrichtungsqualität (ECC)",
    "Sharpest frames kept": "Schärfste Frames behalten",
    "Scale": "Vergrößerung",
    "Fusion method": "Fusionsmethode",
    "Robust mean (outliers rejected)": "Robuster Mittelwert (Ausreißer verworfen)",
    "Shift-and-add (normalized convolution)": "Shift-and-Add (normalisierte Faltung)",
    "Median": "Median",
    "Weight by sharpness": "Nach Schärfe gewichten",
    "Equalize brightness": "Helligkeit angleichen",
    "Restoration": "Restaurierung",
    "Noise reduction": "Rauschunterdrückung",
    "Off": "Aus",
    "Light": "Leicht",
    "Medium": "Mittel",
    "Strong": "Stark",
    "Deconvolution iterations": "Iterationen der Dekonvolution",
    "0 (none)": "0 (keine)",
    "not applied": "nicht angewendet",
    "PSF σ (output pixels)": "PSF σ (Ausgabepixel)",
    "Automatic": "Automatisch",
    "Regularization (total variation)": "Regularisierung (Totalvariation)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Mehr Iterationen schärfen stärker, verstärken aber auch Rauschen und Halos; die Regularisierung hält "
        "das Rauschen zurück. Ändern Sie jeweils nur wenig und vergleichen Sie.",
    "Presentation": "Darstellung",
    "Auto levels": "Automatische Tonwerte",
    "Local contrast (CLAHE)": "Lokaler Kontrast (CLAHE)",
    "Grayscale": "Graustufen",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Die Tonwerte sind eine Gerade, die vor der Dekonvolution angewendet wird (Schwarz und Weiß am 0,5- und "
        "99,5-Perzentil); der lokale Kontrast ein zonenweiser Ausgleich. Alles steht im Bericht.",
    "Defaults": "Standardwerte",
    "Puts every parameter of the pipeline back to its default value":
        "Setzt jeden Parameter der Pipeline auf seinen Standardwert zurück",
    "Parameters back to their defaults.": "Parameter auf die Standardwerte zurückgesetzt.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Gespeicherte Einstellungen",
    "(none saved)": "(keine gespeichert)",
    "Save…": "Speichern…",
    "Saves the current parameters under a name (in config.json)":
        "Speichert die aktuellen Parameter unter einem Namen (in config.json)",
    "Delete": "Löschen",
    "From report…": "Aus Bericht…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Lädt die Parameter aus der report.json einer gespeicherten Fusion",
    "Save settings": "Einstellungen speichern",
    "Name of these settings:": "Name dieser Einstellungen:",
    "Settings «{name}» already exist. Replace them?": "Die Einstellungen „{name}“ existieren bereits. Ersetzen?",
    "Settings «{name}» saved.": "Einstellungen „{name}“ gespeichert.",
    "Settings «{name}» loaded.": "Einstellungen „{name}“ geladen.",
    "Delete settings": "Einstellungen löschen",
    "Delete the settings «{name}»?": "Die Einstellungen „{name}“ löschen?",
    "Settings «{name}» deleted.": "Einstellungen „{name}“ gelöscht.",
    "Load parameters from a report": "Parameter aus einem Bericht laden",
    "Cannot read the report": "Der Bericht kann nicht gelesen werden",
    "{name} is not a FrameFusion report.": "{name} ist kein FrameFusion-Bericht.",
    "Parameters loaded from {path}": "Parameter geladen aus {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Vergleich",
    "FRAMES": "FRAMES",
    "RESULT": "ERGEBNIS",
    "Ghost of the frames": "Geisterbild der Frames",
    "Reference frame": "Referenzbild",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "GEISTERBILD  ·  {count} FRAMES  ·  ×{scale}",
    "Final": "Endergebnis",
    "Fusion only": "Nur Fusion",
    "Draw the subject area on the Subject page, then run the fusion":
        "Zeichnen Sie den Motivausschnitt auf der Seite Motiv, dann starten Sie die Fusion",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "Mausrad: Zoom  ·  Ziehen: Verschieben  ·  Doppelklick: Einpassen  ·  die beiden Ansichten bewegen sich "
        "gemeinsam  ·  Geisterbild: jeder verwendete Frame, überlagert an der Position, an der er gefunden wurde",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "REFERENZ f{frame}  ·  BIKUBISCH ×{scale}",
    "RESULT  ·  {count} FRAMES": "ERGEBNIS  ·  {count} FRAMES",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Frame-Extraktion",
    "Subject detection": "Motiverkennung",
    "Local alignment": "Lokale Ausrichtung",
    "Sub-pixel registration": "Subpixel-Registrierung",
    "Multi-frame fusion": "Multi-Frame-Fusion",
    "Deconvolution and denoising": "Dekonvolution und Rauschunterdrückung",
    "Single frame": "Einzelbild",
    "Save result": "Ergebnis speichern",
    "Saves images and report in a new folder (Ctrl+S)": "Speichert Bilder und Bericht in einem neuen Ordner (Strg+S)",
    "Run fusion": "Fusion starten",
    "Runs the pipeline again with these parameters (F5)": "Führt die Pipeline mit diesen Parametern erneut aus (F5)",
    "Open folder": "Ordner öffnen",
    "Cancel": "Abbrechen",
    "reused": "wiederverwendet",
    "Fusion in progress…": "Fusion läuft…",
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Fusion: f{first} → f{last}, Referenz f{ref}, Ausschnitt {width} × {height} bei ({x}, {y}), ×{scale}, {method}",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} von {count} Frames  ·  ×{scale}  ·  Rauschen σ {ref:.1f} → {fused:.1f} nach der Fusion  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fusion abgeschlossen: {summary}",
    "Excluded: {list}": "Ausgeschlossen: {list}",
    "Fusion cancelled.": "Fusion abgebrochen.",
    "Fusion cancelled by the user": "Fusion vom Benutzer abgebrochen",
    "Fusion failed: see the log.": "Fusion fehlgeschlagen: siehe Protokoll.",
    "Fusion failed": "Fusion fehlgeschlagen",
    "Fusion in progress": "Fusion läuft",
    "The fusion is still running. Stop it and close?": "Die Fusion läuft noch. Abbrechen und schließen?",
    "Saving the result…": "Ergebnis wird gespeichert…",
    "Saved in «{folder}».": "Gespeichert in „{folder}“.",
    "Saved in {folder}": "Gespeichert in {folder}",
    "Result, comparison images and report saved in {folder}":
        "Ergebnis, Vergleichsbilder und Bericht gespeichert in {folder}",

    # messaggi dei passaggi (fusion.py)
    "{done} / {total} frames decoded": "{done} / {total} Frames dekodiert",
    "{count} frames decoded": "{count} Frames dekodiert",
    "The video ended before the reference frame.": "Das Video endete vor dem Referenzbild.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Motivsuche auf Frames, die auf {percent:.0f} % verkleinert wurden (Speicherlimit).",
    "searching the subject: {done} / {total}": "Motivsuche: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Nur jeder {stride}. Frame behalten (Speicherlimit für große Ausschnitte).",
    "{done} / {total} frames read at full resolution": "{done} / {total} Frames in voller Auflösung gelesen",
    "The reference frame could not be read.": "Das Referenzbild konnte nicht gelesen werden.",
    "subject found in {found} / {total} frames": "Motiv in {found} / {total} Frames gefunden",
    "{done} / {total} frames aligned": "{done} / {total} Frames ausgerichtet",
    "motion model: {model}": "Bewegungsmodell: {model}",
    "{done} / {total} frames registered": "{done} / {total} Frames registriert",
    "{count} frames registered": "{count} Frames registriert",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} Frames mit einem einfacheren Bewegungsmodell ausgerichtet, weil das gewählte bei ihnen nicht "
        "konvergierte.",
    "{count} frames selected": "{count} Frames ausgewählt",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Nur {count} verwendbare Frames: Das Ergebnis kann nur wenig besser sein als die Referenz. Erweitern Sie "
        "den Bereich oder senken Sie die Qualitätsschwelle.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Vergrößerung von ×{asked} auf ×{used} reduziert: Der Ausschnitt ist zu groß.",
    "resampling on the fine grid: {percent:.0f} %": "Neuabtastung auf dem feinen Raster: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "Shift-and-Add: {done} / {total} Frames",
    "{count} frames fused on a ×{scale} grid": "{count} Frames auf einem ×{scale}-Raster fusioniert",
    "noise reduction ({level})": "Rauschunterdrückung ({level})",
    "deconvolution: iteration {n} / {total}": "Dekonvolution: Iteration {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} Iterationen",
    "no deconvolution": "keine Dekonvolution",
    "{width} × {height} pixels": "{width} × {height} Pixel",

    # motivi di esclusione di un fotogramma
    "subject not found": "Motiv nicht gefunden",
    "not sampled (memory limit)": "nicht abgetastet (Speicherlimit)",
    "frame not decoded": "Frame nicht dekodiert",
    "alignment failed": "Ausrichtung fehlgeschlagen",
    "sub-pixel registration failed": "Subpixel-Registrierung fehlgeschlagen",
    "low alignment quality": "geringe Ausrichtungsqualität",
    "less sharp than the selected ones": "weniger scharf als die ausgewählten",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Quelle",
    "Open video…": "Video öffnen…",
    "Duration": "Dauer",
    "Frames": "Frames",
    "Resolution": "Auflösung",
    "Codec": "Codec",
    "  (rotated {degrees}°)": "  (um {degrees}° gedreht)",
    "Open video": "Video öffnen",
    "Videos": "Videos",
    "All files": "Alle Dateien",
    "Reading {name}…": "{name} wird gelesen…",
    "Cannot open the video": "Das Video kann nicht geöffnet werden",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} Frames, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Geöffnet: {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} Bit), {duration}",
    "Output": "Ausgabe",
    "Destination folder": "Zielordner",
    "Subfolder named after the video": "Unterordner mit dem Namen des Videos",
    "Browse…": "Durchsuchen…",
    "Format": "Format",
    "Color depth": "Farbtiefe",
    "Also save every aligned frame (aligned/ folder)": "Auch jeden ausgerichteten Frame speichern (Ordner aligned/)",
    "next to the video": "neben dem Video",
    ", in a subfolder named after it": ", in einem Unterordner mit seinem Namen",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Jede gespeicherte Fusion erhält einen eigenen Ordner ({where}) mit result.{ext}, der Fusion vor der "
        "Restaurierung, dem Referenzbild zum Vergleich, report.txt, report.pdf und report.json (Parameter, "
        "Schritte, verwendete Frames, SHA-256). Bilder mit {bits} Bit pro Kanal.",
    "Language": "Sprache",
    "Interface language. The change is immediate and is saved for the next start.":
        "Sprache der Oberfläche. Die Änderung wirkt sofort und wird für den nächsten Start gespeichert.",
    "Credits": "Credits",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Freie Software unter der GNU GPL v3 mit Nennung des Autors: siehe die Dateien LICENSE und NOTICE. "
        "Videodekodierung durch FFmpeg, ein separates Programm unter eigener Lizenz; Bildverarbeitung mit "
        "OpenCV und NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (verlustfrei)",
    "Saving frame {frame}…": "Frame {frame} wird gespeichert…",
    "Saved {path}": "Gespeichert: {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Frame f{frame} gespeichert in {path} ({pix_fmt})",
    "Save failed": "Speichern fehlgeschlagen",
    "The folder does not exist yet.": "Der Ordner existiert noch nicht.",
    "Cannot open the folder": "Der Ordner kann nicht geöffnet werden",
    "Open a video first.": "Öffnen Sie zuerst ein Video.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "{name} kann nicht kodiert werden.",
    "Writing the images…": "Bilder werden geschrieben…",
    "Writing the PDF report…": "PDF-Bericht wird geschrieben…",
    "page {page} of {pages}": "Seite {page} von {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Referenz f{frame}  ·  bikubisch ×{scale}",
    "Result  ·  {count} frames": "Ergebnis  ·  {count} Frames",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Geisterbild  ·  {count} Frames, jeder an der Position, an der er gefunden wurde",
    "Fusion before restoration": "Fusion vor der Restaurierung",
    "Writing the aligned frames: {done} / {total}": "Ausgerichtete Frames werden geschrieben: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "SHA-256-Prüfsummen werden berechnet…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — Bericht zur Multi-Frame-Fusion",
    "Created: {when}": "Erstellt: {when}",
    "File": "Datei",
    "Size": "Größe",
    "{size} bytes": "{size} Byte",
    "Video": "Video",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} Bit), {duration}",
    "Range and subject": "Bereich und Motiv",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} Frames, {start} → {end})",
    "Subject area on the reference frame": "Motivausschnitt auf dem Referenzbild",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} Pixel",
    "Parameters": "Parameter",
    "yes": "ja",
    "no": "nein",
    "Deconvolution": "Dekonvolution",
    "{iterations} Richardson-Lucy iterations": "{iterations} Richardson-Lucy-Iterationen",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px der Ausgabe ({mode})",
    "automatic: measured on the edges of the fused image": "automatisch: an den Kanten des fusionierten Bildes gemessen",
    "manual": "manuell",
    "Steps": "Schritte",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} Frames von FFmpeg dekodiert, framegenau; {scale}.",
    "subject search at full resolution": "Motivsuche in voller Auflösung",
    "subject search at {percent:.0f} % of the resolution": "Motivsuche bei {percent:.0f} % der Auflösung",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Motiv vom Referenzbild aus vorwärts und rückwärts per normierter Kreuzkorrelation verfolgt "
        "(OpenCV matchTemplate, TM_CCOEFF_NORMED); in {found} / {count} Frames gefunden, in voller Auflösung "
        "um das Motiv herum zugeschnitten.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Grobe Ausrichtung jedes Frames an der Referenz mit dem ECC-Algorithmus (Evangelidis & Psarakis, "
        "2008), Modell: {model}, auf geglätteten Bildern.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC in voller Auflösung verfeinert (Subpixel-Genauigkeit): {registered} Frames registriert. Auswahl: "
        "ECC ≥ {quality:.2f}, die schärfsten {keep} % (Laplace-Energie): {used} Frames verwendet.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: Frames auf ein ×{scale}-Raster der Referenz neu abgetastet (Lanczos), gewichtet nach "
        "Ausrichtungsqualität{sharp}{equal}.",
    " and sharpness": " und Schärfe",
    ", brightness equalized to the reference": ", Helligkeit an die Referenz angeglichen",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Nur auf der Luminanz (die Farbe wird geglättet: in komprimiertem Video trägt sie Rauschen, "
        "kein Detail). Rauschunterdrückung: {denoise}. Dekonvolution: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Zuerst automatische Tonwerte: Luminanz {black:.3f} → 0, {white:.3f} → 1, gleiche Gerade auf jedem Kanal",
    "No auto levels": "Keine automatischen Tonwerte",
    " (bilateral filter)": " (bilateraler Filter)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, Gauß-PSF σ {sigma:.2f} px, {iterations} Iterationen, Totalvariations-Regularisierung "
        "{reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Darstellung: lokaler Kontrast {clahe}; {gray}. Einzelbild mit {width} × {height} Pixeln.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, Clip-Limit {clip:g})",
    "grayscale": "Graustufen",
    "color": "farbig",
    "Result": "Ergebnis",
    "Frames used": "Verwendete Frames",
    "{used} of {count}": "{used} von {count}",
    "Estimated noise σ": "Geschätztes Rauschen σ",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Methode nach Immerkær, 0-255, bei Videoauflösung: Referenz {ref:.2f} → fusioniert {fused:.2f} → final "
        "{final:.2f}. Die Dekonvolution hebt feines Detail und Rauschen gemeinsam an, der letzte Wert ist also "
        "kein reines Rauschmaß.",
    "Samples per output pixel": "Abtastwerte pro Ausgabepixel",
    "Sub-pixel phases covered (4 × 4 grid)": "Abgedeckte Subpixel-Phasen (4 × 4-Raster)",
    "frame": "Frame",
    "time": "Zeit",
    "search": "Suche",
    "sharp.": "Schärfe",
    "weight": "Gewicht",
    "used": "verw.",
    "model": "Modell",
    "note": "Hinweis",
    "(reference)": "(Referenz)",
    "Files": "Dateien",
    "aligned/: {count} aligned frames": "aligned/: {count} ausgerichtete Frames",
    "Note": "Hinweis",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Das Ergebnis ist eine Verbesserung der oben aufgeführten Frames: Es kombiniert in ihnen vorhandene "
        "Information und fügt keine Details hinzu. Feine Details an der Auflösungsgrenze und ähnlich aussehende "
        "Zeichen müssen vor jeder Schlussfolgerung an den Quell-Frames überprüft werden.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Bereit.",
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Strg+1/2/3  Seite   ·   ← →  Frame   ·   I / O  Bereich   ·   F5  fusionieren   ·   Strg+S  speichern",
    "ffmpeg missing": "ffmpeg fehlt",
    "Operation failed": "Vorgang fehlgeschlagen",
    "ERROR - {title}: {message}": "FEHLER - {title}: {message}",
    "Error: {title}": "Fehler: {title}",
    "INTERNAL ERROR": "INTERNER FEHLER",
    "Internal error: details in the log.": "Interner Fehler: Details im Protokoll.",
}
