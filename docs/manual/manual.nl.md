# FrameFusion — Gebruikershandleiding

[English](manual.en.md) · [Italiano](manual.it.md) · [Deutsch](manual.de.md) · [Français](manual.fr.md) · [Español](manual.es.md) · **Nederlands** · [Polski](manual.pl.md) · [Ελληνικά](manual.el.md) · [Shqip](manual.sq.md)

FrameFusion verbetert de leesbaarheid van een klein detail — een kenteken,
een gezicht, een bord — dat in meerdere frames van een video is gefilmd. Het
lijnt die frames met subpixelprecisie uit, fuseert ze op een fijner raster,
vermindert ruis en onscherpte, en levert **één enkel beeld** op, met een
rapport dat elke parameter en elke stap documenteert.

*Andrea Cumini — www.osintinfo.net — andrea@osintinfo.net*

## Inhoud

1. [Hoe het werkt](#1-hoe-het-werkt)
2. [Installatie en eerste start](#2-installatie-en-eerste-start)
3. [Pagina Configuratie](#3-pagina-configuratie)
4. [Pagina Onderwerp: frames, onderwerp en referentie](#4-pagina-onderwerp-frames-onderwerp-en-referentie)
5. [Pagina Fusie](#5-pagina-fusie)
6. [Opslaan: afbeeldingen en rapport](#6-opslaan-afbeeldingen-en-rapport)
7. [Het beste halen uit een kenteken of een gezicht](#7-het-beste-halen-uit-een-kenteken-of-een-gezicht)
8. [Grenzen en correct gebruik](#8-grenzen-en-correct-gebruik)
9. [Sneltoetsen](#9-sneltoetsen)

## 1. Hoe het werkt

Elk frame van een video legt het onderwerp vast op een iets andere positie
ten opzichte van het pixelraster, en met een eigen willekeurige ruis.
FrameFusion maakt daar gebruik van: het zoekt het onderwerp in elk frame,
lijnt alle frames met subpixelprecisie uit op één **referentieframe** en
combineert ze. De ruis neemt af en een deel van het detail dat elk afzonderlijk
frame verliest, komt terug. Er wordt niets verzonnen: het resultaat bevat
alleen wat de frames ondersteunen.

Het werk gebeurt in zeven stappen, die in het vak *Pipeline* worden getoond:

| Stap | Wat er gebeurt |
| --- | --- |
| 1. Frame-extractie | Het gekozen bereik wordt door FFmpeg gedecodeerd, exact op het frame. |
| 2. Onderwerpdetectie | Het onderwerp wordt frame voor frame gevolgd, vanaf de referentie voorwaarts en achterwaarts. |
| 3. Lokale uitlijning | Elk frame wordt uitgelijnd op de referentie (ECC-algoritme; model: translatie, rotatie, affien of perspectief). |
| 4. Subpixelregistratie | De uitlijning wordt verfijnd op volledige resolutie; de scherpste en best uitgelijnde frames worden gekozen. |
| 5. Multiframe-fusie | De frames worden herbemonsterd op een tot 4 keer fijner raster en gecombineerd, waarbij uitschieters worden verworpen. |
| 6. Deconvolutie en ruisonderdrukking | Automatische niveaus, optionele ruisonderdrukking en Richardson-Lucy-deconvolutie op de luminantie. |
| 7. Enkel frame | Definitief beeld, spookbeeld van de frames, vergelijking met de referentie, gegevens voor het rapport. |

## 2. Installatie en eerste start

**Uitvoerbaar bestand (Windows 10/11, 64-bit).** Pak `FrameFusion-<versie>-windows-x64.zip`
uit op een willekeurige plek en start `FrameFusion.exe`. Python is niet nodig.
Het uitvoerbare bestand is niet ondertekend: de eerste keer kan Windows
SmartScreen om bevestiging vragen.

**Vanuit de broncode.** Met Python 3.10 of nieuwer:

```bash
python -m pip install -r requirements.txt
python FrameFusion.py
```

**FFmpeg.** FrameFusion gebruikt FFmpeg om video's te lezen, maar bevat het
niet. Als FFmpeg bij de eerste start ontbreekt, opent de pagina
**Configuratie** op het vak *FFmpeg*: **Downloaden / Bijwerken** haalt de
officiële Windows-build op in de map `tools\ffmpeg` naast het programma. Er
wordt niets op het systeem geïnstalleerd.

Een video kan ook vanaf de opdrachtregel worden geopend:
`FrameFusion.exe video.mp4`.

## 3. Pagina Configuratie

![Pagina Configuratie](images/nl/01_configuration.png)

- **Bron** — **Video openen…** (of Ctrl+O, of het mappictogram in het vak
  *VIDEO* bovenaan). Hier worden duur, aantal frames, resolutie en codec
  getoond. Wanneer een video wordt geopend, gaat het programma naar de pagina
  *Onderwerp*.
- **Uitvoer** — *Doelmap* waar de fusies worden opgeslagen (leeg = naast de
  video), *Submap met de naam van de video*, *Formaat* (PNG of TIFF) en
  *Kleurdiepte* (*Auto* = 16 bits per kanaal voor de fusie). *Ook elk
  uitgelijnd frame opslaan (map aligned/)* bewaart bovendien elk gebruikt
  frame, uitgelijnd op de referentie.
- **FFmpeg** — waar FFmpeg staat en welke versie: **Controleren**, **Zoeken
  naar updates**, **Downloaden / Bijwerken**.
- **Taal** — de interface en de rapporten zijn beschikbaar in negen talen:
  EN, IT, DE, FR, ES, NL, PL, EL, SQ. De wijziging is onmiddellijk en wordt
  onthouden.
- **Colofon** — auteur en licentie.

## 4. Pagina Onderwerp: frames, onderwerp en referentie

![Pagina Onderwerp](images/nl/02_subject.png)

Het *Voorbeeld* toont het frame onder de cursor: het **scrollwiel** zoomt
rond de muis (tot op de echte pixels), **slepen** verschuift het beeld, een
**dubbelklik** maakt het frame weer passend. Daaronder verplaatsen de knoppen
de cursor één of tien frames; **← →** en **Shift+← →** doen hetzelfde met het
toetsenbord.

De tijdlijn (het vak *Timeline*) toont de hele video als een filmstrook.
**Ctrl+scrollwiel** zoomt, het **scrollwiel** scrolt; klikken of slepen
verplaatst de cursor. *Alles* en *Selectie* passen de weergave aan.

**1. Kies het referentieframe.** Ga naar het frame waarin het onderwerp **het
grootst en het scherpst** is — bij een voertuig dat nadert meestal een van de
laatste frames waarin het hele kenteken nog zichtbaar is.

**2. Selecteer het gebied van het onderwerp.** Sleep met de
**rechtermuisknop** over het kenteken of het gezicht, of druk op **Gebied
selecteren** en sleep met de linkermuisknop. Omkader het onderwerp met een
kleine marge. Het getoonde frame wordt de **referentie** (markering **R** op
de tijdlijn; **→ R** brengt de cursor ernaar terug) en **de fusie start
vanzelf**: het programma gaat naar de pagina *Fusie*. Als u een nieuw gebied
tekent terwijl de fusie loopt, wordt die opnieuw gestart. **Wissen**
verwijdert het gebied.

**3. Kies het bereik.** **In [I]** en **Uit [O]** (toetsen I en O) bepalen
het eerste en het laatste frame dat wordt gebruikt: de frames waarin het
onderwerp zichtbaar is en niet bedekt. De markeringen I en O kunnen ook worden
versleept, en de velden IN / OUT accepteren een tijd (`1:23.456`) of een frame
(`f2000`). Als het bereik bij het tekenen van het gebied nog de hele video is,
wordt het ingesteld op 30 frames vóór en na de referentie. Start na een
wijziging van het bereik de fusie opnieuw met **Frames fuseren →** (of F5).
Hoogstens 300 frames per fusie.

## 5. Pagina Fusie

![Pagina Fusie: spookbeeld en resultaat](images/nl/03_fusion_ghost.png)

**Vergelijking.** Links het **Spookbeeld van de frames**: alle gebruikte
frames, over elkaar gelegd op de positie waar elk ervan werd gevonden, vóór de
uitlijning. Het laat zien wat er in de fusie gaat en hoeveel het onderwerp
beweegt. Met het menu erboven kan de linkerweergave in plaats daarvan het
**Referentieframe** tonen, vergroot met bicubische interpolatie: dat is het
eerlijke ‘vóór’-beeld. Rechts het resultaat: **Definitief**, of **Alleen
fusie** (vóór ruisonderdrukking en deconvolutie). De twee weergaven zoomen en
verschuiven samen.

![Pagina Fusie: referentie en resultaat](images/nl/04_fusion_reference.png)

**Pipeline.** De zeven stappen met hun uitkomst en tijd; daaronder de
samenvatting (gebruikte frames, vergroting, ruis vóór en na de fusie), de
voortgangsbalk en de knoppen **Map openen**, **Annuleren**, **Resultaat
opslaan**, **Fusie starten**. Stappen 1–4 hangen alleen af van video, bereik,
referentie, gebied en bewegingsmodel: als alleen de parameters van fusie of
restauratie veranderen, worden ze hergebruikt en duurt een nieuwe fusie een
fractie van een seconde (*hergebruikt* in de lijst van stappen).

### Parameters

De kolom links groepeert de parameters per stap.

**Opgeslagen instellingen.** Sets parameters met een naam: **Opslaan…** vraagt
om een naam en bewaart de huidige parameters; een naam kiezen in het menu
laadt ze; **Verwijderen** verwijdert de gekozen set; **Standaard** zet elke
parameter terug. **Uit rapport…** laadt de parameters uit de `report.json`
van een eerder opgeslagen fusie, om die exact te herhalen. De gebruikte
parameters worden ook onthouden wanneer het programma wordt afgesloten.

| Vak | Parameter | Effect |
| --- | --- | --- |
| Frames en uitlijning | Bewegingsmodel | Translatie, Rotatie + translatie, Affien, **Perspectief (homografie)** — standaard; volgt een onderwerp dat nadert, zich verwijdert of draait. Als een frame niet convergeert, wordt een eenvoudiger model geprobeerd. |
| | Zoeken naar het onderwerp: minimale correlatie | Onder deze score geldt het onderwerp in een frame als niet gevonden. |
| | Minimale uitlijningskwaliteit (ECC) | Frames die slechter zijn uitgelijnd, worden weggelaten (standaard 0.80). |
| | Scherpste frames behouden | Standaard 75 %: het minst scherpe kwart (bewegingsonscherpte) wordt weggelaten. |
| Fusie | Vergroting | × 1 (alleen ruisonderdrukking) tot × 4. × 2 of × 3 is meestal de juiste keuze. |
| | Fusiemethode | **Robuust gemiddelde (uitschieters verworpen)** — standaard; Mediaan; Shift-and-add (genormaliseerde convolutie). |
| | Wegen op scherpte | Scherpere frames tellen veel zwaarder. |
| | Helderheid gelijkmaken | Compenseert belichtingsverschillen tussen frames. |
| Restauratie | Ruisonderdrukking | Uit, Licht, Gemiddeld, Sterk (bilateraal filter). |
| | Deconvolutie-iteraties | Richardson-Lucy: meer iteraties verscherpen meer, maar versterken ook ruis en halo's. Standaard 20. |
| | PSF σ (uitvoerpixels) | Breedte van de onscherpte die moet worden verwijderd. *Automatisch* meet die op de randen van het gefuseerde beeld. |
| | Regularisatie (totale variatie) | Houdt de ruis in toom tijdens de deconvolutie. Standaard Gemiddeld. |
| Presentatie | Automatische niveaus | Zwart en wit op de percentielen 0,5 en 99,5 van de luminantie, vóór de deconvolutie. |
| | Lokaal contrast (CLAHE) | Egalisatie per zone: nuttig bij kentekens in de schaduw of in tegenlicht. |
| | Grijstinten | Laat de kleur weg: vaak schoner om tekens te lezen. |

## 6. Opslaan: afbeeldingen en rapport

**Resultaat opslaan** (Ctrl+S op de pagina *Fusie*) maakt in de doelmap een
nieuwe map `fusion_f<referentie>_<datum-tijd>` aan, met:

| Bestand | Inhoud |
| --- | --- |
| `result.png` | het definitieve beeld |
| `fused.png` | de fusie vóór ruisonderdrukking en deconvolutie |
| `ghost.png` | het spookbeeld van de gebruikte frames |
| `reference_x<k>.png` | het referentiegebied, vergroot met bicubische interpolatie, ter vergelijking |
| `reference_crop.png` | hetzelfde gebied op de resolutie van de video |
| `report.pdf` | het rapport, opgemaakt op A4, met de afbeeldingen |
| `report.txt` | hetzelfde rapport als platte tekst |
| `report.json` | dezelfde gegevens in gestructureerde vorm, inclusief de instellingen (**Uit rapport…** laadt ze opnieuw) |
| `aligned/` | op verzoek elk gebruikt frame, uitgelijnd op de referentie |

![Eerste pagina van het PDF-rapport](images/nl/05_report.png)

Het rapport wordt geschreven in de taal van de interface. Het bevat de bron
(pad, grootte, **SHA-256**-vingerafdruk, formaat), het bereik, het
referentieframe en het gebied, alle parameters, de zeven stappen met de
gebruikte methoden en hun tijden, de tabel van de frames (zoekscore,
uitlijningscoëfficiënten, subpixelverschuiving, scherpte, gewicht, reden van
uitsluiting), ruisschattingen en de SHA-256 van elke geschreven afbeelding.
Wie het leest, kan de verwerking herhalen en controleren dat de bestanden
niet zijn gewijzigd.

*Frame opslaan* op de pagina *Onderwerp* slaat daarentegen alleen het frame
onder de cursor op, op volledige resolutie en verliesvrij.

## 7. Het beste halen uit een kenteken of een gezicht

- **Referentie**: het frame waarin het onderwerp het grootst en het scherpst
  is.
- **Bereik**: alleen de frames waarin het onderwerp volledig zichtbaar is.
  Frames die ver van de referentie liggen (veel kleiner, ander perspectief),
  dragen weinig bij en worden vaak toch al door de kwaliteitsdrempel
  weggelaten.
- **Gebied**: het hele kenteken of gezicht met een kleine marge; niet te veel
  achtergrond, die anders kan bewegen.
- **Vergroting**: × 2 of × 3. × 4 loont alleen met veel frames.
- **Tekens nog zacht?** Verhoog *PSF σ* met één stap (bijv. van Automatisch
  naar de eerstvolgende waarde boven de waarde in het rapport), of de
  *Deconvolutie-iteraties*.
- **Halo's of ‘ringing’ rond de tekens?** Verlaag *PSF σ* of de iteraties, of
  verhoog de *Regularisatie (totale variatie)*.
- **Kenteken in de schaduw of in tegenlicht**: *Lokaal contrast (CLAHE)* op
  Licht of Gemiddeld, vaak samen met *Grijstinten*.
- **Vergelijk** altijd met de weergave *Referentieframe* en zoom in op de
  tekens: wat daar niet leesbaar is en pas na sterke verscherping verschijnt,
  moet met voorzichtigheid worden behandeld.
- Bewaar een set parameters die voor een camera goed werkt met **Opslaan…**
  en gebruik die opnieuw.

## 8. Grenzen en correct gebruik

- Het resultaat is een **verbetering** van de opgenomen frames, geen
  reconstructie van de werkelijkheid: het kan niet terughalen wat in geen
  enkel frame staat.
- Fijne details op de grens van de resolutie, en tekens die op elkaar lijken
  (8/B, 0/D, 1/7, 5/S), moeten aan de bronframes worden getoetst voordat u
  conclusies trekt.
- De winst is het grootst bij veel frames, kleine verschuivingen daartussen,
  onafhankelijke ruis en een voldoende scherpe referentie. Bewegingsonscherpte
  binnen één frame wordt niet verwijderd.
- Sterke compressie veroorzaakt fouten die in opeenvolgende frames gelijk
  zijn: de fusie vermindert die minder dan willekeurige ruis.
- Kentekens en gezichten zijn persoonsgegevens: gebruik het programma binnen
  de regels die op u van toepassing zijn.

## 9. Sneltoetsen

| Toetsen | Actie |
| --- | --- |
| Ctrl+1 / Ctrl+2 / Ctrl+3 | Pagina Configuratie / Onderwerp / Fusie |
| Ctrl+O | Video openen |
| ← / → | Vorig / volgend frame |
| Shift+← / Shift+→ | 10 frames terug / vooruit |
| Home / End | Eerste / laatste frame |
| I / O | Begin / einde van het bereik op de cursor |
| + / − | Tijdlijn inzoomen / uitzoomen |
| F | Hele video op de tijdlijn |
| Rechts slepen in het voorbeeld | Onderwerpgebied selecteren (de fusie start) |
| Esc | *Gebied selecteren* verlaten |
| F5 | De fusie starten |
| Ctrl+S | Het resultaat (pagina Fusie) of het frame (pagina Onderwerp) opslaan |


*Schermafbeeldingen: video ‘[Busy Highway Traffic at Sunset](https://www.pexels.com/video/busy-highway-traffic-at-sunset-31779728/)’ van [Şeyhmus Kino](https://www.pexels.com/@seyhmuskino/), via Pexels, gebruikt onder de [Pexels-licentie](https://www.pexels.com/license/). De kentekens in de schermafbeeldingen komen uit die video.*

---

FrameFusion is vrije software onder de GNU GPL v3 met naamsvermelding van de
auteur: zie `LICENSE` en `NOTICE`. Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net
