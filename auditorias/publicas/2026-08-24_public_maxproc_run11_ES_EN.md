# MAXPROC público · Run 11 · reparación de navegación lingüística LXXX
# Public MAXPROC · Run 11 · LXXX language-navigation repair

**Fecha / Date:** 2026-08-24 11:39 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en LXXX, ruta viva + espejo canónico / restoration of the ES/EN selector in LXXX, live route + canonical mirror  
**Commit de reparación / Repair commit:** `0cebd6b477ce59795e25bd32bf950cb40d760076`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, la auditoría global ES/EN vigente y la nota MAXPROC inmediatamente anterior.

La frontera pública sigue siendo **NEOCore™ 7.3-CANDIDATE**, abierta y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La capa neoaxiomática mantiene **NAX-01–NAX-14** como canon y **C-NAX-15–C-NAX-26** como candidatos abiertos a SAN™. Las Issues públicas #161 y #169 conservan explícitamente `CANDIDATE ≠ CANON`; #172 continúa abierto como lote 04 de autosíntesis.

La auditoría global ES/EN versionada observada antes de este delta informa **322 Markdown activos**, **256 documentos ES/EN divididos**, **1 fallo estructural**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. El único fallo estructural versionado continúa siendo `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`. Por tanto, no existe PASS global demostrable.

Las PR públicas abiertas verificadas siguen siendo **#165** y **#167**, ambas antiguas ramas de mantenimiento PRE-7.3, `OPEN / NOT_MERGED / NOT_MERGEABLE`; no se utilizaron ni modificaron en esta iteración.

## Problema elegido

Run 10 dejó como único paso siguiente **LXXX**, cuya ruta viva y espejo canónico conservaban contenido ES/EN materialmente completo pero carecían del selector inicial visible.

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector visible:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

a:

- `manifiestos/80_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md`;
- `manifiestos/canonicos/LXXX_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md`.

Para evitar reconstruir manualmente un manifiesto largo, la reparación se ejecutó mediante un workflow conservativo de una sola ejecución que comprobó primero la presencia de `# ES · Castellano` y `# EN · English`, insertó el selector únicamente en la frontera inicial, ejecutó `git diff --check`, verificó orden y unicidad del selector y se eliminó a sí mismo en el mismo commit material.

No se modificó contenido sustantivo, genealogía, referencias cruzadas, estado, Síntesis, Neoaxiomas™, Issues ni reglas de canon.

## Pruebas y resultado

El commit `0cebd6b...` demuestra exactamente dos inserciones materiales equivalentes —una en la ruta viva y otra en el espejo canónico— y la retirada del workflow temporal. La lectura posterior confirma en ambas superficies:

1. un único selector visible;
2. selector situado antes de `# ES · Castellano`;
3. anchors reales `#es--castellano` y `#en--english`;
4. ausencia de cambios adicionales en el cuerpo del manifiesto.

**Resultado del objetivo LXXX:** `PASS`.

No se declara `LANGUAGE_SELECTOR_GATE = PASS` global: **LXXXI** sigue pendiente en ruta viva y espejo canónico, es decir, **2 superficies activas conocidas**.

Tampoco se declara PASS global ES/EN: la auditoría versionada conserva **1 fallo estructural conocido, Run 06**, y todavía no existe una regeneración posterior a este delta que demuestre otra cosa.

## Residuos

- Simetría estructural global versionada: **1 fallo conocido**, Run 06.
- Navegación lingüística: **LXXXI**, ruta viva + espejo canónico.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 y #167: `OPEN / NOT_MERGED / NOT_MERGEABLE`.

## Paso siguiente

Reparar **LXXXI** añadiendo el selector visible ES/EN en su ruta viva y en su espejo canónico, preservando íntegramente contenido y rutas internas, y verificar ambos documentos después del cambio.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, the current global ES/EN audit and the immediately preceding MAXPROC note.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, open and non-canonical. The manifesto index remains **I–LXXXI + ∞**. The Neoaxiomatic layer retains **NAX-01–NAX-14** as canon and **C-NAX-15–C-NAX-26** as candidates open to SAN™. Public Issues #161 and #169 explicitly preserve `CANDIDATE ≠ CANON`; #172 remains open as self-synthesis batch 04.

The versioned global ES/EN audit observed before this delta reports **322 active Markdown files**, **256 split ES/EN documents**, **1 structural failure**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. The sole versioned structural failure remains `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`. Therefore no global PASS is demonstrated.

The verified open public PRs remain **#165** and **#167**, both older PRE-7.3 maintenance branches, `OPEN / NOT_MERGED / NOT_MERGEABLE`; neither was used or modified in this iteration.

## Selected problem

Run 10 left **LXXX** as its single next step. Its live route and canonical mirror retained materially complete ES/EN content but lacked the visible initial language selector.

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the visible selector:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

was added to:

- `manifiestos/80_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md`;
- `manifiestos/canonicos/LXXX_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md`.

To avoid manually reconstructing a long manifesto, the repair used a conservative one-shot workflow. It first asserted the presence of `# ES · Castellano` and `# EN · English`, inserted the selector only at the initial language boundary, ran `git diff --check`, verified selector order and uniqueness, and removed itself in the same material commit.

No substantive content, genealogy, cross-references, status, Synthesis, Neoaxioms™, Issues or canon rules were changed.

## Tests and result

Commit `0cebd6b...` demonstrates exactly two equivalent material insertions —one in the live route and one in the canonical mirror— plus removal of the temporary workflow. Post-read verification confirms on both surfaces:

1. exactly one visible selector;
2. the selector appears before `# ES · Castellano`;
3. real anchors `#es--castellano` and `#en--english`;
4. no additional changes to the manifesto body.

**LXXX target result:** `PASS`.

No global `LANGUAGE_SELECTOR_GATE = PASS` is declared: **LXXXI** remains pending in its live route and canonical mirror, leaving **2 known active surfaces**.

No global ES/EN PASS is declared either: the versioned audit still records **1 known structural failure, Run 06**, and no post-delta regeneration has yet demonstrated otherwise.

## Residues

- Versioned global structural symmetry: **1 known failure**, Run 06.
- Language navigation: **LXXXI**, live route + canonical mirror.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 and #167: `OPEN / NOT_MERGED / NOT_MERGEABLE`.

## Next step

Repair **LXXXI** by adding the visible ES/EN selector to its live route and canonical mirror, preserving all content and internal paths exactly, then verify both documents after the change.
