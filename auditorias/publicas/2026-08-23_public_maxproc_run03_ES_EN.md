# MAXPROC público · Run 03 / Public MAXPROC · Run 03

**Fecha / Date:** 2026-08-23  
**Estado / Status:** `REPAIR_TRIGGERED / VERIFICATION_PENDING`  
**Frontera / Boundary:** `NEOCore™ 7.3-CANDIDATE ≠ CANON`

## ES · Castellano

### Estado observado

La auditoría global vigente confirma **305 Markdown activos**, **240 documentos ES/EN divididos**, **1 fallo estructural**, **0 fallos de marcadores** y **0 superficies pareadas pendientes**. El único fallo restante es `propuestas/sintesis-abierta/2026-08-19_NEOCore_7_3_AUTOSINTESIS_LOTE_02_XIII_XXXII_ES_EN.md`.

### Problema elegido

El lote 02 conserva contenido ES/EN sustantivamente pareado, pero usa una arquitectura intercalada por sección (`### ES` / `### EN`). El gate global interpreta el primer `### ES` como comienzo de la mitad española y el primer `### EN` como comienzo de la mitad inglesa, de modo que contabiliza el resto del documento dentro de EN y produce un falso desequilibrio estructural (`ES=184`, `EN=5290`, ratio `28.75`).

### Acción

Se añadió el workflow de una sola ejecución `.github/workflows/oneshot-fix-lot02-symmetry.yml`, commit `4572f68c5a3f3c3c93ac598cdc13873c0c27bf98`. El workflow reconstruye XIII–XXXII en dos mitades documentales completas `# ES · Castellano` y `# EN · English`, conserva las veinte respuestas y antítesis, duplica el gate en forma lingüísticamente simétrica, ejecuta `audit_global_bilingual_symmetry.py` y `audit_markdown_links_readmes.py`, exige explícitamente `0` fallos estructurales, `0` fallos de marcadores y `0` superficies pareadas, y sólo entonces compromete el cambio. El propio workflow se elimina en el commit final para no dejar infraestructura temporal.

### Prueba y resultado

El gate previo está demostrado en `auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md`: queda exactamente un fallo, lote 02. La reparación automática ha sido disparada, pero en el momento de esta nota todavía no existe un commit posterior verificable que demuestre que la ejecución terminó y pasó todos los gates. Por tanto **no se declara PASS**.

### Residuo

`GLOBAL_ES_EN = 1 → reparación en curso / verificación pendiente`.

### PASO_SIGUIENTE

Verificar el commit producido por `oneshot-fix-lot02-symmetry`; sólo si la auditoría regenerada marca `0` fallos estructurales, `0` marcadores y `0` superficies pareadas, registrar `GLOBAL_ES_EN=PASS` y pasar a revisar el siguiente defecto público no relacionado con simetría.

---

## EN · English

### Observed state

The current global audit confirms **305 active Markdown files**, **240 split ES/EN documents**, **1 structural failure**, **0 marker failures**, and **0 paired surfaces pending review**. The only remaining failure is `propuestas/sintesis-abierta/2026-08-19_NEOCore_7_3_AUTOSINTESIS_LOTE_02_XIII_XXXII_ES_EN.md`.

### Selected problem

Batch 02 contains materially paired ES/EN content, but it uses a section-interleaved architecture (`### ES` / `### EN`). The global gate interprets the first `### ES` as the start of the Spanish half and the first `### EN` as the start of the English half, so the rest of the document is charged to EN and produces a false structural imbalance (`ES=184`, `EN=5290`, ratio `28.75`).

### Action

A one-shot workflow was added at `.github/workflows/oneshot-fix-lot02-symmetry.yml`, commit `4572f68c5a3f3c3c93ac598cdc13873c0c27bf98`. The workflow rebuilds XIII–XXXII into two complete documentary halves, `# ES · Castellano` and `# EN · English`, preserves all twenty answers and antitheses, duplicates the gate in linguistically symmetric form, runs `audit_global_bilingual_symmetry.py` and `audit_markdown_links_readmes.py`, explicitly requires `0` structural failures, `0` marker failures and `0` paired surfaces, and commits only after those conditions pass. The workflow removes itself in the final commit so no temporary infrastructure remains.

### Test and result

The pre-repair gate is demonstrated in `auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md`: exactly one failure remains, Batch 02. The automated repair has been triggered, but at the time of this note there is not yet a later verifiable commit proving completion and gate success. Therefore **PASS is not declared**.

### Residual state

`GLOBAL_ES_EN = 1 → repair in progress / verification pending`.

### NEXT_STEP

Verify the commit produced by `oneshot-fix-lot02-symmetry`; only if the regenerated audit reports `0` structural failures, `0` marker failures and `0` paired surfaces, record `GLOBAL_ES_EN=PASS` and proceed to the next public defect unrelated to symmetry.
