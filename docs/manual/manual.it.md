# FrameFusion — Manuale d'uso

[English](manual.en.md) · **Italiano** · [Deutsch](manual.de.md) · [Français](manual.fr.md) · [Español](manual.es.md) · [Nederlands](manual.nl.md) · [Polski](manual.pl.md) · [Ελληνικά](manual.el.md) · [Shqip](manual.sq.md)

FrameFusion migliora la leggibilità di un dettaglio piccolo — una targa, un
volto, una scritta — ripreso in più fotogrammi di un video. Allinea quei
fotogrammi con precisione sub-pixel, li fonde su una griglia più fine, riduce
rumore e sfocatura e produce **un'unica immagine**, con un rapporto che
documenta ogni parametro e ogni passaggio.

*Andrea Cumini — www.osintinfo.net — andrea@osintinfo.net*

## Indice

1. [Come funziona](#1-come-funziona)
2. [Installazione e primo avvio](#2-installazione-e-primo-avvio)
3. [Pagina Configurazione](#3-pagina-configurazione)
4. [Pagina Soggetto: fotogrammi, soggetto e riferimento](#4-pagina-soggetto-fotogrammi-soggetto-e-riferimento)
5. [Pagina Fusione](#5-pagina-fusione)
6. [Salvataggio: immagini e rapporto](#6-salvataggio-immagini-e-rapporto)
7. [Ottenere il massimo da una targa o da un volto](#7-ottenere-il-massimo-da-una-targa-o-da-un-volto)
8. [Limiti e uso corretto](#8-limiti-e-uso-corretto)
9. [Scorciatoie da tastiera](#9-scorciatoie-da-tastiera)

## 1. Come funziona

Ogni fotogramma di un video registra il soggetto in una posizione leggermente
diversa rispetto alla griglia dei pixel, e con un suo rumore casuale.
FrameFusion sfrutta proprio questo: trova il soggetto in ogni fotogramma,
allinea tutti i fotogrammi a un **fotogramma di riferimento** con precisione
sub-pixel e li combina. Il rumore cala e torna una parte del dettaglio che ogni
singolo fotogramma aveva perso. Nulla viene inventato: il risultato contiene
solo ciò che i fotogrammi sostengono.

Il lavoro si svolge in sette passaggi, mostrati nel riquadro *Pipeline*:

| Passaggio | Che cosa succede |
| --- | --- |
| 1. Estrazione dei fotogrammi | L'intervallo scelto viene decodificato da FFmpeg, esatto al fotogramma. |
| 2. Rilevamento del soggetto | Il soggetto viene seguito fotogramma per fotogramma, in avanti e all'indietro dal riferimento. |
| 3. Allineamento locale | Ogni fotogramma viene allineato al riferimento (algoritmo ECC; modello a traslazione, rotazione, affine o prospettico). |
| 4. Registrazione sub-pixel | L'allineamento viene raffinato a piena risoluzione; si scelgono i fotogrammi più nitidi e meglio allineati. |
| 5. Fusione multi-frame | I fotogrammi vengono ricampionati su una griglia fino a 4 volte più fine e combinati, scartando i valori anomali. |
| 6. Deconvoluzione e riduzione del rumore | Livelli automatici, riduzione del rumore facoltativa e deconvoluzione di Richardson-Lucy sulla luminanza. |
| 7. Fotogramma unico | Immagine finale, ghost dei fotogrammi, confronto con il riferimento, dati per il rapporto. |

## 2. Installazione e primo avvio

**Eseguibile (Windows 10/11, 64 bit).** Estrai `FrameFusion-<versione>-windows-x64.zip`
dove vuoi e avvia `FrameFusion.exe`. Python non serve. L'eseguibile non è
firmato: la prima volta Windows SmartScreen può chiedere una conferma.

**Dai sorgenti.** Con Python 3.10 o successivo:

```bash
python -m pip install -r requirements.txt
python FrameFusion.py
```

**FFmpeg.** FrameFusion usa FFmpeg per leggere i video ma non lo include. Al
primo avvio, se FFmpeg manca, si apre la pagina **Configurazione** sul
riquadro *FFmpeg*: **Scarica / Aggiorna** prende il build ufficiale per
Windows e lo mette nella cartella `tools\ffmpeg` accanto al programma. Nulla
viene installato nel sistema.

Un video si può aprire anche dalla riga di comando:
`FrameFusion.exe video.mp4`.

## 3. Pagina Configurazione

![Pagina Configurazione](images/it/01_configuration.png)

- **Sorgente** — **Apri video…** (oppure Ctrl+O, o l'icona della cartella nel
  riquadro *VIDEO* in alto). Qui si vedono durata, numero di fotogrammi,
  risoluzione e codec. Aperto un video, il programma passa alla pagina
  *Soggetto*.
- **Uscita** — *Cartella di destinazione* in cui salvare le fusioni (vuota =
  accanto al video), *Sottocartella con il nome del video*, *Formato* (PNG o
  TIFF) e *Profondità colore* (*Auto* = 16 bit per canale per la fusione).
  *Salva anche ogni fotogramma allineato* aggiunge una cartella `aligned/` con
  ogni fotogramma usato, allineato al riferimento.
- **FFmpeg** — dove si trova FFmpeg e quale versione: **Verifica**, **Cerca
  aggiornamenti**, **Scarica / Aggiorna**.
- **Lingua** — interfaccia e rapporti sono disponibili in nove lingue: EN,
  IT, DE, FR, ES, NL, PL, EL, SQ. Il cambio è immediato e viene ricordato.
- **Crediti** — autore e licenza.

## 4. Pagina Soggetto: fotogrammi, soggetto e riferimento

![Pagina Soggetto](images/it/02_subject.png)

L'*Anteprima* mostra il fotogramma sotto il cursore: la **rotellina**
ingrandisce attorno al mouse (fino ai pixel reali), **trascinando** si sposta
la vista, il **doppio clic** riadatta il fotogramma. Sotto, i pulsanti
avanzano di uno o di dieci fotogrammi; **← →** e **Shift+← →** fanno lo stesso
da tastiera.

La *Timeline* mostra tutto il video come una pellicola. **Ctrl+rotellina**
ingrandisce, la **rotellina** scorre; cliccando o trascinando si sposta il
cursore. *Tutto* e *Selezione* regolano la vista.

**1. Scegli il fotogramma di riferimento.** Porta il cursore sul fotogramma in
cui il soggetto è **più grande e più nitido** — per un veicolo che si
avvicina, di solito uno degli ultimi in cui la targa è ancora intera.

**2. Seleziona l'area del soggetto.** Trascina col **tasto destro** sopra la
targa o il volto, oppure premi **Seleziona area** e trascina col sinistro.
Inquadra il soggetto con un piccolo margine. Il fotogramma mostrato diventa il
**riferimento** (segnaposto **R** sulla timeline; **→ R** riporta lì il
cursore) e **la fusione parte da sola**: il programma passa alla pagina
*Fusione*. Se disegni un'area nuova mentre la fusione gira, questa riparte.
**Cancella** toglie l'area.

**3. Scegli l'intervallo.** **Inizio [I]** e **Fine [O]** (tasti I e O)
fissano il primo e l'ultimo fotogramma da usare: quelli in cui il soggetto è
visibile e non coperto. Le bandierine I e O si possono anche trascinare, e i
campi IN / OUT accettano un tempo (`1:23.456`) o un fotogramma (`f2000`). Se
quando disegni l'area l'intervallo è ancora tutto il video, viene impostato a
30 fotogrammi prima e dopo il riferimento. Dopo aver cambiato l'intervallo,
**Fondi fotogrammi →** (o F5) rifà la fusione. Al massimo 300 fotogrammi per
fusione.

## 5. Pagina Fusione

![Pagina Fusione: ghost e risultato](images/it/03_fusion_ghost.png)

**Confronto.** A sinistra il **Ghost dei fotogrammi**: tutti i fotogrammi
usati, sovrapposti ciascuno nella posizione in cui è stato trovato, prima
dell'allineamento. Mostra che cosa entra nella fusione e quanto si muove il
soggetto. Con il menu sopra, la vista di sinistra può mostrare invece il
**Fotogramma di riferimento**, ingrandito con interpolazione bicubica: è il
«prima» corretto. A destra il risultato: **Finale**, oppure **Solo fusione**
(prima di riduzione del rumore e deconvoluzione). Le due viste si ingrandiscono
e si spostano insieme.

![Pagina Fusione: riferimento e risultato](images/it/04_fusion_reference.png)

**Pipeline.** I sette passaggi con esito e tempi; sotto, il riepilogo
(fotogrammi usati, ingrandimento, rumore prima e dopo la fusione), la barra di
avanzamento e i pulsanti **Apri cartella**, **Annulla**, **Salva risultato**,
**Avvia fusione**. I passaggi 1–4 dipendono solo da video, intervallo,
riferimento, area e modello di moto: se cambiano soltanto i parametri di
fusione o di restauro vengono riusati, e una nuova fusione richiede una
frazione di secondo (*riusato* nell'elenco dei passaggi).

### Parametri

La colonna di sinistra raggruppa i parametri per passaggio.

**Impostazioni salvate.** Insiemi di parametri con un nome: **Salva…** chiede
un nome e memorizza i parametri correnti; scegliendo un nome nel menu si
caricano; **Elimina** toglie l'insieme scelto; **Predefiniti** riporta ogni
parametro al suo valore di base. **Da rapporto…** carica i parametri dal
`report.json` di una fusione salvata in precedenza, per ripeterla esattamente.
I parametri in uso vengono comunque ricordati alla chiusura del programma.

| Riquadro | Parametro | Effetto |
| --- | --- | --- |
| Fotogrammi e allineamento | Modello di moto | Traslazione, rotazione + traslazione, affine, **prospettiva (omografia)** — predefinito; segue un soggetto che si avvicina, si allontana o gira. Se un fotogramma non converge, si prova un modello più semplice. |
| | Ricerca del soggetto: correlazione minima | Sotto questo punteggio il soggetto conta come non trovato in quel fotogramma. |
| | Qualità minima dell'allineamento (ECC) | I fotogrammi allineati peggio di così restano fuori (0,80 di base). |
| | Fotogrammi più nitidi tenuti | 75 % di base: il quarto meno nitido (mosso) resta fuori. |
| Fusione | Ingrandimento | Da × 1 (solo riduzione del rumore) a × 4. Di solito × 2 o × 3 è la scelta giusta. |
| | Metodo di fusione | **Media robusta (anomali scartati)** — predefinito; mediana; somma con spostamento con convoluzione normalizzata. |
| | Pesa per nitidezza | I fotogrammi più nitidi contano molto di più. |
| | Uniforma la luminosità | Compensa i cambi di esposizione tra i fotogrammi. |
| Restauro | Riduzione del rumore | Nessuna, leggera, media, forte (filtro bilaterale). |
| | Iterazioni di deconvoluzione | Richardson-Lucy: più iterazioni rendono più nitido, ma amplificano anche rumore e aloni. 20 di base. |
| | PSF σ (pixel dell'uscita) | Ampiezza della sfocatura da togliere. *Automatica* la misura sui bordi dell'immagine fusa. |
| | Regolarizzazione (variazione totale) | Frena il rumore durante la deconvoluzione. Media di base. |
| Presentazione | Livelli automatici | Nero e bianco ai percentili 0,5 e 99,5 della luminanza, prima della deconvoluzione. |
| | Contrasto locale (CLAHE) | Equalizzazione a zone: utile su targhe in ombra o in controluce. |
| | Scala di grigi | Toglie il colore: spesso più pulito per leggere i caratteri. |

## 6. Salvataggio: immagini e rapporto

**Salva risultato** (Ctrl+S nella pagina *Fusione*) crea una cartella nuova
`fusion_f<riferimento>_<data-ora>` nella cartella di destinazione, con:

| File | Contenuto |
| --- | --- |
| `result.png` | l'immagine finale |
| `fused.png` | la fusione prima di riduzione del rumore e deconvoluzione |
| `ghost.png` | il ghost dei fotogrammi usati |
| `reference_x<k>.png` | l'area del riferimento ingrandita con interpolazione bicubica, per il confronto |
| `reference_crop.png` | la stessa area alla risoluzione del video |
| `report.pdf` | il rapporto impaginato in A4, con le immagini |
| `report.txt` | lo stesso rapporto in testo semplice |
| `report.json` | gli stessi dati in forma strutturata, comprese le impostazioni (**Da rapporto…** le ricarica) |
| `aligned/` | a richiesta, ogni fotogramma usato, allineato al riferimento |

![Prima pagina del rapporto PDF](images/it/05_report.png)

Il rapporto è scritto nella lingua dell'interfaccia. Contiene la sorgente
(percorso, dimensione, impronta **SHA-256**, formato), intervallo, fotogramma
di riferimento e area, tutti i parametri, i sette passaggi con i metodi usati
e i tempi, la tabella dei fotogrammi (punteggio della ricerca, coefficienti di
allineamento, spostamento sub-pixel, nitidezza, peso, motivo dell'esclusione),
le stime del rumore e lo SHA-256 di ogni immagine scritta. Chi lo legge può
ripetere l'elaborazione e controllare che i file non siano cambiati.

*Salva fotogramma* nella pagina *Soggetto* salva invece il singolo fotogramma
sotto il cursore, a piena risoluzione e senza perdita.

## 7. Ottenere il massimo da una targa o da un volto

- **Riferimento**: il fotogramma in cui il soggetto è più grande e più nitido.
- **Intervallo**: solo i fotogrammi in cui il soggetto è interamente visibile.
  I fotogrammi lontani dal riferimento (molto più piccoli, con un'altra
  prospettiva) portano poco e spesso vengono comunque esclusi dalla soglia di
  qualità.
- **Area**: tutta la targa o tutto il volto con un piccolo margine; poco
  sfondo, che può muoversi in modo diverso.
- **Ingrandimento**: × 2 o × 3. × 4 conviene solo con molti fotogrammi.
- **Caratteri ancora morbidi?** Alza *PSF σ* di un passo (per esempio da
  Automatica al valore subito sopra quello scritto nel rapporto), oppure le
  *Iterazioni di deconvoluzione*.
- **Aloni attorno ai caratteri?** Abbassa *PSF σ* o le iterazioni, oppure alza
  la *Regolarizzazione*.
- **Targa in ombra o in controluce**: *Contrasto locale (CLAHE)* leggero o
  medio, spesso insieme a *Scala di grigi*.
- **Confronta** sempre con la vista *Fotogramma di riferimento*, ingrandendo
  sui caratteri: ciò che lì non si legge e compare solo dopo una nitidezza
  forte va trattato con cautela.
- Salva con **Salva…** un insieme di parametri che funziona per una telecamera
  e riusalo.

## 8. Limiti e uso corretto

- Il risultato è un **miglioramento** dei fotogrammi registrati, non una
  ricostruzione della realtà: non può recuperare ciò che nessun fotogramma
  contiene.
- I dettagli fini al limite della risoluzione, e i caratteri che si somigliano
  (8/B, 0/D, 1/7, 5/S), vanno verificati sui fotogrammi originali prima di trarre
  conclusioni.
- Il guadagno è maggiore con molti fotogrammi, piccoli spostamenti tra loro,
  rumore indipendente e un riferimento abbastanza nitido. Il mosso dentro il
  singolo fotogramma non viene tolto.
- Una compressione forte produce errori uguali in fotogrammi consecutivi: la
  fusione li riduce meno del rumore casuale.
- Targhe e volti sono dati personali: usa il programma nel rispetto delle
  regole che si applicano al tuo caso.

## 9. Scorciatoie da tastiera

| Tasti | Azione |
| --- | --- |
| Ctrl+1 / Ctrl+2 / Ctrl+3 | Pagina Configurazione / Soggetto / Fusione |
| Ctrl+O | Apri video |
| ← / → | Fotogramma precedente / successivo |
| Shift+← / Shift+→ | Indietro / avanti di 10 fotogrammi |
| Home / Fine | Primo / ultimo fotogramma |
| I / O | Inizio / fine dell'intervallo sul cursore |
| + / − | Ingrandisce / riduce la timeline |
| F | Tutto il video sulla timeline |
| Trascinare col destro sull'anteprima | Seleziona l'area del soggetto (la fusione parte) |
| Esc | Esce da *Seleziona area* |
| F5 | Avvia la fusione |
| Ctrl+S | Salva il risultato (pagina Fusione) o il fotogramma (pagina Soggetto) |


*Screenshot: video «[Busy Highway Traffic at Sunset](https://www.pexels.com/video/busy-highway-traffic-at-sunset-31779728/)» di [Şeyhmus Kino](https://www.pexels.com/@seyhmuskino/), da Pexels, usato secondo la [licenza Pexels](https://www.pexels.com/license/). Le targhe visibili negli screenshot sono quelle di quel filmato.*

---

FrameFusion è software libero sotto GNU GPL v3 con attribuzione dell'autore:
vedi `LICENSE` e `NOTICE`. Andrea Cumini - andrea@osintinfo.net - www.osintinfo.net
