# MAXPROC público · Run 19 · reparación de navegación lingüística en análisis LinkedIn
# Public MAXPROC · Run 19 · LinkedIn analysis language-navigation repair

**Fecha / Date:** 2026-08-24 19:40 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md` / restoration of the ES/EN selector in `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md`  
**Commit material / Material commit:** `e9e18114f0747af8c184d980ef2117ba581ca34f`  
**Commit automático de auditoría / Automatic audit commit:** `fe67cab030a6ae2664642e178295285f1877fdbe`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies obligatorias del corpus público: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN vigente, la auditoría global de selectores y la nota MAXPROC inmediatamente anterior.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta a Síntesis y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La Issue #161 permanece abierta como `CANDIDATE · OPEN SYNTHESIS` y conserva el gate que impide promoción automática. Las PR públicas #165 y #167 continúan `OPEN / NOT_MERGED / NOT_MERGEABLE` y no se utilizaron en esta iteración.

Antes del delta, la auditoría global de navegación lingüística versionada informaba **349 páginas ES/EN explícitas auditadas** y **123 fallos**. El primer residuo listado era `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md`, con ausencia de ambos selectores.

La auditoría estructural global vigente permanece limpia: **331 Markdown activos**, **265 documentos ES/EN divididos**, **0 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**.

## Problema elegido

El análisis de LinkedIn contenía capas completas `## ES` y `## EN`, pero no ofrecía navegación directa entre ellas. Conforme a la regla bloqueante:

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector visible:

`[ES](#es) · [EN](#en)`

antes de `## ES`. Se utilizaron estos destinos porque los encabezados reales del documento son precisamente `## ES` y `## EN`, cuyos anchors GitHub son `#es` y `#en`.

No se modificaron tesis, cronología, formulaciones, fuentes, enlaces relacionales, genealogía ni contenido sustantivo del análisis.

## Pruebas y resultado

La lectura posterior confirma selector visible antes del cuerpo español y presencia real de ambos encabezados destino.

El workflow global se ejecutó después del commit material y regeneró las auditorías en `fe67cab030a6ae2664642e178295285f1877fdbe`.

La auditoría de selectores posterior demuestra:

- páginas ES/EN explícitas auditadas: **349**;
- fallos: **122**;
- `LANGUAGE_SELECTOR_GATE = FAIL` global;
- descenso demostrado: **123 → 122**.

**Resultado del objetivo local:** `PASS`.

No se declara PASS global porque permanecen **122 fallos de navegación lingüística**.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` · 0 fallos estructurales/markers/pareados/Issue templates.
- `LANGUAGE_NAVIGATION = FAIL` · 122 fallos sobre 349 superficies auditadas en la auditoría inmediatamente posterior al delta.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

El primer fallo que queda listado después de esta reparación es:

`analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`

con ausencia de selector ES y EN.

## PASO_SIGUIENTE

Reparar **exclusivamente** `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`, añadiendo un selector visible cuyos destinos coincidan con sus encabezados ES/EN reales, sin alterar contenido sustantivo, y volver a verificar que el gate global reduce el contador de fallos.

---

# EN · English

## Observed state

The required public corpus surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the current global ES/EN audit, the global language-selector audit and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open to Synthesis and non-canonical. The manifesto index remains **I–LXXXI + ∞**. Issue #161 remains open as `CANDIDATE · OPEN SYNTHESIS` and preserves the gate preventing automatic promotion. Public PRs #165 and #167 remain `OPEN / NOT_MERGED / NOT_MERGEABLE` and were not used in this iteration.

Before the delta, the versioned global language-navigation audit reported **349 explicit ES/EN pages audited** and **123 failures**. The first listed residue was `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md`, missing both language selectors.

The current global structural audit remains clean: **331 active Markdown files**, **265 split ES/EN documents**, **0 structural failures**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**.

## Selected problem

The LinkedIn analysis contained complete `## ES` and `## EN` layers but offered no direct navigation between them. Under the blocking rule:

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the visible selector:

`[ES](#es) · [EN](#en)`

was added before `## ES`. These destinations were used because the document's real headings are exactly `## ES` and `## EN`, whose GitHub anchors are `#es` and `#en`.

No thesis, chronology, wording, sources, relational links, genealogy or substantive analysis content was changed.

## Tests and result

Post-read verification confirms a visible selector before the Spanish body and the actual presence of both destination headings.

The global workflow ran after the material commit and regenerated the audits in `fe67cab030a6ae2664642e178295285f1877fdbe`.

The subsequent selector audit demonstrates:

- explicit ES/EN pages audited: **349**;
- failures: **122**;
- global `LANGUAGE_SELECTOR_GATE = FAIL`;
- demonstrated decrease: **123 → 122**.

**Local target result:** `PASS`.

No global PASS is declared because **122 language-navigation failures** remain.

## Gate state

- `CONTENT_SYMMETRY = PASS` · 0 structural/marker/paired/Issue-template failures.
- `LANGUAGE_NAVIGATION = FAIL` · 122 failures across 349 surfaces in the audit immediately following the delta.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

The first failure remaining after this repair is:

`analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`

with both ES and EN selectors missing.

## NEXT_STEP

Repair **only** `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`, adding a visible selector whose targets match its real ES/EN headings without changing substantive content, then reverify that the global gate reduces the failure count.