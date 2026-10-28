# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Größere Vorschau: blendet die Zeitleiste aus, die Tasten I / O funktionieren weiter (F11)",
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
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Bereich auf die Frames verkleinert, in denen das Motiv verfolgt wurde: f{first} → f{last}.",
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
    "{name} is not an IdentiFrame report.": "{name} ist kein IdentiFrame-Bericht.",
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
    "{count} frames decoded": "{count} Frames dekodiert",
    "The video ended before the reference frame.": "Das Video endete vor dem Referenzbild.",
    "Range set with I / O": "Mit I / O gesetzter Bereich",
    "Frames examined":
        "Untersuchte Frames",
    "Frames that make up the result":
        "Frames, aus denen das Ergebnis besteht",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "{count} Frames ausgeschlossen, weil sie nach mehr als {seconds:g} s ohne gute Ausrichtung kommen: ab dort ist das Motiv nicht mehr bestätigt (verdeckt, zu klein oder außerhalb des Bildes).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Motiv verfolgt von f{first} bis f{last}: darüber hinaus fehlt es oder ist länger als {seconds:g} s nicht bestätigt.",
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
    "ffmpeg missing": "ffmpeg fehlt",
    "Operation failed": "Vorgang fehlgeschlagen",
    "ERROR - {title}: {message}": "FEHLER - {title}: {message}",
    "Error: {title}": "Fehler: {title}",
    "INTERNAL ERROR": "INTERNER FEHLER",
    "Internal error: details in the log.": "Interner Fehler: Details im Protokoll.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Art des Motivs",
    "Parameters set for the subject type: {subject}.": "Parameter für die Art des Motivs gesetzt: {subject}.",
    "Face": "Gesicht",
    "pose or expression differs from the reference": "Pose oder Mimik weicht vom Referenzbild ab",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Gesicht: lokale, nicht starre Verfeinerung nach ECC auf {count} Einzelbildern, mittlere Verschiebung {residual:.2f} px des Videos.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Gesicht: der Bereich ist für die lokale Verfeinerung zu klein (mindestens {size} px): nur starre Ausrichtung.",
    "simil.": "Ähnl.",
    "Local refinement (face)": "Lokale Verfeinerung (Gesicht)",
    "not applied: area too small, rigid alignment only": "nicht angewendet: Bereich zu klein, nur starre Ausrichtung",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Gesicht: der Motivbereich ist im Video {width} × {height} Pixel groß. Die Fusion kombiniert Einzelbilder, deren Pose und Mimik zum Referenzbild passen, und gewichtet abweichende Teile geringer; sie kann keine Merkmale erzeugen, die kein Einzelbild zeigt. Bei einem Gesicht, das schmaler als etwa 60 Pixel ist, kann das Ergebnis das Gesamtbild verbessern, aber keine identifizierenden Merkmale sichtbar machen: vergleichen Sie es mit dem Referenzbild und den Einzelbildern, bevor Sie Schlüsse über die Identität ziehen.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Gesicht: nach dem starren Modell folgt eine lokale, nicht starre Verfeinerung (optischer Fluss nach Farneback zwischen Referenzbild und ausgerichtetem Einzelbild, geglättet und in der Amplitude begrenzt) Mimik und Kopfbewegung; eine Konfidenz je Pixel (Vorwärts-Rückwärts-Konsistenz und lokale Korrelation) gewichtet jede Probe in der Fusion. Einzelbilder, deren lokale Ähnlichkeit zum Referenzbild unter {limit:.2f} liegt, bleiben außen vor (Pose oder Mimik verändert).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} Einzelbilder verfeinert; mittlere lokale Ähnlichkeit zum Referenzbild {similarity:.2f}, mittlere lokale Verschiebung {displacement:.2f} px des Videos; {excluded} Einzelbilder wegen anderer Pose oder Mimik ausgeschlossen.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fusion: {subject}, f{first} → f{last}, Referenz f{ref}, Ausschnitt {width} × {height} bei ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Strg+1/2/3  Seite   ·   ← →  Frame   ·   Leertaste  abspielen   ·   I / O  Bereich   ·   F5  fusionieren   ·   Strg+S  speichern",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} Einzelbilder mit einem einfacheren Bewegungsmodell ausgerichtet, weil das gewählte eine unplausible Verformung ergab (Skalierung, Scherung oder Perspektive außerhalb der Grenzen).",
    "persp.": "Persp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Gesicht: Proben außerhalb der in den Bereich eingeschriebenen Ellipse zählen wenig, und dort zeigt das Ergebnis das Referenzbild: der Hintergrund bewegt sich anders als das Gesicht.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Kennzeichen und Text: eine starre Ausrichtung pro Einzelbild; die Zeichen werden mit fast-plate-ocr (Kennzeichen) oder PaddleOCR (Texte, auch mehrzeilig) gelesen. Gesicht: nach der Ausrichtung folgt eine lokale, nicht starre Verfeinerung der Mimik und der Kopfbewegung, Einzelbilder mit anderer Pose werden ausgelassen und die Restaurierung ist leichter. Ein Wechsel des Typs lädt dessen Standardwerte.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Liest das Kennzeichen (fast-plate-ocr) oder den Text (PaddleOCR) im Ergebnis und in unabhängigen Fusionen von Gruppen von Einzelbildern und stimmt Zeichen für Zeichen ab",
    "OCR models": "OCR-Modelle",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "Die Zeichen werden von zwei Modellen gelesen, die OpenCV ausführt; sie werden bei Bedarf nach tools\\ocr heruntergeladen und sind nie Teil des Programms (etwa 37 MB): fast-plate-ocr für Kennzeichen (MIT, von ankandrew) und PaddleOCR PP-OCRv6 für Texte in vielen Sprachen (Apache 2.0, Baidu / PaddleOCR, ONNX-Konvertierung von RapidOCR). Jede Datei wird mit ihrem SHA-256-Fingerabdruck geprüft; Lizenzen und Herkunft werden neben den Modellen gespeichert.",
    "Downloading the OCR models…": "OCR-Modelle werden heruntergeladen…",
    "Reading the characters…": "Zeichen werden gelesen…",
    "OCR models download failed": "Herunterladen der OCR-Modelle fehlgeschlagen",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "OCR-Modelle werden heruntergeladen: {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Das OCR-Modell für diesen Motivtyp fehlt: Laden Sie es im Feld OCR-Modelle der Seite Konfiguration herunter.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "Zeichen lesen drücken (automatisch für Kennzeichen und Texte, wenn die OCR-Modelle bereit sind)",
    "model confidence {confidence:.0f} %": "Modellkonfidenz {confidence:.0f} %",
    "OCR models check failed": "Prüfung der OCR-Modelle fehlgeschlagen",
    "OCR: {plate} (plates), {text} (texts)": "OCR: {plate} (Kennzeichen), {text} (Texte)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Fehlen (optional, zum Lesen von Kennzeichen und Texten): Laden Sie sie mit der Schaltfläche rechts herunter.",
    "OCR models ready: {path}": "OCR-Modelle bereit: {path}",
    "possible country ({share:.0f} %)": "mögliches Land ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "mögliches Land: {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  Kennzeichen: {plate}  ·  Texte: {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Das Modell für Texte fehlt: Laden Sie es mit der Schaltfläche rechts herunter.",
    "The model for plates is missing: download it with the button on the right.": "Das Modell für Kennzeichen fehlt: Laden Sie es mit der Schaltfläche rechts herunter.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Schrift, Standard: Perspektive, schärfste 75 %, ×2, robuster Mittelwert, mäßige Dekonvolution. Der Ausgangspunkt.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Schrift bei Nacht oder verrauscht: mehr Einzelbilder, mittlere Rauschunterdrückung, sanftere Dekonvolution mit starker Regularisierung, leichter lokaler Kontrast, Graustufen.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Entfernte, kleine Schrift in vielen Einzelbildern: ×3, Verschieben und Addieren, fast alle Einzelbilder, niedrigere Ausrichtungsschwelle.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Schrift auf einem fahrenden Fahrzeug oder von einer bewegten Kamera gefilmt, mit Bewegungsunschärfe: nur die schärfere Hälfte der Einzelbilder, tolerantere Motivsuche, stärkere Dekonvolution.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Schrift im Schatten oder Gegenlicht: mittlerer lokaler Kontrast, Graustufen, leichte Rauschunterdrückung.",
    "Plate": "Kennzeichen",
    "Text": "Text",
    "No text line found inside the area: the whole area was read as one line.": "Keine Textzeile im Bereich gefunden: der ganze Bereich wurde als eine Zeile gelesen.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "Keine Zeichen gefunden: Zeichnen Sie den Bereich eng um das Kennzeichen oder den Text und prüfen Sie Vergrößerung und Restaurierung.",
    "Cannot load the OCR model {name}: {error}": "Das OCR-Modell {name} kann nicht geladen werden: {error}",
    "The OCR model configuration {name} is not valid.": "Die Konfiguration des OCR-Modells {name} ist ungültig.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Automatische Lesung durch ein OCR-Modell, an den Bildern zu prüfen: Zeichen ähnlicher Form (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) können in jeder Lesung gleich falsch gelesen werden, und die Abstimmung bemerkt es nicht. Das mögliche Land des Kennzeichens ist eine Schätzung des Modells nach dem Aussehen des Kennzeichens, keine Prüfung.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), ausgeführt von {runtime}: gelesen werden das Ergebnis und {groups} Fusionen unabhängiger Gruppen von Einzelbildern, jede mit denselben Parametern restauriert; die Lesungen werden ausgerichtet und Zeichen für Zeichen abgestimmt, gewichtet mit der Wahrscheinlichkeit, die das Modell jedem Zeichen gibt (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), ausgeführt von {runtime}: die Textzeilen werden im Ergebnis gefunden, dann wird jede Zeile im Ergebnis und in {groups} Fusionen unabhängiger Gruppen von Einzelbildern gelesen, jede mit denselben Parametern restauriert; jede Zeile wird Zeichen für Zeichen abgestimmt, gewichtet mit der Wahrscheinlichkeit, die das Modell jedem Zeichen gibt (Quiala et al., 2023).",
    "the whole area": "der ganze Bereich",
    "Model confidence": "Modellkonfidenz",
    "Area read": "Gelesener Bereich",
    "Text lines": "Textzeilen",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} Pixel des Ergebnisses",
    "Possible country": "Mögliches Land",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, mittlere Wahrscheinlichkeit der im Ergebnis gelesenen Zeichen",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % der Stimmen), vom Modell nach dem Aussehen des Kennzeichens geschätzt",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV kann das heruntergeladene Modell {name} nicht laden.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name}: Die heruntergeladene Datei ist nicht die erwartete (ihr SHA-256-Fingerabdruck ist anders).",
    "Read characters": "Zeichen lesen",
    "CHARACTERS": "ZEICHEN",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Gelesene Zeichen: {text}  ·  Übereinstimmung {agreement:.0f} %  ·  {count} Lesungen",
    "Character reading": "Zeichenlesung",
    "reading…": "wird gelesen…",
    "no characters found: draw the area tight around the text": "keine Zeichen gefunden: Bereich eng um die Schrift ziehen",
    "agreement {agreement:.0f} %  ·  {count} readings": "Übereinstimmung {agreement:.0f} %  ·  {count} Lesungen",
    "Character reading failed: {error}": "Zeichenlesung fehlgeschlagen: {error}",
    "doubtful: {list}": "zweifelhaft: {list}",
    "check by eye: {list}": "mit dem Auge prüfen: {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Zu wenige Einzelbilder für unabhängige Gruppen: nur das Ergebnis wurde gelesen, ohne Abstimmung.",
    "Character reading (OCR)": "Zeichenlesung (OCR)",
    "illegible":
        "unleserlich",
    "no character recognizable with enough confidence":
        "kein Zeichen mit ausreichender Konfidenz erkennbar",
    "{count} illegible lines not shown":
        "{count} unleserliche Zeilen nicht angezeigt",
    "not recognizable (?): {list}":
        "nicht erkennbar (?): {list}",
    "illegible: no character recognizable with enough confidence":
        "unleserlich: kein Zeichen mit ausreichender Konfidenz erkennbar",
    "? = character not recognizable":
        "? = Zeichen nicht erkennbar",
    "Thresholds":
        "Schwellen",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "eine Zeile gilt ab einer Modellkonfidenz von {legible:.0f} % als lesbar; ein Zeichen wird angezeigt, wenn seine Stütze (Stimmen, gewichtet mit der Wahrscheinlichkeit, die das Modell ihm gibt, über alle Lesungen) {support:.0f} % erreicht, sonst «?».",
    "Illegible lines":
        "Unleserliche Zeilen",
    "{count} lines found but not recognizable, not shown":
        "{count} Zeilen gefunden, aber nicht erkennbar, nicht angezeigt",
    "support":
        "Stütze",
    "Single readings (model output, before the thresholds)":
        "Einzelne Lesungen (Modellausgabe, vor den Schwellen)",
    "Frames used in the fusion":
        "In der Fusion verwendete Frames",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Alle {count} Frames, aus denen das Ergebnis besteht: der Motivausschnitt jedes Frames, auf den Referenzframe ausgerichtet, wie er in die Fusion eingeht, mit seinem Gewicht (R = Referenzframe).",
    "Play / pause (Space)":
        "Wiedergabe / Pause (Leertaste)",
    "Fit":
        "Einpassen",
    "Choose the language":
        "Sprache wählen",
    "Before you start":
        "Bevor Sie beginnen",
    "What {app} produces":
        "Was {app} erzeugt",
    "How the result is obtained":
        "Wie das Ergebnis entsteht",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} erzeugt keine Bilder: Es kombiniert die Informationen, die in vielen Frames desselben Videos tatsächlich vorhanden sind. Es verfolgt den gezeichneten Bereich von Frame zu Frame, richtet jeden Frame mit Subpixel-Genauigkeit am Referenzframe aus, verwirft die Frames, die sich nicht zuverlässig ausrichten lassen, und verschmilzt die übrigen mit einem gewichteten, gegen Ausreißer robusten Mittelwert. Jeder Frame zeichnet das Motiv mit einer leicht anderen Verschiebung und anderem Rauschen auf: Zusammen sinkt das Rauschen und Details, die über mehrere Frames verteilt sind, treten hervor (Multi-Frame-Superauflösung). Die anschließende Dekonvolution und die Kontrastkorrekturen sind deterministische Operationen, deren Parameter alle im Bericht stehen.",
    "The result is a reconstruction":
        "Das Ergebnis ist eine Rekonstruktion",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "Das erhaltene Bild ist eine Rekonstruktion, die ausschließlich aus den echten Pixeln der verwendeten Frames berechnet wird; jeder davon steht mit seinem Gewicht im Bericht. Kein generatives Modell und keine künstliche Intelligenz fügt Details hinzu, ergänzt oder erfindet sie: Was in keinem Frame enthalten ist, kann im Ergebnis nicht erscheinen. Eine Rekonstruktion kann jedoch Artefakte enthalten (doppelte Kanten bei unvollkommener Ausrichtung, Halos der Dekonvolution) und ist nur so gut wie die Quelle: Vergleichen Sie sie immer mit den Originalframes.",
    "Character reading and country are estimates":
        "Zeichenlesung und Land sind Schätzungen",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "Die Zeichenlesung (OCR) und das Land des Kennzeichens sind dagegen Schätzungen von Erkennungsmodellen, die an Beispielen trainiert wurden und immer die wahrscheinlichsten Zeichen vorschlagen. Das Programm kombiniert mehrere Lesungen und markiert mit «?» oder als unleserlich, was seine Schwellen nicht erreicht, aber auch eine grün angezeigte Lesung kann falsch sein. Sie sind eine Hilfe, kein Beweis: Prüfen Sie jedes Zeichen mit eigenen Augen am Bild.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "Ich habe verstanden, dass das Ergebnis eine Rekonstruktion aus den Frames des Videos ist, in der nichts erfunden ist, während die Zeichenlesung und die Zuordnung des Landes zu prüfende Schätzungen sind.",
    "Accept and continue":
        "Akzeptieren und fortfahren",
    "Exit":
        "Beenden",
    "Vote by position": "Abstimmung je Position",
    "result": "Ergebnis",
    "Reading": "Lesung",
    "Agreement": "Übereinstimmung",
    "Method": "Methode",
    "Statement": "Erklärung",
    "pos.": "Pos.",
    "char.": "Zch.",
    "agreement": "Übereinst.",
    "alternatives": "Alternativen",
    "looks like": "ähnelt",
    "group": "Gruppe",
    "source": "Quelle",
    "text": "Text",
    "conf.": "Konf.",
    "frames": "Einzelbilder",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Von Ihnen gespeichert.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Mitgelieferte Voreinstellungen für die auf der Seite Motiv gewählte Art, danach Ihre eigenen.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» ist eine mitgelieferte Voreinstellung: wählen Sie einen anderen Namen.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Kennzeichen, Standard: Perspektive, schärfste 75 %, ×2, robuster Mittelwert, mäßige Dekonvolution. Der Ausgangspunkt.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Kennzeichen bei Nacht oder verrauscht: mehr Einzelbilder, mittlere Rauschunterdrückung, sanftere Dekonvolution mit starker Regularisierung, leichter lokaler Kontrast, Graustufen.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Entferntes, kleines Kennzeichen in vielen Einzelbildern: ×3, Verschieben und Addieren, fast alle Einzelbilder, niedrigere Ausrichtungsschwelle.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Fahrendes oder sich näherndes Fahrzeug mit Bewegungsunschärfe: nur die schärfere Hälfte der Einzelbilder, tolerantere Motivsuche, stärkere Dekonvolution.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Kennzeichen im Schatten oder Gegenlicht: mittlerer lokaler Kontrast, Graustufen, leichte Rauschunterdrückung.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Gesicht, Standard: affin, lokale Verfeinerung, leichte Rauschunterdrückung, sanfte Dekonvolution mit starker Regularisierung. Der Ausgangspunkt.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Gesicht bei Nacht oder verrauscht: mehr Einzelbilder, mittlere Rauschunterdrückung, sehr leichte Dekonvolution.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Gesicht, minimale Bearbeitung: Fusion nur mit automatischen Pegeln, ohne Rauschunterdrückung und Dekonvolution. Das vorsichtigste Ergebnis.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Entferntes, kleines Gesicht: ×3, fast alle Einzelbilder, niedrigere Ausrichtungsschwelle.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Gesicht im Schatten oder Gegenlicht: leichter lokaler Kontrast, sanfte Dekonvolution.",
}
