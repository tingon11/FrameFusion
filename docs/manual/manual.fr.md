# IdentiFrame — Manuel d'utilisation

[English](manual.en.md) · [Italiano](manual.it.md) · [Deutsch](manual.de.md) · **Français** · [Español](manual.es.md) · [Nederlands](manual.nl.md) · [Polski](manual.pl.md) · [Ελληνικά](manual.el.md) · [Shqip](manual.sq.md)

IdentiFrame améliore la lisibilité d'un petit détail — une plaque
d'immatriculation, un visage, une enseigne — filmé sur plusieurs images d'une
vidéo. Il aligne ces images avec une précision sous-pixel, les fusionne sur une
grille plus fine, réduit le bruit et le flou, et produit **une image unique**
accompagnée d'un rapport qui documente chaque paramètre et chaque étape.

*Andrea Cumini — www.osintinfo.net — andrea@osintinfo.net*

## Sommaire

1. [Principe de fonctionnement](#1-principe-de-fonctionnement)
2. [Installation et premier démarrage](#2-installation-et-premier-démarrage)
3. [Page Configuration](#3-page-configuration)
4. [Page Sujet : images, sujet et référence](#4-page-sujet--images-sujet-et-référence)
5. [Page Fusion](#5-page-fusion)
6. [Enregistrement : images et rapport](#6-enregistrement--images-et-rapport)
7. [Tirer le meilleur parti d'une plaque ou d'un visage](#7-tirer-le-meilleur-parti-dune-plaque-ou-dun-visage)
8. [Limites et bon usage](#8-limites-et-bon-usage)
9. [Raccourcis clavier](#9-raccourcis-clavier)
10. [Modèles OCR (facultatifs)](#10-modèles-ocr-facultatifs)

## 1. Principe de fonctionnement

Chaque image d'une vidéo enregistre le sujet à une position légèrement
différente par rapport à la grille des pixels, avec son propre bruit aléatoire.
IdentiFrame en tire parti : il retrouve le sujet dans chaque image, aligne
toutes les images sur une même **image de référence** avec une précision
sous-pixel, puis les combine. Le bruit diminue et une partie du détail perdu
dans chaque image isolée réapparaît. Rien n'est inventé : le résultat ne
contient que ce que les images permettent d'établir.

Le travail se déroule en sept étapes, affichées dans le cadre *Pipeline* :

| Étape | Ce qui se passe |
| --- | --- |
| 1. Extraction des images | La plage choisie est décodée par FFmpeg, à l'image près. |
| 2. Détection du sujet | Le sujet est suivi image par image, vers l'avant et vers l'arrière à partir de la référence. |
| 3. Alignement local | Chaque image est alignée sur la référence (algorithme ECC ; modèle translation, rotation, affine ou perspective). |
| 4. Recalage sous-pixel | L'alignement est affiné en pleine résolution ; les images les plus nettes et les mieux alignées sont retenues. |
| 5. Fusion multi-images | Les images sont rééchantillonnées sur une grille jusqu'à 4 fois plus fine et combinées, en rejetant les valeurs aberrantes. |
| 6. Déconvolution et débruitage | Niveaux automatiques, réduction du bruit facultative et déconvolution de Richardson-Lucy sur la luminance. |
| 7. Image unique | Image finale, fantôme des images, comparaison avec la référence, données pour le rapport. |

## 2. Installation et premier démarrage

**Exécutable (Windows 10/11, 64 bits).** Décompressez `IdentiFrame-<version>-windows-x64.zip`
à l'emplacement de votre choix et lancez `IdentiFrame.exe`. Python n'est pas
nécessaire. L'exécutable n'est pas signé : la première fois, Windows SmartScreen
peut demander une confirmation.

**Depuis les sources.** Avec Python 3.10 ou ultérieur :

```bash
python -m pip install -r requirements.txt
python IdentiFrame.py
```

**Avertissement au démarrage.** À chaque démarrage s'affiche un
avertissement à accepter : il explique que le résultat est une
reconstruction calculée uniquement à partir des pixels réels des images,
dans laquelle rien n'est inventé, alors que la lecture des caractères et le
pays sont des estimations à vérifier. *Accepter et continuer* devient actif
après avoir coché la déclaration. Au tout premier démarrage, la langue est
demandée d'abord, et l'avertissement apparaît dans la langue choisie.

![Avertissement au démarrage](images/fr/00_notice.png)

**FFmpeg.** IdentiFrame utilise FFmpeg pour lire les vidéos, mais ne l'inclut
pas. Au premier démarrage, si FFmpeg est absent, la page **Configuration**
s'ouvre sur le cadre *FFmpeg* : **Télécharger / Mettre à jour** récupère la
version officielle pour Windows dans le dossier `tools\ffmpeg` à côté du
programme. Rien n'est installé sur le système.

Une vidéo peut aussi être ouverte depuis la ligne de commande :
`IdentiFrame.exe video.mp4`.

## 3. Page Configuration

![Page Configuration](images/fr/01_configuration.png)

- **Source** — **Ouvrir une vidéo…** (ou Ctrl+O, ou l'icône de dossier dans le
  cadre *VIDEO* en haut). La durée, le nombre d'images, la résolution et le
  codec s'affichent ici. Lorsqu'une vidéo est ouverte, le programme passe à la
  page *Sujet*.
- **Sortie** — *Dossier de destination* où les fusions sont enregistrées (vide =
  à côté de la vidéo), *Sous-dossier au nom de la vidéo*, *Format* (PNG ou TIFF)
  et *Profondeur de couleur* (*Auto* = 16 bits par canal pour la fusion).
  *Enregistrer aussi chaque image alignée (dossier aligned/)* ajoute un dossier
  `aligned/` contenant chaque image utilisée, alignée sur la référence.
- **FFmpeg** — emplacement et version de FFmpeg : **Vérifier**, **Rechercher
  des mises à jour**, **Télécharger / Mettre à jour**.
- **Modèles OCR** — les deux modèles facultatifs qui lisent les caractères des plaques et des textes, téléchargés à la demande dans `tools\ocr` (environ 37 Mo) : **Vérifier** et **Télécharger / Mettre à jour**. Sans eux le programme fonctionne, sans la lecture des caractères. Voir [10. Modèles OCR](#10-modèles-ocr-facultatifs).
- **Langue** — l'interface et les rapports sont disponibles en neuf langues :
  EN, IT, DE, FR, ES, NL, PL, EL, SQ. Le changement est immédiat et mémorisé.
- **Crédits** — auteur et licence.

## 4. Page Sujet : images, sujet et référence

![Page Sujet](images/fr/02_subject.png)

L'*Aperçu* affiche l'image sous le curseur : la **molette** zoome autour de la
souris (jusqu'aux pixels réels), **glisser** déplace la vue, un **double-clic**
ajuste de nouveau l'image à la fenêtre. En dessous, les boutons font avancer ou
reculer d'une ou de dix images ; **← →** et **Maj+← →** font de même au clavier.

Le bouton **lecture** au centre lit l'aperçu à partir du curseur et devient
**pause** pendant la lecture (Espace fait de même) ; le curseur et la
timeline suivent, on peut donc marquer un intervalle avec I et O en
regardant. Un clic sur la timeline ou un déplacement d'image arrête la
lecture.

La *Timeline* (chronologie) montre toute la vidéo sous forme de pellicule.
**Ctrl+molette** zoome, la **molette** fait défiler ; un clic ou un glissement
déplace le curseur. *Tout* et *Sélection* ajustent la vue.

**1. Choisissez l'image de référence.** Placez-vous sur l'image où le sujet est
**le plus grand et le plus net** — pour un véhicule qui s'approche, en général
l'une des dernières images où la plaque est encore entièrement visible.

**2. Sélectionnez la zone du sujet.** Glissez avec le **bouton droit de la
souris** sur la plaque ou le visage, ou appuyez sur **Sélectionner la zone** et
glissez avec le bouton gauche. Cadrez le sujet avec une petite marge. L'image
affichée devient la **référence** (repère **R** sur la chronologie ; **→ R** y
ramène le curseur) et **la fusion démarre d'elle-même** : le programme passe à
la page *Fusion*. Si vous dessinez une nouvelle zone pendant le calcul, la
fusion redémarre. **Effacer** supprime la zone.

**3. Choisissez la plage.** **Entrée [I]** et **Sortie [O]** (touches I et O)
fixent la première et la dernière image à utiliser : celles où le sujet est
visible et non masqué. Les drapeaux I et O peuvent aussi être déplacés à la
souris, et les champs IN / OUT acceptent un temps (`1:23.456`) ou une image
(`f2000`). Chaque fois que la zone est dessinée, la plage est fixée à 30
secondes avant et 30 après la référence (dans les limites de la vidéo) : ce ne
sont que les limites de la recherche. La fusion suit le sujet depuis la
référence vers l'extérieur et s'arrête, dans chaque sens, après une seconde sans
le voir ; les drapeaux I et O se resserrent ensuite sur les images où il a été
suivi (le rapport l'indique). Une plage déplacée à la main reste telle quelle.
Après avoir modifié la plage, **Fusionner les images →** (ou F5) relance la
fusion. 3601 images au maximum dans la plage.

## 5. Page Fusion

![Page Fusion : fantôme et résultat](images/fr/03_fusion_ghost.png)

**Comparaison.** À gauche, le **Fantôme des images** : toutes les images
utilisées, superposées à la position où chacune a été trouvée, avant
l'alignement. Il montre ce qui entre dans la fusion et à quel point le sujet
se déplace. Avec le menu situé au-dessus, la vue de gauche peut afficher à
la place l'**Image de référence**, agrandie par interpolation bicubique :
c'est l'image « avant » qui permet une comparaison honnête. À droite, le
résultat : **Final**, ou **Fusion seule** (avant la réduction du bruit et la
déconvolution). Les deux vues zooment et se déplacent ensemble. En plus de
la molette, les boutons sous les vues réduisent (**−**, aussi en dessous de
la taille ajustée, pour voir le résultat en petit), agrandissent (**+**),
affichent à **1:1** ou **ajustent** à la vue ; au clavier **−**, **+** et
**0**.

![Page Fusion : référence et résultat](images/fr/04_fusion_reference.png)

La deuxième image montre un visage, avec le préréglage **Face 05** et l'image
de référence à gauche.

**Caractères.** Avec les modèles OCR téléchargés, après chaque fusion d'une *Plaque* ou d'un *Texte* la ligne **CARACTÈRES** du cadre *Pipeline* affiche les caractères lus (**Lire les caractères** la répète). Le résultat et huit fusions de groupes indépendants d'images sont lus, et les lectures sont votées caractère par caractère. Les modèles de reconnaissance proposent toujours les caractères les plus probables, même là où rien n'est lisible : une ligne n'est affichée qu'à partir d'une confiance du modèle de 60 %, sinon le programme écrit **illisible**, et un caractère qui ne réunit pas au moins 50 % des votes pondérés apparaît comme **«?»**. Pour une plaque, le **pays possible** estimé par le modèle apparaît en jaune à côté des caractères seulement quand la lecture est lisible et qu'un pays a la majorité des votes ; sinon il figure parmi les détails, avec sa part. Les détails indiquent aussi l'**accord** entre les lectures, la **confiance du modèle**, les positions **douteuses** et les caractères à **vérifier à l'œil** (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G). Un *Texte* peut avoir plusieurs lignes, séparées par «|», votées chacune séparément. Sur la première image la plaque est très petite (caractères d'environ 12 pixels de haut dans la vidéo) et elle est lue 34LG4527, pays possible Turkey. Lecture et pays sont des estimations : comparez toujours avec l'image.

**Pipeline.** Les sept étapes avec leur résultat et leur durée ; en dessous, le
résumé (images utilisées, agrandissement, bruit avant et après la fusion), la
barre de progression et les boutons **Ouvrir le dossier**, **Annuler**,
**Enregistrer le résultat**, **Lancer la fusion**. Les étapes 1 à 4 ne dépendent
que de la vidéo, de la plage, de la référence, de la zone et du modèle de
mouvement : lorsque seuls les paramètres de fusion ou de restauration changent,
elles sont réutilisées et une nouvelle fusion ne prend qu'une fraction de
seconde (*réutilisé* dans la liste des étapes).

### Paramètres

La colonne de gauche regroupe les paramètres par étape.

**Type de sujet.** Le menu à côté de *Sélectionner la zone*, dans le cadre *Sujet* de la page *Sujet*, indique ce que l'on améliore. **Plaque** et **Texte** : un sujet plat et rigide, un modèle de mouvement par image ; ils diffèrent par la lecture des caractères (un modèle fait pour les plaques, ou un pour les textes sur une ou plusieurs lignes, en de nombreuses langues). **Visage** : d'une image à l'autre la tête tourne et l'expression change, donc après l'alignement rigide chaque image reçoit un raffinement local non rigide qui suit ces mouvements à quelques pixels près ; les parties encore différentes comptent moins, les images avec une pose ou une expression différente sont écartées, la restauration est plus légère et les niveaux automatiques ménagent la peau et les ombres. Changer de type charge ses valeurs par défaut et refait l'alignement. Rien n'est inventé : le raffinement ne déplace que de quelques pixels ce que contiennent les images. Pour un visage le modèle de mouvement est affine par défaut, l'alignement refuse les déformations qui ne sont pas un mouvement possible de la tête et, hors de l'ellipse inscrite dans la zone, le résultat montre l'image de référence, car l'arrière-plan bouge autrement.

**Réglages enregistrés.** Jeux de paramètres nommés : **Enregistrer…** demande
un nom et mémorise les paramètres actuels ; choisir un nom dans le menu les
charge ; **Supprimer** efface le jeu choisi ; **Par défaut** rétablit chaque
paramètre. **Depuis un rapport…** charge les paramètres depuis le `report.json`
d'une fusion enregistrée auparavant, pour la reproduire à l'identique. Les
paramètres en cours sont également mémorisés à la fermeture du programme.

**Préréglages intégrés.** Le menu *Réglages enregistrés* commence toujours par cinq préréglages pour le type de sujet choisi sur la page Sujet : **Plate 01** standard, **02** nuit ou bruit, **03** plaque lointaine et petite, **04** véhicule en mouvement avec flou de bougé, **05** ombre ou contre-jour ; **Text 01–05** les mêmes cinq cas pour les textes ; **Face 01** standard, **02** nuit ou bruit, **03** traitement minimal, **04** visage lointain et petit, **05** ombre ou contre-jour. Une ligne sous le menu décrit celui choisi ; ils ne peuvent être ni modifiés ni supprimés, et vos propres réglages suivent.

| Cadre | Paramètre | Effet |
| --- | --- | --- |
| Page Sujet | Type de sujet | Plaque (par défaut) ou Texte pour un sujet plat et rigide (ils diffèrent par la lecture des caractères) ; Visage ajoute le raffinement local non rigide et une restauration plus légère. |
| Images et alignement | Modèle de mouvement | Translation, rotation + translation, affine, **perspective (homographie)** — par défaut ; suit un sujet qui s'approche, s'éloigne ou tourne. Si une image ne converge pas, un modèle plus simple est essayé. |
| | Recherche du sujet : corrélation minimale | En dessous de ce score, le sujet est considéré comme non trouvé dans une image. |
| | Qualité minimale de l'alignement (ECC) | Les images moins bien alignées que ce seuil sont écartées (0.80 par défaut). |
| | Images les plus nettes conservées | 75 % par défaut : le quart le moins net (flou de bougé) est écarté. |
| Fusion | Agrandissement | × 1 (réduction du bruit seulement) à × 4. × 2 ou × 3 est généralement le bon choix. |
| | Méthode de fusion | **Moyenne robuste (valeurs aberrantes rejetées)** — par défaut ; médiane ; décalage et addition avec convolution normalisée. |
| | Pondérer par la netteté | Les images plus nettes comptent beaucoup plus. |
| | Égaliser la luminosité | Compense les variations d'exposition entre les images. |
| Restauration | Réduction du bruit | Désactivé, Faible, Moyen, Fort (filtre bilatéral). |
| | Itérations de déconvolution | Richardson-Lucy : plus d'itérations accentuent davantage la netteté, mais amplifient aussi le bruit et les halos. 20 par défaut. |
| | PSF σ (pixels de sortie) | Largeur du flou à supprimer. *Automatique* la mesure sur les contours de l'image fusionnée. |
| | Régularisation (variation totale) | Retient le bruit pendant la déconvolution. Moyen par défaut. |
| Présentation | Niveaux automatiques | Noir et blanc aux centiles 0,5 et 99,5 de la luminance, avant la déconvolution. |
| | Contraste local (CLAHE) | Égalisation par zones : utile sur les plaques à l'ombre ou à contre-jour. |
| | Niveaux de gris | Supprime la couleur : souvent plus propre pour lire les caractères. |

## 6. Enregistrement : images et rapport

**Enregistrer le résultat** (Ctrl+S sur la page *Fusion*) crée un nouveau dossier
`fusion_f<référence>_<date-heure>` dans le dossier de destination, contenant :

| Fichier | Contenu |
| --- | --- |
| `result.png` | l'image finale |
| `fused.png` | la fusion avant la réduction du bruit et la déconvolution |
| `ghost.png` | le fantôme des images utilisées |
| `reference_x<k>.png` | la zone de référence agrandie par interpolation bicubique, pour la comparaison |
| `reference_crop.png` | la même zone à la résolution de la vidéo |
| `report.pdf` | le rapport mis en page au format A4, avec les images |
| `report.txt` | le même rapport en texte brut |
| `report.json` | les mêmes données sous forme structurée, réglages compris (**Depuis un rapport…** les recharge) |
| `aligned/` | sur demande, chaque image utilisée, alignée sur la référence |

![Première page du rapport PDF](images/fr/05_report.png)

Avec une lecture des caractères, le rapport a la section **Lecture des caractères (OCR)** : la lecture, l'accord, la confiance du modèle, pour une plaque le pays possible et la zone lue, pour un texte les lignes trouvées, la méthode, le vote par position avec les alternatives et les caractères semblables, et chaque lecture.

![Lecture des caractères dans le rapport PDF](images/fr/06_report_reading.png)

Le rapport est rédigé dans la langue de l'interface. Il contient la source
(chemin, taille, empreinte **SHA-256**, format), la plage, l'image de référence
et la zone, tous les paramètres, les sept étapes avec les méthodes employées et
leurs durées, le tableau des images (score de recherche, coefficients
d'alignement, décalage sous-pixel, netteté, poids, motif d'exclusion), les
estimations du bruit et le SHA-256 de chaque image écrite. Quiconque le lit peut
refaire le traitement et vérifier que les fichiers n'ont pas été modifiés.

*Enregistrer l'image* sur la page *Sujet* enregistre en revanche uniquement
l'image sous le curseur, en pleine résolution et sans perte.

## 7. Tirer le meilleur parti d'une plaque ou d'un visage

- **Visage** : choisissez d'abord le type de sujet *Visage* ; cadrez tout le visage avec une petite marge, si possible sur une image où il regarde la caméra, et limitez la plage aux images de même pose. Le rapport indique combien d'images ont été écartées pour une pose ou une expression différente et la largeur du visage dans la vidéo : en dessous de 60 pixels environ, attendez-vous à un aspect général plus propre, pas à des traits identifiants.
- **Référence** : l'image où le sujet est le plus grand et le plus net.
- **Plage** : uniquement les images où le sujet est entièrement visible. Les
  images éloignées de la référence (sujet beaucoup plus petit, autre
  perspective) apportent peu et sont de toute façon souvent écartées par le
  seuil de qualité.
- **Zone** : toute la plaque ou tout le visage avec une petite marge ; peu
  d'arrière-plan, qui peut se déplacer différemment.
- **Agrandissement** : × 2 ou × 3. × 4 n'en vaut la peine qu'avec de nombreuses
  images.
- **Caractères encore flous ?** Augmentez *PSF σ* d'un cran (par ex. passez
  d'Automatique à la valeur immédiatement supérieure à celle indiquée dans le
  rapport), ou les *Itérations de déconvolution*.
- **Halos ou « ringing » autour des caractères ?** Diminuez *PSF σ* ou les
  itérations, ou augmentez la *Régularisation (variation totale)*.
- **Plaque à l'ombre ou à contre-jour** : *Contraste local (CLAHE)* sur Faible
  ou Moyen, souvent associé à *Niveaux de gris*.
- **Comparez** toujours avec la vue *Image de référence*, en zoomant sur les
  caractères : ce qui n'y est pas lisible et n'apparaît qu'après une forte
  accentuation de la netteté doit être considéré avec prudence.
- Enregistrez avec **Enregistrer…** un jeu de paramètres qui fonctionne pour une
  caméra donnée, et réutilisez-le.

## 8. Limites et bon usage

- Le résultat est une **amélioration** des images enregistrées, et non une
  reconstruction de la réalité : il ne peut pas restituer ce qu'aucune image ne
  contient.
- Les détails fins à la limite de la résolution, et les caractères qui se
  ressemblent (8/B, 0/D, 1/7, 5/S), doivent être vérifiés sur les images
  sources avant d'en tirer des conclusions.
- Le gain est maximal avec de nombreuses images, de petits décalages entre
  elles, un bruit indépendant et une référence suffisamment nette. Le flou de
  bougé à l'intérieur d'une même image n'est pas supprimé.
- Une forte compression produit des erreurs identiques d'une image à l'autre :
  la fusion les réduit moins que le bruit aléatoire.
- Les plaques d'immatriculation et les visages sont des données à caractère
  personnel : utilisez le programme dans le respect des règles qui vous sont
  applicables.

## 9. Raccourcis clavier

| Touches | Action |
| --- | --- |
| Ctrl+1 / Ctrl+2 / Ctrl+3 | Page Configuration / Sujet / Fusion |
| Ctrl+O | Ouvrir une vidéo |
| ← / → | Image précédente / suivante |
| Maj+← / Maj+→ | Reculer / avancer de 10 images |
| Espace | Lecture ou pause de l'aperçu |
| Début / Fin | Première / dernière image |
| I / O | Début / fin de la plage au curseur |
| + / − | Zoom avant / arrière sur la chronologie |
| F | Toute la vidéo sur la chronologie |
| Glisser-droit sur l'aperçu | Sélectionner la zone du sujet (la fusion démarre) |
| Échap | Quitter *Sélectionner la zone* |
| − / + / 0 (page Fusion) | Réduire / agrandir / ajuster le résultat |
| F11 | Aperçu plus grand : masque ou affiche la chronologie (page Sujet) |
| F5 | Lancer la fusion |
| Ctrl+S | Enregistrer le résultat (page Fusion) ou l'image (page Sujet) |


## 10. Modèles OCR (facultatifs)

La lecture des caractères utilise deux modèles de réseau neuronal, exécutés par OpenCV, qui fait déjà partie du programme. Ils ne sont **pas inclus** dans IdentiFrame et sont **facultatifs** : sans eux tout le reste fonctionne comme d'habitude, seule la ligne CARACTÈRES reste vide. Pour les utiliser, appuyez sur **Télécharger / Mettre à jour** dans le cadre **Modèles OCR** de la page *Configuration* : ils vont dans le dossier `tools\ocr` à côté du programme (environ 37 Mo), et le cadre indique lesquels sont présents.

| Sujet | Modèle | Licence |
| --- | --- | --- |
| Plaque | [fast-plate-ocr](https://github.com/ankandrew/fast-plate-ocr) `cct-s-v2-global`, de ankandrew : lit la plaque entière et estime son pays possible parmi 65 | MIT, code et poids ([confirmé par l'auteur](https://github.com/ankandrew/fast-plate-ocr/issues/97)) |
| Texte | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) PP-OCRv6 small, de Baidu / PaddleOCR, dans la conversion ONNX de [RapidOCR](https://github.com/RapidAI/RapidOCR) : trouve les lignes de texte et les lit en de nombreuses langues | Apache 2.0 |

Chaque fichier est contrôlé avec son empreinte SHA-256 avant d'être conservé ; les textes de licence et un fichier `SOURCE.txt` avec la provenance sont enregistrés à côté des modèles. Le pays est une estimation d'après l'aspect de la plaque, pas une vérification, et il est affiché avec son nom anglais.

*Vidéos de test et captures d'écran, de Pexels, utilisées selon la [licence Pexels](https://www.pexels.com/license/) : « [Busy Highway Traffic at Sunset](https://www.pexels.com/it-it/video/traffico-autostradale-intenso-al-tramonto-31779728/) » de [Şeyhmus Kino](https://www.pexels.com/@seyhmuskino/) (véhicules et plaques), circulation dans une rue de Taipei, Taïwan, de [Levi Wedge](https://www.pexels.com/@levi-wedge-266970209/) ([vidéo](https://www.pexels.com/it-it/video/citta-auto-traffico-veicoli-13271103/), textes) et « [Charming European Street with Cyclist](https://www.pexels.com/it-it/video/affascinante-strada-europea-con-ciclista-33476096/) » de [Tuba Din](https://www.pexels.com/@tubadinn/) (visage). Les plaques, les textes et le visage visibles sur les captures proviennent de ces images.*

---

IdentiFrame est un logiciel libre sous GNU GPL v3 avec attribution de l'auteur :
voir `LICENSE` et `NOTICE`. Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net
