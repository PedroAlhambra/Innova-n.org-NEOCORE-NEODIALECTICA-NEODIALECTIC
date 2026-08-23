# MAXPROC público · Run 08 · procedencia temporal de la auditoría global ES/EN
# Public MAXPROC · Run 08 · temporal provenance of the global ES/EN audit

**Fecha / Date:** 2026-08-23 07:35 CEST  
**Estado / Status:** `TARGET_FIX_COMMITTED / WORKFLOW_VERIFICATION_PENDING`  
**Frontera / Frontier:** `NEOCore™ 7.3-CANDIDATE ≠ CANON`

## ES · Castellano

### Estado observado

La corrección del run 07 quedó efectivamente validada: el postcheck dinámico de README, índices y enlaces ya se ha regenerado con fecha `2026-08-23`, estado `OK`, 398 Markdown activos revisados, 17 README, 10.778 enlaces internos de ruta comprobados, 0 enlaces internos rotos y 0 fallos canónicos críticos.

La auditoría global ES/EN vigente también está materialmente limpia en su gate: 310 Markdown activos, 245 documentos con secciones ES/EN divididas, 0 fallos estructurales, 0 fallos de marcadores, 0 superficies pareadas pendientes y 0 plantillas de Issue con etiquetas visibles no simétricas.

### Problema elegido

El generador `.github/scripts/audit_global_bilingual_symmetry.py` continuaba escribiendo una fecha fija `2026-08-12` en la cabecera de `auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md`, aunque el mismo informe contiene métricas regeneradas y actuales.

Esto crea una contradicción de procedencia temporal equivalente a la ya reparada en el postcheck: el nombre histórico del archivo puede conservarse por genealogía, pero la cabecera del informe vivo debe indicar la fecha real de regeneración.

### Acción

Se actualizó el endurecedor público `.github/scripts/harden_global_symmetry_auditor.py` para que, al ejecutarse:

- añada `datetime` y `timezone` al auditor global si todavía no existen;
- sustituya la fecha fija de la cabecera por `datetime.now(timezone.utc).date().isoformat()`;
- conserve el nombre histórico del archivo de auditoría;
- no altere reglas del gate, umbrales, exclusiones, inventario, canon, manifiestos, Neoaxiomas, Síntesis ni estados de 7.3-CANDIDATE.

**Commit de la corrección del endurecedor:** `e5a6339d497ebc6a24b62ed436245b95d9806a44`.

El workflow `harden-global-symmetry-auditor` está configurado para ejecutarse al cambiar ese endurecedor y escribir el auditor resultante. Al cierre de esta iteración el auditor global en `main` todavía conserva el import antiguo y la fecha fija, por lo que no se atribuye un PASS del workflow antes de observar el commit resultante.

### Pruebas y resultado

- Confirmado que el postcheck del run 07 ya presenta fecha dinámica `2026-08-23` y `Estado = OK`.
- Confirmado que el auditor global vigente conserva todavía `**Fecha / Date:** 2026-08-12` pese a métricas actuales `310 / 245 / 0 / 0 / 0`.
- Confirmado en el código del auditor que la fecha está fijada literalmente en la lista `lines`.
- Confirmado que el endurecedor actualizado contiene la sustitución determinista hacia fecha UTC dinámica.
- No se ha rebajado ninguna regla de auditoría ni se ha promovido `7.3-CANDIDATE`.

**Resultado del objetivo:** `FIX_COMMITTED`.  
**Resultado del workflow posterior:** `VERIFICATION_PENDING`.

### Residuos

Sólo queda verificar que el workflow escriba el cambio en `audit_global_bilingual_symmetry.py`, regenere la auditoría con fecha actual y mantenga el gate global limpio.

### PASO_SIGUIENTE

**Verificar que el workflow derivado de `e5a6339d...` actualiza el auditor y regenera la auditoría global con fecha `2026-08-23` (o fecha UTC efectiva de ejecución) manteniendo exactamente 0 fallos estructurales, 0 fallos de marcadores, 0 superficies pareadas pendientes y 0 plantillas de Issue no simétricas; sólo entonces declarar PASS de esta corrección y pasar al siguiente defecto material.**

---

## EN · English

### Observed state

The run 07 correction has now been effectively validated: the dynamic README, index and link postcheck has regenerated with date `2026-08-23`, status `OK`, 398 active Markdown files reviewed, 17 README files, 10,778 internal path links checked, 0 broken internal links and 0 critical canonical failures.

The current global ES/EN audit is also materially clean at gate level: 310 active Markdown files, 245 documents with split ES/EN sections, 0 structural failures, 0 marker failures, 0 paired surfaces pending review and 0 Issue templates with non-symmetric visible labels.

### Selected problem

The `.github/scripts/audit_global_bilingual_symmetry.py` generator still wrote a fixed `2026-08-12` date into the header of `auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md`, even though the same report contains regenerated current metrics.

This creates the same temporal-provenance contradiction already fixed in the postcheck: the historical filename may remain for genealogy, but the living report header must state the actual regeneration date.

### Action

The public hardener `.github/scripts/harden_global_symmetry_auditor.py` was updated so that, when executed, it:

- adds `datetime` and `timezone` to the global auditor if they are not already present;
- replaces the fixed report-header date with `datetime.now(timezone.utc).date().isoformat()`;
- preserves the historical audit filename;
- does not alter gate rules, thresholds, exclusions, inventory, canon, Manifestos, Neoaxioms, Synthesis or 7.3-CANDIDATE states.

**Hardener repair commit:** `e5a6339d497ebc6a24b62ed436245b95d9806a44`.

The `harden-global-symmetry-auditor` workflow is configured to run when that hardener changes and to write the resulting auditor. At iteration close, the global auditor on `main` still retains the old import and fixed date, so no workflow PASS is attributed before observing the resulting commit.

### Tests and result

- Confirmed that the run 07 postcheck now shows dynamic date `2026-08-23` and `Status = OK`.
- Confirmed that the current global audit still retains `**Fecha / Date:** 2026-08-12` despite current `310 / 245 / 0 / 0 / 0` metrics.
- Confirmed in the auditor source that the date is literally fixed in the `lines` list.
- Confirmed that the updated hardener contains a deterministic replacement to a dynamic UTC date.
- No audit rule was weakened and `7.3-CANDIDATE` was not promoted.

**Target result:** `FIX_COMMITTED`.  
**Post-change workflow result:** `VERIFICATION_PENDING`.

### Residues

Only verification remains: the workflow must write the change into `audit_global_bilingual_symmetry.py`, regenerate the audit with the current date and preserve the clean global gate.

### NEXT_STEP

**Verify that the workflow derived from `e5a6339d...` updates the auditor and regenerates the global audit with date `2026-08-23` (or the effective UTC execution date) while preserving exactly 0 structural failures, 0 marker failures, 0 paired surfaces pending review and 0 non-symmetric Issue templates; only then declare this correction PASS and move to the next material defect.**
