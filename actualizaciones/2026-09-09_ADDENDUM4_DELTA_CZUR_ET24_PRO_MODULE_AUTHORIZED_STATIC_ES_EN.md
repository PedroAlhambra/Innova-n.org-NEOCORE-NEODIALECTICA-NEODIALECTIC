# Addendum IV al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum IV to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `MODULE_AUTHORIZED_EXTRACTED=PASS` · `DIRECT_CLOUD_STRINGS=NO_OBSERVADAS_EN_PRIMER_FILTRO`

Relacionado: Delta principal y Addenda I–III de la auditoría CZUR ET24 Pro/Linux.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

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

The top-level `module_authorized` member was extracted from the `PKG/CArchive` of `CzurScanner` using `pyi-archive_viewer`, without executing CZUR software.

Artifact obtained:

```text
~/CZUR-package-audit/key-modules/module_authorized.bin
observed size: ~4.1 KiB
```

A simple ASCII search was applied with `strings -a` and a filter for:

```text
aliyun|aliyuncs|oss2|bucket|put_object|get_object|kms|encrypt|decrypt|key|token|endpoint|https?://|requests|upload|download|auth
```

The filter returned no visible matches.

### Interpretation

This result is **limited negative evidence**. It does not demonstrate that `module_authorized` lacks network, authorization or cloud logic. The extracted member is a PyInstaller packaged bytecode/object and may:

- import other modules without retaining obvious ASCII strings;
- delegate to another module inside `PYZ-00.pyz`;
- resolve names indirectly;
- contain a wrapper layer distinct from the internal implementation.

In addition, the recursive bundle inventory independently confirmed the presence of `aliyunsdkcore`, `aliyunsdkkms`, `oss2`, `requests`, `urllib3`, `socket`, `ssl` and `cryptography` in the scanner.

Therefore:

```text
MODULE_AUTHORIZED_EXTRACTED = FACT
DIRECT_CLOUD_ASCII_MATCHES = NOT OBSERVED IN THIS FILTER
ABSENCE_OF_CLOUD_CALLS = NOT DEMONSTRATED
OUTBOUND_TRAFFIC = NOT VERIFIED
```

The next useful test is to distinguish the CArchive-level wrapper from the homonymous module included inside `PYZ-00.pyz` and disassemble the bytecode without executing it.
