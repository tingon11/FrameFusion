# FrameFusion — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
# SPDX-License-Identifier: GPL-3.0-only
# GNU GPL v3 con termini aggiuntivi (attribuzione dell'autore): vedi LICENSE e NOTICE.
"""Español: traduzione spagnola dei testi dell'interfaccia e del rapporto.

La chiave e' il testo inglese cosi' come compare nel codice (in tr() e N_()),
il valore la sua traduzione. I segnaposto tra graffe vanno lasciati identici.
Le chiavi non tradotte restano in inglese. Dopo ogni modifica:

    .venv\\Scripts\\python.exe scripts\\check_i18n.py es
"""

from __future__ import annotations

NAME = "Español"

CATALOG: dict[str, str] = {
    # ---------------------------------------------------------------- avvio
    "Cannot start the interface: {error}\n\n"
    "Install the dependencies with:\n"
    "    python -m pip install -r requirements.txt":
        "No se puede iniciar la interfaz: {error}\n\n"
        "Instale las dependencias con:\n"
        "    python -m pip install -r requirements.txt",

    # --------------------------------------------------------------- ffmpeg
    "ffmpeg not found. Download it from the FFmpeg box of the Configuration page, "
    "or install it and put it in the PATH.":
        "ffmpeg no encontrado. Descárguelo desde el recuadro FFmpeg de la página Configuración, "
        "o instálelo y añádalo al PATH.",
    "Cannot check the latest ffmpeg version: {error}": "No se puede comprobar la última versión de ffmpeg: {error}",
    "Unexpected answer from the ffmpeg download site.": "Respuesta inesperada del sitio de descarga de ffmpeg.",
    "Downloading {label}": "Descargando {label}",
    "Download of {label} failed: {error}": "La descarga de {label} ha fallado: {error}",
    "Invalid archive: suspicious path '{member}'.": "Archivo comprimido no válido: ruta sospechosa '{member}'.",
    "The downloaded file is not a valid zip archive.": "El archivo descargado no es un archivo zip válido.",
    "The downloaded package does not contain {name}.": "El paquete descargado no contiene {name}.",
    "Cannot update '{name}': files in use. Wait for the running fusion and try again.":
        "No se puede actualizar '{name}': archivos en uso. Espere a que termine la fusión y vuelva a intentarlo.",
    "Automatic download is available on Windows only: install ffmpeg with the "
    "system package manager.":
        "La descarga automática solo está disponible en Windows: instale ffmpeg con el "
        "gestor de paquetes del sistema.",
    "Extracting ffmpeg": "Extrayendo ffmpeg",
    "The downloaded ffmpeg does not run on this PC.": "El ffmpeg descargado no se ejecuta en este PC.",
    "{name} is missing after extraction.": "Falta {name} tras la extracción.",

    # ------------------------------------------------------- riquadro FFmpeg
    "Checking…": "Comprobando…",
    "Check": "Comprobar",
    "Check for updates": "Buscar actualizaciones",
    "Download / Update": "Descargar / Actualizar",
    "ffmpeg is a separate program (LGPL/GPL). The download takes the official Windows "
    "build from {url} and keeps only ffmpeg.exe, LICENSE and README in the tools\\ffmpeg "
    "folder next to the program: no installation, no changes to the PATH.":
        "ffmpeg es un programa independiente (LGPL/GPL). La descarga toma la compilación oficial para "
        "Windows de {url} y conserva solo ffmpeg.exe, LICENSE y README en la carpeta tools\\ffmpeg "
        "junto al programa: sin instalación, sin cambios en el PATH.",
    "ffmpeg check failed": "Comprobación de ffmpeg fallida",
    "tools folder": "carpeta tools",
    "system PATH": "PATH del sistema",
    "Python package": "paquete Python",
    "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}": "OK  ·  ffmpeg {version}  ·  {source}  ·  {path}",
    "Engine: ffmpeg {version} ({path})": "Motor: ffmpeg {version} ({path})",
    "Missing: download it with the button on the right.": "Falta: descárguelo con el botón de la derecha.",
    "ffmpeg not found: download it from the FFmpeg box of the Configuration page.":
        "ffmpeg no encontrado: descárguelo desde el recuadro FFmpeg de la página Configuración.",
    "ffmpeg missing: download it from the FFmpeg box.": "Falta ffmpeg: descárguelo desde el recuadro FFmpeg.",
    "Checking the latest ffmpeg version…": "Comprobando la última versión de ffmpeg…",
    "ffmpeg {version} is up to date.": "ffmpeg {version} está actualizado.",
    "Latest release: {latest}. Installed: {installed}. Download it now?":
        "Última versión: {latest}. Instalada: {installed}. ¿Descargarla ahora?",
    "Update check failed": "Comprobación de actualizaciones fallida",
    "Wait for the running fusion, then try again.": "Espere a que termine la fusión en curso y vuelva a intentarlo.",
    "Downloading ffmpeg…": "Descargando ffmpeg…",
    "Downloading ffmpeg from {url}": "Descargando ffmpeg desde {url}",
    "ffmpeg downloaded into {path}": "ffmpeg descargado en {path}",
    "Download cancelled.": "Descarga cancelada.",
    "ffmpeg download failed": "Descarga de ffmpeg fallida",
    "ffmpeg: exit code {code}": "ffmpeg: código de salida {code}",
    "File not found: {path}": "Archivo no encontrado: {path}",
    "The file has no recognizable video track.": "El archivo no tiene ninguna pista de vídeo reconocible.",
    "Video size not recognized.": "Tamaño del vídeo no reconocido.",
    "Frame rate not recognized.": "Frecuencia de fotogramas no reconocida.",
    "Invalid frame rate.": "Frecuencia de fotogramas no válida.",
    "Unknown video duration (stream or damaged file).":
        "Duración del vídeo desconocida (flujo o archivo dañado).",
    "Zero video duration.": "Duración del vídeo nula.",
    "No frame at {seconds:.3f} s.": "Ningún fotograma en {seconds:.3f} s.",
    "ffmpeg did not write the file.": "ffmpeg no ha escrito el archivo.",

    # -------------------------------------------------------------- dialoghi
    "CONFIRM": "CONFIRMAR",
    "WARNING": "AVISO",
    "ERROR": "ERROR",
    "Yes": "Sí",

    # ----------------------------------------------------------- navigazione
    "PAGES": "PÁGINAS",
    "Configuration": "Configuración",
    "Subject": "Sujeto",
    "Frames, subject and reference": "Fotogramas, sujeto y referencia",
    "Fusion": "Fusión",
    "Multi-frame fusion and result": "Fusión multifotograma y resultado",
    "{app}  /  PAGE {index:02d}": "{app}  /  PÁGINA {index:02d}",

    # ---------------------------------------------------------- intestazione
    "none": "ninguno",
    "Open video… (Ctrl+O)": "Abrir vídeo… (Ctrl+O)",
    "No video": "Sin vídeo",
    "Reading…": "Leyendo…",
    "Ready": "Listo",
    "Error": "Error",
    "Fusing…": "Fusionando…",
    "Fused": "Fusionado",

    # ------------------------------------------------------------- anteprima
    "Preview": "Vista previa",
    "Open a video to see the preview": "Abra un vídeo para ver la vista previa",
    "right-drag: subject area  ·  wheel: zoom  ·  drag: pan  ·  double-click: fit":
        "arrastrar con el botón derecho: área del sujeto  ·  rueda: zoom  ·  arrastrar: mover  ·  doble clic: ajustar",
    "First frame (Home)": "Primer fotograma (Inicio)",
    "Back 10 frames (Shift+←)": "Retroceder 10 fotogramas (Mayús+←)",
    "Previous frame (←)": "Fotograma anterior (←)",
    "Next frame (→)": "Fotograma siguiente (→)",
    "Forward 10 frames (Shift+→)": "Avanzar 10 fotogramas (Mayús+→)",
    "Last frame (End)": "Último fotograma (Fin)",
    "Save frame": "Guardar fotograma",
    "Save the shown frame at full resolution, lossless (Ctrl+S)":
        "Guarda el fotograma mostrado a resolución completa, sin pérdida (Ctrl+S)",
    "Preview unavailable: {error}": "Vista previa no disponible: {error}",

    # -------------------------------------------------------------- timeline
    "Ctrl+wheel: zoom  ·  wheel: scroll  ·  drag I / O and the cursor  ·  double-click the ruler: all":
        "Ctrl+rueda: zoom  ·  rueda: desplazar  ·  arrastrar I / O y el cursor  ·  doble clic en la regla: todo",
    "In  [I]": "Entrada  [I]",
    "Out  [O]": "Salida  [O]",
    "Sets the start of the selection at the cursor (key I)":
        "Establece el inicio de la selección en el cursor (tecla I)",
    "Sets the end of the selection at the cursor (key O)":
        "Establece el final de la selección en el cursor (tecla O)",
    "Moves the cursor to the start of the selection": "Lleva el cursor al inicio de la selección",
    "Moves the cursor to the end of the selection": "Lleva el cursor al final de la selección",
    "CURSOR": "CURSOR",
    "Time (1:23.456, 83.4) or frame (f2000), then Enter":
        "Tiempo (1:23.456, 83.4) o fotograma (f2000), luego Intro",
    "Zoom out (−)": "Alejar (−)",
    "Zoom in (+)": "Acercar (+)",
    "All": "Todo",
    "Selection": "Selección",
    "Selection: f{first} → f{last}  ·  {count} frames  ·  {seconds:.3f} s":
        "Selección: f{first} → f{last}  ·  {count} fotogramas  ·  {seconds:.3f} s",
    "View: {start} → {end}  ({seconds:.3f} s, {frames:.1f} frames)":
        "Vista: {start} → {end}  ({seconds:.3f} s, {frames:.1f} fotogramas)",
    "Time not recognized: use mm:ss.mmm, seconds or f<number>.":
        "Tiempo no reconocido: use mm:ss.mmm, segundos o f<número>.",
    "Open a video to see the timeline": "Abra un vídeo para ver la línea de tiempo",

    # -------------------------------------------------------------- soggetto
    "Select area": "Seleccionar área",
    "Then drag on the preview to frame the subject (or right-drag at any time); the fusion starts by itself":
        "Luego arrastre sobre la vista previa para encuadrar el sujeto (o arrastre con el botón derecho en "
        "cualquier momento); la fusión se inicia sola",
    "Moves the cursor to the reference frame": "Lleva el cursor al fotograma de referencia",
    "Clear": "Borrar",
    "Fuse frames  →": "Fusionar fotogramas  →",
    "Runs the multi-frame fusion on the selected range (F5)":
        "Ejecuta la fusión multifotograma en el intervalo seleccionado (F5)",
    "Frame the subject on a clear frame: that frame becomes the reference and the fusion starts.":
        "Encuadre el sujeto en un fotograma nítido: ese fotograma se convierte en la referencia y la fusión se inicia.",
    "Drag on the preview to frame the subject (Esc to stop).":
        "Arrastre sobre la vista previa para encuadrar el sujeto (Esc para detener).",
    "The subject area is too small: draw at least {size} × {size} pixels.":
        "El área del sujeto es demasiado pequeña: dibuje al menos {size} × {size} píxeles.",
    "Range set around the reference: f{first} → f{last}. Move I / O to change it.":
        "Intervalo establecido alrededor de la referencia: f{first} → f{last}. Mueva I / O para cambiarlo.",
    "Subject area {width} × {height} at ({x}, {y}) on the reference frame f{frame}":
        "Área del sujeto {width} × {height} en ({x}, {y}) en el fotograma de referencia f{frame}",
    "Subject area cleared.": "Área del sujeto borrada.",
    "Reference f{frame} is outside the range f{first} → f{last}: move I / O.":
        "La referencia f{frame} está fuera del intervalo f{first} → f{last}: mueva I / O.",
    "{count} frames in the range: select at most {limit}.":
        "{count} fotogramas en el intervalo: seleccione como máximo {limit}.",
    "Area {width} × {height} px at ({x}, {y})  ·  reference f{frame}  ·  {count} frames f{first} → f{last}":
        "Área {width} × {height} px en ({x}, {y})  ·  referencia f{frame}  ·  {count} fotogramas f{first} → f{last}",
    "Select the area of the subject (plate, face, object) on a clear frame first: right-drag on the preview, "
    "or use Select area.":
        "Seleccione primero el área del sujeto (matrícula, rostro, objeto) en un fotograma nítido: arrastre con "
        "el botón derecho sobre la vista previa, o use Seleccionar área.",
    "The reference frame must be inside the selected range.":
        "El fotograma de referencia debe estar dentro del intervalo seleccionado.",
    "The range has {count} frames: select at most {limit} around the reference.":
        "El intervalo tiene {count} fotogramas: seleccione como máximo {limit} alrededor de la referencia.",

    # -------------------------------------------------------- parametri
    "Frames and alignment": "Fotogramas y alineación",
    "Motion model": "Modelo de movimiento",
    "Translation": "Traslación",
    "Rotation + translation": "Rotación + traslación",
    "Affine": "Afín",
    "Perspective (homography)": "Perspectiva (homografía)",
    "Subject search: minimum correlation": "Búsqueda del sujeto: correlación mínima",
    "Minimum alignment quality (ECC)": "Calidad mínima de alineación (ECC)",
    "Sharpest frames kept": "Fotogramas más nítidos conservados",
    "Scale": "Escala",
    "Fusion method": "Método de fusión",
    "Robust mean (outliers rejected)": "Media robusta (valores atípicos descartados)",
    "Shift-and-add (normalized convolution)": "Suma con desplazamiento (convolución normalizada)",
    "Median": "Mediana",
    "Weight by sharpness": "Ponderar por nitidez",
    "Equalize brightness": "Igualar el brillo",
    "Restoration": "Restauración",
    "Noise reduction": "Reducción de ruido",
    "Off": "Ninguna",
    "Light": "Ligera",
    "Medium": "Media",
    "Strong": "Fuerte",
    "Deconvolution iterations": "Iteraciones de deconvolución",
    "0 (none)": "0 (ninguna)",
    "not applied": "no aplicada",
    "PSF σ (output pixels)": "PSF σ (píxeles de salida)",
    "Automatic": "Automática",
    "Regularization (total variation)": "Regularización (variación total)",
    "More iterations sharpen more but also amplify noise and halos; the regularization holds the noise back. "
    "Change a little at a time and compare.":
        "Más iteraciones aumentan la nitidez, pero también amplifican el ruido y los halos; la regularización "
        "contiene el ruido. Cambie poco a poco y compare.",
    "Presentation": "Presentación",
    "Auto levels": "Niveles automáticos",
    "Local contrast (CLAHE)": "Contraste local (CLAHE)",
    "Grayscale": "Escala de grises",
    "The levels are a straight line applied before the deconvolution (black and white at the 0.5 and 99.5 "
    "percentiles); the local contrast an equalization by zones. All written in the report.":
        "Los niveles son una recta aplicada antes de la deconvolución (negro y blanco en los percentiles 0,5 y "
        "99,5); el contraste local, una ecualización por zonas. Todo queda escrito en el informe.",
    "Defaults": "Predeterminados",
    "Puts every parameter of the pipeline back to its default value":
        "Devuelve cada parámetro del pipeline a su valor predeterminado",
    "Parameters back to their defaults.": "Parámetros restablecidos a sus valores predeterminados.",

    # -------------------------------------------------- impostazioni salvate
    "Saved settings": "Ajustes guardados",
    "(none saved)": "(ninguno guardado)",
    "Save…": "Guardar…",
    "Saves the current parameters under a name (in config.json)":
        "Guarda los parámetros actuales con un nombre (en config.json)",
    "Delete": "Eliminar",
    "From report…": "Desde informe…",
    "Loads the parameters written in the report.json of a saved fusion":
        "Carga los parámetros escritos en el report.json de una fusión guardada",
    "Save settings": "Guardar ajustes",
    "Name of these settings:": "Nombre de estos ajustes:",
    "Settings «{name}» already exist. Replace them?": "Los ajustes «{name}» ya existen. ¿Reemplazarlos?",
    "Settings «{name}» saved.": "Ajustes «{name}» guardados.",
    "Settings «{name}» loaded.": "Ajustes «{name}» cargados.",
    "Delete settings": "Eliminar ajustes",
    "Delete the settings «{name}»?": "¿Eliminar los ajustes «{name}»?",
    "Settings «{name}» deleted.": "Ajustes «{name}» eliminados.",
    "Load parameters from a report": "Cargar parámetros desde un informe",
    "Cannot read the report": "No se puede leer el informe",
    "{name} is not a FrameFusion report.": "{name} no es un informe de FrameFusion.",
    "Parameters loaded from {path}": "Parámetros cargados desde {path}",

    # ------------------------------------------------------------ confronto
    "Comparison": "Comparación",
    "FRAMES": "FOTOGRAMAS",
    "RESULT": "RESULTADO",
    "Ghost of the frames": "Fantasma de los fotogramas",
    "Reference frame": "Fotograma de referencia",
    "GHOST  ·  {count} FRAMES  ·  ×{scale}": "FANTASMA  ·  {count} FOTOGRAMAS  ·  ×{scale}",
    "Final": "Final",
    "Fusion only": "Solo fusión",
    "Draw the subject area on the Subject page, then run the fusion":
        "Dibuje el área del sujeto en la página Sujeto y luego ejecute la fusión",
    "wheel: zoom  ·  drag: pan  ·  double-click: fit  ·  the two views move together  ·  ghost: every frame "
    "used, superimposed at the position where it was found":
        "rueda: zoom  ·  arrastrar: mover  ·  doble clic: ajustar  ·  las dos vistas se mueven juntas  ·  "
        "fantasma: cada fotograma usado, superpuesto en la posición donde se encontró",
    "REFERENCE f{frame}  ·  BICUBIC ×{scale}": "REFERENCIA f{frame}  ·  BICÚBICA ×{scale}",
    "RESULT  ·  {count} FRAMES": "RESULTADO  ·  {count} FOTOGRAMAS",

    # -------------------------------------------------------------- pipeline
    "Pipeline": "Pipeline",
    "Frame extraction": "Extracción de fotogramas",
    "Subject detection": "Detección del sujeto",
    "Local alignment": "Alineación local",
    "Sub-pixel registration": "Registro subpíxel",
    "Multi-frame fusion": "Fusión multifotograma",
    "Deconvolution and denoising": "Deconvolución y reducción de ruido",
    "Single frame": "Fotograma único",
    "Save result": "Guardar resultado",
    "Saves images and report in a new folder (Ctrl+S)": "Guarda las imágenes y el informe en una carpeta nueva (Ctrl+S)",
    "Run fusion": "Ejecutar fusión",
    "Runs the pipeline again with these parameters (F5)": "Vuelve a ejecutar el pipeline con estos parámetros (F5)",
    "Open folder": "Abrir carpeta",
    "Cancel": "Cancelar",
    "reused": "reutilizado",
    "Fusion in progress…": "Fusión en curso…",
    "Fusion: f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}":
        "Fusión: f{first} → f{last}, referencia f{ref}, área {width} × {height} en ({x}, {y}), ×{scale}, {method}",
    "{seconds:.2f} s  ·  {detail}": "{seconds:.2f} s  ·  {detail}",
    "{used} of {count} frames  ·  ×{scale}  ·  noise σ {ref:.1f} → {fused:.1f} after the fusion  ·  {seconds:.1f} s":
        "{used} de {count} fotogramas  ·  ×{scale}  ·  ruido σ {ref:.1f} → {fused:.1f} tras la fusión  ·  "
        "{seconds:.1f} s",
    "Fusion done: {summary}": "Fusión completada: {summary}",
    "Excluded: {list}": "Excluidos: {list}",
    "Fusion cancelled.": "Fusión cancelada.",
    "Fusion cancelled by the user": "Fusión cancelada por el usuario",
    "Fusion failed: see the log.": "La fusión ha fallado: consulte el registro.",
    "Fusion failed": "Fusión fallida",
    "Fusion in progress": "Fusión en curso",
    "The fusion is still running. Stop it and close?": "La fusión todavía está en curso. ¿Detenerla y cerrar?",
    "Saving the result…": "Guardando el resultado…",
    "Saved in «{folder}».": "Guardado en «{folder}».",
    "Saved in {folder}": "Guardado en {folder}",
    "Result, comparison images and report saved in {folder}":
        "Resultado, imágenes de comparación e informe guardados en {folder}",

    # messaggi dei passaggi (fusion.py)
    "{done} / {total} frames decoded": "{done} / {total} fotogramas decodificados",
    "{count} frames decoded": "{count} fotogramas decodificados",
    "The video ended before the reference frame.": "El vídeo termina antes del fotograma de referencia.",
    "Subject search on frames reduced to {percent:.0f} % (memory limit).":
        "Búsqueda del sujeto en fotogramas reducidos al {percent:.0f} % (límite de memoria).",
    "searching the subject: {done} / {total}": "buscando el sujeto: {done} / {total}",
    "One frame every {stride} kept (memory limit for large areas).":
        "Se conserva un fotograma de cada {stride} (límite de memoria para áreas grandes).",
    "{done} / {total} frames read at full resolution": "{done} / {total} fotogramas leídos a resolución completa",
    "The reference frame could not be read.": "No se ha podido leer el fotograma de referencia.",
    "subject found in {found} / {total} frames": "sujeto encontrado en {found} / {total} fotogramas",
    "{done} / {total} frames aligned": "{done} / {total} fotogramas alineados",
    "motion model: {model}": "modelo de movimiento: {model}",
    "{done} / {total} frames registered": "{done} / {total} fotogramas registrados",
    "{count} frames registered": "{count} fotogramas registrados",
    "{count} frames aligned with a simpler motion model, because the chosen one did not converge on them.":
        "{count} fotogramas alineados con un modelo de movimiento más simple, porque el elegido no convergía "
        "en ellos.",
    "{count} frames selected": "{count} fotogramas seleccionados",
    "Only {count} usable frames: the result can be only slightly better than the reference. Widen the "
    "range or lower the quality threshold.":
        "Solo {count} fotogramas utilizables: el resultado solo puede ser ligeramente mejor que la referencia. "
        "Amplíe el intervalo o baje el umbral de calidad.",
    "Scale reduced from ×{asked} to ×{used}: the area is too large.":
        "Escala reducida de ×{asked} a ×{used}: el área es demasiado grande.",
    "resampling on the fine grid: {percent:.0f} %": "remuestreo en la cuadrícula fina: {percent:.0f} %",
    "shift-and-add: {done} / {total} frames": "suma con desplazamiento: {done} / {total} fotogramas",
    "{count} frames fused on a ×{scale} grid": "{count} fotogramas fusionados en una cuadrícula ×{scale}",
    "noise reduction ({level})": "reducción de ruido ({level})",
    "deconvolution: iteration {n} / {total}": "deconvolución: iteración {n} / {total}",
    "PSF σ {sigma:.2f} px, {iterations} iterations": "PSF σ {sigma:.2f} px, {iterations} iteraciones",
    "no deconvolution": "sin deconvolución",
    "{width} × {height} pixels": "{width} × {height} píxeles",

    # motivi di esclusione di un fotogramma
    "subject not found": "sujeto no encontrado",
    "not sampled (memory limit)": "no muestreado (límite de memoria)",
    "frame not decoded": "fotograma no decodificado",
    "alignment failed": "alineación fallida",
    "sub-pixel registration failed": "registro subpíxel fallido",
    "low alignment quality": "alineación de baja calidad",
    "less sharp than the selected ones": "menos nítido que los seleccionados",

    # ------------------------------------------------- pagina Configurazione
    "Source": "Origen",
    "Open video…": "Abrir vídeo…",
    "Duration": "Duración",
    "Frames": "Fotogramas",
    "Resolution": "Resolución",
    "Codec": "Códec",
    "  (rotated {degrees}°)": "  (girado {degrees}°)",
    "Open video": "Abrir vídeo",
    "Videos": "Vídeos",
    "All files": "Todos los archivos",
    "Reading {name}…": "Leyendo {name}…",
    "Cannot open the video": "No se puede abrir el vídeo",
    "{name}: {frames} frames, {duration}.": "{name}: {frames} fotogramas, {duration}.",
    "Opened {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "Abierto {path} — {width}x{height}, {fps} fps, {codec} {pix_fmt} ({bits} bits), {duration}",
    "Output": "Salida",
    "Destination folder": "Carpeta de destino",
    "Subfolder named after the video": "Subcarpeta con el nombre del vídeo",
    "Browse…": "Examinar…",
    "Format": "Formato",
    "Color depth": "Profundidad de color",
    "Also save every aligned frame (aligned/ folder)": "Guardar también cada fotograma alineado (carpeta aligned/)",
    "next to the video": "junto al vídeo",
    ", in a subfolder named after it": ", en una subcarpeta con su nombre",
    "Every saved fusion gets its own folder ({where}) with result.{ext}, the fusion before restoration, "
    "the reference frame for comparison, report.txt, report.pdf and report.json (parameters, steps, frames used, "
    "SHA-256). Images at {bits} bits per channel.":
        "Cada fusión guardada tiene su propia carpeta ({where}) con result.{ext}, la fusión antes de la "
        "restauración, el fotograma de referencia para la comparación, report.txt, report.pdf y report.json "
        "(parámetros, pasos, fotogramas usados, SHA-256). Imágenes a {bits} bits por canal.",
    "Language": "Idioma",
    "Interface language. The change is immediate and is saved for the next start.":
        "Idioma de la interfaz. El cambio es inmediato y se guarda para el próximo inicio.",
    "Credits": "Créditos",
    "Free software under the GNU GPL v3 with author attribution: see the LICENSE and NOTICE files. Video "
    "decoding by FFmpeg, a separate program under its own license; image processing with OpenCV and NumPy.":
        "Software libre bajo la GNU GPL v3 con atribución del autor: consulte los archivos LICENSE y NOTICE. "
        "La decodificación de vídeo corre a cargo de FFmpeg, un programa independiente con su propia licencia; "
        "el procesamiento de imágenes usa OpenCV y NumPy.",

    # ------------------------------------------------- salvataggio fotogramma
    "{format} (lossless)": "{format} (sin pérdida)",
    "Saving frame {frame}…": "Guardando el fotograma {frame}…",
    "Saved {path}": "Guardado {path}",
    "Frame f{frame} saved to {path} ({pix_fmt})": "Fotograma f{frame} guardado en {path} ({pix_fmt})",
    "Save failed": "Error al guardar",
    "The folder does not exist yet.": "La carpeta todavía no existe.",
    "Cannot open the folder": "No se puede abrir la carpeta",
    "Open a video first.": "Abra primero un vídeo.",

    # -------------------------------------------------------------- rapporto
    "Cannot encode {name}.": "No se puede codificar {name}.",
    "Writing the images…": "Escribiendo las imágenes…",
    "Writing the PDF report…": "Escribiendo el informe PDF…",
    "page {page} of {pages}": "página {page} de {pages}",
    "Reference f{frame}  ·  bicubic ×{scale}": "Referencia f{frame}  ·  bicúbica ×{scale}",
    "Result  ·  {count} frames": "Resultado  ·  {count} fotogramas",
    "Ghost  ·  {count} frames, each at the position where it was found":
        "Fantasma  ·  {count} fotogramas, cada uno en la posición donde se encontró",
    "Fusion before restoration": "Fusión antes de la restauración",
    "Writing the aligned frames: {done} / {total}": "Escribiendo los fotogramas alineados: {done} / {total}",
    "Computing the SHA-256 fingerprints…": "Calculando las huellas SHA-256…",
    "{app} {version} — multi-frame fusion report": "{app} {version} — informe de fusión multifotograma",
    "Created: {when}": "Creado: {when}",
    "File": "Archivo",
    "Size": "Tamaño",
    "{size} bytes": "{size} bytes",
    "Video": "Vídeo",
    "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bit), {duration}":
        "{width} × {height}, {fps} fps, {codec} {pix_fmt} ({bits} bits), {duration}",
    "Range and subject": "Intervalo y sujeto",
    "f{first} → f{last} ({count} frames, {start} → {end})":
        "f{first} → f{last} ({count} fotogramas, {start} → {end})",
    "Subject area on the reference frame": "Área del sujeto en el fotograma de referencia",
    "x {x}, y {y}, {width} × {height} pixels": "x {x}, y {y}, {width} × {height} píxeles",
    "Parameters": "Parámetros",
    "yes": "sí",
    "no": "no",
    "Deconvolution": "Deconvolución",
    "{iterations} Richardson-Lucy iterations": "{iterations} iteraciones de Richardson-Lucy",
    "PSF σ": "PSF σ",
    "{sigma:.2f} px of the output ({mode})": "{sigma:.2f} px de la salida ({mode})",
    "automatic: measured on the edges of the fused image": "automática: medida en los bordes de la imagen fusionada",
    "manual": "manual",
    "Steps": "Pasos",
    "{count} frames decoded by FFmpeg, exact to the frame; {scale}.":
        "{count} fotogramas decodificados por FFmpeg, con precisión de fotograma; {scale}.",
    "subject search at full resolution": "búsqueda del sujeto a resolución completa",
    "subject search at {percent:.0f} % of the resolution": "búsqueda del sujeto al {percent:.0f} % de la resolución",
    "Subject followed from the reference frame forwards and backwards by normalized cross-correlation "
    "(OpenCV matchTemplate, TM_CCOEFF_NORMED); found in {found} / {count} frames, cropped at full "
    "resolution around it.":
        "Sujeto seguido desde el fotograma de referencia hacia delante y hacia atrás por correlación cruzada "
        "normalizada (OpenCV matchTemplate, TM_CCOEFF_NORMED); encontrado en {found} / {count} fotogramas, "
        "recortados a resolución completa a su alrededor.",
    "Coarse alignment of every frame to the reference with the ECC algorithm (Evangelidis & Psarakis, "
    "2008), model: {model}, on smoothed images.":
        "Alineación aproximada de cada fotograma con la referencia mediante el algoritmo ECC (Evangelidis & "
        "Psarakis, 2008), modelo: {model}, sobre imágenes suavizadas.",
    "ECC refined at full resolution (sub-pixel precision): {registered} frames registered. Selection: "
    "ECC ≥ {quality:.2f}, the sharpest {keep} % (Laplacian energy): {used} frames used.":
        "ECC refinado a resolución completa (precisión subpíxel): {registered} fotogramas registrados. "
        "Selección: ECC ≥ {quality:.2f}, el {keep} % más nítido (energía del laplaciano): {used} fotogramas usados.",
    "{method}: frames resampled on a ×{scale} grid of the reference (Lanczos), weighted by alignment "
    "quality{sharp}{equal}.":
        "{method}: fotogramas remuestreados en una cuadrícula ×{scale} de la referencia (Lanczos), ponderados "
        "por la calidad de alineación{sharp}{equal}.",
    " and sharpness": " y la nitidez",
    ", brightness equalized to the reference": ", brillo igualado al de la referencia",
    "{levels}. On the luminance only (the color is smoothed: in compressed video it carries noise, not detail). "
    "Noise reduction: {denoise}. Deconvolution: {deconv}.":
        "{levels}. Solo sobre la luminancia (el color se suaviza: en el vídeo comprimido aporta ruido, no "
        "detalle). Reducción de ruido: {denoise}. Deconvolución: {deconv}.",
    "Auto levels first: luminance {black:.3f} → 0, {white:.3f} → 1, same line on every channel":
        "Primero los niveles automáticos: luminancia {black:.3f} → 0, {white:.3f} → 1, la misma recta en cada canal",
    "No auto levels": "Sin niveles automáticos",
    " (bilateral filter)": " (filtro bilateral)",
    "Richardson-Lucy, Gaussian PSF σ {sigma:.2f} px, {iterations} iterations, total-variation regularization "
    "{reg} (λ = {lam})":
        "Richardson-Lucy, PSF gaussiana σ {sigma:.2f} px, {iterations} iteraciones, regularización por "
        "variación total {reg} (λ = {lam})",
    "Presentation: local contrast {clahe}; {gray}. Single frame of {width} × {height} pixels.":
        "Presentación: contraste local {clahe}; {gray}. Fotograma único de {width} × {height} píxeles.",
    " (CLAHE, clip limit {clip:g})": " (CLAHE, límite de recorte {clip:g})",
    "grayscale": "escala de grises",
    "color": "en color",
    "Result": "Resultado",
    "Frames used": "Fotogramas usados",
    "{used} of {count}": "{used} de {count}",
    "Estimated noise σ": "Ruido σ estimado",
    "Immerkær method, 0-255, at the video resolution: reference {ref:.2f} → fused {fused:.2f} → final "
    "{final:.2f}. Deconvolution raises fine detail and noise together, so the last value is not a noise "
    "measure alone.":
        "Método de Immerkær, 0-255, a la resolución del vídeo: referencia {ref:.2f} → fusión {fused:.2f} → "
        "final {final:.2f}. La deconvolución realza a la vez el detalle fino y el ruido, por lo que el último "
        "valor no es solo una medida del ruido.",
    "Samples per output pixel": "Muestras por píxel de salida",
    "Sub-pixel phases covered (4 × 4 grid)": "Fases subpíxel cubiertas (cuadrícula 4 × 4)",
    "frame": "fotogr.",
    "time": "tiempo",
    "search": "búsqueda",
    "sharp.": "nitid.",
    "weight": "peso",
    "used": "usado",
    "model": "modelo",
    "note": "nota",
    "(reference)": "(referencia)",
    "Files": "Archivos",
    "aligned/: {count} aligned frames": "aligned/: {count} fotogramas alineados",
    "Note": "Nota",
    "The result is an enhancement of the frames listed above: it combines information that is present "
    "in them and does not add details. Fine details at the limit of the resolution, and characters that "
    "look alike, must be checked against the source frames before drawing conclusions.":
        "El resultado es una mejora de los fotogramas enumerados arriba: combina información presente en "
        "ellos y no añade detalles. Los detalles finos en el límite de la resolución, y los caracteres que se "
        "parecen entre sí, deben comprobarse en los fotogramas originales antes de sacar conclusiones.",
    "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.":
        "Software: {app} {version}, Python {python}, OpenCV {opencv}, NumPy {numpy}.",

    # ------------------------------------------------------------------ piede
    "Ready.": "Listo.",
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save":
        "Ctrl+1/2/3  página   ·   ← →  fotograma   ·   I / O  intervalo   ·   F5  fusionar   ·   Ctrl+S  guardar",
    "ffmpeg missing": "falta ffmpeg",
    "Operation failed": "Operación fallida",
    "ERROR - {title}: {message}": "ERROR - {title}: {message}",
    "Error: {title}": "Error: {title}",
    "INTERNAL ERROR": "ERROR INTERNO",
    "Internal error: details in the log.": "Error interno: detalles en el registro.",
}
