# Auditoría de completitud del registro canónico de manifiestos / Canonical manifesto registry completeness audit

**Fecha / Date:** 2026-08-25  
**Entradas canónicas / Canonical entries:** 81  
**Problemas / Problems:** 0

## Regla / Rule

Un archivo de manifiesto con ordinal romano y metadato `Manifiesto / Manifesto` válidos no puede quedar fuera de `CANONICAL_FILENAMES.json`. La ruta del espejo canónico se deriva de forma determinista de la fuente y debe terminar en `.md`; el espejo debe existir y conservar la misma identidad romana. `manifiestos/canonicos/` no puede contener espejos huérfanos fuera del registro, salvo su `README.md`. Los duplicados históricos de un ordinal ya registrado pueden conservarse como rutas legacy fuera de la superficie canónica, pero no crean un segundo nodo canónico. / A manifesto file with a valid Roman ordinal and `Manifesto` identity metadata may not remain outside `CANONICAL_FILENAMES.json`. The canonical mirror path is derived deterministically from the source and must end in `.md`; the mirror must exist and preserve the same Roman identity. `manifiestos/canonicos/` may not contain orphan mirrors outside the registry, except its `README.md`. Historical duplicate routes for an already registered ordinal may be preserved as legacy routes outside the canonical surface, but do not create a second canonical node.

## Hallazgos / Findings

- Ninguno / None.
