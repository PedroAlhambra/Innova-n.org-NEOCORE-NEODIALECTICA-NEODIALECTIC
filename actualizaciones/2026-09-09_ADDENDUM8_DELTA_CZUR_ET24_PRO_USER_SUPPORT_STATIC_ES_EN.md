# Addendum VIII — CZUR ET24 Pro Linux audit: `user_support.py` static reconstruction

Fecha / Date: 2026-09-09

## ES

### Hechos confirmados

Se extrajo `user_support` del `PYZ-00.pyz` de `czur_create`, se reconstruyó como `.pyc` CPython 3.8 (magic 3413) y se desensambló estáticamente con `xdis/pydisasm`, sin ejecutar código CZUR.

El módulo `user_support.py` contiene un motor de licenciamiento/autorización local mucho más amplio de lo que sugería el `main.py` del ejecutable. Entre sus métodos aparecen, entre otros:

- generación y validación de archivos de licencia;
- construcción de identificadores y claves de máquina;
- obtención de UUID/udev UUID;
- gestión de seriales e invite codes;
- actualización de tiempos de uso;
- escritura y lectura de archivos locales cifrados;
- `process_argv()` y `my_run_command()`;
- manejo de rutas/propiedad de archivos.

Los imports directos observados al comienzo del módulo incluyen `logging`, `random`, `shutil`, `time`, `datetime`, `json`, `platform`, `os`, `sys`, `hashlib`, `traceback`, `argparse`, `stat`, `pwd`, `getpass`, `subprocess`, `math`, `dateutil.relativedelta`, `data_support`, `pp_logger` y `define`.

En esos imports directos observados no aparecen `requests`, `urllib3`, `socket`, `http`, `ssl`, `aliyun`, `oss2` ni KMS.

### Cadena funcional confirmada

`module_authorized.py` llama a `czur_create`; `czur_create/main.py` delega a `UserSupport.process_argv()`; `UserSupport` contiene la lógica sustantiva de licencia local.

Se observan operaciones locales de cifrado/descifrado a través de `DataSupport.encrypt()` / `DataSupport.decrypt()`, generación de archivos `vip_<machine_key>.txt`, combinación de UUID/licencia/tiempos y seriales, y validación de pares de archivos locales.

También aparecen nombres de carpetas ocultas `.osserver_config` y `.systemuserd`. Su mera presencia no demuestra comportamiento malicioso; sí justifica auditar su función exacta y los permisos/propietarios que el código les asigna.

### Clasificación epistemológica

- `USER_SUPPORT_EXTRACTED_AND_DISASSEMBLED = CONFIRMED`
- `LOCAL_LICENSE_ENGINE = CONFIRMED`
- `LOCAL_FILE_ENCRYPT_DECRYPT_PATH = CONFIRMED`
- `DIRECT_NETWORK_CLOUD_IMPORTS_IN_OBSERVED_TOP_LEVEL_IMPORTS = NOT OBSERVED`
- `NETWORK_BEHAVIOR_ANYWHERE_IN_USER_SUPPORT = NOT YET EXHAUSTIVELY EXCLUDED`
- `DATA_SUPPORT_ROLE = PENDING_STATIC_AUDIT`
- `ALIBABA_SDK_PRESENT_ELSEWHERE_IN_SCANNER_BUNDLE = CONFIRMED_FROM_PREVIOUS_ADDENDUM`
- `ACTUAL_OUTBOUND_TRAFFIC = NOT VERIFIED`
- `EXFILTRATION = NOT DEMONSTRATED`
- `MALWARE = NOT DEMONSTRATED`

### Siguiente paso

1. Auditar `data_support` del mismo PYZ, especialmente `encrypt/decrypt`, imports y cualquier dependencia de red/cloud.
2. Revisar de forma aislada `my_run_command`, `get_udev_uuid`, `get_uuid`, `get_uuids` y la creación/uso de `.osserver_config` / `.systemuserd`.
3. Ejecutar un grep de red/cloud no contaminado por términos de licencia, sin `head` limitante, sobre el desensamblado completo.
4. Sólo después pasar a prueba dinámica controlada con snapshot y red bloqueada/monitorizada.

## EN

### Confirmed facts

`user_support` was extracted from `czur_create`'s `PYZ-00.pyz`, reconstructed as CPython 3.8 bytecode (magic 3413), and statically disassembled with `xdis/pydisasm` without executing CZUR code.

The module contains a substantial local licensing/authorization engine: local license file generation/validation, machine identifiers and keys, UUID/udev UUID retrieval, serial and invite-code handling, usage-time updates, encrypted local file I/O, argument processing, shell-command helper logic, and file ownership/path handling.

Observed direct imports at module start include standard/local modules such as `subprocess`, `hashlib`, `argparse`, `pwd`, `getpass`, `data_support`, `pp_logger` and `define`. No direct `requests`, `urllib3`, `socket`, `http`, `ssl`, `aliyun`, `oss2` or KMS import was observed in that top-level import set.

`DataSupport.encrypt()` and `DataSupport.decrypt()` are used for local licensing data. Hidden-folder names `.osserver_config` and `.systemuserd` also appear and require targeted review; presence alone is not evidence of malware.

### Epistemic classification

- `USER_SUPPORT_EXTRACTED_AND_DISASSEMBLED = CONFIRMED`
- `LOCAL_LICENSE_ENGINE = CONFIRMED`
- `LOCAL_FILE_ENCRYPT_DECRYPT_PATH = CONFIRMED`
- `DIRECT_NETWORK_CLOUD_IMPORTS_IN_OBSERVED_TOP_LEVEL_IMPORTS = NOT OBSERVED`
- `NETWORK_BEHAVIOR_ANYWHERE_IN_USER_SUPPORT = NOT YET EXHAUSTIVELY EXCLUDED`
- `DATA_SUPPORT_ROLE = PENDING_STATIC_AUDIT`
- `ACTUAL_OUTBOUND_TRAFFIC = NOT VERIFIED`
- `EXFILTRATION = NOT DEMONSTRATED`
- `MALWARE = NOT DEMONSTRATED`

Core rule remains: `CAPABILITY != OBSERVED_BEHAVIOR` and `PACKAGED_CLOUD_SDK != NETWORK_TRAFFIC`.
