# MAXPROC público · Run31 · Retirada de one-shot LXXVII obsoleto / Public MAXPROC · Run31 · Retiring stale LXXVII one-shot

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Fecha / Date:** 2026-08-25  
**Estado / Status:** `CORRECCIÓN MATERIAL VERIFICADA / MATERIAL FIX VERIFIED`  
**Frontera / Boundary:** `7.3-CANDIDATE / NOT_CANON`

---

# ES · Castellano

## 1. Estado vivo revisado

Antes de modificar se revisaron el head vivo, la auditoría global de simetría ES/EN y el postcheck de README, índices y enlaces. El estado vigente mantenía:

- `CONTENT_SYMMETRY = PASS`: **345** Markdown activos de alcance bilingüe, **279** documentos ES/EN divididos y **0** fallos estructurales o de marcadores;
- `LINK_INTEGRITY = PASS_DOCUMENTARY`: **434** Markdown activos del grafo vivo, **10.796** rutas internas comprobadas, **0** rotas y **0** fallos canónicos críticos;
- frontera explícita `7.3-CANDIDATE / NOT_CANON`.

La traza inmediatamente anterior dejó como único siguiente paso auditar el siguiente `oneshot-*` aún capaz de escribir superficies canónicas o de Síntesis.

## 2. Primer fallo real prioritario

Se comprobó que `.github/workflows/oneshot-sync-lxxvii-relations.yml` seguía presente y era todavía ejecutable mediante `workflow_dispatch`.

El workflow tenía `permissions: contents: write`, ejecutaba una cadena amplia de sincronizadores de frontera, canon, Neoaxiomas, Síntesis, navegación y relaciones y terminaba con:

```text
git add -A
→ git commit
→ git pull --rebase origin main
→ git push origin main
```

Además, su semántica estaba fijada expresamente a la antigua frontera **LXXVII / C-NAX-25** y su propio gate de salud emitía `LXXVII_DOCUMENTARY_GRAPH=OK`. No contenía un gate explícito `CANONICAL_STATE=7.3-CANDIDATE/NOT_CANON` antes de escribir.

Por tanto constituía una ruta residual real de escritura: una ejecución manual podía recalcular y empujar superficies vivas usando una frontera histórica y sin atravesar la protección de estado canónico vigente.

## 3. Corrección aplicada

Se retiró exclusivamente el workflow obsoleto:

`.github/workflows/oneshot-sync-lxxvii-relations.yml`

**Commit material:** `bd3c5f65a72ab4ddb47a0defeca9df257fca98b4`.

No se modificaron manifiestos, Neoaxiomas, contenido de Síntesis, genealogía, WEB4 ni la frontera canónica.

## 4. Gates y restricciones preservadas

La corrección no rebaja ningún gate y mantiene expresamente:

- bilingüismo ES/EN sin compresión;
- enlaces y genealogía intactos;
- `7.3-CANDIDATE = NOT_CANON`;
- ninguna promoción de 7.3;
- ninguna reescritura sustantiva del corpus.

## 5. Verificación

La ruta residual elegida queda eliminada de `main`; el cambio material se limita a retirar ese workflow histórico. Las auditorías vigentes anteriores a la corrección estaban limpias y esta traza se añade en ES/EN simétrico para preservar la genealogía de la decisión.

No se anticipa como PASS ningún workflow remoto posterior que aún no haya finalizado: cualquier ejecución automática posterior debe considerarse evidencia independiente.

**Resultado de la iteración:** `PASS` para el único defecto material seleccionado.

## 6. Único siguiente paso

Auditar el siguiente workflow `oneshot-*` que conserve `contents: write` y capacidad real de modificar superficies vivas; retirar únicamente el primero que se demuestre todavía ejecutable, obsoleto y no protegido por el gate vigente de `7.3-CANDIDATE`.

---

# EN · English

## 1. Living state reviewed

Before modifying anything, the living head, the global ES/EN symmetry audit and the README/index/link postcheck were reviewed. The current state retained:

- `CONTENT_SYMMETRY = PASS`: **345** active Markdown files in bilingual scope, **279** split ES/EN documents and **0** structural or marker failures;
- `LINK_INTEGRITY = PASS_DOCUMENTARY`: **434** active Markdown files in the living graph, **10,796** internal paths checked, **0** broken and **0** critical canonical failures;
- explicit `7.3-CANDIDATE / NOT_CANON` boundary.

The immediately previous trace left one next step: audit the next remaining `oneshot-*` still capable of writing canonical or Open Synthesis surfaces.

## 2. First real priority defect

`.github/workflows/oneshot-sync-lxxvii-relations.yml` was confirmed still present and executable through `workflow_dispatch`.

The workflow had `permissions: contents: write`, ran a broad chain of frontier, canonical, Neoaxiom, Synthesis, navigation and relation synchronisers, and ended with:

```text
git add -A
→ git commit
→ git pull --rebase origin main
→ git push origin main
```

Its semantics were also explicitly fixed to the old **LXXVII / C-NAX-25** frontier, while its own health gate emitted `LXXVII_DOCUMENTARY_GRAPH=OK`. It contained no explicit `CANONICAL_STATE=7.3-CANDIDATE/NOT_CANON` gate before writing.

It therefore formed a real residual write path: a manual execution could recalculate and push living surfaces using a historical frontier without passing through the current canonical-state protection.

## 3. Applied correction

Only the obsolete workflow was removed:

`.github/workflows/oneshot-sync-lxxvii-relations.yml`

**Material commit:** `bd3c5f65a72ab4ddb47a0defeca9df257fca98b4`.

No manifestos, Neoaxioms, Open Synthesis content, genealogy, WEB4 or canonical boundary were modified.

## 4. Preserved gates and constraints

The correction lowers no gate and explicitly preserves:

- uncompressed ES/EN bilingual symmetry;
- links and genealogy intact;
- `7.3-CANDIDATE = NOT_CANON`;
- no 7.3 promotion;
- no substantive corpus rewrite.

## 5. Verification

The selected residual write path is removed from `main`; the material change is limited to retiring that historical workflow. The audits current before the correction were clean, and this trace is added with symmetric ES/EN structure to preserve the genealogy of the decision.

No later remote workflow is pre-declared as PASS before completion: any automatic execution after this change must be treated as independent evidence.

**Iteration result:** `PASS` for the single selected material defect.

## 6. Single next step

Audit the next `oneshot-*` workflow that retains `contents: write` and real ability to modify living surfaces; retire only the first one demonstrated to remain executable, obsolete and unprotected by the current `7.3-CANDIDATE` gate.
