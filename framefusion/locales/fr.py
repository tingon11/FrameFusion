# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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
    "{name} is not a FrameFusion report.": "{name} n'est pas un rapport FrameFusion.",
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
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Fusion : f{first} → f{last}, référence f{ref}, zone {width} × {height} en ({x}, {y}), ×{scale}, {method}",
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
    "{done} / {total} frames decoded": "{done} / {total} images décodées",
    "{count} frames decoded": "{count} images décodées",
    "The video ended before the reference frame.": "La vidéo se termine avant l'image de référence.",
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
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  page   ·   ← →  image   ·   I / O  plage   ·   F5  fusionner   ·   Ctrl+S  enregistrer",
    "ffmpeg missing": "ffmpeg manquant",
    "Operation failed": "Échec de l'opération",
    "ERROR - {title}: {message}": "ERREUR - {title} : {message}",
    "Error: {title}": "Erreur : {title}",
    "INTERNAL ERROR": "ERREUR INTERNE",
    "Internal error: details in the log.": "Erreur interne : détails dans le journal.",
}
