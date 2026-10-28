# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Polski: tłumaczenie tekstów interfejsu i raportu.

Kluczem jest tekst angielski w postaci, w jakiej występuje w kodzie (w tr() i N_()),
wartością jego tłumaczenie. Symbole zastępcze w nawiasach klamrowych zostają bez zmian.
Klucze bez tłumaczenia pozostają po angielsku. Po każdej zmianie:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py pl
"""

from __future__ import annotations

NAME = "Polski"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "Nie można uruchomić interfejsu: {error}\n\n"
        "Zainstaluj zależności poleceniem:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "Nie znaleziono ffmpeg. Pobierz go z panelu FFmpeg na stronie Konfiguracja "
        "albo zainstaluj go i dodaj do PATH.",
    "Cannot check the latest ffmpeg version: {error}": "Nie można sprawdzić najnowszej wersji ffmpeg: {error}",
    "Unexpected answer from the ffmpeg download site.": "Nieoczekiwana odpowiedź ze strony pobierania ffmpeg.",
    "Downloading {label}": "Pobieranie {label}",
    "Download of {label} failed: {error}": "Pobieranie {label} nie powiodło się: {error}",
    "Invalid archive: suspicious path '{member}'.": "Nieprawidłowe archiwum: podejrzana ścieżka '{member}'.",
    "The downloaded file is not a valid zip archive.": "Pobrany plik nie jest prawidłowym archiwum zip.",
    "The downloaded package does not contain {name}.": "Pobrany pakiet nie zawiera {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "Nie można zaktualizować '{name}': pliki są w użyciu. Poczekaj na zakończenie fuzji i spróbuj ponownie.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "Automatyczne pobieranie jest dostępne tylko w systemie Windows: zainstaluj ffmpeg "
        "menedżerem pakietów systemu.",
    "Extracting ffmpeg": "Rozpakowywanie ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "Pobrany ffmpeg nie uruchamia się na tym komputerze.",
    "{name} is missing after extraction.": "Po rozpakowaniu brakuje {name}.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Sprawdzanie…",
    "Check": "Sprawdź",
    "Check for updates": "Sprawdź aktualizacje",
    "Download / Update": "Pobierz / Aktualizuj",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg to osobny program (LGPL/GPL). Pobieranie bierze oficjalną kompilację dla Windows "
        "z {url} i zachowuje tylko ffmpeg.exe, LICENSE i README w folderze tools\\ffmpeg "
        "obok programu: bez instalacji, bez zmian w PATH.",
    "ffmpeg check failed": "Sprawdzenie ffmpeg nie powiodło się",
    "tools folder": "folder tools",
    "system PATH": "systemowy PATH",
    "Python package": "pakiet Pythona",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Silnik: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Brak: pobierz go przyciskiem po prawej.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "Nie znaleziono ffmpeg: pobierz go z panelu FFmpeg na stronie Konfiguracja.",
    "ffmpeg missing: download it from the FFmpeg box.": "Brak ffmpeg: pobierz go z panelu FFmpeg.",
    "Checking the latest ffmpeg version…": "Sprawdzanie najnowszej wersji ffmpeg…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} jest aktualny.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Najnowsze wydanie: {latest}. Zainstalowane: {installed}. Pobrać je teraz?",
    "Update check failed": "Sprawdzenie aktualizacji nie powiodło się",
    "Wait for the running fusion, then try again.": "Poczekaj na zakończenie trwającej fuzji, potem spróbuj ponownie.",
    "Downloading ffmpeg…": "Pobieranie ffmpeg…",
    "Downloading ffmpeg from {url}": "Pobieranie ffmpeg z {url}",
    "ffmpeg downloaded into {path}": "ffmpeg pobrano do {path}",
    "Download cancelled.": "Pobieranie anulowane.",
    "ffmpeg download failed": "Pobieranie ffmpeg nie powiodło się",
    "ffmpeg: exit code {code}": "ffmpeg: kod wyjścia {code}",
    "File not found: {path}": "Nie znaleziono pliku: {path}",
    "The file has no recognizable video track.": "Plik nie zawiera rozpoznawalnej ścieżki wideo.",
    "Video size not recognized.": "Nie rozpoznano rozmiaru wideo.",
    "Frame rate not recognized.": "Nie rozpoznano liczby klatek na sekundę.",
    "Invalid frame rate.": "Nieprawidłowa liczba klatek na sekundę.",
    "Unknown video duration (stream or damaged file).":
        "Nieznany czas trwania wideo (strumień lub uszkodzony plik).",
    "Zero video duration.": "Zerowy czas trwania wideo.",
    "No frame at {seconds:.3f} s.": "Brak klatki w chwili {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg nie zapisał pliku.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "POTWIERDŹ",
    "WARNING": "OSTRZEŻENIE",
    "ERROR": "BŁĄD",
    "Yes": "Tak",

    # ----------------------------------------------------------- navigazione
    "PAGES": "STRONY",
    "Configuration": "Konfiguracja",
    "Subject": "Obiekt",
    "Frames, subject and reference": "Klatki, obiekt i odniesienie",
    "Fusion": "Fuzja",
    "Multi-frame fusion and result": "Fuzja wieloklatkowa i wynik",
    "{app}  /  PAGE {index:02d}": "{app}  /  STRONA {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "brak",
    "Open video… (Ctrl+O)": "Otwórz wideo… (Ctrl+O)",
    "No video": "Brak wideo",
    "Reading…": "Wczytywanie…",
    "Ready": "Gotowe",
    "Error": "Błąd",
    "Fusing…": "Scalanie…",
    "Fused": "Scalono",

    # ------------------------------------------------------------- anteprima
    "Preview": "Podgląd",
    "Open a video to see the preview": "Otwórz wideo, aby zobaczyć podgląd",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "przeciąganie prawym: obszar obiektu  ·  kółko: zoom  ·  przeciąganie: przesuwanie  ·  dwuklik: dopasuj",
    "First frame (Home)": "Pierwsza klatka (Home)",
    "Back 10 frames (Shift+←)": "10 klatek wstecz (Shift+←)",
    "Previous frame (←)": "Poprzednia klatka (←)",
    "Next frame (→)": "Następna klatka (→)",
    "Forward 10 frames (Shift+→)": "10 klatek naprzód (Shift+→)",
    "Last frame (End)": "Ostatnia klatka (End)",
    "Save frame": "Zapisz klatkę",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Zapisuje pokazaną klatkę w pełnej rozdzielczości, bezstratnie (Ctrl+S)",
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Większy podgląd: ukrywa oś czasu, klawisze I / O nadal działają (F11)",
    "Preview unavailable: {error}": "Podgląd niedostępny: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+kółko: zoom  ·  kółko: przewijanie  ·  przeciągaj I / O i kursor  ·  dwuklik na linijce: wszystko",
    "In  [I]": "Początek  [I]",
    "Out  [O]": "Koniec  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Ustawia początek zaznaczenia na kursorze (klawisz I)",
    "Sets the end of the selection at the cursor (key O)":
        "Ustawia koniec zaznaczenia na kursorze (klawisz O)",
    "Moves the cursor to the start of the selection": "Przenosi kursor na początek zaznaczenia",
    "Moves the cursor to the end of the selection": "Przenosi kursor na koniec zaznaczenia",
    "CURSOR": "KURSOR",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Czas (1:23.456, 83.4) lub klatka (f2000), potem Enter",
    "Zoom out (−)": "Pomniejsz (−)",
    "Zoom in (+)": "Powiększ (+)",
    "All": "Wszystko",
    "Selection": "Zaznaczenie",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Zaznaczenie: f{first} → f{last}  ·  klatek: {count}  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Widok: {start} → {end}  ({seconds:.3f} s, klatek: {frames:.1f})",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Nie rozpoznano czasu: użyj mm:ss.mmm, sekund lub f<liczba>.",
    "Open a video to see the timeline": "Otwórz wideo, aby zobaczyć oś czasu",

    # -------------------------------------------------------------- soggetto
    "Select area": "Zaznacz obszar",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Potem przeciągnij na podglądzie, aby objąć obiekt (lub w dowolnej chwili przeciągnij prawym przyciskiem); "
        "fuzja rozpocznie się sama",
    "Moves the cursor to the reference frame": "Przenosi kursor na klatkę odniesienia",
    "Clear": "Wyczyść",
    "Fuse frames  →": "Scal klatki  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Uruchamia fuzję wieloklatkową na zaznaczonym zakresie (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Obejmij obiekt na wyraźnej klatce: ta klatka staje się klatką odniesienia i fuzja się rozpoczyna.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Przeciągnij na podglądzie, aby objąć obiekt (Esc, aby przerwać).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "Obszar obiektu jest za mały: narysuj co najmniej {size} × {size} pikseli.",
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Zakres zawężony do klatek, w których śledzono obiekt: f{first} → f{last}.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Zakres ustawiony wokół klatki odniesienia: f{first} → f{last}. Przesuń I / O, aby go zmienić.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Obszar obiektu {width} × {height} w ({x}, {y}) na klatce odniesienia f{frame}",
    "Subject area cleared.": "Obszar obiektu wyczyszczony.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "Odniesienie f{frame} leży poza zakresem f{first} → f{last}: przesuń I / O.",
    "{count} frames in the range: select at most {limit}.":
        "Klatek w zakresie: {count}; zaznacz najwyżej {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Obszar {width} × {height} px w ({x}, {y})  ·  odniesienie f{frame}  ·  klatek: {count}, f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Najpierw zaznacz obszar obiektu (tablica, twarz, przedmiot) na wyraźnej klatce: przeciągnij prawym "
        "przyciskiem na podglądzie albo użyj Zaznacz obszar.",
    "The reference frame must be inside the selected range.":
        "Klatka odniesienia musi leżeć w zaznaczonym zakresie.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "Liczba klatek w zakresie: {count}; zaznacz najwyżej {limit} wokół klatki odniesienia.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Klatki i dopasowanie",
    "Motion model": "Model ruchu",
    "Translation": "Przesunięcie",
    "Rotation + translation": "Obrót + przesunięcie",
    "Affine": "Afiniczny",
    "Perspective (homography)": "Perspektywa (homografia)",
    "Subject search: minimum correlation": "Wyszukiwanie obiektu: minimalna korelacja",
    "Minimum alignment quality (ECC)": "Minimalna jakość dopasowania (ECC)",
    "Sharpest frames kept": "Zachowane najostrzejsze klatki",
    "Scale": "Powiększenie",
    "Fusion method": "Metoda fuzji",
    "Robust mean (outliers rejected)": "Średnia odporna (bez wartości odstających)",
    "Shift-and-add (normalized convolution)": "Shift-and-add (splot znormalizowany)",
    "Median": "Mediana",
    "Weight by sharpness": "Ważenie według ostrości",
    "Equalize brightness": "Wyrównaj jasność",
    "Restoration": "Rekonstrukcja",
    "Noise reduction": "Redukcja szumu",
    "Off": "Brak",
    "Light": "Lekka",
    "Medium": "Średnia",
    "Strong": "Silna",
    "Deconvolution iterations": "Iteracje dekonwolucji",
    "0 (none)": "0 (brak)",
    "not applied": "nie zastosowano",
    "PSF σ (output pixels)": "PSF σ (piksele wyjściowe)",
    "Automatic": "Automatycznie",
    "Regularization (total variation)": "Regularyzacja (wariacja całkowita)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Więcej iteracji bardziej wyostrza, ale wzmacnia też szum i halo; regularyzacja hamuje szum. "
        "Zmieniaj po trochu i porównuj.",
    "Presentation": "Prezentacja",
    "Auto levels": "Automatyczne poziomy",
    "Local contrast (CLAHE)": "Korekta kontrastu lokalnego (CLAHE)",
    "Grayscale": "Skala szarości",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Poziomy to prosta stosowana przed dekonwolucją (czerń i biel na percentylach 0,5 i 99,5); "
        "kontrast lokalny to wyrównanie strefowe. Wszystko jest zapisane w raporcie.",
    "Defaults": "Domyślne",
    "Puts every parameter of the pipeline back to its default value":
        "Przywraca domyślne wartości wszystkich parametrów przetwarzania",
    "Parameters back to their defaults.": "Parametry przywrócone do wartości domyślnych.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Zapisane ustawienia",
    "(none saved)": "(brak zapisanych)",
    "Save…": "Zapisz…",
    "Saves the current parameters under a name (in config.json)":
        "Zapisuje bieżące parametry pod nazwą (w config.json)",
    "Delete": "Usuń",
    "From report…": "Z raportu…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Wczytuje parametry zapisane w report.json zapisanej fuzji",
    "Save settings": "Zapisz ustawienia",
    "Name of these settings:": "Nazwa tych ustawień:",
    "Settings «{name}» already exist. Replace them?": "Ustawienia „{name}” już istnieją. Zastąpić je?",
    "Settings «{name}» saved.": "Ustawienia „{name}” zapisane.",
    "Settings «{name}» loaded.": "Ustawienia „{name}” wczytane.",
    "Delete settings": "Usuń ustawienia",
    "Delete the settings «{name}»?": "Usunąć ustawienia „{name}”?",
    "Settings «{name}» deleted.": "Ustawienia „{name}” usunięte.",
    "Load parameters from a report": "Wczytaj parametry z raportu",
    "Cannot read the report": "Nie można odczytać raportu",
    "{name} is not an IdentiFrame report.": "{name} nie jest raportem IdentiFrame.",
    "Parameters loaded from {path}": "Parametry wczytane z {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Porównanie",
    "FRAMES": "KLATKI",
    "RESULT": "WYNIK",
    "Ghost of the frames": "Nałożenie klatek",
    "Reference frame": "Klatka odniesienia",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "NAŁOŻENIE  ·  KLATEK: {count}  ·  ×{scale}",
    "Final": "Końcowy",
    "Fusion only": "Tylko fuzja",
    "Draw the subject area on the Subject page, then run the fusion":
        "Narysuj obszar obiektu na stronie Obiekt, potem uruchom fuzję",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "kółko: zoom  ·  przeciąganie: przesuwanie  ·  dwuklik: dopasuj  ·  oba widoki poruszają się razem  ·  "
        "nałożenie: wszystkie użyte klatki, każda w miejscu, w którym została znaleziona",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "ODNIESIENIE f{frame}  ·  BIKUBICZNA ×{scale}",
    "RESULT  ·  {count} FRAMES": "WYNIK  ·  KLATEK: {count}",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Przetwarzanie",
    "Frame extraction": "Wyodrębnianie klatek",
    "Subject detection": "Wykrywanie obiektu",
    "Local alignment": "Dopasowanie lokalne",
    "Sub-pixel registration": "Rejestracja subpikselowa",
    "Multi-frame fusion": "Fuzja wieloklatkowa",
    "Deconvolution and denoising": "Dekonwolucja i odszumianie",
    "Single frame": "Pojedyncza klatka",
    "Save result": "Zapisz wynik",
    "Saves images and report in a new folder (Ctrl+S)": "Zapisuje obrazy i raport w nowym folderze (Ctrl+S)",
    "Run fusion": "Uruchom fuzję",
    "Runs the pipeline again with these parameters (F5)": "Uruchamia przetwarzanie ponownie z tymi parametrami (F5)",
    "Open folder": "Otwórz folder",
    "Cancel": "Anuluj",
    "reused": "ponownie użyto",
    "Fusion in progress…": "Trwa fuzja…",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "klatek: {used} z {count}  ·  ×{scale}  ·  szum σ {ref:.1f} → {fused:.1f} po fuzji  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fuzja zakończona: {summary}",
    "Excluded: {list}": "Wykluczone: {list}",
    "Fusion cancelled.": "Fuzja anulowana.",
    "Fusion cancelled by the user": "Fuzja anulowana przez użytkownika",
    "Fusion failed: see the log.": "Fuzja nie powiodła się: zobacz dziennik.",
    "Fusion failed": "Fuzja nie powiodła się",
    "Fusion in progress": "Fuzja w toku",
    "The fusion is still running. Stop it and close?": "Fuzja wciąż trwa. Przerwać ją i zamknąć?",
    "Saving the result…": "Zapisywanie wyniku…",
    "Saved in «{folder}».": "Zapisano w „{folder}”.",
    "Saved in {folder}": "Zapisano w {folder}",
    "Result, comparison images and report saved in {folder}":
        "Wynik, obrazy porównawcze i raport zapisano w {folder}",

    # messaggi dei passaggi (fusion.py)
    "{count} frames decoded": "zdekodowano klatek: {count}",
    "The video ended before the reference frame.": "Wideo skończyło się przed klatką odniesienia.",
    "Range set with I / O": "Zakres ustawiony przez I / O",
    "Frames examined":
        "Zbadane klatki",
    "Frames that make up the result":
        "Klatki tworzące wynik",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "Pominięto {count} klatek, ponieważ następują po ponad {seconds:g} s bez dobrego wyrównania: od tego miejsca obiekt nie jest już potwierdzony (zasłonięty, zbyt mały lub poza kadrem).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Obiekt śledzony od f{first} do f{last}: dalej go brak lub nie jest potwierdzony przez ponad {seconds:g} s.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Wyszukiwanie obiektu na klatkach pomniejszonych do {percent:.0f} % (limit pamięci).",
    "searching the subject: {done} / {total}": "wyszukiwanie obiektu: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Zachowano jedną klatkę na każde {stride} (limit pamięci dla dużych obszarów).",
    "{done} / {total} frames read at full resolution": "klatki odczytane w pełnej rozdzielczości: {done} / {total}",
    "The reference frame could not be read.": "Nie udało się odczytać klatki odniesienia.",
    "subject found in {found} / {total} frames": "obiekt znaleziony w klatkach: {found} / {total}",
    "{done} / {total} frames aligned": "dopasowane klatki: {done} / {total}",
    "motion model: {model}": "model ruchu: {model}",
    "{done} / {total} frames registered": "zarejestrowane klatki: {done} / {total}",
    "{count} frames registered": "zarejestrowano klatek: {count}",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "Klatki dopasowane prostszym modelem ruchu, bo wybrany model nie był na nich zbieżny: {count}.",
    "{count} frames selected": "wybrano klatek: {count}",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Użytecznych klatek jest tylko {count}: wynik może być tylko nieznacznie lepszy od klatki odniesienia. "
        "Poszerz zakres lub obniż próg jakości.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Powiększenie zmniejszono z ×{asked} do ×{used}: obszar jest za duży.",
    "resampling on the fine grid: {percent:.0f} %": "przepróbkowanie na drobnej siatce: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "shift-and-add: klatki {done} / {total}",
    "{count} frames fused on a ×{scale} grid": "klatek scalonych na siatce ×{scale}: {count}",
    "noise reduction ({level})": "redukcja szumu ({level})",
    "deconvolution: iteration {n} / {total}": "dekonwolucja: iteracja {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, liczba iteracji: {iterations}",
    "no deconvolution": "bez dekonwolucji",
    "{width} × {height} pixels": "{width} × {height} pikseli",

    # motivi di esclusione di un fotogramma
    "subject not found": "nie znaleziono obiektu",
    "not sampled (memory limit)": "nie próbkowano (limit pamięci)",
    "frame not decoded": "klatka niezdekodowana",
    "alignment failed": "dopasowanie nie powiodło się",
    "sub-pixel registration failed": "rejestracja subpikselowa nie powiodła się",
    "low alignment quality": "niska jakość dopasowania",
    "less sharp than the selected ones": "mniej ostra niż wybrane",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Źródło",
    "Open video…": "Otwórz wideo…",
    "Duration": "Czas trwania",
    "Frames": "Klatki",
    "Resolution": "Rozdzielczość",
    "Codec": "Kodek",
    "  (rotated {degrees}°)": "  (obrót {degrees}°)",
    "Open video": "Otwórz wideo",
    "Videos": "Pliki wideo",
    "All files": "Wszystkie pliki",
    "Reading {name}…": "Wczytywanie {name}…",
    "Cannot open the video": "Nie można otworzyć wideo",
    "{name}: {frames} frames, {duration}.": "{name}: liczba klatek {frames}, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Otwarto {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Output": "Wyjście",
    "Destination folder": "Folder docelowy",
    "Subfolder named after the video": "Podfolder o nazwie wideo",
    "Browse…": "Przeglądaj…",
    "Format": "Format",
    "Color depth": "Głębia kolorów",
    "Also save every aligned frame (aligned/ folder)": "Zapisz także każdą dopasowaną klatkę (folder aligned/)",
    "next to the video": "obok wideo",
    ", in a subfolder named after it": ", w podfolderze o jego nazwie",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Każda zapisana fuzja ma własny folder ({where}) z plikami result.{ext}, fuzją przed rekonstrukcją, "
        "klatką odniesienia do porównania, report.txt, report.pdf i report.json (parametry, etapy, użyte "
        "klatki, SHA-256). Obrazy: {bits} bitów na kanał.",
    "Language": "Język",
    "Interface language. The change is immediate and is saved for the next start.":
        "Język interfejsu. Zmiana jest natychmiastowa i zostaje zapamiętana do następnego uruchomienia.",
    "Credits": "Autorzy",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Wolne oprogramowanie na licencji GNU GPL v3 z wymogiem wskazania autora: zobacz pliki LICENSE i "
        "NOTICE. Dekodowanie wideo wykonuje FFmpeg, osobny program na własnej licencji; przetwarzanie "
        "obrazu z użyciem OpenCV i NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (bezstratny)",
    "Saving frame {frame}…": "Zapisywanie klatki {frame}…",
    "Saved {path}": "Zapisano {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Klatka f{frame} zapisana w {path} ({pix_fmt})",
    "Save failed": "Zapis nie powiódł się",
    "The folder does not exist yet.": "Folder jeszcze nie istnieje.",
    "Cannot open the folder": "Nie można otworzyć folderu",
    "Open a video first.": "Najpierw otwórz wideo.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "Nie można zakodować {name}.",
    "Writing the images…": "Zapisywanie obrazów…",
    "Writing the PDF report…": "Zapisywanie raportu PDF…",
    "page {page} of {pages}": "strona {page} z {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Odniesienie f{frame}  ·  bikubiczna ×{scale}",
    "Result  ·  {count} frames": "Wynik  ·  klatek: {count}",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Nałożenie  ·  klatek: {count}, każda w miejscu, w którym została znaleziona",
    "Fusion before restoration": "Fuzja przed rekonstrukcją",
    "Writing the aligned frames: {done} / {total}": "Zapisywanie dopasowanych klatek: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Obliczanie sum kontrolnych SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — raport fuzji wieloklatkowej",
    "Created: {when}": "Utworzono: {when}",
    "File": "Plik",
    "Size": "Rozmiar",
    "{size} bytes": "{size} bajtów",
    "Video": "Wideo",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}",
    "Range and subject": "Zakres i obiekt",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} (klatek: {count}, {start} → {end})",
    "Subject area on the reference frame": "Obszar obiektu na klatce odniesienia",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} pikseli",
    "Parameters": "Parametry",
    "yes": "tak",
    "no": "nie",
    "Deconvolution": "Dekonwolucja",
    "{iterations} Richardson-Lucy iterations": "Richardson-Lucy, liczba iteracji: {iterations}",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px obrazu wyjściowego ({mode})",
    "automatic: measured on the edges of the fused image": "automatycznie: zmierzona na krawędziach scalonego obrazu",
    "manual": "ręcznie",
    "Steps": "Etapy",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "Klatek zdekodowanych przez FFmpeg, z dokładnością co do klatki: {count}; {scale}.",
    "subject search at full resolution": "wyszukiwanie obiektu w pełnej rozdzielczości",
    "subject search at {percent:.0f} % of the resolution": "wyszukiwanie obiektu przy {percent:.0f} % rozdzielczości",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Obiekt śledzony od klatki odniesienia w przód i w tył za pomocą znormalizowanej korelacji wzajemnej "
        "(OpenCV matchTemplate, TM_CCOEFF_NORMED); znaleziony w klatkach: {found} / {count}, wyciętych "
        "w pełnej rozdzielczości wokół niego.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Zgrubne dopasowanie każdej klatki do klatki odniesienia algorytmem ECC (Evangelidis & "
        "Psarakis, 2008), model: {model}, na wygładzonych obrazach.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC doprecyzowane w pełnej rozdzielczości (dokładność subpikselowa): zarejestrowanych klatek: "
        "{registered}. Wybór: ECC ≥ {quality:.2f}, {keep} % najostrzejszych (energia laplasjanu): użytych "
        "klatek: {used}.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: klatki przepróbkowane na siatce ×{scale} klatki odniesienia (Lanczos), ważone jakością "
        "dopasowania{sharp}{equal}.",
    " and sharpness": " i ostrością",
    ", brightness equalized to the reference": ", jasność wyrównana do klatki odniesienia",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Tylko na luminancji (kolor jest wygładzany: w skompresowanym wideo niesie szum, a nie "
        "szczegóły). Redukcja szumu: {denoise}. Dekonwolucja: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Najpierw automatyczne poziomy: luminancja {black:.3f} → 0, {white:.3f} → 1, ta sama prosta na każdym kanale",
    "No auto levels": "Bez automatycznych poziomów",
    " (bilateral filter)": " (filtr bilateralny)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, gaussowska PSF σ {sigma:.2f} px, liczba iteracji: {iterations}, regularyzacja "
        "wariacją całkowitą: {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Prezentacja: korekta kontrastu lokalnego: {clahe}; {gray}. Pojedyncza klatka {width} × {height} pikseli.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, limit obcięcia {clip:g})",
    "grayscale": "w skali szarości",
    "color": "w kolorze",
    "Result": "Wynik",
    "Frames used": "Użyte klatki",
    "{used} of {count}": "{used} z {count}",
    "Estimated noise σ": "Szacowany szum σ",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Metoda Immerkæra, 0-255, w rozdzielczości wideo: odniesienie {ref:.2f} → po fuzji {fused:.2f} → "
        "wynik końcowy {final:.2f}. Dekonwolucja wzmacnia jednocześnie drobne szczegóły i szum, więc ostatnia "
        "wartość nie jest wyłącznie miarą szumu.",
    "Samples per output pixel": "Próbek na piksel wyjściowy",
    "Sub-pixel phases covered (4 × 4 grid)": "Pokryte fazy subpikselowe (siatka 4 × 4)",
    "frame": "klatka",
    "time": "czas",
    "search": "szukanie",
    "sharp.": "ostr.",
    "weight": "waga",
    "used": "użyta",
    "model": "model",
    "note": "uwaga",
    "(reference)": "(odniesienie)",
    "Files": "Pliki",
    "aligned/: {count} aligned frames": "aligned/: dopasowanych klatek: {count}",
    "Note": "Uwaga",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "Wynik jest ulepszeniem wymienionych wyżej klatek: łączy informacje w nich obecne i nie dodaje "
        "szczegółów. Drobne szczegóły na granicy rozdzielczości oraz podobne do siebie znaki należy "
        "sprawdzić na klatkach źródłowych przed wyciągnięciem wniosków.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Oprogramowanie: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Gotowe.",
    "ffmpeg missing": "brak ffmpeg",
    "Operation failed": "Operacja nie powiodła się",
    "ERROR - {title}: {message}": "BŁĄD - {title}: {message}",
    "Error: {title}": "Błąd: {title}",
    "INTERNAL ERROR": "BŁĄD WEWNĘTRZNY",
    "Internal error: details in the log.": "Błąd wewnętrzny: szczegóły w dzienniku.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Rodzaj obiektu",
    "Parameters set for the subject type: {subject}.": "Parametry ustawione dla rodzaju obiektu: {subject}.",
    "Face": "Twarz",
    "pose or expression differs from the reference": "poza lub mimika różni się od klatki odniesienia",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Twarz: lokalne, niesztywne dopasowanie po ECC na {count} klatkach, średnie przesunięcie {residual:.2f} px wideo.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Twarz: obszar jest zbyt mały na lokalne dopasowanie (co najmniej {size} px): tylko sztywne wyrównanie.",
    "simil.": "podob.",
    "Local refinement (face)": "Lokalne dopasowanie (twarz)",
    "not applied: area too small, rigid alignment only": "nie zastosowano: obszar zbyt mały, tylko sztywne wyrównanie",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Twarz: obszar obiektu ma {width} × {height} pikseli w wideo. Fuzja łączy klatki, których poza i mimika zgadzają się z klatką odniesienia, i nadaje mniejszą wagę częściom, które się różnią; nie może stworzyć cech, których nie pokazuje żadna klatka. Przy twarzy węższej niż około 60 pikseli wynik może poprawić ogólny wygląd, ale nie ujawni cech identyfikujących: porównaj go z klatką odniesienia i z pojedynczymi klatkami, zanim wyciągniesz wnioski o tożsamości.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Twarz: po modelu sztywnym lokalne, niesztywne dopasowanie (przepływ optyczny Farnebäcka między klatką odniesienia a wyrównaną klatką, wygładzony i ograniczony co do amplitudy) podąża za mimiką i ruchem głowy; pewność dla każdego piksela (spójność w przód i w tył oraz lokalna korelacja) waży każdą próbkę w fuzji. Klatki, których lokalne podobieństwo do odniesienia jest niższe niż {limit:.2f}, są odrzucane (zmiana pozy lub mimiki).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} klatek dopasowanych; średnie lokalne podobieństwo do odniesienia {similarity:.2f}, średnie lokalne przesunięcie {displacement:.2f} px wideo; {excluded} klatek odrzuconych z powodu innej pozy lub mimiki.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fuzja: {subject}, f{first} → f{last}, odniesienie f{ref}, obszar {width} × {height} w ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Ctrl+1/2/3  strona   ·   ← →  klatka   ·   Spacja  odtwarzaj   ·   I / O  zakres   ·   F5  scal   ·   Ctrl+S  zapisz",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} klatek wyrównano prostszym modelem ruchu, ponieważ wybrany dawał nieprawdopodobne zniekształcenie (skala, ścinanie lub perspektywa poza granicami).",
    "persp.": "persp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Twarz: próbki poza elipsą wpisaną w obszar liczą się mało, a tam wynik pokazuje klatkę odniesienia: tło porusza się inaczej niż twarz.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Tablica i Tekst: jedno sztywne dopasowanie na klatkę; znaki odczytuje fast-plate-ocr (tablice) lub PaddleOCR (napisy, także w wielu wierszach). Twarz: po dopasowaniu lokalne niesztywne doprecyzowanie śledzi mimikę i ruch głowy, klatki z inną pozą są pomijane, a odtwarzanie jest lżejsze. Zmiana typu wczytuje jego wartości domyślne.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Odczytuje tablicę (fast-plate-ocr) lub napis (PaddleOCR) na wyniku i na niezależnych fuzjach grup klatek oraz głosuje znak po znaku",
    "OCR models": "Modele OCR",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "Znaki odczytują dwa modele uruchamiane przez OpenCV, pobierane na żądanie do tools\\ocr i nigdy niewchodzące w skład programu (około 37 MB): fast-plate-ocr dla tablic (MIT, autor ankandrew) i PaddleOCR PP-OCRv6 dla napisów w wielu językach (Apache 2.0, Baidu / PaddleOCR, konwersja ONNX RapidOCR). Każdy plik jest sprawdzany odciskiem SHA-256; licencje i pochodzenie są zapisywane obok modeli.",
    "Downloading the OCR models…": "Pobieranie modeli OCR…",
    "Reading the characters…": "Odczyt znaków…",
    "OCR models download failed": "Pobieranie modeli OCR nie powiodło się",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "Pobieranie modeli OCR: {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Brak modelu OCR dla tego typu obiektu: pobierz go w polu Modele OCR na stronie Konfiguracja.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "naciśnij Odczytaj znaki (automatycznie dla tablic i napisów, gdy modele OCR są gotowe)",
    "model confidence {confidence:.0f} %": "pewność modelu {confidence:.0f} %",
    "OCR models check failed": "Sprawdzanie modeli OCR nie powiodło się",
    "OCR: {plate} (plates), {text} (texts)": "OCR: {plate} (tablice), {text} (napisy)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Brak (opcjonalne, do odczytu tablic i napisów): pobierz je przyciskiem po prawej.",
    "OCR models ready: {path}": "Modele OCR gotowe: {path}",
    "possible country ({share:.0f} %)": "możliwy kraj ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "możliwy kraj: {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  tablice: {plate}  ·  napisy: {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Brak modelu dla napisów: pobierz go przyciskiem po prawej.",
    "The model for plates is missing: download it with the button on the right.": "Brak modelu dla tablic: pobierz go przyciskiem po prawej.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Napis, standard: perspektywa, 75 % najostrzejszych, ×2, średnia odporna, umiarkowana dekonwolucja. Punkt wyjścia.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Napis nocą lub zaszumiony: więcej klatek, średnia redukcja szumu, łagodniejsza dekonwolucja z silną regularyzacją, lekki kontrast lokalny, skala szarości.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Odległy, mały napis nagrany w wielu klatkach: ×3, przesunięcie i sumowanie, prawie wszystkie klatki, niższy próg dopasowania.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Napis na jadącym pojeździe lub nagrany poruszającą się kamerą, z rozmyciem ruchu: tylko ostrzejsza połowa klatek, bardziej tolerancyjne wyszukiwanie obiektu, silniejsza dekonwolucja.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Napis w cieniu lub pod światło: średni kontrast lokalny, skala szarości, lekka redukcja szumu.",
    "Plate": "Tablica",
    "Text": "Tekst",
    "No text line found inside the area: the whole area was read as one line.": "W obszarze nie znaleziono wiersza tekstu: cały obszar odczytano jako jeden wiersz.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "Nie znaleziono znaków: narysuj obszar ciasno wokół tablicy lub napisu i sprawdź powiększenie oraz odtwarzanie.",
    "Cannot load the OCR model {name}: {error}": "Nie można wczytać modelu OCR {name}: {error}",
    "The OCR model configuration {name} is not valid.": "Konfiguracja modelu OCR {name} jest nieprawidłowa.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Automatyczny odczyt modelu OCR, do sprawdzenia na obrazach: znaki o podobnym kształcie (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) mogą być błędnie odczytane w ten sam sposób w każdym odczycie, a głosowanie tego nie zauważy. Możliwy kraj tablicy to szacunek modelu na podstawie wyglądu tablicy, nie weryfikacja.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), uruchamiany przez {runtime}: odczytywany jest wynik i {groups} fuzji niezależnych grup klatek, każda odtworzona z tymi samymi parametrami; odczyty są wyrównywane i głosowane znak po znaku, ważone prawdopodobieństwem, jakie model przypisuje każdemu znakowi (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), uruchamiany przez {runtime}: wiersze tekstu są wyszukiwane w wyniku, a następnie każdy wiersz jest odczytywany na wyniku i na {groups} fuzjach niezależnych grup klatek, każda odtworzona z tymi samymi parametrami; każdy wiersz jest głosowany znak po znaku, ważony prawdopodobieństwem, jakie model przypisuje każdemu znakowi (Quiala et al., 2023).",
    "the whole area": "cały obszar",
    "Model confidence": "Pewność modelu",
    "Area read": "Odczytany obszar",
    "Text lines": "Wiersze tekstu",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} pikseli wyniku",
    "Possible country": "Możliwy kraj",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, średnie prawdopodobieństwo znaków odczytanych w wyniku",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % głosów), oszacowany przez model na podstawie wyglądu tablicy",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV nie może wczytać pobranego modelu {name}.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name}: pobrany plik nie jest oczekiwanym plikiem (jego odcisk SHA-256 jest inny).",
    "Read characters": "Odczytaj znaki",
    "CHARACTERS": "ZNAKI",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Odczytane znaki: {text}  ·  zgodność {agreement:.0f} %  ·  {count} odczytów",
    "Character reading": "Odczyt znaków",
    "reading…": "odczyt…",
    "no characters found: draw the area tight around the text": "nie znaleziono znaków: zaznacz obszar ciasno wokół napisu",
    "agreement {agreement:.0f} %  ·  {count} readings": "zgodność {agreement:.0f} %  ·  {count} odczytów",
    "Character reading failed: {error}": "Odczyt znaków nie powiódł się: {error}",
    "doubtful: {list}": "wątpliwe: {list}",
    "check by eye: {list}": "sprawdź wzrokowo: {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Za mało klatek na niezależne grupy: odczytano tylko wynik, bez głosowania.",
    "Character reading (OCR)": "Odczyt znaków (OCR)",
    "illegible":
        "nieczytelne",
    "no character recognizable with enough confidence":
        "żaden znak nie jest rozpoznawalny z wystarczającą pewnością",
    "{count} illegible lines not shown":
        "Nie pokazano {count} nieczytelnych wierszy",
    "not recognizable (?): {list}":
        "nierozpoznawalne (?): {list}",
    "illegible: no character recognizable with enough confidence":
        "nieczytelne: żaden znak nie jest rozpoznawalny z wystarczającą pewnością",
    "? = character not recognizable":
        "? = znak nierozpoznawalny",
    "Thresholds":
        "Progi",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "wiersz uznaje się za czytelny od pewności modelu {legible:.0f} %; znak jest pokazywany, gdy jego poparcie (głosy ważone prawdopodobieństwem, jakie daje mu model, ze wszystkich odczytów) osiąga {support:.0f} %, w przeciwnym razie «?».",
    "Illegible lines":
        "Nieczytelne wiersze",
    "{count} lines found but not recognizable, not shown":
        "Znaleziono {count} wierszy, ale są nierozpoznawalne i nie zostały pokazane",
    "support":
        "poparcie",
    "Single readings (model output, before the thresholds)":
        "Pojedyncze odczyty (wyjście modelu, przed progami)",
    "Frames used in the fusion":
        "Klatki użyte w fuzji",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Wszystkie {count} klatki tworzące wynik: obszar obiektu każdej z nich, wyrównany do klatki odniesienia tak, jak wchodzi do fuzji, z jej wagą (R = klatka odniesienia).",
    "Play / pause (Space)":
        "Odtwórz / pauza (Spacja)",
    "Fit":
        "Dopasuj",
    "Choose the language":
        "Wybierz język",
    "Before you start":
        "Zanim zaczniesz",
    "What {app} produces":
        "Co tworzy {app}",
    "How the result is obtained":
        "Jak powstaje wynik",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} nie tworzy obrazów: łączy informacje rzeczywiście obecne w wielu klatkach tego samego wideo. Śledzi narysowany obszar od klatki do klatki, wyrównuje każdą klatkę do klatki odniesienia z dokładnością subpikselową, odrzuca klatki, których nie da się wiarygodnie wyrównać, i łączy pozostałe średnią ważoną odporną na wartości odstające. Każda klatka rejestruje obiekt z nieco innym przesunięciem i innym szumem: po połączeniu szum maleje i pojawiają się szczegóły rozłożone na wiele klatek (superrozdzielczość wieloklatkowa). Następująca potem dekonwolucja i korekty kontrastu to operacje deterministyczne, a wszystkie ich parametry są zapisane w raporcie.",
    "The result is a reconstruction":
        "Wynik jest rekonstrukcją",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "Otrzymany obraz to rekonstrukcja obliczona wyłącznie z rzeczywistych pikseli użytych klatek, z których każda jest wymieniona w raporcie wraz z wagą. Żaden model generatywny ani sztuczna inteligencja nie dodaje, nie uzupełnia ani nie wymyśla szczegółów: to, czego nie ma w żadnej klatce, nie może pojawić się w wyniku. Rekonstrukcja może jednak zawierać artefakty (podwójne krawędzie tam, gdzie wyrównanie jest niedoskonałe, poświaty po dekonwolucji) i jest tyle warta, co źródło: zawsze porównuj ją z oryginalnymi klatkami.",
    "Character reading and country are estimates":
        "Odczyt znaków i kraj to szacunki",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "Odczyt znaków (OCR) i kraj tablicy są natomiast szacunkami modeli rozpoznawania wytrenowanych na przykładach, które zawsze proponują najbardziej prawdopodobne znaki. Program łączy kilka odczytów i oznacza «?» lub jako nieczytelne to, co nie osiąga jego progów, ale nawet odczyt pokazany na zielono może być błędny. To pomoc, a nie dowód: sprawdź każdy znak na obrazie własnym okiem.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "Rozumiem, że wynik jest rekonstrukcją z klatek wideo, w której nic nie zostało wymyślone, natomiast odczyt znaków i przypisanie kraju są szacunkami do sprawdzenia.",
    "Accept and continue":
        "Akceptuj i kontynuuj",
    "Exit":
        "Zakończ",
    "Vote by position": "Głosowanie wg pozycji",
    "result": "wynik",
    "Reading": "Odczyt",
    "Agreement": "Zgodność",
    "Method": "Metoda",
    "Statement": "Oświadczenie",
    "pos.": "poz.",
    "char.": "znak",
    "agreement": "zgodność",
    "alternatives": "alternatywy",
    "looks like": "przypomina",
    "group": "grupa",
    "source": "źródło",
    "text": "tekst",
    "conf.": "pewn.",
    "frames": "klatki",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Zapisane przez Ciebie.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Wbudowane ustawienia dla rodzaju obiektu wybranego na stronie Obiekt, potem Twoje.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» to wbudowane ustawienie: wybierz inną nazwę.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Tablica, standard: perspektywa, 75 % najostrzejszych, ×2, średnia odporna, umiarkowana dekonwolucja. Punkt wyjścia.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Tablica nocą lub zaszumiona: więcej klatek, średnia redukcja szumu, łagodniejsza dekonwolucja z silną regularyzacją, lekki kontrast lokalny, skala szarości.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Odległa, mała tablica nagrana w wielu klatkach: ×3, przesunięcie i sumowanie, prawie wszystkie klatki, niższy próg dopasowania.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Pojazd w ruchu lub zbliżający się, z rozmyciem ruchu: tylko ostrzejsza połowa klatek, bardziej tolerancyjne wyszukiwanie obiektu, silniejsza dekonwolucja.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Tablica w cieniu lub pod światło: średni kontrast lokalny, skala szarości, lekka redukcja szumu.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Twarz, standard: afiniczny, lokalne dopasowanie, lekka redukcja szumu, łagodna dekonwolucja z silną regularyzacją. Punkt wyjścia.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Twarz nocą lub zaszumiona: więcej klatek, średnia redukcja szumu, bardzo lekka dekonwolucja.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Twarz, minimalna obróbka: fuzja tylko z automatycznymi poziomami, bez redukcji szumu i dekonwolucji. Najbardziej ostrożny wynik.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Odległa, mała twarz: ×3, prawie wszystkie klatki, niższy próg dopasowania.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Twarz w cieniu lub pod światło: lekki kontrast lokalny, łagodna dekonwolucja.",
}
