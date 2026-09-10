# Addendum III al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum III to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia estática reproducible · `ALIBABA_CLOUD_SDK_PRESENT=CONFIRMADO` · `OUTBOUND_TRAFFIC=NO_VERIFICADO`  
**Relacionado / Related:** [Delta principal](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md) · [Addendum I](./2026-09-08_ADDENDUM_DELTA_CZUR_ET24_PRO_CZUR_CREATE_STATIC_ES_EN.md) · [Addendum II](./2026-09-08_ADDENDUM2_DELTA_CZUR_ET24_PRO_PYINSTALLER_CONFIRMADO_ES_EN.md)

---

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

### 1. Nueva evidencia: el bundle del scanner incluye SDKs completos de Alibaba Cloud

La enumeración recursiva del `PYZ-00.pyz` de `CzurScanner` confirma que el paquete incorpora módulos de Alibaba Cloud, no sólo cadenas residuales:

```text
aliyunsdkcore
aliyunsdkcore.client
aliyunsdkcore.auth.*
aliyunsdkcore.endpoint.*
aliyunsdkcore.http.*
aliyunsdkcore.retry.*
aliyunsdkkms.request.v20160120.DecryptRequest
aliyunsdkkms.request.v20160120.EncryptRequest
aliyunsdkkms.request.v20160120.GenerateDataKeyRequest
oss2.api
oss2.auth
oss2.http
```

También incorpora stacks HTTP/TLS completos (`requests`, `urllib3`, `socket`, `ssl`, `cryptography`) y módulos de aplicación relacionados con autorización, informes, sugerencias, push y correo.

### 2. Qué significa y qué no significa

La documentación oficial de Alibaba Cloud identifica `oss2` como su SDK Python V1 para Object Storage Service (OSS), con operaciones de lectura y escritura de objetos, y KMS como el servicio para operaciones criptográficas y gestión de claves/secretos.

Fuentes oficiales:

- https://www.alibabacloud.com/help/en/oss/developer-reference/python-sdk-v1/
- https://www.alibabacloud.com/help/en/pai/read-data-from-and-write-data-to-oss
- https://www.alibabacloud.com/help/en/kms/key-management-service/developer-reference/kms-instance-sdk-for-python/

Por tanto:

```text
CAPACIDAD DE CONEXION A ALIBABA CLOUD = CONFIRMADA POR INVENTARIO
CAPACIDAD DE OSS (OBJETOS/UPLOAD/DOWNLOAD) = CONFIRMADA POR SDK PRESENTE
CAPACIDAD KMS (ENCRYPT/DECRYPT/DATA KEY) = CONFIRMADA POR SDK PRESENTE
DESTINO CONCRETO = NO VERIFICADO
USO EFECTIVO = NO VERIFICADO
TRAFICO SALIENTE = NO VERIFICADO
EXFILTRACION = NO DEMOSTRADA
MALWARE = NO DEMOSTRADO
```

La presencia de un SDK completo demuestra capacidad técnica empaquetada; no demuestra por sí sola que la aplicación invoque esos módulos ni que transmita datos sin acción o consentimiento del usuario.

### 3. `czur_create` también contiene un stack de red completo

La enumeración recursiva de `czur_create` confirma presencia de:

```text
requests.*
urllib3.*
socket
socketserver
ssl
http.client
http.server
cryptography.*
```

Esto eleva el hallazgo previo de “strings compatibles con red” a **módulos Python realmente presentes en su `PYZ-00.pyz`**. Aun así, no demuestra que el pequeño entrypoint `main` los importe o ejecute.

### 4. Relaciones funcionales relevantes en `CzurScanner`

El CArchive/PYZ contiene además módulos como:

```text
crash_report
main_window_auth_validate
module_authorized
pop_authorization_dialog
pop_offline_report_dialog
main_window_submit_wrong_data
main_window_suggestion
main_window_pushmessage_dialog
email_input_dialog
pop_email_input_dialog
```

La coexistencia de esos módulos con OSS/KMS/HTTP constituye una **relación técnica que merece seguimiento dirigido**, pero todavía no prueba qué flujo concreto activa la red.

### 5. Siguiente prueba estática prioritaria

Antes de ejecutar el software con red o privilegios se debe extraer y analizar bytecode de los módulos propios que pueden enlazar interfaz ↔ red/cloud:

```text
module_authorized
crash_report
main_window_auth_validate
main_window_submit_wrong_data
main_window_suggestion
main_window_pushmessage_dialog
pop_offline_report_dialog
```

También deben buscarse referencias a:

```text
oss2.Bucket
put_object
get_object
aliyunsdkcore.AcsClient
EncryptRequest
DecryptRequest
GenerateDataKeyRequest
requests.get / requests.post
URLs, endpoints, bucket names, access-key variables y dominios aliyuncs.com
```

La siguiente clasificación depende de evidencia de llamadas reales desde módulos CZUR hacia esos SDKs, no de la mera presencia de dependencias.

### 6. Estado incremental

| Hallazgo | Estado |
|---|---|
| PyInstaller/CArchive/PYZ | **CONFIRMADO** |
| `requests`/`urllib3`/`socket`/`ssl` en `czur_create` | **CONFIRMADO POR INVENTARIO PYZ** |
| `aliyunsdkcore` en `CzurScanner` | **CONFIRMADO** |
| `aliyunsdkkms` con Encrypt/Decrypt/GenerateDataKey | **CONFIRMADO** |
| `oss2` (OSS) | **CONFIRMADO** |
| módulos CZUR de auth/report/push/email | **CONFIRMADO POR INVENTARIO** |
| invocación efectiva de Alibaba Cloud | **NO VERIFICADO** |
| tráfico saliente | **NO VERIFICADO** |
| exfiltración | **NO DEMOSTRADA** |
| malware | **NO DEMOSTRADO** |

---

## EN · English

### 1. New evidence: the scanner bundle includes complete Alibaba Cloud SDKs

Recursive enumeration of `CzurScanner`'s `PYZ-00.pyz` confirms that the package contains Alibaba Cloud modules, not merely residual strings:

```text
aliyunsdkcore
aliyunsdkcore.client
aliyunsdkcore.auth.*
aliyunsdkcore.endpoint.*
aliyunsdkcore.http.*
aliyunsdkcore.retry.*
aliyunsdkkms.request.v20160120.DecryptRequest
aliyunsdkkms.request.v20160120.EncryptRequest
aliyunsdkkms.request.v20160120.GenerateDataKeyRequest
oss2.api
oss2.auth
oss2.http
```

It also contains complete HTTP/TLS stacks (`requests`, `urllib3`, `socket`, `ssl`, `cryptography`) and application modules related to authorization, reports, suggestions, push and email.

### 2. What this means and what it does not mean

Alibaba Cloud's official documentation identifies `oss2` as its Python V1 SDK for Object Storage Service (OSS), with object read/write operations, and KMS as the service for cryptographic operations and key/secret management.

Official sources:

- https://www.alibabacloud.com/help/en/oss/developer-reference/python-sdk-v1/
- https://www.alibabacloud.com/help/en/pai/read-data-from-and-write-data-to-oss
- https://www.alibabacloud.com/help/en/kms/key-management-service/developer-reference/kms-instance-sdk-for-python/

Therefore:

```text
ALIBABA CLOUD CONNECTION CAPABILITY = CONFIRMED BY INVENTORY
OSS CAPABILITY (OBJECTS/UPLOAD/DOWNLOAD) = CONFIRMED BY PRESENT SDK
KMS CAPABILITY (ENCRYPT/DECRYPT/DATA KEY) = CONFIRMED BY PRESENT SDK
SPECIFIC DESTINATION = NOT VERIFIED
EFFECTIVE USE = NOT VERIFIED
OUTBOUND TRAFFIC = NOT VERIFIED
EXFILTRATION = NOT DEMONSTRATED
MALWARE = NOT DEMONSTRATED
```

Presence of a complete SDK demonstrates packaged technical capability; it does not by itself demonstrate that the application invokes those modules or transmits data without user action or consent.

### 3. `czur_create` also contains a complete network stack

Recursive enumeration of `czur_create` confirms the presence of:

```text
requests.*
urllib3.*
socket
socketserver
ssl
http.client
http.server
cryptography.*
```

This raises the earlier finding from “strings compatible with networking” to **Python modules actually present in its `PYZ-00.pyz`**. It still does not demonstrate that the small `main` entrypoint imports or executes them.

### 4. Relevant functional relationships in `CzurScanner`

The CArchive/PYZ also contains modules such as:

```text
crash_report
main_window_auth_validate
module_authorized
pop_authorization_dialog
pop_offline_report_dialog
main_window_submit_wrong_data
main_window_suggestion
main_window_pushmessage_dialog
email_input_dialog
pop_email_input_dialog
```

The coexistence of these modules with OSS/KMS/HTTP is a **technical relationship that warrants targeted follow-up**, but it still does not prove which specific flow activates the network.

### 5. Priority next static test

Before running the software with network access or privileges, bytecode should be extracted and analysed from proprietary modules that may connect interface ↔ network/cloud:

```text
module_authorized
crash_report
main_window_auth_validate
main_window_submit_wrong_data
main_window_suggestion
main_window_pushmessage_dialog
pop_offline_report_dialog
```

References should also be sought for:

```text
oss2.Bucket
put_object
get_object
aliyunsdkcore.AcsClient
EncryptRequest
DecryptRequest
GenerateDataKeyRequest
requests.get / requests.post
URLs, endpoints, bucket names, access-key variables and aliyuncs.com domains
```

The next classification depends on evidence of real calls from CZUR modules to those SDKs, not on mere dependency presence.

### 6. Incremental state

| Finding | State |
|---|---|
| PyInstaller/CArchive/PYZ | **CONFIRMED** |
| `requests`/`urllib3`/`socket`/`ssl` in `czur_create` | **CONFIRMED BY PYZ INVENTORY** |
| `aliyunsdkcore` in `CzurScanner` | **CONFIRMED** |
| `aliyunsdkkms` with Encrypt/Decrypt/GenerateDataKey | **CONFIRMED** |
| `oss2` (OSS) | **CONFIRMED** |
| CZUR auth/report/push/email modules | **CONFIRMED BY INVENTORY** |
| effective Alibaba Cloud invocation | **NOT VERIFIED** |
| outbound traffic | **NOT VERIFIED** |
| exfiltration | **NOT DEMONSTRATED** |
| malware | **NOT DEMONSTRATED** |

---

## Trazabilidad / Traceability

`NEW_EVIDENCE → REPRODUCTION → CLASSIFICATION → ADDENDUM`
