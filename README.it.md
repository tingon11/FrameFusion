# IdentiFrame

[English](README.md) · **Italiano**

Migliora la leggibilità di un dettaglio piccolo — una targa, un volto, una
scritta — ripreso in più fotogrammi di un video. IdentiFrame allinea quei
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

IdentiFrame è la continuazione, con un nome nuovo, di FrameFusion dello stesso
autore, con una modalità pensata per i volti e la lettura di targhe e
scritte. L'interfaccia è scritta in Python con **customtkinter**. La
decodifica è di **ffmpeg**, eseguito come programma separato; l'elaborazione
delle immagini usa **OpenCV** e **NumPy**.

## Il nome

Fino alla versione 1.0.1 IdentiFrame è stato pubblicato come **FrameFusion**.
Quel nome è già usato da un prodotto commerciale che fa lo stesso tipo di
lavoro: per evitare confusione il programma continua come IdentiFrame, con
nome, logo e icona nuovi. Codice, rapporti e impostazioni proseguono da
FrameFusion 1.0.1; le vecchie release restano disponibili in questo
repository, e i link al vecchio repository FrameFusion portano qui.

## La pipeline

| Passaggio | Che cosa succede |
| --- | --- |
| 1. Estrazione dei fotogrammi | L'intervallo scelto viene decodificato da ffmpeg, esatto al fotogramma (una passata ridotta in grigio per cercare il soggetto, poi una a piena risoluzione che tiene solo l'area attorno a lui). Le sorgenti a 10 bit e oltre si leggono a 16 bit. |
| 2. Rilevamento del soggetto | Il soggetto, inquadrato sul **fotogramma di riferimento**, viene seguito fotogramma per fotogramma, in avanti e all'indietro, per correlazione incrociata normalizzata con previsione del moto. I fotogrammi in cui si perde vengono scartati. |
| 3. Allineamento locale | Ogni fotogramma viene allineato al riferimento con l'algoritmo **ECC** (Evangelidis & Psarakis, 2008) su immagini smussate e ridotte: modello a traslazione, rotazione, affine o **prospettico** (omografia), così un veicolo che si avvicina o gira viene compensato. Se il modello scelto non converge su un fotogramma, o converge su una deformazione che non è un moto possibile del soggetto (scala locale, taglio o prospettiva oltre i limiti), si prova uno più semplice (scritto nel rapporto). Con il tipo di soggetto **Volto**, dopo il modello rigido ogni fotogramma riceve anche un **raffinamento locale non rigido** (flusso ottico di Farneback tra riferimento e fotogramma allineato, lisciato e limitato in ampiezza) che segue espressione e movimenti della testa, con una confidenza per pixel (coerenza avanti-indietro del flusso e correlazione locale). |
| 4. Registrazione sub-pixel | ECC viene raffinato a piena risoluzione. Poi si scelgono i fotogrammi più utili: allineamento affidabile (coefficiente ECC) e maggiore nitidezza (energia del laplaciano sull'area allineata). Con un volto, i fotogrammi la cui somiglianza locale col riferimento è troppo bassa (posa o espressione cambiate) restano fuori. |
| 5. Fusione multi-frame | I fotogrammi scelti vengono ricampionati su una griglia da 1 a 4 volte più fine del riferimento e combinati: **media robusta** (pesata, con scarto pixel per pixel dei valori anomali: riflessi, occlusioni, artefatti di compressione), **mediana**, oppure **somma con spostamento** dei singoli campioni con convoluzione normalizzata. I pesi seguono qualità dell'allineamento e nitidezza e, con un volto, la confidenza locale di ogni campione; la luminosità può essere uniformata a quella del riferimento. |
| 6. Deconvoluzione e riduzione del rumore | Prima i livelli automatici (nero e bianco ai percentili 0,5 e 99,5 della luminanza; 0,1 e 99,9 per un volto), poi, sulla **sola luminanza** (nel video compresso il colore è a metà risoluzione e porta rumore, non dettaglio: viene solo smussato): filtro bilaterale facoltativo e deconvoluzione di **Richardson-Lucy** con una PSF gaussiana la cui ampiezza è **misurata sui bordi dell'immagine fusa** (o scelta), un numero limitato di iterazioni e **regolarizzazione a variazione totale** (Dey et al., 2006), che frena il rumore. |
| 7. Fotogramma unico | Presentazione (contrasto locale, scala di grigi, documentati), l'immagine finale, il **ghost** (ogni fotogramma usato, sovrapposto nella posizione in cui è stato trovato) e il fotogramma di riferimento ingrandito con interpolazione bicubica, per il confronto. |

I passaggi 1-4 dipendono solo da video, intervallo, riferimento, area,
modello di moto e tipo di soggetto: il loro esito viene conservato, e
cambiando i parametri di fusione e restauro si rifanno solo i passaggi 5-7,
in una frazione di secondo.

## Requisiti

- Windows 10/11 (sugli altri sistemi funziona con la barra del titolo standard)
- Python 3.10 o successivo (con Tkinter, incluso nell'installer ufficiale)
- ffmpeg, come programma **separato**: IdentiFrame lo scarica nella cartella
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
python IdentiFrame.py
```

Oppure doppio clic su `Avvia.bat` (parte senza finestra console e usa il
virtualenv `.venv` se c'è). Il video da aprire si può passare come
argomento: `python IdentiFrame.py filmato.mp4`.

## Uso

L'interfaccia ha tre pagine, nella barra laterale (Ctrl+1 / 2 / 3).

A ogni avvio un avviso spiega la tecnica e chiede di confermare che il
risultato è una ricostruzione dai pixel reali dei fotogrammi, in cui nulla è
inventato, mentre la lettura dei caratteri e il paese sono stime da
verificare; al primissimo avvio viene chiesta prima la lingua.

1. **Configurazione** — apri il video (**Apri video…**, Ctrl+O, o l'icona nel
   riquadro VIDEO in alto), scegli la cartella di destinazione e il formato
   delle immagini (PNG o TIFF, 16 bit per canale di base), scarica ffmpeg se
   manca, scegli la lingua.
2. **Soggetto** — anteprima e timeline:
   - scegli il **tipo di soggetto** nel riquadro *Soggetto*: *Targa*,
     *Testo* oppure *Volto* (vedi *Tipo di soggetto* più sotto);
   - porta il cursore su un fotogramma in cui il soggetto è il più nitido
     possibile e **inquadralo**: trascina col **tasto destro** sull'anteprima,
     oppure premi **Seleziona area** e trascina col sinistro. Quel fotogramma
     diventa il **riferimento** (segnaposto **R** sulla timeline) e la fusione
     **parte da sola**; disegnare un'area nuova mentre gira la fa ripartire;
   - scegli l'intervallo con **Inizio [I]** / **Fine [O]** (o trascinando le
     bandierine I e O): i fotogrammi in cui il soggetto è visibile. Ogni
     volta che disegni l'area, l'intervallo viene impostato a 30 secondi
     prima e 30 dopo il riferimento (dentro il video), solo come limiti della
     ricerca: la fusione segue il soggetto dal riferimento verso l'esterno, si
     ferma in ciascun verso dopo un secondo senza vederlo e poi stringe Inizio
     e Fine sui fotogrammi in cui l'ha seguito. Un intervallo spostato a mano
     resta com'è. **Fondi fotogrammi →** (o F5) rifà la pipeline dopo aver
     cambiato l'intervallo.
3. **Fusione** — parametri a sinistra, confronto a destra: a sinistra il
   **ghost** dei fotogrammi usati (tutti sovrapposti, ciascuno nella posizione
   in cui è stato trovato) oppure il fotogramma di riferimento ingrandito con
   interpolazione bicubica; a destra il risultato (o la fusione prima del
   restauro). Si ingrandisce con la rotellina e si sposta trascinando: le due
   viste si muovono insieme. Sotto, i sette passaggi con esito e tempi.
   **Avvia fusione** la ripete con parametri nuovi, **Salva risultato**
   (Ctrl+S) scrive immagini e rapporto.

### Tipo di soggetto

Il menu accanto a **Seleziona area**, nella pagina **Soggetto**, dice che cosa
si sta migliorando. **Targa** e **Testo**: un soggetto piano e rigido,
descritto da un solo modello di moto per fotogramma; cambia la lettura dei
caratteri (fast-plate-ocr per le targhe, PaddleOCR per le scritte, vedi più
sotto). **Volto**: tra un fotogramma e l'altro
la testa gira e l'espressione cambia, quindi dopo l'allineamento rigido ogni
fotogramma riceve un raffinamento locale non rigido che segue questi
movimenti entro pochi pixel; le parti che restano diverse contano meno, i
fotogrammi con posa o espressione diverse restano fuori, il restauro è più
leggero (10 iterazioni, regolarizzazione forte, riduzione del rumore leggera,
per evitare aloni ed effetto «plastica» sulla pelle) e i livelli automatici
sono più prudenti su pelle e ombre. Cambiare tipo carica i suoi predefiniti e
rifà l'allineamento. Il rapporto scrive il tipo usato, somiglianza e
spostamento medi del raffinamento, una colonna di somiglianza nella tabella
dei fotogrammi e una nota sulla dimensione del volto nel video: sotto circa
60 pixel di larghezza la fusione può migliorare l'aspetto complessivo, non
far emergere tratti identificativi. Nulla di generativo: il raffinamento
sposta solo di pochi pixel ciò che i fotogrammi contengono. Per un volto il
modello di moto predefinito è **affine**: su un volto di poche decine di
pixel l'omografia si piega per far salire la correlazione, e la prospettiva
non è un moto reale della testa. Fuori dall'ellisse inscritta nell'area i
campioni contano poco e il risultato mostra il fotogramma di riferimento,
perché lo sfondo si muove in modo diverso dal volto.

### Impostazioni salvate

Il menu comincia sempre con cinque **preset di serie** per il tipo di
soggetto scelto nella pagina Soggetto, che non si possono modificare né
eliminare: **Plate 01** standard, **02** notte o rumore, **03** targa lontana
e piccola (×3, somma con spostamento), **04** veicolo in movimento con mosso,
**05** ombra o controluce; **Text 01–05** gli stessi casi per le scritte;
**Face 01** standard, **02** notte o rumore, **03**
elaborazione minima (senza riduzione del rumore né deconvoluzione), **04**
volto lontano e piccolo (×3), **05** ombra o controluce. Una riga sotto il
menu descrive quello scelto. Seguono le tue impostazioni.

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
| Tipo di soggetto (pagina Soggetto) | Targa (predefinito), Testo oppure Volto: vedi sopra. Cambiarlo carica i predefiniti di quel tipo. |
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

### Lettura dei caratteri (OCR)

Con i modelli OCR scaricati (vedi *Modelli OCR* più sotto), dopo ogni fusione
di una *Targa* o di un *Testo* la riga **CARATTERI** del riquadro *Pipeline*
mostra i caratteri letti; **Leggi caratteri** rifà la lettura. Su una targa
piccola nessun fotogramma da solo è leggibile da un OCR, quindi si leggono il
risultato e **otto fusioni di gruppi indipendenti di fotogrammi** (fotogrammi
alterni per nitidezza, ogni gruppo fuso e restaurato con gli stessi
parametri). Le letture vengono allineate alla più rappresentativa e votate
**carattere per carattere**, pesate per la probabilità che il modello dà a
ogni carattere (Quiala et al., 2023).

- **Targa**: [fast-plate-ocr](https://github.com/ankandrew/fast-plate-ocr)
  legge la targa intera (l'area, o il rettangolo chiaro della targa trovato
  al suo interno) e indica anche il **possibile paese** della targa, tra 65:
  una stima dall'aspetto della targa, non una verifica.
- **Testo**: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) PP-OCRv6
  trova le righe di testo nel risultato e legge ognuna, in molte lingue e
  alfabeti; ogni riga viene votata per conto suo.

La riga indica l'accordo tra le letture, la **fiducia del modello**
(probabilità media dei caratteri letti: letture concordi con fiducia bassa
sono di solito testo illeggibile letto sempre allo stesso modo), le posizioni
*dubbie* (accordo sotto il 70 %, o una forma simile come seconda scelta) e,
sulle targhe, i caratteri da **verificare a occhio** (8/B, 0/D/O, 1/I, 5/S,
2/Z, 6/G: un modello può sbagliarli allo stesso modo in ogni lettura, e il
voto non lo vede). Il rapporto riceve una sezione con la lettura, il voto per
posizione e le letture singole. Senza i modelli il programma funziona lo
stesso: manca solo la lettura dei caratteri.

I modelli propongono sempre i caratteri più probabili, anche dove non si
legge nulla: una riga si mostra solo da una fiducia del modello del 60 %,
altrimenti è **illeggibile**, e un carattere con meno del 50 % dei voti
pesati compare come **«?»**. Il paese compare in giallo accanto ai caratteri
solo su una lettura leggibile in cui un paese ha la maggioranza dei voti.
Lettura e paese restano stime: confronta sempre con l'immagine.

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
sub-pixel, nitidezza, peso prospettico del warp, peso, motivo
dell'esclusione, matrice di allineamento nel JSON), le stime del rumore, la densità dei campioni, le fasi sub-pixel
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
- Al massimo 3601 fotogrammi nell'intervallo; le aree molto grandi si elaborano
  su un numero ridotto di fotogrammi (scritto nel rapporto).

## Eseguibile unico

```bash
.venv\Scripts\python.exe scripts\build_exe.py
```

installa PyInstaller nel virtualenv se manca, scrive un file spec in `build\`
e compila `dist\IdentiFrame.exe` (un solo file, senza finestra console, icona
«IF» e proprietà del file). FFmpeg resta fuori di proposito, in ogni forma:
l'eseguibile cerca `ffmpeg.exe` in `tools\ffmpeg\` accanto a sé e propone di
scaricarlo, e la libreria FFmpeg che il pacchetto OpenCV porta con sé (LGPL,
usata solo dalla lettura video di OpenCV, che IdentiFrame non usa) viene
tolta dal bundle; il build controlla che sia assente.

`--release` scrive anche `dist\IdentiFrame-<versione>-windows-x64.zip` (exe,
LICENSE, NOTICE, README e una cartella `licenses` con i file di licenza di
Python e delle librerie contenute nell'eseguibile, presi dal virtualenv) e
`dist\release-notes-<versione>.md`, con le novità prese dalla sezione più
recente di `CHANGELOG.md`; `--publish` crea la release GitHub `<versione>`
sul repository del remote `origin` (token da `GITHUB_TOKEN` o chiesto al
momento, mai salvato). Prima di una nuova release alza `__version__` in
`identiframe/__init__.py` e aggiungi una sezione a `CHANGELOG.md`.

## Modelli OCR

La lettura dei caratteri usa due modelli di rete neurale in formato ONNX,
eseguiti da OpenCV (già nel programma). Sono facoltativi, non sono mai
inclusi nell'eseguibile e si scaricano a richiesta dal riquadro **Modelli
OCR** della pagina **Configurazione** in `tools/ocr/`, circa 37 MB in tutto.
Senza di loro IdentiFrame funziona normalmente: fusione, restauro e rapporti
non cambiano, manca solo la lettura dei caratteri.

| Cartella | Modello | Licenza | Provenienza |
| --- | --- | --- | --- |
| `tools/ocr/plate/` | fast-plate-ocr `cct-s-v2-global` con la sua configurazione | MIT (codice e pesi, confermato dall'autore nella [issue 97](https://github.com/ankandrew/fast-plate-ocr/issues/97)) | [release arg-plates](https://github.com/ankandrew/fast-plate-ocr/releases/tag/arg-plates) |
| `tools/ocr/text/` | PaddleOCR PP-OCRv6 small, rilevamento e lettura del testo, con l'elenco dei caratteri | Apache 2.0 (pesi di Baidu / PaddleOCR; conversione ONNX di RapidOCR, Apache 2.0) | [modelli di RapidOCR 3.10.0](https://www.modelscope.cn/models/RapidAI/RapidOCR) |

Ogni file viene controllato con la sua impronta SHA-256, scritta in
`identiframe/tools.py`, e ogni rete viene caricata una volta da OpenCV prima
di essere tenuta; accanto ai modelli vengono salvati i testi di licenza e un
`SOURCE.txt` con provenienza e impronte. OpenCV 5.0 calcola Tanh con un
esponenziale che va in overflow per ingressi oltre circa 44: al caricamento
IdentiFrame mette in memoria un Clip(-40, 40) davanti a ogni Tanh della rete
(tanh(±40) vale già ±1 in precisione singola), così le uscite coincidono con
quelle di onnxruntime; i file su disco restano quelli originali.

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
`config.json`. Ogni lingua è un modulo in `identiframe/locales/` (testo
inglese → traduzione); `scripts\check_i18n.py` controlla che ogni testo abbia
la sua traduzione in ogni lingua. Le traduzioni diverse dall'italiano sono
state prodotte con l'aiuto di un modello linguistico e non sono ancora state
riviste da madrelingua: le correzioni sono benvenute.

## Struttura

| File | Contenuto |
| --- | --- |
| `IdentiFrame.py` | punto di ingresso |
| `identiframe/app.py` | finestra principale |
| `identiframe/fusion.py` | la pipeline: ricerca del soggetto, registrazione ECC, fusione, deconvoluzione |
| `identiframe/report.py`, `pdfreport.py` | salvataggio di immagini e rapporto (testo, JSON, PDF) |
| `identiframe/preview.py` | anteprima ingrandibile con area del soggetto e viste collegate |
| `identiframe/timeline.py` | timeline con anteprime, zoom, segnaposto e riferimento |
| `identiframe/ffmpeg.py` | informazioni sul video, anteprime, fotogrammi grezzi |
| `identiframe/tools.py` | ricerca, download e aggiornamento di ffmpeg e dei modelli OCR in `tools/` |
| `identiframe/i18n.py`, `locales/` | lingua dell'interfaccia e i cataloghi delle traduzioni (un modulo per lingua) |
| `identiframe/theme.py`, `widgets.py`, `shell.py`, `frameless.py` | tema scuro, componenti, barra laterale, finestra senza barra |
| `identiframe/tasks.py`, `procs.py` | lavori in background; processi figli legati all'applicazione |
| `identiframe/config.py` | impostazioni in `config.json` |
| `identiframe/ocr.py` | lettura dei caratteri: fusioni dei gruppi, fast-plate-ocr e PaddleOCR tramite OpenCV, voto per posizione |
| `scripts/build_exe.py` | compila `IdentiFrame.exe` (file spec senza la libreria FFmpeg di OpenCV); `--release` zip, licenze e note; `--publish` release su GitHub |
| `scripts/make_brand.py` | rigenera logo e icona (serve il carattere Panchang) |
| `scripts/check_i18n.py` | controlla che ogni testo abbia la traduzione in ogni lingua |

## Licenza

GNU GPL v3 con termini aggiuntivi di attribuzione dell'autore: vedi
[LICENSE](LICENSE) e [NOTICE](NOTICE). La dicitura

    Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net

va mantenuta nei sorgenti, nell'interfaccia (piede della finestra e riquadro
Crediti) e nella documentazione. Il programma la scrive anche nei rapporti:
le versioni modificate possono conservarla, senza obbligo. Il nome
"IdentiFrame", il logo e l'icona "IF" identificano il programma originale:
una versione modificata distribuita ad altri deve usare un nome e un logo
diversi.

ffmpeg è un programma separato con la propria licenza (LGPL/GPL): vedi
<https://ffmpeg.org/legal.html>. Python e le librerie contenute
nell'eseguibile (CustomTkinter, Pillow, NumPy, OpenCV, fpdf2 e le loro dipendenze)
restano sotto le proprie licenze: lo zip di release porta i loro file di
licenza nella cartella `licenses`. Nemmeno i modelli OCR fanno parte del
programma: licenze e provenienza sono in *Modelli OCR* più sopra.

### Carattere tipografico

Logo e icona sono composti in **Panchang**, un carattere di Indian Type
Foundry (ITF) distribuito da [Fontshare](https://www.fontshare.com/fonts/panchang)
con la ITF Free Font License; marchi e diritti d'autore sono di ITF. Le
immagini del logo e dell'icona contengono solo contorni e pixel: il carattere
non viene distribuito con IdentiFrame, e `scripts/make_brand.py` ha bisogno
che sia installato per rigenerarle.

### Video di prova

Il programma è stato provato, e gli screenshot del manuale sono stati fatti,
con tre video di Pexels, usati secondo la
[licenza Pexels](https://www.pexels.com/license/):

| Soggetto | Video | Autore |
| --- | --- | --- |
| Veicoli e targhe | [Traffico Autostradale Intenso Al Tramonto](https://www.pexels.com/it-it/video/traffico-autostradale-intenso-al-tramonto-31779728/) | [Şeyhmus Kino](https://www.pexels.com/it-it/@seyhmuskino/) |
| Scritte | [Traffico Sulla Strada nella Città di Taipei, Taiwan](https://www.pexels.com/it-it/video/citta-auto-traffico-veicoli-13271103/) | [Levi Wedge](https://www.pexels.com/it-it/@levi-wedge-266970209/) |
| Volto | [Affascinante Strada Europea Con Ciclista](https://www.pexels.com/it-it/video/affascinante-strada-europea-con-ciclista-33476096/) | [Tuba Din](https://www.pexels.com/it-it/@tubadinn/) |

Le targhe, le scritte e il volto visibili nella documentazione sono quelli di
quei filmati.
