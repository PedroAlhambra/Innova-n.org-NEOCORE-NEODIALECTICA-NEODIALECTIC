# WEB4™ ↔ NEOCore™ · evolución pública y regla de versionado
# WEB4™ ↔ NEOCore™ · public evolution and versioning rule

**Estado / Status:** Documento público de genealogía y navegación · no sustituye al registro canónico de versión / Public genealogy and navigation document · does not replace the canonical version registry  
**Fecha / Date:** 2026-09-04  
**Issue de revisión / Revision issue:** [#184](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/184)  
**Manifiesto relacionado / Related manifesto:** [X · WEB4™ · SistemaTrazable™](../manifiestos/07_web4_sistematrazable_ES_EN.md)  
**Versión vigente de NEOCore™ / Current NEOCore™ version:** [resolver siempre desde `versiones/README.md` / always resolve from `versiones/README.md`](./README.md)

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Para qué existe este documento

WEB4™ y NEOCore™ evolucionan relacionados, pero **no comparten un único número de versión**.

```text
NEOCORE_VERSION ≠ WEB4_VERSION
```

Este documento conserva una genealogía pública de alto nivel para explicar cómo se relacionan ambos sistemas sin convertir el Manifiesto X en un changelog ni exponer mecanismos privados innecesarios.

La única fuente pública que determina qué versión de NEOCore™ está vigente es [`versiones/README.md`](./README.md). Cualquier número incluido aquí describe un **hito histórico material**, no una copia dinámica de `CURRENT_VERSION`.

## 2. Regla de evolución

La evolución pública se interpreta así:

```text
ESTADO HEREDADO
+ DELTA EXPLÍCITO
+ PROCEDENCIA / EVIDENCIA
+ RELACIONES AFECTADAS
+ CONTRASTE / PRUEBA CUANDO PROCEDA
+ FIJACIÓN COMPETENTE
= NUEVO ESTADO TRAZABLE
```

Y conserva estas separaciones:

```text
DELTA ≠ CANON
TRAZA ≠ VALIDACIÓN
DRAFT / PENDIENTE-SAN ≠ APROBADO
CURRENT_VERSION ≠ VERSION_OF_ORIGIN
```

Una versión nueva **no reescribe retroactivamente** lo que una versión anterior sabía, afirmaba o implementaba. La versión anterior conserva su contexto y puede ser reconstruida desde la genealogía Git, documentos de versión y trazas asociadas.

## 3. Hitos públicos

### 2026-08-06 · Manifiesto X 1.1

La formulación fundacional de [WEB4™ · SistemaTrazable™](../manifiestos/07_web4_sistematrazable_ES_EN.md) fijó la idea de una capa pública relacional capaz de conservar identidad, función, estado, genealogía, relaciones, transformación y niveles de acceso.

Ese texto era correcto como origen, pero deliberadamente breve.

### 2026-08-26 · NEOCore™ 7.3 pasa a canon abierto

La fase `7.3-CANDIDATE` queda como estado histórico cuando NEOCore™ 7.3 es promovido a canon abierto, canónico y reabrible. La evolución posterior hereda ese estado sin borrar la fase pre-canónica.

Fuentes:

- [Canon 7.3](../propuestas/sintesis-abierta/NEOCORE_7_3_CANON_ES_EN.md)
- [Matriz 7.3 · Autosíntesis Recursiva](../propuestas/sintesis-abierta/NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)

### 2026-08-31 · NEOCore™ 7.3.3 integra la evolución modular WEB4™

[NEOCore™ 7.3.3](./NEOCORE_7_3_3_ES_EN.md) fija como delta material la evolución modular verificada de WEB4™ disponible en ese momento y hace explícita su arquitectura social como red de conocimiento, creación y aporte trazable.

Ese hito establece públicamente, entre otras cosas:

- `NEOCORE_VERSION ≠ WEB4_VERSION`;
- WEB4™ no es una colección de páginas independientes;
- el nodo trazable, sus fuentes, relaciones y actividad material forman la unidad social de la red;
- la existencia de una arquitectura o capacidad objetivo no equivale a capacidad funcional ya promovida;
- la IA puede ampliar memoria, navegación, contraste y estructuración bajo responsabilidad humana;
- la proyección pública efectiva requiere su propia verificación.

### 2026-09-04 · Manifiesto X 1.2

La revisión 1.2 amplía la formulación pública de WEB4™ para hacer visible lo que ya era estructuralmente cierto pero no estaba suficientemente explicado en la versión 1.1:

- WEB4™ como proyección pública y operativa de un corpus humano–IA vivo;
- corpus versionado, relacional, reabrible y autogestionado;
- red viva **OFF-CHAIN** como modelo de referencia;
- relación funcional de alto nivel con NEOCore™, SAN™, NAVE™, Leónidas™ y NeoCronos™;
- arquitectura social basada en nodos y aportes trazables, no en popularidad;
- separación entre arquitectura, estado verificable y proyección pública;
- reconstrucción temporal y atribución humano–IA;
- privacidad por capas e interoperabilidad/salida;
- límites públicos de exposición de la arquitectura protegida.

La revisión está trazada en [Issue #184](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/184) y permanece abierta a [Síntesis Abierta #39](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/39).

## 4. Qué significa OFF-CHAIN aquí

**OFF-CHAIN** no significa ausencia de evidencia ni opacidad.

Significa que la identidad del corpus, la relación semántica, la genealogía, el estado de una síntesis, el reconocimiento de un aporte o la memoria del sistema **no dependen obligatoriamente de una cadena pública o blockchain para existir**.

La evidencia puede apoyarse, según el objeto, en repositorios, commits, hashes, documentos, fuentes, registros, firmas, identificadores o pruebas externas. Lo importante es que la relación pueda conservar procedencia y reconstrucción suficiente.

```text
OFF-CHAIN ≠ SIN TRAZA
OFF-CHAIN ≠ SIN VERIFICACIÓN
OFF-CHAIN ≠ BLOCKCHAIN OBLIGATORIA
```

La implementación concreta y las mecánicas privadas de cálculo, ponderación, automatización o sincronización no se publican por defecto.

## 5. Qué permanece protegido

La transparencia pública debe permitir comprender y auditar **qué hace el sistema y qué evidencia deja**, sin convertir el repositorio público en un manual de clonación de toda su arquitectura interna.

No forman parte de esta genealogía pública, salvo decisión expresa posterior:

- reglas privadas de cálculo y ponderación;
- heurísticas internas;
- instrucciones de agentes y automatismos protegidos;
- credenciales, secretos o configuraciones sensibles;
- topología privada completa;
- mecanismos de sincronización interna no necesarios para verificación pública;
- datos personales o material restringido.

## 6. Regla de lectura futura

Para saber el estado vigente:

1. consultar [`versiones/README.md`](./README.md);
2. leer el documento específico de la versión cuando sea necesario;
3. usar este documento para la genealogía pública WEB4™ ↔ NEOCore™;
4. usar el [Manifiesto X](../manifiestos/07_web4_sistematrazable_ES_EN.md) para principios y arquitectura pública de alto nivel;
5. usar Issues, auditorías y commits para reconstruir deltas concretos.

---

# EN · English

## 1. Purpose of this document

WEB4™ and NEOCore™ evolve in relation to each other, but **they do not share a single version number**.

```text
NEOCORE_VERSION ≠ WEB4_VERSION
```

This document preserves a high-level public genealogy explaining how both systems relate without turning Manifesto X into a changelog or unnecessarily exposing protected internal mechanics.

The only public source that determines the current NEOCore™ version is [`versiones/README.md`](./README.md). Any number included here describes a **material historical milestone**, not a dynamic copy of `CURRENT_VERSION`.

## 2. Evolution rule

Public evolution is read as:

```text
INHERITED STATE
+ EXPLICIT DELTA
+ PROVENANCE / EVIDENCE
+ AFFECTED RELATIONS
+ CONTRAST / TESTING WHERE APPLICABLE
+ COMPETENT FIXATION
= NEW TRACEABLE STATE
```

The following distinctions remain protected:

```text
DELTA ≠ CANON
TRACE ≠ VALIDATION
DRAFT / PENDING-SAN ≠ APPROVED
CURRENT_VERSION ≠ VERSION_OF_ORIGIN
```

A new version **does not retroactively rewrite** what an earlier version knew, claimed or implemented. The earlier version retains its context and may be reconstructed through Git genealogy, version documents and associated traces.

## 3. Public milestones

### 2026-08-06 · Manifesto X 1.1

The foundational wording of [WEB4™ · SistemaTrazable™](../manifiestos/07_web4_sistematrazable_ES_EN.md) fixed the idea of a public relational layer able to preserve identity, function, state, genealogy, relations, transformation and access levels.

The text was correct as an origin, but deliberately brief.

### 2026-08-26 · NEOCore™ 7.3 becomes open canon

The `7.3-CANDIDATE` phase becomes historical state when NEOCore™ 7.3 is promoted to open, canonical and reopenable canon. Later evolution inherits that state without erasing the pre-canonical phase.

Sources:

- [7.3 Canon](../propuestas/sintesis-abierta/NEOCORE_7_3_CANON_ES_EN.md)
- [7.3 Matrix · Recursive Self-Synthesis](../propuestas/sintesis-abierta/NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)

### 2026-08-31 · NEOCore™ 7.3.3 integrates WEB4™ modular evolution

[NEOCore™ 7.3.3](./NEOCORE_7_3_3_ES_EN.md) fixes as a material delta the verified modular evolution of WEB4™ available at that point and makes explicit its social architecture as a network of knowledge, creation and traceable contribution.

That milestone publicly establishes, among other things:

- `NEOCORE_VERSION ≠ WEB4_VERSION`;
- WEB4™ is not a collection of independent pages;
- the traceable node, its sources, relations and material activity form the social unit of the network;
- the existence of an architecture or target capability does not equal an already promoted functional capability;
- AI may extend memory, navigation, contrast and structuring under human responsibility;
- effective public projection requires its own verification.

### 2026-09-04 · Manifesto X 1.2

Revision 1.2 expands the public wording of WEB4™ to make visible what was already structurally true but insufficiently explained in version 1.1:

- WEB4™ as the public and operational projection of a living human–AI corpus;
- a versioned, relational, reopenable and self-managed corpus;
- a living **OFF-CHAIN** network as the reference model;
- high-level functional relation with NEOCore™, SAN™, NAVE™, Leónidas™ and NeoCronos™;
- social architecture based on nodes and traceable contributions rather than popularity;
- separation between architecture, verifiable state and public projection;
- temporal reconstruction and human–AI attribution;
- layered privacy and interoperability/exit;
- public exposure limits for protected architecture.

The revision is traced in [Issue #184](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/184) and remains open to [Open Synthesis #39](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/39).

## 4. What OFF-CHAIN means here

**OFF-CHAIN** does not mean absence of evidence or opacity.

It means that corpus identity, semantic relation, genealogy, synthesis state, contribution recognition or system memory **do not have to depend on a public chain or blockchain in order to exist**.

Evidence may rely, according to the object, on repositories, commits, hashes, documents, sources, records, signatures, identifiers or external proofs. What matters is that the relation can preserve sufficient provenance and reconstructibility.

```text
OFF-CHAIN ≠ WITHOUT TRACE
OFF-CHAIN ≠ WITHOUT VERIFICATION
OFF-CHAIN ≠ MANDATORY BLOCKCHAIN
```

Concrete implementation and private mechanics for calculation, weighting, automation or synchronisation are not public by default.

## 5. What remains protected

Public transparency should allow others to understand and audit **what the system does and what evidence it leaves** without turning the public repository into a cloning manual for its whole internal architecture.

The following are outside this public genealogy unless explicitly authorised later:

- private calculation and weighting rules;
- internal heuristics;
- protected agent and automation instructions;
- credentials, secrets or sensitive configuration;
- the complete private topology;
- internal synchronisation mechanisms unnecessary for public verification;
- personal data or restricted material.

## 6. Future reading rule

To determine current state:

1. consult [`versiones/README.md`](./README.md);
2. read the version-specific document where needed;
3. use this document for the public WEB4™ ↔ NEOCore™ genealogy;
4. use [Manifesto X](../manifiestos/07_web4_sistematrazable_ES_EN.md) for high-level public principles and architecture;
5. use Issues, audits and commits to reconstruct concrete deltas.