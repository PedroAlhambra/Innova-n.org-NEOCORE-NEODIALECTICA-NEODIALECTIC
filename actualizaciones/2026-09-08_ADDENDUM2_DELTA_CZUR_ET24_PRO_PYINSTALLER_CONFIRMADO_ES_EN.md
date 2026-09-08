# Addendum II al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum II to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia estática reproducible · `PYINSTALLER=CONFIRMADO` · `NETWORK_ACTIVITY=NO_DEMOSTRADA`  
**Relacionado / Related:** [Delta principal](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md) · [Addendum I](./2026-09-08_ADDENDUM_DELTA_CZUR_ET24_PRO_CZUR_CREATE_STATIC_ES_EN.md)

---

## ES · Castellano

### 1. PyInstaller queda confirmado

La hipótesis abierta en el Addendum I queda confirmada mediante inspección con `pyi-archive_viewer` instalado en un entorno virtual separado. Tanto `czur_authorized/czur_create` como `CzurScanner` son ejecutables PyInstaller con `PKG/CArchive` y un archivo interno `PYZ-00.pyz`.

Marcadores observados en ambos artefactos:

```text
_MEIPASS
_MEIPASS2
pyi-
pyimod01_archive
pyimod02_importers
pyimod03_ctypes
pyiboot01_bootstrap
PYZ-00.pyz
```

`pyi-archive_viewer -l` identificó explícitamente:

```text
Contents of 'czur_create' (PKG/CArchive)
Contents of 'CzurScanner' (PKG/CArchive)
```

Por tanto:

`PYINSTALLER_STYLE = HIPOTESIS_FUERTE` pasa a `PYINSTALLER = HECHO CONFIRMADO`.

### 2. `czur_create` es un wrapper Python muy pequeño sobre un PYZ grande

El CArchive de `czur_create` contiene principalmente el bootloader/runtime de PyInstaller, hooks de ejecución y un entrypoint `main` muy pequeño:

```text
main: 315 bytes comprimidos / 430 bytes sin comprimir
PYZ-00.pyz: 3,275,881 bytes
```

También aparecen los hooks:

```text
pyi_rth_subprocess
pyi_rth_pkgutil
pyi_rth_multiprocessing
pyi_rth_inspect
pyi_rth_pkgres
pyi_rth_setuptools
```

Esto explica por qué el ELF presentaba pocas dependencias directas pero strings de módulos Python de alto nivel: la mayor parte de la lógica está empaquetada dentro del archivo Python interno.

### 3. `CzurScanner` confirma una aplicación Python/PySide2 con múltiples funciones propietarias

El CArchive de `CzurScanner` contiene un entrypoint `main`, runtime hook de PySide2 y numerosos módulos específicos de aplicación antes del `PYZ-00.pyz`, que mide 7,856,218 bytes.

Entre los nombres observados:

```text
main_window_scan_preview
item_scan_preview_select_resolution_combo
item_laser_auxiliary_process
item_advanced_crop
main_window_batch_OCR
module_czocr
main_window_batch_PDF
main_window_batch_TIFF
main_window_batch_edge_clipping
main_window_batch_fill_hole
main_window_batch_hue_contrast
main_window_batch_watermark
main_window_auth_validate
module_authorized
main_window_serial_enter_dialog
pop_authorization_dialog
pop_offline_report_dialog
pop_purchase_channel_dialog
main_window_submit_wrong_data
main_window_suggestion
main_window_formula_web_window
main_window_pushmessage_dialog
email_input_dialog
pop_email_input_dialog
```

Estos nombres son evidencia de que el software propietario incluye módulos para previsualización, resolución, láser/auxiliares, recorte avanzado, OCR, PDF/TIFF, procesado por lotes, autorización/licencia, informes, canal de compra, sugerencias, funciones web, push y correo.

**La existencia de esos módulos no demuestra que todos se ejecuten en una sesión concreta ni que transmitan datos sin consentimiento.**

### 4. El BuildID compartido deja de ser una anomalía fuerte

La observación anterior de que `czur_create` y `CzurScanner` comparten el mismo BuildID ELF pese a tener SHA-256 y tamaños distintos es coherente con el uso del mismo bootloader PyInstaller y distintos archivos CArchive/PYZ anexados.

Tamaños observados:

```text
czur_create: 3,348,384 bytes
CzurScanner: 8,549,336 bytes
```

Por tanto, este punto ya no se trata como anomalía inexplicada del binario.

### 5. Estado de red y autorización

Permanece vigente la separación:

```text
MODULOS/SDK/CAPACIDAD DE RED PRESENTES = HECHO
TRAFICO SALIENTE REAL = NO VERIFICADO
EXFILTRACION = NO DEMOSTRADA
MALWARE = NO DEMOSTRADO
```

La siguiente prueba debe ser estática y dirigida al `PYZ-00.pyz` y a los entrypoints antes de cualquier ejecución privilegiada.

### 6. Siguiente fase reproducible

PyInstaller documenta que `pyi-archive_viewer` puede abrir archivos internos mediante `O nombre`, extraer un miembro con `X nombre` y listar recursivamente con `-r`.

Pruebas recomendadas:

```bash
CREATE="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/czur_authorized/czur_create"
SCANNER="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/CzurScanner"

pyi-archive_viewer -r -l "$CREATE" > "$HOME/CZUR-package-audit/czur_create_recursive.txt"
pyi-archive_viewer -r -l "$SCANNER" > "$HOME/CZUR-package-audit/czurscanner_recursive.txt"

grep -Ei 'aliyun|requests|urllib3|socket|http|ssl|cryptography|oauth|token|auth|upload|download|update|push|email|api|server|report' \
  "$HOME/CZUR-package-audit/czur_create_recursive.txt" \
  "$HOME/CZUR-package-audit/czurscanner_recursive.txt"
```

También debe extraerse el entrypoint `main` de `czur_create` con el visor interactivo para analizar su bytecode sin ejecutar el programa:

```text
pyi-archive_viewer "$CREATE"
X main
```

El visor pedirá un nombre de salida. La extracción no ejecuta el target.

### 7. Síntesis incremental

| Hallazgo | Estado |
|---|---|
| `czur_create` empaquetado con PyInstaller | **CONFIRMADO** |
| `CzurScanner` empaquetado con PyInstaller | **CONFIRMADO** |
| CArchive / `PYZ-00.pyz` | **CONFIRMADO** |
| PySide2/runtime GUI en scanner | **CONFIRMADO** |
| módulos de OCR/procesado/autorización/web/push/email | **CONFIRMADO POR INVENTARIO** |
| uso efectivo de red | **NO VERIFICADO** |
| comportamiento malicioso | **NO DEMOSTRADO** |

---

## EN · English

### 1. PyInstaller is now confirmed

Static inspection with `pyi-archive_viewer` confirms that both `czur_authorized/czur_create` and `CzurScanner` are PyInstaller executables containing a `PKG/CArchive` and an embedded `PYZ-00.pyz`.

The earlier strong hypothesis therefore becomes a confirmed fact.

`czur_create` contains a very small `main` entrypoint (430 bytes uncompressed) plus a ~3.28 MB PYZ archive. `CzurScanner` contains a PySide2 runtime hook, many application-specific modules and a ~7.86 MB PYZ archive.

Module names observed in the scanner bundle cover preview/resolution, laser assistance, advanced crop, OCR, PDF/TIFF, image processing, authorization/licensing, offline reports, purchase channel, suggestions, web-window, push-message and email-related UI.

These module names establish packaged functionality only. They do not prove that all features execute in a given session or that data is transmitted without user action.

### 2. Current classification

| Finding | State |
|---|---|
| PyInstaller packaging for `czur_create` | **CONFIRMED** |
| PyInstaller packaging for `CzurScanner` | **CONFIRMED** |
| CArchive / embedded `PYZ-00.pyz` | **CONFIRMED** |
| scanner PySide2/runtime GUI | **CONFIRMED** |
| OCR/processing/auth/web/push/email modules present | **CONFIRMED BY INVENTORY** |
| actual outbound network traffic | **NOT VERIFIED** |
| malicious behaviour | **NOT DEMONSTRATED** |

Next step: recursively enumerate the embedded PYZ contents and extract/disassemble the small `czur_create` entrypoint before any privileged execution.

---

## Referencia técnica / Technical reference

PyInstaller official advanced topics / archive viewer documentation:

https://pyinstaller.org/en/stable/advanced-topics.html

`NEW_EVIDENCE → REPRODUCTION → CLASSIFICATION → ADDENDUM`