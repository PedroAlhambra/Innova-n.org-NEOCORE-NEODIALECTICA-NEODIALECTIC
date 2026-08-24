# MAXPROC público · Run 22 · reparación de navegación lingüística en análisis religión–identidad
# Public MAXPROC · Run 22 · religion–identity analysis language-navigation repair

**Fecha / Date:** 2026-08-24 22:40 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración de navegación ES/EN bidireccional en `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md` / restoration of bidirectional ES/EN navigation in `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md`  
**Commit material / Material commit:** `bc5f30ee96b887f382c322b9eba8e2791b774da8`  
**Mecanismo temporal eliminado / Temporary mechanism removed:** `d3fb94574a8021c4e7fe92814b7af049f32cb2b0`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global de simetría ES/EN, la auditoría global de selectores y la nota MAXPROC inmediatamente anterior.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa y no canónica. `manifiestos/README.md` mantiene **I–LXXXI + ∞**; la capa neoaxiomática conserva candidatos explícitos separados del canon; Síntesis Abierta mantiene `ABIERTO A SÍNTESIS ≠ VALIDADO`; WEB4™ continúa definida como especificación documental pública y no como implementación final. La Issue #161 permanece abierta como `CANDIDATE · OPEN SYNTHESIS` y su gate sigue impidiendo promoción automática a 7.3 canónica. Las PR públicas #165 y #167 continúan abiertas, no fusionadas y no mergeables.

Antes del delta, la auditoría global de navegación lingüística registraba **352 superficies ES/EN explícitas** y **120 fallos**, siendo el primero `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md`.

La auditoría estructural global vigente permanece limpia: **334 Markdown activos**, **268 documentos ES/EN divididos**, **0 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**.

## Problema elegido

El análisis de religión e identidad contenía `## ES` y `## EN` y además una navegación parcial hacia inglés y retorno desde inglés, pero la cabecera sólo ofrecía un enlace unilateral a `#en`. El auditor global lo clasificaba correctamente como `LANGUAGE_NAVIGATION_FAILURE` por ausencia de selector ES y EN válido en la zona inicial.

## Acción

Se sustituyó exclusivamente la navegación unilateral de cabecera por:

`[ES](#es) · [EN](#en)`

Los destinos corresponden exactamente a los encabezados reales `## ES` y `## EN`. No se modificaron tesis, fuentes, cronología, genealogía, relaciones, referencias ni contenido sustantivo.

Para aplicar el delta sin reescribir manualmente un documento extenso se utilizó un workflow temporal de reparación literal. El workflow fue eliminado después de confirmar el commit material; no queda superficie operativa temporal residual en `.github/workflows/`.

## Pruebas y resultado

La lectura posterior del archivo confirma:

1. selector visible antes del cuerpo ES;
2. destino ES `#es` con encabezado real `## ES`;
3. destino EN `#en` con encabezado real `## EN`;
4. preservación del cuerpo completo y de la navegación de retorno existente desde EN.

El auditor global de selectores fue ejecutado dentro del delta y dejó una auditoría versionada posterior con:

- superficies ES/EN explícitas auditadas: **352**;
- fallos: **119**;
- `LANGUAGE_SELECTOR_GATE = FAIL` global;
- descenso demostrado: **120 → 119**;
- el archivo reparado ya no aparece en el inventario de fallos.

**Resultado del objetivo local:** `PASS`.

No se declara PASS global porque permanecen **119 fallos de navegación lingüística**.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` · 0 fallos estructurales/markers/pareados/Issue templates en la auditoría vigente.
- `LANGUAGE_NAVIGATION = FAIL` · 119 fallos sobre 352 superficies auditadas.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`; no se modificaron rutas y los anchors añadidos fueron verificados estructuralmente.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`; no se modificaron relaciones ni referencias cruzadas.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

El primer fallo restante de la auditoría versionada es:

`analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md`

con ausencia de selector ES y EN.

## Paso siguiente

Reparar exclusivamente `analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md`, añadiendo un selector visible cuyos destinos coincidan con sus encabezados ES/EN reales, sin alterar contenido sustantivo, y volver a verificar que el gate global reduce el contador de fallos.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the global ES/EN structural audit, the global language-selector audit and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active and non-canonical. `manifiestos/README.md` retains **I–LXXXI + ∞**; the Neoaxiomatic layer keeps explicit candidates separate from canon; Open Synthesis preserves `OPEN TO SYNTHESIS ≠ VALIDATED`; WEB4™ remains a public documentary specification rather than a final implementation. Issue #161 remains open as `CANDIDATE · OPEN SYNTHESIS`, and its gate still prevents automatic promotion to canonical 7.3. Public PRs #165 and #167 remain open, unmerged and non-mergeable.

Before the delta, the global language-navigation audit reported **352 explicit ES/EN surfaces** and **120 failures**, with `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md` first in the list.

The current global structural audit remains clean: **334 active Markdown files**, **268 split ES/EN documents**, **0 structural failures**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**.

## Selected problem

The religion-and-identity analysis contained `## ES` and `## EN` and also partial navigation to English plus a return link from English, but its header offered only a one-way link to `#en`. The global auditor therefore correctly classified it as `LANGUAGE_NAVIGATION_FAILURE` because a valid ES and EN selector was absent from the initial navigation zone.

## Action

Only the one-way header navigation was replaced with:

`[ES](#es) · [EN](#en)`

The targets exactly match the real `## ES` and `## EN` headings. No thesis, sources, chronology, genealogy, relationships, references or substantive content were changed.

A temporary literal-repair workflow was used to apply the delta without manually rewriting a long document. The workflow was removed after the material commit was confirmed; no temporary operational surface remains under `.github/workflows/`.

## Tests and result

Post-read verification confirms:

1. a visible selector before the ES body;
2. ES target `#es` with actual `## ES` heading;
3. EN target `#en` with actual `## EN` heading;
4. preservation of the full body and of the existing return navigation from EN.

The global selector auditor ran within the delta and left a subsequent versioned audit reporting:

- explicit ES/EN surfaces audited: **352**;
- failures: **119**;
- global `LANGUAGE_SELECTOR_GATE = FAIL`;
- demonstrated decrease: **120 → 119**;
- the repaired file no longer appears in the failure inventory.

**Local target result:** `PASS`.

No global PASS is declared because **119 language-navigation failures** remain.

## Gate state

- `CONTENT_SYMMETRY = PASS` · 0 structural/marker/paired/Issue-template failures in the current audit.
- `LANGUAGE_NAVIGATION = FAIL` · 119 failures across 352 audited surfaces.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`; no routes were changed and the new anchors were structurally verified.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`; no relationships or cross-references were modified.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

The first remaining failure in the versioned audit is:

`analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md`

with both ES and EN selectors missing.

## Next step

The single next action is the bilingual `PASO_SIGUIENTE / NEXT_STEP` stated above; no second next step is opened in this run.
