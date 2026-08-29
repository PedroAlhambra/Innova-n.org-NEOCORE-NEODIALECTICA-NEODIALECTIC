# Reparación relacional de manifiestos · Iteración 04
# Manifesto relational repair · Iteration 04

**Fecha / Date:** 2026-08-29  
**Ámbito / Scope:** repositorio público · corpus de manifiestos legacy + espejos canónicos + ∞ / public repository · legacy manifesto corpus + canonical mirrors + ∞  
**Estado / Status:** **FAIL CONTROLADO / CONTROLLED FAIL** — no se declara PASS global. / no global PASS is declared.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Estado observado

La reparación incremental anterior había mejorado la cobertura de hipervínculos, pero las pasadas automáticas históricas habían dejado dos problemas sistémicos distintos:

1. Markdown relacional malformado o no idempotente —enlaces duplicados, sufijos `](href)` repetidos, enlaces anidados y referencias NAX parcialmente enlazadas— en superficies `Relación genealógica`, `Relaciones principales` y `Relaciones raíz`.
2. El nuevo detector `NESTED_LINK` del auditor era demasiado codicioso y marcaba como anidación cualquier línea válida que contuviera varios enlaces independientes.

### 2. Reparación material

Se añadió un saneador determinista dedicado a las superficies relacionales y se integró en el workflow antes y después del reparador. El objetivo es que la secuencia sea idempotente:

```text
SANITIZE
→ REPAIR_VERIFIED_TARGETS
→ SANITIZE
→ AUDIT
→ COMMIT_IF_MATERIAL
→ FINAL_AUDIT
```

El workflow saneó y volvió a escribir materialmente **18 superficies** en el commit `f77150ba600e38e03644d64bf45b3fa8ed8f51a3`, incluyendo las líneas NAX problemáticas de LXVI, LXIX, LXX, LXXI y LXXII y sus espejos canónicos, además de varias relaciones genealógicas con sufijos duplicados. La inspección posterior de LXIX confirma que `NAX-10` queda como un único enlace válido al archivo público `neoaxiomas/NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md`.

### 3. Endurecimiento de causa raíz

Cambios sistémicos relevantes de esta iteración:

- `7d22fa60d309141c8a65dc5bdfad4b525b94b4fd` — endurecimiento del reparador frente a Markdown legacy malformado.
- `9913208fd73e95bb46d08cb3d9cdc9eed7d812dd` — el auditor pasa a rechazar pseudoenlaces y sintaxis relacional rota.
- `1f0eb4fdf207de388931748bdce5e00259f91597` — nuevo saneador determinista de Markdown relacional.
- `11aa86c327f954d9e0d9c2e24dbee150ef04bfe0` — el workflow ejecuta saneado también después de reparar y antes de auditar.
- `f77150ba600e38e03644d64bf45b3fa8ed8f51a3` — reparación material de 18 superficies.
- `22d32794ece21e4e79788d860ba14eae2b8f55ef` — corrección del falso positivo del detector `NESTED_LINK`; ahora exige anidación local real y no confunde una lista de enlaces independientes con enlaces anidados.

### 4. Evidencia y residuo

La auditoría ejecutada inmediatamente después de `f77150ba...` recorrió **168 superficies** y permaneció correctamente en `CLICKABLE_RELATIONS=FAIL`. Esa ejecución todavía utilizaba el detector `NESTED_LINK` demasiado amplio, por lo que su gran conjunto de `RELATIONAL_MARKDOWN_SYNTAX_FAILURE` no puede tratarse como evidencia de defectos reales; esa causa del propio auditor ha sido corregida en `22d32794...` y se ha solicitado una nueva pasada mediante el workflow endurecido.

Sí permanecen como residuo epistemológicamente válido los objetivos genealógicos para los que no existe todavía una correspondencia canónica única demostrada. Entre los observados están:

- `Neodialectica Framework™`;
- `Neodialéctica™` cuando aparece como concepto genérico sin destino canónico unívoco;
- `Sistema Inmunitario Intelectual Neodialéctico™`;
- `Inteligencia Fractal™`;
- `Lupa Neodialéctica™`;
- `Revisión de Pares Aumentada™` dentro de una formulación compuesta.

No se ha inventado ningún destino para hacer pasar el gate.

### 5. Estado de las invariantes

`MAIN_RELATIONS_NOT_CLICKABLE`: pendiente de nueva medición limpia tras corregir el falso positivo del auditor.  
`GENEALOGICAL_NAVIGATION_FAILURE`: existen objetivos no resueltos y verificables; bloquea PASS.  
`OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`: sin nuevo fallo material demostrado en esta iteración.  
`CANONICAL_CROSSREF_BLOCK_MISSING`: sin nuevo fallo material demostrado en esta iteración.  
`RELATIONAL_MARKDOWN_SYNTAX_FAILURE`: saneador implantado; la medición anterior estaba contaminada por un falso positivo del propio auditor y debe recalcularse.

### PASO_SIGUIENTE

**Recoger la nueva auditoría de 168 superficies con el detector `NESTED_LINK` corregido y, sobre ese residuo limpio, resolver únicamente los objetivos genealógicos que puedan demostrarse contra un destino canónico único, manteniendo `UNRESOLVED_GENEALOGICAL_TARGET` para los demás.**

---

## EN · English

### 1. Observed state

The previous incremental repair improved hyperlink coverage, but historical automated passes had left two distinct systemic problems:

1. malformed or non-idempotent relational Markdown — duplicated links, repeated `](href)` suffixes, nested links and partially linked NAX references — inside `Genealogical relation`, `Main relations` and `Root relations` surfaces;
2. the newly added auditor `NESTED_LINK` detector was overly greedy and treated any valid line containing several independent links as if those links were nested.

### 2. Material repair

A dedicated deterministic sanitizer was added and integrated into the workflow both before and after the verified-target repairer. The intended sequence is now idempotent:

```text
SANITIZE
→ REPAIR_VERIFIED_TARGETS
→ SANITIZE
→ AUDIT
→ COMMIT_IF_MATERIAL
→ FINAL_AUDIT
```

The workflow materially sanitized and rewrote **18 surfaces** in commit `f77150ba600e38e03644d64bf45b3fa8ed8f51a3`, including problematic NAX lines in LXVI, LXIX, LXX, LXXI and LXXII and their canonical mirrors, together with several genealogical relations carrying duplicated suffixes. A subsequent inspection of LXIX confirms that `NAX-10` is now a single valid link to the public `neoaxiomas/NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md` file.

### 3. Root-cause hardening

Relevant systemic changes in this iteration:

- `7d22fa60d309141c8a65dc5bdfad4b525b94b4fd` — repairer hardened against malformed legacy Markdown;
- `9913208fd73e95bb46d08cb3d9cdc9eed7d812dd` — auditor now rejects pseudo-links and broken relational syntax;
- `1f0eb4fdf207de388931748bdce5e00259f91597` — new deterministic relational-Markdown sanitizer;
- `11aa86c327f954d9e0d9c2e24dbee150ef04bfe0` — workflow sanitizes again after repair and before audit;
- `f77150ba600e38e03644d64bf45b3fa8ed8f51a3` — material repair of 18 surfaces;
- `22d32794ece21e4e79788d860ba14eae2b8f55ef` — false-positive `NESTED_LINK` detection fixed so that local real nesting is required and independent links on the same line are not conflated with nested links.

### 4. Evidence and residue

The audit executed immediately after `f77150ba...` traversed **168 surfaces** and correctly remained `CLICKABLE_RELATIONS=FAIL`. That run still used the overly broad `NESTED_LINK` detector, so its large set of `RELATIONAL_MARKDOWN_SYNTAX_FAILURE` findings cannot be treated as evidence of real defects. That auditor-side cause has been corrected in `22d32794...`, and a fresh pass has been requested through the hardened workflow.

The epistemically valid residue remains the set of genealogical targets for which no unique canonical correspondence has yet been demonstrated, including `Neodialectica Framework™`, generic `Neodialéctica™`, `Sistema Inmunitario Intelectual Neodialéctico™`, `Inteligencia Fractal™`, `Lupa Neodialéctica™`, and `Revisión de Pares Aumentada™` in a compound formulation.

No destination has been invented merely to make the gate pass.

### 5. Invariant status

`MAIN_RELATIONS_NOT_CLICKABLE`: awaits a clean new measurement after correcting the auditor false positive.  
`GENEALOGICAL_NAVIGATION_FAILURE`: verified unresolved targets remain and block PASS.  
`OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`: no new material failure demonstrated in this iteration.  
`CANONICAL_CROSSREF_BLOCK_MISSING`: no new material failure demonstrated in this iteration.  
`RELATIONAL_MARKDOWN_SYNTAX_FAILURE`: sanitizer implemented; the previous measurement was contaminated by an auditor false positive and must be recalculated.

### NEXT_STEP

**Collect the fresh 168-surface audit with corrected `NESTED_LINK` detection and, from that clean residue, resolve only genealogical targets that can be demonstrated against one unique canonical destination, preserving `UNRESOLVED_GENEALOGICAL_TARGET` for all others.**
