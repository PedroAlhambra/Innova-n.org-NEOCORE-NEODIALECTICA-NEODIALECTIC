# Delta de síntesis · CZUR ET24 Pro en Linux: UVC funcional y auditoría del software oficial
# Synthesis delta · CZUR ET24 Pro on Linux: working UVC and audit of the official software

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia técnica reproducible · auditoría abierta · `HARDWARE_UVC=PASS` · `PAQUETE_DEB=REPAIR/NO_VERIFICADO`  
**Objeto / Scope:** CZUR ET24 Pro · Linux · Debian 13 (Trixie) x86_64 · paquete oficial `CZUR Scanner 1.0.20250413`

> Este documento separa funcionamiento del hardware, compatibilidad del kernel y comportamiento del instalador propietario. No afirma malware ni atribuye intenciones sin evidencia.
>
> This document separates hardware operation, kernel compatibility and proprietary-installer behaviour. It does not claim malware or attribute intent without evidence.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Pregunta práctica

**¿Necesita el CZUR ET24 Pro un “driver” propietario para funcionar en Linux?**

Para **captura de imagen a nivel de kernel, no en el sistema probado**. El ET24 Pro se enumera como dispositivo estándar **USB Video Class (UVC)** y Debian 13 lo enlaza directamente con `uvcvideo`. El software propietario de CZUR es otra capa: aporta flujo de escaneo, procesado, aplanado de páginas, recorte, OCR y exportación, pero no es necesario para que Linux reconozca la cámara.

La separación correcta es:

```text
ET24 Pro
→ USB/UVC
→ kernel Linux: uvcvideo
→ V4L2: /dev/video0
→ captura estándar disponible

CZUR Scanner .deb
→ aplicación propietaria + librerías + OCR/procesado + reglas/instalación propias
```

`DRIVER_KERNEL != APLICACION_CZUR`

### 2. Evidencia reproducida en Debian 13

Entorno de prueba: Debian GNU/Linux 13 (Trixie), amd64, con un controlador USB xHCI entregado al sistema invitado. El equipo se detectó como:

```text
04fc:6333 Sunplus Technology Co., Ltd Siri A9 UVC chipset
QHD CAMERA: CZUR
/dev/video0
/dev/video1
/dev/media0
```

El árbol USB mostró dos interfaces de vídeo enlazadas a `uvcvideo` y dos interfaces de audio enlazadas a `snd-usb-audio`, a 480 Mbit/s. `/dev/video0` enumeró formatos MJPEG y YUYV; `/dev/video1` no enumeró formatos de captura en esta prueba.

Entre los modos MJPEG observados:

```text
5696x4272 @ 4.5 fps
4608x3456 @ 20 fps
3840x2160 @ 30 fps
3072x1728 @ 30 fps
1920x1080 @ 30 fps
...
7424x5568 @ 4.5 fps
```

`5696×4272 = 24.33 MP`, coherente con la especificación nominal del ET24 Pro. CZUR publica para este modelo sensor CMOS de 24 MP, resolución 5696×4272 y 320 DPI. Los modos UVC por encima de 24 MP observados en el dispositivo **no se clasifican aquí como resolución óptica adicional**: deben contrastarse con un blanco de resolución o microdetalle fijo para descartar interpolación/escalado de firmware.

### 3. La documentación pública sí confirma Linux, pero con una limitación importante

A fecha 2026-09-08, la página oficial de soporte de ET24 Pro / ET25 Pro publica:

- `CZUR Scanner 1.0.20250413 for Linux`
- fecha indicada: `2025-12-03`
- tamaño indicado: `602.18 MB`
- requisito de sistema: **Ubuntu 20.04 a 24.04, x86_64**

Fuente oficial: https://www.czur.com/support/et24_25pro

La descarga oficial enlazada por CZUR resuelve actualmente a:

`https://resource.czur-files.com/software/linux/differ/scanner_1.0.20250413_amd64_en_2512021.deb`

Por tanto, **Linux sí está soportado por CZUR**, pero el soporte publicado se limita explícitamente a Ubuntu 20.04–24.04. Debian 13 no figura en esa matriz. Eso no impide que el hardware UVC funcione —ya se ha demostrado—, pero obliga a separar “compatibilidad del kernel” de “distribución oficialmente soportada por la aplicación”.

### 4. No es un caso aislado: hay evidencia Linux previa

Una prueba pública de 2023 sobre ET24 Pro con Ubuntu 22.04 observó el mismo identificador `04fc:6333`, `Product: CZUR`, `Manufacturer: Fic` y el mensaje del kernel `Found UVC 1.00 device CZUR (04fc:6333)`. Esa prueba concluyó que el dispositivo podía abrirse como cámara UVC con software genérico, aunque señaló limitaciones de los nodos/modos accesibles fuera de la aplicación CZUR.

Fuente: https://www.cnx-software.com/2023/07/23/czur-et24-pro-book-scanner-review-with-ubuntu-22-04-linux/

Existe además trabajo comunitario reciente que automatiza el flujo de CZUR en Linux y declara pruebas en Ubuntu/Debian, aunque depende del software oficial para funciones propias del escáner:

https://github.com/thomasbutzbach/czur-scanner-wrapper

En febrero de 2026 también apareció una propuesta comunitaria para ejecutar el paquete oficial dentro de un contenedor Ubuntu/Distrobox en openSUSE, precisamente para aislar sus dependencias y evitar introducir bibliotecas antiguas en el sistema anfitrión. Es evidencia comunitaria, no certificación del fabricante:

https://www.reddit.com/r/openSUSE/comments/1ragshj/question_anyone_using_a_czur_et24_book_scanner/

### 5. Paquete oficial auditado

Archivo descargado desde el enlace oficial:

```text
scanner / CZUR Scanner
Version: 1.0.20250413
Architecture: amd64
Size observed: 631433740 bytes (~603 MiB shown by ls)
SHA-256:
0b7618a390a695af151f1aa9ba8d6a1e8dd9ce922ab103ccd52a0e0a86509a91
```

El control Debian declara `Depends:` vacío y contiene scripts `preinst`, `postinst`, `prerm` y `postrm`. El paquete lleva buena parte de su runtime incorporado: Qt/PySide2, OpenCV, IRIS/iDRS OCR, bibliotecas Python, `cryptography`, `certifi`, `lxml`, `python-docx`, componentes `aliyunsdkcore`, modelos de visión y librerías propias CZUR.

**La presencia de una biblioteca o SDK de red, incluida `aliyunsdkcore`, demuestra capacidad de código, no tráfico realizado.** No se ha demostrado en esta fase ninguna exfiltración, conexión no autorizada ni comportamiento malicioso.

### 6. Hallazgos del instalador

El `preinst` recorre usuarios de `/home`, limpia accesos `.desktop` anteriores, elimina `/etc/ld.so.conf.d/CZURPlugin.conf` y ejecuta `ldconfig`.

El `postinst` realiza, entre otras, estas operaciones:

```text
mueve contenido temporal a /opt
recarga y reinicia udev
udevadm control --reload-rules
udevadm trigger
chmod -R 777 /opt/apps/scanner
ejecuta iris/bin/linux_install_idrs.sh
ejecuta czur_authorized/setup.sh como root
crea/manipula ~/.czur/ScannerInfo/config.data
recorre /home/* y crea accesos de escritorio
puede modificar, iniciar y habilitar CZURPlugin.service
escribe trazas en /home/1.txt
```

La conclusión no es “malware”. La conclusión reproducible es **endurecimiento deficiente del instalador**. En especial, `chmod -R 777 /opt/apps/scanner` hace escribible por cualquier usuario todo el árbol de una aplicación cuyos binarios/librerías se ejecutan después; eso aumenta innecesariamente la superficie de sustitución/manipulación local.

### 7. Reglas udev demasiado amplias

El paquete contiene `etc/udev/rules.d/czurscanner.rules` con reglas como:

```udev
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

Esto concede lectura/escritura mundial a familias completas de dispositivos USB y a puertos serie que exceden el ET24 Pro probado (`04fc:6333`). Técnicamente es una política de permisos mucho más amplia de lo necesario.

Si en otra instalación hiciera falta una regla manual, una alternativa de menor privilegio para **este VID:PID concreto** sería conceptualmente:

```udev
SUBSYSTEM=="usb", ATTR{idVendor}=="04fc", ATTR{idProduct}=="6333", MODE="0660", GROUP="video", TAG+="uaccess"
```

No debe añadirse si el sistema ya proporciona ACL/permisos suficientes; en la prueba actual el dispositivo ya era accesible mediante V4L2 antes de instalar el paquete propietario.

### 8. Scripts y binarios relevantes

`iris/bin/linux_install_idrs.sh` se limita en la revisión estática a crear enlaces simbólicos para bibliotecas y recursos del runtime IRIS/iDRS.

`czur_authorized/setup.sh` es mucho más relevante:

```sh
#!/bin/sh
me=$(who)
ORIGINAL_USER=${me%% *}
sudo ./czur_create --logname=$ORIGINAL_USER
```

Por tanto, el instalador entrega privilegios de root a `czur_create`, un ELF x86-64 *stripped* que aún requiere análisis dinámico/estático más profundo.

Hashes observados:

```text
czur_authorized/czur_create
SHA-256 cf16915e5948fe3128605db71d039d51bc36004716e82edd35905650b1c3b6e9

CzurScanner
SHA-256 233bd777f24051b5681857aa3a66d637f0c10ce3e5bb8ca80edd70e96203142c
```

Ambos ELF muestran en `file` el mismo BuildID SHA-1 `3f71fafa6e2e915b9bed491dd97e1bab785158de`, pese a tener SHA-256 distintos. Se conserva como anomalía de empaquetado/compilación a explicar; **no constituye por sí sola evidencia de comportamiento malicioso**.

El lanzador de escritorio usa:

```text
LD_PRELOAD=./libczurusb-1.0.so
GDK_BACKEND=x11
./CzurScanner
```

Esto confirma que la aplicación añade una capa propia sobre el acceso USB y fuerza X11 para su GUI.

### 9. Punto todavía no resuelto: CZURPlugin.service

`postinst` contiene lógica para editar, iniciar y habilitar `/lib/systemd/system/CZURPlugin.service` si existe. Sin embargo, en la extracción estática inicial del `.deb` **no se encontró ese archivo** dentro del payload. Queda por determinar si:

1. lo crea `czur_create` u otro binario durante instalación;
2. aparece sólo en determinadas variantes/estados;
3. es código residual del instalador.

Hasta resolverlo, el comportamiento de esa parte se clasifica `NO_VERIFICADO`.

### 10. Síntesis provisional

| Capa | Estado | Evidencia |
|---|---|---|
| Detección USB ET24 Pro | **PASS** | `04fc:6333` visible |
| Driver de kernel | **PASS** | `uvcvideo` enlazado automáticamente |
| Captura V4L2 | **PASS** | `/dev/video0`, MJPEG/YUYV |
| Resolución nominal 24 MP | **PASS** | 5696×4272 observado y publicado por CZUR |
| Modos >24 MP | **NO_VERIFICADO** | requieren prueba óptica para descartar interpolación |
| Software Linux oficial | **HECHO** | CZUR publica 1.0.20250413 |
| Soporte oficial Debian 13 | **NO_VERIFICADO / NO DECLARADO** | CZUR especifica Ubuntu 20.04–24.04 |
| Calidad de permisos del instalador | **REPAIR** | `777` + reglas udev `0666` amplias |
| Comportamiento de `czur_create` | **NO_VERIFICADO** | binario stripped ejecutado como root |
| Tráfico de red del paquete | **NO_VERIFICADO** | capacidad de librerías ≠ tráfico demostrado |
| Malware | **NO DEMOSTRADO** | no existe evidencia suficiente para afirmarlo |

La respuesta pública a “¿puedo usar este escáner en Linux?” es por tanto más precisa que sí/no:

> **El ET24 Pro funciona en Linux como dispositivo UVC estándar y no necesita un driver propietario de kernel para la captura básica. CZUR sí publica una aplicación Linux oficial, actualmente declarada para Ubuntu 20.04–24.04. En Debian 13 el hardware funciona, pero el instalador propietario presenta decisiones de permisos y privilegios que justifican auditoría/endurecimiento antes de adoptarlo sin modificaciones.**

### 11. Próximas pruebas falsables

- ejecutar la aplicación en un entorno controlado y registrar `strace`, procesos, ficheros creados y sockets;
- inspeccionar imports/strings/llamadas de `czur_create`, `CzurScanner` y `libczurusb-1.0.so`;
- comprobar si `CZURPlugin.service` se genera dinámicamente y documentar su contenido;
- comparar captura genérica UVC frente a salida de CZUR en 5696×4272;
- medir detalle real entre 5696×4272 y modos UVC mayores mediante patrón fijo/regla milimetrada/microdetalle;
- determinar qué funciones avanzadas (aplanado, eliminación de dedos, láser, OCR, auto-scan) dependen realmente de la aplicación propietaria.

---

## EN · English

### 1. Practical answer

**Does the CZUR ET24 Pro require a proprietary Linux “driver”?**

For kernel-level image capture, **not on the tested system**. The scanner enumerates as a standard USB Video Class device and Debian 13 binds it directly to the mainline `uvcvideo` driver. CZUR's proprietary package is a separate application layer providing scanning workflow, image processing, page flattening/cropping, OCR and export.

```text
ET24 Pro → USB/UVC → Linux uvcvideo → V4L2 /dev/video0 → standard capture
CZUR .deb → proprietary application/runtime/processing layer
```

### 2. Reproduced Linux evidence

On Debian 13 (Trixie), x86_64, the device was observed as `04fc:6333`, exposed as `QHD CAMERA: CZUR`, with `/dev/video0`, `/dev/video1` and `/dev/media0`. Video interfaces were bound to `uvcvideo`; audio interfaces to `snd-usb-audio`. `/dev/video0` exposed MJPEG/YUYV modes including 5696×4272 and 3840×2160@30 fps. The nominal 5696×4272 mode is ~24.3 MP and matches CZUR's published ET24 Pro specification of 24 MP / 320 DPI.

Higher UVC modes observed up to 7424×5568 must not be treated as additional optical resolution until a controlled detail target demonstrates added information rather than firmware scaling/interpolation.

### 3. Vendor support and distribution boundary

CZUR's official ET24 Pro / ET25 Pro support page currently publishes `CZUR Scanner 1.0.20250413 for Linux`, dated 2025-12-03, about 602.18 MB, and explicitly lists **Ubuntu 20.04–24.04 x86_64** as the supported Linux environment:

https://www.czur.com/support/et24_25pro

The official download currently resolves to:

`https://resource.czur-files.com/software/linux/differ/scanner_1.0.20250413_amd64_en_2512021.deb`

Debian 13 is therefore outside the vendor's published support matrix even though its kernel-level UVC compatibility is demonstrated.

### 4. Independent/community corroboration

A 2023 Ubuntu 22.04 review recorded the same `04fc:6333` identifier and kernel UVC detection, confirming that this is not unique to the present test:

https://www.cnx-software.com/2023/07/23/czur-et24-pro-book-scanner-review-with-ubuntu-22-04-linux/

Recent community work also exists around CZUR on Linux, including an Ubuntu/Debian wrapper and an openSUSE Distrobox approach. These are community evidence, not vendor certification:

https://github.com/thomasbutzbach/czur-scanner-wrapper

https://www.reddit.com/r/openSUSE/comments/1ragshj/question_anyone_using_a_czur_et24_book_scanner/

### 5. Installer audit

The official downloaded `.deb` observed SHA-256 is:

`0b7618a390a695af151f1aa9ba8d6a1e8dd9ce922ab103ccd52a0e0a86509a91`

Static inspection found broad privilege/permission operations: restarting/reloading udev, recursively setting `/opt/apps/scanner` to mode `777`, executing `czur_create` as root, iterating across home directories, and shipping udev rules that set multiple USB vendor families and serial interfaces to `0666`.

This is classified as **poor hardening / REPAIR**, not as evidence of malware.

The package also bundles networking/crypto-related libraries, including Aliyun SDK components. Their presence demonstrates software capability only; outbound traffic has not yet been demonstrated.

### 6. Open questions and provisional state

`czur_create` and `CzurScanner` are stripped ELF binaries. The installer references `CZURPlugin.service`, but the initial static extraction did not find that unit in the package payload. Dynamic behaviour, generated services and network activity therefore remain `NO_VERIFICADO`.

**Provisional synthesis:** hardware/UVC/V4L2 = `PASS`; vendor Linux software exists = verified; Debian 13 vendor support = not declared; installer hardening = `REPAIR`; malicious behaviour = not demonstrated.

---

## Fuentes principales / Primary sources

- CZUR official support, ET24 Pro / ET25 Pro: https://www.czur.com/support/et24_25pro
- CZUR ET series comparison, Linux/ET24 context: https://shop.czur.com/pages/comparescanner
- CZUR ET24 Pro 24 MP / 320 DPI overview: https://shop.czur.com/blogs/blog/why-and-how-to-choose-czur-et-series-book-scanners
- Independent Ubuntu 22.04 UVC test: https://www.cnx-software.com/2023/07/23/czur-et24-pro-book-scanner-review-with-ubuntu-22-04-linux/
- Community Linux wrapper: https://github.com/thomasbutzbach/czur-scanner-wrapper
- Community openSUSE/Distrobox discussion: https://www.reddit.com/r/openSUSE/comments/1ragshj/question_anyone_using_a_czur_et24_book_scanner/

## Regla de cierre / Closure rule

```text
NUEVA_EVIDENCIA
→ REPRODUCCIÓN
→ CLASIFICACIÓN
→ ACTUALIZACIÓN DEL DELTA
```

Este delta permanece abierto a correcciones de CZUR, usuarios de otras distribuciones, investigadores de seguridad y evidencia contradictoria reproducible.

This delta remains open to corrections from CZUR, users of other distributions, security researchers and reproducible contradictory evidence.
