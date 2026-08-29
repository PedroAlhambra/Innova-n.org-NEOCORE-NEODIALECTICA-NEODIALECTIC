# Reparación relacional de manifiestos · Iteración 02
# Manifest relational repair · Iteration 02

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Fecha / Date:** 2026-08-29  
**Alcance / Scope:** repositorio público · manifiestos I–LXXXV + ∞ · controles relacionales  
**Resultado / Result:** **FAIL CONTROLADO / CONTROLLED FAIL** — no se declara PASS global.

---

## ES · Castellano

### Estado observado

La iteración anterior dejó la auditoría ampliada sobre la unión de superficies registradas y archivos realmente presentes. Esta iteración ha trabajado sobre la causa sistémica y sobre una tanda material de relaciones declaradas.

### Cambios ejecutados

1. Se amplió `.github/scripts/repair_manifesto_genealogical_links.py` para reparar no sólo `Relación genealógica / Genealogical relation`, sino también `Relaciones principales / Main relations` y `Relaciones raíz / Root relations`.
2. El reparador resuelve números romanos explícitos y desnudos contra `manifiestos/CANONICAL_FILENAMES.json`, verifica existencia del destino y enlaza `∞` a su manifiesto real.
3. Se amplió `.github/scripts/audit_manifesto_clickable_relations.py` para bloquear también relaciones principales/raíz con numerales sin enlace y para verificar que los destinos Markdown locales existen.
4. El workflow de reparación produjo una tanda material automática sobre las relaciones declaradas, incluyendo superficies LXIV–LXXII y sus espejos cuando procedía.
5. Se añadió tratamiento verificable de identificadores Neoaxioma (`NAX-*` / `C-NAX-*`): `NAX-10` apunta a su documento dedicado y los demás identificadores verificados apuntan al registro canónico `neoaxiomas/README.md` sin inventar anchors inexistentes.
6. El auditor quedó endurecido con `NEOAXIOM_RELATIONS_NOT_CLICKABLE` para que un identificador de Neoaxioma presentado como relación no pueda permanecer en texto plano.

### Commits materiales de esta iteración

- `8eb6492b92e34447f83721aec7d7a94e62751c26` — reparación de todas las superficies relacionales declaradas.
- `ace56dcea467ad4ea7bdbc86f129a355e2bf58ba` — gate de todas las superficies relacionales declaradas.
- `7662a9bbc474d8b67742f86be8f35dc916c13d45` — enlaces para identificadores Neoaxioma.
- `2f2000b046c7d1c1b367fc5723c74dbdd5a1bc8b` — reparación automática material sobre 10 superficies de manifiesto.
- `39563808a52b6fda41fd929adc8ca456f5258105` — gate para Neoaxiomas no enlazados.

### Evidencia de ejecución

El workflow de reparación ejecutó el reparador con éxito y detectó cambios materiales en diez superficies. La auditoría posterior inspeccionó **168 superficies** y mantuvo correctamente `CLICKABLE_RELATIONS=FAIL`.

La causa residual principal ya no es la ausencia de control sobre relaciones principales: son **objetivos genealógicos nominales todavía no resueltos de forma inequívoca**. Entre los casos registrados aparecen `Umbral-X™`, `Protección Integral de la Infancia™`, `Soberanía del Tiempo Cognitivo™`, `Contra el Neuromarketing Antihumanista™`, `Neowar™`, `Síntesis Abierta Neodialéctica™`, `Reconocimiento Neodialéctico™` y otros. Muchos corresponden a manifiestos existentes y deben incorporarse al registro explícito de aliases sólo tras comprobar su destino canónico; otros, como `WEB4™`, `Neodialectica Framework™` o conceptos compuestos, pueden requerir una superficie canónica distinta de un manifiesto y no deben enlazarse por semejanza textual.

La ejecución también ha revelado una anomalía heredada en algunas líneas legacy de `Relaciones principales`: existen construcciones Markdown históricas mal balanceadas donde un vínculo iniciado al principio de la relación se cierra al final de la línea. No se considera resuelto por haber enlazado numerales internos. Debe normalizarse sin alterar el contenido doctrinal.

### Invariante fijado

```text
RELACION_DECLARADA
→ DESTINO_CANONICO_VERIFICADO
→ ENLACE_MARKDOWN_REAL
→ DESTINO_EXISTENTE

SIN_DESTINO_UNIVOCO
→ UNRESOLVED_GENEALOGICAL_TARGET
→ NO_INVENTAR_ENLACE
```

Un enlace en `Referencias cruzadas canónicas` no subsana una relación genealógica o principal presentada originalmente como texto plano.

### Resultado

**FAIL CONTROLADO.** No existe base para declarar el corpus relacionalmente limpio. Los controles son ahora más estrictos y la tanda material ha reducido relaciones planas, pero persisten objetivos genealógicos no resueltos y líneas legacy que requieren normalización estructural.

### PASO_SIGUIENTE

**Resolver por tabla explícita y verificable los aliases genealógicos que corresponden inequívocamente a manifiestos canónicos existentes y, en la misma tanda, normalizar las líneas legacy de relaciones principales mal balanceadas antes de volver a ejecutar el gate sobre las 168+ superficies.**

---

## EN · English

### Observed state

The previous iteration left the expanded audit operating on the union of registered surfaces and files actually present on disk. This iteration worked on the systemic cause and on a material batch of declared relations.

### Changes executed

1. `.github/scripts/repair_manifesto_genealogical_links.py` was expanded beyond `Genealogical relation` to also repair `Main relations` and `Root relations`.
2. The repairer resolves explicit and bare Roman identifiers through `manifiestos/CANONICAL_FILENAMES.json`, verifies target existence and links `∞` to its real manifesto.
3. `.github/scripts/audit_manifesto_clickable_relations.py` was expanded to block unlinked Roman identifiers in main/root relations and verify local Markdown targets.
4. The repair workflow produced a material automatic batch across declared relations, including LXIV–LXXII surfaces and mirrors where applicable.
5. Verified Neoaxiom identifiers (`NAX-*` / `C-NAX-*`) are now handled: `NAX-10` targets its dedicated document, while other verified identifiers target the canonical `neoaxiomas/README.md` registry without inventing non-existent anchors.
6. The audit now emits `NEOAXIOM_RELATIONS_NOT_CLICKABLE` when a Neoaxiom identifier presented as navigation remains plain text.

### Material commits in this iteration

- `8eb6492b92e34447f83721aec7d7a94e62751c26` — repair all declared relational surfaces.
- `ace56dcea467ad4ea7bdbc86f129a355e2bf58ba` — gate all declared relational surfaces.
- `7662a9bbc474d8b67742f86be8f35dc916c13d45` — link Neoaxiom identifiers.
- `2f2000b046c7d1c1b367fc5723c74dbdd5a1bc8b` — material automatic repair across ten manifesto surfaces.
- `39563808a52b6fda41fd929adc8ca456f5258105` — gate unlinked Neoaxiom relations.

### Execution evidence

The repair workflow ran the repairer successfully and detected material changes in ten surfaces. The subsequent audit inspected **168 surfaces** and correctly remained at `CLICKABLE_RELATIONS=FAIL`.

The main residual cause is no longer lack of control over main relations. It is **named genealogical targets that are not yet resolved unambiguously**. Recorded examples include `Umbral-X™`, `Integral Protection of Childhood™`, `Sovereignty of Cognitive Time™`, `Against Anti-Humanist Neuromarketing™`, `Neowar™`, `Neodialectical Open Synthesis™`, `Neodialectical Recognition™` and others. Many correspond to existing manifestos and should be added to an explicit alias registry only after their canonical destination is verified. Others, such as `WEB4™`, `Neodialectica Framework™` or compound concepts, may require a canonical surface other than a manifesto and must not be linked by textual similarity.

The run also exposed an inherited anomaly in some legacy `Main relations` lines: historical malformed Markdown starts a link near the beginning and closes it only at the end of the line. Linking inner identifiers does not make that structure valid. It must be normalised without changing doctrine.

### Fixed invariant

```text
DECLARED_RELATION
→ VERIFIED_CANONICAL_TARGET
→ REAL_MARKDOWN_LINK
→ EXISTING_TARGET

NO_UNAMBIGUOUS_TARGET
→ UNRESOLVED_GENEALOGICAL_TARGET
→ NEVER_INVENT_A_LINK
```

A later canonical cross-reference does not repair an originally plain genealogical or main relation.

### Result

**CONTROLLED FAIL.** There is no basis for declaring the relational corpus clean. Controls are now stricter and the material batch reduced plain relations, but unresolved genealogical targets and structurally malformed legacy relation lines remain.

### NEXT_STEP

**Resolve, through an explicit verified alias table, genealogical aliases that map unambiguously to existing canonical manifestos and in the same batch normalise malformed legacy main-relation lines before rerunning the gate across all 168+ surfaces.**
