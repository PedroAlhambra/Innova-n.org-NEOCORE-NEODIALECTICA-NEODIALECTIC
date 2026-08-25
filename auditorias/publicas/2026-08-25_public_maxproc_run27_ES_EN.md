# MAXPROC público · Run27 / Public MAXPROC · Run27

**Fecha / Date:** 2026-08-25  
**Estado observado / Observed state:** 7.3-CANDIDATE continúa abierta y no canónica / 7.3-CANDIDATE remains open and non-canonical.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado inicial demostrado

- `CONTENT_SYMMETRY`: PASS en la auditoría pública vigente.
- `LANGUAGE_NAVIGATION`: PASS con 0 fallos en la auditoría pública vigente.
- `LINK_INTEGRITY`: el informe vigente declara `OK`, 0 enlaces internos rotos y 0 fallos canónicos críticos.
- `RELATIONAL_NAVIGATION`: permanece en PASS documental según la auditoría relacional vigente.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## Problema elegido

El workflow `.github/workflows/audit-markdown-readmes-links.yml` ejecutaba un auditor que recorre todo el Markdown activo, pero su filtro `push.paths` sólo cubría subconjuntos concretos (`README`, manifiestos y Síntesis Abierta). Un cambio en otras superficies Markdown activas —por ejemplo análisis, obras, auditorías o documentación WEB4 no-README— podía introducir un enlace local roto sin disparar automáticamente `LINK_INTEGRITY`.

Esto era una brecha de cobertura del gate, no un enlace roto demostrado en el corpus actual.

## Acción

Se sustituyó la lista parcial de rutas Markdown del trigger por `**/*.md`, conservando además los disparadores específicos del propio workflow, del auditor Python y de `manifiestos/CANONICAL_FILENAMES.json`.

**Commit material:** `99ace32801ee7d982486d9e5f042809bd6cd8898`.

No se modificó contenido sustantivo, genealogía, manifiestos, neoaxiomas, WEB4, estados de Síntesis ni la condición de 7.3-CANDIDATE.

## Verificación

El workflow actualizado conserva la ejecución de `.github/scripts/audit_markdown_links_readmes.py`, el commit trazable del informe cuando cambia y el bloqueo `DOCUMENTARY_GRAPH=OK`. El último informe público disponible continúa declarando 0 enlaces internos rotos y 0 fallos canónicos críticos. La modificación amplía únicamente la cobertura automática futura del mismo gate.

**Resultado de la iteración:** **PASS** para el delta elegido: la cobertura automática de `LINK_INTEGRITY` ya alcanza cualquier modificación Markdown pública activa.

## PASO_SIGUIENTE

Auditar la cobertura automática de `RELATIONAL_NAVIGATION` frente a cambios en todo el corpus activo y corregir únicamente el primer hueco de trigger o sincronización que pueda demostrarse.

---

# EN · English

## Demonstrated initial state

- `CONTENT_SYMMETRY`: PASS in the current public audit.
- `LANGUAGE_NAVIGATION`: PASS with 0 failures in the current public audit.
- `LINK_INTEGRITY`: the current report declares `OK`, 0 broken internal links and 0 critical canonical failures.
- `RELATIONAL_NAVIGATION`: remains documentary PASS according to the current relational audit.
- `CANONICAL_STATE`: `7.3-CANDIDATE / NOT_CANON`.

## Selected problem

The `.github/workflows/audit-markdown-readmes-links.yml` workflow ran an auditor that scans all active Markdown, while its `push.paths` filter covered only specific subsets (`README`, manifestos and Open Synthesis). A change in another active Markdown surface —for example analyses, works, audits or non-README WEB4 documentation— could therefore introduce a broken local link without automatically triggering `LINK_INTEGRITY`.

This was a gate-coverage gap, not a demonstrated broken link in the current corpus.

## Action

The partial Markdown path list was replaced by `**/*.md`, while retaining specific triggers for the workflow itself, the Python auditor and `manifiestos/CANONICAL_FILENAMES.json`.

**Material commit:** `99ace32801ee7d982486d9e5f042809bd6cd8898`.

No substantive content, genealogy, manifestos, neoaxioms, WEB4, Synthesis states or the 7.3-CANDIDATE condition were modified.

## Verification

The updated workflow retains execution of `.github/scripts/audit_markdown_links_readmes.py`, traceable report commits when the report changes, and the `DOCUMENTARY_GRAPH=OK` blocking check. The latest available public report continues to declare 0 broken internal links and 0 critical canonical failures. The change only expands future automatic coverage of the same gate.

**Iteration result:** **PASS** for the selected delta: automatic `LINK_INTEGRITY` coverage now reaches any active public Markdown modification.

## NEXT_STEP

Audit automatic `RELATIONAL_NAVIGATION` coverage against changes across the whole active corpus and correct only the first demonstrable trigger or synchronisation gap.