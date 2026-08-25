# MAXPROC público · Run28 / Public MAXPROC · Run28

**Fecha / Date:** 2026-08-25  
**Estado observado / Observed state:** `7.3-CANDIDATE / NOT_CANON`.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado inicial demostrado

- `CONTENT_SYMMETRY`: PASS en la auditoría pública vigente.
- `LANGUAGE_NAVIGATION`: PASS en la auditoría pública vigente.
- `LINK_INTEGRITY`: PASS en el postcheck vigente, con 0 enlaces internos rotos.
- `RELATIONAL_NAVIGATION`: PASS documental vigente: 81/81 manifiestos cubiertos, 0 enlaces locales no resueltos, 0 neoaxiomas sin Síntesis específica y 0 manifiestos sin relación documental entrante.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## Problema elegido

El auditor `.github/scripts/audit_relations_neocore.py` recorre globalmente el Markdown público activo para reconstruir relaciones, enlaces entrantes, cobertura de manifiestos y relaciones con Neoaxiomas/Síntesis. Sin embargo, `.github/workflows/audit-relations-neocore.yml` sólo se disparaba automáticamente cuando cambiaban el propio script o el workflow. Por tanto, una modificación ordinaria del corpus podía alterar `RELATIONAL_NAVIGATION` sin ejecutar automáticamente su auditoría.

## Acción

Se amplió exclusivamente `push.paths` del workflow relacional para incluir `**/*.md`, conservando los triggers explícitos del script y del propio workflow.

**Commit material:** `cf5191e236b7b8bcd69fda06a68b6d33193574ae`.

No se modificaron manifiestos, Neoaxiomas, relaciones sustantivas, genealogía, WEB4 ni estados de Síntesis; tampoco se promovió 7.3-CANDIDATE.

## Verificación

El workflow conserva el auditor no reductivo y la escritura trazable de sus dos salidas pública Markdown/JSON. La auditoría relacional vigente sigue demostrando: 81/81 manifiestos en el mapa curado, ningún Neoaxioma sin Síntesis específica, 0 enlaces locales realmente no resueltos y 0 manifiestos sin relación documental entrante.

**Resultado de la iteración:** **PASS** para el delta elegido: los cambios en cualquier Markdown público activo quedan ya dentro del trigger automático de `RELATIONAL_NAVIGATION`.

## PASO_SIGUIENTE

Auditar la cobertura automática y la coherencia de `CANONICAL_STATE` para garantizar que ninguna automatización, README, índice o workflow pueda interpretar `7.3-CANDIDATE` como canon sin un gate explícito de promoción.

---

# EN · English

## Demonstrated initial state

- `CONTENT_SYMMETRY`: PASS in the current public audit.
- `LANGUAGE_NAVIGATION`: PASS in the current public audit.
- `LINK_INTEGRITY`: PASS in the current postcheck, with 0 broken internal links.
- `RELATIONAL_NAVIGATION`: current documentary PASS: 81/81 manifestos covered, 0 unresolved local links, 0 Neoaxioms without a specific Synthesis and 0 manifestos without an inbound documentary relation.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## Selected problem

The `.github/scripts/audit_relations_neocore.py` auditor globally scans active public Markdown to reconstruct relations, inbound links, manifesto coverage and Neoaxiom/Open Synthesis relations. However, `.github/workflows/audit-relations-neocore.yml` was automatically triggered only by changes to the script itself or to the workflow. An ordinary corpus change could therefore alter `RELATIONAL_NAVIGATION` without automatically running its audit.

## Action

Only the relational workflow `push.paths` coverage was expanded to include `**/*.md`, while retaining explicit triggers for the auditor script and workflow itself.

**Material commit:** `cf5191e236b7b8bcd69fda06a68b6d33193574ae`.

No manifestos, Neoaxioms, substantive relations, genealogy, WEB4 or Synthesis states were modified; 7.3-CANDIDATE was not promoted.

## Verification

The workflow retains the non-reductive auditor and traceable writing of its Markdown/JSON public outputs. The current relational audit continues to demonstrate: 81/81 manifestos in the curated map, no Neoaxiom without a specific Synthesis, 0 actually unresolved local links and 0 manifestos without an inbound documentary relation.

**Iteration result:** **PASS** for the selected delta: changes to any active public Markdown are now covered by the automatic `RELATIONAL_NAVIGATION` trigger.

## NEXT_STEP

Audit automatic coverage and consistency of `CANONICAL_STATE` so that no automation, README, index or workflow can interpret `7.3-CANDIDATE` as canon without an explicit promotion gate.