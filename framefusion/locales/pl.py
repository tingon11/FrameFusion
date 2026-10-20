# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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
    "{name} is not a FrameFusion report.": "{name} nie jest raportem FrameFusion.",
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
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Fuzja: f{first} → f{last}, odniesienie f{ref}, obszar {width} × {height} w ({x}, {y}), ×{scale}, {method}",
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
    "{done} / {total} frames decoded": "zdekodowane klatki: {done} / {total}",
    "{count} frames decoded": "zdekodowano klatek: {count}",
    "The video ended before the reference frame.": "Wideo skończyło się przed klatką odniesienia.",
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
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  strona   ·   ← →  klatka   ·   I / O  zakres   ·   F5  scal   ·   Ctrl+S  zapisz",
    "ffmpeg missing": "brak ffmpeg",
    "Operation failed": "Operacja nie powiodła się",
    "ERROR - {title}: {message}": "BŁĄD - {title}: {message}",
    "Error: {title}": "Błąd: {title}",
    "INTERNAL ERROR": "BŁĄD WEWNĘTRZNY",
    "Internal error: details in the log.": "Błąd wewnętrzny: szczegóły w dzienniku.",
}
