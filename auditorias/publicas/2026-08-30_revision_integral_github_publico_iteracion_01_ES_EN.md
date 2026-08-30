# Revisión integral GitHub público · Iteración 01
# Integral public GitHub review · Iteration 01

**Fecha / Date:** 2026-08-30
**Estado / Status:** **REPARACIÓN MATERIAL APLICADA · PASS GLOBAL NO DECLARADO / MATERIAL REPAIR APPLIED · GLOBAL PASS NOT DECLARED**

[ES · Castellano](#es--resultado) · [EN · English](#en--result)

## ES · Resultado

### Fallo de mayor impacto reparado

La migración reciente de la capa neoaxiomática había restaurado `neoaxiomas/README.md` como índice y extraído NAX-01–NAX-14 y C-NAX-15–C-NAX-26 a documentos propios. Sin embargo, el auditor y tres automatismos seguían modelando el antiguo README monolítico. El gate exigía formulaciones embebidas que ya no debían existir y un workflow podía intentar reconstruirlas. Además, C-NAX-27 figuraba en el índice SAN y en su documento fuente, pero no tenía documento canónico legible propio ni entrada en el README.

### Archivos reparados

- `neoaxiomas/C-NAX-27_SOBERANIA_DIFERENCIADA_SISTEMA_SINTESIS_ES_EN.md`: documento propio íntegro ES/EN, SAN #176, procedencia y retorno al índice.
- `neoaxiomas/README.md`: frontera C-NAX-15–C-NAX-27 y enlace principal de C-NAX-27 a su propio documento.
- `propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md`: estado operativo reconciliado a 13 candidatos, C-NAX-15–C-NAX-27.
- `.github/scripts/audit_neoaxiom_registry_integrity.py`: auditor reescrito para la arquitectura `README = índice` y `NAX/C-NAX = documento propio`.
- `.github/scripts/sync_neoaxiom_candidates.py` y `.github/scripts/repair_neoaxioms_strict_bilingual_symmetry.py`: convertidos en gates no reductivos; ya no reescriben doctrina en el README.
- `.github/workflows/repair-neoaxiom-navigation.yml` y `.github/workflows/audit-nondestructive-corpus.yml`: comprueban rutas documentales propias y fallan cerradamente ante monolitización, ausencia o duplicación.

### Pruebas

- Integridad neoaxiomática: `OK` · 14 NAX canónicos · 13 C-NAX · frontera C-NAX-15–C-NAX-27.
- Registro de manifiestos: 85 entradas · 0 problemas.
- Relaciones clicables: PASS · 172 superficies.
- Ontología NEOCore™: PASS · 521 superficies; Neo0™ y ONe Starkdr™ permanecen diferenciados; competencia delta privada NeoTitán™ requerida.
- Enlaces internos rotos: 0.

### Residuos bloqueantes

- `CONTENT_SYMMETRY`: 11 superficies siguen marcadas por el auditor global.
- `LANGUAGE_NAVIGATION`: 4 documentos carecen de selectores ES/EN navegables.
- `LINK_INTEGRITY`: 8 README conservan bloques de último manifiesto desincronizados, aunque no hay rutas internas rotas.
- `WIKI_PARITY`: no se verificó la proyección de la Wiki real; `WIKI_PROJECTION_PENDING`.

### Regla sistémica endurecida

`README = ÍNDICE` · `NAX/C-NAX = DOCUMENTO PROPIO` · `PROCEDENCIA ≠ LECTURA` · `SAN ≠ PROCEDENCIA` · ningún sincronizador puede sustituir texto doctrinal por un resumen.

**PASO_SIGUIENTE_RECOMENDADO:** reconciliar dinámicamente los bloques `NEO_LATEST_MANIFESTO` de los ocho README señalados por el gate de enlaces.

## EN · Result

### Highest-impact failure repaired

The recent Neoaxiom-layer migration had restored `neoaxiomas/README.md` as an index and extracted NAX-01–NAX-14 and C-NAX-15–C-NAX-26 into their own documents. The auditor and three automations, however, still modelled the former monolithic README. The gate required embedded formulations that should no longer exist, and a workflow could attempt to rebuild them. C-NAX-27 also appeared in the SAN index and its source document but lacked its own readable canonical document and README entry.

### Repaired files

- `neoaxiomas/C-NAX-27_SOBERANIA_DIFERENCIADA_SISTEMA_SINTESIS_ES_EN.md`: complete ES/EN own document, SAN #176, provenance and index return route.
- `neoaxiomas/README.md`: C-NAX-15–C-NAX-27 frontier and primary C-NAX-27 link to its own document.
- `propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md`: operational state reconciled to 13 candidates, C-NAX-15–C-NAX-27.
- `.github/scripts/audit_neoaxiom_registry_integrity.py`: auditor rewritten for `README = index` and `NAX/C-NAX = own document`.
- `.github/scripts/sync_neoaxiom_candidates.py` and `.github/scripts/repair_neoaxioms_strict_bilingual_symmetry.py`: converted into non-reductive gates; they no longer rewrite doctrine into README.
- `.github/workflows/repair-neoaxiom-navigation.yml` and `.github/workflows/audit-nondestructive-corpus.yml`: verify own-document routes and fail closed on monolith reconstruction, missing documents or duplicates.

### Tests

- Neoaxiom integrity: `OK` · 14 canonical NAX · 13 C-NAX · C-NAX-15–C-NAX-27 frontier.
- Manifesto registry: 85 entries · 0 problems.
- Clickable relations: PASS · 172 surfaces.
- NEOCore™ ontology: PASS · 521 surfaces; Neo0™ and ONe Starkdr™ remain distinct; private NeoTitan™ delta literacy is required.
- Broken internal links: 0.

### Remaining blockers

- `CONTENT_SYMMETRY`: 11 surfaces remain flagged by the global auditor.
- `LANGUAGE_NAVIGATION`: 4 documents lack navigable ES/EN selectors.
- `LINK_INTEGRITY`: 8 README files retain unsynchronised latest-manifesto blocks, although no internal path is broken.
- `WIKI_PARITY`: the live Wiki projection was not verified; `WIKI_PROJECTION_PENDING`.

### Hardened systemic rule

`README = INDEX` · `NAX/C-NAX = OWN DOCUMENT` · `PROVENANCE ≠ READING` · `SAN ≠ PROVENANCE` · no synchroniser may substitute doctrinal text with a summary.

**RECOMMENDED_NEXT_STEP:** dynamically reconcile the `NEO_LATEST_MANIFESTO` blocks in the eight README files reported by the link gate.
