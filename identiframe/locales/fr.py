# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Français : traduction des textes de l'interface et du rapport.

La clé est le texte anglais tel qu'il apparaît dans le code (dans tr() et N_()),
la valeur sa traduction. Les espaces réservés entre accolades restent identiques.
Les clés non traduites restent en anglais. Après chaque modification :

    .venv\\Scripts\\python.exe scripts\\check_i18n.py
"""

from __future__ import annotations

NAME = "Français"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Impossible de démarrer l'interface : {error}\n\n"
        "Installez les dépendances avec :\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg introuvable. Téléchargez-le depuis le cadre FFmpeg de la page Configuration, "
        "ou installez-le et placez-le dans le PATH.",
    "Cannot check the latest ffmpeg version: {error}": "Impossible de vérifier la dernière version de ffmpeg : {error}",
    "Unexpected answer from the ffmpeg download site.": "Réponse inattendue du site de téléchargement de ffmpeg.",
    "Downloading {label}": "Téléchargement de {label}",
    "Download of {label} failed: {error}": "Échec du téléchargement de {label} : {error}",
    "Invalid archive: suspicious path '{member}'.": "Archive non valide : chemin suspect '{member}'.",
    "The downloaded file is not a valid zip archive.": "Le fichier téléchargé n'est pas une archive zip valide.",
    "The downloaded package does not contain {name}.": "Le paquet téléchargé ne contient pas {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Impossible de mettre à jour '{name}' : fichiers en cours d'utilisation. Attendez la fin de la fusion "
        "en cours et réessayez.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Le téléchargement automatique n'est disponible que sous Windows : installez ffmpeg avec le "
        "gestionnaire de paquets du système.",
    "Extracting ffmpeg": "Extraction de ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "Le ffmpeg téléchargé ne fonctionne pas sur ce PC.",
    "{name} is missing after extraction.": "{name} manque après l'extraction.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Vérification…",
    "Check": "Vérifier",
    "Check for updates": "Rechercher des mises à jour",
    "Download / Update": "Télécharger / Mettre à jour",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg est un programme séparé (LGPL/GPL). Le téléchargement prend la version officielle pour "
        "Windows depuis {url} et ne garde que ffmpeg.exe, LICENSE et README dans le dossier tools\\ffmpeg "
        "à côté du programme : aucune installation, aucune modification du PATH.",
    "ffmpeg check failed": "Échec de la vérification de ffmpeg",
    "tools folder": "dossier tools",
    "system PATH": "PATH du système",
    "Python package": "paquet Python",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Moteur : ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Manquant : téléchargez-le avec le bouton de droite.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg introuvable : téléchargez-le depuis le cadre FFmpeg de la page Configuration.",
    "ffmpeg missing: download it from the FFmpeg box.": "ffmpeg manquant : téléchargez-le depuis le cadre FFmpeg.",
    "Checking the latest ffmpeg version…": "Vérification de la dernière version de ffmpeg…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} est à jour.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Dernière version : {latest}. Installée : {installed}. La télécharger maintenant ?",
    "Update check failed": "Échec de la recherche de mises à jour",
    "Wait for the running fusion, then try again.": "Attendez la fin de la fusion en cours, puis réessayez.",
    "Downloading ffmpeg…": "Téléchargement de ffmpeg…",
    "Downloading ffmpeg from {url}": "Téléchargement de ffmpeg depuis {url}",
    "ffmpeg downloaded into {path}": "ffmpeg téléchargé dans {path}",
    "Download cancelled.": "Téléchargement annulé.",
    "ffmpeg download failed": "Échec du téléchargement de ffmpeg",
    "ffmpeg: exit code {code}": "ffmpeg : code de sortie {code}",
    "File not found: {path}": "Fichier introuvable : {path}",
    "The file has no recognizable video track.": "Le fichier ne contient aucune piste vidéo reconnaissable.",
    "Video size not recognized.": "Dimensions de la vidéo non reconnues.",
    "Frame rate not recognized.": "Fréquence d'images non reconnue.",
    "Invalid frame rate.": "Fréquence d'images non valide.",
    "Unknown video duration (stream or damaged file).":
        "Durée de la vidéo inconnue (flux ou fichier endommagé).",
    "Zero video duration.": "Durée de la vidéo nulle.",
    "No frame at {seconds:.3f} s.": "Aucune image à l'instant {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg n'a pas écrit le fichier.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "CONFIRMATION",
    "WARNING": "ATTENTION",
    "ERROR": "ERREUR",
    "Yes": "Oui",

    # ----------------------------------------------------------- navigazione
    "PAGES": "PAGES",
    "Configuration": "Configuration",
    "Subject": "Sujet",
    "Frames, subject and reference": "Images, sujet et référence",
    "Fusion": "Fusion",
    "Multi-frame fusion and result": "Fusion multi-images et résultat",
    "{app}  /  PAGE {index:02d}": "{app}  /  PAGE {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "aucune",
    "Open video… (Ctrl+O)": "Ouvrir une vidéo… (Ctrl+O)",
    "No video": "Aucune vidéo",
    "Reading…": "Lecture…",
    "Ready": "Prêt",
    "Error": "Erreur",
    "Fusing…": "Fusion…",
    "Fused": "Fusionné",

    # ------------------------------------------------------------- anteprima
    "Preview": "Aperçu",
    "Open a video to see the preview": "Ouvrez une vidéo pour voir l'aperçu",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "glisser-droit : zone du sujet  ·  molette : zoom  ·  glisser : déplacer  ·  double-clic : ajuster",
    "First frame (Home)": "Première image (Début)",
    "Back 10 frames (Shift+←)": "Reculer de 10 images (Maj+←)",
    "Previous frame (←)": "Image précédente (←)",
    "Next frame (→)": "Image suivante (→)",
    "Forward 10 frames (Shift+→)": "Avancer de 10 images (Maj+→)",
    "Last frame (End)": "Dernière image (Fin)",
    "Save frame": "Enregistrer l'image",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Enregistrer l'image affichée en pleine résolution, sans perte (Ctrl+S)",
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Aperçu plus grand : masque la chronologie, les touches I / O restent actives (F11)",
    "Preview unavailable: {error}": "Aperçu indisponible : {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+molette : zoom  ·  molette : défiler  ·  glisser I / O et le curseur  ·  double-clic sur la règle : tout",
    "In  [I]": "Entrée  [I]",
    "Out  [O]": "Sortie  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Place le début de la sélection au curseur (touche I)",
    "Sets the end of the selection at the cursor (key O)":
        "Place la fin de la sélection au curseur (touche O)",
    "Moves the cursor to the start of the selection": "Amène le curseur au début de la sélection",
    "Moves the cursor to the end of the selection": "Amène le curseur à la fin de la sélection",
    "CURSOR": "CURSEUR",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Temps (1:23.456, 83.4) ou image (f2000), puis Entrée",
    "Zoom out (−)": "Zoom arrière (−)",
    "Zoom in (+)": "Zoom avant (+)",
    "All": "Tout",
    "Selection": "Sélection",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Sélection : f{first} → f{last}  ·  {count} images  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Vue : {start} → {end}  ({seconds:.3f} s, {frames:.1f} images)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Temps non reconnu : utilisez mm:ss.mmm, des secondes ou f<numéro>.",
    "Open a video to see the timeline": "Ouvrez une vidéo pour voir la chronologie",

    # -------------------------------------------------------------- soggetto
    "Select area": "Sélectionner la zone",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Puis glissez sur l'aperçu pour cadrer le sujet (ou glisser-droit à tout moment) ; "
        "la fusion démarre d'elle-même",
    "Moves the cursor to the reference frame": "Amène le curseur sur l'image de référence",
    "Clear": "Effacer",
    "Fuse frames  →": "Fusionner les images  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Lance la fusion multi-images sur la plage sélectionnée (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Cadrez le sujet sur une image nette : cette image devient la référence et la fusion démarre.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Glissez sur l'aperçu pour cadrer le sujet (Échap pour arrêter).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "La zone du sujet est trop petite : dessinez-en une d'au moins {size} × {size} pixels.",
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Plage réduite aux images où le sujet a été suivi : f{first} → f{last}.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Plage définie autour de la référence : f{first} → f{last}. Déplacez I / O pour la modifier.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Zone du sujet {width} × {height} en ({x}, {y}) sur l'image de référence f{frame}",
    "Subject area cleared.": "Zone du sujet effacée.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "La référence f{frame} est hors de la plage f{first} → f{last} : déplacez I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} images dans la plage : sélectionnez-en au plus {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Zone {width} × {height} px en ({x}, {y})  ·  référence f{frame}  ·  {count} images f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Sélectionnez d'abord la zone du sujet (plaque, visage, objet) sur une image nette : glisser-droit "
        "sur l'aperçu, ou utilisez Sélectionner la zone.",
    "The reference frame must be inside the selected range.":
        "L'image de référence doit se trouver dans la plage sélectionnée.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "La plage contient {count} images : sélectionnez-en au plus {limit} autour de la référence.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Images et alignement",
    "Motion model": "Modèle de mouvement",
    "Translation": "Translation",
    "Rotation + translation": "Rotation + translation",
    "Affine": "Affine",
    "Perspective (homography)": "Perspective (homographie)",
    "Subject search: minimum correlation": "Recherche du sujet : corrélation minimale",
    "Minimum alignment quality (ECC)": "Qualité minimale de l'alignement (ECC)",
    "Sharpest frames kept": "Images les plus nettes conservées",
    "Scale": "Agrandissement",
    "Fusion method": "Méthode de fusion",
    "Robust mean (outliers rejected)": "Moyenne robuste (valeurs aberrantes rejetées)",
    "Shift-and-add (normalized convolution)": "Décalage et addition (convolution normalisée)",
    "Median": "Médiane",
    "Weight by sharpness": "Pondérer par la netteté",
    "Equalize brightness": "Égaliser la luminosité",
    "Restoration": "Restauration",
    "Noise reduction": "Réduction du bruit",
    "Off": "Désactivé",
    "Light": "Faible",
    "Medium": "Moyen",
    "Strong": "Fort",
    "Deconvolution iterations": "Itérations de déconvolution",
    "0 (none)": "0 (aucune)",
    "not applied": "non appliquée",
    "PSF σ (output pixels)": "PSF σ (pixels de sortie)",
    "Automatic": "Automatique",
    "Regularization (total variation)": "Régularisation (variation totale)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Plus d'itérations accentuent la netteté mais amplifient aussi le bruit et les halos ; la régularisation "
        "retient le bruit. Changez peu à la fois et comparez.",
    "Presentation": "Présentation",
    "Auto levels": "Niveaux automatiques",
    "Local contrast (CLAHE)": "Contraste local (CLAHE)",
    "Grayscale": "Niveaux de gris",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Les niveaux sont une droite appliquée avant la déconvolution (noir et blanc aux centiles 0,5 et "
        "99,5) ; le contraste local, une égalisation par zones. Tout est écrit dans le rapport.",
    "Defaults": "Par défaut",
    "Puts every parameter of the pipeline back to its default value":
        "Remet chaque paramètre du pipeline à sa valeur par défaut",
    "Parameters back to their defaults.": "Paramètres remis à leurs valeurs par défaut.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Réglages enregistrés",
    "(none saved)": "(aucun enregistré)",
    "Save…": "Enregistrer…",
    "Saves the current parameters under a name (in config.json)":
        "Enregistre les paramètres actuels sous un nom (dans config.json)",
    "Delete": "Supprimer",
    "From report…": "Depuis un rapport…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Charge les paramètres écrits dans le report.json d'une fusion enregistrée",
    "Save settings": "Enregistrer les réglages",
    "Name of these settings:": "Nom de ces réglages :",
    "Settings «{name}» already exist. Replace them?": "Les réglages « {name} » existent déjà. Les remplacer ?",
    "Settings «{name}» saved.": "Réglages « {name} » enregistrés.",
    "Settings «{name}» loaded.": "Réglages « {name} » chargés.",
    "Delete settings": "Supprimer les réglages",
    "Delete the settings «{name}»?": "Supprimer les réglages « {name} » ?",
    "Settings «{name}» deleted.": "Réglages « {name} » supprimés.",
    "Load parameters from a report": "Charger les paramètres depuis un rapport",
    "Cannot read the report": "Impossible de lire le rapport",
    "{name} is not an IdentiFrame report.": "{name} n'est pas un rapport IdentiFrame.",
    "Parameters loaded from {path}": "Paramètres chargés depuis {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Comparaison",
    "FRAMES": "IMAGES",
    "RESULT": "RÉSULTAT",
    "Ghost of the frames": "Fantôme des images",
    "Reference frame": "Image de référence",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "FANTÔME  ·  {count} IMAGES  ·  ×{scale}",
    "Final": "Final",
    "Fusion only": "Fusion seule",
    "Draw the subject area on the Subject page, then run the fusion":
        "Dessinez la zone du sujet sur la page Sujet, puis lancez la fusion",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "molette : zoom  ·  glisser : déplacer  ·  double-clic : ajuster  ·  les deux vues bougent ensemble  ·  "
        "fantôme : chaque image utilisée, superposée à la position où elle a été trouvée",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "RÉFÉRENCE f{frame}  ·  BICUBIQUE ×{scale}",
    "RESULT  ·  {count} FRAMES": "RÉSULTAT  ·  {count} IMAGES",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Extraction des images",
    "Subject detection": "Détection du sujet",
    "Local alignment": "Alignement local",
    "Sub-pixel registration": "Recalage sous-pixel",
    "Multi-frame fusion": "Fusion multi-images",
    "Deconvolution and denoising": "Déconvolution et débruitage",
    "Single frame": "Image unique",
    "Save result": "Enregistrer le résultat",
    "Saves images and report in a new folder (Ctrl+S)":
        "Enregistre les images et le rapport dans un nouveau dossier (Ctrl+S)",
    "Run fusion": "Lancer la fusion",
    "Runs the pipeline again with these parameters (F5)": "Relance le pipeline avec ces paramètres (F5)",
    "Open folder": "Ouvrir le dossier",
    "Cancel": "Annuler",
    "reused": "réutilisé",
    "Fusion in progress…": "Fusion en cours…",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} images sur {count}  ·  ×{scale}  ·  bruit σ {ref:.1f} → {fused:.1f} après la fusion  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fusion terminée : {summary}",
    "Excluded: {list}": "Exclues : {list}",
    "Fusion cancelled.": "Fusion annulée.",
    "Fusion cancelled by the user": "Fusion annulée par l'utilisateur",
    "Fusion failed: see the log.": "Échec de la fusion : voir le journal.",
    "Fusion failed": "Échec de la fusion",
    "Fusion in progress": "Fusion en cours",
    "The fusion is still running. Stop it and close?": "La fusion est encore en cours. L'interrompre et fermer ?",
    "Saving the result…": "Enregistrement du résultat…",
    "Saved in «{folder}».": "Enregistré dans « {folder} ».",
    "Saved in {folder}": "Enregistré dans {folder}",
    "Result, comparison images and report saved in {folder}":
        "Résultat, images de comparaison et rapport enregistrés dans {folder}",

    # messaggi dei passaggi (fusion.py)
    "{count} frames decoded": "{count} images décodées",
    "The video ended before the reference frame.": "La vidéo se termine avant l'image de référence.",
    "Range set with I / O": "Plage définie avec I / O",
    "Frames examined":
        "Images examinées",
    "Frames that make up the result":
        "Images qui composent le résultat",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "{count} images exclues car elles viennent après plus de {seconds:g} s sans bon alignement : à partir de là, le sujet n'est plus confirmé (masqué, trop petit ou hors du cadre).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Sujet suivi de f{first} à f{last} : au-delà, il est absent ou non confirmé pendant plus de {seconds:g} s.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Recherche du sujet sur des images réduites à {percent:.0f} % (limite de mémoire).",
    "searching the subject: {done} / {total}": "recherche du sujet : {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Une image sur {stride} conservée (limite de mémoire pour les grandes zones).",
    "{done} / {total} frames read at full resolution": "{done} / {total} images lues en pleine résolution",
    "The reference frame could not be read.": "Impossible de lire l'image de référence.",
    "subject found in {found} / {total} frames": "sujet trouvé dans {found} / {total} images",
    "{done} / {total} frames aligned": "{done} / {total} images alignées",
    "motion model: {model}": "modèle de mouvement : {model}",
    "{done} / {total} frames registered": "{done} / {total} images recalées",
    "{count} frames registered": "{count} images recalées",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} images alignées avec un modèle de mouvement plus simple, car celui choisi ne convergeait pas "
        "sur elles.",
    "{count} frames selected": "{count} images retenues",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Seulement {count} images utilisables : le résultat ne peut être que légèrement meilleur que la "
        "référence. Élargissez la plage ou abaissez le seuil de qualité.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Agrandissement réduit de ×{asked} à ×{used} : la zone est trop grande.",
    "resampling on the fine grid: {percent:.0f} %": "rééchantillonnage sur la grille fine : {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "décalage et addition : {done} / {total} images",
    "{count} frames fused on a ×{scale} grid": "{count} images fusionnées sur une grille ×{scale}",
    "noise reduction ({level})": "réduction du bruit ({level})",
    "deconvolution: iteration {n} / {total}": "déconvolution : itération {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} itérations",
    "no deconvolution": "pas de déconvolution",
    "{width} × {height} pixels": "{width} × {height} pixels",

    # motivi di esclusione di un fotogramma
    "subject not found": "sujet non trouvé",
    "not sampled (memory limit)": "non échantillonnée (limite de mémoire)",
    "frame not decoded": "image non décodée",
    "alignment failed": "échec de l'alignement",
    "sub-pixel registration failed": "échec du recalage sous-pixel",
    "low alignment quality": "alignement peu fiable",
    "less sharp than the selected ones": "moins nette que les images retenues",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Source",
    "Open video…": "Ouvrir une vidéo…",
    "Duration": "Durée",
    "Frames": "Images",
    "Resolution": "Résolution",
    "Codec": "Codec",
    "  (rotated {degrees}°)": "  (pivotée de {degrees}°)",
    "Open video": "Ouvrir une vidéo",
    "Videos": "Vidéos",
    "All files": "Tous les fichiers",
    "Reading {name}…": "Lecture de {name}…",
    "Cannot open the video": "Impossible d'ouvrir la vidéo",
    "{name}: {frames} frames, {duration}.": "{name} : {frames} images, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Ouvert {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bits), {duration}",
    "Output": "Sortie",
    "Destination folder": "Dossier de destination",
    "Subfolder named after the video": "Sous-dossier au nom de la vidéo",
    "Browse…": "Parcourir…",
    "Format": "Format",
    "Color depth": "Profondeur de couleur",
    "Also save every aligned frame (aligned/ folder)": "Enregistrer aussi chaque image alignée (dossier aligned/)",
    "next to the video": "à côté de la vidéo",
    ", in a subfolder named after it": ", dans un sous-dossier à son nom",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Chaque fusion enregistrée a son propre dossier ({where}) avec result.{ext}, la fusion avant "
        "restauration, l'image de référence pour la comparaison, report.txt, report.pdf et report.json "
        "(paramètres, étapes, images utilisées, SHA-256). Images à {bits} bits par canal.",
    "Language": "Langue",
    "Interface language. The change is immediate and is saved for the next start.":
        "Langue de l'interface. Le changement est immédiat et sera conservé au prochain démarrage.",
    "Credits": "Crédits",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Logiciel libre sous GNU GPL v3 avec attribution de l'auteur : voir les fichiers LICENSE et NOTICE. "
        "Décodage vidéo par FFmpeg, programme séparé sous sa propre licence ; traitement des images avec "
        "OpenCV et NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (sans perte)",
    "Saving frame {frame}…": "Enregistrement de l'image {frame}…",
    "Saved {path}": "Enregistré {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Image f{frame} enregistrée dans {path} ({pix_fmt})",
    "Save failed": "Échec de l'enregistrement",
    "The folder does not exist yet.": "Le dossier n'existe pas encore.",
    "Cannot open the folder": "Impossible d'ouvrir le dossier",
    "Open a video first.": "Ouvrez d'abord une vidéo.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "Impossible d'encoder {name}.",
    "Writing the images…": "Écriture des images…",
    "Writing the PDF report…": "Écriture du rapport PDF…",
    "page {page} of {pages}": "page {page} sur {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Référence f{frame}  ·  bicubique ×{scale}",
    "Result  ·  {count} frames": "Résultat  ·  {count} images",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Fantôme  ·  {count} images, chacune à la position où elle a été trouvée",
    "Fusion before restoration": "Fusion avant restauration",
    "Writing the aligned frames: {done} / {total}": "Écriture des images alignées : {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Calcul des empreintes SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — rapport de fusion multi-images",
    "Created: {when}": "Créé le : {when}",
    "File": "Fichier",
    "Size": "Taille",
    "{size} bytes": "{size} octets",
    "Video": "Vidéo",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bits), {duration}",
    "Range and subject": "Plage et sujet",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} images, {start} → {end})",
    "Subject area on the reference frame": "Zone du sujet sur l'image de référence",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} pixels",
    "Parameters": "Paramètres",
    "yes": "oui",
    "no": "non",
    "Deconvolution": "Déconvolution",
    "{iterations} Richardson-Lucy iterations": "{iterations} itérations de Richardson-Lucy",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px de la sortie ({mode})",
    "automatic: measured on the edges of the fused image": "automatique : mesurée sur les contours de l'image fusionnée",
    "manual": "manuelle",
    "Steps": "Étapes",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} images décodées par FFmpeg, à l'image près ; {scale}.",
    "subject search at full resolution": "recherche du sujet en pleine résolution",
    "subject search at {percent:.0f} % of the resolution": "recherche du sujet à {percent:.0f} % de la résolution",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Sujet suivi depuis l'image de référence vers l'avant et vers l'arrière par corrélation croisée "
        "normalisée (OpenCV matchTemplate, TM_CCOEFF_NORMED) ; trouvé dans {found} / {count} images, "
        "recadrées en pleine résolution autour de lui.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Alignement grossier de chaque image sur la référence avec l'algorithme ECC (Evangelidis & "
        "Psarakis, 2008), modèle : {model}, sur des images lissées.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC affiné en pleine résolution (précision sous-pixel) : {registered} images recalées. "
        "Sélection : ECC ≥ {quality:.2f}, les {keep} % les plus nettes (énergie du laplacien) : {used} images utilisées.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method} : images rééchantillonnées sur une grille ×{scale} de la référence (Lanczos), pondérées par "
        "la qualité d'alignement{sharp}{equal}.",
    " and sharpness": " et la netteté",
    ", brightness equalized to the reference": ", luminosité égalisée sur la référence",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Sur la luminance seule (la couleur est lissée : dans une vidéo compressée, elle porte du "
        "bruit, pas du détail). Réduction du bruit : {denoise}. Déconvolution : {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Niveaux automatiques d'abord : luminance {black:.3f} → 0, {white:.3f} → 1, même droite sur chaque canal",
    "No auto levels": "Sans niveaux automatiques",
    " (bilateral filter)": " (filtre bilatéral)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, PSF gaussienne σ {sigma:.2f} px, {iterations} itérations, régularisation par "
        "variation totale {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Présentation : contraste local {clahe} ; {gray}. Image unique de {width} × {height} pixels.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, limite d'écrêtage {clip:g})",
    "grayscale": "en niveaux de gris",
    "color": "en couleur",
    "Result": "Résultat",
    "Frames used": "Images utilisées",
    "{used} of {count}": "{used} sur {count}",
    "Estimated noise σ": "Bruit σ estimé",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Méthode d'Immerkær, 0-255, à la résolution de la vidéo : référence {ref:.2f} → fusion {fused:.2f} → "
        "final {final:.2f}. La déconvolution rehausse ensemble les détails fins et le bruit : la dernière "
        "valeur ne mesure pas que le bruit.",
    "Samples per output pixel": "Échantillons par pixel de sortie",
    "Sub-pixel phases covered (4 × 4 grid)": "Phases sous-pixel couvertes (grille 4 × 4)",
    "frame": "image",
    "time": "temps",
    "search": "recherche",
    "sharp.": "nett.",
    "weight": "poids",
    "used": "utilisée",
    "model": "modèle",
    "note": "note",
    "(reference)": "(référence)",
    "Files": "Fichiers",
    "aligned/: {count} aligned frames": "aligned/ : {count} images alignées",
    "Note": "Note",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Le résultat est une amélioration des images listées ci-dessus : il combine des informations qui y "
        "sont présentes et n'ajoute aucun détail. Les détails fins à la limite de la résolution, et les "
        "caractères qui se ressemblent, doivent être vérifiés sur les images sources avant d'en tirer des "
        "conclusions.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Logiciel : {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Prêt.",
    "ffmpeg missing": "ffmpeg manquant",
    "Operation failed": "Échec de l'opération",
    "ERROR - {title}: {message}": "ERREUR - {title} : {message}",
    "Error: {title}": "Erreur : {title}",
    "INTERNAL ERROR": "ERREUR INTERNE",
    "Internal error: details in the log.": "Erreur interne : détails dans le journal.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Type de sujet",
    "Parameters set for the subject type: {subject}.": "Paramètres réglés pour le type de sujet : {subject}.",
    "Face": "Visage",
    "pose or expression differs from the reference": "pose ou expression différente de la référence",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Visage : affinement local non rigide après ECC sur {count} images, déplacement moyen {residual:.2f} px de la vidéo.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Visage : la zone est trop petite pour l'affinement local ({size} px au moins) : alignement rigide seulement.",
    "simil.": "simil.",
    "Local refinement (face)": "Affinement local (visage)",
    "not applied: area too small, rigid alignment only": "non appliqué : zone trop petite, alignement rigide seulement",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Visage : la zone du sujet mesure {width} × {height} pixels dans la vidéo. La fusion combine les images dont la pose et l'expression correspondent à la référence et donne moins de poids aux parties qui diffèrent ; elle ne peut pas créer des traits qu'aucune image ne montre. Avec un visage de moins de 60 pixels de large environ, le résultat peut améliorer l'aspect général mais pas révéler des traits identifiants : comparez-le à l'image de référence et aux images isolées avant toute conclusion sur l'identité.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Visage : après le modèle rigide, un affinement local non rigide (flux optique de Farneback entre la référence et l'image alignée, lissé et limité en amplitude) suit l'expression et les mouvements de la tête ; une confiance par pixel (cohérence aller-retour et corrélation locale) pondère chaque échantillon dans la fusion. Les images dont la similarité locale avec la référence est inférieure à {limit:.2f} sont écartées (pose ou expression changée).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} images affinées ; similarité locale moyenne avec la référence {similarity:.2f}, déplacement local moyen {displacement:.2f} px de la vidéo ; {excluded} images écartées pour une pose ou une expression différente.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fusion : {subject}, f{first} → f{last}, référence f{ref}, zone {width} × {height} en ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Ctrl+1/2/3  page   ·   ← →  image   ·   Espace  lecture   ·   I / O  plage   ·   F5  fusionner   ·   Ctrl+S  enregistrer",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} images alignées avec un modèle de mouvement plus simple, parce que celui choisi donnait une déformation invraisemblable (échelle, cisaillement ou perspective au-delà des limites).",
    "persp.": "persp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Visage : les échantillons hors de l'ellipse inscrite dans la zone comptent peu, et là le résultat montre l'image de référence : l'arrière-plan bouge différemment du visage.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Plaque et Texte : un alignement rigide par image ; les caractères sont lus avec fast-plate-ocr (plaques) ou PaddleOCR (textes, aussi sur plusieurs lignes). Visage : après l'alignement, un raffinement local non rigide suit l'expression et les mouvements de la tête, les images avec une pose différente sont écartées et la restauration est plus légère. Changer de type charge ses valeurs par défaut.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Lit la plaque (fast-plate-ocr) ou le texte (PaddleOCR) sur le résultat et sur des fusions indépendantes de groupes d'images, et vote caractère par caractère",
    "OCR models": "Modèles OCR",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "Les caractères sont lus par deux modèles exécutés par OpenCV, téléchargés à la demande dans tools\\ocr et jamais inclus dans le programme (environ 37 Mo) : fast-plate-ocr pour les plaques (MIT, de ankandrew) et PaddleOCR PP-OCRv6 pour les textes en de nombreuses langues (Apache 2.0, Baidu / PaddleOCR, conversion ONNX de RapidOCR). Chaque fichier est contrôlé avec son empreinte SHA-256 ; licences et provenance sont enregistrées à côté des modèles.",
    "Downloading the OCR models…": "Téléchargement des modèles OCR…",
    "Reading the characters…": "Lecture des caractères…",
    "OCR models download failed": "Échec du téléchargement des modèles OCR",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "Téléchargement des modèles OCR : {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Le modèle OCR pour ce type de sujet manque : téléchargez-le depuis le cadre Modèles OCR de la page Configuration.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "appuyez sur Lire les caractères (automatique pour les plaques et les textes quand les modèles OCR sont prêts)",
    "model confidence {confidence:.0f} %": "confiance du modèle {confidence:.0f} %",
    "OCR models check failed": "Échec du contrôle des modèles OCR",
    "OCR: {plate} (plates), {text} (texts)": "OCR : {plate} (plaques), {text} (textes)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Manquants (facultatifs, pour lire plaques et textes) : téléchargez-les avec le bouton à droite.",
    "OCR models ready: {path}": "Modèles OCR prêts : {path}",
    "possible country ({share:.0f} %)": "pays possible ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "pays possible : {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  plaques : {plate}  ·  textes : {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Le modèle pour les textes manque : téléchargez-le avec le bouton à droite.",
    "The model for plates is missing: download it with the button on the right.": "Le modèle pour les plaques manque : téléchargez-le avec le bouton à droite.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Texte, standard : perspective, 75 % les plus nettes, ×2, moyenne robuste, déconvolution modérée. Le point de départ.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Texte de nuit ou bruité : plus d'images, réduction du bruit moyenne, déconvolution plus douce avec régularisation forte, contraste local léger, niveaux de gris.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Texte lointain et petit filmé sur de nombreuses images : ×3, décalage et addition, presque toutes les images, seuil d'alignement plus bas.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Texte sur un véhicule en mouvement ou filmé par une caméra en mouvement, avec flou de bougé : seulement la moitié la plus nette des images, recherche du sujet plus tolérante, déconvolution plus forte.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Texte à l'ombre ou à contre-jour : contraste local moyen, niveaux de gris, réduction du bruit légère.",
    "Plate": "Plaque",
    "Text": "Texte",
    "No text line found inside the area: the whole area was read as one line.": "Aucune ligne de texte trouvée dans la zone : toute la zone a été lue comme une seule ligne.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "Aucun caractère trouvé : tracez la zone au plus près de la plaque ou du texte, et vérifiez l'agrandissement et la restauration.",
    "Cannot load the OCR model {name}: {error}": "Impossible de charger le modèle OCR {name} : {error}",
    "The OCR model configuration {name} is not valid.": "La configuration du modèle OCR {name} n'est pas valide.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Lecture automatique par un modèle OCR, à vérifier sur les images : des caractères de forme semblable (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) peuvent être mal lus de la même façon dans chaque lecture, et le vote ne peut pas le voir. Le pays possible de la plaque est une estimation du modèle d'après l'aspect de la plaque, pas une vérification.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), exécuté par {runtime} : on lit le résultat et {groups} fusions de groupes indépendants d'images, chacune restaurée avec les mêmes paramètres ; les lectures sont alignées et votées caractère par caractère, pondérées par la probabilité que le modèle donne à chaque caractère (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), exécuté par {runtime} : les lignes de texte sont trouvées dans le résultat, puis chaque ligne est lue sur le résultat et sur {groups} fusions de groupes indépendants d'images, chacune restaurée avec les mêmes paramètres ; chaque ligne est votée caractère par caractère, pondérée par la probabilité que le modèle donne à chaque caractère (Quiala et al., 2023).",
    "the whole area": "toute la zone",
    "Model confidence": "Confiance du modèle",
    "Area read": "Zone lue",
    "Text lines": "Lignes de texte",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} pixels du résultat",
    "Possible country": "Pays possible",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, probabilité moyenne des caractères lus dans le résultat",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % des votes), estimé par le modèle d'après l'aspect de la plaque",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV ne peut pas charger le modèle téléchargé {name}.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name} : le fichier téléchargé n'est pas celui attendu (son empreinte SHA-256 est différente).",
    "Read characters": "Lire les caractères",
    "CHARACTERS": "CARACTÈRES",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Caractères lus : {text}  ·  accord {agreement:.0f} %  ·  {count} lectures",
    "Character reading": "Lecture des caractères",
    "reading…": "lecture…",
    "no characters found: draw the area tight around the text": "aucun caractère trouvé : tracez la zone au plus près du texte",
    "agreement {agreement:.0f} %  ·  {count} readings": "accord {agreement:.0f} %  ·  {count} lectures",
    "Character reading failed: {error}": "Échec de la lecture des caractères : {error}",
    "doubtful: {list}": "douteux : {list}",
    "check by eye: {list}": "à vérifier à l'œil : {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Trop peu d'images pour des groupes indépendants : seul le résultat a été lu, sans vote.",
    "Character reading (OCR)": "Lecture des caractères (OCR)",
    "illegible":
        "illisible",
    "no character recognizable with enough confidence":
        "aucun caractère reconnaissable avec une confiance suffisante",
    "{count} illegible lines not shown":
        "{count} lignes illisibles non affichées",
    "not recognizable (?): {list}":
        "non reconnaissables (?) : {list}",
    "illegible: no character recognizable with enough confidence":
        "illisible : aucun caractère reconnaissable avec une confiance suffisante",
    "? = character not recognizable":
        "? = caractère non reconnaissable",
    "Thresholds":
        "Seuils",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "une ligne compte comme lisible à partir d'une confiance du modèle de {legible:.0f} % ; un caractère est affiché quand son soutien (votes pondérés par la probabilité que le modèle lui donne, sur toutes les lectures) atteint {support:.0f} %, sinon «?».",
    "Illegible lines":
        "Lignes illisibles",
    "{count} lines found but not recognizable, not shown":
        "{count} lignes trouvées mais non reconnaissables, non affichées",
    "support":
        "soutien",
    "Single readings (model output, before the thresholds)":
        "Lectures individuelles (sortie du modèle, avant les seuils)",
    "Frames used in the fusion":
        "Images utilisées dans la fusion",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Les {count} images qui composent le résultat : la zone du sujet de chacune, alignée sur l'image de référence telle qu'elle entre dans la fusion, avec son poids (R = image de référence).",
    "Play / pause (Space)":
        "Lecture / pause (Espace)",
    "Fit":
        "Ajuster",
    "Choose the language":
        "Choisissez la langue",
    "Before you start":
        "Avant de commencer",
    "What {app} produces":
        "Ce que produit {app}",
    "How the result is obtained":
        "Comment le résultat est obtenu",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} ne crée pas d'images : il combine les informations réellement présentes dans de nombreuses images de la même vidéo. Il suit d'image en image la zone que vous dessinez, aligne chaque image sur l'image de référence avec une précision inférieure au pixel, écarte les images qui ne s'alignent pas de façon fiable et fusionne les autres par une moyenne pondérée résistante aux valeurs aberrantes. Chaque image enregistre le sujet avec un décalage légèrement différent et un bruit différent : combinées, le bruit diminue et des détails répartis sur plusieurs images apparaissent (super-résolution multi-images). La déconvolution et les corrections de contraste qui suivent sont des opérations déterministes, dont tous les paramètres sont écrits dans le rapport.",
    "The result is a reconstruction":
        "Le résultat est une reconstruction",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "L'image obtenue est une reconstruction calculée uniquement à partir des pixels réels des images utilisées, chacune listée dans le rapport avec son poids. Aucun modèle génératif ni intelligence artificielle n'ajoute, ne complète ni n'imagine de détails : ce qui n'est dans aucune image ne peut pas apparaître dans le résultat. Une reconstruction peut toutefois contenir des artefacts (bords dédoublés là où l'alignement est imparfait, halos de la déconvolution) et ne vaut que ce que vaut la source : comparez-la toujours aux images originales.",
    "Character reading and country are estimates":
        "Lecture des caractères et pays sont des estimations",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "La lecture des caractères (OCR) et le pays de la plaque sont en revanche des estimations de modèles de reconnaissance entraînés sur des exemples, qui proposent toujours les caractères les plus probables. Le programme combine plusieurs lectures et marque par «?» ou comme illisible ce qui n'atteint pas ses seuils, mais même une lecture affichée en vert peut être fausse. C'est une aide, pas une preuve : vérifiez chaque caractère à l'œil sur l'image.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "J'ai compris que le résultat est une reconstruction à partir des images de la vidéo, dans laquelle rien n'est inventé, alors que la lecture des caractères et l'attribution du pays sont des estimations à vérifier.",
    "Accept and continue":
        "Accepter et continuer",
    "Exit":
        "Quitter",
    "Vote by position": "Vote par position",
    "result": "résultat",
    "Reading": "Lecture",
    "Agreement": "Accord",
    "Method": "Méthode",
    "Statement": "Déclaration",
    "pos.": "pos.",
    "char.": "car.",
    "agreement": "accord",
    "alternatives": "alternatives",
    "looks like": "ressemble à",
    "group": "groupe",
    "source": "source",
    "text": "texte",
    "conf.": "conf.",
    "frames": "images",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Enregistré par vous.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Préréglages fournis pour le type de sujet choisi dans la page Sujet, puis les vôtres.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» est un préréglage fourni : choisissez un autre nom.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Plaque, standard : perspective, 75 % les plus nettes, ×2, moyenne robuste, déconvolution modérée. Le point de départ.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Plaque de nuit ou bruitée : plus d'images, réduction du bruit moyenne, déconvolution plus douce avec régularisation forte, contraste local léger, niveaux de gris.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Plaque lointaine et petite filmée sur de nombreuses images : ×3, décalage et addition, presque toutes les images, seuil d'alignement plus bas.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Véhicule en mouvement ou qui s'approche, avec flou de bougé : seulement la moitié la plus nette des images, recherche du sujet plus tolérante, déconvolution plus forte.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Plaque à l'ombre ou à contre-jour : contraste local moyen, niveaux de gris, réduction du bruit légère.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Visage, standard : affine, affinement local, réduction du bruit légère, déconvolution douce avec régularisation forte. Le point de départ.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Visage de nuit ou bruité : plus d'images, réduction du bruit moyenne, déconvolution très légère.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Visage, traitement minimal : fusion avec les seuls niveaux automatiques, sans réduction du bruit ni déconvolution. Le résultat le plus prudent.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Visage lointain et petit : ×3, presque toutes les images, seuil d'alignement plus bas.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Visage à l'ombre ou à contre-jour : contraste local léger, déconvolution douce.",
}
