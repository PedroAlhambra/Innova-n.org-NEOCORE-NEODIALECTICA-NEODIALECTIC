# Reparación relacional de manifiestos · Iteración 04
# Manifesto relational repair · Iteration 04

**Fecha / Date:** 2026-08-29  
**Ámbito / Scope:** repositorio público · corpus legacy + espejos canónicos + ∞ / public repository · legacy corpus + canonical mirrors + ∞  
**Estado / Status:** **FAIL CONTROLADO / CONTROLLED FAIL** — no se declara PASS global. / no global PASS is declared.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Hallazgo y reparación material

Las pasadas automáticas anteriores habían dejado Markdown relacional no idempotente: enlaces duplicados, sufijos `](href)` repetidos, pseudoenlaces anidados y referencias NAX parcialmente enlazadas. Se añadió un saneador determinista y se integró antes y después del reparador:

```text
SANITIZE → REPAIR_VERIFIED_TARGETS → SANITIZE → AUDIT → COMMIT_IF_MATERIAL → FINAL_AUDIT
```

El workflow saneó materialmente **18 superficies** en `f77150ba600e38e03644d64bf45b3fa8ed8f51a3`, incluyendo LXVI, LXIX, LXX, LXXI y LXXII y sus espejos canónicos. La inspección posterior confirma, por ejemplo, que `NAX-10` en LXIX queda como un único hipervínculo válido al archivo público `neoaxiomas/NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md`.

### 2. Causa raíz endurecida

- `7d22fa60d309141c8a65dc5bdfad4b525b94b4fd` — reparador endurecido frente a Markdown legacy malformado.
- `9913208fd73e95bb46d08cb3d9cdc9eed7d812dd` — auditor capaz de rechazar pseudoenlaces/sintaxis relacional rota.
- `1f0eb4fdf207de388931748bdce5e00259f91597` — saneador determinista de Markdown relacional.
- `11aa86c327f954d9e0d9c2e24dbee150ef04bfe0` — saneado también después de reparar y antes de auditar.
- `f77150ba600e38e03644d64bf45b3fa8ed8f51a3` — reparación material de 18 superficies.
- `22d32794ece21e4e79788d860ba14eae2b8f55ef` — corrección de un falso positivo del propio auditor: `NESTED_LINK` exige ahora anidación local real y no confunde varios enlaces independientes de una misma línea.

### 3. Auditoría fresca

Tras corregir el falso positivo se ejecutó de nuevo el gate sobre **168 superficies**. Resultado demostrado:

```text
CLICKABLE_RELATIONS=FAIL
MANIFEST_SURFACES_AUDITED=168
```

La nueva pasada ya **no reporta** `RELATIONAL_MARKDOWN_SYNTAX_FAILURE`, `MAIN_RELATIONS_NOT_CLICKABLE`, `NEOAXIOM_RELATIONS_NOT_CLICKABLE`, `OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE` ni ausencia de bloque canónico de referencias en el residuo mostrado. El fallo queda reducido a **10 superficies legacy/canónicas** con `GENEALOGICAL_NAVIGATION_FAILURE` por conceptos cuyo destino canónico único todavía no está demostrado:

- XXXIX legacy + canónico: `Neodialectica Framework™`;
- XLV legacy + canónico: `Neodialéctica™` y `Sistema Inmunitario Intelectual Neodialéctico™`;
- XLVIII legacy + canónico: `Inteligencia Fractal™` y `Lupa Neodialéctica™`;
- XLIX legacy + canónico: `Neodialéctica™`;
- L legacy + canónico: `Inteligencia Fractal™`.

`Revisión de Pares Aumentada™`, que había aparecido anteriormente como residuo producido por el parser, **ya no aparece en la auditoría limpia** y no se conserva artificialmente como fallo.

No se ha inventado ningún destino para forzar PASS.

### 4. Estado de invariantes

`MAIN_RELATIONS_NOT_CLICKABLE`: sin fallo en la auditoría fresca.  
`RELATIONAL_MARKDOWN_SYNTAX_FAILURE`: sin fallo en la auditoría fresca.  
`NEOAXIOM_RELATIONS_NOT_CLICKABLE`: sin fallo en la auditoría fresca.  
`OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`: sin fallo en la auditoría fresca.  
`CANONICAL_CROSSREF_BLOCK_MISSING`: sin fallo en la auditoría fresca.  
`GENEALOGICAL_NAVIGATION_FAILURE`: **FAIL residual; bloquea PASS global.**

### PASO_SIGUIENTE

**Investigar exclusivamente los cinco conceptos genealógicos residuales contra el corpus y `CANONICAL_FILENAMES.json`; enlazar sólo los que tengan un destino público canónico único demostrable y conservar como `UNRESOLVED_GENEALOGICAL_TARGET` cualquier concepto sin correspondencia inequívoca.**

---

## EN · English

### 1. Finding and material repair

Previous automated passes had left non-idempotent relational Markdown: duplicated links, repeated `](href)` suffixes, nested pseudo-links and partially linked NAX references. A deterministic sanitizer was added and integrated both before and after the repairer:

```text
SANITIZE → REPAIR_VERIFIED_TARGETS → SANITIZE → AUDIT → COMMIT_IF_MATERIAL → FINAL_AUDIT
```

The workflow materially sanitized **18 surfaces** in `f77150ba600e38e03644d64bf45b3fa8ed8f51a3`, including LXVI, LXIX, LXX, LXXI and LXXII and their canonical mirrors. Subsequent inspection confirms, for example, that `NAX-10` in LXIX is now one valid hyperlink to the public `neoaxiomas/NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md` file.

### 2. Root-cause hardening

- `7d22fa60d309141c8a65dc5bdfad4b525b94b4fd` — repairer hardened against malformed legacy Markdown.
- `9913208fd73e95bb46d08cb3d9cdc9eed7d812dd` — auditor hardened against pseudo-links and broken relational syntax.
- `1f0eb4fdf207de388931748bdce5e00259f91597` — deterministic relational-Markdown sanitizer.
- `11aa86c327f954d9e0d9c2e24dbee150ef04bfe0` — sanitize again after repair and before audit.
- `f77150ba600e38e03644d64bf45b3fa8ed8f51a3` — material repair of 18 surfaces.
- `22d32794ece21e4e79788d860ba14eae2b8f55ef` — auditor false positive fixed: `NESTED_LINK` now requires actual local nesting rather than mistaking independent links on the same line for nesting.

### 3. Fresh audit

After fixing the false positive, the gate was rerun across **168 surfaces**. Demonstrated result:

```text
CLICKABLE_RELATIONS=FAIL
MANIFEST_SURFACES_AUDITED=168
```

The fresh run no longer reports `RELATIONAL_MARKDOWN_SYNTAX_FAILURE`, `MAIN_RELATIONS_NOT_CLICKABLE`, `NEOAXIOM_RELATIONS_NOT_CLICKABLE`, `OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`, or missing canonical cross-reference blocks in the displayed residue. The failure is reduced to **10 legacy/canonical surfaces** carrying `GENEALOGICAL_NAVIGATION_FAILURE` for concepts whose one unique canonical destination has not yet been demonstrated:

- XXXIX legacy + canonical: `Neodialectica Framework™`;
- XLV legacy + canonical: `Neodialéctica™` and `Sistema Inmunitario Intelectual Neodialéctico™`;
- XLVIII legacy + canonical: `Inteligencia Fractal™` and `Lupa Neodialéctica™`;
- XLIX legacy + canonical: `Neodialéctica™`;
- L legacy + canonical: `Inteligencia Fractal™`.

`Revisión de Pares Aumentada™`, previously surfaced by a parser artefact, **does not appear in the clean audit** and is not artificially retained as a failure.

No destination has been invented merely to force PASS.

### 4. Invariant status

`MAIN_RELATIONS_NOT_CLICKABLE`: no failure in the fresh audit.  
`RELATIONAL_MARKDOWN_SYNTAX_FAILURE`: no failure in the fresh audit.  
`NEOAXIOM_RELATIONS_NOT_CLICKABLE`: no failure in the fresh audit.  
`OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE`: no failure in the fresh audit.  
`CANONICAL_CROSSREF_BLOCK_MISSING`: no failure in the fresh audit.  
`GENEALOGICAL_NAVIGATION_FAILURE`: **residual FAIL; blocks global PASS.**

### NEXT_STEP

**Investigate only the five residual genealogical concepts against the corpus and `CANONICAL_FILENAMES.json`; link only those with one demonstrable public canonical destination and preserve `UNRESOLVED_GENEALOGICAL_TARGET` for every concept lacking an unambiguous correspondence.**
