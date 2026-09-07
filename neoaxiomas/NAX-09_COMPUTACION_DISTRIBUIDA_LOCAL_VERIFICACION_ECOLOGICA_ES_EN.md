# NAX-09 · Computación Distribuida Local con Verificación Ecológica™
# NAX-09 · Distributed Local Computing with Ecological Verification™

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Estado / Status:** ACTIVADO COMO PRINCIPIO DE DISEÑO CONDICIONAL · ABIERTO A SÍNTESIS Y MEDICIÓN / ACTIVATED AS A CONDITIONAL DESIGN PRINCIPLE · OPEN TO SYNTHESIS AND MEASUREMENT  
**Capa de profundidad / Depth layer:** desarrollo MAXPROC no reductivo · la formulación canónica se conserva / non-reductive MAXPROC development · canonical formulation preserved

## ES · Castellano

> **Cuando resulte técnica, social y ecológicamente razonable, debe preferirse aprovechar capacidad computacional local y distribuida antes que concentrar de forma innecesaria cálculo, tránsito y dependencia.**

Este Neoaxioma **no afirma que lo local sea siempre más eficiente ambientalmente**. La comparación debe considerar utilización del hardware, eficiencia energética, mezcla eléctrica, refrigeración, fabricación, vida útil, transmisión de datos, latencia, reutilización de equipos y carga real.

```text
PREFERENCIA LOCAL/DISTRIBUIDA
≠ DOGMA DE EFICIENCIA

PREFERENCIA
+ MEDICIÓN
+ COMPARACIÓN DE CICLO DE VIDA
→ DECISIÓN
```

### Desarrollo MAXPROC · preferencia condicionada, no ideología de infraestructura

NAX-09 responde a una tendencia frecuente: convertir una arquitectura técnica en valor moral por sí misma. «Local», «Edge», «nube», «centro de datos» o «distribuido» describen configuraciones; **ninguna garantiza automáticamente menor impacto, mayor soberanía o mejor uso de recursos**.

El principio introduce una preferencia sólo cuando la distribución permite aprovechar capacidad ya disponible, reducir dependencias innecesarias, disminuir tránsito o latencia, aumentar resiliencia o preservar mayor autonomía **sin trasladar un coste ecológico o social superior a otra parte del sistema**.

### Unidad real de comparación

Comparar sólo vatios durante inferencia puede ser insuficiente. La decisión debe considerar, cuando sea materialmente relevante:

- energía por tarea y utilización real;
- mezcla eléctrica y variabilidad temporal;
- refrigeración y pérdidas auxiliares;
- fabricación y renovación del hardware;
- vida útil y posibilidad de reutilización;
- tráfico y almacenamiento de datos;
- latencia y coste de transmisión;
- necesidad de duplicación o sobredimensionamiento;
- mantenibilidad y reparabilidad;
- privacidad y soberanía de datos;
- resiliencia y dependencia de proveedores;
- frecuencia y escala reales de la carga.

```text
IMPACTO COMPUTACIONAL
≠ CONSUMO INSTANTÁNEO

IMPACTO
= OPERACIÓN
+ INFRAESTRUCTURA
+ CICLO DE VIDA
+ RED
+ CONTEXTO ENERGÉTICO
+ EFECTOS SOCIALES RELEVANTES
```

No siempre será posible medir todo con la misma precisión. La incertidumbre debe registrarse en lugar de ocultarse detrás de una falsa cifra total.

### Reutilización frente a nueva fabricación

Una ventaja potencial de lo local aparece cuando existe hardware infrautilizado que puede asumir trabajo útil sin exigir nueva fabricación. Esa ventaja desaparece o se reduce si la supuesta distribución obliga a comprar miles de dispositivos dedicados de baja utilización que sustituyen una infraestructura compartida más eficiente.

Por tanto:

```text
HARDWARE YA EXISTENTE + VIDA ÚTIL EXTENDIDA
→ POSIBLE VENTAJA

NUEVA FLOTA SOBREDIMENSIONADA + BAJA UTILIZACIÓN
→ POSIBLE DESVENTAJA
```

La misma lógica se aplica a centros de datos: una instalación altamente eficiente puede ser preferible para determinadas cargas intensivas, mientras otras tareas con datos sensibles, baja latencia o capacidad local ociosa pueden ser mejores en Edge.

### Ecología y soberanía no son la misma variable

Una arquitectura puede ser ecológicamente eficiente y crear dependencia estratégica elevada; otra puede aumentar soberanía local pero consumir más energía. NAX-09 no permite esconder esa tensión en una sola etiqueta. Deben declararse las dimensiones y explicar qué compromiso se acepta.

```text
MENOR ENERGÍA
≠ MAYOR SOBERANÍA AUTOMÁTICA

MAYOR SOBERANÍA
≠ MENOR IMPACTO ECOLÓGICO AUTOMÁTICO
```

### Condiciones de fallo

NAX-09 falla si:

- se proclama «local = verde» sin medición;
- se compara sólo consumo de GPU y se ignora fabricación, refrigeración o utilización;
- se desplaza cómputo a Edge aumentando mucho la energía total sin una ganancia material que lo justifique;
- se centraliza por comodidad una carga que podría ejecutarse localmente con menor tránsito, mayor privacidad y coste comparable;
- se usa una métrica energética aislada para ignorar dependencia, resiliencia o derechos;
- se presentan estimaciones inciertas como equivalencias exactas.

### Relaciones neoaxiomáticas

- [NAX-01](./NAX-01_UNIDAD_SENTIDO_DISTRIBUCION_POTENCIA_ES_EN.md) ofrece la preferencia general por distribuir potencia cuando no existe necesidad de concentración.
- [NAX-07](./NAX-07_RED_NEOREAL_ACTORES_OPERATIVOS_ES_EN.md) exige que nodos Edge y actores distribuidos sigan siendo trazables.
- [NAX-08](./NAX-08_COOPERACION_EXCELENCIA_COMPETENCIA_DEPREDADORA_ES_EN.md) impide que eficiencia local se obtenga externalizando daños comunes.
- [NAX-12](./NAX-12_TRAZABILIDAD_SUSTITUTIVA_BUROCRACIA_REDUNDANTE_ES_EN.md) permite usar evidencia operacional para comparar configuraciones reales.
- [NAX-14](./NAX-14_PREVENCION_BIFURCACION_SIMBIOTICA_ES_EN.md) recuerda que acceso a capacidad computacional también tiene dimensión de inclusión y desigualdad.

### Criterios de contraste y revisión

Toda decisión relevante local/distribuida/central debería poder responder:

```text
¿QUÉ CARGA REAL SE COMPARA?
¿QUÉ HARDWARE EXISTE YA?
¿QUÉ HARDWARE NUEVO EXIGE CADA OPCIÓN?
¿QUÉ ENERGÍA TOTAL Y AUXILIAR CONSUME?
¿QUÉ VIDA ÚTIL SE ESPERA?
¿QUÉ TRÁFICO EVITA O AÑADE?
¿QUÉ PRIVACIDAD / LATENCIA / RESILIENCIA CAMBIA?
¿QUÉ INCERTIDUMBRES NO ESTÁN MEDIDAS?
¿LA DECISIÓN SIGUE SIENDO VÁLIDA SI CAMBIA LA ESCALA?
```

El Neoaxioma debe revisarse a la luz de mediciones empíricas. Si la evidencia demuestra que una arquitectura central es materialmente mejor para una carga concreta, la preferencia condicionada cede en ese caso; no se fuerza la conclusión.

**En sencillo:** Usar computación local o distribuida es una preferencia condicionada, no un dogma ecológico. Hay que medir el caso real y comparar energía, hardware, red, refrigeración y vida útil antes de decidir.

**Ejemplo:** Ejecutar una tarea de IA en un ordenador local reutilizado puede ahorrar tráfico y aprovechar hardware ya existente, pero un centro de datos eficiente puede consumir menos energía por tarea. La decisión correcta sale de comparar ambos casos completos, no de asumir que “local” o “nube” siempre gana.

## EN · English

> **When technically, socially and ecologically reasonable, local and distributed computational capacity should be preferred before unnecessarily concentrating computation, traffic and dependency.**

This Neoaxiom **does not claim that local computing is always environmentally more efficient**. Comparison must consider hardware utilisation, energy efficiency, electricity mix, cooling, manufacturing, useful life, data transmission, latency, equipment reuse and actual workload.

```text
LOCAL/DISTRIBUTED PREFERENCE
≠ EFFICIENCY DOGMA

PREFERENCE
+ MEASUREMENT
+ LIFE-CYCLE COMPARISON
→ DECISION
```

### MAXPROC development · conditional preference, not infrastructure ideology

NAX-09 responds to a common tendency: turning a technical architecture into a moral value by itself. “Local”, “Edge”, “cloud”, “data centre” or “distributed” describe configurations; **none automatically guarantees lower impact, greater sovereignty or better use of resources**.

The principle introduces a preference only when distribution can use already available capacity, reduce unnecessary dependencies, lower traffic or latency, increase resilience or preserve greater autonomy **without shifting a greater ecological or social cost elsewhere in the system**.

### Real unit of comparison

Comparing only watts during inference may be insufficient. Where materially relevant, the decision should consider:

- energy per task and real utilisation;
- electricity mix and temporal variation;
- cooling and auxiliary losses;
- hardware manufacturing and replacement;
- useful life and possibility of reuse;
- data traffic and storage;
- latency and transmission cost;
- need for duplication or overprovisioning;
- maintainability and repairability;
- privacy and data sovereignty;
- resilience and provider dependency;
- actual frequency and scale of workload.

```text
COMPUTATIONAL IMPACT
≠ INSTANTANEOUS CONSUMPTION

IMPACT
= OPERATION
+ INFRASTRUCTURE
+ LIFE CYCLE
+ NETWORK
+ ENERGY CONTEXT
+ RELEVANT SOCIAL EFFECTS
```

Not everything can always be measured with the same precision. Uncertainty should be recorded rather than hidden behind a false total number.

### Reuse versus new manufacturing

A potential advantage of local computing appears when underused existing hardware can perform useful work without requiring new manufacturing. That advantage disappears or shrinks if supposed distribution requires purchasing thousands of dedicated low-utilisation devices to replace more efficient shared infrastructure.

```text
EXISTING HARDWARE + EXTENDED USEFUL LIFE
→ POSSIBLE ADVANTAGE

NEW OVERPROVISIONED FLEET + LOW UTILISATION
→ POSSIBLE DISADVANTAGE
```

The same logic applies to data centres: a highly efficient facility may be preferable for some intensive workloads, while tasks involving sensitive data, low latency or idle local capacity may be better at the Edge.

### Ecology and sovereignty are not the same variable

An architecture may be ecologically efficient while creating high strategic dependency; another may increase local sovereignty while consuming more energy. NAX-09 does not allow that tension to be hidden inside one label. Dimensions should be declared and the accepted trade-off explained.

```text
LOWER ENERGY
≠ GREATER SOVEREIGNTY AUTOMATICALLY

GREATER SOVEREIGNTY
≠ LOWER ECOLOGICAL IMPACT AUTOMATICALLY
```

### Failure conditions

NAX-09 fails if:

- “local = green” is proclaimed without measurement;
- only GPU consumption is compared while manufacturing, cooling or utilisation are ignored;
- compute is shifted to Edge with much higher total energy and no material benefit justifying it;
- a workload is centralised for convenience even though it could run locally with lower traffic, greater privacy and comparable cost;
- an isolated energy metric is used to ignore dependency, resilience or rights;
- uncertain estimates are presented as exact equivalences.

### Neoaxiomatic relations

- [NAX-01](./NAX-01_UNIDAD_SENTIDO_DISTRIBUCION_POTENCIA_ES_EN.md) provides the general preference for distributing power when concentration is unnecessary.
- [NAX-07](./NAX-07_RED_NEOREAL_ACTORES_OPERATIVOS_ES_EN.md) requires Edge nodes and distributed actors to remain traceable.
- [NAX-08](./NAX-08_COOPERACION_EXCELENCIA_COMPETENCIA_DEPREDADORA_ES_EN.md) prevents local efficiency from being achieved by externalising common harm.
- [NAX-12](./NAX-12_TRAZABILIDAD_SUSTITUTIVA_BUROCRACIA_REDUNDANTE_ES_EN.md) allows operational evidence to compare real configurations.
- [NAX-14](./NAX-14_PREVENCION_BIFURCACION_SIMBIOTICA_ES_EN.md) recalls that access to computational capacity also has an inclusion and inequality dimension.

### Criteria for scrutiny and revision

Every relevant local/distributed/central decision should answer:

```text
WHAT REAL WORKLOAD IS BEING COMPARED?
WHAT HARDWARE ALREADY EXISTS?
WHAT NEW HARDWARE DOES EACH OPTION REQUIRE?
WHAT TOTAL AND AUXILIARY ENERGY DOES IT USE?
WHAT USEFUL LIFE IS EXPECTED?
WHAT TRAFFIC DOES IT AVOID OR ADD?
WHAT PRIVACY / LATENCY / RESILIENCE CHANGES?
WHAT UNCERTAINTIES REMAIN UNMEASURED?
DOES THE DECISION STILL HOLD IF SCALE CHANGES?
```

The Neoaxiom should be revised in light of empirical measurements. If evidence shows a central architecture is materially better for a specific workload, the conditional preference yields in that case; the conclusion is not forced.

**In plain language:** Using local or distributed computing is a conditional preference, not an ecological dogma. The real case must be measured by comparing energy, hardware, network use, cooling and useful life before deciding.

**Example:** Running an AI task on a reused local computer may reduce traffic and use existing hardware, while an efficient data centre may consume less energy per task. The correct decision comes from comparing both complete cases, not from assuming that “local” or “cloud” always wins.

<!-- NEOAXIOM_MANIFEST_RELATIONS_START -->

## Relaciones con manifiestos / Relations with Manifestos

> **Relación documental/conceptual, no procedencia exclusiva.** Estos vínculos hacen explícita la red vigente del Neoaxioma con manifiestos que desarrollan, aplican, limitan o contextualizan su función. Un enlace no declara identidad, subordinación ni causalidad. / **Documentary/conceptual relation, not exclusive provenance.** These links make explicit the Neoaxiom's current network with Manifestos that develop, apply, limit or contextualise its function. A link does not assert identity, subordination or causality.

- [XVII · Respeto a Todos los Seres Vivos™ / Respect for All Living Beings™](../manifiestos/17_respeto_todos_seres_vivos_ES_EN.md)
- [XLV · Multidimensionalidad Neodialéctica™ / Neodialectical Multidimensionality™](../manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md)

<!-- NEOAXIOM_MANIFEST_RELATIONS_END -->

**Síntesis / Synthesis:** [#92](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/92) · [Matriz general / General matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80).

[← Índice de Neoaxiomas™](README.md)
