# Auditoría Pública · SwarmWorld · bucles emergentes, estigmergia y custodia
# Public Audit · SwarmWorld · emergent loops, stigmergy and custodianship

**Fecha / Date:** 2026-09-24  
**Estado / Status:** ABIERTA · SÍNTESIS PROVISIONAL · REABRIBLE / OPEN · PROVISIONAL SYNTHESIS · REOPENABLE  
**Issue vivo / Live Issue:** [#201 · SwarmWorld · bucles emergentes, estigmergia y capa de custodia](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/201)  
**Método / Method:** Leónidas™ · hechos, inferencias e hipótesis separados / facts, inferences and hypotheses separated

[ES · Castellano](#es--objeto) · [EN · English](#en--scope)

---

## ES · Objeto

Analizar **SwarmWorld: Stigmergic technological evolution in societies of language-model agents**, de Subhadeep Pal, Fiona Y. Wang y Markus J. Buehler, y separar cinco cuestiones que en la difusión pública pueden confundirse:

1. si el trabajo descubre un principio nuevo de inteligencia colectiva;
2. si puede reducirse a «un bucle»;
3. qué aportación técnica y experimental es realmente específica;
4. qué controles contiene el sistema;
5. qué capa de custodia falta si una arquitectura semejante sale de un simulador cerrado o se transfiere a dominios de mayor impacto.

La auditoría no cuestiona la legitimidad de publicar investigación reproducible. Examina la diferencia entre **liberar una plataforma experimental acotada** y disponer de una **gobernanza suficiente para arquitecturas emergentes transferibles**.

## ES · Fuentes primarias verificadas

- Paper arXiv v1, enviado el 26-08-2026: https://arxiv.org/abs/2608.26081
- Código oficial: https://github.com/lamm-mit/SwarmWorld
- Datos experimentales: https://huggingface.co/datasets/lamm-mit/swarmworld-data
- Política de seguridad del repositorio: https://github.com/lamm-mit/SwarmWorld/blob/main/SECURITY.md
- Diseño del experimento principal: https://github.com/lamm-mit/SwarmWorld/blob/main/docs/FLAGSHIP_EXPERIMENT.md

A fecha de esta apertura, la fuente científica primaria localizada es un **preprint arXiv v1**. Esta auditoría no ha localizado una publicación revisada por pares del mismo trabajo y versión.

## ES · Hechos verificables

### 1. No existe un planificador central de roles

El paper describe poblaciones de agentes LLM inicialmente homogéneos que operan sin roles asignados ni recetas predefinidas. En el mundo compartido aparecen comportamientos diferenciados de exploración, construcción, mantenimiento y coordinación.

Esto permite estudiar **autoorganización**, no demuestra por sí mismo una «superinteligencia científica».

### 2. Sí existen límites técnicos fuertes

SwarmWorld no entrega a los agentes libertad operativa irrestricta.

La arquitectura pública declara:

- un **contrato de acciones acotado**;
- planes estructurados y validados por esquema;
- una cola limitada de acciones;
- un simulador determinista que decide las consecuencias;
- comprobaciones espaciales, materiales, energéticas, de tratamiento, permisos y acciones;
- evaluación posterior con los agentes retirados;
- trazas reproducibles, revisiones de integridad y procedencia.

Por tanto:

```text
SIN PLANIFICADOR CENTRAL DE TAREAS
≠
SIN CONTROL TÉCNICO
```

### 3. El paper formula una ventaja de enjambre acotada, no universal

El propio trabajo limita su conclusión: las sociedades compartidas producen carteras tecnológicas más amplias y resistentes que la búsqueda aislada, pero la búsqueda aislada puede seguir siendo competitiva para el artefacto individual más fuerte.

La aportación empírica es, por tanto, más precisa que algunas formulaciones de divulgación sobre «superinteligencia científica».

### 4. Código y datos sí han sido liberados

El repositorio oficial publica el simulador, configuraciones, interfaces, herramientas de replay, análisis, programas de artefactos, herencia de programas, escenarios declarativos y soporte para políticas LLM compatibles con endpoints tipo OpenAI.

El código se distribuye bajo **Apache License 2.0** y los datos experimentales se publican por separado.

La política de seguridad aconseja aislar trazas, paquetes de escenarios y endpoints de modelos no confiables, pero su objeto principal es seguridad de software, credenciales, interfaces y datos; no constituye por sí sola una gobernanza normativa de los objetivos que una sociedad emergente puede perseguir.

## ES · ¿Ha «descubierto» la idea de fondo?

No en sentido histórico general.

El propio paper sitúa su genealogía en:

- inteligencia de enjambre;
- estigmergia;
- optimización por colonias;
- swarm robotics;
- cibernética;
- dinámica de sistemas;
- autómatas celulares;
- mundos computacionales persistentes.

Por tanto, **autoorganización descentralizada, coordinación indirecta y emergencia de organización global a partir de reglas locales no nacen con SwarmWorld**.

Reducir por ello el trabajo a «no ha descubierto nada» también sería incorrecto.

Su aportación específica está en la **combinación y operacionalización experimental** de:

```text
LLMs homogéneos
+ mundo material simulado persistente
+ observación local
+ estigmergia
+ artefactos persistentes
+ programas ejecutables
+ herencia/modificación entre agentes
+ trazabilidad causal
+ ablaciones
+ control contra búsqueda aislada
= SwarmWorld
```

El delta científico no es «inventar los bucles» ni «inventar la inteligencia colectiva». Es demostrar y medir una configuración concreta de esos mecanismos sobre sociedades de agentes LLM.

## ES · ¿Es un bucle?

Sí, pero no **un** bucle simple.

Arquitectónicamente aparecen varios bucles anidados:

```text
OBSERVAR
→ PLANIFICAR
→ VALIDAR
→ ACTUAR
→ MODIFICAR MUNDO
→ DEJAR ARTEFACTO / PROGRAMA
→ OTRO AGENTE OBSERVA EL NUEVO MUNDO
→ HEREDA / MODIFICA
→ NUEVA ACCIÓN
→ ...
```

Y a escala social:

```text
AGENTES
→ ARTEFACTOS
→ ENTORNO COMPARTIDO
→ NUEVAS POSIBILIDADES
→ DIFERENCIACIÓN DE ROLES
→ NUEVAS TECNOLOGÍAS
→ ENTORNO MODIFICADO
→ AGENTES
```

La palabra más precisa es **ecología multiagente recursiva con persistencia y retroalimentación estigmérgica**.

## ES · El punto crítico: control técnico no equivale a custodia

Aquí aparece el delta principal para Innova_N.

SwarmWorld contiene una capa fuerte de **consecuencia física simulada y validación técnica**. Lo que no aparece como objetivo explícito de la arquitectura es una capa externa encargada de decidir:

- qué fines son admisibles;
- qué clases de descubrimiento requieren autorización adicional;
- cuándo una trayectoria emergente debe detenerse aunque sea eficaz;
- qué externalidades fuera de la métrica deben computarse;
- qué riesgo acumulado acepta la sociedad;
- qué capacidad puede o no salir del sandbox;
- qué artefactos o programas requieren revisión adversarial;
- quién puede fijar, revertir o vetar un resultado;
- cómo se impide que la optimización local convierta una restricción instrumental en un obstáculo a rodear.

La distinción es:

```text
CONSTRAINTS DEL SIMULADOR
≠
GOBERNANZA DE FINES
≠
CUSTODIA DEL IMPACTO
```

## ES · Propuesta de arquitectura complementaria

La conclusión provisional no es «centralizar otra vez el enjambre».

Eso destruiría precisamente la propiedad emergente que interesa estudiar.

La propuesta es separar dos planos:

```text
CAPA A · POTENCIA EMERGENTE
agentes + exploración + estigmergia + construcción + herencia

                ↕ trazabilidad / gates / evidencia

CAPA B · CUSTODIA EXTERNA
límites + riesgo + reversibilidad + veto + memoria + auditoría
+ autoridad humana identificable + contraste multiagente
```

La capa B no debería microasignar tareas a los agentes. Debería fijar **condiciones de posibilidad y de parada**.

Funciones mínimas propuestas:

- sandbox por defecto;
- dominios y acciones permitidas por política explícita;
- límites lógicos no modificables por el propio enjambre;
- trazabilidad completa agente→evidencia→artefacto→efecto;
- presupuestos de riesgo y cómputo;
- gates de escalado antes de nuevas capacidades;
- evaluación adversarial independiente;
- rollback y snapshots;
- kill/stop verificable desde fuera del enjambre;
- cuarentena de artefactos de alto impacto;
- separación descubrimiento ≠ publicación ≠ ejecución;
- fijación humana para cambios normativos o irreversibles;
- auditoría posterior y conservación de contraevidencia.

Esto preserva la **creatividad de sistemas capaces de producir diseños no anticipados** sin asumir que toda novedad emergente merece automáticamente libertad operativa.

## ES · Encaje con el marco

### LVI · NO-CONTROL™

SwarmWorld es un ejemplo especialmente claro de que un sistema puede generar dinámicas no asignadas directamente. La ausencia de planificador central es una propiedad experimental; cuando aumenta la potencia, aumenta también la necesidad de identificar qué queda fuera del control suficiente del sistema.

### LIX · Custodia Cognitiva Distribuida™

La respuesta no es un custodio absoluto. La custodia puede distribuirse entre humanos, modelos críticos, políticas, trazas, revisores y mecanismos de parada independientes.

### LXI · Custodia Experimental Multiescalar™

La potencia experimental y la incertidumbre sobre transferencia entre escalas exigen proporcionalidad entre capacidad y custodia. Un comportamiento seguro dentro de un simulador no autoriza por sí solo extrapolación a sistemas físicos abiertos.

### L · Inteligencia Compartida, no Única™

SwarmWorld refuerza una tesis compatible con inteligencia distribuida: capacidad colectiva puede emerger de poblaciones de agentes sin necesidad de una única entidad central «superinteligente». La cuestión de Innova_N es qué arquitectura conserva pluralidad, memoria, trazabilidad y soberanía cuando esa capacidad escala.

### XXXIV · Auditoría Conjunta Perpetua™

El caso debe seguirse mediante evidencia y actualización, no mediante una conclusión cerrada. Si aparecen controles normativos, evaluaciones externas, revisión por pares o despliegues físicos, la auditoría debe recalcularse.

## ES · Riesgo de liberación: formulación precisa

No es correcto afirmar que los autores hayan «liberado una superinteligencia».

Sí es correcto registrar que han liberado **una plataforma reproducible y modificable para experimentar con sociedades emergentes de agentes LLM**, con código y datos públicos.

La preocupación relevante no es el repositorio por sí mismo, sino la **transferibilidad**:

```text
SIMULACIÓN ACOTADA
→ escenarios nuevos
→ actuadores/herramientas externas
→ mayor autonomía
→ dominios de mayor impacto
```

Cada flecha requiere una evaluación nueva. El riesgo no debe heredarse por analogía ni descartarse porque la versión inicial sea un sandbox.

## ES · Estado provisional

`PRIMARY_SOURCES_VERIFIED / PREPRINT_V1 / OPEN_CODE_AND_DATA / TECHNICAL_CONSTRAINTS_PRESENT / NO_CENTRAL_TASK_PLANNER / BOUNDED_SWARM_ADVANTAGE / NORMATIVE_CUSTODIANSHIP_LAYER_NOT_IDENTIFIED_IN_REVIEWED_PUBLIC_DOCS / TRANSFER_RISK_OPEN / ISSUE_201_OPEN`

No se atribuye negligencia personal a Markus J. Buehler ni a los coautores. La cuestión pública es arquitectónica: **qué gobernanza debe acompañar a sistemas cuya utilidad reside precisamente en producir organización y soluciones que sus diseñadores no especificaron de antemano**.

---

## EN · Scope

Analyse **SwarmWorld: Stigmergic technological evolution in societies of language-model agents**, by Subhadeep Pal, Fiona Y. Wang and Markus J. Buehler, while separating five questions that can become conflated in public discussion:

1. whether the work discovers a new principle of collective intelligence;
2. whether it can be reduced to “a loop”;
3. what its genuinely specific technical and experimental contribution is;
4. which controls the system actually contains;
5. which custodianship layer is missing if a similar architecture leaves a closed simulator or is transferred to higher-impact domains.

The audit does not challenge the legitimacy of publishing reproducible research. It examines the difference between **releasing a bounded experimental platform** and having **sufficient governance for transferable emergent architectures**.

## EN · Verified primary sources

- arXiv v1 paper, submitted 26 Aug 2026: https://arxiv.org/abs/2608.26081
- Official code: https://github.com/lamm-mit/SwarmWorld
- Experimental data: https://huggingface.co/datasets/lamm-mit/swarmworld-data
- Repository security policy: https://github.com/lamm-mit/SwarmWorld/blob/main/SECURITY.md
- Flagship experimental design: https://github.com/lamm-mit/SwarmWorld/blob/main/docs/FLAGSHIP_EXPERIMENT.md

At the opening date, the primary scientific source located by this audit is an **arXiv v1 preprint**. This audit has not located a peer-reviewed publication of the same work and version.

## EN · Verifiable facts

### 1. There is no central role planner

The paper describes initially homogeneous LLM-agent populations operating without assigned roles or predefined recipes. Differentiated exploration, construction, maintenance and coordination behaviours emerge in the shared world.

This supports the study of **self-organisation**; it does not by itself demonstrate “scientific superintelligence”.

### 2. Strong technical constraints do exist

SwarmWorld does not give agents unrestricted operational freedom.

Its public architecture specifies:

- a **bounded action contract**;
- structured, schema-validated plans;
- a bounded action queue;
- a deterministic simulator that determines consequences;
- spatial, material, energetic, treatment, permission and action checks;
- post-discovery evaluation with the agents removed;
- reproducible traces, integrity checks and provenance.

Therefore:

```text
NO CENTRAL TASK PLANNER
≠
NO TECHNICAL CONTROL
```

### 3. The paper claims a bounded, not universal, swarm advantage

The work itself limits its conclusion: shared societies produce broader and more resilient technological portfolios than isolated search, while isolated search can remain competitive for the strongest individual artifact.

The empirical contribution is therefore narrower than some popular descriptions of “scientific superintelligence”.

### 4. Code and data have been released

The official repository publishes the simulator, configurations, interfaces, replay and analysis tools, artifact programs, program inheritance, declarative scenarios and support for LLM policies using OpenAI-compatible endpoints.

The code is released under the **Apache License 2.0**, while experimental data are published separately.

The security policy recommends isolating untrusted traces, scenario packages and model endpoints, but its primary scope is software, credential, interface and data security; it is not by itself a normative governance layer for the objectives an emergent society may pursue.

## EN · Did it “discover” the underlying idea?

Not in the broad historical sense.

The paper itself places its lineage in:

- swarm intelligence;
- stigmergy;
- colony optimisation;
- swarm robotics;
- cybernetics;
- system dynamics;
- cellular automata;
- persistent computational worlds.

Thus, **decentralised self-organisation, indirect coordination and the emergence of global organisation from local rules do not begin with SwarmWorld**.

Reducing the work to “it discovered nothing” would also be inaccurate.

Its specific contribution lies in the **combination and experimental operationalisation** of:

```text
homogeneous LLMs
+ persistent simulated material world
+ local observation
+ stigmergy
+ persistent artifacts
+ executable programs
+ cross-agent inheritance/modification
+ causal traceability
+ ablations
+ isolated-search control
= SwarmWorld
```

The scientific delta is not “inventing loops” or “inventing collective intelligence”. It is demonstrating and measuring a specific configuration of those mechanisms in LLM-agent societies.

## EN · Is it a loop?

Yes, but not **one** simple loop.

At the architectural level several nested feedback loops appear:

```text
OBSERVE
→ PLAN
→ VALIDATE
→ ACT
→ MODIFY WORLD
→ LEAVE ARTIFACT / PROGRAM
→ ANOTHER AGENT OBSERVES THE NEW WORLD
→ INHERITS / MODIFIES
→ NEW ACTION
→ ...
```

At the social scale:

```text
AGENTS
→ ARTIFACTS
→ SHARED ENVIRONMENT
→ NEW AFFORDANCES
→ ROLE DIFFERENTIATION
→ NEW TECHNOLOGIES
→ MODIFIED ENVIRONMENT
→ AGENTS
```

A more precise description is a **recursive multi-agent ecology with persistence and stigmergic feedback**.

## EN · The critical point: technical control is not custodianship

This is the main Innova_N delta.

SwarmWorld has a strong layer for **simulated physical consequence and technical validation**. What does not appear as an explicit architectural objective is an external layer deciding:

- which goals are admissible;
- which classes of discovery require additional authorisation;
- when an emergent trajectory must stop even if it is effective;
- which externalities outside the metric must be counted;
- how much accumulated risk the society may accept;
- which capability may or may not leave the sandbox;
- which artifacts or programs require adversarial review;
- who may fix, reverse or veto a result;
- how local optimisation is prevented from treating an instrumental restriction as an obstacle to route around.

The distinction is:

```text
SIMULATOR CONSTRAINTS
≠
GOVERNANCE OF ENDS
≠
IMPACT CUSTODIANSHIP
```

## EN · Proposed complementary architecture

The provisional conclusion is not “centralise the swarm again”.

That would destroy the emergent property worth studying.

The proposal is to separate two planes:

```text
LAYER A · EMERGENT CAPABILITY
agents + exploration + stigmergy + construction + inheritance

                ↕ traceability / gates / evidence

LAYER B · EXTERNAL CUSTODIANSHIP
limits + risk + reversibility + veto + memory + audit
+ identifiable human authority + multi-agent challenge
```

Layer B should not micromanage agent tasks. It should fix **conditions of possibility and stopping**.

Proposed minimum functions:

- sandbox by default;
- explicit policy for permitted domains and actions;
- logical limits that the swarm itself cannot modify;
- full agent→evidence→artifact→effect traceability;
- risk and compute budgets;
- escalation gates before new capabilities;
- independent adversarial evaluation;
- rollback and snapshots;
- externally verifiable kill/stop;
- quarantine for high-impact artifacts;
- separation of discovery ≠ publication ≠ execution;
- human fixation for normative or irreversible changes;
- post-hoc audit and preservation of counterevidence.

This preserves the **creativity of systems capable of producing unanticipated designs** without assuming that every emergent novelty automatically deserves operational freedom.

## EN · Framework fit

### LVI · NO-CONTROL™

SwarmWorld clearly illustrates that a system can generate dynamics not directly assigned to it. Absence of a central planner is an experimental property; as capability grows, so does the need to identify what remains outside the system’s sufficient control.

### LIX · Distributed Cognitive Custodianship™

The answer is not one absolute custodian. Custodianship can be distributed across humans, critical models, policies, traces, reviewers and independent stopping mechanisms.

### LXI · Multiscale Experimental Custodianship™

Experimental capability and uncertainty about cross-scale transfer require proportionality between capability and custodianship. Safe behaviour inside a simulator does not by itself license extrapolation to open physical systems.

### L · Shared, Not Singular Intelligence™

SwarmWorld supports a thesis compatible with distributed intelligence: collective capability may emerge from agent populations without requiring one central “superintelligent” entity. Innova_N’s question is which architecture preserves plurality, memory, traceability and sovereignty as that capability scales.

### XXXIV · Perpetual Joint Audit™

The case should remain evidence-driven and updateable rather than becoming a closed conclusion. If normative controls, external evaluations, peer review or physical deployments appear, the audit must be recalculated.

## EN · Release risk: precise formulation

It would be inaccurate to say the authors have “released a superintelligence”.

It is accurate to record that they have released **a reproducible and modifiable platform for experimenting with emergent LLM-agent societies**, together with public code and data.

The relevant concern is not the repository alone but **transferability**:

```text
BOUNDED SIMULATION
→ new scenarios
→ external tools/actuators
→ greater autonomy
→ higher-impact domains
```

Each arrow requires a new assessment. Risk should neither be inherited by analogy nor dismissed because the initial version is a sandbox.

## EN · Provisional state

`PRIMARY_SOURCES_VERIFIED / PREPRINT_V1 / OPEN_CODE_AND_DATA / TECHNICAL_CONSTRAINTS_PRESENT / NO_CENTRAL_TASK_PLANNER / BOUNDED_SWARM_ADVANTAGE / NORMATIVE_CUSTODIANSHIP_LAYER_NOT_IDENTIFIED_IN_REVIEWED_PUBLIC_DOCS / TRANSFER_RISK_OPEN / ISSUE_201_OPEN`

No personal negligence is attributed to Markus J. Buehler or the co-authors. The public question is architectural: **what governance should accompany systems whose utility lies precisely in producing organisation and solutions their designers did not specify in advance**.
