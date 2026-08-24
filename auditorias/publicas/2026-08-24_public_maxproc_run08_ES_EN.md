# MAXPROC público · Run 08 · Gate vivo, reparación de Run 07 y residuo de navegación lingüística
# Public MAXPROC · Run 08 · Live gate, Run 07 repair and language-navigation residue

**Fecha / Date:** 2026-08-24  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Head observado al iniciar / Head observed at start:** `191d43fe9f4f37d39ff32c1cade3d9bd9dae4eb2`  
**Commit del delta / Delta commit:** `318ab287bb2703aee7512e61ff7ef19207408eae`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

### Estado observado

Se releen las superficies públicas requeridas: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN vigente y la nota MAXPROC pública anterior.

La frontera pública continúa siendo `7.3-CANDIDATE`, explícitamente abierta y no canónica. La auditoría global versionada más reciente informa **319 Markdown activos**, **253 documentos ES/EN divididos**, **2 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. Los dos fallos señalados son las trazas `Run 06` y `Run 07`; por tanto no existe PASS global demostrable.

También se comprueba la nueva capa de navegación lingüística: `.github/scripts/audit_language_selectors.py` y `.github/workflows/audit-language-selectors.yml` existen ya en `main`. El gate exige selector visible ES/EN antes del cuerpo de toda página con gates explícitos. No se observa todavía status CI recuperable para el head, por lo que su resultado global no se inventa.

### Revisión de Issues, PR y regresión de selector

La Issue pública #132 permanece abierta y conserva aportes externos con atribución explícita y la cautela `APORTE EXTERNO ≠ VALIDACIÓN`.

Existen dos PR de mantenimiento antiguas todavía abiertas, #165 y #167, ambas vinculadas a limpieza de referencias PRE-7.3. No se fusionan ni se reutilizan en esta iteración.

La regresión de navegación lingüística está verificada al menos en LXXVIII–LXXXI: LXXVIII, LXXIX, LXXX y LXXXI tienen las capas `# ES` y `# EN` pero carecen del selector inicial visible en sus rutas vivas; la misma ausencia está verificada en sus espejos canónicos. Por contraste, LXXV–LXXVII sí conservan selector. Esto confirma una frontera de regresión reciente y un fallo de capacidad de lectura, no de traducción.

### Problema elegido

El gate global ES/EN vigente señalaba la propia nota `2026-08-24_public_maxproc_run07_ES_EN.md` como fallo estructural porque el `PASO_SIGUIENTE / NEXT_STEP` compartido posterior al bloque EN era contado como un párrafo adicional de la mitad inglesa.

Es un defecto público verificable, autocontenido y reversible que impedía reducir el gate estructural con fidelidad.

### Acción

Se modificó exclusivamente `auditorias/publicas/2026-08-24_public_maxproc_run07_ES_EN.md`.

El paso siguiente dejó de existir como párrafo compartido posterior a EN y pasó a estar representado simétricamente dentro de ambas mitades como `### Paso siguiente` y `### Next step`. No se alteraron manifiestos, Neoaxiomas™, Issues, contenido de Síntesis, genealogía ni reglas de canon.

**Commit:** `318ab287bb2703aee7512e61ff7ef19207408eae`.

### Pruebas y resultado

La lectura posterior de Run 07 confirma cinco encabezados `###` en ES y cinco equivalentes en EN, con el mismo bloque de continuación dentro de cada mitad y sin párrafo compartido posterior al bloque inglés.

**Resultado del objetivo:** `PASS` para la reparación estructural local de Run 07.

No se declara PASS global: la auditoría versionada aún conserva dos fallos hasta que se regenere y Run 06 continúa como residuo conocido. El nuevo gate de selector tampoco dispone todavía de un status CI recuperable y existen fallos de navegación lingüística materialmente verificados.

### Residuos

- `Run 06` continúa listado por la auditoría global como fallo estructural hasta nueva reparación/reauditoría.
- LXXVIII–LXXXI carecen de selector inicial ES/EN en las rutas vivas verificadas y en sus espejos canónicos.
- `LANGUAGE_SELECTOR_GATE` debe considerarse `NOT_VERIFIED / MATERIAL_FAILURES_CONFIRMED`, nunca PASS por ausencia de status.
- PR #165 y #167 siguen abiertas como mantenimiento histórico y no forman parte de esta reparación.

### Paso siguiente

Reparar LXXVIII como primer caso de la regresión de navegación lingüística, añadiendo el selector visible `[ES · Castellano](#es--castellano) · [EN · English](#en--english)` tanto a la ruta viva como a su espejo canónico sin modificar el contenido sustantivo, y verificar después el gate de selector antes de avanzar a LXXIX.

## EN · English

### Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the current global ES/EN audit, and the previous public MAXPROC note.

The public frontier remains `7.3-CANDIDATE`, explicitly open and non-canonical. The latest versioned global audit reports **319 active Markdown files**, **253 split ES/EN documents**, **2 structural failures**, **0 marker failures**, **0 paired surfaces pending review**, and **0 asymmetric Issue templates**. The two reported failures are the `Run 06` and `Run 07` traces; therefore no global PASS is demonstrated.

The new language-navigation layer was also checked: `.github/scripts/audit_language_selectors.py` and `.github/workflows/audit-language-selectors.yml` already exist on `main`. The gate requires a visible ES/EN selector before the body of every page with explicit language gates. No recoverable CI status is yet visible for the head, so its global result is not invented.

### Issue, PR and selector-regression review

Public Issue #132 remains open and preserves external inputs with explicit attribution and the safeguard `EXTERNAL INPUT ≠ ENDORSEMENT`.

Two older maintenance PRs remain open, #165 and #167, both related to cleanup of PRE-7.3 references. Neither is merged nor reused in this iteration.

The language-navigation regression is verified at least in LXXVIII–LXXXI: LXXVIII, LXXIX, LXXX and LXXXI contain both `# ES` and `# EN` layers but lack the visible initial selector in their live routes; the same absence is verified in their canonical mirrors. By contrast, LXXV–LXXVII retain the selector. This confirms a recent regression frontier and a reader-capability failure rather than a translation failure.

### Selected problem

The current global ES/EN gate flagged `2026-08-24_public_maxproc_run07_ES_EN.md` itself as a structural failure because its shared `PASO_SIGUIENTE / NEXT_STEP` paragraph after the EN block was counted as an additional paragraph belonging to the English half.

This was a public, verifiable, self-contained and reversible defect preventing the structural gate from decreasing faithfully.

### Action

Only `auditorias/publicas/2026-08-24_public_maxproc_run07_ES_EN.md` was changed.

The next step no longer exists as a shared paragraph after EN; it is now represented symmetrically inside both language halves as `### Paso siguiente` and `### Next step`. No manifesto, Neoaxiom™, Issue, Synthesis content, genealogy or canon rule was changed.

**Commit:** `318ab287bb2703aee7512e61ff7ef19207408eae`.

### Tests and result

A post-read of Run 07 confirms five `###` headings in ES and five equivalent headings in EN, with the continuation block inside each half and no shared paragraph after the English block.

**Target result:** `PASS` for the local structural repair of Run 07.

No global PASS is declared: the versioned audit still contains two failures until it regenerates, and Run 06 remains a known residue. The new selector gate also has no recoverable CI status yet, while material language-navigation failures are independently verified.

### Residues

- `Run 06` remains listed by the global audit as a structural failure until repair/re-audit.
- LXXVIII–LXXXI lack the initial ES/EN selector in the verified live routes and in their canonical mirrors.
- `LANGUAGE_SELECTOR_GATE` must be treated as `NOT_VERIFIED / MATERIAL_FAILURES_CONFIRMED`, never PASS because status is absent.
- PR #165 and #167 remain open as historical maintenance and are outside this repair.

### Next step

Repair LXXVIII as the first case of the language-navigation regression by adding the visible selector `[ES · Castellano](#es--castellano) · [EN · English](#en--english)` to both its live route and canonical mirror without changing substantive content, then verify the selector gate before moving to LXXIX.
