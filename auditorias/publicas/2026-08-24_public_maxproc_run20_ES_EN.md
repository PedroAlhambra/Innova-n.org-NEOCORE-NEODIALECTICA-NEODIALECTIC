# MAXPROC público · Run 20 · reparación de navegación lingüística en análisis Anthropic
# Public MAXPROC · Run 20 · Anthropic analysis language-navigation repair

**Fecha / Date:** 2026-08-24 20:35 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md` / restoration of the ES/EN selector in `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`  
**Commit material / Material commit:** `ae229a47722601ba08d1a8643952a573cd0a314a`  
**Commit automático de auditoría / Automatic audit commit:** `76fb5a4b5736568e7b6c8f76895e3ff7ca8777e5`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN, la auditoría global de selectores y la nota MAXPROC inmediatamente anterior.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta a Síntesis y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La Issue #161 sigue abierta como `CANDIDATE · OPEN SYNTHESIS` y conserva un gate explícito de promoción. Las PR públicas #165 y #167 permanecen `OPEN / NOT_MERGED / NOT_MERGEABLE`; son ramas antiguas de mantenimiento y no se utilizaron en esta iteración.

Antes del delta, la auditoría versionada de navegación lingüística informaba **350 páginas ES/EN explícitas auditadas** y **122 fallos**. El primer residuo era `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`, sin selector ES ni EN.

La auditoría estructural global permanece limpia: **332 Markdown activos**, **266 documentos ES/EN divididos**, **0 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**.

## Problema elegido

El análisis Anthropic contenía capas completas `## ES` y `## EN`, pero carecía de navegación directa entre ellas.

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector visible:

`[ES](#es) · [EN](#en)`

antes de `## ES`. Estos destinos corresponden exactamente a los encabezados reales `## ES` y `## EN`, cuyos anchors GitHub son `#es` y `#en`.

No se modificaron tesis, cronología, fuentes, referencias externas, relaciones documentales, genealogía ni contenido sustantivo.

## Pruebas y resultado

La lectura posterior confirma el selector visible antes del cuerpo español y la presencia de ambos encabezados destino.

El workflow global se ejecutó después del commit material y regeneró las auditorías en `76fb5a4b5736568e7b6c8f76895e3ff7ca8777e5`.

La auditoría posterior demuestra:

- páginas ES/EN explícitas auditadas: **350**;
- fallos: **121**;
- `LANGUAGE_SELECTOR_GATE = FAIL` global;
- descenso demostrado: **122 → 121**.

**Resultado del objetivo local:** `PASS`.

No se declara PASS global porque permanecen **121 fallos de navegación lingüística**.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` · 0 fallos estructurales/markers/pareados/Issue templates.
- `LANGUAGE_NAVIGATION = FAIL` · 121 fallos sobre 350 superficies auditadas en la auditoría posterior al delta.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

El primer fallo restante es:

`analisis/publicos/2026-04-15_convergencia-neodialectica-openai-anthropic-instituciones-ia.md`

con ausencia de selector ES y EN.

## PASO_SIGUIENTE

Reparar **exclusivamente** `analisis/publicos/2026-04-15_convergencia-neodialectica-openai-anthropic-instituciones-ia.md`, añadiendo un selector visible cuyos destinos coincidan con sus encabezados ES/EN reales, sin alterar contenido sustantivo, y volver a verificar que el gate global reduce el contador de fallos.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the global ES/EN audit, the global language-selector audit and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open to Synthesis and non-canonical. The manifesto index remains **I–LXXXI + ∞**. Issue #161 remains open as `CANDIDATE · OPEN SYNTHESIS` with an explicit promotion gate. Public PRs #165 and #167 remain `OPEN / NOT_MERGED / NOT_MERGEABLE`; they are old maintenance branches and were not used in this iteration.

Before the delta, the versioned language-navigation audit reported **350 explicit ES/EN pages audited** and **122 failures**. The first residue was `analisis/publicos/2026-04-15_anthropic-gobernanza-ia-y-problema-del-marco.md`, missing both ES and EN selectors.

The global structural audit remains clean: **332 active Markdown files**, **266 split ES/EN documents**, **0 structural failures**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**.

## Selected problem

The Anthropic analysis contained complete `## ES` and `## EN` layers but lacked direct navigation between them.

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the visible selector:

`[ES](#es) · [EN](#en)`

was added before `## ES`. These destinations correspond exactly to the real `## ES` and `## EN` headings, whose GitHub anchors are `#es` and `#en`.

No thesis, chronology, sources, external references, documentary relationships, genealogy or substantive content was changed.

## Tests and result

Post-read verification confirms the visible selector before the Spanish body and the actual presence of both destination headings.

The global workflow ran after the material commit and regenerated the audits in `76fb5a4b5736568e7b6c8f76895e3ff7ca8777e5`.

The subsequent audit demonstrates:

- explicit ES/EN pages audited: **350**;
- failures: **121**;
- global `LANGUAGE_SELECTOR_GATE = FAIL`;
- demonstrated decrease: **122 → 121**.

**Local target result:** `PASS`.

No global PASS is declared because **121 language-navigation failures** remain.

## Gate state

- `CONTENT_SYMMETRY = PASS` · 0 structural/marker/paired/Issue-template failures.
- `LANGUAGE_NAVIGATION = FAIL` · 121 failures across 350 surfaces in the audit following the delta.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

The first remaining failure is:

`analisis/publicos/2026-04-15_convergencia-neodialectica-openai-anthropic-instituciones-ia.md`

with both ES and EN selectors missing.

## NEXT_STEP

Repair **only** `analisis/publicos/2026-04-15_convergencia-neodialectica-openai-anthropic-instituciones-ia.md`, adding a visible selector whose targets match its real ES/EN headings without changing substantive content, then reverify that the global gate reduces the failure count.