# Revisión integral GitHub público · Iteración 02
# Integral public GitHub review · Iteration 02

**Fecha / Date:** 2026-08-30
**Estado / Status:** **LINK_INTEGRITY REPARADO · PASS GLOBAL NO DECLARADO / LINK_INTEGRITY REPAIRED · GLOBAL PASS NOT DECLARED**

[ES · Castellano](#es--resultado) · [EN · English](#en--result)

## ES · Resultado

### Reparación material

Ocho README conservaban bloques `NEO_LATEST_MANIFESTO` anclados en LXXXI o LXXXIV. Se han derivado de nuevo desde `manifiestos/README.md` y ahora todos apuntan a **LXXXV**, su documento real, **Síntesis Abierta #180** y la frontera de **85 manifiestos finitos**.

### Archivos reparados

- `analisis/README.md`
- `analisis/auditorias/README.md`
- `analisis/publicos/README.md`
- `analisis/publicos/evidencias/README.md`
- `auditorias/publicas/README.md`
- `obras/README.md`
- `obras/idea/README.md`
- `obras/idea/assets/README.md`
- `.github/scripts/sync_latest_manifesto_feature.py`
- `.github/workflows/sync-latest-manifesto-feature.yml`

### Causa sistémica corregida

El sincronizador anterior mezclaba la actualización del último manifiesto con migraciones globales de versión y bloques neoaxiomáticos. Se ha reducido a una única responsabilidad: sustituir sólo el contenido comprendido entre `NEO_LATEST_MANIFESTO_START/END`, derivando numeral, título, ruta, SAN y recuento desde el índice canónico vigente. El workflow limita también el conjunto de archivos modificables y ejecuta el gate de enlaces antes de publicar.

### Pruebas

- `LINK_INTEGRITY`: **OK** · 496 Markdown activos · 11.946 enlaces internos · 0 rotos · 0 fallos críticos.
- Relaciones NAX↔manifiestos: **PASS** · NAX-01–NAX-14 en README + documento propio.
- Relaciones de manifiestos: **PASS** · 172 superficies.
- Ontología NEOCore™: **PASS** · 525 superficies.

### Residuos bloqueantes

- `LANGUAGE_NAVIGATION`: 4 documentos aún carecen de selectores ES/EN navegables.
- `CONTENT_SYMMETRY`: el auditor global mantiene 24 superficies señaladas.
- `WIKI_PARITY`: `WIKI_PROJECTION_PENDING`; la Wiki real no se ha verificado.

**PASO_SIGUIENTE_RECOMENDADO:** reparar los cuatro selectores ES/EN ausentes y endurecer su gate para nuevos documentos.

## EN · Result

### Material repair

Eight README files retained `NEO_LATEST_MANIFESTO` blocks fixed at LXXXI or LXXXIV. They have been re-derived from `manifiestos/README.md`; all now point to **LXXXV**, its real document, **Open Synthesis #180**, and the **85 finite manifesto** frontier.

### Repaired files

- `analisis/README.md`
- `analisis/auditorias/README.md`
- `analisis/publicos/README.md`
- `analisis/publicos/evidencias/README.md`
- `auditorias/publicas/README.md`
- `obras/README.md`
- `obras/idea/README.md`
- `obras/idea/assets/README.md`
- `.github/scripts/sync_latest_manifesto_feature.py`
- `.github/workflows/sync-latest-manifesto-feature.yml`

### Systemic cause repaired

The previous synchroniser mixed latest-manifesto updates with repository-wide version migrations and Neoaxiom block rewrites. It now has one responsibility only: replacing content inside `NEO_LATEST_MANIFESTO_START/END`, deriving numeral, title, path, SAN and count from the current canonical index. The workflow also limits the allowed changed files and runs the link gate before publication.

### Tests

- `LINK_INTEGRITY`: **OK** · 496 active Markdown files · 11,946 internal links · 0 broken · 0 critical failures.
- NAX↔manifesto relations: **PASS** · NAX-01–NAX-14 in README + own document.
- Manifesto relations: **PASS** · 172 surfaces.
- NEOCore™ ontology: **PASS** · 525 surfaces.

### Remaining blockers

- `LANGUAGE_NAVIGATION`: 4 documents still lack navigable ES/EN selectors.
- `CONTENT_SYMMETRY`: the global auditor still flags 24 surfaces.
- `WIKI_PARITY`: `WIKI_PROJECTION_PENDING`; the live Wiki was not verified.

**RECOMMENDED_NEXT_STEP:** repair the four missing ES/EN selectors and harden their gate for new documents.
