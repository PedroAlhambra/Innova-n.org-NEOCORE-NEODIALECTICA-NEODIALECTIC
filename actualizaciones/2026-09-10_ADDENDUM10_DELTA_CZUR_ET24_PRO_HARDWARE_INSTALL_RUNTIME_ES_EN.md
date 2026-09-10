# Addendum X · CZUR ET24 Pro Linux · hardware real, instalación dinámica y primera ejecución

**Fecha:** 2026-09-10  
**Estado:** auditoría dinámica incremental / síntesis abierta  
**Ámbito:** CZUR ET24 Pro + paquete oficial CZUR Scanner Linux 1.0.20250413  
**Continuidad:** amplía el [delta inicial](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md) y los addenda estáticos previos, incluido [Addendum IX](./2026-09-09_ADDENDUM9_DELTA_CZUR_ET24_PRO_DEFINE_NETWORK_TIME_PATH_ES_EN.md).

[ES · Castellano](#es) · [EN · English](#en)

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

`CAPACIDAD != INVOCACIÓN != TRÁFICO != TRANSMISIÓN INDEBIDA`.

---

## EN

### 1. Real hardware: UVC/V4L2 confirmed

The dynamic phase was performed on Debian 13 in a VM with the complete USB controller passed directly to the guest. The connected scanner enumerated correctly as a UVC device:

```text
USB VID:PID              04fc:6333
USB descriptor           Sunplus Technology Co., Ltd Siri A9 UVC chipset
Linux driver             uvcvideo
/dev/video0              Video Capture + Streaming
/dev/video1              UVC Metadata Capture
V4L2 product             QHD CAMERA: CZUR
```

`/dev/video0` exposes, among others, these MJPEG modes:

```text
7424x5568 @ 4.5 fps
4000x3000 @ 10 fps
3840x2160 @ 30 fps
3072x1728 @ 30 fps
1920x1080 @ 30 fps
```

It also exposes YUYV modes at lower frame rates. The user has `rw` access through the video group/ACL.

A local capture at **7424x5568** was performed through V4L2/FFmpeg before installing the vendor application. The image was opened and reviewed locally and the user confirmed correct visual quality. Therefore the basic physical chain —USB, passthrough, `uvcvideo`, capture and sensor/optics— is functionally confirmed.

### 2. Exact identity of the installed package

```text
Package:      scanner
Version:      1.0.20250413
Architecture: amd64
SHA-256:      0b7618a390a695af151f1aa9ba8d6a1e8dd9ce922ab103ccd52a0e0a86509a91
```

A VM snapshot/checkpoint was created before installation to allow the test to be reverted.

### 3. Dynamic installation result

The real installation through `dpkg` completed successfully:

```text
dpkg_rc = 0
status  = install ok installed scanner 1.0.20250413
```

`strace` was not available, so this run **does not contain a syscall trace of the installer**. This limits that specific layer of evidence but does not invalidate the before/after record of files, permissions, services, processes and network state.

During `postinst`, privileged execution of the following was observed:

```text
/usr/bin/sh ./setup.sh
./czur_create --logname=<user>
sed -i ... /lib/udev/uvcdynctrl
```

`czur_create` also returned:

```text
{"key": "", "res": true, "type": 7, "str_result": "create permission success"}
```

The installation created the local user directory `~/.czur` and a graphical launcher that runs `CzurScanner` from `/opt/apps/scanner`, preloading `libczurusb-1.0.so` and forcing the X11 backend.

### 4. Confirmed finding: excessively open permissions

The static hypothesis concerning `chmod -R 777` was confirmed dynamically. After installation, **3,061 world-writable entries** were counted, all under `/opt/apps/scanner`:

```text
2700  files       -rwxrwxrwx
 233  symlinks    lrwxrwxrwx
 128  directories drwxrwxrwx
-----------------------------
3061  entries
```

Observed ownership distribution:

```text
2832  user:user
 229  root:root
```

`/opt/apps/scanner` itself was left with mode `0777`. This is classified as a **real installer-hardening problem**, not as evidence of malware.

### 5. Confirmed finding: overly broad udev rules

The installation left `/etc/udev/rules.d/czurscanner.rules` with rules such as:

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

In addition, `systemd-udevd` recorded that the rules file was marked executable and recommended removing those bits, although it continued processing the file.

The `04fc` rule matches the USB vendor of the tested device, but accepts any product from that vendor (`idProduct="*"`) and grants global `0666` access; the remaining rules broaden the surface further. The **REPAIR** classification is retained for later hardening, after functional compatibility is verified.

### 6. Resident service: hypothesis negatively closed for this build

After installation:

```text
CZUR systemd unit detected          NO
active CZUR service                NO
persistent CZUR process            NO
```

This strengthens the conclusion of the static addenda: the installation branch that suggested `CZURPlugin.service` does not materialise as a resident service in the tested package/build.

### 7. First application run

The official application was launched and tested interactively with non-sensitive material. The preliminary functional result reported by the user is:

```text
application opens / works           YES, preliminary
scanner usable                       YES, preliminary
minor anomalous behaviour            OBSERVED BY USER, NOT CHARACTERISED
cause                                NOT DETERMINED
reboot before continuing             DECIDED
```

No cause is assigned to the unusual behaviour observed: it may involve the application, USB/UVC state, graphical session, post-install state or another factor. It must be reproduced after reboot before it can be elevated to a product defect.

### 8. Network: what is and is not demonstrated

The previous static analysis already demonstrated **network capability**, including diagnostic/reporting mechanisms and Alibaba OSS components, but did not demonstrate automatic uploading of ordinary scans.

For this first run, a network capture was also performed at host/VM level. Because that capture includes general VM traffic rather than direct per-process attribution, the raw PCAP **is not published or incorporated into the repository**. An exact-string search in that capture did not find:

```text
internal.czur.cc
worldtimeapi.org
oss-cn-beijing.aliyuncs.com
aliyuncs.com
czur.cc
```

This result is only limited negative evidence: **absence of those literal strings in a PCAP does not demonstrate total absence of CZUR traffic**, because prior DNS resolution, encryption, direct IP connections, QUIC or other mechanisms may exist. Attribution of normal-use egress to `CzurScanner` remains pending a more controlled dynamic test.

### 9. Current classification

```text
USB/UVC HARDWARE                    PASS
7424x5568 NATIVE CAPTURE            PASS
BASIC VISUAL QUALITY                PASS (local user review)
FUNCTIONAL INSTALLATION             PASS
dpkg                                PASS
RESIDENT CZUR SERVICE               NOT EVIDENCED
INSTALLER PERMISSIONS               REPAIR — 3061 world-writable entries
UDEV RULES                          REPAIR — MODE 0666 and broad scope
SOFTWARE NETWORK CAPABILITY         STATICALLY CONFIRMED
DIAGNOSTIC/LOG UPLOAD               CONFIRMED AS CAPABILITY
AUTOMATIC SCAN UPLOAD               NOT DEMONSTRATED
NORMAL-USE CZUR EGRESS              PENDING DYNAMIC ATTRIBUTION
FIRST-RUN STABILITY                 PROVISIONAL — anomaly not characterised
MALWARE                             NOT DEMONSTRATED
```

### 10. Next test

After reboot:

1. verify persistence of UVC detection and `CzurScanner` startup;
2. repeat a non-sensitive scan operation and characterise any anomaly;
3. capture egress with tighter attribution;
4. verify physical button, Auto Scan/manual page turning, cropping, book treatment and export;
5. only afterwards, harden `/opt/apps/scanner` permissions and narrow the udev rules, verifying that the product remains functional.

At this point there is no hardware reason to return the ET24 Pro. The decision to keep it should depend mainly on real software stability, book-workflow functionality, and closure of the network/hardening test.

`CAPABILITY != INVOCATION != TRAFFIC != IMPROPER TRANSMISSION`.
