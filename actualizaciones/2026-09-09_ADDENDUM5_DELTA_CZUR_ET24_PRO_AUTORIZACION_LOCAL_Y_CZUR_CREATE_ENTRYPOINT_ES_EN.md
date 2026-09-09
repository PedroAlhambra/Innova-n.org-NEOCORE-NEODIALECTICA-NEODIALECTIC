# Addendum V al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum V to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `AUTH_MODULE_LOCAL_LICENSE_PATTERN=FUERTE` · `CLOUD_CALL_FROM_AUTH_MODULE=NO_OBSERVADA`  
**Relacionado / Related:** Delta CZUR ET24 Pro Linux + Addenda I–IV

---

## ES · Castellano

### 1. `module_authorized` interno del PYZ extraído correctamente

Se extrajo el miembro `module_authorized` desde `PYZ-00.pyz` de `CzurScanner` mediante `pyi-archive_viewer`.

Artefacto observado:

```text
module_authorized_pyz.bin
~6,9 KiB
file: data
```

La salida de `strings` no mostró coincidencias directas para:

```text
aliyun
aliyuncs
oss2
bucket
put_object
get_object
kms
encrypt
decrypt
endpoint
http(s)
requests
upload
download
```

Sí mostró numerosos símbolos específicos de licenciamiento/autorización local:

```text
Authorized
czur_authorized.log
get_auth_path
Authorized.__get_lic_string
Authorized.__subprocess_args
Authorized.__run_authorized
Authorized.__validate_res
Authorized.update_times_left
Authorized.get_times_left
Authorized.update_and_get_times_left
Authorized.get_machine_id
Authorized.update_license_serial
Authorized.update_license_file
Authorized.decode_invite_code
./czur_authorized/
./library/linux/x86/czur_authorized/
./library/linux/arm/czur_authorized/
./library/linux/mips/czur_authorized/
./library/linux/loongarch64/czur_authorized/
```

### 2. Interpretación provisional

Este resultado refuerza la hipótesis de que `module_authorized` actúa principalmente como capa de autorización/licencia local y delega parte de su trabajo en binarios auxiliares específicos de arquitectura mediante subprocess.

La evidencia observada es compatible con:

```text
module_authorized
→ localiza binario czur_authorized
→ obtiene machine_id/licencia
→ valida resultado
→ actualiza serial/licence file/times_left
```

No se observó, mediante `strings`, una relación directa del módulo extraído con Alibaba Cloud, OSS o KMS.

Esto NO demuestra que la autorización sea completamente offline ni que otros módulos no usen cloud.

### 3. `czur_create` entrypoint extraído

Se extrajo también el entrypoint `main` de `czur_create`:

```text
czur_create_main.bin
430 bytes
file: data
```

La búsqueda dirigida de cadenas sólo devolvió:

```text
out_key
```

No aparecieron cadenas directas de:

```text
aliyun / oss2 / kms / requests / http / service / systemctl / udev
```

### 4. Estado probatorio actualizado

```text
PYINSTALLER = CONFIRMADO
ALIBABA CLOUD SDK EN BUNDLE = CONFIRMADO
OSS/KMS CAPABILITY = CONFIRMADA POR INVENTARIO
module_authorized interno = EXTRAIDO
PATRON DE LICENCIA LOCAL = FUERTE
CLOUD CALL DIRECTA DESDE module_authorized = NO OBSERVADA
czur_create main = EXTRAIDO
czur_create main DIRECT CLOUD STRINGS = NO OBSERVADAS
TRAFICO SALIENTE REAL = NO VERIFICADO
MALWARE = NO DEMOSTRADO
```

### 5. Siguiente paso

La siguiente fase debe centrarse en desensamblar/decompilar el bytecode Python 3.8 del `module_authorized` interno y del entrypoint `czur_create:main`, y después rastrear los módulos propios que puedan importar `oss2`/`aliyunsdk*`.

También queda pendiente resolver qué crea o instala `CZURPlugin.service` y, sólo después, realizar una ejecución dinámica en snapshot con red controlada y trazado de procesos/ficheros/sockets.

---

## EN · English

The internal `module_authorized` member from `CzurScanner`'s `PYZ-00.pyz` was successfully extracted. Static strings show a strong local licensing/authorization pattern (`get_machine_id`, `update_license_serial`, `update_license_file`, `times_left`, `decode_invite_code`, architecture-specific `czur_authorized` helpers), while no direct Alibaba Cloud / OSS / KMS / HTTP / requests strings were observed in that module.

The 430-byte `main` entrypoint from `czur_create` was also extracted; the only relevant string observed was `out_key`, with no direct cloud/service/udev strings.

This weakens the hypothesis that the authorization wrapper itself directly drives Alibaba Cloud access, but it does not rule out cloud use elsewhere in the application or through delegated helpers. Outbound traffic remains unverified.

`NEGATIVE_FINDING != ABSENCE_PROOF`
