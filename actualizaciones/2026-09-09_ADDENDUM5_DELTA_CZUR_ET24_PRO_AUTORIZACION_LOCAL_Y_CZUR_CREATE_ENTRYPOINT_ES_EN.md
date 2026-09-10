# Addendum V al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum V to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `AUTH_MODULE_LOCAL_LICENSE_PATTERN=FUERTE` · `CLOUD_CALL_FROM_AUTH_MODULE=NO_OBSERVADA`  
**Relacionado / Related:** Delta CZUR ET24 Pro Linux + Addenda I–IV

---

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

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

### 1. Internal `module_authorized` from PYZ extracted correctly

The `module_authorized` member was extracted from `CzurScanner`'s `PYZ-00.pyz` using `pyi-archive_viewer`.

Observed artifact:

```text
module_authorized_pyz.bin
~6.9 KiB
file: data
```

The `strings` output showed no direct matches for:

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

It did show numerous symbols specific to local licensing/authorization:

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

### 2. Provisional interpretation

This result strengthens the hypothesis that `module_authorized` acts mainly as a local authorization/licensing layer and delegates part of its work to architecture-specific helper binaries through subprocesses.

The observed evidence is compatible with:

```text
module_authorized
→ locates czur_authorized binary
→ obtains machine_id/license
→ validates result
→ updates serial/license file/times_left
```

No direct relationship between the extracted module and Alibaba Cloud, OSS or KMS was observed through `strings`.

This does NOT demonstrate that authorization is fully offline or that other modules do not use cloud services.

### 3. `czur_create` entrypoint extracted

The `main` entrypoint of `czur_create` was also extracted:

```text
czur_create_main.bin
430 bytes
file: data
```

The targeted string search returned only:

```text
out_key
```

No direct strings appeared for:

```text
aliyun / oss2 / kms / requests / http / service / systemctl / udev
```

### 4. Updated evidentiary state

```text
PYINSTALLER = CONFIRMED
ALIBABA CLOUD SDK IN BUNDLE = CONFIRMED
OSS/KMS CAPABILITY = CONFIRMED BY INVENTORY
internal module_authorized = EXTRACTED
LOCAL LICENSE PATTERN = STRONG
DIRECT CLOUD CALL FROM module_authorized = NOT OBSERVED
czur_create main = EXTRACTED
czur_create main DIRECT CLOUD STRINGS = NOT OBSERVED
REAL OUTBOUND TRAFFIC = NOT VERIFIED
MALWARE = NOT DEMONSTRATED
```

### 5. Next step

The next phase should focus on disassembling/decompiling the Python 3.8 bytecode of the internal `module_authorized` and the `czur_create:main` entrypoint, then tracing proprietary modules that may import `oss2`/`aliyunsdk*`.

It also remains necessary to determine what creates or installs `CZURPlugin.service` and, only afterwards, perform dynamic execution in a snapshot with controlled networking and process/file/socket tracing.
