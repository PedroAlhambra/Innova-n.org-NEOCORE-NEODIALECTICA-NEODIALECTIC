# MAXPROC público · Run 03 · semántica temporal de frontera de manifiestos / Public MAXPROC · Run 03 · manifesto frontier temporal semantics

**Timestamp observado / Observed timestamp:** 2026-08-24 03:33 CEST  
**Repositorio / Repository:** `PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC`  
**7.3-CANDIDATE:** `ACTIVE / NOT_CANON`  

## Estado observado / Observed state

La auditoría global ES/EN vigente en el inicio de esta pasada mantiene el corpus limpio: **314 Markdown activos / 249 documentos ES-EN / 0 fallos estructurales / 0 fallos de marcadores / 0 superficies pareadas / 0 plantillas Issue asimétricas**. / The current global ES/EN audit at the start of this run keeps the corpus clean: **314 active Markdown files / 249 ES-EN documents / 0 structural failures / 0 marker failures / 0 paired surfaces / 0 asymmetric Issue templates**.

## Defecto elegido / Selected defect

`manifiestos/README.md` mostraba `Estado en este commit / State at this commit` y `Fecha / Date: 2026-08-18`. El recuento de 81 manifiestos era correcto, pero la fecha procede del front matter del último manifiesto y representa la **fecha histórica de fijación de la frontera**, no la fecha del commit vivo. El generador `.github/scripts/sync_manifesto_frontier_headers.py` reproducía esa ambigüedad en cada sincronización. / `manifiestos/README.md` displayed `Estado en este commit / State at this commit` and `Fecha / Date: 2026-08-18`. The 81-manifesto count was correct, but the date comes from the latest manifesto front matter and represents the **historical frontier fixation date**, not the live commit date. The generator `.github/scripts/sync_manifesto_frontier_headers.py` reproduced that ambiguity on every sync.

## Acción / Action

Se corrigió la causa raíz en `.github/scripts/sync_manifesto_frontier_headers.py`: / The root cause was corrected in `.github/scripts/sync_manifesto_frontier_headers.py`:

- `Estado en este commit / State at this commit` → `Frontera canónica vigente / Current canonical frontier`.
- `Fecha / Date` → `Fecha de fijación de esta frontera / Frontier fixation date`.
- Las expresiones regulares aceptan tanto las etiquetas históricas como las nuevas, por lo que la transición es idempotente y futuras sincronizaciones no revierten el cambio. / The regular expressions accept both historical and new labels, making the transition idempotent and preventing future syncs from reverting the correction.
- No se modificaron recuentos, ordinales, manifiestos, Neoaxiomas™, Issues de Síntesis, canon ni reglas del gate. / No counts, ordinals, manifestos, Neoaxioms™, Synthesis Issues, canon, or gate rules were changed.

**Commit de reparación / Repair commit:** `3429fef2b02ca71ac5bae1b822cbce629ca3b65e`.

## Pruebas / Evidence

- Lectura posterior del script confirma las nuevas etiquetas y compatibilidad con las antiguas. / Post-change reading of the script confirms the new labels and backward-compatible matching.
- `.github/workflows/sync-open-synthesis-network.yml` incluye este script entre sus rutas de disparo y ejecuta `Synchronize manifesto frontier headers` seguido de las auditorías de registro, paridad, estructura, Neoaxiomas™, relaciones y enlaces. / `.github/workflows/sync-open-synthesis-network.yml` includes this script among its trigger paths and runs `Synchronize manifesto frontier headers` followed by registry, parity, structure, Neoaxiom™, relational, and link audits.
- Al cierre de esta pasada todavía no existe un workflow run o commit automático posterior recuperable para `3429fef2...`; por tanto no se atribuye PASS post-cambio. / At the close of this run there is still no retrievable workflow run or subsequent automatic commit for `3429fef2...`; therefore no post-change PASS is claimed.

## Resultado / Result

`ROOT_CAUSE_FIX = COMMITTED`  
`MANIFESTO_FRONTIER_LABEL_REGENERATION = PENDING`  
`GLOBAL_ES_EN_INHERITED_GATE = PASS_0_0_0_0`  
`POST_CHANGE_WORKFLOW = NOT_VERIFIED`  
`7.3-CANDIDATE = NOT_CANON`

## Residuo / Residual

La superficie `manifiestos/README.md` no se considera reparada hasta observar una regeneración real que sustituya las etiquetas antiguas y conserve los gates limpios. / The `manifiestos/README.md` surface is not considered repaired until a real regeneration is observed replacing the old labels while preserving clean gates.

## PASO_SIGUIENTE / NEXT_STEP

**Verificar que `sync-open-synthesis-network` regenere `manifiestos/README.md` desde `3429fef2...` con `Frontera canónica vigente / Current canonical frontier` y `Fecha de fijación de esta frontera / Frontier fixation date`, y declarar PASS únicamente si las auditorías posteriores conservan 0 fallos estructurales, 0 marcadores, 0 superficies pareadas y 0 plantillas Issue asimétricas. / Verify that `sync-open-synthesis-network` regenerates `manifiestos/README.md` from `3429fef2...` with `Frontera canónica vigente / Current canonical frontier` and `Fecha de fijación de esta frontera / Frontier fixation date`, and declare PASS only if the subsequent audits preserve 0 structural failures, 0 marker failures, 0 paired surfaces, and 0 asymmetric Issue templates.**
