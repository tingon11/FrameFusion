# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Italiano: traduzione dei testi dell'interfaccia e del rapporto.

La chiave e' il testo inglese cosi' come compare nel codice (in tr() e N_()),
il valore la sua traduzione. I segnaposto tra graffe vanno lasciati identici.
Le chiavi non tradotte restano in inglese. Dopo ogni modifica:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py
"""

from __future__ import annotations

NAME = "Italiano"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Impossibile avviare l'interfaccia: {error}\n\n"
        "Installa le dipendenze con:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg non trovato. Scaricalo dal riquadro FFmpeg della pagina Configurazione, "
        "oppure installalo e mettilo nel PATH.",
    "Cannot check the latest ffmpeg version: {error}": "Impossibile verificare l'ultima versione di ffmpeg: {error}",
    "Unexpected answer from the ffmpeg download site.": "Risposta inattesa dal sito di download di ffmpeg.",
    "Downloading {label}": "Scaricamento di {label}",
    "Download of {label} failed: {error}": "Scaricamento di {label} non riuscito: {error}",
    "Invalid archive: suspicious path '{member}'.": "Archivio non valido: percorso sospetto '{member}'.",
    "The downloaded file is not a valid zip archive.": "Il file scaricato non è un archivio zip valido.",
    "The downloaded package does not contain {name}.": "Il pacchetto scaricato non contiene {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Impossibile aggiornare '{name}': file in uso. Attendi la fine della fusione e riprova.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Il download automatico è disponibile solo su Windows: installa ffmpeg con il "
        "gestore dei pacchetti del sistema.",
    "Extracting ffmpeg": "Estrazione di ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "L'ffmpeg scaricato non si avvia su questo PC.",
    "{name} is missing after extraction.": "{name} manca dopo l'estrazione.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Verifica…",
    "Check": "Verifica",
    "Check for updates": "Cerca aggiornamenti",
    "Download / Update": "Scarica / Aggiorna",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg è un programma separato (LGPL/GPL). Il download prende il build ufficiale per "
        "Windows da {url} e tiene solo ffmpeg.exe, LICENSE e README nella cartella tools\\ffmpeg "
        "accanto al programma: nessuna installazione, nessuna modifica al PATH.",
    "ffmpeg check failed": "Verifica di ffmpeg non riuscita",
    "tools folder": "cartella tools",
    "system PATH": "PATH di sistema",
    "Python package": "pacchetto Python",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Motore: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Mancante: scaricalo con il pulsante a destra.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg non trovato: scaricalo dal riquadro FFmpeg della pagina Configurazione.",
    "ffmpeg missing: download it from the FFmpeg box.": "ffmpeg mancante: scaricalo dal riquadro FFmpeg.",
    "Checking the latest ffmpeg version…": "Verifica dell'ultima versione di ffmpeg…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} è aggiornato.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Ultima release: {latest}. Installata: {installed}. Scaricarla adesso?",
    "Update check failed": "Controllo aggiornamenti non riuscito",
    "Wait for the running fusion, then try again.": "Attendi la fine della fusione in corso, poi riprova.",
    "Downloading ffmpeg…": "Scaricamento di ffmpeg…",
    "Downloading ffmpeg from {url}": "Scaricamento di ffmpeg da {url}",
    "ffmpeg downloaded into {path}": "ffmpeg scaricato in {path}",
    "Download cancelled.": "Scaricamento annullato.",
    "ffmpeg download failed": "Scaricamento di ffmpeg non riuscito",
    "ffmpeg: exit code {code}": "ffmpeg: codice di uscita {code}",
    "File not found: {path}": "File non trovato: {path}",
    "The file has no recognizable video track.": "Il file non contiene una traccia video riconoscibile.",
    "Video size not recognized.": "Dimensioni del video non riconosciute.",
    "Frame rate not recognized.": "Frequenza dei fotogrammi non riconosciuta.",
    "Invalid frame rate.": "Frequenza dei fotogrammi non valida.",
    "Unknown video duration (stream or damaged file).":
        "Durata del video sconosciuta (flusso o file danneggiato).",
    "Zero video duration.": "Durata del video nulla.",
    "No frame at {seconds:.3f} s.": "Nessun fotogramma all'istante {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg non ha scritto il file.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "CONFERMA",
    "WARNING": "ATTENZIONE",
    "ERROR": "ERRORE",
    "Yes": "Sì",

    # ----------------------------------------------------------- navigazione
    "PAGES": "PAGINE",
    "Configuration": "Configurazione",
    "Subject": "Soggetto",
    "Frames, subject and reference": "Fotogrammi, soggetto e riferimento",
    "Fusion": "Fusione",
    "Multi-frame fusion and result": "Fusione multi-frame e risultato",
    "{app}  /  PAGE {index:02d}": "{app}  /  PAGINA {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "nessuno",
    "Open video… (Ctrl+O)": "Apri video… (Ctrl+O)",
    "No video": "Nessun video",
    "Reading…": "Lettura…",
    "Ready": "Pronto",
    "Error": "Errore",
    "Fusing…": "Fusione…",
    "Fused": "Fuso",

    # ------------------------------------------------------------- anteprima
    "Preview": "Anteprima",
    "Open a video to see the preview": "Apri un video per vedere l'anteprima",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "trascina col destro: area del soggetto  ·  rotellina: zoom  ·  trascina: sposta  ·  doppio clic: adatta",
    "First frame (Home)": "Primo fotogramma (Home)",
    "Back 10 frames (Shift+←)": "Indietro di 10 fotogrammi (Shift+←)",
    "Previous frame (←)": "Fotogramma precedente (←)",
    "Next frame (→)": "Fotogramma successivo (→)",
    "Forward 10 frames (Shift+→)": "Avanti di 10 fotogrammi (Shift+→)",
    "Last frame (End)": "Ultimo fotogramma (End)",
    "Save frame": "Salva fotogramma",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Salva il fotogramma mostrato a piena risoluzione, senza perdita (Ctrl+S)",
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Anteprima più grande: nasconde la timeline, i tasti I / O continuano a funzionare (F11)",
    "Preview unavailable: {error}": "Anteprima non disponibile: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+rotellina: zoom  ·  rotellina: scorri  ·  trascina I / O e il cursore  ·  doppio clic sul righello: tutto",
    "In  [I]": "Inizio  [I]",
    "Out  [O]": "Fine  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Mette l'inizio della selezione sul cursore (tasto I)",
    "Sets the end of the selection at the cursor (key O)":
        "Mette la fine della selezione sul cursore (tasto O)",
    "Moves the cursor to the start of the selection": "Porta il cursore all'inizio della selezione",
    "Moves the cursor to the end of the selection": "Porta il cursore alla fine della selezione",
    "CURSOR": "CURSORE",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Tempo (1:23.456, 83.4) o fotogramma (f2000), poi Invio",
    "Zoom out (−)": "Riduci (−)",
    "Zoom in (+)": "Ingrandisci (+)",
    "All": "Tutto",
    "Selection": "Selezione",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Selezione: f{first} → f{last}  ·  {count} fotogrammi  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Vista: {start} → {end}  ({seconds:.3f} s, {frames:.1f} fotogrammi)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Tempo non riconosciuto: usa mm:ss.mmm, secondi oppure f<numero>.",
    "Open a video to see the timeline": "Apri un video per vedere la timeline",

    # -------------------------------------------------------------- soggetto
    "Select area": "Seleziona area",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Poi trascina sull'anteprima per inquadrare il soggetto (o trascina col destro in qualsiasi momento); "
        "la fusione parte da sola",
    "Moves the cursor to the reference frame": "Porta il cursore sul fotogramma di riferimento",
    "Clear": "Cancella",
    "Fuse frames  →": "Fondi fotogrammi  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Avvia la fusione multi-frame sull'intervallo selezionato (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Inquadra il soggetto su un fotogramma nitido: quel fotogramma diventa il riferimento e la fusione parte.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Trascina sull'anteprima per inquadrare il soggetto (Esc per smettere).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "L'area del soggetto è troppo piccola: disegnane una di almeno {size} × {size} pixel.",
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Intervallo ristretto ai fotogrammi in cui il soggetto è stato seguito: f{first} → f{last}.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Intervallo impostato attorno al riferimento: f{first} → f{last}. Sposta I / O per cambiarlo.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Area del soggetto {width} × {height} in ({x}, {y}) sul fotogramma di riferimento f{frame}",
    "Subject area cleared.": "Area del soggetto cancellata.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Il riferimento f{frame} è fuori dall'intervallo f{first} → f{last}: sposta I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} fotogrammi nell'intervallo: selezionane al massimo {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Area {width} × {height} px in ({x}, {y})  ·  riferimento f{frame}  ·  {count} fotogrammi f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Prima seleziona l'area del soggetto (targa, volto, oggetto) su un fotogramma nitido: trascina col "
        "destro sull'anteprima, oppure usa Seleziona area.",
    "The reference frame must be inside the selected range.":
        "Il fotogramma di riferimento deve stare dentro l'intervallo selezionato.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "L'intervallo ha {count} fotogrammi: selezionane al massimo {limit} attorno al riferimento.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Fotogrammi e allineamento",
    "Motion model": "Modello di moto",
    "Translation": "Traslazione",
    "Rotation + translation": "Rotazione + traslazione",
    "Affine": "Affine",
    "Perspective (homography)": "Prospettiva (omografia)",
    "Subject search: minimum correlation": "Ricerca del soggetto: correlazione minima",
    "Minimum alignment quality (ECC)": "Qualità minima dell'allineamento (ECC)",
    "Sharpest frames kept": "Fotogrammi più nitidi tenuti",
    "Scale": "Ingrandimento",
    "Fusion method": "Metodo di fusione",
    "Robust mean (outliers rejected)": "Media robusta (anomali scartati)",
    "Shift-and-add (normalized convolution)": "Somma con spostamento (convoluzione normalizzata)",
    "Median": "Mediana",
    "Weight by sharpness": "Pesa per nitidezza",
    "Equalize brightness": "Uniforma la luminosità",
    "Restoration": "Restauro",
    "Noise reduction": "Riduzione del rumore",
    "Off": "Nessuna",
    "Light": "Leggera",
    "Medium": "Media",
    "Strong": "Forte",
    "Deconvolution iterations": "Iterazioni di deconvoluzione",
    "0 (none)": "0 (nessuna)",
    "not applied": "non applicata",
    "PSF σ (output pixels)": "PSF σ (pixel dell'uscita)",
    "Automatic": "Automatica",
    "Regularization (total variation)": "Regolarizzazione (variazione totale)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Più iterazioni rendono più nitido ma amplificano anche rumore e aloni; la regolarizzazione frena il "
        "rumore. Cambia poco alla volta e confronta.",
    "Presentation": "Presentazione",
    "Auto levels": "Livelli automatici",
    "Local contrast (CLAHE)": "Contrasto locale (CLAHE)",
    "Grayscale": "Scala di grigi",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "I livelli sono una retta applicata prima della deconvoluzione (nero e bianco ai percentili 0,5 e "
        "99,5); il contrasto locale un'equalizzazione a zone. Tutto scritto nel rapporto.",
    "Defaults": "Predefiniti",
    "Puts every parameter of the pipeline back to its default value":
        "Riporta ogni parametro della pipeline al suo valore predefinito",
    "Parameters back to their defaults.": "Parametri riportati ai valori predefiniti.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Impostazioni salvate",
    "(none saved)": "(nessuna salvata)",
    "Save…": "Salva…",
    "Saves the current parameters under a name (in config.json)":
        "Salva i parametri correnti con un nome (in config.json)",
    "Delete": "Elimina",
    "From report…": "Da rapporto…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Carica i parametri scritti nel report.json di una fusione salvata",
    "Save settings": "Salva impostazioni",
    "Name of these settings:": "Nome di queste impostazioni:",
    "Settings «{name}» already exist. Replace them?": "Le impostazioni «{name}» esistono già. Sostituirle?",
    "Settings «{name}» saved.": "Impostazioni «{name}» salvate.",
    "Settings «{name}» loaded.": "Impostazioni «{name}» caricate.",
    "Delete settings": "Elimina impostazioni",
    "Delete the settings «{name}»?": "Eliminare le impostazioni «{name}»?",
    "Settings «{name}» deleted.": "Impostazioni «{name}» eliminate.",
    "Load parameters from a report": "Carica i parametri da un rapporto",
    "Cannot read the report": "Impossibile leggere il rapporto",
    "{name} is not an IdentiFrame report.": "{name} non è un rapporto di IdentiFrame.",
    "Parameters loaded from {path}": "Parametri caricati da {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Confronto",
    "FRAMES": "FOTOGRAMMI",
    "RESULT": "RISULTATO",
    "Ghost of the frames": "Ghost dei fotogrammi",
    "Reference frame": "Fotogramma di riferimento",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "GHOST  ·  {count} FOTOGRAMMI  ·  ×{scale}",
    "Final": "Finale",
    "Fusion only": "Solo fusione",
    "Draw the subject area on the Subject page, then run the fusion":
        "Disegna l'area del soggetto nella pagina Soggetto, poi avvia la fusione",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "rotellina: zoom  ·  trascina: sposta  ·  doppio clic: adatta  ·  le due viste si muovono insieme  ·  "
        "ghost: ogni fotogramma usato, sovrapposto nella posizione in cui è stato trovato",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "RIFERIMENTO f{frame}  ·  BICUBICA ×{scale}",
    "RESULT  ·  {count} FRAMES": "RISULTATO  ·  {count} FOTOGRAMMI",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Estrazione dei fotogrammi",
    "Subject detection": "Rilevamento del soggetto",
    "Local alignment": "Allineamento locale",
    "Sub-pixel registration": "Registrazione sub-pixel",
    "Multi-frame fusion": "Fusione multi-frame",
    "Deconvolution and denoising": "Deconvoluzione e riduzione del rumore",
    "Single frame": "Fotogramma unico",
    "Save result": "Salva risultato",
    "Saves images and report in a new folder (Ctrl+S)": "Salva immagini e rapporto in una nuova cartella (Ctrl+S)",
    "Run fusion": "Avvia fusione",
    "Runs the pipeline again with these parameters (F5)": "Rifà la pipeline con questi parametri (F5)",
    "Open folder": "Apri cartella",
    "Cancel": "Annulla",
    "reused": "riusato",
    "Fusion in progress…": "Fusione in corso…",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} di {count} fotogrammi  ·  ×{scale}  ·  rumore σ {ref:.1f} → {fused:.1f} dopo la fusione  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fusione completata: {summary}",
    "Excluded: {list}": "Esclusi: {list}",
    "Fusion cancelled.": "Fusione annullata.",
    "Fusion cancelled by the user": "Fusione annullata dall'utente",
    "Fusion failed: see the log.": "Fusione non riuscita: vedi il registro.",
    "Fusion failed": "Fusione non riuscita",
    "Fusion in progress": "Fusione in corso",
    "The fusion is still running. Stop it and close?": "La fusione è ancora in corso. Interromperla e chiudere?",
    "Saving the result…": "Salvataggio del risultato…",
    "Saved in «{folder}».": "Salvato in «{folder}».",
    "Saved in {folder}": "Salvato in {folder}",
    "Result, comparison images and report saved in {folder}":
        "Risultato, immagini di confronto e rapporto salvati in {folder}",

    # messaggi dei passaggi (fusion.py)
    "{count} frames decoded": "{count} fotogrammi decodificati",
    "The video ended before the reference frame.": "Il video finisce prima del fotogramma di riferimento.",
    "Range set with I / O": "Intervallo impostato con I / O",
    "Frames examined":
        "Fotogrammi esaminati",
    "Frames that make up the result":
        "Fotogrammi che compongono il risultato",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "{count} fotogrammi esclusi perché vengono dopo più di {seconds:g} s senza un allineamento buono: da lì il soggetto non è più confermato (coperto, troppo piccolo o fuori inquadratura).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Soggetto seguito da f{first} a f{last}: oltre, manca o non è confermato per più di {seconds:g} s.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Ricerca del soggetto su fotogrammi ridotti al {percent:.0f} % (limite di memoria).",
    "searching the subject: {done} / {total}": "ricerca del soggetto: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Tenuto un fotogramma ogni {stride} (limite di memoria per aree grandi).",
    "{done} / {total} frames read at full resolution": "{done} / {total} fotogrammi letti a piena risoluzione",
    "The reference frame could not be read.": "Impossibile leggere il fotogramma di riferimento.",
    "subject found in {found} / {total} frames": "soggetto trovato in {found} / {total} fotogrammi",
    "{done} / {total} frames aligned": "{done} / {total} fotogrammi allineati",
    "motion model: {model}": "modello di moto: {model}",
    "{done} / {total} frames registered": "{done} / {total} fotogrammi registrati",
    "{count} frames registered": "{count} fotogrammi registrati",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} fotogrammi allineati con un modello di moto più semplice, perché quello scelto non convergeva "
        "su di loro.",
    "{count} frames selected": "{count} fotogrammi scelti",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Solo {count} fotogrammi utilizzabili: il risultato può essere solo di poco migliore del riferimento. "
        "Allarga l'intervallo o abbassa la soglia di qualità.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Ingrandimento ridotto da ×{asked} a ×{used}: l'area è troppo grande.",
    "resampling on the fine grid: {percent:.0f} %": "ricampionamento sulla griglia fine: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "somma con spostamento: {done} / {total} fotogrammi",
    "{count} frames fused on a ×{scale} grid": "{count} fotogrammi fusi su una griglia ×{scale}",
    "noise reduction ({level})": "riduzione del rumore ({level})",
    "deconvolution: iteration {n} / {total}": "deconvoluzione: iterazione {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} iterazioni",
    "no deconvolution": "nessuna deconvoluzione",
    "{width} × {height} pixels": "{width} × {height} pixel",

    # motivi di esclusione di un fotogramma
    "subject not found": "soggetto non trovato",
    "not sampled (memory limit)": "non campionato (limite di memoria)",
    "frame not decoded": "fotogramma non decodificato",
    "alignment failed": "allineamento non riuscito",
    "sub-pixel registration failed": "registrazione sub-pixel non riuscita",
    "low alignment quality": "allineamento poco affidabile",
    "less sharp than the selected ones": "meno nitido di quelli scelti",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Sorgente",
    "Open video…": "Apri video…",
    "Duration": "Durata",
    "Frames": "Fotogrammi",
    "Resolution": "Risoluzione",
    "Codec": "Codec",
    "  (rotated {degrees}°)": "  (ruotato {degrees}°)",
    "Open video": "Apri video",
    "Videos": "Video",
    "All files": "Tutti i file",
    "Reading {name}…": "Lettura di {name}…",
    "Cannot open the video": "Impossibile aprire il video",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} fotogrammi, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Aperto {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Output": "Uscita",
    "Destination folder": "Cartella di destinazione",
    "Subfolder named after the video": "Sottocartella con il nome del video",
    "Browse…": "Sfoglia…",
    "Format": "Formato",
    "Color depth": "Profondità colore",
    "Also save every aligned frame (aligned/ folder)": "Salva anche ogni fotogramma allineato (cartella aligned/)",
    "next to the video": "accanto al video",
    ", in a subfolder named after it": ", in una sottocartella con il suo nome",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Ogni fusione salvata ha una cartella sua ({where}) con result.{ext}, la fusione prima del restauro, "
        "il fotogramma di riferimento per il confronto, report.txt, report.pdf e report.json (parametri, "
        "passaggi, fotogrammi usati, SHA-256). Immagini a {bits} bit per canale.",
    "Language": "Lingua",
    "Interface language. The change is immediate and is saved for the next start.":
        "Lingua dell'interfaccia. Il cambio è immediato e viene ricordato al prossimo avvio.",
    "Credits": "Crediti",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Software libero sotto GNU GPL v3 con attribuzione dell'autore: vedi i file LICENSE e NOTICE. La "
        "decodifica video è di FFmpeg, programma separato con la propria licenza; l'elaborazione delle "
        "immagini usa OpenCV e NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (senza perdita)",
    "Saving frame {frame}…": "Salvataggio del fotogramma {frame}…",
    "Saved {path}": "Salvato {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Fotogramma f{frame} salvato in {path} ({pix_fmt})",
    "Save failed": "Salvataggio fallito",
    "The folder does not exist yet.": "La cartella non esiste ancora.",
    "Cannot open the folder": "Impossibile aprire la cartella",
    "Open a video first.": "Apri prima un video.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "Impossibile codificare {name}.",
    "Writing the images…": "Scrittura delle immagini…",
    "Writing the PDF report…": "Scrittura del rapporto PDF…",
    "page {page} of {pages}": "pagina {page} di {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Riferimento f{frame}  ·  bicubica ×{scale}",
    "Result  ·  {count} frames": "Risultato  ·  {count} fotogrammi",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Ghost  ·  {count} fotogrammi, ciascuno nella posizione in cui è stato trovato",
    "Fusion before restoration": "Fusione prima del restauro",
    "Writing the aligned frames: {done} / {total}": "Scrittura dei fotogrammi allineati: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Calcolo delle impronte SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — rapporto di fusione multi-frame",
    "Created: {when}": "Creato: {when}",
    "File": "File",
    "Size": "Dimensione",
    "{size} bytes": "{size} byte",
    "Video": "Video",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Range and subject": "Intervallo e soggetto",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} fotogrammi, {start} → {end})",
    "Subject area on the reference frame": "Area del soggetto sul fotogramma di riferimento",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} pixel",
    "Parameters": "Parametri",
    "yes": "sì",
    "no": "no",
    "Deconvolution": "Deconvoluzione",
    "{iterations} Richardson-Lucy iterations": "{iterations} iterazioni di Richardson-Lucy",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px dell'uscita ({mode})",
    "automatic: measured on the edges of the fused image": "automatica: misurata sui bordi dell'immagine fusa",
    "manual": "manuale",
    "Steps": "Passaggi",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} fotogrammi decodificati da FFmpeg, esatti al fotogramma; {scale}.",
    "subject search at full resolution": "ricerca del soggetto a piena risoluzione",
    "subject search at {percent:.0f} % of the resolution": "ricerca del soggetto al {percent:.0f} % della risoluzione",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Soggetto seguito dal fotogramma di riferimento in avanti e all'indietro per correlazione incrociata "
        "normalizzata (OpenCV matchTemplate, TM_CCOEFF_NORMED); trovato in {found} / {count} fotogrammi, "
        "ritagliati a piena risoluzione attorno a lui.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Allineamento grossolano di ogni fotogramma sul riferimento con l'algoritmo ECC (Evangelidis & "
        "Psarakis, 2008), modello: {model}, su immagini smussate.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC raffinato a piena risoluzione (precisione sub-pixel): {registered} fotogrammi registrati. "
        "Selezione: ECC ≥ {quality:.2f}, il {keep} % più nitido (energia del laplaciano): {used} fotogrammi usati.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: fotogrammi ricampionati su una griglia ×{scale} del riferimento (Lanczos), pesati per "
        "qualità dell'allineamento{sharp}{equal}.",
    " and sharpness": " e nitidezza",
    ", brightness equalized to the reference": ", luminosità uniformata al riferimento",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Sulla sola luminanza (il colore viene smussato: nel video compresso porta rumore, non "
        "dettaglio). Riduzione del rumore: {denoise}. Deconvoluzione: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Prima i livelli automatici: luminanza {black:.3f} → 0, {white:.3f} → 1, stessa retta su ogni canale",
    "No auto levels": "Senza livelli automatici",
    " (bilateral filter)": " (filtro bilaterale)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, PSF gaussiana σ {sigma:.2f} px, {iterations} iterazioni, regolarizzazione a "
        "variazione totale {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Presentazione: contrasto locale {clahe}; {gray}. Fotogramma unico di {width} × {height} pixel.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, limite di clip {clip:g})",
    "grayscale": "scala di grigi",
    "color": "a colori",
    "Result": "Risultato",
    "Frames used": "Fotogrammi usati",
    "{used} of {count}": "{used} di {count}",
    "Estimated noise σ": "Rumore σ stimato",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Metodo di Immerkær, 0-255, alla risoluzione del video: riferimento {ref:.2f} → fusione {fused:.2f} → "
        "finale {final:.2f}. La deconvoluzione alza insieme dettaglio fine e rumore: l'ultimo valore non misura "
        "solo il rumore.",
    "Samples per output pixel": "Campioni per pixel dell'uscita",
    "Sub-pixel phases covered (4 × 4 grid)": "Fasi sub-pixel coperte (griglia 4 × 4)",
    "frame": "fotogr.",
    "time": "tempo",
    "search": "ricerca",
    "sharp.": "nitid.",
    "weight": "peso",
    "used": "usato",
    "model": "modello",
    "note": "nota",
    "(reference)": "(riferimento)",
    "Files": "File",
    "aligned/: {count} aligned frames": "aligned/: {count} fotogrammi allineati",
    "Note": "Nota",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Il risultato è un miglioramento dei fotogrammi elencati sopra: combina informazioni presenti in "
        "essi e non aggiunge dettagli. I dettagli fini al limite della risoluzione, e i caratteri che si "
        "somigliano, vanno verificati sui fotogrammi originali prima di trarre conclusioni.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Pronto.",
    "ffmpeg missing": "ffmpeg mancante",
    "Operation failed": "Operazione fallita",
    "ERROR - {title}: {message}": "ERRORE - {title}: {message}",
    "Error: {title}": "Errore: {title}",
    "INTERNAL ERROR": "ERRORE INTERNO",
    "Internal error: details in the log.": "Errore interno: dettagli nel registro.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Tipo di soggetto",
    "Parameters set for the subject type: {subject}.": "Parametri impostati per il tipo di soggetto: {subject}.",
    "Face": "Volto",
    "pose or expression differs from the reference": "posa o espressione diverse dal riferimento",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Volto: raffinamento locale non rigido dopo l'ECC su {count} fotogrammi, spostamento medio {residual:.2f} px del video.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Volto: l'area è troppo piccola per il raffinamento locale (almeno {size} px): solo allineamento rigido.",
    "simil.": "somigl.",
    "Local refinement (face)": "Raffinamento locale (volto)",
    "not applied: area too small, rigid alignment only": "non applicato: area troppo piccola, solo allineamento rigido",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Volto: l'area del soggetto è di {width} × {height} pixel nel video. La fusione combina i fotogrammi la cui posa ed espressione coincidono con il riferimento e dà meno peso alle parti che differiscono; non può creare tratti che nessun fotogramma mostra. Con un volto più stretto di circa 60 pixel il risultato può migliorare l'aspetto complessivo ma non far emergere tratti identificativi: confrontalo con il fotogramma di riferimento e con i singoli fotogrammi prima di trarre qualsiasi conclusione sull'identità.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Volto: dopo il modello rigido, un raffinamento locale non rigido (flusso ottico di Farneback tra il riferimento e il fotogramma allineato, lisciato e limitato in ampiezza) segue espressione e movimenti della testa; una confidenza per pixel (coerenza avanti-indietro e correlazione locale) pesa ogni campione nella fusione. I fotogrammi con somiglianza locale al riferimento sotto {limit:.2f} restano fuori (posa o espressione cambiate).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} fotogrammi raffinati; somiglianza locale media al riferimento {similarity:.2f}, spostamento locale medio {displacement:.2f} px del video; {excluded} fotogrammi esclusi per posa o espressione diverse.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fusione: {subject}, f{first} → f{last}, riferimento f{ref}, area {width} × {height} in ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Ctrl+1/2/3  pagina   ·   ← →  fotogramma   ·   Spazio  riproduci   ·   I / O  intervallo   ·   F5  fondi   ·   Ctrl+S  salva",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} fotogrammi allineati con un modello di moto più semplice, perché quello scelto dava una deformazione non plausibile (scala, taglio o prospettiva oltre i limiti).",
    "persp.": "prosp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Volto: i campioni fuori dall'ellisse inscritta nell'area contano poco, e lì il risultato mostra il fotogramma di riferimento: lo sfondo si muove in modo diverso dal volto.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Targa e Testo: un allineamento rigido per fotogramma; i caratteri si leggono con fast-plate-ocr (targhe) o PaddleOCR (scritte, anche su più righe). Volto: dopo l'allineamento, un raffinamento locale non rigido segue espressione e movimenti della testa, i fotogrammi con una posa diversa vengono esclusi e il restauro è più leggero. Cambiare tipo carica i suoi predefiniti.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Legge la targa (fast-plate-ocr) o la scritta (PaddleOCR) sul risultato e su fusioni indipendenti di gruppi di fotogrammi, e vota carattere per carattere",
    "OCR models": "Modelli OCR",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "I caratteri vengono letti da due modelli eseguiti da OpenCV, scaricati a richiesta in tools\\ocr e mai inclusi nel programma (circa 37 MB): fast-plate-ocr per le targhe (MIT, di ankandrew) e PaddleOCR PP-OCRv6 per le scritte in molte lingue (Apache 2.0, Baidu / PaddleOCR, conversione ONNX di RapidOCR). Ogni file viene controllato con la sua impronta SHA-256; licenze e provenienza vengono salvate accanto ai modelli.",
    "Downloading the OCR models…": "Scaricamento dei modelli OCR…",
    "Reading the characters…": "Lettura dei caratteri…",
    "OCR models download failed": "Scaricamento dei modelli OCR non riuscito",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "Scaricamento dei modelli OCR: {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Manca il modello OCR per questo tipo di soggetto: scaricalo dal riquadro Modelli OCR della pagina Configurazione.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "premi Leggi caratteri (automatico per targhe e scritte quando i modelli OCR sono pronti)",
    "model confidence {confidence:.0f} %": "fiducia del modello {confidence:.0f} %",
    "OCR models check failed": "Controllo dei modelli OCR non riuscito",
    "OCR: {plate} (plates), {text} (texts)": "OCR: {plate} (targhe), {text} (scritte)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Mancanti (facoltativi, per leggere targhe e scritte): scaricali con il pulsante a destra.",
    "OCR models ready: {path}": "Modelli OCR pronti: {path}",
    "possible country ({share:.0f} %)": "possibile paese ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "possibile paese: {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  targhe: {plate}  ·  scritte: {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Manca il modello per le scritte: scaricalo con il pulsante a destra.",
    "The model for plates is missing: download it with the button on the right.": "Manca il modello per le targhe: scaricalo con il pulsante a destra.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Scritta, standard: prospettiva, il 75 % più nitido, ×2, media robusta, deconvoluzione moderata. Il punto di partenza.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Scritta di notte o rumorosa: più fotogrammi, riduzione del rumore media, deconvoluzione più dolce con regolarizzazione forte, contrasto locale leggero, scala di grigi.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Scritta lontana e piccola ripresa in molti fotogrammi: ×3, shift-and-add, quasi tutti i fotogrammi, soglia di allineamento più bassa.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Scritta su un veicolo in movimento o ripresa da una telecamera in movimento, con mosso: solo la metà più nitida dei fotogrammi, ricerca del soggetto più tollerante, deconvoluzione più forte.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Scritta in ombra o in controluce: contrasto locale medio, scala di grigi, riduzione del rumore leggera.",
    "Plate": "Targa",
    "Text": "Testo",
    "No text line found inside the area: the whole area was read as one line.": "Nessuna riga di testo trovata nell'area: tutta l'area è stata letta come una riga.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "Nessun carattere trovato: disegna l'area stretta attorno alla targa o alla scritta, e controlla ingrandimento e restauro.",
    "Cannot load the OCR model {name}: {error}": "Impossibile caricare il modello OCR {name}: {error}",
    "The OCR model configuration {name} is not valid.": "La configurazione del modello OCR {name} non è valida.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Lettura automatica di un modello OCR, da verificare sulle immagini: i caratteri dalla forma simile (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) possono essere letti male allo stesso modo in ogni lettura, e il voto non può accorgersene. Il possibile paese della targa è una stima del modello dall'aspetto della targa, non una verifica.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), eseguito da {runtime}: si leggono il risultato e {groups} fusioni di gruppi indipendenti di fotogrammi, ciascuna restaurata con gli stessi parametri; le letture vengono allineate e votate carattere per carattere, pesate per la probabilità che il modello dà a ogni carattere (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), eseguito da {runtime}: le righe di testo vengono trovate nel risultato, poi ogni riga viene letta sul risultato e su {groups} fusioni di gruppi indipendenti di fotogrammi, ciascuna restaurata con gli stessi parametri; ogni riga viene votata carattere per carattere, pesata per la probabilità che il modello dà a ogni carattere (Quiala et al., 2023).",
    "the whole area": "tutta l'area",
    "Model confidence": "Fiducia del modello",
    "Area read": "Area letta",
    "Text lines": "Righe di testo",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} pixel del risultato",
    "Possible country": "Possibile paese",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, probabilità media dei caratteri letti nel risultato",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % dei voti), stimato dal modello dall'aspetto della targa",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV non riesce a caricare il modello scaricato {name}.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name}: il file scaricato non è quello previsto (la sua impronta SHA-256 è diversa).",
    "Read characters": "Leggi caratteri",
    "CHARACTERS": "CARATTERI",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Caratteri letti: {text}  ·  accordo {agreement:.0f} %  ·  {count} letture",
    "Character reading": "Lettura dei caratteri",
    "reading…": "lettura in corso…",
    "no characters found: draw the area tight around the text": "nessun carattere trovato: disegna l'area stretta attorno alla scritta",
    "agreement {agreement:.0f} %  ·  {count} readings": "accordo {agreement:.0f} %  ·  {count} letture",
    "Character reading failed: {error}": "Lettura dei caratteri non riuscita: {error}",
    "doubtful: {list}": "dubbi: {list}",
    "check by eye: {list}": "verifica a occhio: {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Troppo pochi fotogrammi per gruppi indipendenti: letto solo il risultato, senza voto.",
    "Character reading (OCR)": "Lettura dei caratteri (OCR)",
    "illegible":
        "illeggibile",
    "no character recognizable with enough confidence":
        "nessun carattere riconoscibile con fiducia sufficiente",
    "{count} illegible lines not shown":
        "{count} righe illeggibili non mostrate",
    "not recognizable (?): {list}":
        "non riconoscibili (?): {list}",
    "illegible: no character recognizable with enough confidence":
        "illeggibile: nessun carattere riconoscibile con fiducia sufficiente",
    "? = character not recognizable":
        "? = carattere non riconoscibile",
    "Thresholds":
        "Soglie",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "una riga conta come leggibile da una fiducia del modello del {legible:.0f} %; un carattere si mostra quando il suo sostegno (voti pesati per la probabilità che il modello gli dà, su tutte le letture) arriva al {support:.0f} %, altrimenti «?».",
    "Illegible lines":
        "Righe illeggibili",
    "{count} lines found but not recognizable, not shown":
        "{count} righe trovate ma non riconoscibili, non mostrate",
    "support":
        "sostegno",
    "Single readings (model output, before the thresholds)":
        "Letture singole (uscita del modello, prima delle soglie)",
    "Frames used in the fusion":
        "Fotogrammi usati nella fusione",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Tutti i {count} fotogrammi che compongono il risultato: l'area del soggetto di ciascuno, allineata al fotogramma di riferimento come entra nella fusione, con il suo peso (R = fotogramma di riferimento).",
    "Play / pause (Space)":
        "Riproduci / pausa (Spazio)",
    "Fit":
        "Adatta",
    "Choose the language":
        "Scegli la lingua",
    "Before you start":
        "Prima di iniziare",
    "What {app} produces":
        "Che cosa produce {app}",
    "How the result is obtained":
        "Come si ottiene il risultato",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} non crea immagini: combina le informazioni realmente presenti in molti fotogrammi dello stesso video. Segue di fotogramma in fotogramma l'area che disegni, allinea ogni fotogramma a quello di riferimento con precisione inferiore al pixel, scarta i fotogrammi che non si allineano in modo affidabile e fonde gli altri con una media pesata resistente ai valori anomali. Ogni fotogramma registra il soggetto con uno spostamento leggermente diverso e un rumore diverso: combinandoli il rumore cala ed emergono dettagli distribuiti su più fotogrammi (super-risoluzione multi-frame). La deconvoluzione e le correzioni di contrasto che seguono sono operazioni deterministiche, con tutti i parametri scritti nel rapporto.",
    "The result is a reconstruction":
        "Il risultato è una ricostruzione",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "L'immagine ottenuta è una ricostruzione calcolata solo dai pixel reali dei fotogrammi usati, ciascuno elencato nel rapporto con il suo peso. Nessun modello generativo o intelligenza artificiale aggiunge, completa o immagina dettagli: ciò che non c'è in nessun fotogramma non può comparire nel risultato. Una ricostruzione può però contenere artefatti (bordi sdoppiati dove l'allineamento è imperfetto, aloni della deconvoluzione) e vale quanto la sorgente: confrontala sempre con i fotogrammi originali.",
    "Character reading and country are estimates":
        "Lettura dei caratteri e paese sono stime",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "La lettura dei caratteri (OCR) e il paese della targa sono invece stime di modelli di riconoscimento addestrati su esempi, che propongono sempre i caratteri più probabili. Il programma combina più letture e segna con «?» o come illeggibile ciò che non raggiunge le sue soglie, ma anche una lettura mostrata in verde può essere sbagliata. Sono un aiuto, non una prova: controlla ogni carattere a occhio sull'immagine.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "Ho compreso che il risultato è una ricostruzione dai fotogrammi del video, in cui nulla è inventato, mentre la lettura dei caratteri e l'attribuzione del paese sono stime da verificare.",
    "Accept and continue":
        "Accetta e continua",
    "Exit":
        "Esci",
    "Vote by position": "Voto per posizione",
    "result": "risultato",
    "Reading": "Lettura",
    "Agreement": "Accordo",
    "Method": "Metodo",
    "Statement": "Dichiarazione",
    "pos.": "pos.",
    "char.": "car.",
    "agreement": "accordo",
    "alternatives": "alternative",
    "looks like": "somiglia a",
    "group": "gruppo",
    "source": "origine",
    "text": "testo",
    "conf.": "conf.",
    "frames": "fotogrammi",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Salvata da te.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Preset di serie per il tipo di soggetto scelto nella pagina Soggetto, poi i tuoi.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» è un preset di serie: scegli un altro nome.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Targa, standard: prospettiva, 75 % più nitidi, ×2, media robusta, deconvoluzione moderata. Il punto di partenza.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Targa di notte o rumorosa: più fotogrammi, riduzione del rumore media, deconvoluzione più dolce con regolarizzazione forte, contrasto locale leggero, scala di grigi.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Targa lontana e piccola ripresa in molti fotogrammi: ×3, somma con spostamento, quasi tutti i fotogrammi, soglia di allineamento più bassa.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Veicolo in movimento o che si avvicina, con mosso: solo la metà più nitida dei fotogrammi, ricerca del soggetto più tollerante, deconvoluzione più forte.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Targa in ombra o in controluce: contrasto locale medio, scala di grigi, riduzione del rumore leggera.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Volto, standard: affine, raffinamento locale, riduzione del rumore leggera, deconvoluzione dolce con regolarizzazione forte. Il punto di partenza.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Volto di notte o rumoroso: più fotogrammi, riduzione del rumore media, deconvoluzione molto leggera.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Volto, elaborazione minima: fusione con i soli livelli automatici, senza riduzione del rumore né deconvoluzione. Il risultato più prudente.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Volto lontano e piccolo: ×3, quasi tutti i fotogrammi, soglia di allineamento più bassa.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Volto in ombra o in controluce: contrasto locale leggero, deconvoluzione dolce.",
}
