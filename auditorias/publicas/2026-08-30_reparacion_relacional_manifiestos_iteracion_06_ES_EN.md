# Reparación relacional pública · Iteración 06 / Public relational repair · Iteration 06

**Fecha / Date:** 2026-08-30  
**Ámbito / Scope:** corpus público de manifiestos y controles de navegación relacional / public manifesto corpus and relational-navigation controls

[ES · Castellano](#es--estado-inicial) · [EN · English](#en--initial-state)

## ES · Estado inicial

La iteración parte de una reparación relacional previamente verificada sobre los manifiestos finitos I–LXXXV y el Manifiesto ∞. La revisión de continuidad detectó, no obstante, una debilidad sistémica del auditor: una relación genealógica podía nombrar en texto plano una pieza como `Manifiesto XLVII` / `Manifesto XLVII` sin marca `™` y el control específico de referencias genealógicas podía no clasificar ese nombre canónico como navegación no clicable.

Esto era incompatible con la regla pública: una relación declarada debe ser navegable en el punto donde se declara; un enlace duplicado posterior no subsana texto plano en la relación original.

## ES · Delta ejecutado

Se endureció `.github/scripts/audit_manifesto_clickable_relations.py` para detectar referencias de manifiesto nombradas en texto plano dentro de `Relación genealógica / Genealogical relation`, después de retirar los enlaces Markdown reales de la superficie analizada. El nuevo fallo explícito es:

`GENEALOGICAL_NAMED_MANIFESTO_NOT_CLICKABLE`

El cambio conserva los controles ya existentes para `GENEALOGICAL_NAVIGATION_FAILURE`, `MAIN_RELATIONS_NOT_CLICKABLE`, `NEOAXIOM_RELATIONS_NOT_CLICKABLE`, `OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`, destinos rotos, sintaxis relacional y ausencia del bloque de referencias canónicas.

**Commit del endurecimiento / Hardening commit:** `e5d3218475afe921b7af5cfde4a45b09718008c9` — `audit(relations): block bare named manifesto references in genealogy`.

El workflow de sincronización ejecutó después sus generadores de referencias, política e índice y produjo una sincronización material de navegación de manifiestos:

**Commit sincronizado / Synchronised commit:** `a30c90072df1b4c18c7613c33748fe6f337bff2f` — `docs: sincronizar navegación e índice de manifiestos`.

## ES · Evidencia fresca

Sobre el head de endurecimiento `e5d3218475afe921b7af5cfde4a45b09718008c9` finalizaron con éxito:

- `Audit manifesto clickable relations` · run `33301686713` · `completed/success`.
- `Repair manifesto genealogical links` · run `33301686680` · `completed/success`.
- `sync-manifesto-crossrefs` · run `33301686732` · `completed/success`.

`sync-manifesto-crossrefs` ejecuta, por este orden, la sincronización de referencias canónicas, la política de referencias, el índice/frontera y **después audita la navegabilidad relacional antes de crear su commit**. Por tanto, el árbol sincronizado que se convirtió en `a30c90072df1b4c18c7613c33748fe6f337bff2f` fue comprobado por el auditor endurecido antes del commit del bot.

La relectura posterior de `manifiestos/README.md` confirma como frontera viva **85 manifiestos finitos bilingües · I–LXXXV + Manifiesto ∞**, con LXXXV como último manifiesto finito abierto a síntesis.

## ES · Resultado

**RELATIONAL_NAVIGATION_CLICKABLE — PASS para el gate dedicado de manifiestos bajo el auditor endurecido.**

Este PASS no se extrapola a limpieza global de todos los formatos públicos. Los gates independientes de selectores de idioma, simetría global, enlaces de README u otras auditorías deben conservar su propio estado y repararse con evidencia fresca; no se rebaja ningún control para declarar limpio el corpus completo.

## EN · Initial state

This iteration starts from a previously verified relational repair across finite manifestos I–LXXXV and Manifesto ∞. Continuity review nevertheless found a systemic audit weakness: a genealogical relation could name a canonical piece in plain text such as `Manifiesto XLVII` / `Manifesto XLVII` without a `™` marker, and the specific genealogical-reference check could fail to classify that canonical name as non-clickable navigation.

That was incompatible with the public rule: a declared relation must be navigable at the point where it is declared; a duplicated link later in the document does not repair plain text in the original relation.

## EN · Executed delta

`.github/scripts/audit_manifesto_clickable_relations.py` was hardened to detect plain-text named manifesto references inside `Relación genealógica / Genealogical relation` after real Markdown links are removed from the analysed surface. The new explicit failure is:

`GENEALOGICAL_NAMED_MANIFESTO_NOT_CLICKABLE`

The change preserves the existing controls for `GENEALOGICAL_NAVIGATION_FAILURE`, `MAIN_RELATIONS_NOT_CLICKABLE`, `NEOAXIOM_RELATIONS_NOT_CLICKABLE`, `OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`, broken destinations, relational syntax and missing canonical cross-reference blocks.

**Hardening commit:** `e5d3218475afe921b7af5cfde4a45b09718008c9` — `audit(relations): block bare named manifesto references in genealogy`.

The synchronisation workflow then ran its cross-reference, policy and index generators and produced a material manifesto-navigation synchronisation:

**Synchronised commit:** `a30c90072df1b4c18c7613c33748fe6f337bff2f` — `docs: sincronizar navegación e índice de manifiestos`.

## EN · Fresh evidence

On hardening head `e5d3218475afe921b7af5cfde4a45b09718008c9`, the following completed successfully:

- `Audit manifesto clickable relations` · run `33301686713` · `completed/success`.
- `Repair manifesto genealogical links` · run `33301686680` · `completed/success`.
- `sync-manifesto-crossrefs` · run `33301686732` · `completed/success`.

`sync-manifesto-crossrefs` runs canonical cross-reference synchronisation, reference-policy synchronisation and index/frontier synchronisation and **then audits relational navigability before creating its commit**. Therefore, the synchronised tree that became `a30c90072df1b4c18c7613c33748fe6f337bff2f` was checked by the hardened auditor before the bot commit.

A subsequent reread of `manifiestos/README.md` confirms the living frontier as **85 finite bilingual manifestos · I–LXXXV + Manifesto ∞**, with LXXXV as the latest finite manifesto open for synthesis.

## EN · Result

**RELATIONAL_NAVIGATION_CLICKABLE — PASS for the dedicated manifesto gate under the hardened auditor.**

This PASS is not extrapolated to global cleanliness of every public format. Independent language-selector, global-symmetry, README-link and other gates must retain their own state and be repaired with fresh evidence; no control is weakened in order to declare the whole corpus clean.

## PASO_SIGUIENTE_RECOMENDADO / NEXT_STEP

Diagnosticar y reparar el primer fallo vigente de los gates públicos de simetría, selector de idioma o enlaces README, sin rebajar auditorías y preservando el gate relacional recién endurecido. / Diagnose and repair the first current failure in the public symmetry, language-selector or README-link gates without weakening audits and while preserving the newly hardened relational gate.
