# Reparación relacional pública · Iteración 07
# Public relational repair · Iteration 07

**Fecha / Date:** 2026-08-30  
**Ámbito / Scope:** corpus público de manifiestos, frontera canónica y navegación de Síntesis Abierta / public manifesto corpus, canonical frontier and Open Synthesis navigation

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

### Estado observado

La navegabilidad interna de los manifiestos I–LXXXV + ∞ permanecía protegida por el gate relacional, pero el postcheck dinámico detectó una deriva de frontera en `propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md`: el índice completo declaraba todavía I–LXXXIV y omitía LXXXV y su Síntesis Abierta #180, aunque `manifiestos/README.md` ya fijaba correctamente 85 manifiestos finitos I–LXXXV + ∞.

Esto no era un fallo de contenido del Manifiesto LXXXV: `85_memoria_capitan_grant_ES_EN.md` ya declaraba explícitamente su Síntesis Abierta #180. Era un fallo sistémico de reconciliación entre superficies canónicas.

### Causa raíz

`register_manifesto_frontier.py` añadía entradas al índice completo de Síntesis Abierta cuando detectaba manifiestos todavía no registrados. Una vez que LXXXV ya estaba registrado, una deriva residual del índice podía persistir porque el flujo no reconstruía la tabla completa desde la frontera canónica vigente.

La primera versión del nuevo reconciliador fue además demasiado estricta con formatos históricos de metadatos SAN y falló de forma segura. No se rebajó el gate ni se inventaron Issues. Se sustituyó esa hipótesis por una estrategia conservadora: preservar mapeos ya explícitos y coherentes del propio índice para manifiestos existentes y exigir metadato SAN explícito para cualquier fila nueva o ausente.

### Reparación material

1. Se creó `.github/scripts/sync_complete_synthesis_frontier.py` para reconciliar dinámicamente la tabla completa de manifiestos/SAN con la colección canónica de `manifiestos/README.md`.
2. Se creó `.github/workflows/sync-complete-synthesis-frontier.yml` para ejecutar esa reconciliación automáticamente cuando cambian manifiestos, registro canónico o el propio reconciliador.
3. El reconciliador verifica existencia del manifiesto, ordinal único, correspondencia exacta de path, Issue SAN explícito o ya establecido de forma coherente, conservación de ∞ y cobertura ES/EN.
4. El workflow ejecuta después `.github/scripts/audit_manifesto_clickable_relations.py` y `git diff --check` antes de permitir el commit de sincronización.
5. La ejecución correcta generó automáticamente `e42dcb9f821e9c269fe850bda52121b41c897243` (`sync: reconcile complete Open Synthesis frontier`).

Commits de endurecimiento de esta iteración:

- `14e53da487327b3b294fc703066f485d979515ba` · primera versión del reconciliador.
- `a8d5ef204b9ef4c83589e6c1d2df8d4a91594b03` · workflow preventivo.
- `0a810cda85a6ccc31774f0e8f0be82230bdbacd1` · diagnóstico/formato histórico SAN conservador.
- `f85bf942c1d641af83a871cae26f7fbc10215b10` · reconciliación definitiva desde índice explícito + metadato SAN explícito.
- `e42dcb9f821e9c269fe850bda52121b41c897243` · materialización automática de la frontera completa.

### Evidencia fresca

La ejecución `Sync complete Open Synthesis frontier` sobre `f85bf942...` terminó `success`. Pasaron expresamente las etapas `Reconcile complete Open Synthesis index`, `Verify manifesto relational gate`, `Verify Markdown diff` y `Commit reconciled synthesis frontier`.

El índice resultante declara ahora **85 manifiestos finitos I–LXXXV + Manifiesto ∞ / 85 finite manifestos I–LXXXV + Manifesto ∞** y contiene una fila navegable LXXXV hacia `../../manifiestos/85_memoria_capitan_grant_ES_EN.md` y la Síntesis Abierta `#180`, seguida de ∞.

### Resultado

**PASS RELACIONAL DE FRONTERA / RELATIONAL FRONTIER PASS** para el alcance de este bucle. La frontera de manifiestos y el índice completo de Síntesis Abierta vuelven a ser coherentes y existe ahora un control preventivo que reconstruye y valida esa relación ante cambios futuros.

Este PASS no se usa para declarar que todas las superficies documentales no relacionadas del repositorio hayan superado todos sus gates de formato, simetría o actualidad. Los residuos ajenos al alcance relacional conservan su estado propio.

**PASO_SIGUIENTE:** ceder el turno de mejora a WEB4 manteniendo activo en CI el reconciliador preventivo de frontera pública.

---

## EN · English

### Observed state

Internal manifesto navigation across I–LXXXV + ∞ remained protected by the relational gate, but the dynamic postcheck found frontier drift in `propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md`: the complete index still declared I–LXXXIV and omitted LXXXV and its Open Synthesis #180, while `manifiestos/README.md` already correctly fixed the frontier at 85 finite manifestos I–LXXXV + ∞.

This was not a content failure in Manifesto LXXXV: `85_memoria_capitan_grant_ES_EN.md` already explicitly declared Open Synthesis #180. It was a systemic reconciliation failure between canonical surfaces.

### Root cause

`register_manifesto_frontier.py` appended entries to the complete Open Synthesis index when it detected manifestos not yet registered. Once LXXXV was already registered, residual index drift could remain because the flow did not rebuild the full table from the current canonical frontier.

The first version of the new reconciler was also too strict about historical SAN metadata formats and failed safely. The gate was not weakened and no Issues were invented. That hypothesis was replaced by a conservative strategy: preserve already explicit and coherent mappings from the index itself for existing manifestos, while requiring explicit SAN metadata for any new or missing row.

### Material repair

1. `.github/scripts/sync_complete_synthesis_frontier.py` was created to dynamically reconcile the complete manifesto/SAN table against the canonical collection in `manifiestos/README.md`.
2. `.github/workflows/sync-complete-synthesis-frontier.yml` was created to run that reconciliation automatically when manifestos, the canonical registry, or the reconciler itself changes.
3. The reconciler verifies manifesto existence, unique ordinal, exact path correspondence, explicit or already coherently established SAN Issue mapping, preservation of ∞, and ES/EN coverage.
4. The workflow then runs `.github/scripts/audit_manifesto_clickable_relations.py` and `git diff --check` before allowing the synchronization commit.
5. The successful run automatically generated `e42dcb9f821e9c269fe850bda52121b41c897243` (`sync: reconcile complete Open Synthesis frontier`).

Hardening commits in this iteration:

- `14e53da487327b3b294fc703066f485d979515ba` · initial reconciler.
- `a8d5ef204b9ef4c83589e6c1d2df8d4a91594b03` · preventive workflow.
- `0a810cda85a6ccc31774f0e8f0be82230bdbacd1` · conservative historical SAN-format diagnosis.
- `f85bf942c1d641af83a871cae26f7fbc10215b10` · final reconciliation from explicit index + explicit SAN metadata.
- `e42dcb9f821e9c269fe850bda52121b41c897243` · automatic materialisation of the complete frontier.

### Fresh evidence

The `Sync complete Open Synthesis frontier` run on `f85bf942...` completed with `success`. The steps `Reconcile complete Open Synthesis index`, `Verify manifesto relational gate`, `Verify Markdown diff`, and `Commit reconciled synthesis frontier` all passed explicitly.

The resulting index now declares **85 finite manifestos I–LXXXV + Manifesto ∞** and contains a navigable LXXXV row to `../../manifiestos/85_memoria_capitan_grant_ES_EN.md` and Open Synthesis `#180`, followed by ∞.

### Result

**RELATIONAL FRONTIER PASS** for this loop's scope. The manifesto frontier and complete Open Synthesis index are coherent again, and a preventive control now rebuilds and validates that relation against future changes.

This PASS is not used to claim that every unrelated documentary surface in the repository has passed every formatting, symmetry, or freshness gate. Residues outside the relational scope keep their own status.

**NEXT_STEP:** yield the improvement turn to WEB4 while keeping the public-frontier reconciler active in CI.
