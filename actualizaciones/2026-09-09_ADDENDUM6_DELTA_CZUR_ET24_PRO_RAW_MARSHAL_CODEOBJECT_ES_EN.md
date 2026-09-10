# Addendum VI al Delta de Síntesis · CZUR ET24 Pro en Linux
# Addendum VI to the Synthesis Delta · CZUR ET24 Pro on Linux

**Fecha / Date:** 2026-09-09  
**Estado / Status:** evidencia estática reproducible · `RAW_MARSHAL_CODE_OBJECT=CONFIRMADO` · `PYTHON_VERSION=PROBABLE_3.8` · `NETWORK_ACTIVITY=NO_VERIFICADA`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

Se inspeccionaron los primeros 32 bytes de dos miembros extraídos con `pyi-archive_viewer`:

```text
module_authorized_pyz.bin:
e3 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 03 00 00 00 40 00 00 00 f3 5a 00 00 00 64 00

czur_create_main.bin:
e3 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 05 00 00 00 40 00 00 00 73 74 00 00 00 64 00
```

El byte inicial `0xe3` es coherente con un objeto `code` serializado mediante `marshal` con el flag de referencia de CPython, no con una cabecera `.pyc` completa. Esto encaja con la extracción de miembros internos de PyInstaller/PYZ y explica que `file(1)` los clasifique simplemente como `data`.

La presencia previa en el bundle de artefactos `cpython-38.pyc` hace probable que el bytecode corresponda a Python 3.8; debe confirmarse con un disassembler cross-version antes de asignar versión definitivamente.

Estado:

```text
RAW_MARSHAL_CODE_OBJECT = CONFIRMADO
FULL_PYC_HEADER = AUSENTE
PYTHON_3_8 = PROBABLE / A CONFIRMAR
DIRECT_NETWORK_CALLS_IN_THESE_TWO_MEMBERS = AUN_NO_DEMOSTRADAS
```

Siguiente paso: usar `xdis/pydisasm` o herramienta equivalente cross-version para desensamblar el marshal extraído sin ejecutar código CZUR, y seguir la cadena de imports/llamadas desde `module_authorized` y `czur_create:main`.

## EN · English

The first 32 bytes of two members extracted with `pyi-archive_viewer` were inspected:

```text
module_authorized_pyz.bin:
e3 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 03 00 00 00 40 00 00 00 f3 5a 00 00 00 64 00

czur_create_main.bin:
e3 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 05 00 00 00 40 00 00 00 73 74 00 00 00 64 00
```

The initial byte `0xe3` is consistent with a `code` object serialized through `marshal` with CPython's reference flag, rather than a complete `.pyc` header. This fits extraction of internal PyInstaller/PYZ members and explains why `file(1)` classifies them simply as `data`.

The earlier presence of `cpython-38.pyc` artifacts in the bundle makes Python 3.8 a likely bytecode version; this must be confirmed with a cross-version disassembler before assigning the version definitively.

State:

```text
RAW_MARSHAL_CODE_OBJECT = CONFIRMED
FULL_PYC_HEADER = ABSENT
PYTHON_3_8 = PROBABLE / TO BE CONFIRMED
DIRECT_NETWORK_CALLS_IN_THESE_TWO_MEMBERS = NOT YET DEMONSTRATED
```

Next step: use `xdis/pydisasm` or an equivalent cross-version tool to disassemble the extracted marshal without executing CZUR code, then follow the import/call chain from `module_authorized` and `czur_create:main`.
