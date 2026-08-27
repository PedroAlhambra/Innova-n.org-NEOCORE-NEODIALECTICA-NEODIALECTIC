# NEOCore™ 7.3.2 · Política de Referencia Única de Versión
# NEOCore™ 7.3.2 · Single Version Reference Policy

**Fecha / Date:** 2026-08-27  
**Estado / Status:** CANON ABIERTO · CANÓNICO Y REABRIBLE / OPEN CANON · CANONICAL AND REOPENABLE  
**Naturaleza / Nature:** PATCH documental y de gobernanza del versionado / documentary and version-governance PATCH  
**Versión base / Base version:** 7.3

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Motivo

Replicar el número de versión vigente en manifiestos, Síntesis, Issues, Wiki, especificaciones y páginas intermedias obliga a modificar demasiadas superficies con cada evolución y aumenta la probabilidad de estados contradictorios.

7.3.2 corrige esa arquitectura documental.

## 2. Regla canónica

La versión vigente se consulta en [`versiones/README.md`](./README.md). Las superficies intermedias enlazan a esa fuente y no replican el número actual salvo necesidad material.

```text
UNA FUENTE CURRENT_VERSION
+ HISTÓRICO EXPLÍCITO
+ PROCEDENCIA INMUTABLE
= MENOS DUPLICACIÓN + MENOS FLECOS
```

## 3. Excepciones protegidas

No se elimina ni actualiza mecánicamente una versión cuando forma parte del significado del documento:

- `introduced_in` / versión de introducción;
- versión de origen de un protocolo o mecanismo;
- snapshot;
- compatibilidad;
- transición histórica;
- auditoría sobre un estado concreto;
- documento específico de una versión.

Una mención `7.3-CANDIDATE` que documenta realmente una fase pre-canónica puede conservarse como historia. Una mención que pretendía indicar «versión vigente» debe sustituirse por un enlace a la fuente actual.

## 4. Efecto sobre 7.3

7.3.2 **no revierte, invalida ni sustituye conceptualmente** la Capa de Autosíntesis Recursiva™ fijada en 7.3. La hereda y corrige cómo se propaga su estado documental.

Los mecanismos cuya procedencia sea 7.3 mantienen esa procedencia.

## 5. Regla para automatismos

Los scripts, workflows, WEB4 y bucles internos deben resolver el estado vigente desde la fuente canónica y evitar introducir números dinámicos en documentos intermedios.

Un guard puede marcar como defecto una referencia a `CURRENT_VERSION` fuera de una superficie permitida, pero debe disponer de excepciones explícitas para genealogía y compatibilidad.

---

# EN · English

## 1. Motivation

Duplicating the current version number across manifestos, syntheses, Issues, Wiki pages, specifications and intermediate documents forces too many surfaces to change with every evolution and increases the likelihood of contradictory states.

7.3.2 corrects that documentary architecture.

## 2. Canonical rule

The current version is read from [`versiones/README.md`](./README.md). Intermediate surfaces link to that source and do not duplicate the current number unless it is materially necessary.

```text
ONE CURRENT_VERSION SOURCE
+ EXPLICIT HISTORY
+ IMMUTABLE PROVENANCE
= LESS DUPLICATION + FEWER LOOSE ENDS
```

## 3. Protected exceptions

A version is not removed or mechanically updated when it is part of the document's meaning:

- `introduced_in` / introduction version;
- origin version of a protocol or mechanism;
- snapshot;
- compatibility;
- historical transition;
- audit of a specific state;
- version-specific document.

A `7.3-CANDIDATE` mention that genuinely records a pre-canonical phase may remain as history. A mention intended merely to state “current version” must be replaced by a link to the current source.

## 4. Effect on 7.3

7.3.2 **does not reverse, invalidate or conceptually replace** the Recursive Self-Synthesis Layer™ fixed in 7.3. It inherits it and corrects how its documentary state is propagated.

Mechanisms whose provenance is 7.3 retain that provenance.

## 5. Automation rule

Scripts, workflows, WEB4 and internal loops must resolve current state from the canonical source and avoid introducing dynamic version numbers into intermediate documents.

A guard may flag a `CURRENT_VERSION` reference outside an allowed surface, but it must support explicit exceptions for genealogy and compatibility.
