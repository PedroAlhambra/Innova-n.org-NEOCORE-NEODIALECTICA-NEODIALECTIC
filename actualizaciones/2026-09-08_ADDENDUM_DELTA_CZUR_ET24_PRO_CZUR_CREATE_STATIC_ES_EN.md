# Addendum al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia estática reproducible · `CZUR_CREATE=NO_VERIFICADO` · `NETWORK_ACTIVITY=NO_DEMOSTRADA`  
**Relacionado / Related:** [Delta principal CZUR ET24 Pro + Linux](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md)

> Este addendum documenta nueva evidencia obtenida sin ejecutar el binario objetivo. La presencia de módulos o capacidades de red no demuestra tráfico de red, exfiltración ni comportamiento malicioso.
>
> This addendum records new evidence obtained without executing the target binary. The presence of networking modules or capabilities does not demonstrate network traffic, exfiltration, or malicious behaviour.

---

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

`czur_authorized/czur_create` is a stripped x86-64 dynamically linked ELF, 3,348,384 bytes, SHA-256 `cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9`, with BuildID `3f71fafa6e2e915b9bed491dd97e1bab785158de`.

Direct dynamic dependencies observed were limited to `libdl`, `libz`, `libpthread`, `libc` and the ELF loader. Relevant dynamic imports included `dlopen`, `execvp` and `fork`; direct `connect/socket/send/recv/curl/SSL` symbols were not observed.

This does **not** establish that the program cannot use networking: it may dynamically load code, launch another process or embed a higher-level runtime.

### 2. Embedded-module evidence

Strings include Python module names such as `requests.api`, `urllib3.connection`, `socket`, `socketserver`, `http.server`, `Crypto.Util._raw_api`, `cffi.api` and several `multiprocessing` modules.

These strings demonstrate packaged capability/names, not executed network activity.

The combination of a small ELF bootloader-like dependency set, Python module strings, process/dynamic-loading imports, and the previously observed identical ELF BuildID for `czur_create` and `CzurScanner` despite different whole-file SHA-256 values is strongly compatible with a PyInstaller-style bundle using a common bootloader plus different appended archives. This remains a **strong hypothesis pending direct CArchive/cookie detection**.

PyInstaller's own documentation states that its one-file executable can carry an appended `CArchive` and that `pyi-archive_viewer` can inspect ELF executables built in this form:

- https://pyinstaller.org/en/stable/installation.html
- https://www.pyinstaller.org/en/stable/advanced-topics.html

### 3. Current classification

| Question | State |
|---|---|
| `czur_create` executed as root by installer path | **FACT** |
| direct process/dynamic loading capability | **FACT** |
| Python HTTP/socket module names embedded | **FACT** |
| actual outbound network traffic | **NOT VERIFIED** |
| PyInstaller-style packaging | **STRONG HYPOTHESIS / PENDING VERIFICATION** |
| malicious behaviour | **NOT DEMONSTRATED** |

Next step: inspect for PyInstaller markers/CArchive and enumerate embedded entrypoints **without executing the target**. Only after static extraction should dynamic execution be considered inside an isolated snapshot/container/VM with filesystem, process and network tracing.
