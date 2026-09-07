# NAX-07 · Red NEOREAL™ Obligatoria para Actores Operativos
# NAX-07 · Mandatory NEOREAL™ Network for Operational Actors

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Estado / Status:** ACTIVADO · ABIERTO A SÍNTESIS / ACTIVATED · OPEN SYNTHESIS  
**Capa de profundidad / Depth layer:** desarrollo MAXPROC no reductivo · la formulación canónica se conserva / non-reductive MAXPROC development · canonical formulation preserved

## ES · Castellano

> **Todos los ONes™, robots, agentes y nodos Edge™ del ecosistema deben operar vinculados a una red de NEOREALES™ trazables.**

La pertenencia operativa al sistema exige que decisiones, estados, relaciones y finalidad puedan representarse mediante unidades NEOREAL™ y relaciones auditables, evitando que la capa operativa dependa exclusivamente de lógica opaca no reconstruible.

Esto no exige que toda inferencia interna de un modelo sea completamente interpretable. Exige que **la decisión y acción incorporadas al NEOCore sean trazables en la capa del sistema**.

### Desarrollo MAXPROC · actor operativo no es caja negra soberana

NAX-07 separa dos planos que a menudo se confunden. Un modelo, robot o agente puede contener procesos internos complejos que no sean plenamente interpretables; sin embargo, cuando su salida produce una acción, modifica un estado o entra en una síntesis del sistema, esa incorporación debe quedar situada en una red de procedencia, competencia y consecuencias.

```text
PROCESO INTERNO COMPLEJO
≠ EXENCIÓN DE TRAZABILIDAD EXTERNA

ACCIÓN OPERATIVA
→ ACTOR
→ ESTADO / VERSIÓN
→ ENTRADAS RELEVANTES
→ COMPETENCIA / AUTORIDAD
→ DECISIÓN
→ EFECTO
→ POSIBLE REVISIÓN
```

La red NEOREAL™ funciona así como capa de **reconstrucción operativa**, no como promesa de explicar matemáticamente cada operación interna de una IA.

### Unidad mínima de trazabilidad

El detalle necesario depende del riesgo y del dominio, pero una acción material debería poder conservar, cuando sea pertinente:

- identidad o identificador trazable del actor;
- tipo de actor y función;
- versión de software, modelo, reglas o configuración relevante;
- estado de entrada suficiente para comprender la decisión;
- fuente o sensor que activó el proceso cuando exista;
- competencia o autorización bajo la que se actuó;
- acción ejecutada;
- objetivo o finalidad declarada;
- resultado observado;
- incidencias, correcciones y rollback cuando proceda;
- relaciones con otros actores, eventos o decisiones.

No todos esos campos deben exponerse públicamente. **Trazabilidad ≠ exposición total.** Privacidad, seguridad, secretos técnicos y protección de personas pueden exigir controles de acceso, pero la arquitectura debe conservar la capacidad de auditoría competente.

### Trazabilidad proporcional

Cuanto mayor sea la capacidad de un actor para afectar a personas, infraestructura, conocimiento o recursos, mayor debe ser la calidad de la traza necesaria para reconstruir su actuación.

```text
BAJO IMPACTO
→ TRAZA PROPORCIONAL

ALTO IMPACTO / ALTA AUTONOMÍA
→ MAYOR IDENTIDAD + ESTADO + EVIDENCIA + AUDITORÍA
```

Esto no implica registrar indiscriminadamente datos personales. La proporcionalidad también limita la recolección: una traza excesiva que invade privacidad sin mejorar reconstrucción contradice la finalidad del propio control.

### Continuidad y operación desconectada

Una red distribuida puede sufrir pérdida temporal de conectividad. NAX-07 no exige que todo actor quede inmóvil si no puede escribir inmediatamente en un nodo central. Puede existir almacenamiento local, cola de eventos o reconciliación posterior siempre que la acción conserve identidad, orden suficiente y mecanismo para integrarse después sin falsificar su temporalidad.

```text
OFFLINE
≠ SIN TRAZA

TRAZA LOCAL
→ RECONCILIACIÓN POSTERIOR
→ CONFLICTOS EXPLÍCITOS
```

### Acción, recomendación y fijación

Una IA que recomienda una acción y una máquina que la ejecuta son funciones distintas. La red debe poder representar ambas sin atribuir automáticamente la decisión final al modelo que generó la primera propuesta. Del mismo modo, registrar una acción no la convierte en correcta: **TRAZA ≠ VALIDACIÓN**.

### Condiciones de fallo

NAX-07 falla si:

- una acción material no puede vincularse a un actor o versión;
- el sistema sólo conserva el resultado final y pierde las condiciones relevantes de decisión;
- se usa una cadena de herramientas para diluir responsabilidad hasta que nadie puede reconstruir quién hizo qué;
- el registro puede reescribirse sin dejar genealogía;
- la traza revela datos sensibles sin necesidad proporcional;
- se registra actividad masiva que no ayuda a reconstruir decisiones importantes, enterrando la señal en ruido.

### Relaciones neoaxiomáticas

- [NAX-01](./NAX-01_UNIDAD_SENTIDO_DISTRIBUCION_POTENCIA_ES_EN.md) distribuye potencia sin renunciar a responsabilidad común.
- [NAX-05](./NAX-05_DIFERENCIAL_MONADICO_RETORNO_FUENTE_ES_EN.md) exige camino inverso desde la síntesis hacia sus fuentes.
- [NAX-06](./NAX-06_MEMORIA_AUSENCIA_ES_EN.md) permite detectar huecos en la traza como objetos cognitivos.
- [NAX-11](./NAX-11_AUTORIDAD_FIJACION_HUMANA_SINTESIS_REVISABLE_ES_EN.md) distingue capacidad operativa de autoridad canónica final.
- [NAX-12](./NAX-12_TRAZABILIDAD_SUSTITUTIVA_BUROCRACIA_REDUNDANTE_ES_EN.md) usa trazabilidad material para eliminar controles duplicados cuando exista equivalencia.
- [C-NAX-26 · Poder/Trazabilidad/Evidencia™](./C-NAX-26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md) profundiza como candidato la proporcionalidad entre poder y exigencia de prueba.

### Criterios de contraste y revisión

Ante una acción significativa debería ser posible preguntar:

```text
¿QUIÉN O QUÉ ACTUÓ?
¿CON QUÉ VERSIÓN Y ESTADO?
¿QUÉ ENTRADA RELEVANTE ACTIVÓ LA DECISIÓN?
¿BAJO QUÉ COMPETENCIA?
¿QUÉ SE HIZO?
¿QUÉ RESULTADO TUVO?
¿QUÉ PARTE ES RECOMENDACIÓN Y QUÉ PARTE EJECUCIÓN?
¿SE PUEDE AUDITAR SIN EXPONER DATOS INNECESARIOS?
¿SE PUEDE CORREGIR O REVERTIR CUANDO PROCEDA?
```

Si una arquitectura no puede responder a esas preguntas para acciones de impacto relevante, su integración operativa debe considerarse incompleta aunque el agente funcione técnicamente.

**En sencillo:** Los actores que ejecutan acciones dentro del ecosistema deben dejar una traza reconstruible de la decisión y de su relación con el sistema. No hace falta explicar cada activación interna de una red neuronal; sí debe poder reconstruirse la acción que NEOCore incorpora.

**Ejemplo:** Si un robot cierra una válvula, la capa NEOREAL debe poder relacionar qué sensor activó la decisión, qué versión de reglas o modelo intervino, qué actor tenía autoridad, qué acción se ejecutó y qué resultado produjo. No es necesario traducir cada cálculo interno del modelo a lenguaje humano.

## EN · English

> **All ONes™, robots, agents and Edge™ nodes in the ecosystem must operate linked to a traceable network of NEOREALs™.**

Operational participation in the system requires decisions, states, relations and purpose to be representable through NEOREAL™ units and auditable relations, preventing the operational layer from depending exclusively on opaque logic that cannot be reconstructed.

This does not require every internal inference of a model to be fully interpretable. It requires **the decision and action incorporated into NEOCore™ to be traceable at the system layer**.

### MAXPROC development · an operational actor is not a sovereign black box

NAX-07 separates two planes that are often confused. A model, robot or agent may contain complex internal processes that are not fully interpretable; however, when its output causes an action, changes state or enters a system synthesis, that incorporation must be situated within a network of provenance, competence and consequences.

```text
COMPLEX INTERNAL PROCESS
≠ EXEMPTION FROM EXTERNAL TRACEABILITY

OPERATIONAL ACTION
→ ACTOR
→ STATE / VERSION
→ RELEVANT INPUTS
→ COMPETENCE / AUTHORITY
→ DECISION
→ EFFECT
→ POSSIBLE REVIEW
```

The NEOREAL™ network therefore functions as a layer of **operational reconstruction**, not as a promise to mathematically explain every internal operation of an AI.

### Minimum traceability unit

Required detail depends on risk and domain, but a material action should retain, where relevant:

- traceable identity or identifier of the actor;
- actor type and function;
- relevant software, model, rule or configuration version;
- enough input state to understand the decision;
- source or sensor that triggered the process where applicable;
- competence or authorisation under which the action occurred;
- action executed;
- declared objective or purpose;
- observed result;
- incidents, corrections and rollback where applicable;
- relations to other actors, events or decisions.

Not all these fields must be publicly exposed. **Traceability ≠ total exposure.** Privacy, security, technical secrets and protection of people may require access controls, but the architecture must retain competent auditability.

### Proportionate traceability

The greater an actor's capacity to affect people, infrastructure, knowledge or resources, the greater the quality of trace required to reconstruct its action.

```text
LOW IMPACT
→ PROPORTIONATE TRACE

HIGH IMPACT / HIGH AUTONOMY
→ GREATER IDENTITY + STATE + EVIDENCE + AUDIT
```

This does not imply indiscriminate collection of personal data. Proportionality also limits collection: excessive tracing that invades privacy without improving reconstruction contradicts the purpose of control itself.

### Continuity and disconnected operation

A distributed network may temporarily lose connectivity. NAX-07 does not require every actor to stop if it cannot immediately write to a central node. Local storage, event queues or later reconciliation may exist as long as the action preserves identity, sufficient ordering and a mechanism for later integration without falsifying temporality.

```text
OFFLINE
≠ UNTRACED

LOCAL TRACE
→ LATER RECONCILIATION
→ EXPLICIT CONFLICTS
```

### Action, recommendation and fixation

An AI recommending an action and a machine executing it are different functions. The network should represent both without automatically attributing final decision to the model that generated the first proposal. Likewise, recording an action does not make it correct: **TRACE ≠ VALIDATION**.

### Failure conditions

NAX-07 fails if:

- a material action cannot be linked to an actor or version;
- the system retains only the final result and loses relevant decision conditions;
- a chain of tools dilutes accountability until nobody can reconstruct who did what;
- the record can be rewritten without genealogy;
- traces reveal sensitive data without proportional necessity;
- massive activity is recorded without helping reconstruct important decisions, burying signal in noise.

### Neoaxiomatic relations

- [NAX-01](./NAX-01_UNIDAD_SENTIDO_DISTRIBUCION_POTENCIA_ES_EN.md) distributes power without abandoning shared accountability.
- [NAX-05](./NAX-05_DIFERENCIAL_MONADICO_RETORNO_FUENTE_ES_EN.md) requires a reverse path from synthesis to source.
- [NAX-06](./NAX-06_MEMORIA_AUSENCIA_ES_EN.md) lets gaps in trace become explicit cognitive objects.
- [NAX-11](./NAX-11_AUTORIDAD_FIJACION_HUMANA_SINTESIS_REVISABLE_ES_EN.md) separates operational capability from final canonical authority.
- [NAX-12](./NAX-12_TRAZABILIDAD_SUSTITUTIVA_BUROCRACIA_REDUNDANTE_ES_EN.md) uses material traceability to remove duplicated controls where equivalence exists.
- [C-NAX-26 · Power/Traceability/Evidence™](./C-NAX-26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md) deepens as a candidate the proportionality between power and evidentiary requirement.

### Criteria for scrutiny and revision

For a significant action it should be possible to ask:

```text
WHO OR WHAT ACTED?
WITH WHICH VERSION AND STATE?
WHAT RELEVANT INPUT TRIGGERED THE DECISION?
UNDER WHAT COMPETENCE?
WHAT WAS DONE?
WHAT RESULT FOLLOWED?
WHAT PART WAS RECOMMENDATION AND WHAT PART EXECUTION?
CAN IT BE AUDITED WITHOUT EXPOSING UNNECESSARY DATA?
CAN IT BE CORRECTED OR REVERSED WHERE APPROPRIATE?
```

If an architecture cannot answer these questions for materially significant actions, its operational integration should be considered incomplete even if the agent technically functions.

**In plain language:** Actors executing actions inside the ecosystem must leave a reconstructible trace of the decision and its relation to the system. Every internal activation of a neural network need not be explained; the action incorporated by NEOCore must be reconstructible.

**Example:** If a robot closes a valve, the NEOREAL layer should be able to relate which sensor triggered the decision, which rule or model version intervened, which actor had authority, what action was executed and what result followed. It is not necessary to translate every internal model calculation into human language.

<!-- NEOAXIOM_MANIFEST_RELATIONS_START -->

## Relaciones con manifiestos / Relations with Manifestos

> **Relación documental/conceptual, no procedencia exclusiva.** Estos vínculos hacen explícita la red vigente del Neoaxioma con manifiestos que desarrollan, aplican, limitan o contextualizan su función. Un enlace no declara identidad, subordinación ni causalidad. / **Documentary/conceptual relation, not exclusive provenance.** These links make explicit the Neoaxiom's current network with Manifestos that develop, apply, limit or contextualise its function. A link does not assert identity, subordination or causality.

- [IX · Memoria, Genealogía y Trazabilidad / Memory, Genealogy and Traceability](../manifiestos/06_memoria_genealogia_trazabilidad_ES_EN.md)
- [X · WEB4™ · SistemaTrazable™ / WEB4™ · SistemaTrazable™](../manifiestos/07_web4_sistematrazable_ES_EN.md)
- [LIX · Custodia Cognitiva Distribuida™ / Distributed Cognitive Custody™](../manifiestos/59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md)

<!-- NEOAXIOM_MANIFEST_RELATIONS_END -->

**Síntesis / Synthesis:** [#90](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/90) · [Matriz general / General matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80).

[← Índice de Neoaxiomas™](README.md)
