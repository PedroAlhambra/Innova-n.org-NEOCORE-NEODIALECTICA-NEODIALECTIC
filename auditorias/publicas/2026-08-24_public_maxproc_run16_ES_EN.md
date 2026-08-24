# MAXPROC público · Run 16 · preservar evidencia antes de bloquear el gate
# Public MAXPROC · Run 16 · preserve evidence before blocking the gate

**Fecha / Date:** 2026-08-24 16:42 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** corrección del flujo global para que un `FAIL` de simetría o navegación no impida versionar el propio informe que demuestra el fallo / correction of the global workflow so that a symmetry or navigation `FAIL` cannot prevent versioning the report that proves the failure  
**Commit material / Material commit:** `f790f30485222bc083d746177c132101b385cac7`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md` y la nota MAXPROC inmediatamente anterior.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La capa neoaxiomática mantiene candidatos `C-NAX-15–26` explícitamente separados del canon. WEB4™ pública sigue declarada como especificación documental, no como implementación final.

La auditoría global de simetría ES/EN versionada permanece limpia en sus dimensiones estructurales conocidas, pero la auditoría versionada específica de selectores `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md` todavía no existe en `main`. Por tanto no se declara `LANGUAGE_NAVIGATION = PASS`.

Las PR públicas abiertas detectadas siguen siendo #165 y #167, ambas ramas temporales/antiguas de mantenimiento. No se han utilizado, fusionado ni modificado en esta iteración.

## Problema elegido

El workflow global ya ejecutaba `audit_language_selectors.py`, pero tenía un defecto de observabilidad bloqueante:

```text
AUDITOR GENERA INFORME
→ DETECTA FALLO
→ sys.exit(1)
→ GITHUB DETIENE EL JOB
→ EL PASO "COMMIT AUDIT REPORTS" NO SE EJECUTA
→ EL INFORME DE FAIL NO QUEDA VERSIONADO
```

Esto hacía que un fallo real del selector pudiera producir exactamente la ausencia de informe que se estaba intentando resolver. La falta de artefacto no permitía distinguir de forma trazable entre `PASS`, `FAIL` y ejecución no recuperable.

## Acción

Se modificó exclusivamente `.github/workflows/audit-global-bilingual-symmetry.yml` para preservar primero la evidencia y aplicar después el bloqueo:

1. `CONTENT_SYMMETRY` y `LANGUAGE_NAVIGATION` ejecutan con `continue-on-error: true` y conservan su `outcome` real.
2. El paso de versionado usa `if: always()` y conserva los informes producidos incluso cuando un auditor devuelve código no cero.
3. Un paso final `Enforce blocking audit result` inspecciona ambos outcomes.
4. Si cualquiera no es `success`, el workflow termina con código 1 después de preservar la evidencia.
5. Sólo si ambos son `success` puede imprimir los dos PASS.

La regla no se ha rebajado: **el cambio hace más observable el FAIL, no más fácil el PASS**.

## Pruebas y resultado

La lectura posterior de `main` confirma que el workflow conserva `contents: write`, ejecuta ambos auditores, versiona con `if: always()` y vuelve a fallar al final si cualquiera de los dos gates falla.

Commit material:

`f790f30485222bc083d746177c132101b385cac7`

**Resultado del objetivo local:** `PASS` — la evidencia de un fallo ya no queda estructuralmente bloqueada por el propio fallo.

No se declara todavía resultado global de navegación porque el nuevo informe versionado aún no estaba presente en la lectura inmediatamente posterior al commit.

## Estado de gates

```text
CONTENT_SYMMETRY      = PASS VERSIONADO EN LA ÚLTIMA AUDITORÍA DISPONIBLE
LANGUAGE_NAVIGATION   = NOT_VERIFIED · INFORME GLOBAL AÚN NO VERSIONADO
LINK_INTEGRITY        = NO NUEVA REGRESIÓN DEMOSTRADA EN ESTA ITERACIÓN
RELATIONAL_NAVIGATION = NO NUEVA REGRESIÓN DEMOSTRADA EN ESTA ITERACIÓN
CANONICAL_STATE       = 7.3-CANDIDATE / NOT_CANON
```

No se interpreta `NO NUEVA REGRESIÓN DEMOSTRADA` como PASS fresco de enlaces o relaciones.

## Residuos

- Falta comprobar el primer informe global de selectores que produzca el workflow corregido.
- `7.3-CANDIDATE` permanece no canónica.
- Las PR #165 y #167 permanecen abiertas y no fusionadas.

## Paso siguiente

Verificar **exclusivamente** `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md` cuando quede versionada por el workflow corregido: si registra cero fallos, fijar `LANGUAGE_NAVIGATION = PASS`; si registra fallos, reparar únicamente el primer `LANGUAGE_NAVIGATION_FAILURE` o `LANGUAGE_ANCHOR_FAILURE` listado sin rebajar el gate.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md` and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open and non-canonical. The manifesto index remains **I–LXXXI + ∞**. The Neoaxiomatic layer keeps candidates `C-NAX-15–26` explicitly separate from canon. Public WEB4™ remains a documentary specification rather than a final implementation.

The versioned global ES/EN symmetry audit remains clean across its known structural dimensions, but the dedicated versioned selector audit `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md` still does not exist on `main`. Therefore `LANGUAGE_NAVIGATION = PASS` is not declared.

The detected open public PRs remain #165 and #167, both temporary/old maintenance branches. Neither was used, merged or modified in this iteration.

## Selected problem

The global workflow already executed `audit_language_selectors.py`, but retained a blocking observability defect:

```text
AUDITOR GENERATES REPORT
→ DETECTS FAILURE
→ sys.exit(1)
→ GITHUB STOPS THE JOB
→ "COMMIT AUDIT REPORTS" DOES NOT RUN
→ THE FAIL REPORT IS NOT VERSIONED
```

A real selector failure could therefore produce exactly the missing report that the process was trying to resolve. The absence of the artifact could not traceably distinguish `PASS`, `FAIL` and an unrecoverable execution.

## Action

Only `.github/workflows/audit-global-bilingual-symmetry.yml` was modified so that evidence is preserved before enforcement:

1. `CONTENT_SYMMETRY` and `LANGUAGE_NAVIGATION` run with `continue-on-error: true` while retaining their real `outcome`.
2. The versioning step uses `if: always()` and preserves produced reports even when an auditor returns a non-zero exit code.
3. A final `Enforce blocking audit result` step inspects both outcomes.
4. If either outcome is not `success`, the workflow exits with code 1 after evidence has been preserved.
5. Only when both are `success` may it print both PASS states.

The rule was not weakened: **the change makes FAIL more observable, not PASS easier**.

## Tests and result

Post-change inspection on `main` confirms that the workflow retains `contents: write`, executes both auditors, versions reports with `if: always()` and fails at the end if either gate fails.

Material commit:

`f790f30485222bc083d746177c132101b385cac7`

**Local target result:** `PASS` — failure evidence can no longer be structurally blocked by the failure itself.

No global language-navigation result is declared yet because the new versioned report was still absent in the immediate post-commit read.

## Gate state

```text
CONTENT_SYMMETRY      = PASS VERSIONED IN THE LATEST AVAILABLE AUDIT
LANGUAGE_NAVIGATION   = NOT_VERIFIED · GLOBAL REPORT NOT YET VERSIONED
LINK_INTEGRITY        = NO NEW REGRESSION DEMONSTRATED IN THIS ITERATION
RELATIONAL_NAVIGATION = NO NEW REGRESSION DEMONSTRATED IN THIS ITERATION
CANONICAL_STATE       = 7.3-CANDIDATE / NOT_CANON
```

`NO NEW REGRESSION DEMONSTRATED` is not treated as a fresh PASS for links or relations.

## Residues

- The first global selector report produced by the corrected workflow still needs to be checked.
- `7.3-CANDIDATE` remains non-canonical.
- PRs #165 and #167 remain open and unmerged.

## Next step

Verify **only** `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md` once it is versioned by the corrected workflow: if it records zero failures, set `LANGUAGE_NAVIGATION = PASS`; if it records failures, repair only the first listed `LANGUAGE_NAVIGATION_FAILURE` or `LANGUAGE_ANCHOR_FAILURE` without weakening the gate.
