# Addendum al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia estática reproducible · `CZUR_CREATE=NO_VERIFICADO` · `NETWORK_ACTIVITY=NO_DEMOSTRADA`  
**Relacionado / Related:** [Delta principal CZUR ET24 Pro + Linux](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md)

> Este addendum documenta nueva evidencia obtenida sin ejecutar el binario objetivo. La presencia de módulos o capacidades de red no demuestra tráfico de red, exfiltración ni comportamiento malicioso.
>
> This addendum records new evidence obtained without executing the target binary. The presence of networking modules or capabilities does not demonstrate network traffic, exfiltration, or malicious behaviour.

---

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

### 1. Binario auditado

Ruta dentro del paquete extraído:

`/opt/apps/scanner/czur_authorized/czur_create`

Características observadas:

```text
ELF 64-bit LSB executable, x86-64
SYSV
dynamically linked
interpreter /lib64/ld-linux-x86-64.so.2
for GNU/Linux 2.6.32
stripped
size: 3,348,384 bytes
mtime del payload: 2025-03-31 14:03:49
SHA-256: cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9
BuildID SHA-1: 3f71fafa6e2e915b9bed491dd97e1bab785158de
```

Dependencias dinámicas directas observadas por `ldd`:

```text
libdl.so.2
libz.so.1
libpthread.so.0
libc.so.6
ld-linux-x86-64.so.2
```

### 2. Imports sensibles

La tabla dinámica del ELF mostró únicamente estos imports relevantes para creación/carga de procesos:

```text
dlopen
execvp
fork
```

No aparecieron en esa tabla dinámica directa símbolos como `connect`, `socket`, `send`, `recv`, `curl`, `SSL_*` o `HTTP_*`.

**Interpretación:** esto no demuestra ausencia de red. Un ejecutable puede cargar bibliotecas dinámicamente con `dlopen`, invocar otro proceso con `execvp`, o contener/interpolar un runtime que resuelva la red en otra capa.

### 3. Strings y fuerte indicio de runtime Python empaquetado

Entre las cadenas del binario aparecen nombres de módulos como:

```text
Crypto.Util._raw_api
cffi.api
charset_normalizer.api
http.server
multiprocessing.connection
multiprocessing.forkserver
multiprocessing.popen_forkserver
packaging._tokenizer
requests.api
socket
socketserver
urllib3.connection
urllib3.connectionpool
urllib3.util.connection
```

Esto demuestra que nombres de módulos Python asociados a HTTP/red y multiproceso están presentes en el artefacto. **No demuestra que se ejecuten ni que se establezca una conexión.**

La combinación de:

- ELF pequeño con pocas dependencias directas;
- `dlopen`, `fork` y `execvp`;
- abundantes nombres de módulos Python;
- y el hecho previamente observado de que `czur_create` y `CzurScanner` comparten el mismo BuildID ELF pese a tener SHA-256 distintos;

es **compatible con —y constituye un indicio fuerte de— un empaquetado tipo PyInstaller con un mismo bootloader y distintos archivos embebidos/anexados**. Todavía no se fija como hecho hasta detectar el `CArchive`/cookie de PyInstaller o abrir el ejecutable con una herramienta de inspección compatible.

La documentación oficial de PyInstaller explica que un ejecutable one-file puede llevar un `CArchive` concatenado al ejecutable, que el bootloader abre buscando al final del propio fichero, y que `pyi-archive_viewer` puede inspeccionar directamente ejecutables ELF empaquetados de este modo.

Fuentes de referencia:

- https://pyinstaller.org/en/stable/installation.html
- https://www.pyinstaller.org/en/stable/advanced-topics.html

### 4. Relación con `CzurScanner`

En la revisión anterior se observó:

```text
czur_create
SHA-256 cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9

CzurScanner
SHA-256 233bd777f24051b5681857aa3a66d637f0c10ce3e5bb8ca80edd70e96203142c

BuildID en ambos:
3f71fafa6e2e915b9bed491dd97e1bab785158de
```

Si se confirma PyInstaller, el BuildID idéntico dejaría de ser una anomalía especialmente extraña: sería coherente con dos aplicaciones construidas con el mismo bootloader ELF pero con distinto archivo Python/`CArchive` anexado, que sí altera el SHA-256 del fichero completo.

**Estado:** `HIPOTESIS_FUERTE / VERIFICACION_PENDIENTE`.

### 5. Búsqueda pública del helper

En búsquedas web realizadas el 2026-09-08 no se encontró un resultado indexado útil para el nombre exacto `czur_create` ni para su SHA-256 observado. Esto **no demuestra que no exista documentación o análisis público**; sólo indica que el helper no apareció en los resultados indexados consultados.

### 6. Próxima prueba estática, sin ejecutar código CZUR

La siguiente fase debe intentar identificar y listar un posible archivo PyInstaller sin ejecutar `czur_create`:

```bash
CREATE="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/czur_authorized/czur_create"
SCANNER="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/CzurScanner"

# Indicadores de PyInstaller / archivo anexado
strings -a "$CREATE" | grep -Ei '_MEIPASS|PYZ|pyi-|pyiboot|pyimod|CArchive|MEI' | head -200
strings -a "$SCANNER" | grep -Ei '_MEIPASS|PYZ|pyi-|pyiboot|pyimod|CArchive|MEI' | head -200

echo '===== TAIL CREATE ====='
tail -c 512 "$CREATE" | xxd -g1

echo '===== TAIL SCANNER ====='
tail -c 512 "$SCANNER" | xxd -g1

# Comparar dónde divergen ambos artefactos
cmp -l "$CREATE" "$SCANNER" | head -40 || true

# Tamaño y ELF/sections
stat -c '%n %s bytes' "$CREATE" "$SCANNER"
readelf -n "$CREATE" | sed -n '1,120p'
readelf -S "$CREATE" | tail -40
```

Para inspección especializada puede instalarse PyInstaller en un **venv de auditoría**, sin instalar ni ejecutar el paquete CZUR:

```bash
python3 -m venv "$HOME/CZUR-package-audit/venv-pyinstaller"
. "$HOME/CZUR-package-audit/venv-pyinstaller/bin/activate"
pip install --upgrade pip pyinstaller
pyi-archive_viewer -l "$CREATE"
```

`pyi-archive_viewer -l` inspecciona el archivo empaquetado; no es equivalente a ejecutar `czur_create`.

### 7. Síntesis incremental

```text
HECHO:
czur_create es ELF x86-64 stripped y el instalador pretende ejecutarlo como root.

HECHO:
su tabla dinámica importa dlopen, fork y execvp.

HECHO:
el fichero contiene nombres de requests, urllib3, socket, http.server y otros módulos Python.

NO DEMOSTRADO:
que czur_create abra sockets o realice tráfico de red.

INFERENCIA FUERTE:
el artefacto parece un runtime Python empaquetado, posiblemente PyInstaller.

SIGUIENTE FALSACIÓN:
detectar/abrir CArchive, identificar entrypoints y módulos realmente empaquetados antes de cualquier ejecución privilegiada.
```

---

## EN · English

### 1. Audited binary

Path inside the extracted package:

`/opt/apps/scanner/czur_authorized/czur_create`

Observed characteristics:

```text
ELF 64-bit LSB executable, x86-64
SYSV
dynamically linked
interpreter /lib64/ld-linux-x86-64.so.2
for GNU/Linux 2.6.32
stripped
size: 3,348,384 bytes
payload mtime: 2025-03-31 14:03:49
SHA-256: cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9
BuildID SHA-1: 3f71fafa6e2e915b9bed491dd97e1bab785158de
```

Direct dynamic dependencies observed through `ldd`:

```text
libdl.so.2
libz.so.1
libpthread.so.0
libc.so.6
ld-linux-x86-64.so.2
```

### 2. Sensitive imports

The ELF dynamic table showed only these imports relevant to process creation/loading:

```text
dlopen
execvp
fork
```

No symbols such as `connect`, `socket`, `send`, `recv`, `curl`, `SSL_*` or `HTTP_*` appeared in that direct dynamic table.

**Interpretation:** this does not demonstrate absence of networking. An executable may dynamically load libraries with `dlopen`, invoke another process with `execvp`, or contain/embed a runtime that resolves networking in another layer.

### 3. Strings and strong indication of a packaged Python runtime

Strings in the binary include module names such as:

```text
Crypto.Util._raw_api
cffi.api
charset_normalizer.api
http.server
multiprocessing.connection
multiprocessing.forkserver
multiprocessing.popen_forkserver
packaging._tokenizer
requests.api
socket
socketserver
urllib3.connection
urllib3.connectionpool
urllib3.util.connection
```

This demonstrates that Python module names associated with HTTP/networking and multiprocessing are present in the artifact. **It does not demonstrate that they execute or that a connection is established.**

The combination of:

- a small ELF with few direct dependencies;
- `dlopen`, `fork` and `execvp`;
- abundant Python module names;
- and the previously observed fact that `czur_create` and `CzurScanner` share the same ELF BuildID despite different SHA-256 hashes;

is **compatible with —and constitutes a strong indication of— PyInstaller-style packaging using the same bootloader with different embedded/appended files**. This is not fixed as fact until the PyInstaller `CArchive`/cookie is detected or the executable is opened with a compatible inspection tool.

PyInstaller's official documentation explains that a one-file executable may carry a `CArchive` concatenated to the executable, that the bootloader opens it by searching at the end of its own file, and that `pyi-archive_viewer` can directly inspect ELF executables packaged in this way.

Reference sources:

- https://pyinstaller.org/en/stable/installation.html
- https://www.pyinstaller.org/en/stable/advanced-topics.html

### 4. Relationship with `CzurScanner`

The previous review observed:

```text
czur_create
SHA-256 cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9

CzurScanner
SHA-256 233bd777f24051b5681857aa3a66d637f0c10ce3e5bb8ca80edd70e96203142c

BuildID in both:
3f71fafa6e2e915b9bed491dd97e1bab785158de
```

If PyInstaller is confirmed, the identical BuildID would cease to be a particularly unusual anomaly: it would be consistent with two applications built with the same ELF bootloader but different appended Python/`CArchive` files, which do alter the SHA-256 of the complete file.

**State:** `STRONG_HYPOTHESIS / VERIFICATION_PENDING`.

### 5. Public search for the helper

Web searches performed on 2026-09-08 did not find a useful indexed result for the exact name `czur_create` or its observed SHA-256. This **does not demonstrate that public documentation or analysis does not exist**; it only means the helper did not appear in the indexed results consulted.

### 6. Next static test, without executing CZUR code

The next phase should attempt to identify and list a possible PyInstaller archive without executing `czur_create`:

```bash
CREATE="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/czur_authorized/czur_create"
SCANNER="$HOME/CZUR-package-audit/rootfs/tmp/opt/apps/scanner/CzurScanner"

# PyInstaller indicators / appended archive
strings -a "$CREATE" | grep -Ei '_MEIPASS|PYZ|pyi-|pyiboot|pyimod|CArchive|MEI' | head -200
strings -a "$SCANNER" | grep -Ei '_MEIPASS|PYZ|pyi-|pyiboot|pyimod|CArchive|MEI' | head -200

echo '===== TAIL CREATE ====='
tail -c 512 "$CREATE" | xxd -g1

echo '===== TAIL SCANNER ====='
tail -c 512 "$SCANNER" | xxd -g1

# Compare where both artifacts diverge
cmp -l "$CREATE" "$SCANNER" | head -40 || true

# Size and ELF/sections
stat -c '%n %s bytes' "$CREATE" "$SCANNER"
readelf -n "$CREATE" | sed -n '1,120p'
readelf -S "$CREATE" | tail -40
```

For specialised inspection, PyInstaller can be installed in an **audit venv**, without installing or executing the CZUR package:

```bash
python3 -m venv "$HOME/CZUR-package-audit/venv-pyinstaller"
. "$HOME/CZUR-package-audit/venv-pyinstaller/bin/activate"
pip install --upgrade pip pyinstaller
pyi-archive_viewer -l "$CREATE"
```

`pyi-archive_viewer -l` inspects the packaged archive; it is not equivalent to executing `czur_create`.

### 7. Incremental synthesis

```text
FACT:
czur_create is a stripped x86-64 ELF and the installer intends to run it as root.

FACT:
its dynamic table imports dlopen, fork and execvp.

FACT:
the file contains names for requests, urllib3, socket, http.server and other Python modules.

NOT DEMONSTRATED:
that czur_create opens sockets or performs network traffic.

STRONG INFERENCE:
the artifact appears to be a packaged Python runtime, possibly PyInstaller.

NEXT FALSIFICATION:
detect/open CArchive, identify entrypoints and actually packaged modules before any privileged execution.
```
