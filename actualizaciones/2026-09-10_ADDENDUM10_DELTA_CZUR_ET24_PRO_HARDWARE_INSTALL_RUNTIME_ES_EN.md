# Addendum X · CZUR ET24 Pro Linux · hardware real, instalación dinámica y primera ejecución

**Fecha:** 2026-09-10  
**Estado:** auditoría dinámica incremental / síntesis abierta  
**Ámbito:** CZUR ET24 Pro + paquete oficial CZUR Scanner Linux 1.0.20250413  
**Continuidad:** amplía el [delta inicial](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md) y los addenda estáticos previos, incluido [Addendum IX](./2026-09-09_ADDENDUM9_DELTA_CZUR_ET24_PRO_DEFINE_NETWORK_TIME_PATH_ES_EN.md).

## ES

### 1. Hardware real: UVC/V4L2 confirmado

La fase dinámica se realizó sobre Debian 13 en una VM con el controlador USB completo pasado directamente al invitado. El escáner conectado se enumeró correctamente como dispositivo UVC:

```text
USB VID:PID              04fc:6333
descriptor USB           Sunplus Technology Co., Ltd Siri A9 UVC chipset
driver Linux             uvcvideo
/dev/video0              Video Capture + Streaming
/dev/video1              Metadata Capture UVC
producto V4L2            QHD CAMERA: CZUR
```

`/dev/video0` expone, entre otros, estos modos MJPEG:

```text
7424x5568 @ 4.5 fps
4000x3000 @ 10 fps
3840x2160 @ 30 fps
3072x1728 @ 30 fps
1920x1080 @ 30 fps
```

También expone modos YUYV a menor frecuencia. El usuario dispone de acceso `rw` mediante el grupo/ACL de vídeo.

Se realizó una captura local a **7424x5568** mediante V4L2/FFmpeg antes de instalar la aplicación del fabricante. La imagen fue abierta y revisada localmente y el usuario confirmó calidad visual correcta. Por tanto, la cadena física básica —USB, passthrough, `uvcvideo`, captura y sensor/óptica— queda funcionalmente confirmada.

### 2. Identidad exacta del paquete instalado

```text
Package:      scanner
Version:      1.0.20250413
Architecture: amd64
SHA-256:      0b7618a390a695af151f1aa9ba8d6a1e8dd9ce922ab103ccd52a0e0a86509a91
```

Antes de la instalación se creó un snapshot/checkpoint de la VM para permitir reversión de la prueba.

### 3. Resultado de instalación dinámica

La instalación real mediante `dpkg` terminó correctamente:

```text
dpkg_rc = 0
status  = install ok installed scanner 1.0.20250413
```

No estaba disponible `strace`, por lo que esta ejecución **no dispone de traza de syscalls del instalador**. Esto limita esa capa concreta de evidencia, pero no invalida el registro de ficheros, permisos, servicios, procesos y estado de red tomado antes/después.

Durante `postinst` se observó ejecución privilegiada de:

```text
/usr/bin/sh ./setup.sh
./czur_create --logname=<usuario>
sed -i ... /lib/udev/uvcdynctrl
```

`czur_create` devolvió además:

```text
{"key": "", "res": true, "type": 7, "str_result": "create permission success"}
```

La instalación creó el directorio local de usuario `~/.czur` y un lanzador gráfico que ejecuta `CzurScanner` desde `/opt/apps/scanner`, precargando `libczurusb-1.0.so` y forzando backend X11.

### 4. Hallazgo confirmado: permisos excesivamente abiertos

La hipótesis estática sobre `chmod -R 777` quedó confirmada dinámicamente. Tras instalar se contabilizaron **3.061 entradas world-writable**, todas bajo `/opt/apps/scanner`:

```text
2700  ficheros   -rwxrwxrwx
 233  symlinks   lrwxrwxrwx
 128  directorios drwxrwxrwx
--------------------------
3061  entradas
```

Distribución de propietarios observada:

```text
2832  usuario:usuario
 229  root:root
```

El propio `/opt/apps/scanner` quedó con modo `0777`. Esto se clasifica como **problema real de hardening del instalador**, no como evidencia de malware.

### 5. Hallazgo confirmado: reglas udev demasiado amplias

La instalación dejó `/etc/udev/rules.d/czurscanner.rules` con reglas como:

```text
SUBSYSTEMS=="usb", ATTRS{idVendor}=="04fc", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1e4f", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1e4e", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="5929", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0400", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="23a4", ATTRS{idProduct}=="*", MODE:="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2109", ATTRS{idProduct}=="*", MODE:="0666"
KERNEL=="ttyUSB*", ATTRS{idVendor}=="1a86", MODE:="0666"
KERNEL=="ttyS1", MODE:="0666"
```

Además, `systemd-udevd` registró que el archivo de reglas estaba marcado como ejecutable y recomendó retirar esos bits, aunque continuó procesándolo.

La regla para `04fc` coincide con el fabricante USB del dispositivo probado, pero acepta cualquier producto de ese vendor (`idProduct="*"`) y utiliza acceso global `0666`; el resto de reglas amplía aún más la superficie. Se mantiene la clasificación **REPAIR** para endurecimiento posterior, después de verificar compatibilidad funcional.

### 6. Servicio residente: hipótesis cerrada negativamente para este build

Tras la instalación:

```text
unidad systemd CZUR detectada     NO
servicio CZUR activo              NO
proceso CZUR persistente          NO
```

Esto refuerza la conclusión de los addenda estáticos: la rama de instalación que hacía pensar en `CZURPlugin.service` no se materializa como servicio residente en este paquete/build probado.

### 7. Primera ejecución de la aplicación

La aplicación oficial fue arrancada y probada de forma interactiva con material no sensible. El resultado funcional preliminar comunicado por el usuario es:

```text
aplicación abre / funciona        SÍ, preliminar
escáner usable                    SÍ, preliminar
comportamiento anómalo menor      OBSERVADO POR EL USUARIO, NO CARACTERIZADO
causa                             NO DETERMINADA
reinicio antes de continuar       DECIDIDO
```

No se asigna causa al comportamiento extraño observado: puede ser aplicación, estado USB/UVC, sesión gráfica, estado posterior a instalación u otro factor. Debe reproducirse después de reiniciar antes de elevarlo a defecto del producto.

### 8. Red: qué está y qué no está demostrado

El análisis estático previo ya demostró **capacidad de red**, incluidos mecanismos de diagnóstico/reporting y componentes Alibaba OSS, pero no demostró subida automática de escaneos normales.

Para esta primera ejecución se realizó además una captura de red a nivel del host/VM. Debido a que la captura incluye tráfico general de la VM y no atribución directa por proceso, el PCAP bruto **no se publica ni se incorpora al repositorio**. Una búsqueda exacta de cadenas en esa captura no encontró:

```text
internal.czur.cc
worldtimeapi.org
oss-cn-beijing.aliyuncs.com
aliyuncs.com
czur.cc
```

Este resultado es solamente evidencia negativa limitada: **la ausencia de esas cadenas literales en un PCAP no demuestra ausencia total de tráfico CZUR**, porque puede existir resolución DNS previa, cifrado, conexión por IP, QUIC u otros mecanismos. La atribución de egress normal a `CzurScanner` continúa pendiente de una prueba dinámica más controlada.

### 9. Clasificación actual

```text
HARDWARE USB/UVC                    PASS
CAPTURA NATIVA 7424x5568            PASS
CALIDAD VISUAL BÁSICA               PASS (revisión local del usuario)
INSTALACIÓN FUNCIONAL               PASS
dpkg                                PASS
SERVICIO RESIDENTE CZUR             NO EVIDENCIADO
PERMISOS DEL INSTALADOR             REPAIR — 3061 entradas world-writable
REGLAS UDEV                         REPAIR — MODE 0666 y alcance amplio
CAPACIDAD DE RED DEL SOFTWARE       CONFIRMADA ESTÁTICAMENTE
UPLOAD DE DIAGNÓSTICO/LOGS          CONFIRMADO COMO CAPACIDAD
UPLOAD AUTOMÁTICO DE ESCANEOS       NO DEMOSTRADO
EGRESS CZUR EN USO NORMAL           PENDIENTE DE ATRIBUCIÓN DINÁMICA
ESTABILIDAD DE PRIMERA EJECUCIÓN    PROVISIONAL — anomalía no caracterizada
MALWARE                             NO DEMOSTRADO
```

### 10. Próxima prueba

Después del reinicio:

1. comprobar persistencia de detección UVC y arranque de `CzurScanner`;
2. repetir una operación de escaneo no sensible y caracterizar cualquier anomalía;
3. capturar egress con atribución más estrecha;
4. comprobar botón físico, Auto Scan/paso manual de página, recorte, tratamiento de libro y exportación;
5. sólo después, endurecer permisos de `/opt/apps/scanner` y estrechar reglas udev, verificando que el producto sigue funcionando.

No existe en este punto una razón de hardware para devolver el ET24 Pro. La decisión de conservarlo debe depender principalmente de estabilidad real del software, funcionalidad del flujo de libro y cierre de la prueba de red/hardening.

---

## EN

### Dynamic result summary

The CZUR ET24 Pro was dynamically tested on Debian 13 with direct USB-controller passthrough to the guest. The unit enumerates correctly as USB `04fc:6333`, uses the standard Linux `uvcvideo` driver, exposes `/dev/video0` as the real capture node and `/dev/video1` as UVC metadata, and supports MJPEG up to **7424x5568 at 4.5 fps**, plus 4K/30 and several intermediate modes.

A native V4L2/FFmpeg capture at 7424x5568 succeeded before vendor-software installation. The user visually inspected the result and reported good image quality. Basic physical, optical and Linux/UVC operation therefore passes.

The exact package dynamically installed was:

```text
Package:      scanner
Version:      1.0.20250413
Architecture: amd64
SHA-256:      0b7618a390a695af151f1aa9ba8d6a1e8dd9ce922ab103ccd52a0e0a86509a91
```

A VM snapshot/checkpoint was created before installation. `dpkg` completed with return code 0. `strace` was not installed, so syscall-level installer tracing is absent from this run.

Dynamic installation confirmed the static hardening concern: **3,061 world-writable entries** exist under `/opt/apps/scanner` after installation: 2,700 regular files, 233 symlinks and 128 directories. The application root itself is mode `0777`.

The package also installs broad udev rules using `MODE="0666"`, including a wildcard product match for vendor `04fc`. `systemd-udevd` warned that the rules file itself was executable. These findings warrant **REPAIR/hardening**, but are not evidence of malware.

No CZUR systemd unit, active CZUR service or persistent CZUR process was observed after installation. This dynamically supports the prior static conclusion that the `CZURPlugin.service` branch is residual/inactive for the tested build.

The first interactive application run was preliminarily functional according to the user, although an unspecified odd behaviour was noticed. A reboot was chosen before continuing. The anomaly is not yet attributed to the application or hardware.

A host-side VM traffic capture was also collected. Raw PCAP data is intentionally not published because it contains unrelated VM traffic. Exact byte-string searches did not find `internal.czur.cc`, `worldtimeapi.org`, `oss-cn-beijing.aliyuncs.com`, `aliyuncs.com` or `czur.cc`. This is only limited negative evidence and **does not prove absence of CZUR traffic**; encrypted/IP-only/cached-resolution paths remain possible.

### Current classification

```text
USB/UVC HARDWARE                    PASS
7424x5568 NATIVE CAPTURE            PASS
BASIC VISUAL QUALITY                PASS (local user review)
FUNCTIONAL INSTALL                  PASS
RESIDENT CZUR SERVICE               NOT EVIDENCED
INSTALLER PERMISSIONS               REPAIR
UDEV RULES                          REPAIR
NETWORK CAPABILITY                  STATICALLY CONFIRMED
DIAGNOSTIC/LOG UPLOAD CAPABILITY    CONFIRMED
AUTOMATIC NORMAL-SCAN UPLOAD        NOT DEMONSTRATED
NORMAL-USE CZUR EGRESS              PENDING DYNAMIC ATTRIBUTION
FIRST-RUN STABILITY                 PROVISIONAL
MALWARE                             NOT DEMONSTRATED
```

The next controlled run after reboot should reproduce or dismiss the odd behaviour, validate the physical scan button / Auto Scan / book-processing workflow, obtain tighter process-attributed network evidence, and only then harden permissions and udev rules while preserving functionality.

`CAPABILITY != INVOCATION != TRAFFIC != IMPROPER TRANSMISSION`.