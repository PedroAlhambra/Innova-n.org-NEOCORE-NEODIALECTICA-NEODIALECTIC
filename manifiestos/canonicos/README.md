# Nombres canónicos de manifiestos / Canonical manifesto filenames

## Regla

El **número romano es el identificador canónico** del manifiesto y debe ser visible también en su nombre de archivo canónico.

Patrón:

`<ROMANO>_<slug>_ES_EN.md`

Ejemplo:

`I_neo0_soberania_de_guia_ES_EN.md`

Los nombres históricos se mantienen temporalmente como rutas **legacy** para no romper enlaces, citas, navegación, auditorías ni referencias externas. La correspondencia completa I–LX está registrada en `../CANONICAL_FILENAMES.json`.

**No se debe inferir jamás el número canónico a partir del prefijo decimal histórico.**

La migración debe copiar el mismo blob/contenido a la ruta canónica, actualizar referencias y sólo retirar una ruta legacy cuando no queden dependencias.
