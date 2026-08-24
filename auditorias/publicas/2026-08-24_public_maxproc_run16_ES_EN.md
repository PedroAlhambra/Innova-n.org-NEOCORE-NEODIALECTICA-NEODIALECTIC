# MAXPROC público · Run 16 · preservar evidencia antes de bloquear el gate
# Public MAXPROC · Run 16 · preserve evidence before blocking the gate

**Fecha / Date:** 2026-08-24 16:42 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** corrección del flujo global para que un `FAIL` de simetría o navegación no impida versionar el propio informe que demuestra el fallo / correction of the global workflow so that a symmetry or navigation `FAIL` cannot prevent versioning the report that proves the failure  
**Commit material / Material commit:** `f790f30485222bc083d746177c132101b385cac7`  
**Commits automáticos de auditoría observados / Observed automated audit commits:** `07fa49eafa487c00699464c9b08c6442503346ef` · `06349a3ba0ee53ab91590efecb2fdf1220070575`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md` y la nota MAXPROC inmediatamente anterior.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La capa neoaxiomática mantiene candidatos `C-NAX-15–26` explícitamente separados del canon. WEB4™ pública sigue declarada como especificación documental, no como implementación final.

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

El cambio funcionó: el workflow produjo y versionó finalmente:

`auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md`

La auditoría demuestra:

- páginas ES/EN explícitas auditadas: **345**;
- fallos de navegación lingüística: **125**;
- `LANGUAGE_SELECTOR_GATE = FAIL`.

El primer fallo listado es:

`analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md` · `LANGUAGE_NAVIGATION_FAILURE` · faltan selector ES y selector EN.

**Resultado del objetivo local:** `PASS` — la evidencia de un fallo ya no queda estructuralmente bloqueada por el propio fallo.

**Resultado global de navegación:** `FAIL` — demostrado por auditoría versionada; no se infiere ni se declara PASS.

## Estado de gates

```text
CONTENT_SYMMETRY      = PASS EN LA ÚLTIMA AUDITORÍA ESTRUCTURAL DISPONIBLE
LANGUAGE_NAVIGATION   = FAIL · 125/345 SUPERFICIES
LINK_INTEGRITY        = NO NUEVA REGRESIÓN DEMOSTRADA EN ESTA ITERACIÓN
RELATIONAL_NAVIGATION = NO NUEVA REGRESIÓN DEMOSTRADA EN ESTA ITERACIÓN
CANONICAL_STATE       = 7.3-CANDIDATE / NOT_CANON
```

No se interpreta `NO NUEVA REGRESIÓN DEMOSTRADA` como PASS fresco de enlaces o relaciones.

## Residuos

- Quedan **125 fallos** de navegación lingüística registrados por el gate global.
- La reparación conocida LXXVIII–LXXXI no era el conjunto completo; la auditoría global confirma deuda distribuida por análisis, auditorías, anuncios, manifiestos y otras superficies vivas.
- `7.3-CANDIDATE` permanece no canónica.
- Las PR #165 y #167 permanecen abiertas y no fusionadas.

## Paso siguiente

Reparar **exclusivamente** `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md`, primer `LANGUAGE_NAVIGATION_FAILURE` listado por la auditoría global, añadiendo selector visible ES/EN con anchors reales sin modificar su contenido sustantivo; después volver a ejecutar el gate sin rebajar sus reglas.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md` and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open and non-canonical. The manifesto index remains **I–LXXXI + ∞**. The Neoaxiomatic layer keeps candidates `C-NAX-15–26` explicitly separate from canon. Public WEB4™ remains a documentary specification rather than a final implementation.

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

The change worked: the workflow finally produced and versioned:

`auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md`

The audit demonstrates:

- explicit ES/EN pages audited: **345**;
- language-navigation failures: **125**;
- `LANGUAGE_SELECTOR_GATE = FAIL`.

The first listed failure is:

`analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md` · `LANGUAGE_NAVIGATION_FAILURE` · both ES and EN selectors are missing.

**Local target result:** `PASS` — failure evidence can no longer be structurally blocked by the failure itself.

**Global navigation result:** `FAIL` — demonstrated by a versioned audit; PASS is neither inferred nor declared.

## Gate state

```text
CONTENT_SYMMETRY      = PASS IN THE LATEST AVAILABLE STRUCTURAL AUDIT
LANGUAGE_NAVIGATION   = FAIL · 125/345 SURFACES
LINK_INTEGRITY        = NO NEW REGRESSION DEMONSTRATED IN THIS ITERATION
RELATIONAL_NAVIGATION = NO NEW REGRESSION DEMONSTRATED IN THIS ITERATION
CANONICAL_STATE       = 7.3-CANDIDATE / NOT_CANON
```

`NO NEW REGRESSION DEMONSTRATED` is not treated as a fresh PASS for links or relations.

## Residues

- **125 language-navigation failures** remain registered by the global gate.
- The known LXXVIII–LXXXI repair was not the complete set; the global audit demonstrates distributed debt across analyses, audits, announcements, manifestos and other live surfaces.
- `7.3-CANDIDATE` remains non-canonical.
- PRs #165 and #167 remain open and unmerged.

## Next step

Repair **only** `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md`, the first `LANGUAGE_NAVIGATION_FAILURE` listed by the global audit, by adding a visible ES/EN selector with real anchors without changing substantive content; then rerun the gate without weakening its rules.
