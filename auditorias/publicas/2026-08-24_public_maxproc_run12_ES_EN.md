# MAXPROC público · Run 12 · reparación de navegación lingüística LXXXI
# Public MAXPROC · Run 12 · LXXXI language-navigation repair

**Fecha / Date:** 2026-08-24 12:37 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en LXXXI, ruta viva + espejo canónico / restoration of the ES/EN selector in LXXXI, live route + canonical mirror  
**Commits de reparación / Repair commits:** `1570d859e52550e2802e4ae69556b5c41d5b3ccb` · `fc803c9c000432516a288aa41ce319c42cb7519b`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN vigente y la nota MAXPROC inmediatamente anterior.

La frontera pública sigue siendo **NEOCore™ 7.3-CANDIDATE**, abierta y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La capa neoaxiomática mantiene **NAX-01–NAX-14** como canon y **C-NAX-15–C-NAX-26** como candidatos abiertos a SAN™. La Issue pública #161 continúa abierta y declara expresamente `CANDIDATE · OPEN SYNTHESIS`; su gate prohíbe la promoción automática a 7.3 canónica.

La auditoría global ES/EN vigente observada antes de este delta informa **323 Markdown activos**, **257 documentos ES/EN divididos**, **1 fallo estructural**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. El único fallo estructural versionado continúa siendo `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`. Por tanto, no existe PASS global demostrable.

Las PR públicas #165 y #167 siguen `OPEN / NOT_MERGED / NOT_MERGEABLE`; ambas son ramas antiguas de mantenimiento y no se han utilizado ni modificado en esta iteración.

## Problema elegido

Run 11 dejó como único paso siguiente **LXXXI**. La ruta viva y el espejo canónico contenían ambas capas ES/EN completas, pero carecían del selector inicial visible.

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector visible:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

a:

- `manifiestos/81_ultralujo_bien_comun_elite_neodialectica_aporte_ES_EN.md`;
- `manifiestos/canonicos/LXXXI_ultralujo_bien_comun_elite_neodialectica_aporte_ES_EN.md`.

No se modificó contenido sustantivo, genealogía, referencias cruzadas, estado, Síntesis, Neoaxiomas™, Issues ni reglas de canon.

## Pruebas y resultado

La lectura posterior de ambas superficies confirma:

1. selector visible antes de `# ES · Castellano`;
2. enlaces a `#es--castellano` y `#en--english`;
3. presencia real posterior de ambos encabezados de idioma;
4. preservación del cuerpo y de la diferencia de ruta relativa esperada entre fuente viva (`../README.md`) y espejo canónico (`../../README.md`).

**Resultado del objetivo LXXXI:** `PASS`.

Las cuatro parejas conocidas afectadas por la regresión LXXVIII–LXXXI han sido reparadas en las iteraciones públicas 09–12. Esto cierra el **residuo conocido** de esa regresión, pero no se declara todavía `LANGUAGE_SELECTOR_GATE = PASS` global porque no existe una ejecución recuperable del nuevo workflow sobre el commit actual.

Tampoco se declara PASS global ES/EN: la auditoría versionada conserva **1 fallo estructural conocido, Run 06**.

## Residuos

- Simetría estructural global versionada: **1 fallo conocido**, Run 06.
- Navegación lingüística conocida LXXVIII–LXXXI: **reparada**, pendiente de gate global verificable.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 y #167: `OPEN / NOT_MERGED / NOT_MERGEABLE`.

## Paso siguiente

Reparar **exclusivamente** el residuo estructural de `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`, preservando su contenido probatorio e igualando la granularidad de párrafos ES/EN; después volver a verificar la auditoría global sin rebajar sus reglas.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the current global ES/EN audit and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, open and non-canonical. The manifesto index remains **I–LXXXI + ∞**. The Neoaxiomatic layer retains **NAX-01–NAX-14** as canon and **C-NAX-15–C-NAX-26** as candidates open to SAN™. Public Issue #161 remains open and explicitly declares `CANDIDATE · OPEN SYNTHESIS`; its gate prevents automatic promotion to canonical 7.3.

The current versioned global ES/EN audit observed before this delta reports **323 active Markdown files**, **257 split ES/EN documents**, **1 structural failure**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. The sole versioned structural failure remains `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`. Therefore no global PASS is demonstrated.

Public PRs #165 and #167 remain `OPEN / NOT_MERGED / NOT_MERGEABLE`; both are older maintenance branches and neither was used or modified in this iteration.

## Selected problem

Run 11 left **LXXXI** as its single next step. Its live route and canonical mirror both contained complete ES/EN layers but lacked the visible initial language selector.

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the visible selector:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

was added to:

- `manifiestos/81_ultralujo_bien_comun_elite_neodialectica_aporte_ES_EN.md`;
- `manifiestos/canonicos/LXXXI_ultralujo_bien_comun_elite_neodialectica_aporte_ES_EN.md`.

No substantive content, genealogy, cross-references, status, Synthesis, Neoaxioms™, Issues or canon rules were changed.

## Tests and result

Post-read verification of both surfaces confirms:

1. a visible selector before `# ES · Castellano`;
2. links to `#es--castellano` and `#en--english`;
3. the actual later presence of both language headings;
4. preservation of the body and of the expected relative-path difference between the live source (`../README.md`) and canonical mirror (`../../README.md`).

**LXXXI target result:** `PASS`.

All four known affected pairs from the LXXVIII–LXXXI regression have now been repaired across public runs 09–12. This closes the **known residue** of that regression, but no global `LANGUAGE_SELECTOR_GATE = PASS` is declared yet because no recoverable execution of the new workflow exists for the current commit.

No global ES/EN PASS is declared either: the versioned audit still records **1 known structural failure, Run 06**.

## Residues

- Versioned global structural symmetry: **1 known failure**, Run 06.
- Known LXXVIII–LXXXI language-navigation regression: **repaired**, pending a verifiable global gate.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 and #167: `OPEN / NOT_MERGED / NOT_MERGEABLE`.

## Next step

Repair **only** the remaining structural residue in `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`, preserving its evidentiary content while equalising ES/EN paragraph granularity; then rerun or re-verify the global audit without weakening its rules.
