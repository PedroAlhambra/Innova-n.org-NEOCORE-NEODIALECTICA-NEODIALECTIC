# Addendum III al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum III to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-08  
**Estado / Status:** evidencia estática reproducible · `ALIBABA_CLOUD_SDK_PRESENT=CONFIRMADO` · `OUTBOUND_TRAFFIC=NO_VERIFICADO`  
**Relacionado / Related:** [Delta principal](./2026-09-08_DELTA_SINTESIS_CZUR_ET24_PRO_LINUX_AUDITORIA_ES_EN.md) · [Addendum I](./2026-09-08_ADDENDUM_DELTA_CZUR_ET24_PRO_CZUR_CREATE_STATIC_ES_EN.md) · [Addendum II](./2026-09-08_ADDENDUM2_DELTA_CZUR_ET24_PRO_PYINSTALLER_CONFIRMADO_ES_EN.md)

---

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

Recursive `PYZ-00.pyz` enumeration confirms that `CzurScanner` bundles complete Alibaba Cloud-related Python modules including `aliyunsdkcore`, `aliyunsdkkms` request classes for Encrypt/Decrypt/GenerateDataKey, and `oss2` (`oss2.api`, `oss2.auth`, `oss2.http`). It also bundles full HTTP/TLS stacks (`requests`, `urllib3`, `socket`, `ssl`, `cryptography`).

Alibaba Cloud documents `oss2` as its OSS Python SDK for object storage and KMS as its key-management/cryptographic service. This establishes packaged technical capability for Alibaba Cloud APIs, OSS object operations and KMS operations. It does **not** establish that CZUR invokes them in a given session, which endpoint/bucket is used, or that any outbound transfer occurs.

`czur_create` itself also contains complete `requests`, `urllib3`, `socket`, `ssl`, `http.*` and `cryptography.*` modules inside its PYZ archive. This upgrades the prior observation from raw strings to confirmed packaged Python modules, but the tiny `main` entrypoint still needs to be traced before network use can be attributed to that helper.

**Current classification:** Alibaba Cloud SDK capability = `CONFIRMED`; actual invocation = `NOT VERIFIED`; outbound traffic = `NOT VERIFIED`; exfiltration = `NOT DEMONSTRATED`; malware = `NOT DEMONSTRATED`.

`NEW_EVIDENCE → REPRODUCTION → CLASSIFICATION → ADDENDUM`
