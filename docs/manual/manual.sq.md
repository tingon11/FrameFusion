# FrameFusion — Manuali i përdoruesit

[English](manual.en.md) · [Italiano](manual.it.md) · [Deutsch](manual.de.md) · [Français](manual.fr.md) · [Español](manual.es.md) · [Nederlands](manual.nl.md) · [Polski](manual.pl.md) · [Ελληνικά](manual.el.md) · **Shqip**

FrameFusion përmirëson lexueshmërinë e një detaji të vogël — një targe, një
fytyre, një tabele — të filmuar në disa kuadro të një videoje. Ai i rreshton
këto kuadro me saktësi nënpiksel, i shkrin në një rrjetë më të imët, redukton
zhurmën dhe turbullirën, dhe prodhon **një imazh të vetëm** me një raport që
dokumenton çdo parametër dhe çdo hap.

*Andrea Cumini — www.osintinfo.net — andrea@osintinfo.net*

## Përmbajtja

1. [Si funksionon](#1-si-funksionon)
2. [Instalimi dhe nisja e parë](#2-instalimi-dhe-nisja-e-parë)
3. [Faqja Konfigurimi](#3-faqja-konfigurimi)
4. [Faqja Subjekti: kuadrot, subjekti dhe referenca](#4-faqja-subjekti-kuadrot-subjekti-dhe-referenca)
5. [Faqja Shkrirja](#5-faqja-shkrirja)
6. [Ruajtja: imazhet dhe raporti](#6-ruajtja-imazhet-dhe-raporti)
7. [Si të nxirrni maksimumin nga një targë ose një fytyrë](#7-si-të-nxirrni-maksimumin-nga-një-targë-ose-një-fytyrë)
8. [Kufizimet dhe përdorimi i duhur](#8-kufizimet-dhe-përdorimi-i-duhur)
9. [Shkurtoret e tastierës](#9-shkurtoret-e-tastierës)

## 1. Si funksionon

Çdo kuadër i një videoje e regjistron subjektin në një pozicion paksa të
ndryshëm në raport me rrjetën e pikselëve, dhe me zhurmën e vet të
rastësishme. FrameFusion e shfrytëzon këtë: e gjen subjektin në çdo kuadër, i
rreshton të gjitha kuadrot me saktësi nënpiksel me një kuadër të vetëm,
**kuadrin e referencës**, dhe i kombinon. Zhurma ulet dhe rikthehet një pjesë
e detajeve që humb secili kuadër më vete. Asgjë nuk shpiket: rezultati përmban
vetëm atë që e mbështetin kuadrot.

Puna kryhet në shtatë hapa, të shfaqur në kutinë *Pipeline*:

| Hapi | Çfarë ndodh |
| --- | --- |
| 1. Nxjerrja e kuadrove | Intervali i zgjedhur dekodohet nga FFmpeg, i saktë deri në kuadër. |
| 2. Zbulimi i subjektit | Subjekti ndiqet kuadër pas kuadri, përpara dhe prapa nga referenca. |
| 3. Rreshtimi lokal | Çdo kuadër rreshtohet me referencën (algoritmi ECC; model zhvendosjeje, rrotullimi, afin ose perspektive). |
| 4. Regjistrimi nënpiksel | Rreshtimi rafinohet me rezolucion të plotë; zgjidhen kuadrot më të mprehta dhe të rreshtuara më mirë. |
| 5. Shkrirja me shumë kuadro | Kuadrot rikampionohen në një rrjetë deri në 4 herë më të imët dhe kombinohen, duke përjashtuar vlerat anomale. |
| 6. Dekonvolucioni dhe reduktimi i zhurmës | Nivele automatike, reduktim opsional i zhurmës dhe dekonvolucion Richardson-Lucy mbi luminancën. |
| 7. Kuadër i vetëm | Imazhi përfundimtar, fantazma e kuadrove, krahasimi me referencën, të dhënat për raportin. |

## 2. Instalimi dhe nisja e parë

**Skedari i ekzekutueshëm (Windows 10/11, 64-bit).** Shpaketojeni
`FrameFusion-<versioni>-windows-x64.zip` në çfarëdo dosje dhe nisni
`FrameFusion.exe`. Python nuk nevojitet. Skedari i ekzekutueshëm nuk është i
nënshkruar: herën e parë, Windows SmartScreen mund të kërkojë konfirmim.

**Nga kodi burimor.** Me Python 3.10 ose më të ri:

```bash
python -m pip install -r requirements.txt
python FrameFusion.py
```

**FFmpeg.** FrameFusion përdor FFmpeg për të lexuar videot, por nuk e
përfshin. Në nisjen e parë, nëse FFmpeg mungon, faqja **Konfigurimi** hapet te
kutia *FFmpeg*: **Shkarko / Përditëso** merr versionin zyrtar për Windows në
dosjen `tools\ffmpeg` pranë programit. Asgjë nuk instalohet në sistem.

Një video mund të hapet edhe nga rreshti i komandave:
`FrameFusion.exe video.mp4`.

## 3. Faqja Konfigurimi

![Faqja Konfigurimi](images/sq/01_configuration.png)

- **Burimi** — **Hap video…** (ose Ctrl+O, ose ikona e dosjes në kutinë
  *VIDEO* lart). Këtu shfaqen kohëzgjatja, numri i kuadrove, rezolucioni dhe
  kodeku. Kur hapet një video, programi kalon te faqja *Subjekti*.
- **Dalja** — *Dosja e destinacionit* ku ruhen shkrirjet (bosh = pranë
  videos), *Nëndosje me emrin e videos*, *Formati* (PNG ose TIFF) dhe
  *Thellësia e ngjyrës* (*Auto* = 16 bit për kanal për shkrirjen). *Ruaj
  edhe çdo kuadër të rreshtuar (dosja aligned/)* shton dosjen `aligned/` me
  çdo kuadër të përdorur, të rreshtuar me referencën.
- **FFmpeg** — ku ndodhet FFmpeg dhe cili është versioni i tij: **Kontrollo**,
  **Kontrollo për përditësime**, **Shkarko / Përditëso**.
- **Gjuha** — ndërfaqja dhe raportet janë të disponueshme në nëntë gjuhë:
  EN, IT, DE, FR, ES, NL, PL, EL, SQ. Ndryshimi është i menjëhershëm dhe
  ruhet.
- **Kredite** — autori dhe licenca.

## 4. Faqja Subjekti: kuadrot, subjekti dhe referenca

![Faqja Subjekti](images/sq/02_subject.png)

*Parapamja* shfaq kuadrin nën kursor: **rrotulla** zmadhon rreth treguesit të
miut (deri te pikselët realë), **zvarritja** lëviz pamjen, një **klik i
dyfishtë** e përshtat përsëri kuadrin. Poshtë, butonat lëvizin me një ose
dhjetë kuadro; **← →** dhe **Shift+← →** bëjnë të njëjtën gjë nga tastiera.

Kutia *Timeline* (vija kohore) shfaq të gjithë videon si një shirit filmi.
**Ctrl+rrotull** zmadhon, **rrotulla** rrëshqet; klikimi ose zvarritja
lëviz kursorin. *E gjitha* dhe *Përzgjedhja* përshtatin pamjen.

**1. Zgjidhni kuadrin e referencës.** Shkoni te kuadri në të cilin subjekti
është **më i madh dhe më i mprehtë** — për një automjet që afrohet, zakonisht
një nga kuadrot e fundit në të cilat e gjithë targa është ende e dukshme.

**2. Zgjidhni zonën e subjektit.** Zvarritni me **butonin e djathtë të miut**
mbi targë ose mbi fytyrë, ose shtypni **Zgjidh zonën** dhe zvarritni me
butonin e majtë. Rrethojeni subjektin duke lënë pak hapësirë rreth tij.
Kuadri i shfaqur bëhet **referenca** (shenja **R** në vijën kohore, **→ R** e
kthen kursorin tek ai) dhe **shkrirja nis vetë**: programi kalon te faqja
*Shkrirja*. Nëse vizatoni një zonë të re ndërsa shkrirja është në vazhdim, ajo
rinis. **Pastro** e heq zonën.

**3. Zgjidhni intervalin.** **Fillimi [I]** dhe **Fundi [O]** (tastet I dhe
O) vendosin kuadrin e parë dhe të fundit që do të përdoren: kuadrot në të
cilat subjekti është i dukshëm dhe i pambuluar. Shenjat I dhe O mund të
zvarriten gjithashtu, dhe fushat IN / OUT pranojnë një kohë (`1:23.456`) ose
një kuadër (`f2000`). Nëse, kur vizatohet zona, intervali është ende e gjithë
videoja, ai vendoset në 30 kuadro para dhe pas referencës. Pas ndryshimit të
intervalit, **Shkrij kuadrot →** (ose F5) e nis përsëri shkrirjen. Më së
shumti 300 kuadro për shkrirje.

## 5. Faqja Shkrirja

![Faqja Shkrirja: fantazma dhe rezultati](images/sq/03_fusion_ghost.png)

**Krahasimi.** Majtas, **Fantazma e kuadrove**: të gjitha kuadrot e
përdorura, të mbivendosura në pozicionin ku u gjet secili, para rreshtimit.
Ajo tregon se çfarë hyn në shkrirje dhe sa lëviz subjekti. Nëse zgjidhni te
menyja sipër saj zërin **Kuadri i referencës**, pamja e majtë shfaq në vend
të fantazmës kuadrin e referencës, të zmadhuar me interpolim bikubik: ky
është imazhi «para» i paanshëm për krahasim. Djathtas, rezultati: **Përfundimtar**,
ose **Vetëm shkrirja** (para reduktimit të zhurmës dhe dekonvolucionit). Dy
pamjet zmadhohen dhe lëvizin bashkë.

![Faqja Shkrirja: referenca dhe rezultati](images/sq/04_fusion_reference.png)

**Pipeline.** Shtatë hapat me përfundimin dhe kohën e tyre; poshtë,
përmbledhja (kuadrot e përdorura, zmadhimi, zhurma para dhe pas shkrirjes),
shiriti i progresit dhe butonat **Hap dosjen**, **Anulo**, **Ruaj
rezultatin**, **Nis shkrirjen**. Hapat 1–4 varen vetëm nga videoja,
intervali, referenca, zona dhe modeli i lëvizjes: kur ndryshojnë vetëm
parametrat e shkrirjes ose të restaurimit, ata ripërdoren dhe një shkrirje e
re zgjat vetëm një pjesë të sekondës (*i ripërdorur* në listën e hapave).

### Parametrat

Kolona majtas i grupon parametrat sipas hapave.

**Cilësime të ruajtura.** Grupe parametrash me emër: **Ruaj…** kërkon një
emër dhe ruan parametrat aktualë; zgjedhja e një emri në meny i ngarkon ata;
**Fshi** heq grupin e zgjedhur; **Parazgjedhjet** e kthen çdo parametër në
vlerën e parazgjedhur. **Nga raporti…** ngarkon parametrat nga skedari
`report.json` i një shkrirjeje të ruajtur më parë, për ta përsëritur saktësisht. Parametrat
në përdorim ruhen gjithashtu kur programi mbyllet.

| Kutia | Parametri | Efekti |
| --- | --- | --- |
| Kuadrot dhe rreshtimi | Modeli i lëvizjes | Zhvendosje, Rrotullim + zhvendosje, Afin, **Perspektivë (homografi)** — e parazgjedhur; ndjek një subjekt që afrohet, largohet ose kthehet. Nëse një kuadër nuk konvergon, provohet një model më i thjeshtë. |
| | Kërkimi i subjektit: korrelacioni minimal | Nën këtë vlerë subjekti konsiderohet i pagjetur në një kuadër. |
| | Cilësia minimale e rreshtimit (ECC) | Kuadrot e rreshtuara më keq se kjo vlerë përjashtohen (0.80 si parazgjedhje). |
| | Kuadrot më të mprehta që mbahen | 75 % si parazgjedhje: çereku më pak i mprehtë (turbullira nga lëvizja) përjashtohet. |
| Shkrirja | Zmadhimi | Nga × 1 (vetëm reduktim i zhurmës) deri në × 4. × 2 ose × 3 është zakonisht zgjedhja e duhur. |
| | Metoda e shkrirjes | **Mesatare e qëndrueshme (vlerat anomale përjashtohen)** — e parazgjedhur; Mediana; Zhvendosje dhe mbledhje (konvolucion i normalizuar). |
| | Pesho sipas mprehtësisë | Kuadrot më të mprehta kanë shumë më tepër peshë. |
| | Barazo ndriçimin | Kompenson ndryshimet e ekspozimit midis kuadrove. |
| Restaurimi | Reduktimi i zhurmës | Asnjë, E lehtë, Mesatare, E fortë (filtër bilateral). |
| | Iteracionet e dekonvolucionit | Richardson-Lucy: më shumë iteracione mprehin më shumë, por përforcojnë edhe zhurmën dhe aureolat. 20 si parazgjedhje. |
| | PSF σ (piksel të daljes) | Gjerësia e turbullirës që duhet hequr. *Automatike* e mat atë në skajet e imazhit të shkrirë. |
| | Rregullarizimi (variacioni total) | E frenon zhurmën gjatë dekonvolucionit. Mesatare si parazgjedhje. |
| Paraqitja | Nivele automatike | E zeza dhe e bardha në përqindëset 0,5 dhe 99,5 të luminancës, para dekonvolucionit. |
| | Kontrast lokal (CLAHE) | Barazim sipas zonave: i dobishëm për targat në hije ose kundër dritës. |
| | Shkallë gri | Heq ngjyrën: shpesh jep një imazh më të pastër për leximin e shkronjave. |

## 6. Ruajtja: imazhet dhe raporti

**Ruaj rezultatin** (Ctrl+S në faqen *Shkrirja*) krijon një dosje të re
`fusion_f<referenca>_<data-ora>` në dosjen e destinacionit, me:

| Skedari | Përmbajtja |
| --- | --- |
| `result.png` | imazhi përfundimtar |
| `fused.png` | shkrirja para reduktimit të zhurmës dhe dekonvolucionit |
| `ghost.png` | fantazma e kuadrove të përdorura |
| `reference_x<k>.png` | zona e referencës e zmadhuar me interpolim bikubik, për krahasim |
| `reference_crop.png` | e njëjta zonë me rezolucionin e videos |
| `report.pdf` | raporti i faqosur në A4, me imazhet |
| `report.txt` | i njëjti raport si tekst i thjeshtë |
| `report.json` | të njëjtat të dhëna në formë të strukturuar, përfshirë cilësimet (**Nga raporti…** i ringarkon) |
| `aligned/` | sipas kërkesës, çdo kuadër i përdorur, i rreshtuar me referencën |

![Faqja e parë e raportit PDF](images/sq/05_report.png)

Raporti shkruhet në gjuhën e ndërfaqes. Ai përmban burimin (shtegun,
madhësinë, gjurmën **SHA-256**, formatin), intervalin, kuadrin e referencës
dhe zonën, të gjithë parametrat, shtatë hapat me metodat e përdorura dhe
kohët e tyre, tabelën e kuadrove (vlerësimi i kërkimit, koeficientët e
rreshtimit, zhvendosja nënpiksel, mprehtësia, pesha, arsyeja e përjashtimit),
vlerësimet e zhurmës dhe SHA-256 të çdo imazhi të shkruar. Kushdo që e lexon
mund ta përsërisë përpunimin dhe të verifikojë që skedarët nuk kanë ndryshuar.

*Ruaj kuadrin* në faqen *Subjekti* ruan, përkundrazi, vetëm kuadrin nën
kursor, me rezolucion të plotë dhe pa humbje.

## 7. Si të nxirrni maksimumin nga një targë ose një fytyrë

- **Referenca**: kuadri në të cilin subjekti është më i madh dhe më i mprehtë.
- **Intervali**: vetëm kuadrot në të cilat subjekti është plotësisht i
  dukshëm. Kuadrot larg referencës (shumë më të vogla, me perspektivë tjetër)
  sjellin pak dhe gjithsesi shpesh përjashtohen nga pragu i cilësisë.
- **Zona**: e gjithë targa ose fytyra me pak hapësirë rreth saj; jo shumë
  sfond, i cili mund të lëvizë ndryshe.
- **Zmadhimi**: × 2 ose × 3. × 4 ia vlen vetëm me shumë kuadro.
- **Shkronjat janë ende të turbullta?** Ngrini *PSF σ* me një nivel (p.sh. nga
  *Automatike* te vlera e parë mbi atë që tregohet në raport), ose parametrin
  *Iteracionet e dekonvolucionit*.
- **Aureola ose «ringing» rreth shkronjave?** Ulni *PSF σ* ose iteracionet,
  ose ngrini parametrin *Rregullarizimi (variacioni total)*.
- **Targë në hije ose kundër dritës**: *Kontrast lokal (CLAHE)* në nivelin
  *E lehtë* ose *Mesatare*, shpesh së bashku me *Shkallë gri*.
- **Krahasoni** gjithmonë me pamjen *Kuadri i referencës*, duke zmadhuar mbi
  shkronjat: ajo që nuk lexohet aty dhe shfaqet vetëm pas një mprehjeje të
  fortë duhet trajtuar me kujdes.
- Një grup parametrash që funksionon për një kamerë ruajeni me **Ruaj…** dhe
  ripërdoreni.

## 8. Kufizimet dhe përdorimi i duhur

- Rezultati është një **përmirësim** i kuadrove të regjistruara, jo një
  rindërtim i realitetit: ai nuk mund të rikuperojë atë që nuk e përmban
  asnjë kuadër.
- Detajet e imëta në kufirin e rezolucionit, dhe shkronjat që ngjajnë me
  njëra-tjetrën (8/B, 0/D, 1/7, 5/S), duhet të verifikohen mbi kuadrot
  burimore para se të nxirren përfundime.
- Përfitimi është më i madh me shumë kuadro, zhvendosje të vogla midis tyre,
  zhurmë të pavarur dhe një referencë mjaftueshëm të mprehtë. Turbullira nga
  lëvizja brenda një kuadri të vetëm nuk hiqet.
- Ngjeshja e fortë prodhon gabime që janë të njëjta në kuadro të
  njëpasnjëshme: shkrirja i redukton ato më pak se zhurmën e rastësishme.
- Targat dhe fytyrat janë të dhëna personale: përdoreni programin brenda
  rregullave që zbatohen për ju.

## 9. Shkurtoret e tastierës

| Tastet | Veprimi |
| --- | --- |
| Ctrl+1 / Ctrl+2 / Ctrl+3 | Faqja Konfigurimi / Subjekti / Shkrirja |
| Ctrl+O | Hap video |
| ← / → | Kuadri i mëparshëm / kuadri tjetër |
| Shift+← / Shift+→ | 10 kuadro prapa / përpara |
| Home / End | Kuadri i parë / i fundit |
| I / O | Fillimi / fundi i intervalit te kursori |
| + / − | Zmadho / zvogëlo vijën kohore |
| F | E gjithë videoja në vijën kohore |
| Zvarritje me të djathtën mbi parapamje | Zgjidh zonën e subjektit (shkrirja nis) |
| Esc | Dil nga mënyra *Zgjidh zonën* |
| F5 | Nis shkrirjen |
| Ctrl+S | Ruaj rezultatin (faqja Shkrirja) ose kuadrin (faqja Subjekti) |


*Pamjet e ekranit: videoja «[Busy Highway Traffic at Sunset](https://www.pexels.com/video/busy-highway-traffic-at-sunset-31779728/)» nga [Şeyhmus Kino](https://www.pexels.com/@seyhmuskino/), nga Pexels, e përdorur sipas [licencës së Pexels](https://www.pexels.com/license/). Targat që duken në pamjet e ekranit janë nga ajo video.*

---

FrameFusion është program i lirë nën GNU GPL v3 me atribuim të autorit:
shihni `LICENSE` dhe `NOTICE`. Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net
