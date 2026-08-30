# Revisión integral GitHub público · Iteración 05
# Integral public GitHub review · Iteration 05

**Fecha / Date:** 2026-08-31
**Baseline de rama / Branch baseline:** `f8c7e9b9b88df43ac47ba608524bffdf52ed868a`
**Commit material:** `7f687e87637e1d108c81bc231e7546abde08396d`
**Rama / Branch:** `fix/maxproc-lxxxv-symmetry-20260830`
**Tipo / Type:** MAXPROC · reparación pública propuesta mediante PR; NO_WEB4 · NO_HOSTALIA · NO_PRIVATE / public repair proposed through PR; NO_WEB4 · NO_HOSTALIA · NO_PRIVATE

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### Hallazgo material y causa raíz

Cuatro superficies bilingües activas contenían capas ES y EN con encabezados válidos, pero carecían de un selector visible anterior al cuerpo español. El contenido era accesible por desplazamiento, pero no cumplía la navegación lingüística declarada. Los workflows que sincronizan y reparan manifiestos ejecutaban simetría global, pero no invocaban explícitamente el gate de selectores antes de confirmar cambios.

### Reparación aplicada

- Añadidos selectores ES/EN con anchors reales a las iteraciones relacionales 06, 07 y 08.
- Añadido el mismo selector al delta de relación genealógica navegable.
- La iteración 06 apunta a sus primeros encabezados reales `ES · Estado inicial` y `EN · Initial state`; no se inventaron anchors genéricos.
- Los workflows de sincronización y reparación genealógica bloquean ahora el commit si falla `audit_language_selectors.py`.
- El auditor de registro canónico deja de generar espacios finales en metadatos, evitando que su propia evidencia falle `git diff --check`.

### Archivos materiales

- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_06_ES_EN.md`
- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_07_ES_EN.md`
- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_08_ES_EN.md`
- `manifiestos/deltas/2026-08-29_relacion_genealogica_navegable_ES_EN.md`
- `.github/workflows/sync-manifesto-crossrefs.yml`
- `.github/workflows/repair-manifesto-genealogical-links.yml`
- `.github/scripts/audit_manifesto_registry_completeness.py`

### Pruebas frescas

- `LANGUAGE_NAVIGATION`: PASS · 428 superficies antes de añadir esta traza · 0 fallos.
- Prueba negativa: retirar el selector del delta genealógico produce `LANGUAGE_NAVIGATION_FAILURE` y código de salida 1.
- `LINK_INTEGRITY`: PASS · 500 Markdown · 12.027 enlaces internos · 0 rotos · 0 críticos.
- `RELATIONAL_NAVIGATION` y `GENEALOGICAL_NAVIGATION`: PASS · 172 superficies.
- `CANONICAL_STATE` y `SOURCE_MIRROR_INTEGRITY`: PASS · 85 entradas · 0 problemas.
- `VERSION_STATE`: PASS · versión vigente resuelta exclusivamente desde `versiones/README.md`.
- `WIKI_PARITY`: PASS · 15 páginas de `wiki-source` alcanzables; la proyección mínima verificada conserva 12 páginas publicadas.
- Guard ontológico: PASS · 529 superficies; Neo0™ y ONe Starkdr™ conservan funciones distintas.
- `git diff --check`: PASS.

### Residuos bloqueantes

- `CONTENT_SYMMETRY = FAIL_2`: las iteraciones relacionales 06 y 08 conservan asimetrías históricas de volumen o esqueleto.
- No hay PASS global ni promoción automática a `main`; la reparación permanece en la PR #181.

### Dictamen

`LANGUAGE_NAVIGATION_REPAIRED / NEGATIVE_TEST_PASS / CONTENT_SYMMETRY_BLOCKED / PR_REVIEW_REQUIRED`.

---

## EN · English

### Material finding and root cause

Four active bilingual surfaces contained valid ES and EN layers, but lacked a visible selector before the Spanish body. Their content was reachable by scrolling, yet did not satisfy declared language navigation. The workflows that synchronise and repair manifestos ran global symmetry checks, but did not explicitly invoke the selector gate before committing changes.

### Applied repair

- Added ES/EN selectors with real anchors to relational iterations 06, 07 and 08.
- Added the same selector to the navigable genealogical-relation delta.
- Iteration 06 targets its actual first headings, `ES · Estado inicial` and `EN · Initial state`; no generic anchors were invented.
- Genealogical synchronisation and repair workflows now block their commit when `audit_language_selectors.py` fails.
- The canonical-registry auditor no longer generates trailing spaces in metadata, preventing its own evidence from failing `git diff --check`.

### Material files

- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_06_ES_EN.md`
- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_07_ES_EN.md`
- `auditorias/publicas/2026-08-30_reparacion_relacional_manifiestos_iteracion_08_ES_EN.md`
- `manifiestos/deltas/2026-08-29_relacion_genealogica_navegable_ES_EN.md`
- `.github/workflows/sync-manifesto-crossrefs.yml`
- `.github/workflows/repair-manifesto-genealogical-links.yml`
- `.github/scripts/audit_manifesto_registry_completeness.py`

### Fresh tests

- `LANGUAGE_NAVIGATION`: PASS · 428 surfaces before adding this trace · 0 failures.
- Negative test: removing the selector from the genealogical delta produces `LANGUAGE_NAVIGATION_FAILURE` and exit code 1.
- `LINK_INTEGRITY`: PASS · 500 Markdown files · 12,027 internal links · 0 broken · 0 critical.
- `RELATIONAL_NAVIGATION` and `GENEALOGICAL_NAVIGATION`: PASS · 172 surfaces.
- `CANONICAL_STATE` and `SOURCE_MIRROR_INTEGRITY`: PASS · 85 entries · 0 problems.
- `VERSION_STATE`: PASS · current version resolved exclusively from `versiones/README.md`.
- `WIKI_PARITY`: PASS · 15 `wiki-source` pages reachable; the verified minimum projection retains 12 published pages.
- Ontological guard: PASS · 529 surfaces; Neo0™ and ONe Starkdr™ retain distinct roles.
- `git diff --check`: PASS.

### Blocking residue

- `CONTENT_SYMMETRY = FAIL_2`: relational iterations 06 and 08 retain historical volume or heading-skeleton asymmetries.
- There is no global PASS or automatic promotion to `main`; the repair remains in PR #181.

### Verdict

`LANGUAGE_NAVIGATION_REPAIRED / NEGATIVE_TEST_PASS / CONTENT_SYMMETRY_BLOCKED / PR_REVIEW_REQUIRED`.

---

## PASO_SIGUIENTE_RECOMENDADO / NEXT_RECOMMENDED_STEP

Reconciliar la simetría semántica y estructural de las iteraciones relacionales 06 y 08, preservando literalmente sus hechos históricos, commits y dictámenes, y volver a ejecutar el gate global. / Reconcile the semantic and structural symmetry of relational iterations 06 and 08 while preserving their historical facts, commits and verdicts verbatim, then rerun the global gate.
