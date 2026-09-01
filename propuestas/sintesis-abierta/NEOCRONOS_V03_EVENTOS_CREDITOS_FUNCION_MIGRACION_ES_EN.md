# Recuperación genealógica / Genealogical recovery

**Recuperado / Recovered:** 2026-09-01 desde/from `sintesis-aportes-tokenizados` · blob histórico/historical `6e601153a723821fe50e72be8d4cee37cf7ec12f`.  
**Estado actual / Current state:** `HISTORICAL_RECOVERED / OPEN_SYNTHESIS_INPUT / NOT_CURRENT_RUNTIME`.  
**Regla vigente / Current rule:** conservar `NC-EVT-* ≠ NC-CR-*`; toda implementación actual debe aplicar además aporte auditable, privacidad proporcional, `MEDICIÓN ≠ VALORACIÓN`, `TRAZA ≠ VALIDACIÓN` y los deltas posteriores. La versión vigente de NEOCore™ se resuelve exclusivamente desde [`versiones/README.md`](../../versiones/README.md). / Preserve `NC-EVT-* ≠ NC-CR-*`; current implementations must additionally enforce auditable contribution, proportional privacy, `MEASUREMENT ≠ VALUATION`, `TRACE ≠ VALIDATION`, and later deltas. Current NEOCore™ version is resolved only from [`versiones/README.md`](../../versiones/README.md).

---

# ES · NeoCronos™ v0.3 · Migración a Eventos y Créditos de Función
# EN · NeoCronos™ v0.3 · Migration to Events and Role Credits

**Fecha / Date:** 2026-08-12  
**Estado / Status:** DELTA DE IMPLEMENTACIÓN EN RAMA · BRANCH IMPLEMENTATION DELTA  
**Rama / Branch:** `sintesis-aportes-tokenizados`  
**Relación / Relation:** [#141](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/141) · [#142](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/142)

---

# ES · Castellano

## 1. Motivo

El modelo plano inicial confundía tres cosas distintas:

```text
PROCEDENCIA DE LA SEÑAL
AUTORÍA DE LA RELACIÓN
AUTORÍA / OPERACIÓN DEL DELTA
```

La corrección v0.3 separa el **evento completo** de los **créditos de función**.

## 2. Regla

```text
NC-EVT-* = EVENTO
NC-CR-*  = CRÉDITO DE FUNCIÓN
```

Una misma persona puede ocupar varias funciones y varias personas pueden participar en un mismo evento.

Funciones actuales:

- source_originator;
- discoverer;
- receiver;
- manual_ingestor;
- curator;
- relation_author;
- contradiction_author;
- synthesis_operator;
- delta_author;
- implementation_operator;
- fixation_operator.

## 3. Fase manual

Mientras WEB4™ no permita contribución directa completa, Neo0™ realiza manualmente trabajo de recepción/descubrimiento, selección, ingesta, contextualización, relación, contraste y fijación. Ese trabajo recibe crédito cuando puede demostrarse.

```text
CRÉDITO NEO0™
≠ IMPUESTO DEL FUNDADOR
≠ APROPIACIÓN DE LA IDEA EXTERNA
```

## 4. Caso de prueba · Asilomar

La publicación de José Luis Casal es procedencia de la señal. Neo0™ la descubre en LinkedIn, la introduce manualmente, establece la relación Asilomar↔marco y produce/fija el delta relacional.

El antiguo `NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR` queda `deprecated-misattribution`.

El evento correcto es `NC-EVT-2026-0005`, con:

- `NC-CR-2026-0005-A` · Casal · `source_originator`;
- `NC-CR-2026-0005-B` · Neo0™ · descubrimiento, ingesta, curación, relación, síntesis, delta y fijación.

RADAR-Π™ queda como un evento posterior separado.

## 5. No se reescribe el pasado

Los identificadores anteriores se conservan como historial de migración. La corrección no borra el error: documenta qué se atribuyó, por qué era insuficiente y cuál es la relación vigente.

---

# EN · English

## 1. Reason

The initial flat model conflated three distinct things:

```text
SIGNAL PROVENANCE
AUTHORSHIP OF THE RELATION
AUTHORSHIP / OPERATION OF THE DELTA
```

The v0.3 correction separates the **complete event** from **role credits**.

## 2. Rule

```text
NC-EVT-* = EVENT
NC-CR-*  = ROLE CREDIT
```

One person may occupy several functions and several people may participate in one event.

Current functions:

- source_originator;
- discoverer;
- receiver;
- manual_ingestor;
- curator;
- relation_author;
- contradiction_author;
- synthesis_operator;
- delta_author;
- implementation_operator;
- fixation_operator.

## 3. Manual phase

While WEB4™ does not support complete direct contribution, Neo0™ manually performs reception/discovery, selection, ingestion, contextualisation, relation, scrutiny and fixation work. That work receives credit when it can be demonstrated.

```text
NEO0™ CREDIT
≠ FOUNDER TAX
≠ APPROPRIATION OF THE EXTERNAL IDEA
```

## 4. Test case · Asilomar

José Luis Casal's publication is signal provenance. Neo0™ discovers it on LinkedIn, manually ingests it, establishes the Asilomar↔framework relation and produces/fixes the relational delta.

The former `NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR` is `deprecated-misattribution`.

The correct event is `NC-EVT-2026-0005`, with:

- `NC-CR-2026-0005-A` · Casal · `source_originator`;
- `NC-CR-2026-0005-B` · Neo0™ · discovery, ingestion, curation, relation, synthesis, delta and fixation.

RADAR-Π™ remains a separate later event.

## 5. The past is not rewritten

Previous identifiers are preserved as migration history. The correction does not erase the error: it documents what was attributed, why it was insufficient and which relation is current.
