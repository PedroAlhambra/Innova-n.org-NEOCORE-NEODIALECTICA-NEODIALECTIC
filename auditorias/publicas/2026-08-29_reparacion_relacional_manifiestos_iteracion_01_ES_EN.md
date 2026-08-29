# Reparación relacional de manifiestos · Iteración 01
# Manifesto relational repair · Iteration 01

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

**Fecha:** 2026-08-29  
**Ámbito:** repositorio público · manifiestos finitos, espejos canónicos y Manifiesto ∞  
**Estado:** **FAIL ABIERTO — reparación material en curso**

### Problema observado

Se confirmó una regresión sistémica: varias cabeceras `Relación genealógica / Genealogical relation` y `Relaciones principales / Main relations` presentaban conceptos o manifiestos relacionados como texto plano. Que la misma relación apareciera enlazada posteriormente en `Referencias cruzadas canónicas` no hacía navegable la declaración original.

El caso de referencia XLVII mostraba en texto plano Neoego™, Misericordia Universal Recíproca™, Neofraternidad™, Multidimensionalidad Neodialéctica™, Cerrar la Herida™, Persistencia de la Memoria™ e Inteligencia Humana Expandida™.

### Acciones ejecutadas

1. Se endureció `.github/scripts/audit_manifesto_clickable_relations.py` para auditar tanto superficies legacy como espejos canónicos y Manifiesto ∞, y posteriormente se amplió a la unión entre `CANONICAL_FILENAMES.json` y los manifiestos realmente presentes en disco para que un registro desfasado no pueda ocultar una pieza nueva.
2. Se creó `.github/scripts/repair_manifesto_genealogical_links.py`, reparador conservador que sólo enlaza destinos verificados contra el mapa canónico y registra lo no resoluble como `UNRESOLVED_GENEALOGICAL_TARGET` en lugar de inventar destinos.
3. Se creó `.github/workflows/repair-manifesto-genealogical-links.yml` para aplicar reparaciones verificadas y volver a ejecutar el auditor.
4. La primera tanda material produjo el commit `04826e9b2366f09f79072f530c93aabfe5ad3d39` con 24 superficies reparadas. XLVII quedó reparado tanto en su ruta legacy como en su espejo canónico.
5. Una segunda ampliación permitió enlazar referencias genealógicas explícitas del tipo `ROMANO · Nombre™` mediante `CANONICAL_FILENAMES.json`; produjo el commit `6bf9d21c56b7e03f9042b04d6ed3c4b16f0693a4` con 16 superficies adicionales modificadas.
6. Durante esa segunda tanda se detectó una regresión del propio reparador: algunos nombres que ya estaban enlazados podían quedar envueltos por un segundo enlace Markdown. Se corrigió la causa raíz y se añadió normalización defensiva; el commit de reparación resultante fue `34012bdcda522c4ea6c3328e4caa83d77b9c7ea7`, que eliminó los enlaces anidados detectados.
7. Se creó `.github/workflows/audit-manifesto-clickable-relations.yml`, gate de sólo lectura que ejecuta la auditoría en cambios de manifiestos tanto por `push` a `main` como por `pull_request`.
8. Se creó una reconciliación automática de frontera. La ejecución confirmó que el último manifiesto finito real es LXXXV, añadió los marcadores del bloque de referencias cruzadas al Manifiesto LXXXV y corrigió `manifiestos/README.md` de LXXXIV/84 a LXXXV/85. Commit generado: `eb338c1e`.

### Evidencia actual

La auditoría ampliada cubre ahora **168 superficies**. El corpus **no está en PASS**. Permanecen `GENEALOGICAL_NAVIGATION_FAILURE` en varias cabeceras cuyo destino todavía debe resolverse de forma inequívoca, y `MAIN_RELATIONS_NOT_CLICKABLE` en varios espejos canónicos, especialmente LXIV–LXXII. No se detectó razón válida para rebajar el gate: esos fallos son accionables y deben repararse.

La regla sistémica vigente es:

```text
RELACION_DECLARADA_COMO_NAVEGACION
→ DESTINO_CANONICO_VERIFICADO
→ HIPERVINCULO_MARKDOWN_REAL
→ DESTINO_EXISTENTE
→ AUDITORIA

SIN_DESTINO_UNIVOCO
→ UNRESOLVED_GENEALOGICAL_TARGET
→ NO_INVENTAR_ENLACE
```

### PASO_SIGUIENTE

Resolver el siguiente lote de `GENEALOGICAL_NAVIGATION_FAILURE` contra destinos canónicos verificables y, en paralelo dentro de la misma reparación sistémica, convertir las `Relaciones principales` planas de LXIV–LXXII en enlaces reales sin alterar contenido doctrinal.

---

## EN · English

**Date:** 2026-08-29  
**Scope:** public repository · finite manifestos, canonical mirrors and Manifesto ∞  
**Status:** **OPEN FAIL — material repair in progress**

### Observed problem

A systemic regression was confirmed: several `Relación genealógica / Genealogical relation` and `Relaciones principales / Main relations` headers exposed related concepts or manifestos as plain text. A later duplicate link inside `Canonical cross-references` did not make the original declaration navigable.

The XLVII reference case exposed Neoego™, Universal Reciprocal Mercy™, Neofraternity™, Neodialectical Multidimensionality™, Closing the Wound™, Persistence of Memory™ and Expanded Human Intelligence™ as plain text.

### Actions executed

1. `.github/scripts/audit_manifesto_clickable_relations.py` was hardened to audit both legacy surfaces and canonical mirrors plus Manifesto ∞, then expanded to the union of `CANONICAL_FILENAMES.json` and manifestos actually present on disk so a stale registry cannot hide a new piece.
2. `.github/scripts/repair_manifesto_genealogical_links.py` was created as a conservative repairer: it links only targets verified against the canonical map and reports unresolved names as `UNRESOLVED_GENEALOGICAL_TARGET` instead of inventing destinations.
3. `.github/workflows/repair-manifesto-genealogical-links.yml` was created to apply verified repairs and rerun the auditor.
4. The first material batch produced commit `04826e9b2366f09f79072f530c93aabfe5ad3d39`, repairing 24 surfaces. XLVII was repaired in both its legacy route and canonical mirror.
5. A second extension added verified linking for explicit `ROMAN · Name™` genealogical references through `CANONICAL_FILENAMES.json`; it produced commit `6bf9d21c56b7e03f9042b04d6ed3c4b16f0693a4`, modifying 16 additional surfaces.
6. That second batch exposed a regression in the repairer itself: some already-linked names could become wrapped by a second Markdown link. The root cause was fixed and defensive normalisation added; resulting repair commit `34012bdcda522c4ea6c3328e4caa83d77b9c7ea7` removed the detected nested links.
7. `.github/workflows/audit-manifesto-clickable-relations.yml` was created as a read-only gate running on manifesto changes in both `main` pushes and pull requests.
8. Automatic frontier reconciliation was added. Its run confirmed that the real latest finite manifesto is LXXXV, added canonical cross-reference markers to Manifesto LXXXV and corrected `manifiestos/README.md` from LXXXIV/84 to LXXXV/85. Generated commit: `eb338c1e`.

### Current evidence

The expanded audit now covers **168 surfaces**. The corpus is **not in PASS**. Several headers still contain `GENEALOGICAL_NAVIGATION_FAILURE` whose targets must be resolved unambiguously, while multiple canonical mirrors—especially LXIV–LXXII—still contain `MAIN_RELATIONS_NOT_CLICKABLE`. There is no valid reason to weaken the gate: these are actionable defects and must be repaired.

Current systemic rule:

```text
RELATION_DECLARED_AS_NAVIGATION
→ VERIFIED_CANONICAL_TARGET
→ REAL_MARKDOWN_LINK
→ EXISTING_DESTINATION
→ AUDIT

NO_UNAMBIGUOUS_TARGET
→ UNRESOLVED_GENEALOGICAL_TARGET
→ DO_NOT_INVENT_LINK
```

### NEXT_STEP

Resolve the next batch of `GENEALOGICAL_NAVIGATION_FAILURE` against verified canonical destinations and, within the same systemic repair, turn the plain `Main relations` of LXIV–LXXII into real links without altering doctrinal content.
