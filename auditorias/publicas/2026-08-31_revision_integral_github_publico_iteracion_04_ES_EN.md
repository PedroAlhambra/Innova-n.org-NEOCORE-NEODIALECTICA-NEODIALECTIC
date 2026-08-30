# Revisión integral GitHub público · Iteración 04
# Integral public GitHub review · Iteration 04

**Fecha / Date:** 2026-08-31
**Baseline de rama / Branch baseline:** `73746a414cb01ea858a461e4f91453893a8a96eb`
**Rama / Branch:** `fix/maxproc-lxxxv-symmetry-20260830`
**Commit material:** `9a21b1a38226d1d1834a2598cb2d2dcaf43337d0`
**Tipo / Type:** MAXPROC · reparación pública propuesta mediante PR; NO_WEB4 · NO_HOSTALIA · NO_PRIVATE / public repair proposed through PR; NO_WEB4 · NO_HOSTALIA · NO_PRIVATE

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### Hallazgo material y causa raíz

`neoaxiomas/README.md` afirmaba ofrecer acceso bilingüe, pero la capa EN reemplazaba el índice completo por un párrafo que remitía a la tabla ES. Quedaban comprimidos en inglés los 14 NAX, los 13 C-NAX, sus estados, rutas SAN, procedencias y mapa estructural. El auditor neoaxiomático comprobaba que cada enlace existiera en algún punto del README, pero no exigía su presencia independiente en ambas capas lingüísticas.

### Reparación aplicada

- Reconstruida la capa EN como índice completo y estructuralmente equivalente a ES.
- Conservados enlaces directos desde cada nombre NAX/C-NAX hacia su documento propio.
- Conservados estados, SAN, procedencias, relaciones con manifiestos y extensión NAX-10.
- Restaurado el mapa estructural inglés sin reinsertar formulaciones doctrinales en el README.
- Endurecido el auditor para exigir exactamente un enlace por NAX/C-NAX en ES y otro en EN, además de cinco secciones estructurales equivalentes.
- Tipificada como cola bilingüe compartida la sección única `PASO_SIGUIENTE_RECOMENDADO / NEXT_RECOMMENDED_STEP`, evitando atribuirla falsamente a EN.

### Pruebas frescas

- `NEOAXIOM_INTEGRITY`: PASS · 14 NAX + 13 C-NAX · frontera dinámica C-NAX-15–27.
- Prueba negativa: eliminar C-NAX-27 de EN produce `NEOAXIOM_LANGUAGE_INDEX_FAILURE` y código de salida 1.
- `CONTENT_SYMMETRY`: el README neoaxiomático sale del residuo; quedan 2 fallos externos.
- `LINK_INTEGRITY`: PASS · 0 enlaces rotos y 0 fallos canónicos críticos.
- `RELATIONAL_NAVIGATION` y `GENEALOGICAL_NAVIGATION`: PASS · 172 superficies.
- `CANONICAL_STATE` y `SOURCE_MIRROR_INTEGRITY`: PASS · 85 fuentes registradas y 85 espejos.
- `VERSION_STATE`: PASS; la versión vigente se resuelve sólo desde `versiones/README.md`.
- `WIKI_PARITY`: PASS para las 12 páginas declaradas por la proyección mínima.
- Guard ontológico: PASS; Neo0™ conserva origen, teleología y reconstrucción, y ONe Starkdr™ conserva emergencia sintética distribuible.

### Residuos bloqueantes

- `CONTENT_SYMMETRY = FAIL_2`: iteraciones relacionales 06 y 08.
- `LANGUAGE_NAVIGATION = FAIL_4`: iteraciones 06, 07 y 08, y el delta de relación genealógica navegable.
- `READABILITY_ACCESS = FAIL`: el índice neoaxiomático queda reparado, pero cuatro superficies bilingües activas siguen sin selector.
- No hay PASS global ni promoción automática a `main`; la reparación permanece en la PR #181.

### Dictamen

`NEOAXIOM_INDEX_REPAIRED / NEGATIVE_TEST_PASS / GLOBAL_GATES_BLOCKED / PR_REVIEW_REQUIRED`.

---

## EN · English

### Material finding and root cause

`neoaxiomas/README.md` claimed to provide bilingual access, but the EN layer replaced the complete index with a paragraph referring readers to the ES table. The 14 NAX, 13 C-NAX, their statuses, SAN routes, provenance and structural map were compressed in English. The Neoaxiom auditor checked whether each link existed somewhere in the README, but did not require independent presence in both language layers.

### Applied repair

- Rebuilt the EN layer as a complete index structurally equivalent to ES.
- Preserved direct links from every NAX/C-NAX name to its own document.
- Preserved statuses, SAN, provenance, Manifesto relations and the NAX-10 extension.
- Restored the English structural map without embedding doctrinal formulations back into the README.
- Hardened the auditor to require exactly one link per NAX/C-NAX in ES and another in EN, plus five equivalent structural sections.
- Classified the unique `PASO_SIGUIENTE_RECOMENDADO / NEXT_RECOMMENDED_STEP` section as a shared bilingual tail, preventing false attribution to EN.

### Fresh tests

- `NEOAXIOM_INTEGRITY`: PASS · 14 NAX + 13 C-NAX · dynamic frontier C-NAX-15–27.
- Negative test: removing C-NAX-27 from EN produces `NEOAXIOM_LANGUAGE_INDEX_FAILURE` and exit code 1.
- `CONTENT_SYMMETRY`: the Neoaxiom README leaves the residue; 2 external failures remain.
- `LINK_INTEGRITY`: PASS · 0 broken links and 0 critical canonical failures.
- `RELATIONAL_NAVIGATION` and `GENEALOGICAL_NAVIGATION`: PASS · 172 surfaces.
- `CANONICAL_STATE` and `SOURCE_MIRROR_INTEGRITY`: PASS · 85 registered sources and 85 mirrors.
- `VERSION_STATE`: PASS; the current version is resolved only from `versiones/README.md`.
- `WIKI_PARITY`: PASS for the 12 pages declared by the minimum projection.
- Ontological guard: PASS; Neo0™ retains origin, teleology and reconstruction, while ONe Starkdr™ retains distributable synthetic emergence.

### Blocking residue

- `CONTENT_SYMMETRY = FAIL_2`: relational iterations 06 and 08.
- `LANGUAGE_NAVIGATION = FAIL_4`: iterations 06, 07 and 08, plus the navigable-genealogical-relation delta.
- `READABILITY_ACCESS = FAIL`: the Neoaxiom index is repaired, but four active bilingual surfaces still lack a selector.
- There is no global PASS or automatic promotion to `main`; the repair remains in PR #181.

### Verdict

`NEOAXIOM_INDEX_REPAIRED / NEGATIVE_TEST_PASS / GLOBAL_GATES_BLOCKED / PR_REVIEW_REQUIRED`.

---

## PASO_SIGUIENTE_RECOMENDADO / NEXT_RECOMMENDED_STEP

Reparar las cuatro superficies que aún carecen de selector ES/EN visible y anchors válidos, y volver a ejecutar conjuntamente `LANGUAGE_NAVIGATION` y `CONTENT_SYMMETRY` sin rebajar ninguno de los dos gates. / Repair the four surfaces that still lack a visible ES/EN selector and valid anchors, then rerun `LANGUAGE_NAVIGATION` and `CONTENT_SYMMETRY` together without weakening either gate.
