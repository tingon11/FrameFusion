# IdentiFrame — fusione multi-frame di fotogrammi video.  Copyright (C) 2026 Andrea Cumini <andrea@osintinfo.net>
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
    "Larger preview: hides the timeline, the I / O keys keep working (F11)":
        "Vista previa más grande: oculta la línea de tiempo, las teclas I / O siguen funcionando (F11)",
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
    "Range narrowed to the frames where the subject was followed: f{first} → f{last}.":
        "Intervalo reducido a los fotogramas en los que se siguió al sujeto: f{first} → f{last}.",
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
    "{name} is not an IdentiFrame report.": "{name} no es un informe de IdentiFrame.",
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
    "{count} frames decoded": "{count} fotogramas decodificados",
    "The video ended before the reference frame.": "El vídeo termina antes del fotograma de referencia.",
    "Range set with I / O": "Intervalo fijado con I / O",
    "Frames examined":
        "Fotogramas examinados",
    "Frames that make up the result":
        "Fotogramas que componen el resultado",
    "{count} frames left out because they come after more than {seconds:g} s without a good alignment: from there the subject is no longer confirmed (covered, too small or out of the frame).":
        "{count} fotogramas excluidos porque llegan tras más de {seconds:g} s sin una buena alineación: desde ahí el sujeto ya no está confirmado (tapado, demasiado pequeño o fuera del encuadre).",
    "Subject followed from f{first} to f{last}: beyond that it is missing, or not confirmed, for more than {seconds:g} s.":
        "Sujeto seguido de f{first} a f{last}: más allá, falta o no está confirmado durante más de {seconds:g} s.",
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
    "ffmpeg missing": "falta ffmpeg",
    "Operation failed": "Operación fallida",
    "ERROR - {title}: {message}": "ERROR - {title}: {message}",
    "Error: {title}": "Error: {title}",
    "INTERNAL ERROR": "ERROR INTERNO",
    "Internal error: details in the log.": "Error interno: detalles en el registro.",

    # ------------------------------------------------- tipo di soggetto (volti)
    "Subject type": "Tipo de sujeto",
    "Parameters set for the subject type: {subject}.": "Parámetros ajustados para el tipo de sujeto: {subject}.",
    "Face": "Rostro",
    "pose or expression differs from the reference": "pose o expresión distinta de la referencia",
    "Face: local non-rigid refinement after ECC on {count} frames, mean displacement {residual:.2f} px of the video.": "Rostro: refinamiento local no rígido tras ECC en {count} fotogramas, desplazamiento medio {residual:.2f} px del vídeo.",
    "Face: the area is too small for the local refinement ({size} px at least): rigid alignment only.": "Rostro: el área es demasiado pequeña para el refinamiento local ({size} px como mínimo): solo alineación rígida.",
    "simil.": "simil.",
    "Local refinement (face)": "Refinamiento local (rostro)",
    "not applied: area too small, rigid alignment only": "no aplicado: área demasiado pequeña, solo alineación rígida",
    "Face: the subject area is {width} × {height} pixels in the video. The fusion combines frames whose pose and expression match the reference and gives less weight to the parts that differ; it cannot create traits that no frame shows. With a face narrower than about 60 pixels the result can improve the overall appearance but not reveal identifying features: compare it with the reference frame and with the single frames before drawing any conclusion about identity.": "Rostro: el área del sujeto mide {width} × {height} píxeles en el vídeo. La fusión combina los fotogramas cuya pose y expresión coinciden con la referencia y da menos peso a las partes que difieren; no puede crear rasgos que ningún fotograma muestre. Con un rostro de menos de unos 60 píxeles de ancho, el resultado puede mejorar el aspecto general pero no revelar rasgos identificativos: compárelo con el fotograma de referencia y con los fotogramas sueltos antes de sacar conclusiones sobre la identidad.",
    "Face: after the rigid model, a local non-rigid refinement (Farneback optical flow between the reference and the aligned frame, smoothed and limited in amplitude) follows expression and head movement; a per-pixel confidence (forward-backward consistency and local correlation) weights every sample in the fusion. Frames whose local similarity to the reference is below {limit:.2f} are left out (pose or expression changed).": "Rostro: tras el modelo rígido, un refinamiento local no rígido (flujo óptico de Farneback entre la referencia y el fotograma alineado, suavizado y limitado en amplitud) sigue la expresión y los movimientos de la cabeza; una confianza por píxel (coherencia ida y vuelta y correlación local) pondera cada muestra en la fusión. Los fotogramas cuya similitud local con la referencia es inferior a {limit:.2f} se descartan (pose o expresión cambiada).",
    "{count} frames refined; mean local similarity to the reference {similarity:.2f}, mean local displacement {displacement:.2f} px of the video; {excluded} frames left out for a different pose or expression.": "{count} fotogramas refinados; similitud local media con la referencia {similarity:.2f}, desplazamiento local medio {displacement:.2f} px del vídeo; {excluded} fotogramas descartados por una pose o expresión distinta.",
    "Fusion: {subject}, f{first} → f{last}, reference f{ref}, area {width} × {height} at ({x}, {y}), ×{scale}, {method}": "Fusión: {subject}, f{first} → f{last}, referencia f{ref}, área {width} × {height} en ({x}, {y}), ×{scale}, {method}",

    # ------------------------------------------- riproduzione dell'anteprima
    "Ctrl+1/2/3  page   ·   ← →  frame   ·   Space  play   ·   I / O  range   ·   F5  fuse   ·   Ctrl+S  save": "Ctrl+1/2/3  página   ·   ← →  fotograma   ·   Espacio  reproducir   ·   I / O  intervalo   ·   F5  fusionar   ·   Ctrl+S  guardar",

    # ------------------------------ plausibilita' del warp, prospettiva, finestra dei volti
    "{count} frames aligned with a simpler motion model, because the chosen one gave an implausible deformation (scale, shear or perspective beyond the limits).": "{count} fotogramas alineados con un modelo de movimiento más simple, porque el elegido daba una deformación inverosímil (escala, cizalla o perspectiva fuera de los límites).",
    "persp.": "persp.",
    "Face: samples outside the ellipse inscribed in the area count little, and there the result shows the reference frame: the background moves differently from the face.": "Rostro: las muestras fuera de la elipse inscrita en el área cuentan poco, y allí el resultado muestra el fotograma de referencia: el fondo se mueve de forma distinta al rostro.",



    # ------------------------------------------- modelli e lettura dei caratteri (OCR)
    "Plate and Text: one rigid alignment per frame; the characters are read with fast-plate-ocr (plates) or PaddleOCR (texts, also on several lines). Face: after the alignment, a local non-rigid refinement follows expression and head movement, frames with a different pose are left out and the restoration is lighter. Changing the type loads its defaults.": "Matrícula y Texto: una alineación rígida por fotograma; los caracteres se leen con fast-plate-ocr (matrículas) o PaddleOCR (textos, también en varias líneas). Rostro: tras la alineación, un refinamiento local no rígido sigue la expresión y los movimientos de la cabeza, los fotogramas con una pose distinta se descartan y la restauración es más ligera. Cambiar el tipo carga sus valores predeterminados.",
    "Reads the plate (fast-plate-ocr) or the text (PaddleOCR) on the result and on independent fusions of groups of frames, and votes character by character": "Lee la matrícula (fast-plate-ocr) o el texto (PaddleOCR) en el resultado y en fusiones independientes de grupos de fotogramas, y vota carácter por carácter",
    "OCR models": "Modelos OCR",
    "The characters are read by two models run by OpenCV, downloaded on request into tools\\ocr and never part of the program (about 37 MB): fast-plate-ocr for plates (MIT, by ankandrew) and PaddleOCR PP-OCRv6 for texts in many languages (Apache 2.0, Baidu / PaddleOCR, ONNX conversion by RapidOCR). Every file is checked with its SHA-256 fingerprint; licenses and origin are saved next to the models.": "Los caracteres los leen dos modelos ejecutados por OpenCV, descargados a petición en tools\\ocr y nunca incluidos en el programa (unos 37 MB): fast-plate-ocr para las matrículas (MIT, de ankandrew) y PaddleOCR PP-OCRv6 para textos en muchos idiomas (Apache 2.0, Baidu / PaddleOCR, conversión ONNX de RapidOCR). Cada archivo se comprueba con su huella SHA-256; las licencias y la procedencia se guardan junto a los modelos.",
    "Downloading the OCR models…": "Descargando los modelos OCR…",
    "Reading the characters…": "Leyendo los caracteres…",
    "OCR models download failed": "Falló la descarga de los modelos OCR",
    "Downloading the OCR models: {plate} ({page_plate}), {text} ({page_text})": "Descargando los modelos OCR: {plate} ({page_plate}), {text} ({page_text})",
    "The OCR model for this subject type is missing: download it from the OCR models box of the Configuration page.": "Falta el modelo OCR para este tipo de sujeto: descárgalo desde el recuadro Modelos OCR de la página Configuración.",
    "press Read characters (automatic for plates and texts when the OCR models are ready)": "pulsa Leer caracteres (automático para matrículas y textos cuando los modelos OCR están listos)",
    "model confidence {confidence:.0f} %": "confianza del modelo {confidence:.0f} %",
    "OCR models check failed": "Falló la comprobación de los modelos OCR",
    "OCR: {plate} (plates), {text} (texts)": "OCR: {plate} (matrículas), {text} (textos)",
    "Missing (optional, for reading plates and texts): download them with the button on the right.": "Faltan (opcionales, para leer matrículas y textos): descárgalos con el botón de la derecha.",
    "OCR models ready: {path}": "Modelos OCR listos: {path}",
    "possible country ({share:.0f} %)": "país posible ({share:.0f} %)",
    "possible country: {region} ({share:.0f} %)": "país posible: {region} ({share:.0f} %)",
    "OK  ·  plates: {plate}  ·  texts: {text}  ·  {path}": "OK  ·  matrículas: {plate}  ·  textos: {text}  ·  {path}",
    "The model for texts is missing: download it with the button on the right.": "Falta el modelo para los textos: descárgalo con el botón de la derecha.",
    "The model for plates is missing: download it with the button on the right.": "Falta el modelo para las matrículas: descárgalo con el botón de la derecha.",
    "Text, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Texto, estándar: perspectiva, el 75 % más nítido, ×2, media robusta, deconvolución moderada. El punto de partida.",
    "Text at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Texto de noche o con ruido: más fotogramas, reducción de ruido media, deconvolución más suave con regularización fuerte, contraste local ligero, escala de grises.",
    "Distant, small text filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Texto lejano y pequeño filmado en muchos fotogramas: ×3, desplazar y sumar, casi todos los fotogramas, umbral de alineación más bajo.",
    "Text on a moving vehicle or filmed by a moving camera, with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Texto en un vehículo en movimiento o filmado por una cámara en movimiento, con desenfoque de movimiento: solo la mitad más nítida de los fotogramas, búsqueda del sujeto más tolerante, deconvolución más fuerte.",
    "Text in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Texto a la sombra o a contraluz: contraste local medio, escala de grises, reducción de ruido ligera.",
    "Plate": "Matrícula",
    "Text": "Texto",
    "No text line found inside the area: the whole area was read as one line.": "No se encontró ninguna línea de texto en el área: toda el área se leyó como una sola línea.",
    "No characters found: draw the area tight around the plate or the text, and check the scale and the restoration.": "No se encontraron caracteres: dibuja el área ajustada a la matrícula o al texto, y revisa la ampliación y la restauración.",
    "Cannot load the OCR model {name}: {error}": "No se puede cargar el modelo OCR {name}: {error}",
    "The OCR model configuration {name} is not valid.": "La configuración del modelo OCR {name} no es válida.",
    "Automatic reading by an OCR model, to be checked against the images: characters with a similar shape (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) can be misread in the same way in every reading, and the vote cannot see it. The possible country of the plate is an estimate of the model from the look of the plate, not a check.": "Lectura automática de un modelo OCR, a verificar en las imágenes: caracteres de forma parecida (8/B, 0/D/O, 1/I, 5/S, 2/Z, 6/G) pueden leerse mal del mismo modo en todas las lecturas, y el voto no puede notarlo. El país posible de la matrícula es una estimación del modelo a partir del aspecto de la matrícula, no una comprobación.",
    "{engine} ({license}), run by {runtime}: the result and {groups} fusions of independent groups of frames, each restored with the same parameters, are read; the readings are aligned and voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), ejecutado por {runtime}: se leen el resultado y {groups} fusiones de grupos independientes de fotogramas, cada una restaurada con los mismos parámetros; las lecturas se alinean y se votan carácter por carácter, ponderadas por la probabilidad que el modelo da a cada carácter (Quiala et al., 2023).",
    "{engine} ({license}), run by {runtime}: the text lines are found in the result, then every line is read on the result and on {groups} fusions of independent groups of frames, each restored with the same parameters; every line is voted character by character, weighted by the probability the model gives each character (Quiala et al., 2023).": "{engine} ({license}), ejecutado por {runtime}: las líneas de texto se encuentran en el resultado, luego cada línea se lee en el resultado y en {groups} fusiones de grupos independientes de fotogramas, cada una restaurada con los mismos parámetros; cada línea se vota carácter por carácter, ponderada por la probabilidad que el modelo da a cada carácter (Quiala et al., 2023).",
    "the whole area": "toda el área",
    "Model confidence": "Confianza del modelo",
    "Area read": "Área leída",
    "Text lines": "Líneas de texto",
    "x {x}, y {y}, {width} × {height} pixels of the result": "x {x}, y {y}, {width} × {height} píxeles del resultado",
    "Possible country": "País posible",
    "{confidence:.0f} %, mean probability of the characters read in the result": "{confidence:.0f} %, probabilidad media de los caracteres leídos en el resultado",
    "{region} ({share:.0f} % of the votes), estimated by the model from the look of the plate": "{region} ({share:.0f} % de los votos), estimado por el modelo a partir del aspecto de la matrícula",
    "OpenCV cannot load the downloaded model {name}.": "OpenCV no puede cargar el modelo descargado {name}.",
    "{name}: the downloaded file is not the expected one (its SHA-256 fingerprint is different).": "{name}: el archivo descargado no es el esperado (su huella SHA-256 es distinta).",
    "Read characters": "Leer caracteres",
    "CHARACTERS": "CARACTERES",
    "Characters read: {text}  ·  agreement {agreement:.0f} %  ·  {count} readings": "Caracteres leídos: {text}  ·  acuerdo {agreement:.0f} %  ·  {count} lecturas",
    "Character reading": "Lectura de caracteres",
    "reading…": "leyendo…",
    "no characters found: draw the area tight around the text": "no se encontraron caracteres: dibuje el área ajustada al texto",
    "agreement {agreement:.0f} %  ·  {count} readings": "acuerdo {agreement:.0f} %  ·  {count} lecturas",
    "Character reading failed: {error}": "La lectura de caracteres falló: {error}",
    "doubtful: {list}": "dudosos: {list}",
    "check by eye: {list}": "verificar a ojo: {list}",
    "Too few frames for independent groups: only the result was read, without a vote.": "Demasiado pocos fotogramas para grupos independientes: solo se leyó el resultado, sin voto.",
    "Character reading (OCR)": "Lectura de caracteres (OCR)",
    "illegible":
        "ilegible",
    "no character recognizable with enough confidence":
        "ningún carácter reconocible con confianza suficiente",
    "{count} illegible lines not shown":
        "{count} líneas ilegibles no mostradas",
    "not recognizable (?): {list}":
        "no reconocibles (?): {list}",
    "illegible: no character recognizable with enough confidence":
        "ilegible: ningún carácter reconocible con confianza suficiente",
    "? = character not recognizable":
        "? = carácter no reconocible",
    "Thresholds":
        "Umbrales",
    "a line counts as legible from a model confidence of {legible:.0f} %; a character is shown when its support (votes weighted by the probability the model gives it, over all the readings) reaches {support:.0f} %, otherwise «?».":
        "una línea cuenta como legible a partir de una confianza del modelo del {legible:.0f} %; un carácter se muestra cuando su apoyo (votos ponderados por la probabilidad que el modelo le da, sobre todas las lecturas) llega al {support:.0f} %, si no «?».",
    "Illegible lines":
        "Líneas ilegibles",
    "{count} lines found but not recognizable, not shown":
        "{count} líneas encontradas pero no reconocibles, no mostradas",
    "support":
        "apoyo",
    "Single readings (model output, before the thresholds)":
        "Lecturas individuales (salida del modelo, antes de los umbrales)",
    "Frames used in the fusion":
        "Fotogramas usados en la fusión",
    "All the {count} frames that make up the result: the subject area of each one, aligned to the reference frame as it enters the fusion, with its weight (R = reference frame).":
        "Los {count} fotogramas que componen el resultado: el área del sujeto de cada uno, alineada con el fotograma de referencia tal como entra en la fusión, con su peso (R = fotograma de referencia).",
    "Play / pause (Space)":
        "Reproducir / pausa (Espacio)",
    "Fit":
        "Ajustar",
    "Choose the language":
        "Elija el idioma",
    "Before you start":
        "Antes de empezar",
    "What {app} produces":
        "Qué produce {app}",
    "How the result is obtained":
        "Cómo se obtiene el resultado",
    "{app} does not create images: it combines the information really present in many frames of the same video. It follows the area you draw from frame to frame, aligns each frame to the reference frame with sub-pixel precision, discards the frames that do not align reliably and fuses the others with a weighted average that resists outliers. Each frame records the subject with a slightly different shift and different noise: combined, the noise drops and details spread over several frames emerge (multi-frame super-resolution). The deconvolution and the contrast corrections that follow are deterministic operations, with all their parameters written in the report.":
        "{app} no crea imágenes: combina la información realmente presente en muchos fotogramas del mismo vídeo. Sigue de fotograma en fotograma el área que dibuja, alinea cada fotograma con el de referencia con precisión inferior al píxel, descarta los fotogramas que no se alinean de forma fiable y fusiona los demás con una media ponderada resistente a los valores atípicos. Cada fotograma registra el sujeto con un desplazamiento ligeramente distinto y un ruido distinto: al combinarlos el ruido baja y aparecen detalles repartidos entre varios fotogramas (superresolución multifotograma). La deconvolución y las correcciones de contraste que siguen son operaciones deterministas, con todos sus parámetros escritos en el informe.",
    "The result is a reconstruction":
        "El resultado es una reconstrucción",
    "The image obtained is a reconstruction computed only from the real pixels of the frames used, each one listed in the report with its weight. No generative model or artificial intelligence adds, completes or imagines details: what is in none of the frames cannot appear in the result. A reconstruction can however contain artifacts (doubled edges where the alignment is imperfect, halos from the deconvolution) and is only as good as the source: always compare it with the original frames.":
        "La imagen obtenida es una reconstrucción calculada solo a partir de los píxeles reales de los fotogramas usados, cada uno listado en el informe con su peso. Ningún modelo generativo ni inteligencia artificial añade, completa o imagina detalles: lo que no está en ningún fotograma no puede aparecer en el resultado. Sin embargo, una reconstrucción puede contener artefactos (bordes duplicados donde la alineación es imperfecta, halos de la deconvolución) y vale lo que vale la fuente: compárela siempre con los fotogramas originales.",
    "Character reading and country are estimates":
        "La lectura de caracteres y el país son estimaciones",
    "The character reading (OCR) and the country of the plate are instead estimates of recognition models trained on examples, which always propose the most probable characters. The program combines several readings and marks as «?» or illegible what does not reach its thresholds, but even a reading shown in green can be wrong. They are an aid, not a proof: check every character by eye on the image.":
        "La lectura de caracteres (OCR) y el país de la matrícula son en cambio estimaciones de modelos de reconocimiento entrenados con ejemplos, que siempre proponen los caracteres más probables. El programa combina varias lecturas y marca con «?» o como ilegible lo que no alcanza sus umbrales, pero incluso una lectura mostrada en verde puede ser errónea. Son una ayuda, no una prueba: compruebe cada carácter a ojo en la imagen.",
    "I have understood that the result is a reconstruction from the frames of the video, in which nothing is invented, while the character reading and the attribution of the country are estimates to be checked.":
        "He comprendido que el resultado es una reconstrucción a partir de los fotogramas del vídeo, en la que nada es inventado, mientras que la lectura de caracteres y la atribución del país son estimaciones que hay que verificar.",
    "Accept and continue":
        "Aceptar y continuar",
    "Exit":
        "Salir",
    "Vote by position": "Voto por posición",
    "result": "resultado",
    "Reading": "Lectura",
    "Agreement": "Acuerdo",
    "Method": "Método",
    "Statement": "Declaración",
    "pos.": "pos.",
    "char.": "car.",
    "agreement": "acuerdo",
    "alternatives": "alternativas",
    "looks like": "se parece a",
    "group": "grupo",
    "source": "origen",
    "text": "texto",
    "conf.": "conf.",
    "frames": "fotogramas",

    # ---------------------------------------------------------------- preset di serie
    "Saved by you.": "Guardado por usted.",
    "Built-in presets for the subject type chosen on the Subject page, then yours.": "Ajustes incluidos para el tipo de sujeto elegido en la página Sujeto, después los suyos.",
    "«{name}» is a built-in preset: choose another name.": "«{name}» es un ajuste incluido: elija otro nombre.",
    "Plate, standard: perspective, sharpest 75 %, ×2, robust mean, moderate deconvolution. The starting point.": "Matrícula, estándar: perspectiva, el 75 % más nítido, ×2, media robusta, deconvolución moderada. El punto de partida.",
    "Plate at night or noisy: more frames, medium noise reduction, gentler deconvolution with strong regularization, light local contrast, grayscale.": "Matrícula de noche o con ruido: más fotogramas, reducción de ruido media, deconvolución más suave con regularización fuerte, contraste local ligero, escala de grises.",
    "Distant, small plate filmed in many frames: ×3, shift-and-add, almost all frames, lower alignment threshold.": "Matrícula lejana y pequeña filmada en muchos fotogramas: ×3, desplazar y sumar, casi todos los fotogramas, umbral de alineación más bajo.",
    "Moving or approaching vehicle with motion blur: only the sharpest half of the frames, more tolerant subject search, stronger deconvolution.": "Vehículo en movimiento o que se acerca, con desenfoque de movimiento: solo la mitad más nítida de los fotogramas, búsqueda del sujeto más tolerante, deconvolución más fuerte.",
    "Plate in shadow or against the light: medium local contrast, grayscale, light noise reduction.": "Matrícula a la sombra o a contraluz: contraste local medio, escala de grises, reducción de ruido ligera.",
    "Face, standard: affine, local refinement, light noise reduction, gentle deconvolution with strong regularization. The starting point.": "Rostro, estándar: afín, refinamiento local, reducción de ruido ligera, deconvolución suave con regularización fuerte. El punto de partida.",
    "Face at night or noisy: more frames, medium noise reduction, very light deconvolution.": "Rostro de noche o con ruido: más fotogramas, reducción de ruido media, deconvolución muy ligera.",
    "Face, minimal processing: fusion with auto levels only, no noise reduction and no deconvolution. The most conservative result.": "Rostro, procesado mínimo: fusión solo con niveles automáticos, sin reducción de ruido ni deconvolución. El resultado más prudente.",
    "Distant, small face: ×3, almost all frames, lower alignment threshold.": "Rostro lejano y pequeño: ×3, casi todos los fotogramas, umbral de alineación más bajo.",
    "Face in shadow or against the light: light local contrast, gentle deconvolution.": "Rostro a la sombra o a contraluz: contraste local ligero, deconvolución suave.",
}
