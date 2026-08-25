# MAXPROC público · Run29 / Public MAXPROC · Run29

**Fecha / Date:** 2026-08-25  
**Estado observado / Observed state:** `7.3-CANDIDATE / NOT_CANON`.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado inicial demostrado

- `CONTENT_SYMMETRY`: PASS en la auditoría pública vigente.
- `LANGUAGE_NAVIGATION`: PASS en la auditoría pública vigente.
- `LINK_INTEGRITY`: PASS en el postcheck vigente, con 0 enlaces internos rotos.
- `RELATIONAL_NAVIGATION`: PASS documental vigente, con cobertura completa del mapa curado.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## Primer fallo real prioritario

El workflow `.github/workflows/sync-open-synthesis-network.yml` sincronizaba la superficie `7.3-CANDIDATE` y bloqueaba fallos de registro, Neoaxiomas, enlaces, paridad, estructura y relaciones, pero **no tenía un gate explícito de `CANONICAL_STATE`**. Además, un cambio directo en `README.md` no estaba incluido entre sus `push.paths`. Por tanto, una modificación accidental de la cabecera viva podía presentar `7.3` como canónico sin que este workflow se ejecutara para restaurar/verificar la frontera candidata.

## Acción

Se modificó exclusivamente el workflow de sincronización para:

1. añadir `README.md` a `push.paths`;
2. añadir un gate bloqueante de `CANONICAL_STATE` que exige que la primera línea viva conserve `NEOCore™ 7.3-CANDIDATE`;
3. abortar si la cabecera presenta `NEOCore™ 7.3 ·` o una forma `7.3 CANON`;
4. exigir que el índice completo de Síntesis conserve tanto `7.3-CANDIDATE` como la regla bilingüe que condiciona cualquier promoción a completar cobertura, clasificación de fuentes/evidencia, simetría, Neoaxiomas y auditoría relacional final;
5. emitir `CANONICAL_STATE=7.3-CANDIDATE/NOT_CANON` sólo después de superar esas comprobaciones.

**Commit material:** `83da1fe8ef95a0650f1374e41cad90038a2e8582`.

No se modificó contenido sustantivo del marco, manifiestos, Neoaxiomas, genealogía ni WEB4; tampoco se promovió `7.3-CANDIDATE`.

## Verificación

La superficie raíz vigente continúa titulada `NEOCore™ 7.3-CANDIDATE`. El índice completo de Síntesis mantiene explícitamente `7.3-CANDIDATE` y la regla bilingüe de promoción condicionada. El workflow actualizado conserva todos los gates anteriores y añade el nuevo gate sin rebajar ninguno.

El estado combinado del commit no expone estados CI clásicos en la API consultada; por ello esta iteración **no inventa un PASS de ejecución remota**. La verificación demostrada es estructural sobre el workflow escrito y sobre las dos superficies que el nuevo gate comprueba.

**Resultado de la iteración:** **PASS para el delta elegido**: la frontera candidata dispone ya de un gate automático explícito en el sincronizador principal y `README.md` queda dentro de su cobertura de trigger.

## PASO_SIGUIENTE

Auditar si existe alguna otra automatización pública con capacidad de reescribir `README.md`, el índice de Síntesis o las superficies WEB4 de versión sin pasar por este gate de `CANONICAL_STATE`; corregir únicamente la primera ruta de escritura no protegida que se demuestre.

---

# EN · English

## Demonstrated initial state

- `CONTENT_SYMMETRY`: PASS in the current public audit.
- `LANGUAGE_NAVIGATION`: PASS in the current public audit.
- `LINK_INTEGRITY`: PASS in the current postcheck, with 0 broken internal links.
- `RELATIONAL_NAVIGATION`: current documentary PASS, with complete curated-map coverage.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## First real priority failure

The `.github/workflows/sync-open-synthesis-network.yml` workflow synchronized the `7.3-CANDIDATE` surface and blocked registry, Neoaxiom, link, parity, structure and relational failures, but **did not contain an explicit `CANONICAL_STATE` gate**. In addition, a direct change to `README.md` was not included in its `push.paths`. An accidental edit to the living header could therefore present `7.3` as canonical without this workflow running to restore/verify the candidate boundary.

## Action

Only the synchronization workflow was modified to:

1. add `README.md` to `push.paths`;
2. add a blocking `CANONICAL_STATE` gate requiring the living first line to retain `NEOCore™ 7.3-CANDIDATE`;
3. abort if the header presents `NEOCore™ 7.3 ·` or a `7.3 CANON` form;
4. require the complete Open Synthesis index to preserve both `7.3-CANDIDATE` and the bilingual rule conditioning any promotion on completed coverage, source/evidence classification, symmetry, Neoaxioms and final relational audit;
5. emit `CANONICAL_STATE=7.3-CANDIDATE/NOT_CANON` only after those checks succeed.

**Material commit:** `83da1fe8ef95a0650f1374e41cad90038a2e8582`.

No substantive framework content, manifestos, Neoaxioms, genealogy or WEB4 were modified; `7.3-CANDIDATE` was not promoted.

## Verification

The current root surface remains titled `NEOCore™ 7.3-CANDIDATE`. The complete Open Synthesis index explicitly retains `7.3-CANDIDATE` and the bilingual conditional-promotion rule. The updated workflow preserves every previous gate and adds the new one without weakening any of them.

The commit combined-status endpoint exposes no classic CI statuses for this commit; this iteration therefore **does not invent a remote execution PASS**. The demonstrated verification is structural, covering the written workflow and the two surfaces checked by the new gate.

**Iteration result:** **PASS for the selected delta**: the candidate boundary now has an explicit automatic gate in the main synchronizer, and `README.md` is covered by its trigger.

## NEXT_STEP

Audit whether any other public automation can rewrite `README.md`, the Open Synthesis index or WEB4 version surfaces without passing through this `CANONICAL_STATE` gate; fix only the first demonstrated unprotected write path.