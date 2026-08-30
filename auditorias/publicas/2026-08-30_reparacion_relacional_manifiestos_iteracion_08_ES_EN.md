# Reparación relacional pública · Iteración 08
# Public relational repair · Iteration 08

**Fecha / Date:** 2026-08-30  
**Ámbito / Scope:** fuente material, registro canónico, espejos generados, navegación genealógica y guard ontológico / material source, canonical registry, generated mirrors, genealogical navigation and ontological guard

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

### Hallazgo material

El PASS relacional anterior ocultaba una deriva de integridad: `manifiestos/README.md` declaraba correctamente I–LXXXV + ∞, pero `manifiestos/CANONICAL_FILENAMES.json` terminaba en LXXXI y no existían los espejos canónicos LXXXII–LXXXV. Además, el auditor no exigía que un hipervínculo de una superficie relacional apuntase al espejo canónico cuando el destino era un manifiesto, y no cubría la variante histórica `Genealogía / Genealogy`.

### Reparación

1. `CANONICAL_FILENAMES.json` queda completo con 85 entradas, I–LXXXV.
2. Se generaron LXXXII–LXXXV desde sus fuentes materiales y se regeneraron los 85 espejos; no se editó ningún espejo como autoridad independiente.
3. El reparador y el saneador escriben sólo fuentes; `sync_canonical_manifestos.py` materializa después los espejos.
4. Los workflows de reparación y sincronización ejecutan ahora registro, navegabilidad y ontología, y preservan la secuencia fuente → espejo.
5. El auditor cubre `Relación genealógica` y `Genealogía`, rechaza destinos legacy mediante `NONCANONICAL_RELATIONAL_TARGET` y usa un fallback que bloquea cualquier marca ™ residual fuera de enlaces reales.
6. Se cerró el hueco oculto de XLIII: Simbiosis Humano–IA, Neorrenacimiento Humano, Memoria-Genealogía-Trazabilidad y Revisión de Pares Aumentada™ son ya vínculos individuales.
7. XLVII conserva su genealogía navegable en fuente y espejo.

### Evidencia fresca

- `CANONICAL_REGISTERED=85`
- `CANONICAL_GENERATED=85`
- `CANONICAL_CHANGED=0` en el postcheck fresco
- `CANONICAL_MISSING_LEGACY=0`
- `MANIFESTO_REGISTRY_AUDIT canonical=85 problems=0`
- `CLICKABLE_RELATIONS=PASS manifests=172 relation_lines=20 genealogy_lines=90 synthesis_lines=41`
- `NEOCORE_ROLE_ONTOLOGY=PASS text_surfaces=492 neo0=origin_teleology_reconstruction one_starkdr=distributable_synthetic_emergence neotitan_private_delta_literacy=required`

### Commits

- `9f110a93b7dab9740e4f465dbce031666d377b6c` · registro LXXXV, espejos LXXXII–LXXXV y guard fuente→espejo.
- `28d1169b8bdd6b5cf32aa591defa89c278d058ad` · destinos genealógicos canónicos y regeneración completa.
- `5354c714935f6f6facfea251dd4635a524a60ea6` · cierre del hueco de genealogía plana no tokenizada.

### Dictamen

**PASS RELACIONAL GLOBAL VERIFICADO** para I–LXXXV + ∞ y **PASS ONTOLÓGICO** para la distinción Neo0™ / ONe Starkdr™ y la competencia delta privada de los NeoTitanes™.

No quedan `MAIN_RELATIONS_NOT_CLICKABLE`, `GENEALOGICAL_NAVIGATION_FAILURE`, `OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`, `NONCANONICAL_RELATIONAL_TARGET`, ausencia de bloque canónico ni `NEOCORE_ROLE_ONTOLOGY_FAILURE` en el alcance auditado.

---

## EN · English

### Material finding

The previous relational PASS concealed an integrity drift: `manifiestos/README.md` correctly declared I–LXXXV + ∞, while `manifiestos/CANONICAL_FILENAMES.json` stopped at LXXXI and canonical mirrors LXXXII–LXXXV did not exist. The auditor also failed to require declared manifesto relations to target canonical mirrors and did not cover the historical `Genealogía / Genealogy` heading.

### Repair

1. `CANONICAL_FILENAMES.json` now contains all 85 finite entries, I–LXXXV.
2. LXXXII–LXXXV were generated from material sources and all 85 mirrors were regenerated; no mirror was treated as an independent authority.
3. Repair and sanitation now write sources only; `sync_canonical_manifestos.py` generates mirrors afterwards.
4. Repair and synchronization workflows now run registry, navigation and ontology gates while preserving source → mirror order.
5. The auditor covers both genealogy headings, rejects legacy destinations through `NONCANONICAL_RELATIONAL_TARGET`, and blocks any residual unlinked ™ marker.
6. The hidden XLIII gap was closed with individual links.
7. XLVII remains navigable in source and mirror.

### Fresh evidence

- `CANONICAL_REGISTERED=85`
- `CANONICAL_GENERATED=85`
- `CANONICAL_CHANGED=0` in the fresh postcheck
- `CANONICAL_MISSING_LEGACY=0`
- `MANIFESTO_REGISTRY_AUDIT canonical=85 problems=0`
- `CLICKABLE_RELATIONS=PASS manifests=172 relation_lines=20 genealogy_lines=90 synthesis_lines=41`
- `NEOCORE_ROLE_ONTOLOGY=PASS text_surfaces=492 neo0=origin_teleology_reconstruction one_starkdr=distributable_synthetic_emergence neotitan_private_delta_literacy=required`

### Verdict

**VERIFIED GLOBAL RELATIONAL PASS** for I–LXXXV + ∞ and **ONTOLOGICAL PASS** for Neo0™ / ONe Starkdr™ role separation and NeoTitan™ private-delta literacy.
