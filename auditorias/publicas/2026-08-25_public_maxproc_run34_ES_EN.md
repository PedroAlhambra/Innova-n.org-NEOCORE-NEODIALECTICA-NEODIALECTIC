# MAXPROC público · Run34 · Reparación de enlaces residuales Issue #174 / Public MAXPROC · Run34 · Residual Issue #174 link repair

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Fecha / Date:** 2026-08-25  
**Frontera / Boundary:** `7.3-CANDIDATE / NOT_CANON`  
**Resultado / Result:** `SELECTED_DEFECT_FIXED · LINK_INTEGRITY_PASS · GLOBAL_PASS_NO`

---

# ES · Castellano

## 1. Estado vivo previo

Se revisaron el head público y las auditorías vigentes antes de modificar. El estado era:

- `CONTENT_SYMMETRY = FAIL`: 352 Markdown activos de alcance bilingüe, 286 documentos ES/EN divididos y 1 fallo estructural restante en `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`;
- `LANGUAGE_NAVIGATION = FAIL`: 370 superficies explícitas ES/EN auditadas y 3 fallos de selector;
- `LINK_INTEGRITY = FAIL`: 441 Markdown activos del grafo vivo, 10.835 rutas internas comprobadas, 2 enlaces internos rotos y 0 fallos canónicos críticos;
- canon detectado por el auditor: 81 manifiestos I–LXXXI; `7.3-CANDIDATE` permanece `NOT_CANON`.

## 2. Primer fallo real prioritario

Los dos enlaces internos rotos procedían de `auditorias/publicas/2026-08-25_public_maxproc_run32_ES_EN.md`. La traza conservaba dos apariciones Markdown de la ruta histórica `../issues/174`; el validador las interpretaba como destinos vivos relativos inexistentes aunque la Issue pública #174 existe y está abierta.

## 3. Corrección exclusiva

Se modificó únicamente la traza run32 para eliminar esas dos rutas relativas interpretables como enlaces vivos y conservar su significado histórico en texto, manteniendo la URL pública real de Issue #174.

**Commit material:** `d00d6712bd8e91d31f0ac8424d5e046b25b63f6e`.

No se modificaron manifiestos, Neoaxiomas, protocolos CMN, contenido de Síntesis, índices canónicos ni genealogía. No se corrigieron en esta iteración los fallos ES/EN o de selector todavía abiertos.

## 4. Verificación

La Issue #174 fue verificada como existente, abierta y correspondiente a `Síntesis Abierta · Ciencia Multidimensional Neodialéctica™ y «Cáncer de la Síntesis»`.

El postcheck automático posterior quedó en:

- 441 Markdown activos revisados;
- 10.833 rutas internas comprobadas;
- **0 enlaces internos rotos**;
- **0 fallos canónicos críticos**;
- 81 manifiestos canónicos detectados, I–LXXXI.

Por tanto `LINK_INTEGRITY = PASS` para el fallo seleccionado. Los gates de contenido y navegación lingüística siguen sin rebajarse y permanecen `FAIL` mientras sus defectos reales continúen.

## 5. Genealogía y frontera preservadas

La reparación no cambia la condición de Issue #174 como Síntesis Abierta ni convierte LXXXII o cualquier otra superficie candidata en canon. Se mantiene explícitamente:

`7.3-CANDIDATE = NOT_CANON`.

## 6. Único siguiente paso

Corregir exclusivamente el único fallo estructural ES/EN restante en `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`, restaurando el mismo esqueleto de encabezados en ambas capas sin comprimir contenido y volver a ejecutar la auditoría global.

---

# EN · English

## 1. Previous living state

The public head and current audits were reviewed before modification. The state was:

- `CONTENT_SYMMETRY = FAIL`: 352 active Markdown files in bilingual scope, 286 split ES/EN documents and 1 remaining structural failure in `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`;
- `LANGUAGE_NAVIGATION = FAIL`: 370 explicit ES/EN surfaces audited and 3 selector failures;
- `LINK_INTEGRITY = FAIL`: 441 active Markdown files in the living graph, 10,835 internal paths checked, 2 broken internal links and 0 critical canonical failures;
- canon detected by the auditor: 81 manifestos I–LXXXI; `7.3-CANDIDATE` remains `NOT_CANON`.

## 2. First real priority defect

Both broken internal links originated in `auditorias/publicas/2026-08-25_public_maxproc_run32_ES_EN.md`. The trace retained two Markdown occurrences of the historical `../issues/174` path; the validator interpreted them as nonexistent live relative targets even though public Issue #174 exists and is open.

## 3. Exclusive correction

Only the run32 trace was modified to remove those relative paths as parseable live links while preserving their historical meaning in text and retaining the real public URL for Issue #174.

**Material commit:** `d00d6712bd8e91d31f0ac8424d5e046b25b63f6e`.

No manifestos, Neoaxioms, CMN protocols, Synthesis content, canonical indexes or genealogy were modified. The still-open ES/EN and language-selector defects were not corrected in this iteration.

## 4. Verification

Issue #174 was verified as existing, open and corresponding to `Open Synthesis · Neodialectical Multidimensional Science™ and “Cancer of Synthesis”`.

The subsequent automatic postcheck reports:

- 441 active Markdown files reviewed;
- 10,833 internal paths checked;
- **0 broken internal links**;
- **0 critical canonical failures**;
- 81 canonical manifestos detected, I–LXXXI.

Therefore `LINK_INTEGRITY = PASS` for the selected defect. Content and language-navigation gates were not lowered and remain `FAIL` while their real defects persist.

## 5. Preserved genealogy and boundary

The repair does not change Issue #174's status as Open Synthesis and does not turn LXXXII or any other candidate surface into canon. It explicitly preserves:

`7.3-CANDIDATE = NOT_CANON`.

## 6. Single next step

Fix exclusively the sole remaining ES/EN structural failure in `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`, restoring the same heading skeleton in both language layers without compressing content, then rerun the global audit.
