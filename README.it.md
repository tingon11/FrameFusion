# FrameFusion

[English](README.md) · **Italiano**

Migliora la leggibilità di un dettaglio piccolo — una targa, un volto, una
scritta — ripreso in più fotogrammi di un video. FrameFusion allinea quei
fotogrammi con precisione sub-pixel, li fonde su una griglia più fine, riduce
rumore e sfocatura e produce **un'unica immagine**, insieme a un rapporto che
documenta ogni parametro e ogni passaggio.

**Autore: Andrea Cumini — [www.osintinfo.net](https://www.osintinfo.net) — andrea@osintinfo.net**

**Manuale d'uso, con screenshot:** [English](docs/manual/manual.en.md) · [Italiano](docs/manual/manual.it.md) · [Deutsch](docs/manual/manual.de.md) · [Français](docs/manual/manual.fr.md) · [Español](docs/manual/manual.es.md) · [Nederlands](docs/manual/manual.nl.md) · [Polski](docs/manual/manual.pl.md) · [Ελληνικά](docs/manual/manual.el.md) · [Shqip](docs/manual/manual.sq.md)

La tecnica si chiama **super-risoluzione multi-frame** (o multi-frame image
enhancement). Ogni fotogramma campiona il soggetto in una posizione
leggermente diversa rispetto alla griglia dei pixel e porta un rumore
indipendente: combinati dopo un allineamento preciso, i fotogrammi danno
un'immagine più pulita e con più del dettaglio realmente registrato. Nulla
viene inventato: il risultato contiene solo ciò che i fotogrammi sostengono.

L'interfaccia è scritta in Python con **customtkinter**, nello stesso stile di
AndrOsint, TagFaces e VideoSlicer (il tema scuro Seity), da cui FrameFusion
deriva. La decodifica è di **ffmpeg**, eseguito come programma separato;
l'elaborazione delle immagini usa **OpenCV** e **NumPy**.

## La pipeline

| Passaggio | Che cosa succede |
| --- | --- |
| 1. Estrazione dei fotogrammi | L'intervallo scelto viene decodificato da ffmpeg, esatto al fotogramma (una passata ridotta in grigio per cercare il soggetto, poi una a piena risoluzione che tiene solo l'area attorno a lui). Le sorgenti a 10 bit e oltre si leggono a 16 bit. |
| 2. Rilevamento del soggetto | Il soggetto, inquadrato sul **fotogramma di riferimento**, viene seguito fotogramma per fotogramma, in avanti e all'indietro, per correlazione incrociata normalizzata con previsione del moto. I fotogrammi in cui si perde vengono scartati. |
| 3. Allineamento locale | Ogni fotogramma viene allineato al riferimento con l'algoritmo **ECC** (Evangelidis & Psarakis, 2008) su immagini smussate e ridotte: modello a traslazione, rotazione, affine o **prospettico** (omografia), così un veicolo che si avvicina o gira viene compensato. Se il modello scelto non converge su un fotogramma, si prova uno più semplice (scritto nel rapporto). |
| 4. Registrazione sub-pixel | ECC viene raffinato a piena risoluzione. Poi si scelgono i fotogrammi più utili: allineamento affidabile (coefficiente ECC) e maggiore nitidezza (energia del laplaciano sull'area allineata). |
| 5. Fusione multi-frame | I fotogrammi scelti vengono ricampionati su una griglia da 1 a 4 volte più fine del riferimento e combinati: **media robusta** (pesata, con scarto pixel per pixel dei valori anomali: riflessi, occlusioni, artefatti di compressione), **mediana**, oppure **somma con spostamento** dei singoli campioni con convoluzione normalizzata. I pesi seguono qualità dell'allineamento e nitidezza; la luminosità può essere uniformata a quella del riferimento. |
| 6. Deconvoluzione e riduzione del rumore | Prima i livelli automatici (nero e bianco ai percentili 0,5 e 99,5 della luminanza), poi, sulla **sola luminanza** (nel video compresso il colore è a metà risoluzione e porta rumore, non dettaglio: viene solo smussato): filtro bilaterale facoltativo e deconvoluzione di **Richardson-Lucy** con una PSF gaussiana la cui ampiezza è **misurata sui bordi dell'immagine fusa** (o scelta), un numero limitato di iterazioni e **regolarizzazione a variazione totale** (Dey et al., 2006), che frena il rumore. |
| 7. Fotogramma unico | Presentazione (contrasto locale, scala di grigi, documentati), l'immagine finale, il **ghost** (ogni fotogramma usato, sovrapposto nella posizione in cui è stato trovato) e il fotogramma di riferimento ingrandito con interpolazione bicubica, per il confronto. |

I passaggi 1-4 dipendono solo da video, intervallo, riferimento, area e
modello di moto: il loro esito viene conservato, e cambiando i parametri di
fusione e restauro si rifanno solo i passaggi 5-7, in una frazione di secondo.

## Requisiti

- Windows 10/11 (sugli altri sistemi funziona con la barra del titolo standard)
- Python 3.10 o successivo (con Tkinter, incluso nell'installer ufficiale)
- ffmpeg, come programma **separato**: FrameFusion lo scarica nella cartella
  `tools/ffmpeg/` accanto al programma (vedi *FFmpeg* più sotto); viene usato
  anche un ffmpeg già presente nel PATH

Dipendenze Python (`requirements.txt`): `customtkinter`, `pillow`, `numpy`,
`opencv-python-headless` (4.8 o successivo; va bene anche la 5.x) e `fpdf2`
(rapporto PDF).

```bash
python -m pip install -r requirements.txt
```

## Avvio

```bash
python FrameFusion.py
```

Oppure doppio clic su `Avvia.bat` (parte senza finestra console e usa il
virtualenv `.venv` se c'è). Il video da aprire si può passare come
argomento: `python FrameFusion.py filmato.mp4`.

## Uso

L'interfaccia ha tre pagine, nella barra laterale (Ctrl+1 / 2 / 3).

1. **Configurazione** — apri il video (**Apri video…**, Ctrl+O, o l'icona nel
   riquadro VIDEO in alto), scegli la cartella di destinazione e il formato
   delle immagini (PNG o TIFF, 16 bit per canale di base), scarica ffmpeg se
   manca, scegli la lingua.
2. **Soggetto** — anteprima e timeline, come in VideoSlicer:
   - porta il cursore su un fotogramma in cui il soggetto è il più nitido
     possibile e **inquadralo**: trascina col **tasto destro** sull'anteprima,
     oppure premi **Seleziona area** e trascina col sinistro. Quel fotogramma
     diventa il **riferimento** (segnaposto **R** sulla timeline) e la fusione
     **parte da sola**; disegnare un'area nuova mentre gira la fa ripartire;
   - scegli l'intervallo con **Inizio [I]** / **Fine [O]** (o trascinando le
     bandierine I e O): i fotogrammi in cui il soggetto è visibile. Ogni
     volta che disegni l'area, l'intervallo viene impostato a 150 fotogrammi
     prima e 150 dopo il riferimento (dentro il video). **Fondi fotogrammi →**
     (o F5) rifà la pipeline dopo aver cambiato l'intervallo.
3. **Fusione** — parametri a sinistra, confronto a destra: a sinistra il
   **ghost** dei fotogrammi usati (tutti sovrapposti, ciascuno nella posizione
   in cui è stato trovato) oppure il fotogramma di riferimento ingrandito con
   interpolazione bicubica; a destra il risultato (o la fusione prima del
   restauro). Si ingrandisce con la rotellina e si sposta trascinando: le due
   viste si muovono insieme. Sotto, i sette passaggi con esito e tempi.
   **Avvia fusione** la ripete con parametri nuovi, **Salva risultato**
   (Ctrl+S) scrive immagini e rapporto.

### Impostazioni salvate

Il riquadro *Impostazioni salvate* in cima alla colonna dei parametri tiene
insiemi di parametri con un nome: **Salva…** chiede un nome e scrive subito i
parametri correnti in `config.json`; scegliendo un nome nel menu si caricano;
**Elimina** toglie l'insieme scelto; **Predefiniti** riporta ogni parametro
al suo valore di base. **Da rapporto…** carica i parametri scritti nel
`report.json` di una fusione salvata in precedenza, così un'elaborazione si
può ripetere esattamente. I parametri in uso vengono comunque salvati da soli
alla chiusura del programma.

### Parametri

| Parametro | Effetto |
| --- | --- |
| Modello di moto | Traslazione, rotazione + traslazione, affine, prospettiva (predefinito). La prospettiva segue un soggetto che si avvicina, si allontana o gira. |
| Ricerca del soggetto: correlazione minima | Sotto questo punteggio il soggetto conta come non trovato in quel fotogramma. |
| Qualità minima dell'allineamento (ECC) | I fotogrammi allineati con un coefficiente più basso vengono scartati (0,80 di base). |
| Fotogrammi più nitidi tenuti | 75 % di base: il quarto meno nitido (mosso, fotogrammi lontani dal riferimento) resta fuori; 100 % tiene tutti quelli ben allineati. |
| Ingrandimento | Da ×1 (solo riduzione del rumore) a ×4. Di solito ×2 o ×3 è la scelta giusta: il guadagno dipende da quanti fotogrammi ci sono e da come sono spostati. |
| Metodo di fusione | Media robusta (predefinita), somma con spostamento con convoluzione normalizzata, mediana. |
| Pesa per nitidezza / Uniforma la luminosità | I fotogrammi più nitidi contano molto di più (quarta potenza della nitidezza relativa); i cambi di esposizione vengono compensati. |
| Riduzione del rumore | Nessuna, leggera, media, forte (filtro bilaterale, proporzionale al rumore stimato). |
| Iterazioni di deconvoluzione / PSF σ | Richardson-Lucy: più iterazioni rendono più nitido ma amplificano anche rumore e aloni. La PSF automatica è misurata sui bordi più netti dell'immagine fusa (ampiezza / pendenza massima): circa 0,8–1 px del video nelle riprese da telefono. Alzala se i caratteri restano morbidi, abbassala se compaiono aloni. |
| Regolarizzazione (variazione totale) | Nessuna, leggera, media (predefinita), forte: frena il rumore durante la deconvoluzione, così si possono usare più iterazioni. |
| Livelli automatici | Stira la luminanza in modo che i percentili 0,5 e 99,5 diventino nero e bianco (stessa retta su ogni canale: i colori non cambiano), prima della deconvoluzione. Accesi di base. |
| Contrasto locale (CLAHE) | Nessuno, leggero, medio, forte: equalizzazione a zone sulla luminanza. Utile su targhe in ombra o in controluce. |
| Scala di grigi | Toglie il colore: spesso più pulito per leggere i caratteri. |

## Uscita e rapporto

**Salva risultato** crea una cartella nuova `fusion_f<riferimento>_<data-ora>`
nella cartella di destinazione (in una sottocartella con il nome del video,
se scelto; accanto al video se non è impostata una cartella) con:

| File | Contenuto |
| --- | --- |
| `result.png` | l'immagine finale |
| `fused.png` | la fusione prima di riduzione del rumore e deconvoluzione |
| `ghost.png` | ogni fotogramma usato, sovrapposto nella posizione in cui è stato trovato |
| `reference_x<k>.png` | l'area del fotogramma di riferimento ingrandita con interpolazione bicubica, per il confronto |
| `reference_crop.png` | la stessa area alla risoluzione del video |
| `aligned/` | a richiesta, ogni fotogramma usato, allineato sulla griglia del riferimento |
| `report.txt` | rapporto leggibile, nella lingua dell'interfaccia |
| `report.pdf` | lo stesso rapporto impaginato in A4 con le immagini (riferimento, risultato, ghost, fusione), la tabella dei fotogrammi e le impronte SHA-256; i caratteri sono presi dal sistema (Segoe UI e Consolas su Windows) |
| `report.json` | gli stessi dati in forma strutturata, comprese le impostazioni così come le usa il programma (**Da rapporto…** le ricarica) |

Il rapporto contiene la sorgente (percorso, dimensione, **SHA-256**,
formato), l'intervallo, il fotogramma di riferimento, l'area, tutti i
parametri, i sette passaggi con i metodi usati e i tempi, la tabella dei
fotogrammi (punteggio della ricerca, coefficienti ECC, spostamento
sub-pixel, nitidezza, peso, motivo dell'esclusione, matrice di allineamento
nel JSON), le stime del rumore, la densità dei campioni, le fasi sub-pixel
coperte e lo SHA-256 di ogni immagine scritta. Chi lo legge può ripetere
l'elaborazione.

## Limiti

- Il risultato è un **miglioramento** dei fotogrammi registrati, non una
  ricostruzione della realtà: non può recuperare ciò che nessun fotogramma
  contiene. I dettagli fini al limite della risoluzione, e i caratteri che si
  somigliano (8/B, 0/D, 1/7), vanno verificati sui fotogrammi originali.
- Il guadagno è maggiore con molti fotogrammi, piccoli spostamenti tra loro,
  rumore indipendente e un riferimento abbastanza nitido. Il mosso dentro il
  singolo fotogramma non viene tolto dalla fusione.
- Una compressione forte (blocchi, impastamento) produce errori uguali in
  fotogrammi consecutivi: la fusione li riduce meno del rumore casuale.
- Al massimo 301 fotogrammi per fusione; le aree molto grandi si elaborano
  su un numero ridotto di fotogrammi (scritto nel rapporto).

## Eseguibile unico

```bash
.venv\Scripts\python.exe scripts\build_exe.py
```

installa PyInstaller nel virtualenv se manca e scrive `dist\FrameFusion.exe`
(un solo file, senza finestra console, icona «FF» e proprietà del file).
ffmpeg resta fuori di proposito: l'eseguibile lo cerca in `tools\ffmpeg\`
accanto a sé e propone di scaricarlo.

`--release` scrive anche `dist\FrameFusion-<versione>-windows-x64.zip` (exe,
LICENSE, NOTICE, README e una cartella `licenses` con i file di licenza di
Python e delle librerie contenute nell'eseguibile, presi dal virtualenv) e
`dist\release-notes-<versione>.md`, con le novità prese dalla sezione più
recente di `CHANGELOG.md`; `--publish` crea la release GitHub `v<versione>`
sul repository del remote `origin` (token da `GITHUB_TOKEN` o chiesto al
momento, mai salvato). Prima di una nuova release alza `__version__` in
`framefusion/__init__.py` e aggiungi una sezione a `CHANGELOG.md`.

## FFmpeg

ffmpeg non è incluso: è un programma separato con la propria licenza. Al
primo avvio, se non trova ffmpeg, si apre la pagina **Configurazione** sul
riquadro *FFmpeg*: **Scarica / Aggiorna** prende il build ufficiale per
Windows ("release essentials") da <https://www.gyan.dev/ffmpeg/builds/>,
quello indicato dal sito di FFmpeg, e tiene solo `ffmpeg.exe`, `LICENSE` e
`README.txt` in `tools/ffmpeg/`. Nessuna installazione, nessuna modifica al
PATH. **Cerca aggiornamenti** confronta la release installata con l'ultima.

## Lingua

Interfaccia e rapporti sono in **inglese** (predefinito), **italiano**,
**tedesco**, **francese**, **spagnolo**, **olandese**, **polacco**, **greco**
o **albanese**. Si cambia con i pulsanti delle lingue nel riquadro *Lingua*
della pagina **Configurazione**: il cambio è immediato e viene salvato in
`config.json`. Ogni lingua è un modulo in `framefusion/locales/` (testo
inglese → traduzione); `scripts\check_i18n.py` controlla che ogni testo abbia
la sua traduzione in ogni lingua. Le traduzioni diverse dall'italiano sono
state prodotte con l'aiuto di un modello linguistico e non sono ancora state
riviste da madrelingua: le correzioni sono benvenute.

## Struttura

| File | Contenuto |
| --- | --- |
| `FrameFusion.py` | punto di ingresso |
| `framefusion/app.py` | finestra principale |
| `framefusion/fusion.py` | la pipeline: ricerca del soggetto, registrazione ECC, fusione, deconvoluzione |
| `framefusion/report.py`, `pdfreport.py` | salvataggio di immagini e rapporto (testo, JSON, PDF) |
| `framefusion/preview.py` | anteprima ingrandibile con area del soggetto e viste collegate |
| `framefusion/timeline.py` | timeline con anteprime, zoom, segnaposto e riferimento |
| `framefusion/ffmpeg.py` | informazioni sul video, anteprime, fotogrammi grezzi |
| `framefusion/tools.py` | ricerca, download e aggiornamento di ffmpeg in `tools/` |
| `framefusion/i18n.py`, `locales/` | lingua dell'interfaccia e i cataloghi delle traduzioni (un modulo per lingua) |
| `framefusion/theme.py`, `widgets.py`, `shell.py`, `frameless.py` | tema scuro, componenti, barra laterale, finestra senza barra |
| `framefusion/tasks.py`, `procs.py` | lavori in background; processi figli legati all'applicazione |
| `framefusion/config.py` | impostazioni in `config.json` |
| `scripts/build_exe.py` | compila `FrameFusion.exe`; `--release` zip e note; `--publish` release su GitHub |
| `scripts/check_i18n.py` | controlla la traduzione italiana |

## Licenza

GNU GPL v3 con termini aggiuntivi di attribuzione dell'autore: vedi
[LICENSE](LICENSE) e [NOTICE](NOTICE). La dicitura

    Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net

va mantenuta nei sorgenti, nell'interfaccia (piede della finestra e riquadro
Crediti) e nella documentazione. Il programma la scrive anche nei rapporti:
le versioni modificate possono conservarla, senza obbligo. Il nome
"FrameFusion", il logo e l'icona "FF" identificano il programma originale:
una versione modificata distribuita ad altri deve usare un nome e un logo
diversi.

ffmpeg è un programma separato con la propria licenza (LGPL/GPL): vedi
<https://ffmpeg.org/legal.html>. Python e le librerie contenute
nell'eseguibile (CustomTkinter, Pillow, NumPy, OpenCV, fpdf2 e le loro dipendenze)
restano sotto le proprie licenze: lo zip di release porta i loro file di
licenza nella cartella `licenses`.
