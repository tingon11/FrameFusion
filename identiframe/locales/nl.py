# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Grotere voorvertoning: verbergt de tijdlijn, de toetsen I / O blijven werken (F11)",
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
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Bereik verkleind tot de frames waarin het onderwerp werd gevolgd: f{first} → f{last}.",
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
    "{name} is not an IdentiFrame report.": "{name} is geen IdentiFrame-rapport.",
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
    "{count} frames decoded": "{count} frames gedecodeerd",
    "The video ended before the reference frame.": "De video eindigde vóór het referentieframe.",
    "Range set with I / O": "Met I / O ingesteld bereik",
    "Frames examined":
        "Onderzochte frames",
    "Frames that make up the result":
        "Frames waaruit het resultaat bestaat",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "{count} frames weggelaten omdat ze na meer dan {seconds:g} s zonder goede uitlijning komen: vanaf daar is het onderwerp niet meer bevestigd (bedekt, te klein of buiten beeld).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Onderwerp gevolgd van f{first} tot f{last}: daarbuiten ontbreekt het, of is het niet bevestigd, langer dan {seconds:g} s.",
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
    "ffmpeg missing": "ffmpeg ontbreekt",
    "Operation failed": "Bewerking mislukt",
    "ERROR - {title}: {message}": "FOUT - {title}: {message}",
    "Error: {title}": "Fout: {title}",
    "INTERNAL ERROR": "INTERNE FOUT",
    "Internal error: details in the log.": "Interne fout: details in het logboek.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Soort onderwerp",
    "Parameters set for the subject type: {subject}.": "Parameters ingesteld voor het soort onderwerp: {subject}.",
    "Face": "Gezicht",
    "pose or expression differs from the reference": "pose of uitdrukking verschilt van de referentie",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Gezicht: lokale, niet-starre verfijning na ECC op {count} frames, gemiddelde verplaatsing {residual:.2f} px van de video.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Gezicht: het gebied is te klein voor de lokale verfijning (minstens {size} px): alleen starre uitlijning.",
    "simil.": "gelijk.",
    "Local refinement (face)": "Lokale verfijning (gezicht)",
    "not applied: area too small, rigid alignment only": "niet toegepast: gebied te klein, alleen starre uitlijning",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Gezicht: het onderwerpgebied is {width} × {height} pixels groot in de video. De fusie combineert frames waarvan pose en uitdrukking overeenkomen met de referentie en geeft minder gewicht aan de delen die verschillen; ze kan geen kenmerken scheppen die geen enkel frame toont. Bij een gezicht smaller dan ongeveer 60 pixels kan het resultaat het algemene beeld verbeteren, maar geen identificerende kenmerken onthullen: vergelijk het met het referentieframe en met de losse frames voordat u conclusies trekt over de identiteit.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Gezicht: na het starre model volgt een lokale, niet-starre verfijning (optische stroom van Farneback tussen de referentie en het uitgelijnde frame, gladgemaakt en begrensd in amplitude) de uitdrukking en hoofdbeweging; een betrouwbaarheid per pixel (heen-en-terugconsistentie en lokale correlatie) weegt elk monster in de fusie. Frames waarvan de lokale gelijkenis met de referentie onder {limit:.2f} ligt, vallen af (pose of uitdrukking veranderd).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} frames verfijnd; gemiddelde lokale gelijkenis met de referentie {similarity:.2f}, gemiddelde lokale verplaatsing {displacement:.2f} px van de video; {excluded} frames afgevallen wegens een andere pose of uitdrukking.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fusie: {subject}, f{first} → f{last}, referentie f{ref}, gebied {width} × {height} op ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Ctrl+1/2/3  pagina   ·   ← →  frame   ·   Spatie  afspelen   ·   I / O  bereik   ·   F5  fuseren   ·   Ctrl+S  opslaan",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} frames uitgelijnd met een eenvoudiger bewegingsmodel, omdat het gekozen model een onwaarschijnlijke vervorming gaf (schaal, afschuiving of perspectief buiten de grenzen).",
    "persp.": "persp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Gezicht: monsters buiten de in het gebied ingeschreven ellips tellen weinig mee, en daar toont het resultaat het referentieframe: de achtergrond beweegt anders dan het gezicht.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Kenteken en Tekst: één starre uitlijning per frame; de tekens worden gelezen met fast-plate-ocr (kentekens) of PaddleOCR (teksten, ook over meerdere regels). Gezicht: na de uitlijning volgt een lokale niet-starre verfijning de expressie en de hoofdbeweging, frames met een andere pose worden weggelaten en het herstel is lichter. Het type wijzigen laadt de standaardwaarden ervan.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Leest het kenteken (fast-plate-ocr) of de tekst (PaddleOCR) in het resultaat en in onafhankelijke fusies van groepen frames, en stemt teken voor teken",
    "OCR models": "OCR-modellen",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "De tekens worden gelezen door twee modellen die OpenCV uitvoert, op verzoek gedownload naar tools\\ocr en nooit deel van het programma (ongeveer 37 MB): fast-plate-ocr voor kentekens (MIT, van ankandrew) en PaddleOCR PP-OCRv6 voor teksten in veel talen (Apache 2.0, Baidu / PaddleOCR, ONNX-conversie door RapidOCR). Elk bestand wordt gecontroleerd met zijn SHA-256-vingerafdruk; licenties en herkomst worden naast de modellen opgeslagen.",
    "Downloading the OCR models…": "OCR-modellen downloaden…",
    "Reading the characters…": "Tekens lezen…",
    "OCR models download failed": "Downloaden van de OCR-modellen mislukt",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "OCR-modellen downloaden: {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Het OCR-model voor dit onderwerptype ontbreekt: download het in het vak OCR-modellen op de pagina Configuratie.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "druk op Tekens lezen (automatisch voor kentekens en teksten als de OCR-modellen klaar zijn)",
    "model confidence {confidence:.0f} %": "modelbetrouwbaarheid {confidence:.0f} %",
    "OCR models check failed": "Controle van de OCR-modellen mislukt",
    "OCR: {plate} (plates), {text} (texts)": "OCR: {plate} (kentekens), {text} (teksten)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Ontbreken (optioneel, om kentekens en teksten te lezen): download ze met de knop rechts.",
    "OCR models ready: {path}": "OCR-modellen klaar: {path}",
    "possible country ({share:.0f} %)": "mogelijk land ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "mogelijk land: {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  kentekens: {plate}  ·  teksten: {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Het model voor teksten ontbreekt: download het met de knop rechts.",
    "The model for plates is missing: download it with the button on the right.": "Het model voor kentekens ontbreekt: download het met de knop rechts.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Tekst, standaard: perspectief, scherpste 75 %, ×2, robuust gemiddelde, matige deconvolutie. Het uitgangspunt.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Tekst 's nachts of met ruis: meer frames, middelmatige ruisonderdrukking, zachtere deconvolutie met sterke regularisatie, licht lokaal contrast, grijswaarden.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Verre, kleine tekst in veel frames: ×3, verschuiven en optellen, bijna alle frames, lagere uitlijningsdrempel.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Tekst op een rijdend voertuig of gefilmd met een bewegende camera, met bewegingsonscherpte: alleen de scherpste helft van de frames, tolerantere zoektocht naar het onderwerp, sterkere deconvolutie.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Tekst in de schaduw of in tegenlicht: middelmatig lokaal contrast, grijswaarden, lichte ruisonderdrukking.",
    "Plate": "Kenteken",
    "Text": "Tekst",
    "No text line found inside the area: the whole area was read as one line.": "Geen tekstregel in het gebied gevonden: het hele gebied is als één regel gelezen.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "Geen tekens gevonden: teken het gebied strak rond het kenteken of de tekst, en controleer vergroting en herstel.",
    "Cannot load the OCR model {name}: {error}": "Kan het OCR-model {name} niet laden: {error}",
    "The OCR model configuration {name} is not valid.": "De configuratie van het OCR-model {name} is ongeldig.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Automatische lezing door een OCR-model, te controleren op de afbeeldingen: tekens met een gelijkende vorm (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) kunnen in elke lezing op dezelfde manier verkeerd gelezen worden, en de stemming kan dat niet zien. Het mogelijke land van het kenteken is een schatting van het model op basis van het uiterlijk van het kenteken, geen controle.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), uitgevoerd door {runtime}: het resultaat en {groups} fusies van onafhankelijke groepen frames, elk hersteld met dezelfde parameters, worden gelezen; de lezingen worden uitgelijnd en teken voor teken gestemd, gewogen naar de waarschijnlijkheid die het model aan elk teken geeft (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), uitgevoerd door {runtime}: de tekstregels worden in het resultaat gevonden, daarna wordt elke regel gelezen in het resultaat en in {groups} fusies van onafhankelijke groepen frames, elk hersteld met dezelfde parameters; elke regel wordt teken voor teken gestemd, gewogen naar de waarschijnlijkheid die het model aan elk teken geeft (Quiala et al., 2023).",
    "the whole area": "het hele gebied",
    "Model confidence": "Modelbetrouwbaarheid",
    "Area read": "Gelezen gebied",
    "Text lines": "Tekstregels",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} pixels van het resultaat",
    "Possible country": "Mogelijk land",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, gemiddelde waarschijnlijkheid van de in het resultaat gelezen tekens",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % van de stemmen), door het model geschat op basis van het uiterlijk van het kenteken",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV kan het gedownloade model {name} niet laden.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name}: het gedownloade bestand is niet het verwachte (de SHA-256-vingerafdruk is anders).",
    "Read characters": "Tekens lezen",
    "CHARACTERS": "TEKENS",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Gelezen tekens: {text}  ·  overeenstemming {agreement:.0f} %  ·  {count} lezingen",
    "Character reading": "Tekens lezen",
    "reading…": "bezig met lezen…",
    "no characters found: draw the area tight around the text": "geen tekens gevonden: teken het gebied strak rond de tekst",
    "agreement {agreement:.0f} %  ·  {count} readings": "overeenstemming {agreement:.0f} %  ·  {count} lezingen",
    "Character reading failed: {error}": "Tekens lezen mislukt: {error}",
    "doubtful: {list}": "twijfelachtig: {list}",
    "check by eye: {list}": "met het oog controleren: {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Te weinig frames voor onafhankelijke groepen: alleen het resultaat is gelezen, zonder stemming.",
    "Character reading (OCR)": "Tekens lezen (OCR)",
    "illegible":
        "onleesbaar",
    "no character recognizable with enough confidence":
        "geen teken herkenbaar met voldoende betrouwbaarheid",
    "{count} illegible lines not shown":
        "{count} onleesbare regels niet getoond",
    "not recognizable (?): {list}":
        "niet herkenbaar (?): {list}",
    "illegible: no character recognizable with enough confidence":
        "onleesbaar: geen teken herkenbaar met voldoende betrouwbaarheid",
    "? = character not recognizable":
        "? = teken niet herkenbaar",
    "Thresholds":
        "Drempels",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "een regel telt als leesbaar vanaf een modelbetrouwbaarheid van {legible:.0f} %; een teken wordt getoond als zijn steun (stemmen gewogen met de waarschijnlijkheid die het model eraan geeft, over alle lezingen) {support:.0f} % bereikt, anders «?».",
    "Illegible lines":
        "Onleesbare regels",
    "{count} lines found but not recognizable, not shown":
        "{count} regels gevonden maar niet herkenbaar, niet getoond",
    "support":
        "steun",
    "Single readings (model output, before the thresholds)":
        "Losse lezingen (uitvoer van het model, vóór de drempels)",
    "Frames used in the fusion":
        "Frames gebruikt in de fusie",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Alle {count} frames waaruit het resultaat bestaat: het onderwerpgebied van elk frame, uitgelijnd op het referentieframe zoals het de fusie ingaat, met zijn gewicht (R = referentieframe).",
    "Play / pause (Space)":
        "Afspelen / pauze (spatie)",
    "Fit":
        "Passend",
    "Choose the language":
        "Kies de taal",
    "Before you start":
        "Voordat u begint",
    "What {app} produces":
        "Wat {app} maakt",
    "How the result is obtained":
        "Hoe het resultaat ontstaat",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} maakt geen beelden: het combineert de informatie die werkelijk aanwezig is in veel frames van dezelfde video. Het volgt het getekende gebied van frame tot frame, lijnt elk frame met subpixelprecisie uit op het referentieframe, verwerpt de frames die niet betrouwbaar uitlijnen en voegt de overige samen met een gewogen gemiddelde dat bestand is tegen uitschieters. Elk frame legt het onderwerp vast met een iets andere verschuiving en andere ruis: samen daalt de ruis en komen details naar voren die over meerdere frames verspreid zijn (multi-frame superresolutie). De deconvolutie en de contrastcorrecties die volgen zijn deterministische bewerkingen, met al hun parameters in het rapport.",
    "The result is a reconstruction":
        "Het resultaat is een reconstructie",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "Het verkregen beeld is een reconstructie die alleen uit de echte pixels van de gebruikte frames is berekend, elk met zijn gewicht vermeld in het rapport. Geen generatief model of kunstmatige intelligentie voegt details toe, vult ze aan of verzint ze: wat in geen enkel frame staat, kan niet in het resultaat verschijnen. Een reconstructie kan wel artefacten bevatten (dubbele randen waar de uitlijning onvolmaakt is, halo's van de deconvolutie) en is zo goed als de bron: vergelijk haar altijd met de originele frames.",
    "Character reading and country are estimates":
        "Tekenlezing en land zijn schattingen",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "De tekenlezing (OCR) en het land van de kentekenplaat zijn daarentegen schattingen van herkenningsmodellen die op voorbeelden zijn getraind en altijd de meest waarschijnlijke tekens voorstellen. Het programma combineert meerdere lezingen en markeert met «?» of als onleesbaar wat zijn drempels niet haalt, maar ook een groen getoonde lezing kan fout zijn. Ze zijn een hulpmiddel, geen bewijs: controleer elk teken met het oog op het beeld.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "Ik begrijp dat het resultaat een reconstructie uit de frames van de video is, waarin niets verzonnen is, terwijl de tekenlezing en de toekenning van het land te controleren schattingen zijn.",
    "Accept and continue":
        "Accepteren en doorgaan",
    "Exit":
        "Afsluiten",
    "Vote by position": "Stemming per positie",
    "result": "resultaat",
    "Reading": "Lezing",
    "Agreement": "Overeenstemming",
    "Method": "Methode",
    "Statement": "Verklaring",
    "pos.": "pos.",
    "char.": "teken",
    "agreement": "overeenst.",
    "alternatives": "alternatieven",
    "looks like": "lijkt op",
    "group": "groep",
    "source": "bron",
    "text": "tekst",
    "conf.": "betr.",
    "frames": "frames",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Door u opgeslagen.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Ingebouwde voorinstellingen voor het soort onderwerp dat op de pagina Onderwerp is gekozen, daarna die van u.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» is een ingebouwde voorinstelling: kies een andere naam.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Kenteken, standaard: perspectief, scherpste 75 %, ×2, robuust gemiddelde, matige deconvolutie. Het uitgangspunt.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Kenteken 's nachts of met ruis: meer frames, middelmatige ruisonderdrukking, zachtere deconvolutie met sterke regularisatie, licht lokaal contrast, grijswaarden.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Ver, klein kenteken in veel frames: ×3, verschuiven en optellen, bijna alle frames, lagere uitlijningsdrempel.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Rijdend of naderend voertuig met bewegingsonscherpte: alleen de scherpste helft van de frames, tolerantere zoektocht naar het onderwerp, sterkere deconvolutie.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Kenteken in de schaduw of in tegenlicht: middelmatig lokaal contrast, grijswaarden, lichte ruisonderdrukking.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Gezicht, standaard: affien, lokale verfijning, lichte ruisonderdrukking, zachte deconvolutie met sterke regularisatie. Het uitgangspunt.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Gezicht 's nachts of met ruis: meer frames, middelmatige ruisonderdrukking, zeer lichte deconvolutie.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Gezicht, minimale bewerking: fusie met alleen automatische niveaus, zonder ruisonderdrukking en deconvolutie. Het voorzichtigste resultaat.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Ver, klein gezicht: ×3, bijna alle frames, lagere uitlijningsdrempel.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Gezicht in de schaduw of in tegenlicht: licht lokaal contrast, zachte deconvolutie.",
}
