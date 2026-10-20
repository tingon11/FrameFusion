# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Ελληνικά: traduzione dei testi dell'interfaccia e del rapporto.

La chiave e' il testo inglese cosi' come compare nel codice (in tr() e N_()),
il valore la sua traduzione. I segnaposto tra graffe vanno lasciati identici.
Le chiavi non tradotte restano in inglese. Dopo ogni modifica:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py el
"""

from __future__ import annotations

NAME = "Ελληνικά"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Δεν είναι δυνατή η εκκίνηση της διεπαφής: {error}\n\n"
        "Εγκαταστήστε τις εξαρτήσεις με:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "Το ffmpeg δεν βρέθηκε. Κατεβάστε το από το πλαίσιο FFmpeg της σελίδας Διαμόρφωση, "
        "ή εγκαταστήστε το και βάλτε το στο PATH.",
    "Cannot check the latest ffmpeg version: {error}":
        "Δεν είναι δυνατός ο έλεγχος της τελευταίας έκδοσης του ffmpeg: {error}",
    "Unexpected answer from the ffmpeg download site.": "Μη αναμενόμενη απάντηση από τον ιστότοπο λήψης του ffmpeg.",
    "Downloading {label}": "Λήψη του {label}",
    "Download of {label} failed: {error}": "Η λήψη του {label} απέτυχε: {error}",
    "Invalid archive: suspicious path '{member}'.": "Μη έγκυρο αρχείο: ύποπτη διαδρομή '{member}'.",
    "The downloaded file is not a valid zip archive.": "Το αρχείο που κατέβηκε δεν είναι έγκυρο αρχείο zip.",
    "The downloaded package does not contain {name}.": "Το πακέτο που κατέβηκε δεν περιέχει το {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Δεν είναι δυνατή η ενημέρωση του '{name}': αρχεία σε χρήση. Περιμένετε να τελειώσει η σύντηξη "
        "και δοκιμάστε ξανά.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Η αυτόματη λήψη είναι διαθέσιμη μόνο στα Windows: εγκαταστήστε το ffmpeg με τον "
        "διαχειριστή πακέτων του συστήματος.",
    "Extracting ffmpeg": "Αποσυμπίεση του ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "Το ffmpeg που κατέβηκε δεν εκτελείται σε αυτόν τον υπολογιστή.",
    "{name} is missing after extraction.": "Το {name} λείπει μετά την αποσυμπίεση.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Έλεγχος…",
    "Check": "Έλεγχος",
    "Check for updates": "Έλεγχος για ενημερώσεις",
    "Download / Update": "Λήψη / Ενημέρωση",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "Το ffmpeg είναι ξεχωριστό πρόγραμμα (LGPL/GPL). Η λήψη παίρνει την επίσημη έκδοση για "
        "Windows από το {url} και κρατά μόνο τα ffmpeg.exe, LICENSE και README στον φάκελο tools\\ffmpeg "
        "δίπλα στο πρόγραμμα: καμία εγκατάσταση, καμία αλλαγή στο PATH.",
    "ffmpeg check failed": "Ο έλεγχος του ffmpeg απέτυχε",
    "tools folder": "φάκελος tools",
    "system PATH": "PATH συστήματος",
    "Python package": "πακέτο Python",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Μηχανή: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Λείπει: κατεβάστε το με το κουμπί στα δεξιά.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "Το ffmpeg δεν βρέθηκε: κατεβάστε το από το πλαίσιο FFmpeg της σελίδας Διαμόρφωση.",
    "ffmpeg missing: download it from the FFmpeg box.": "Λείπει το ffmpeg: κατεβάστε το από το πλαίσιο FFmpeg.",
    "Checking the latest ffmpeg version…": "Έλεγχος της τελευταίας έκδοσης του ffmpeg…",
    "ffmpeg {version} is up to date.": "Το ffmpeg {version} είναι ενημερωμένο.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Τελευταία έκδοση: {latest}. Εγκατεστημένη: {installed}. Λήψη τώρα;",
    "Update check failed": "Ο έλεγχος ενημερώσεων απέτυχε",
    "Wait for the running fusion, then try again.": "Περιμένετε να τελειώσει η σύντηξη σε εξέλιξη και δοκιμάστε ξανά.",
    "Downloading ffmpeg…": "Λήψη του ffmpeg…",
    "Downloading ffmpeg from {url}": "Λήψη του ffmpeg από το {url}",
    "ffmpeg downloaded into {path}": "Το ffmpeg κατέβηκε στο {path}",
    "Download cancelled.": "Η λήψη ακυρώθηκε.",
    "ffmpeg download failed": "Η λήψη του ffmpeg απέτυχε",
    "ffmpeg: exit code {code}": "ffmpeg: κωδικός εξόδου {code}",
    "File not found: {path}": "Το αρχείο δεν βρέθηκε: {path}",
    "The file has no recognizable video track.": "Το αρχείο δεν περιέχει αναγνωρίσιμη ροή βίντεο.",
    "Video size not recognized.": "Οι διαστάσεις του βίντεο δεν αναγνωρίστηκαν.",
    "Frame rate not recognized.": "Ο ρυθμός καρέ δεν αναγνωρίστηκε.",
    "Invalid frame rate.": "Μη έγκυρος ρυθμός καρέ.",
    "Unknown video duration (stream or damaged file).":
        "Άγνωστη διάρκεια βίντεο (ροή ή κατεστραμμένο αρχείο).",
    "Zero video duration.": "Μηδενική διάρκεια βίντεο.",
    "No frame at {seconds:.3f} s.": "Κανένα καρέ στα {seconds:.3f} s.",
    "ffmpeg did not write the file.": "Το ffmpeg δεν έγραψε το αρχείο.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "ΕΠΙΒΕΒΑΙΩΣΗ",
    "WARNING": "ΠΡΟΕΙΔΟΠΟΙΗΣΗ",
    "ERROR": "ΣΦΑΛΜΑ",
    "Yes": "Ναι",

    # ----------------------------------------------------------- navigazione
    "PAGES": "ΣΕΛΙΔΕΣ",
    "Configuration": "Διαμόρφωση",
    "Subject": "Θέμα",
    "Frames, subject and reference": "Καρέ, θέμα και αναφορά",
    "Fusion": "Σύντηξη",
    "Multi-frame fusion and result": "Σύντηξη πολλαπλών καρέ και αποτέλεσμα",
    "{app}  /  PAGE {index:02d}": "{app}  /  ΣΕΛΙΔΑ {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "κανένα",
    "Open video… (Ctrl+O)": "Άνοιγμα βίντεο… (Ctrl+O)",
    "No video": "Χωρίς βίντεο",
    "Reading…": "Ανάγνωση…",
    "Ready": "Έτοιμο",
    "Error": "Σφάλμα",
    "Fusing…": "Σύντηξη…",
    "Fused": "Συντηγμένο",

    # ------------------------------------------------------------- anteprima
    "Preview": "Προεπισκόπηση",
    "Open a video to see the preview": "Ανοίξτε ένα βίντεο για να δείτε την προεπισκόπηση",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "δεξί σύρσιμο: περιοχή θέματος  ·  ροδέλα: ζουμ  ·  σύρσιμο: μετακίνηση  ·  διπλό κλικ: προσαρμογή",
    "First frame (Home)": "Πρώτο καρέ (Home)",
    "Back 10 frames (Shift+←)": "Πίσω 10 καρέ (Shift+←)",
    "Previous frame (←)": "Προηγούμενο καρέ (←)",
    "Next frame (→)": "Επόμενο καρέ (→)",
    "Forward 10 frames (Shift+→)": "Εμπρός 10 καρέ (Shift+→)",
    "Last frame (End)": "Τελευταίο καρέ (End)",
    "Save frame": "Αποθήκευση καρέ",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Αποθηκεύει το εμφανιζόμενο καρέ σε πλήρη ανάλυση, χωρίς απώλειες (Ctrl+S)",
    "Preview unavailable: {error}": "Η προεπισκόπηση δεν είναι διαθέσιμη: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+ροδέλα: ζουμ  ·  ροδέλα: κύλιση  ·  σύρετε τα I / O και τον δρομέα  ·  διπλό κλικ στον χάρακα: όλα",
    "In  [I]": "Αρχή  [I]",
    "Out  [O]": "Τέλος  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Ορίζει την αρχή της επιλογής στον δρομέα (πλήκτρο I)",
    "Sets the end of the selection at the cursor (key O)":
        "Ορίζει το τέλος της επιλογής στον δρομέα (πλήκτρο O)",
    "Moves the cursor to the start of the selection": "Μετακινεί τον δρομέα στην αρχή της επιλογής",
    "Moves the cursor to the end of the selection": "Μετακινεί τον δρομέα στο τέλος της επιλογής",
    "CURSOR": "ΔΡΟΜΕΑΣ",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Χρόνος (1:23.456, 83.4) ή καρέ (f2000), μετά Enter",
    "Zoom out (−)": "Σμίκρυνση (−)",
    "Zoom in (+)": "Μεγέθυνση (+)",
    "All": "Όλα",
    "Selection": "Επιλογή",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Επιλογή: f{first} → f{last}  ·  {count} καρέ  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Προβολή: {start} → {end}  ({seconds:.3f} s, {frames:.1f} καρέ)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Ο χρόνος δεν αναγνωρίστηκε: χρησιμοποιήστε mm:ss.mmm, δευτερόλεπτα ή f<αριθμός>.",
    "Open a video to see the timeline": "Ανοίξτε ένα βίντεο για να δείτε τη χρονογραμμή",

    # -------------------------------------------------------------- soggetto
    "Select area": "Επιλογή περιοχής",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Έπειτα σύρετε στην προεπισκόπηση για να πλαισιώσετε το θέμα (ή σύρετε με το δεξί ανά πάσα στιγμή)· "
        "η σύντηξη ξεκινά μόνη της",
    "Moves the cursor to the reference frame": "Μετακινεί τον δρομέα στο καρέ αναφοράς",
    "Clear": "Καθαρισμός",
    "Fuse frames  →": "Σύντηξη καρέ  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Εκτελεί τη σύντηξη πολλαπλών καρέ στο επιλεγμένο εύρος (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Πλαισιώστε το θέμα σε ένα καθαρό καρέ: αυτό το καρέ γίνεται η αναφορά και η σύντηξη ξεκινά.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Σύρετε στην προεπισκόπηση για να πλαισιώσετε το θέμα (Esc για διακοπή).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "Η περιοχή του θέματος είναι πολύ μικρή: σχεδιάστε τουλάχιστον {size} × {size} pixel.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Το εύρος ορίστηκε γύρω από την αναφορά: f{first} → f{last}. Μετακινήστε τα I / O για να το αλλάξετε.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Περιοχή θέματος {width} × {height} στο ({x}, {y}) στο καρέ αναφοράς f{frame}",
    "Subject area cleared.": "Η περιοχή του θέματος καθαρίστηκε.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Η αναφορά f{frame} είναι εκτός του εύρους f{first} → f{last}: μετακινήστε τα I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} καρέ στο εύρος: επιλέξτε το πολύ {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Περιοχή {width} × {height} px στο ({x}, {y})  ·  αναφορά f{frame}  ·  {count} καρέ f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Επιλέξτε πρώτα την περιοχή του θέματος (πινακίδα, πρόσωπο, αντικείμενο) σε ένα καθαρό καρέ: σύρετε με "
        "το δεξί στην προεπισκόπηση, ή χρησιμοποιήστε το Επιλογή περιοχής.",
    "The reference frame must be inside the selected range.":
        "Το καρέ αναφοράς πρέπει να βρίσκεται μέσα στο επιλεγμένο εύρος.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "Το εύρος έχει {count} καρέ: επιλέξτε το πολύ {limit} γύρω από την αναφορά.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Καρέ και ευθυγράμμιση",
    "Motion model": "Μοντέλο κίνησης",
    "Translation": "Μετατόπιση",
    "Rotation + translation": "Περιστροφή + μετατόπιση",
    "Affine": "Αφινικό",
    "Perspective (homography)": "Προοπτικό (ομογραφία)",
    "Subject search: minimum correlation": "Αναζήτηση θέματος: ελάχιστη συσχέτιση",
    "Minimum alignment quality (ECC)": "Ελάχιστη ποιότητα ευθυγράμμισης (ECC)",
    "Sharpest frames kept": "Ευκρινέστερα καρέ που διατηρούνται",
    "Scale": "Μεγέθυνση",
    "Fusion method": "Μέθοδος σύντηξης",
    "Robust mean (outliers rejected)": "Εύρωστος μέσος (απόρριψη ακραίων τιμών)",
    "Shift-and-add (normalized convolution)": "Μετατόπιση και άθροιση (κανονικοποιημένη συνέλιξη)",
    "Median": "Διάμεσος",
    "Weight by sharpness": "Στάθμιση κατά ευκρίνεια",
    "Equalize brightness": "Εξίσωση φωτεινότητας",
    "Restoration": "Αποκατάσταση",
    "Noise reduction": "Μείωση θορύβου",
    "Off": "Καμία",
    "Light": "Ελαφριά",
    "Medium": "Μέτρια",
    "Strong": "Ισχυρή",
    "Deconvolution iterations": "Επαναλήψεις αποσυνέλιξης",
    "0 (none)": "0 (καμία)",
    "not applied": "δεν εφαρμόζεται",
    "PSF σ (output pixels)": "PSF σ (pixel εξόδου)",
    "Automatic": "Αυτόματο",
    "Regularization (total variation)": "Ομαλοποίηση (ολική κύμανση)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Περισσότερες επαναλήψεις οξύνουν περισσότερο, αλλά ενισχύουν και τον θόρυβο και τα φωτοστέφανα· η "
        "ομαλοποίηση συγκρατεί τον θόρυβο. Αλλάζετε λίγο κάθε φορά και συγκρίνετε.",
    "Presentation": "Παρουσίαση",
    "Auto levels": "Αυτόματα επίπεδα",
    "Local contrast (CLAHE)": "Τοπική αντίθεση (CLAHE)",
    "Grayscale": "Κλίμακα του γκρι",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Τα επίπεδα είναι μια ευθεία που εφαρμόζεται πριν από την αποσυνέλιξη (μαύρο και λευκό στα "
        "εκατοστημόρια 0,5 και 99,5)· η τοπική αντίθεση μια εξίσωση κατά ζώνες. Όλα καταγράφονται στην έκθεση.",
    "Defaults": "Προεπιλογές",
    "Puts every parameter of the pipeline back to its default value":
        "Επαναφέρει κάθε παράμετρο της ροής επεξεργασίας στην προεπιλεγμένη τιμή της",
    "Parameters back to their defaults.": "Οι παράμετροι επανήλθαν στις προεπιλογές τους.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Αποθηκευμένες ρυθμίσεις",
    "(none saved)": "(καμία αποθηκευμένη)",
    "Save…": "Αποθήκευση…",
    "Saves the current parameters under a name (in config.json)":
        "Αποθηκεύει τις τρέχουσες παραμέτρους με ένα όνομα (στο config.json)",
    "Delete": "Διαγραφή",
    "From report…": "Από έκθεση…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Φορτώνει τις παραμέτρους που είναι γραμμένες στο report.json μιας αποθηκευμένης σύντηξης",
    "Save settings": "Αποθήκευση ρυθμίσεων",
    "Name of these settings:": "Όνομα αυτών των ρυθμίσεων:",
    "Settings «{name}» already exist. Replace them?": "Οι ρυθμίσεις «{name}» υπάρχουν ήδη. Αντικατάσταση;",
    "Settings «{name}» saved.": "Οι ρυθμίσεις «{name}» αποθηκεύτηκαν.",
    "Settings «{name}» loaded.": "Οι ρυθμίσεις «{name}» φορτώθηκαν.",
    "Delete settings": "Διαγραφή ρυθμίσεων",
    "Delete the settings «{name}»?": "Διαγραφή των ρυθμίσεων «{name}»;",
    "Settings «{name}» deleted.": "Οι ρυθμίσεις «{name}» διαγράφηκαν.",
    "Load parameters from a report": "Φόρτωση παραμέτρων από έκθεση",
    "Cannot read the report": "Δεν είναι δυνατή η ανάγνωση της έκθεσης",
    "{name} is not a FrameFusion report.": "Το {name} δεν είναι έκθεση του FrameFusion.",
    "Parameters loaded from {path}": "Παράμετροι φορτωμένες από το {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Σύγκριση",
    "FRAMES": "ΚΑΡΕ",
    "RESULT": "ΑΠΟΤΕΛΕΣΜΑ",
    "Ghost of the frames": "Φάντασμα των καρέ",
    "Reference frame": "Καρέ αναφοράς",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "ΦΑΝΤΑΣΜΑ  ·  {count} ΚΑΡΕ  ·  ×{scale}",
    "Final": "Τελικό",
    "Fusion only": "Μόνο σύντηξη",
    "Draw the subject area on the Subject page, then run the fusion":
        "Σχεδιάστε την περιοχή του θέματος στη σελίδα Θέμα και μετά εκτελέστε τη σύντηξη",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "ροδέλα: ζουμ  ·  σύρσιμο: μετακίνηση  ·  διπλό κλικ: προσαρμογή  ·  οι δύο προβολές κινούνται μαζί  ·  "
        "φάντασμα: κάθε καρέ που χρησιμοποιήθηκε, υπερτιθέμενο στη θέση όπου βρέθηκε",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "ΑΝΑΦΟΡΑ f{frame}  ·  ΔΙΚΥΒΙΚΗ ×{scale}",
    "RESULT  ·  {count} FRAMES": "ΑΠΟΤΕΛΕΣΜΑ  ·  {count} ΚΑΡΕ",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Ροή επεξεργασίας",
    "Frame extraction": "Εξαγωγή καρέ",
    "Subject detection": "Εντοπισμός θέματος",
    "Local alignment": "Τοπική ευθυγράμμιση",
    "Sub-pixel registration": "Συνταύτιση υπο-pixel",
    "Multi-frame fusion": "Σύντηξη πολλαπλών καρέ",
    "Deconvolution and denoising": "Αποσυνέλιξη και αποθορυβοποίηση",
    "Single frame": "Ενιαίο καρέ",
    "Save result": "Αποθήκευση αποτελέσματος",
    "Saves images and report in a new folder (Ctrl+S)": "Αποθηκεύει εικόνες και έκθεση σε νέο φάκελο (Ctrl+S)",
    "Run fusion": "Εκτέλεση σύντηξης",
    "Runs the pipeline again with these parameters (F5)": "Εκτελεί ξανά τη ροή επεξεργασίας με αυτές τις παραμέτρους (F5)",
    "Open folder": "Άνοιγμα φακέλου",
    "Cancel": "Ακύρωση",
    "reused": "επαναχρησιμοποιήθηκε",
    "Fusion in progress…": "Σύντηξη σε εξέλιξη…",
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Σύντηξη: f{first} → f{last}, αναφορά f{ref}, περιοχή {width} × {height} στο ({x}, {y}), ×{scale}, {method}",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} από {count} καρέ  ·  ×{scale}  ·  θόρυβος σ {ref:.1f} → {fused:.1f} μετά τη σύντηξη  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Η σύντηξη ολοκληρώθηκε: {summary}",
    "Excluded: {list}": "Εξαιρέθηκαν: {list}",
    "Fusion cancelled.": "Η σύντηξη ακυρώθηκε.",
    "Fusion cancelled by the user": "Η σύντηξη ακυρώθηκε από τον χρήστη",
    "Fusion failed: see the log.": "Η σύντηξη απέτυχε: δείτε το αρχείο καταγραφής.",
    "Fusion failed": "Η σύντηξη απέτυχε",
    "Fusion in progress": "Σύντηξη σε εξέλιξη",
    "The fusion is still running. Stop it and close?": "Η σύντηξη εκτελείται ακόμη. Διακοπή και κλείσιμο;",
    "Saving the result…": "Αποθήκευση του αποτελέσματος…",
    "Saved in «{folder}».": "Αποθηκεύτηκε στο «{folder}».",
    "Saved in {folder}": "Αποθηκεύτηκε στο {folder}",
    "Result, comparison images and report saved in {folder}":
        "Αποτέλεσμα, εικόνες σύγκρισης και έκθεση αποθηκεύτηκαν στο {folder}",

    # messaggi dei passaggi (fusion.py)
    "{done} / {total} frames decoded": "{done} / {total} καρέ αποκωδικοποιημένα",
    "{count} frames decoded": "{count} καρέ αποκωδικοποιημένα",
    "The video ended before the reference frame.": "Το βίντεο τελείωσε πριν από το καρέ αναφοράς.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Αναζήτηση θέματος σε καρέ σμικρυμένα στο {percent:.0f} % (όριο μνήμης).",
    "searching the subject: {done} / {total}": "αναζήτηση θέματος: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Διατηρήθηκε ένα καρέ ανά {stride} (όριο μνήμης για μεγάλες περιοχές).",
    "{done} / {total} frames read at full resolution": "{done} / {total} καρέ αναγνωσμένα σε πλήρη ανάλυση",
    "The reference frame could not be read.": "Δεν ήταν δυνατή η ανάγνωση του καρέ αναφοράς.",
    "subject found in {found} / {total} frames": "θέμα που βρέθηκε σε {found} / {total} καρέ",
    "{done} / {total} frames aligned": "{done} / {total} καρέ ευθυγραμμισμένα",
    "motion model: {model}": "μοντέλο κίνησης: {model}",
    "{done} / {total} frames registered": "{done} / {total} καρέ συνταυτισμένα",
    "{count} frames registered": "{count} καρέ συνταυτισμένα",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} καρέ ευθυγραμμίστηκαν με απλούστερο μοντέλο κίνησης, επειδή το επιλεγμένο δεν συνέκλινε "
        "σε αυτά.",
    "{count} frames selected": "{count} καρέ επιλεγμένα",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Μόνο {count} αξιοποιήσιμα καρέ: το αποτέλεσμα μπορεί να είναι μόνο ελαφρώς καλύτερο από την αναφορά. "
        "Διευρύνετε το εύρος ή χαμηλώστε το κατώφλι ποιότητας.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Η μεγέθυνση μειώθηκε από ×{asked} σε ×{used}: η περιοχή είναι πολύ μεγάλη.",
    "resampling on the fine grid: {percent:.0f} %": "επαναδειγματοληψία στο λεπτό πλέγμα: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "μετατόπιση και άθροιση: {done} / {total} καρέ",
    "{count} frames fused on a ×{scale} grid": "{count} καρέ συντηγμένα σε πλέγμα ×{scale}",
    "noise reduction ({level})": "μείωση θορύβου ({level})",
    "deconvolution: iteration {n} / {total}": "αποσυνέλιξη: επανάληψη {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} επαναλήψεις",
    "no deconvolution": "χωρίς αποσυνέλιξη",
    "{width} × {height} pixels": "{width} × {height} pixel",

    # motivi di esclusione di un fotogramma
    "subject not found": "το θέμα δεν βρέθηκε",
    "not sampled (memory limit)": "δεν δειγματοληπτήθηκε (όριο μνήμης)",
    "frame not decoded": "καρέ μη αποκωδικοποιημένο",
    "alignment failed": "αποτυχία ευθυγράμμισης",
    "sub-pixel registration failed": "αποτυχία συνταύτισης υπο-pixel",
    "low alignment quality": "χαμηλή ποιότητα ευθυγράμμισης",
    "less sharp than the selected ones": "λιγότερο ευκρινές από τα επιλεγμένα",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Πηγή",
    "Open video…": "Άνοιγμα βίντεο…",
    "Duration": "Διάρκεια",
    "Frames": "Καρέ",
    "Resolution": "Ανάλυση",
    "Codec": "Codec",
    "  (rotated {degrees}°)": "  (περιστραμμένο {degrees}°)",
    "Open video": "Άνοιγμα βίντεο",
    "Videos": "Βίντεο",
    "All files": "Όλα τα αρχεία",
    "Reading {name}…": "Ανάγνωση του {name}…",
    "Cannot open the video": "Δεν είναι δυνατό το άνοιγμα του βίντεο",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} καρέ, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Άνοιξε το {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Output": "Έξοδος",
    "Destination folder": "Φάκελος προορισμού",
    "Subfolder named after the video": "Υποφάκελος με το όνομα του βίντεο",
    "Browse…": "Περιήγηση…",
    "Format": "Μορφή",
    "Color depth": "Βάθος χρώματος",
    "Also save every aligned frame (aligned/ folder)": "Αποθήκευση και κάθε ευθυγραμμισμένου καρέ (φάκελος aligned/)",
    "next to the video": "δίπλα στο βίντεο",
    ", in a subfolder named after it": ", σε υποφάκελο με το όνομά του",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Κάθε αποθηκευμένη σύντηξη αποκτά δικό της φάκελο ({where}) με το result.{ext}, τη σύντηξη πριν από την "
        "αποκατάσταση, το καρέ αναφοράς για σύγκριση, report.txt, report.pdf και report.json (παράμετροι, "
        "βήματα, καρέ που χρησιμοποιήθηκαν, SHA-256). Εικόνες με {bits} bit ανά κανάλι.",
    "Language": "Γλώσσα",
    "Interface language. The change is immediate and is saved for the next start.":
        "Γλώσσα της διεπαφής. Η αλλαγή είναι άμεση και αποθηκεύεται για την επόμενη εκκίνηση.",
    "Credits": "Συντελεστές",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Ελεύθερο λογισμικό υπό την GNU GPL v3 με απόδοση στον δημιουργό: δείτε τα αρχεία LICENSE και NOTICE. Η "
        "αποκωδικοποίηση βίντεο γίνεται από το FFmpeg, ξεχωριστό πρόγραμμα με δική του άδεια· η επεξεργασία "
        "εικόνας με OpenCV και NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (χωρίς απώλειες)",
    "Saving frame {frame}…": "Αποθήκευση του καρέ {frame}…",
    "Saved {path}": "Αποθηκεύτηκε το {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Το καρέ f{frame} αποθηκεύτηκε στο {path} ({pix_fmt})",
    "Save failed": "Η αποθήκευση απέτυχε",
    "The folder does not exist yet.": "Ο φάκελος δεν υπάρχει ακόμη.",
    "Cannot open the folder": "Δεν είναι δυνατό το άνοιγμα του φακέλου",
    "Open a video first.": "Ανοίξτε πρώτα ένα βίντεο.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "Δεν είναι δυνατή η κωδικοποίηση του {name}.",
    "Writing the images…": "Εγγραφή των εικόνων…",
    "Writing the PDF report…": "Εγγραφή της έκθεσης PDF…",
    "page {page} of {pages}": "σελίδα {page} από {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Αναφορά f{frame}  ·  δικυβική ×{scale}",
    "Result  ·  {count} frames": "Αποτέλεσμα  ·  {count} καρέ",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Φάντασμα  ·  {count} καρέ, το καθένα στη θέση όπου βρέθηκε",
    "Fusion before restoration": "Σύντηξη πριν από την αποκατάσταση",
    "Writing the aligned frames: {done} / {total}": "Εγγραφή των ευθυγραμμισμένων καρέ: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Υπολογισμός των αποτυπωμάτων SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — έκθεση σύντηξης πολλαπλών καρέ",
    "Created: {when}": "Δημιουργήθηκε: {when}",
    "File": "Αρχείο",
    "Size": "Μέγεθος",
    "{size} bytes": "{size} byte",
    "Video": "Βίντεο",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Range and subject": "Εύρος και θέμα",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} καρέ, {start} → {end})",
    "Subject area on the reference frame": "Περιοχή θέματος στο καρέ αναφοράς",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} pixel",
    "Parameters": "Παράμετροι",
    "yes": "ναι",
    "no": "όχι",
    "Deconvolution": "Αποσυνέλιξη",
    "{iterations} Richardson-Lucy iterations": "{iterations} επαναλήψεις Richardson-Lucy",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px της εξόδου ({mode})",
    "automatic: measured on the edges of the fused image": "αυτόματο: μετρημένο στις ακμές της συντηγμένης εικόνας",
    "manual": "χειροκίνητο",
    "Steps": "Βήματα",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} καρέ αποκωδικοποιημένα από το FFmpeg, με ακρίβεια καρέ· {scale}.",
    "subject search at full resolution": "αναζήτηση θέματος σε πλήρη ανάλυση",
    "subject search at {percent:.0f} % of the resolution": "αναζήτηση θέματος στο {percent:.0f} % της ανάλυσης",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Το θέμα παρακολουθήθηκε από το καρέ αναφοράς προς τα εμπρός και προς τα πίσω με κανονικοποιημένη "
        "ετεροσυσχέτιση (OpenCV matchTemplate, TM_CCOEFF_NORMED)· βρέθηκε σε {found} / {count} καρέ, που "
        "περικόπηκαν σε πλήρη ανάλυση γύρω από αυτό.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Χονδρική ευθυγράμμιση κάθε καρέ με την αναφορά μέσω του αλγορίθμου ECC (Evangelidis & Psarakis, "
        "2008), μοντέλο: {model}, σε εξομαλυμένες εικόνες.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC εκλεπτυσμένο σε πλήρη ανάλυση (ακρίβεια υπο-pixel): {registered} καρέ συνταυτισμένα. Επιλογή: "
        "ECC ≥ {quality:.2f}, το ευκρινέστερο {keep} % (ενέργεια λαπλασιανής): {used} καρέ χρησιμοποιήθηκαν.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: καρέ επαναδειγματοληπτημένα σε πλέγμα ×{scale} της αναφοράς (Lanczos), σταθμισμένα κατά την "
        "ποιότητα ευθυγράμμισης{sharp}{equal}.",
    " and sharpness": " και την ευκρίνεια",
    ", brightness equalized to the reference": ", φωτεινότητα εξισωμένη με την αναφορά",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Μόνο στη λαμπρότητα (το χρώμα εξομαλύνεται: στο συμπιεσμένο βίντεο μεταφέρει θόρυβο, όχι "
        "λεπτομέρεια). Μείωση θορύβου: {denoise}. Αποσυνέλιξη: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Πρώτα αυτόματα επίπεδα: λαμπρότητα {black:.3f} → 0, {white:.3f} → 1, ίδια ευθεία σε κάθε κανάλι",
    "No auto levels": "Χωρίς αυτόματα επίπεδα",
    " (bilateral filter)": " (διμερές φίλτρο)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, γκαουσιανή PSF σ {sigma:.2f} px, {iterations} επαναλήψεις, ομαλοποίηση ολικής "
        "κύμανσης {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Παρουσίαση: τοπική αντίθεση {clahe}· {gray}. Ενιαίο καρέ {width} × {height} pixel.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, όριο αποκοπής {clip:g})",
    "grayscale": "κλίμακα του γκρι",
    "color": "έγχρωμο",
    "Result": "Αποτέλεσμα",
    "Frames used": "Καρέ που χρησιμοποιήθηκαν",
    "{used} of {count}": "{used} από {count}",
    "Estimated noise σ": "Εκτιμώμενο σ θορύβου",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Μέθοδος Immerkær, 0-255, στην ανάλυση του βίντεο: αναφορά {ref:.2f} → σύντηξη {fused:.2f} → τελικό "
        "{final:.2f}. Η αποσυνέλιξη ενισχύει μαζί τη λεπτή λεπτομέρεια και τον θόρυβο, οπότε η τελευταία τιμή "
        "δεν είναι μέτρο μόνο του θορύβου.",
    "Samples per output pixel": "Δείγματα ανά pixel εξόδου",
    "Sub-pixel phases covered (4 × 4 grid)": "Φάσεις υπο-pixel που καλύφθηκαν (πλέγμα 4 × 4)",
    "frame": "καρέ",
    "time": "χρόνος",
    "search": "αναζήτ.",
    "sharp.": "ευκρίν.",
    "weight": "βάρος",
    "used": "χρήση",
    "model": "μοντέλο",
    "note": "σημείωση",
    "(reference)": "(αναφορά)",
    "Files": "Αρχεία",
    "aligned/: {count} aligned frames": "aligned/: {count} ευθυγραμμισμένα καρέ",
    "Note": "Σημείωση",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Το αποτέλεσμα είναι βελτίωση των καρέ που αναφέρονται παραπάνω: συνδυάζει πληροφορίες που υπάρχουν "
        "σε αυτά και δεν προσθέτει λεπτομέρειες. Οι λεπτές λεπτομέρειες στο όριο της ανάλυσης, και οι "
        "χαρακτήρες που μοιάζουν μεταξύ τους, πρέπει να ελέγχονται στα αρχικά καρέ πριν από την εξαγωγή "
        "συμπερασμάτων.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Λογισμικό: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Έτοιμο.",
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  σελίδα   ·   ← →  καρέ   ·   I / O  εύρος   ·   F5  σύντηξη   ·   Ctrl+S  αποθήκευση",
    "ffmpeg missing": "λείπει το ffmpeg",
    "Operation failed": "Η λειτουργία απέτυχε",
    "ERROR - {title}: {message}": "ΣΦΑΛΜΑ - {title}: {message}",
    "Error: {title}": "Σφάλμα: {title}",
    "INTERNAL ERROR": "ΕΣΩΤΕΡΙΚΟ ΣΦΑΛΜΑ",
    "Internal error: details in the log.": "Εσωτερικό σφάλμα: λεπτομέρειες στο αρχείο καταγραφής.",
}
