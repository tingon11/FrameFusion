# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Nederlands: traduzione olandese dei testi dell'interfaccia e del rapporto.

La chiave e' il testo inglese cosi' come compare nel codice (in tr() e N_()),
il valore la sua traduzione. I segnaposto tra graffe vanno lasciati identici.
Le chiavi non tradotte restano in inglese. Dopo ogni modifica:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py nl
"""

from __future__ import annotations

NAME = "Nederlands"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Kan de interface niet starten: {error}\n\n"
        "Installeer de afhankelijkheden met:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg niet gevonden. Download het via het vak FFmpeg op de pagina Configuratie, "
        "of installeer het en zet het in het PATH.",
    "Cannot check the latest ffmpeg version: {error}": "Kan de nieuwste ffmpeg-versie niet controleren: {error}",
    "Unexpected answer from the ffmpeg download site.": "Onverwacht antwoord van de downloadsite van ffmpeg.",
    "Downloading {label}": "{label} downloaden",
    "Download of {label} failed: {error}": "Download van {label} mislukt: {error}",
    "Invalid archive: suspicious path '{member}'.": "Ongeldig archief: verdacht pad ‘{member}’.",
    "The downloaded file is not a valid zip archive.": "Het gedownloade bestand is geen geldig zip-archief.",
    "The downloaded package does not contain {name}.": "Het gedownloade pakket bevat geen {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Kan ‘{name}’ niet bijwerken: bestanden in gebruik. Wacht tot de lopende fusie klaar is en probeer opnieuw.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Automatisch downloaden is alleen beschikbaar op Windows: installeer ffmpeg met de "
        "pakketbeheerder van het systeem.",
    "Extracting ffmpeg": "ffmpeg uitpakken",
    "The downloaded ffmpeg does not run on this PC.": "De gedownloade ffmpeg werkt niet op deze pc.",
    "{name} is missing after extraction.": "{name} ontbreekt na het uitpakken.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Controleren…",
    "Check": "Controleren",
    "Check for updates": "Zoeken naar updates",
    "Download / Update": "Downloaden / Bijwerken",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg is een apart programma (LGPL/GPL). De download haalt de officiële Windows-build "
        "van {url} en bewaart alleen ffmpeg.exe, LICENSE en README in de map tools\\ffmpeg "
        "naast het programma: geen installatie, geen wijzigingen aan het PATH.",
    "ffmpeg check failed": "Controle van ffmpeg mislukt",
    "tools folder": "map tools",
    "system PATH": "systeem-PATH",
    "Python package": "Python-pakket",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Engine: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Ontbreekt: download het met de knop rechts.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg niet gevonden: download het via het vak FFmpeg op de pagina Configuratie.",
    "ffmpeg missing: download it from the FFmpeg box.": "ffmpeg ontbreekt: download het via het vak FFmpeg.",
    "Checking the latest ffmpeg version…": "Nieuwste ffmpeg-versie controleren…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} is up-to-date.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Nieuwste versie: {latest}. Geïnstalleerd: {installed}. Nu downloaden?",
    "Update check failed": "Controle op updates mislukt",
    "Wait for the running fusion, then try again.": "Wacht tot de lopende fusie klaar is en probeer dan opnieuw.",
    "Downloading ffmpeg…": "ffmpeg downloaden…",
    "Downloading ffmpeg from {url}": "ffmpeg downloaden van {url}",
    "ffmpeg downloaded into {path}": "ffmpeg gedownload naar {path}",
    "Download cancelled.": "Download geannuleerd.",
    "ffmpeg download failed": "Download van ffmpeg mislukt",
    "ffmpeg: exit code {code}": "ffmpeg: exitcode {code}",
    "File not found: {path}": "Bestand niet gevonden: {path}",
    "The file has no recognizable video track.": "Het bestand bevat geen herkenbaar videospoor.",
    "Video size not recognized.": "Videoafmetingen niet herkend.",
    "Frame rate not recognized.": "Framesnelheid niet herkend.",
    "Invalid frame rate.": "Ongeldige framesnelheid.",
    "Unknown video duration (stream or damaged file).":
        "Onbekende videoduur (stream of beschadigd bestand).",
    "Zero video duration.": "Videoduur is nul.",
    "No frame at {seconds:.3f} s.": "Geen frame op {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg heeft het bestand niet geschreven.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "BEVESTIGEN",
    "WARNING": "WAARSCHUWING",
    "ERROR": "FOUT",
    "Yes": "Ja",

    # ----------------------------------------------------------- navigazione
    "PAGES": "PAGINA'S",
    "Configuration": "Configuratie",
    "Subject": "Onderwerp",
    "Frames, subject and reference": "Frames, onderwerp en referentie",
    "Fusion": "Fusie",
    "Multi-frame fusion and result": "Multiframe-fusie en resultaat",
    "{app}  /  PAGE {index:02d}": "{app}  /  PAGINA {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "geen",
    "Open video… (Ctrl+O)": "Video openen… (Ctrl+O)",
    "No video": "Geen video",
    "Reading…": "Lezen…",
    "Ready": "Gereed",
    "Error": "Fout",
    "Fusing…": "Fuseren…",
    "Fused": "Gefuseerd",

    # ------------------------------------------------------------- anteprima
    "Preview": "Voorbeeld",
    "Open a video to see the preview": "Open een video om het voorbeeld te zien",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "rechts slepen: onderwerpgebied  ·  scrollwiel: zoomen  ·  slepen: verschuiven  ·  dubbelklik: passend",
    "First frame (Home)": "Eerste frame (Home)",
    "Back 10 frames (Shift+←)": "10 frames terug (Shift+←)",
    "Previous frame (←)": "Vorig frame (←)",
    "Next frame (→)": "Volgend frame (→)",
    "Forward 10 frames (Shift+→)": "10 frames vooruit (Shift+→)",
    "Last frame (End)": "Laatste frame (End)",
    "Save frame": "Frame opslaan",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Slaat het getoonde frame verliesvrij op volledige resolutie op (Ctrl+S)",
    "Preview unavailable: {error}": "Voorbeeld niet beschikbaar: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+scrollwiel: zoomen  ·  scrollwiel: scrollen  ·  sleep I / O en de cursor  ·  dubbelklik op de liniaal: alles",
    "In  [I]": "In  [I]",
    "Out  [O]": "Uit  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Zet het begin van de selectie op de cursor (toets I)",
    "Sets the end of the selection at the cursor (key O)":
        "Zet het einde van de selectie op de cursor (toets O)",
    "Moves the cursor to the start of the selection": "Verplaatst de cursor naar het begin van de selectie",
    "Moves the cursor to the end of the selection": "Verplaatst de cursor naar het einde van de selectie",
    "CURSOR": "CURSOR",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Tijd (1:23.456, 83.4) of frame (f2000), dan Enter",
    "Zoom out (−)": "Uitzoomen (−)",
    "Zoom in (+)": "Inzoomen (+)",
    "All": "Alles",
    "Selection": "Selectie",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Selectie: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Weergave: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Tijd niet herkend: gebruik mm:ss.mmm, seconden of f<getal>.",
    "Open a video to see the timeline": "Open een video om de tijdlijn te zien",

    # -------------------------------------------------------------- soggetto
    "Select area": "Gebied selecteren",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Sleep daarna in het voorbeeld om het onderwerp te omkaderen (of sleep op elk moment met de rechtermuisknop); "
        "de fusie start vanzelf",
    "Moves the cursor to the reference frame": "Verplaatst de cursor naar het referentieframe",
    "Clear": "Wissen",
    "Fuse frames  →": "Frames fuseren  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Voert de multiframe-fusie uit op het geselecteerde bereik (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Omkader het onderwerp op een scherp frame: dat frame wordt de referentie en de fusie start.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Sleep in het voorbeeld om het onderwerp te omkaderen (Esc om te stoppen).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "Het onderwerpgebied is te klein: teken minstens {size} × {size} pixels.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Bereik ingesteld rond de referentie: f{first} → f{last}. Verplaats I / O om het te wijzigen.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Onderwerpgebied {width} × {height} op ({x}, {y}) in het referentieframe f{frame}",
    "Subject area cleared.": "Onderwerpgebied gewist.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Referentie f{frame} ligt buiten het bereik f{first} → f{last}: verplaats I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} frames in het bereik: selecteer er hoogstens {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Gebied {width} × {height} px op ({x}, {y})  ·  referentie f{frame}  ·  {count} frames f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Selecteer eerst het gebied van het onderwerp (kenteken, gezicht, voorwerp) op een scherp frame: sleep met "
        "de rechtermuisknop in het voorbeeld, of gebruik Gebied selecteren.",
    "The reference frame must be inside the selected range.":
        "Het referentieframe moet binnen het geselecteerde bereik liggen.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "Het bereik heeft {count} frames: selecteer er hoogstens {limit} rond de referentie.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Frames en uitlijning",
    "Motion model": "Bewegingsmodel",
    "Translation": "Translatie",
    "Rotation + translation": "Rotatie + translatie",
    "Affine": "Affien",
    "Perspective (homography)": "Perspectief (homografie)",
    "Subject search: minimum correlation": "Zoeken naar het onderwerp: minimale correlatie",
    "Minimum alignment quality (ECC)": "Minimale uitlijningskwaliteit (ECC)",
    "Sharpest frames kept": "Scherpste frames behouden",
    "Scale": "Vergroting",
    "Fusion method": "Fusiemethode",
    "Robust mean (outliers rejected)": "Robuust gemiddelde (uitschieters verworpen)",
    "Shift-and-add (normalized convolution)": "Shift-and-add (genormaliseerde convolutie)",
    "Median": "Mediaan",
    "Weight by sharpness": "Wegen op scherpte",
    "Equalize brightness": "Helderheid gelijkmaken",
    "Restoration": "Restauratie",
    "Noise reduction": "Ruisonderdrukking",
    "Off": "Uit",
    "Light": "Licht",
    "Medium": "Gemiddeld",
    "Strong": "Sterk",
    "Deconvolution iterations": "Deconvolutie-iteraties",
    "0 (none)": "0 (geen)",
    "not applied": "niet toegepast",
    "PSF σ (output pixels)": "PSF σ (uitvoerpixels)",
    "Automatic": "Automatisch",
    "Regularization (total variation)": "Regularisatie (totale variatie)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Meer iteraties verscherpen meer, maar versterken ook ruis en halo's; de regularisatie houdt de ruis in "
        "toom. Wijzig telkens een beetje en vergelijk.",
    "Presentation": "Presentatie",
    "Auto levels": "Automatische niveaus",
    "Local contrast (CLAHE)": "Lokaal contrast (CLAHE)",
    "Grayscale": "Grijstinten",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "De niveaus zijn een rechte lijn die vóór de deconvolutie wordt toegepast (zwart en wit op de percentielen "
        "0,5 en 99,5); het lokale contrast een egalisatie per zone. Alles staat in het rapport.",
    "Defaults": "Standaard",
    "Puts every parameter of the pipeline back to its default value":
        "Zet elke parameter van de pipeline terug op de standaardwaarde",
    "Parameters back to their defaults.": "Parameters teruggezet op de standaardwaarden.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Opgeslagen instellingen",
    "(none saved)": "(geen opgeslagen)",
    "Save…": "Opslaan…",
    "Saves the current parameters under a name (in config.json)":
        "Slaat de huidige parameters op onder een naam (in config.json)",
    "Delete": "Verwijderen",
    "From report…": "Uit rapport…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Laadt de parameters uit de report.json van een opgeslagen fusie",
    "Save settings": "Instellingen opslaan",
    "Name of these settings:": "Naam van deze instellingen:",
    "Settings «{name}» already exist. Replace them?": "De instellingen ‘{name}’ bestaan al. Vervangen?",
    "Settings «{name}» saved.": "Instellingen ‘{name}’ opgeslagen.",
    "Settings «{name}» loaded.": "Instellingen ‘{name}’ geladen.",
    "Delete settings": "Instellingen verwijderen",
    "Delete the settings «{name}»?": "De instellingen ‘{name}’ verwijderen?",
    "Settings «{name}» deleted.": "Instellingen ‘{name}’ verwijderd.",
    "Load parameters from a report": "Parameters laden uit een rapport",
    "Cannot read the report": "Kan het rapport niet lezen",
    "{name} is not a FrameFusion report.": "{name} is geen FrameFusion-rapport.",
    "Parameters loaded from {path}": "Parameters geladen uit {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Vergelijking",
    "FRAMES": "FRAMES",
    "RESULT": "RESULTAAT",
    "Ghost of the frames": "Spookbeeld van de frames",
    "Reference frame": "Referentieframe",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "SPOOKBEELD  ·  {count} FRAMES  ·  ×{scale}",
    "Final": "Definitief",
    "Fusion only": "Alleen fusie",
    "Draw the subject area on the Subject page, then run the fusion":
        "Teken het onderwerpgebied op de pagina Onderwerp en start daarna de fusie",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "scrollwiel: zoomen  ·  slepen: verschuiven  ·  dubbelklik: passend  ·  de twee weergaven bewegen samen  ·  "
        "spookbeeld: elk gebruikt frame, over elkaar gelegd op de positie waar het werd gevonden",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "REFERENTIE f{frame}  ·  BICUBISCH ×{scale}",
    "RESULT  ·  {count} FRAMES": "RESULTAAT  ·  {count} FRAMES",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Frame-extractie",
    "Subject detection": "Onderwerpdetectie",
    "Local alignment": "Lokale uitlijning",
    "Sub-pixel registration": "Subpixelregistratie",
    "Multi-frame fusion": "Multiframe-fusie",
    "Deconvolution and denoising": "Deconvolutie en ruisonderdrukking",
    "Single frame": "Enkel frame",
    "Save result": "Resultaat opslaan",
    "Saves images and report in a new folder (Ctrl+S)": "Slaat afbeeldingen en rapport op in een nieuwe map (Ctrl+S)",
    "Run fusion": "Fusie starten",
    "Runs the pipeline again with these parameters (F5)": "Voert de pipeline opnieuw uit met deze parameters (F5)",
    "Open folder": "Map openen",
    "Cancel": "Annuleren",
    "reused": "hergebruikt",
    "Fusion in progress…": "Fusie bezig…",
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Fusie: f{first} → f{last}, referentie f{ref}, gebied {width} × {height} op ({x}, {y}), ×{scale}, {method}",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} van {count} frames  ·  ×{scale}  ·  ruis σ {ref:.1f} → {fused:.1f} na de fusie  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fusie voltooid: {summary}",
    "Excluded: {list}": "Uitgesloten: {list}",
    "Fusion cancelled.": "Fusie geannuleerd.",
    "Fusion cancelled by the user": "Fusie geannuleerd door de gebruiker",
    "Fusion failed: see the log.": "Fusie mislukt: zie het logboek.",
    "Fusion failed": "Fusie mislukt",
    "Fusion in progress": "Fusie bezig",
    "The fusion is still running. Stop it and close?": "De fusie loopt nog. Stoppen en afsluiten?",
    "Saving the result…": "Resultaat opslaan…",
    "Saved in «{folder}».": "Opgeslagen in ‘{folder}’.",
    "Saved in {folder}": "Opgeslagen in {folder}",
    "Result, comparison images and report saved in {folder}":
        "Resultaat, vergelijkingsafbeeldingen en rapport opgeslagen in {folder}",

    # messaggi dei passaggi (fusion.py)
    "{done} / {total} frames decoded": "{done} / {total} frames gedecodeerd",
    "{count} frames decoded": "{count} frames gedecodeerd",
    "The video ended before the reference frame.": "De video eindigde vóór het referentieframe.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Zoeken naar het onderwerp op frames verkleind tot {percent:.0f} % (geheugenlimiet).",
    "searching the subject: {done} / {total}": "onderwerp zoeken: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Eén frame per {stride} behouden (geheugenlimiet voor grote gebieden).",
    "{done} / {total} frames read at full resolution": "{done} / {total} frames gelezen op volledige resolutie",
    "The reference frame could not be read.": "Het referentieframe kon niet worden gelezen.",
    "subject found in {found} / {total} frames": "onderwerp gevonden in {found} / {total} frames",
    "{done} / {total} frames aligned": "{done} / {total} frames uitgelijnd",
    "motion model: {model}": "bewegingsmodel: {model}",
    "{done} / {total} frames registered": "{done} / {total} frames geregistreerd",
    "{count} frames registered": "{count} frames geregistreerd",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} frames uitgelijnd met een eenvoudiger bewegingsmodel, omdat het gekozen model er niet op "
        "convergeerde.",
    "{count} frames selected": "{count} frames geselecteerd",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Slechts {count} bruikbare frames: het resultaat kan maar iets beter zijn dan de referentie. "
        "Vergroot het bereik of verlaag de kwaliteitsdrempel.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Vergroting verlaagd van ×{asked} naar ×{used}: het gebied is te groot.",
    "resampling on the fine grid: {percent:.0f} %": "herbemonstering op het fijne raster: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "shift-and-add: {done} / {total} frames",
    "{count} frames fused on a ×{scale} grid": "{count} frames gefuseerd op een ×{scale}-raster",
    "noise reduction ({level})": "ruisonderdrukking ({level})",
    "deconvolution: iteration {n} / {total}": "deconvolutie: iteratie {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} iteraties",
    "no deconvolution": "geen deconvolutie",
    "{width} × {height} pixels": "{width} × {height} pixels",

    # motivi di esclusione di un fotogramma
    "subject not found": "onderwerp niet gevonden",
    "not sampled (memory limit)": "niet bemonsterd (geheugenlimiet)",
    "frame not decoded": "frame niet gedecodeerd",
    "alignment failed": "uitlijning mislukt",
    "sub-pixel registration failed": "subpixelregistratie mislukt",
    "low alignment quality": "lage uitlijningskwaliteit",
    "less sharp than the selected ones": "minder scherp dan de geselecteerde",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Bron",
    "Open video…": "Video openen…",
    "Duration": "Duur",
    "Frames": "Frames",
    "Resolution": "Resolutie",
    "Codec": "Codec",
    "  (rotated {degrees}°)": "  (gedraaid {degrees}°)",
    "Open video": "Video openen",
    "Videos": "Video's",
    "All files": "Alle bestanden",
    "Reading {name}…": "{name} lezen…",
    "Cannot open the video": "Kan de video niet openen",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} frames, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{path} geopend — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Output": "Uitvoer",
    "Destination folder": "Doelmap",
    "Subfolder named after the video": "Submap met de naam van de video",
    "Browse…": "Bladeren…",
    "Format": "Formaat",
    "Color depth": "Kleurdiepte",
    "Also save every aligned frame (aligned/ folder)": "Ook elk uitgelijnd frame opslaan (map aligned/)",
    "next to the video": "naast de video",
    ", in a subfolder named after it": ", in een submap met de naam van de video",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Elke opgeslagen fusie krijgt een eigen map ({where}) met result.{ext}, de fusie vóór restauratie, "
        "het referentieframe ter vergelijking, report.txt, report.pdf en report.json (parameters, stappen, "
        "gebruikte frames, SHA-256). Afbeeldingen met {bits} bits per kanaal.",
    "Language": "Taal",
    "Interface language. The change is immediate and is saved for the next start.":
        "Taal van de interface. De wijziging is onmiddellijk en wordt bewaard voor de volgende start.",
    "Credits": "Colofon",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Vrije software onder de GNU GPL v3 met naamsvermelding van de auteur: zie de bestanden LICENSE en "
        "NOTICE. Videodecodering door FFmpeg, een apart programma met een eigen licentie; beeldverwerking met "
        "OpenCV en NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (verliesvrij)",
    "Saving frame {frame}…": "Frame {frame} opslaan…",
    "Saved {path}": "Opgeslagen: {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Frame f{frame} opgeslagen in {path} ({pix_fmt})",
    "Save failed": "Opslaan mislukt",
    "The folder does not exist yet.": "De map bestaat nog niet.",
    "Cannot open the folder": "Kan de map niet openen",
    "Open a video first.": "Open eerst een video.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "Kan {name} niet coderen.",
    "Writing the images…": "Afbeeldingen schrijven…",
    "Writing the PDF report…": "PDF-rapport schrijven…",
    "page {page} of {pages}": "pagina {page} van {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Referentie f{frame}  ·  bicubisch ×{scale}",
    "Result  ·  {count} frames": "Resultaat  ·  {count} frames",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Spookbeeld  ·  {count} frames, elk op de positie waar het werd gevonden",
    "Fusion before restoration": "Fusie vóór restauratie",
    "Writing the aligned frames: {done} / {total}": "Uitgelijnde frames schrijven: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "SHA-256-vingerafdrukken berekenen…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — rapport van de multiframe-fusie",
    "Created: {when}": "Aangemaakt: {when}",
    "File": "Bestand",
    "Size": "Grootte",
    "{size} bytes": "{size} bytes",
    "Video": "Video",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Range and subject": "Bereik en onderwerp",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} frames, {start} → {end})",
    "Subject area on the reference frame": "Onderwerpgebied op het referentieframe",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} pixels",
    "Parameters": "Parameters",
    "yes": "ja",
    "no": "nee",
    "Deconvolution": "Deconvolutie",
    "{iterations} Richardson-Lucy iterations": "{iterations} Richardson-Lucy-iteraties",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px van de uitvoer ({mode})",
    "automatic: measured on the edges of the fused image": "automatisch: gemeten op de randen van het gefuseerde beeld",
    "manual": "handmatig",
    "Steps": "Stappen",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} frames gedecodeerd door FFmpeg, exact op het frame; {scale}.",
    "subject search at full resolution": "onderwerp gezocht op volledige resolutie",
    "subject search at {percent:.0f} % of the resolution": "onderwerp gezocht op {percent:.0f} % van de resolutie",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Onderwerp vanaf het referentieframe voorwaarts en achterwaarts gevolgd met genormaliseerde "
        "kruiscorrelatie (OpenCV matchTemplate, TM_CCOEFF_NORMED); gevonden in {found} / {count} frames, "
        "op volledige resolutie eromheen bijgesneden.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Grove uitlijning van elk frame op de referentie met het ECC-algoritme (Evangelidis & Psarakis, "
        "2008), model: {model}, op gladgemaakte beelden.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC verfijnd op volledige resolutie (subpixelprecisie): {registered} frames geregistreerd. Selectie: "
        "ECC ≥ {quality:.2f}, de scherpste {keep} % (energie van de laplaciaan): {used} frames gebruikt.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: frames herbemonsterd op een ×{scale}-raster van de referentie (Lanczos), gewogen naar "
        "uitlijningskwaliteit{sharp}{equal}.",
    " and sharpness": " en scherpte",
    ", brightness equalized to the reference": ", helderheid gelijkgemaakt aan de referentie",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Alleen op de luminantie (de kleur wordt gladgemaakt: in gecomprimeerde video bevat die ruis, "
        "geen detail). Ruisonderdrukking: {denoise}. Deconvolutie: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Eerst automatische niveaus: luminantie {black:.3f} → 0, {white:.3f} → 1, dezelfde lijn op elk kanaal",
    "No auto levels": "Geen automatische niveaus",
    " (bilateral filter)": " (bilateraal filter)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, gaussiaanse PSF σ {sigma:.2f} px, {iterations} iteraties, regularisatie met totale "
        "variatie {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Presentatie: lokaal contrast {clahe}; {gray}. Enkel frame van {width} × {height} pixels.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, cliplimiet {clip:g})",
    "grayscale": "grijstinten",
    "color": "kleur",
    "Result": "Resultaat",
    "Frames used": "Gebruikte frames",
    "{used} of {count}": "{used} van {count}",
    "Estimated noise σ": "Geschatte ruis σ",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Methode van Immerkær, 0-255, op de videoresolutie: referentie {ref:.2f} → gefuseerd {fused:.2f} → "
        "definitief {final:.2f}. Deconvolutie versterkt fijn detail en ruis samen, dus de laatste waarde is "
        "niet alleen een maat voor de ruis.",
    "Samples per output pixel": "Monsters per uitvoerpixel",
    "Sub-pixel phases covered (4 × 4 grid)": "Gedekte subpixelfasen (4 × 4-raster)",
    "frame": "frame",
    "time": "tijd",
    "search": "zoeken",
    "sharp.": "scherp.",
    "weight": "gewicht",
    "used": "gebruikt",
    "model": "model",
    "note": "opm.",
    "(reference)": "(referentie)",
    "Files": "Bestanden",
    "aligned/: {count} aligned frames": "aligned/: {count} uitgelijnde frames",
    "Note": "Opmerking",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Het resultaat is een verbetering van de hierboven vermelde frames: het combineert informatie die "
        "daarin aanwezig is en voegt geen details toe. Fijne details op de grens van de resolutie, en tekens "
        "die op elkaar lijken, moeten aan de bronframes worden getoetst voordat u conclusies trekt.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Gereed.",
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  pagina   ·   ← →  frame   ·   I / O  bereik   ·   F5  fuseren   ·   Ctrl+S  opslaan",
    "ffmpeg missing": "ffmpeg ontbreekt",
    "Operation failed": "Bewerking mislukt",
    "ERROR - {title}: {message}": "FOUT - {title}: {message}",
    "Error: {title}": "Fout: {title}",
    "INTERNAL ERROR": "INTERNE FOUT",
    "Internal error: details in the log.": "Interne fout: details in het logboek.",
}
