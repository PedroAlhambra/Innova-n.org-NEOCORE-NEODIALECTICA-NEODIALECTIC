# Addendum VII al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum VII to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `AUTH_WRAPPER_LOCAL=CONFIRMADO` · `NETWORK_PATH_IN_AUTH_WRAPPER=NO_OBSERVADO` · `CZUR_CREATE_USER_SUPPORT=PENDIENTE`

---

## ES · Castellano

### 1. `module_authorized.py` queda caracterizado como wrapper local

El bytecode CPython 3.8 de `module_authorized.py` ha sido reconstruido a `.pyc` y desensamblado con `xdis/pydisasm` sin ejecutar el software CZUR.

Imports directos observados:

```text
subprocess
time
os
json
traceback
math
loguru
global_public_method
```

No se observan imports directos de `requests`, `urllib3`, `socket`, `aliyun`, `oss2` o KMS en este módulo.

### 2. Flujo local hacia `czur_create`

La clase `Authorized` resuelve una ruta local según sistema/arquitectura (`x86_64`, ARM, MIPS, LoongArch), construye `exe_path` hacia `./czur_create`, configura `LD_LIBRARY_PATH` y `cwd` al directorio de autorización y ejecuta el helper mediante `subprocess.Popen`.

La línea de órdenes se construye con:

```text
czur_create
--logfile=<ruta>
--license=<valor embebido>
--get_id=...
--get_time_left=...
--update_times_left=...
--update_license_file=...
--update_license_serial=...
--decode_invite_code=...
--soft_version=...
--get_time_left_type=...
```

El valor embebido pasado como `--license` no se reproduce aquí por precaución: se registra únicamente que existe una constante larga de aspecto token/clave en el bytecode.

### 3. Protocolo de respuesta

`__validate_res` interpreta el último texto producido por `czur_create` como JSON y exige una clave fija de protocolo antes de aceptar `res` y `str_result`.

Por tanto, el patrón observado es:

```text
CzurScanner/module_authorized
    -> subprocess.Popen(local czur_create)
    -> stdout JSON
    -> validación local
```

Esto no demuestra tráfico de red.

### 4. Datos de licencia/identidad manejados

El wrapper solicita al helper operaciones que devuelven o actualizan:

```text
machine_id
times_left
invite_code
serial_string
times_server_until
soft_version
serial_type
license serial
license file
```

`decode_invite_code` acepta códigos de 12 caracteres y puede devolver campos `member_id` y `phone_number`.

La presencia de estos campos demuestra tratamiento funcional de datos de licencia/cuenta en la capa de autorización. No demuestra que esos datos se transmitan fuera del equipo.

### 5. `czur_create/main.py` no contiene la lógica sustantiva

El `main.py` extraído de `czur_create` importa:

```python
from user_support import UserSupport
```

crea `UserSupport(sys.argv)`, llama a `process_argv()` y serializa el resultado a JSON por stdout.

Por tanto, la lógica real de `czur_create` está desplazada a `user_support` y sus dependencias. Éste es el siguiente objetivo estático.

### 6. Clasificación actual

```text
AUTH_WRAPPER_LOCAL                   = CONFIRMADO
SUBPROCESS HACIA CZUR_CREATE         = CONFIRMADO
RUTA MULTIARQUITECTURA LOCAL         = CONFIRMADA
DATOS LICENCIA/MACHINE/INVITE        = CONFIRMADOS
MEMBER_ID / PHONE_NUMBER EN DECODE   = CONFIRMADOS POR BYTECODE
RED DIRECTA EN module_authorized     = NO OBSERVADA
RED DENTRO DE czur_create            = NO RESUELTA
LOGICA REAL EN user_support          = FUERTE / SIGUIENTE PASO
TRAFICO SALIENTE REAL                = NO VERIFICADO
EXFILTRACION                         = NO DEMOSTRADA
MALWARE                              = NO DEMOSTRADO
```

---

## EN · English

Static CPython 3.8 disassembly now characterises `module_authorized.py` as a local wrapper around the bundled `czur_create` helper. It resolves architecture-specific local paths, sets `LD_LIBRARY_PATH`/working directory, invokes the helper through `subprocess.Popen`, reads JSON from stdout and validates a fixed protocol key.

The wrapper exposes operations for machine ID, remaining licence time, licence-file/serial updates, invite-code decoding, software version and serial type. Invite-code decoding may return `member_id` and `phone_number`.

No direct `requests`, `urllib3`, socket, Alibaba Cloud, OSS or KMS imports were observed in `module_authorized.py`. This does **not** prove that `czur_create` is offline: its extracted `main.py` delegates actual argument processing to `user_support.UserSupport.process_argv()`.

Next static target: extract and disassemble `user_support` from the `czur_create` embedded PYZ, then trace its imports and any network/cloud calls before privileged execution.

`CAPABILITY != OBSERVED_BEHAVIOUR`  
`PACKAGED_SDK != NETWORK_TRAFFIC`  
`WRAPPER_LOCAL != HELPER_OFFLINE`
