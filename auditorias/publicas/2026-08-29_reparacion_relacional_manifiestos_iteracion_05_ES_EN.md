# Reparación relacional de manifiestos · Iteración 05
# Manifesto relational repair · Iteration 05

**Fecha / Date:** 2026-08-29  
**Ámbito / Scope:** repositorio público · corpus legacy + espejos canónicos + ∞ / public repository · legacy corpus + canonical mirrors + ∞  
**Estado / Status:** **PASS RELACIONAL VERIFICADO / VERIFIED RELATIONAL PASS**

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Cierre del residuo genealógico

La iteración anterior había reducido el fallo a cinco conceptos genealógicos sin destino explícitamente resuelto. Esta pasada investigó cada uno contra sus fuentes públicas y fijó únicamente destinos demostrables:

- `Neodialectica Framework™` → `README.md`, portada pública que define y presenta el Framework / Network;
- `Neodialéctica™` → Manifiesto IV · `manifiestos/canonicos/IV_neodialectica_bien_comun_ES_EN.md`, manifiesto fundacional de la Neodialéctica y el Bien Común;
- `Sistema Inmunitario Intelectual Neodialéctico™` → Manifiesto XX · `manifiestos/canonicos/XX_defensa_intelectual_neodialectica_umbral_x_ES_EN.md`, donde el sistema se nombra y define explícitamente;
- `Inteligencia Fractal™` → Manifiesto V · `manifiestos/canonicos/V_simbiosis_humano_ia_ES_EN.md`, cuya versión vigente contiene su definición explícita;
- `Lupa Neodialéctica™` → `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md`, fuente pública donde se clasifica y aplica explícitamente la Lupa y a la que el Manifiesto XLVIII remite genealógicamente mediante la metáfora de la mini placa de Petri.

No se utilizó inferencia difusa por título ni se fabricó ninguna superficie inexistente.

### 2. Reparación sistémica

Commit de causa raíz:

`4285712d5d21cae5356fe6753b88c976ad2678be` — el reparador admite ahora dos clases explícitas de destino verificado:

1. aliases hacia manifiestos canónicos resueltos por `CANONICAL_FILENAMES.json`;
2. aliases directos hacia una fuente pública concreta, cuya existencia debe verificarse antes de generar el enlace.

Esto permite enlazar conceptos genealógicos cuya fuente canónica no es un manifiesto sin degradar la regla `NO_FUZZY_INFERENCE`.

El workflow de reparación produjo después:

`7fd8e7750d964c4bb6bda0f42047080b07e47f63` — reparación material de las 10 superficies legacy/canónicas residuales.

### 3. Evidencia de cierre

El workflow `Repair manifesto genealogical links` terminó con `success`. Sus etapas de saneado previo, reparación de destinos verificados, saneado posterior, auditoría previa, commit y **auditoría final sobre el árbol resultante** terminaron todas con `success`.

El gate final ejecutó `.github/scripts/audit_manifesto_clickable_relations.py` después de materializar la reparación. Por tanto, en el árbol resultante no quedan fallos bloqueantes detectados por ese auditor en las categorías exigidas por esta campaña:

```text
MAIN_RELATIONS_NOT_CLICKABLE = PASS
GENEALOGICAL_NAVIGATION_FAILURE = PASS
OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE = PASS
CANONICAL_CROSSREF_BLOCK_MISSING = PASS
RELATIONAL_MARKDOWN_SYNTAX_FAILURE = PASS
NEOAXIOM_RELATIONS_NOT_CLICKABLE = PASS
```

La frontera del índice permanece reconciliada en **85 manifiestos finitos bilingües · I–LXXXV + Manifiesto ∞**.

### 4. Regla preventiva vigente

La política resultante es bloqueante:

```text
RELACIÓN DECLARADA COMO NAVEGACIÓN
→ DESTINO PÚBLICO VERIFICADO
→ HIPERVÍNCULO MARKDOWN REAL EN EL PUNTO DE DECLARACIÓN
→ AUDITORÍA

DESTINO NO INEQUÍVOCO
→ UNRESOLVED_GENEALOGICAL_TARGET
→ NO INVENTAR ENLACE
→ NO PASS GLOBAL
```

Un vínculo duplicado en el bloque final de referencias nunca sustituye la navegabilidad en `Relación genealógica / Genealogical relation` o `Relaciones principales / Main relations`.

### RESULTADO

**PASS RELACIONAL VERIFICADO.** El objetivo específico de este bucle queda cumplido sobre el estado público actual.

---

## EN · English

### 1. Closing the genealogical residue

The previous iteration had reduced the failure to five genealogical concepts without an explicitly resolved destination. This pass investigated each one against its public sources and fixed only demonstrable targets:

- `Neodialectica Framework™` → `README.md`, the public front page that defines and presents the Framework / Network;
- `Neodialéctica™` → Manifesto IV · `manifiestos/canonicos/IV_neodialectica_bien_comun_ES_EN.md`, the foundational manifesto of Neodialectics and the Common Good;
- `Sistema Inmunitario Intelectual Neodialéctico™` → Manifesto XX · `manifiestos/canonicos/XX_defensa_intelectual_neodialectica_umbral_x_ES_EN.md`, where the system is explicitly named and defined;
- `Inteligencia Fractal™` → Manifesto V · `manifiestos/canonicos/V_simbiosis_humano_ia_ES_EN.md`, whose current text explicitly defines it;
- `Lupa Neodialéctica™` → `analisis/publicos/2026-07-13-religion-identidad-dogma-conciencia-neodialectica_ES_EN.md`, the public source where the Lens is explicitly classified and applied and to which Manifesto XLVIII genealogically points through the mini-Petri-dish metaphor.

No fuzzy title inference was used and no nonexistent surface was fabricated.

### 2. Systemic repair

Root-cause commit:

`4285712d5d21cae5356fe6753b88c976ad2678be` — the repairer now supports two explicit classes of verified destination:

1. aliases to canonical manifestos resolved through `CANONICAL_FILENAMES.json`;
2. direct aliases to a concrete public source whose existence must be verified before a link is generated.

This permits genealogical concepts whose canonical source is not a manifesto to remain navigable without weakening `NO_FUZZY_INFERENCE`.

The repair workflow then produced:

`7fd8e7750d964c4bb6bda0f42047080b07e47f63` — material repair of the 10 residual legacy/canonical surfaces.

### 3. Closure evidence

The `Repair manifesto genealogical links` workflow completed with `success`. Its pre-sanitisation, verified-target repair, post-sanitisation, pre-commit audit, commit and **final audit on the resulting tree** all completed successfully.

The final gate executed `.github/scripts/audit_manifesto_clickable_relations.py` after materialising the repair. Therefore the resulting tree contains no blocking failures detected by that auditor in the categories required by this campaign:

```text
MAIN_RELATIONS_NOT_CLICKABLE = PASS
GENEALOGICAL_NAVIGATION_FAILURE = PASS
OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE = PASS
CANONICAL_CROSSREF_BLOCK_MISSING = PASS
RELATIONAL_MARKDOWN_SYNTAX_FAILURE = PASS
NEOAXIOM_RELATIONS_NOT_CLICKABLE = PASS
```

The index frontier remains reconciled at **85 finite bilingual manifestos · I–LXXXV + Manifesto ∞**.

### 4. Preventive rule now in force

The resulting policy is blocking:

```text
RELATION DECLARED AS NAVIGATION
→ VERIFIED PUBLIC DESTINATION
→ REAL MARKDOWN HYPERLINK AT THE POINT OF DECLARATION
→ AUDIT

DESTINATION NOT UNAMBIGUOUS
→ UNRESOLVED_GENEALOGICAL_TARGET
→ DO NOT INVENT A LINK
→ NO GLOBAL PASS
```

A duplicate link in the final cross-reference block never substitutes navigability inside `Relación genealógica / Genealogical relation` or `Relaciones principales / Main relations`.

### RESULT

**VERIFIED RELATIONAL PASS.** The specific objective of this loop is complete for the current public state.
