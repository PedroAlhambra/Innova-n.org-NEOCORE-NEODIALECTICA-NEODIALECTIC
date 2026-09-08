# Addendum IV al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum IV to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `MODULE_AUTHORIZED_EXTRACTED=PASS` · `DIRECT_CLOUD_STRINGS=NO_OBSERVADAS_EN_PRIMER_FILTRO`

Relacionado: Delta principal y Addenda I–III de la auditoría CZUR ET24 Pro/Linux.

## ES · Castellano

Se extrajo mediante `pyi-archive_viewer` el miembro superior `module_authorized` del `PKG/CArchive` de `CzurScanner`, sin ejecutar el software CZUR.

Artefacto obtenido:

```text
~/CZUR-package-audit/key-modules/module_authorized.bin
size observado: ~4.1 KiB
```

Se aplicó una búsqueda ASCII simple con `strings -a` y filtro para:

```text
aliyun|aliyuncs|oss2|bucket|put_object|get_object|kms|encrypt|decrypt|key|token|endpoint|https?://|requests|upload|download|auth
```

El filtro no devolvió coincidencias visibles.

### Interpretación

Este resultado es **evidencia negativa limitada**. No demuestra que `module_authorized` carezca de lógica de red, autorización o cloud. El miembro extraído es bytecode/objeto empaquetado de PyInstaller y puede:

- importar otros módulos sin conservar cadenas ASCII obvias;
- delegar en otro módulo del `PYZ-00.pyz`;
- resolver nombres de forma indirecta;
- contener una capa wrapper distinta de la implementación interna.

Además, el inventario recursivo del bundle ya confirmó por separado la presencia de `aliyunsdkcore`, `aliyunsdkkms`, `oss2`, `requests`, `urllib3`, `socket`, `ssl` y `cryptography` en el scanner.

Por tanto:

```text
MODULE_AUTHORIZED_EXTRAIDO = HECHO
COINCIDENCIAS_CLOUD_ASCII_DIRECTAS = NO OBSERVADAS EN ESTE FILTRO
AUSENCIA_DE_LLAMADAS_CLOUD = NO DEMOSTRADA
TRAFICO_SALIENTE = NO VERIFICADO
```

La siguiente prueba útil es distinguir el wrapper de nivel CArchive del módulo homónimo incluido dentro de `PYZ-00.pyz` y disensamblar bytecode sin ejecutarlo.

## EN · English

The top-level `module_authorized` member was extracted from the `CzurScanner` PyInstaller CArchive without executing CZUR code. A simple ASCII `strings` search for Alibaba/OSS/KMS/HTTP/auth-related terms returned no visible matches.

This is **limited negative evidence only**. It does not demonstrate absence of cloud/network behaviour, because the extracted member may be a wrapper, may delegate to the homonymous module inside `PYZ-00.pyz`, or may resolve functionality indirectly. The recursive bundle inventory independently confirmed Alibaba Cloud SDKs and complete HTTP/TLS stacks elsewhere in the package.

Current classification:

```text
MODULE_AUTHORIZED_EXTRACTED = FACT
DIRECT_CLOUD_ASCII_MATCHES = NOT OBSERVED IN THIS FILTER
ABSENCE_OF_CLOUD_CALLS = NOT DEMONSTRATED
OUTBOUND_TRAFFIC = NOT VERIFIED
```
