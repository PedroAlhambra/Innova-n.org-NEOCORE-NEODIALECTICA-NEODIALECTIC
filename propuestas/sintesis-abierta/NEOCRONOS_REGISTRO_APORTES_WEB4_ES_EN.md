# NeoCronos™ · Eventos de Aporte y Créditos de Función en WEB4™
# NeoCronos™ · Contribution Events and Role Credits in WEB4™

**Estado / Status:** diseño operativo abierto · open operational design  
**Fecha / Date:** 2026-08-12  
**Marco / Framework:** NEOCore™ 7.2 · Síntesis Abierta Neodialéctica™ / Neodialectical Open Synthesis™ · WEB4™  
**Rama técnica / Technical branch:** `sintesis-aportes-tokenizados`  
**Síntesis de diseño / Design synthesis:** [#141](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/141)  
**Auditoría retrospectiva / Retrospective audit:** [#142](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/142)  
**Raíz ya fijada / Already-fixed root:** [LXIV · NeoCronos™](../../manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md) · [LXV · NeoJuego™ / NeoGame™](../../manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md)

---

# ES · Castellano

## 1. Corrección del modelo anterior

La primera implementación de esta rama utilizó un modelo plano:

```text
UN APORTE
→ UN APORTANTE
→ UN TOKEN
```

Ese modelo es insuficiente y queda sustituido.

Un evento de Síntesis puede contener varias funciones realizadas por personas distintas. La persona que publica una información puede no ser quien descubre su relación con el marco; quien descubre la relación puede no ser quien ejecuta la implementación; y una IA puede asistir en el contraste sin convertirse por ello en origen humano del delta.

La unidad correcta pasa a ser:

```text
EVENTO DE APORTE
→ FUENTE / PROCEDENCIA
→ DESCUBRIMIENTO O RECEPCIÓN
→ INGESTA
→ CURACIÓN
→ RELACIÓN
→ CONTRADICCIÓN / CONTRASTE
→ SÍNTESIS
→ DELTA
→ IMPLEMENTACIÓN
→ FIJACIÓN
```

Cada función atribuible conserva su propia traza.

## 2. Regla fundamental de autoría

> **La procedencia de una señal no determina por sí sola la autoría del delta.**

NeoCronos™ debe distinguir, cuando existan:

- `source_originator` · autor/procedencia de la señal o material original;
- `discoverer` · quien encuentra la señal y reconoce que puede ser relevante;
- `receiver` · quien recibe una aportación dirigida al sistema;
- `manual_ingestor` · quien introduce manualmente el aporte en el sistema;
- `curator` · quien selecciona, contextualiza y prepara el material;
- `relation_author` · quien establece una relación nueva entre la señal y el corpus;
- `contradiction_author` · quien formula una objeción, tensión o contraejemplo;
- `synthesis_operator` · quien ejecuta trabajo de contraste y recomposición;
- `delta_author` · quien origina el cambio conceptual o funcional demostrable;
- `implementation_operator` · quien materializa técnicamente el cambio;
- `fixation_operator` · quien fija documental o técnicamente la nueva traza.

```text
FUENTE
≠ DESCUBRIDOR
≠ INGESTOR
≠ AUTOR DE LA RELACIÓN
≠ AUTOR DEL DELTA
≠ IMPLEMENTADOR
```

Una misma persona puede ocupar varias funciones. Varias personas pueden intervenir en el mismo evento. Ninguna de esas situaciones autoriza a borrar las demás genealogías.

## 3. Evento y créditos de traza

NeoCronos™ v0.3 separa:

### 3.1. Evento

El `NC-EVT-*` identifica el acontecimiento completo de aporte y transformación.

El evento conserva:

- fecha;
- procedencia;
- modo de ingesta;
- objeto;
- estado Umbral-X™;
- estado SAN™;
- delta global del evento;
- relaciones con Issues, documentos y commits;
- estado económico;
- créditos de función asociados.

### 3.2. Crédito de función

El `NC-CR-*` reconoce trabajo atribuible dentro del evento.

```text
NC-EVT-* = CONTENEDOR GENEALÓGICO DEL EVENTO
NC-CR-*  = CRÉDITO DE TRAZA DE UNA FUNCIÓN ATRIBUIBLE
```

No se asignan porcentajes económicos en esta fase. La traza registra qué hizo cada actor; una futura Economía del Aporte™ podrá valorar después las distintas funciones sin reescribir la historia.

## 4. Fase manual actual

WEB4™ todavía no permite que toda persona entre directamente en la Síntesis y registre por sí misma fuentes, relaciones, deltas y tiempo de trabajo.

Por ello, durante esta fase, gran parte de los aportes externos siguen este recorrido:

```text
SEÑAL EXTERNA
→ NEO0™ LA VE O LA RECIBE
→ NEO0™ DECIDE SI MERECE ENTRADA
→ NEO0™ LA INTRODUCE MANUALMENTE
→ NEO0™ LA RELACIONA CON EL CORPUS
→ NEO0™ + IA PUEDEN CONTRASTARLA
→ NEO0™ FIJA O ABRE EL DELTA
```

Cuando ese trabajo ocurre, debe registrarse.

Esto **no es un impuesto del fundador** ni convierte a Neo0™ en coautor de la idea externa. Reconoce trabajo real de ingestión, curación, contextualización, relación, contraste y fijación que actualmente no realiza todavía la infraestructura automática.

Cuando WEB4™ permita aportes directos, el modo podrá cambiar a:

```text
INGESTION_MODE = direct-web4
```

y la persona podrá ser ingestor y operador de su propio aporte sin intervención manual de Neo0™.

Modos previstos:

- `manual-neo0`;
- `direct-web4`;
- `api`;
- `imported`;
- `automated`.

## 5. Caso correctivo · Asilomar

La primera versión de esta rama creó erróneamente:

`NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR`.

Ese identificador queda **deprecado por atribución incorrecta**.

La genealogía correcta es:

```text
JOSÉ LUIS CASAL
→ autor/procedencia de una publicación vista en LinkedIn

NEO0™
→ descubre la publicación
→ reconoce su relevancia
→ introduce manualmente la información en SAN™
→ establece la relación ASILOMAR ↔ MARCO
→ abre el contraste
→ produce y fija el delta relacional
```

Por tanto, el evento pasa a ser:

`NC-EVT-2026-0005`.

Créditos:

- `NC-CR-2026-0005-A` · José Luis Casal · **source_originator** · crédito de procedencia, no autor del delta relacional;
- `NC-CR-2026-0005-B` · Pedro Martínez Alhambra · Neo0™ · **discoverer + manual_ingestor + curator + relation_author + synthesis_operator + delta_author + fixation_operator**.

La posterior formalización de RADAR-Π™ es otro evento porque constituye un delta distinto:

`NC-EVT-2026-0006`.

Así se preserva simultáneamente la fuente externa y el trabajo real que produjo la nueva relación.

## 6. Regla aplicable a todos los aportes externos de esta fase

El mismo criterio se aplica a Alfonso Calvo, David J. Gunkel, Hugo Roger Paz, feedback WEB4™, preguntas externas, correspondencia y futuras señales.

Ejemplo general:

```text
AUTOR EXTERNO
→ CRÍTICA / PREGUNTA / FUENTE ORIGINAL
→ CRÉDITO POR ESA FUNCIÓN

NEO0™
→ RECEPCIÓN / DESCUBRIMIENTO
→ INGESTA MANUAL
→ CURACIÓN
→ RELACIÓN CON EL MARCO
→ APERTURA / FIJACIÓN DE SÍNTESIS
→ CRÉDITO POR ESAS FUNCIONES

IA NEODIALÉCTICA
→ CONTRASTE / ESTRUCTURACIÓN / IMPLEMENTACIÓN CUANDO PROCEDA
→ CRÉDITO POR ESAS FUNCIONES
```

La existencia de trabajo de Neo0™ dentro de un evento no reduce el crédito del autor externo por aquello que efectivamente aportó.

## 7. Migración de los tokens planos existentes

Los antiguos `NC-2026-0001...0009` quedan conservados en `contributions.json` como **historial de migración**, no como modelo activo.

El caso Casal se marca específicamente `deprecated-misattribution`.

Los demás se marcan `deprecated-flat-model`: no necesariamente eran falsos en cuanto al origen de la señal, pero eran incompletos porque reducían un evento multirrol a una sola atribución.

```text
CORREGIR GENEALOGÍA
≠ BORRAR ERROR PREVIO

CORREGIR GENEALOGÍA
= CONSERVAR QUÉ SE ATRIBUYÓ
+ EXPLICAR POR QUÉ ERA INSUFICIENTE
+ FIJAR LA NUEVA RELACIÓN
```

## 8. Modelo mínimo de datos v0.3

```text
event_id                       # NC-EVT-*
date
ingestion_mode                 # manual-neo0 / direct-web4 / api / imported / automated
source_url
title.es
title.en
event_delta.es
event_delta.en
umbral_x
san_state
economic_state
credits[]
  credit_token_id              # NC-CR-*
  actor
  visibility
  roles[]
  work_es
  work_en
  token_state
```

En fases posteriores podrán añadirse:

```text
started_at
ended_at
neocronos_session
source_references[]
related_manifestos[]
related_neoaxioms[]
related_projects[]
delta_commits[]
assessment_history[]
implementation_evidence[]
economic_eligibility
privacy_notes
```

## 9. Token de traza y economía siguen separados

```text
CRÉDITO / TOKEN DE TRAZA
= RECONOCIMIENTO GENEALÓGICO
+ FUNCIÓN
+ TRABAJO DEMOSTRABLE
+ HISTORIAL

RETORNO ECONÓMICO
= CAPA POSTERIOR
+ VALORACIÓN
+ REGLAS
+ RESPALDO MATERIAL
+ LEGALIDAD / CONTABILIDAD
+ GOBERNANZA
```

Por tanto:

```text
TOKEN DE TRAZA
≠ VERDAD
≠ SOBERANÍA
≠ RANGO HUMANO
≠ EURO AUTOMÁTICO
≠ EQUITY
```

## 10. WEB4™ gamificada

WEB4™ debe representar el **evento completo** y permitir desplegar sus créditos internos.

Una tarjeta puede mostrar:

1. evento `NC-EVT-*`;
2. título y fecha;
3. modo de ingesta;
4. delta del evento;
5. Umbral-X™ y SAN™;
6. actores participantes;
7. funciones de cada actor;
8. créditos `NC-CR-*`;
9. fuente original;
10. Issue, documento y commits;
11. revaloraciones;
12. estado económico separado.

La gamificación no puede convertir un único número en medida de dignidad, autoridad o verdad.

## 11. Regla de auditoría retrospectiva

Para cualquier caso antiguo:

```text
¿QUÉ EXISTÍA ANTES?
+ ¿QUIÉN ORIGINÓ LA SEÑAL?
+ ¿QUIÉN LA DESCUBRIÓ O RECIBIÓ?
+ ¿QUIÉN LA INTRODUJO?
+ ¿QUIÉN ESTABLECIÓ LA RELACIÓN?
+ ¿QUIÉN HIZO EL CONTRASTE?
+ ¿QUIÉN PRODUJO EL DELTA?
+ ¿QUIÉN LO IMPLEMENTÓ?
+ ¿QUIÉN LO FIJÓ?
= EVENTO + CRÉDITOS DE FUNCIÓN
```

Si una función no puede demostrarse, no se atribuye.

## 12. Fuente de trazabilidad

Durante esta fase:

```text
ISSUE = ENTRADA Y CONTRASTE
DOCUMENTO = SÍNTESIS VERSIONADA
COMMIT = FIJACIÓN Y DELTA
NEOCRONOS™ = EVENTO + CRÉDITOS + TIEMPO + GENEALOGÍA
WEB4™ = EXPERIENCIA / JUEGO / VISUALIZACIÓN
```

---

# EN · English

## 1. Correction of the previous model

The first implementation in this branch used a flat model:

```text
ONE CONTRIBUTION
→ ONE CONTRIBUTOR
→ ONE TOKEN
```

That model is insufficient and is replaced.

A Synthesis event may contain several functions performed by different people. The person publishing information may not be the person who discovers its relation with the framework; the person discovering the relation may not be the implementation operator; and an AI may assist scrutiny without thereby becoming the human origin of the delta.

The correct unit becomes:

```text
CONTRIBUTION EVENT
→ SOURCE / PROVENANCE
→ DISCOVERY OR RECEPTION
→ INGESTION
→ CURATION
→ RELATION
→ CONTRADICTION / SCRUTINY
→ SYNTHESIS
→ DELTA
→ IMPLEMENTATION
→ FIXATION
```

Each attributable function preserves its own trace.

## 2. Fundamental authorship rule

> **The provenance of a signal does not by itself determine authorship of the delta.**

NeoCronos™ must distinguish, where they exist:

- `source_originator` · author/provenance of the original signal or material;
- `discoverer` · person who finds the signal and recognises possible relevance;
- `receiver` · person receiving a contribution addressed to the system;
- `manual_ingestor` · person manually introducing the contribution into the system;
- `curator` · person selecting, contextualising and preparing the material;
- `relation_author` · person establishing a new relation between signal and corpus;
- `contradiction_author` · person formulating an objection, tension or counterexample;
- `synthesis_operator` · person carrying out scrutiny and recomposition work;
- `delta_author` · person originating the demonstrable conceptual or functional change;
- `implementation_operator` · person technically materialising the change;
- `fixation_operator` · person documentarily or technically fixing the new trace.

```text
SOURCE
≠ DISCOVERER
≠ INGESTOR
≠ RELATION AUTHOR
≠ DELTA AUTHOR
≠ IMPLEMENTER
```

One person may occupy several functions. Several people may intervene in the same event. Neither situation authorises erasure of the other genealogies.

## 3. Event and trace credits

NeoCronos™ v0.3 separates:

### 3.1. Event

The `NC-EVT-*` identifies the complete contribution-and-transformation event.

The event preserves:

- date;
- provenance;
- ingestion mode;
- object;
- Umbral-X™ state;
- SAN™ state;
- global event delta;
- relations with Issues, documents and commits;
- economic state;
- associated role credits.

### 3.2. Role credit

The `NC-CR-*` recognises attributable work inside the event.

```text
NC-EVT-* = GENEALOGICAL EVENT CONTAINER
NC-CR-*  = TRACE CREDIT FOR AN ATTRIBUTABLE FUNCTION
```

No economic percentages are assigned at this stage. Trace records what each actor did; a future Contribution Economy™ may later value different functions without rewriting history.

## 4. Current manual phase

WEB4™ does not yet allow every person to enter Synthesis directly and independently record sources, relations, deltas and working time.

Therefore, during this phase, many external contributions follow this path:

```text
EXTERNAL SIGNAL
→ NEO0™ SEES OR RECEIVES IT
→ NEO0™ DECIDES WHETHER IT MERITS ENTRY
→ NEO0™ MANUALLY INGESTS IT
→ NEO0™ RELATES IT TO THE CORPUS
→ NEO0™ + AI MAY SCRUTINISE IT
→ NEO0™ FIXES OR OPENS THE DELTA
```

When this work occurs, it must be recorded.

This is **not a founder tax** and does not make Neo0™ co-author of the external idea. It recognises real ingestion, curation, contextualisation, relation, scrutiny and fixation work that the automated infrastructure does not yet perform.

When WEB4™ supports direct contributions, the mode may become:

```text
INGESTION_MODE = direct-web4
```

and the person may become ingestor and operator of their own contribution without manual Neo0™ intervention.

Planned modes:

- `manual-neo0`;
- `direct-web4`;
- `api`;
- `imported`;
- `automated`.

## 5. Corrective case · Asilomar

The first branch version incorrectly created:

`NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR`.

That identifier is **deprecated for incorrect attribution**.

The correct genealogy is:

```text
JOSÉ LUIS CASAL
→ author/provenance of a publication seen on LinkedIn

NEO0™
→ discovers the publication
→ recognises its relevance
→ manually introduces the information into SAN™
→ establishes the ASILOMAR ↔ FRAMEWORK relation
→ opens scrutiny
→ produces and fixes the relational delta
```

Therefore, the event becomes:

`NC-EVT-2026-0005`.

Credits:

- `NC-CR-2026-0005-A` · José Luis Casal · **source_originator** · provenance credit, not author of the relational delta;
- `NC-CR-2026-0005-B` · Pedro Martínez Alhambra · Neo0™ · **discoverer + manual_ingestor + curator + relation_author + synthesis_operator + delta_author + fixation_operator**.

The later formalisation of RADAR-Π™ is another event because it constitutes a distinct delta:

`NC-EVT-2026-0006`.

This simultaneously preserves the external source and the actual work producing the new relation.

## 6. Rule applying to all external contributions in this phase

The same criterion applies to Alfonso Calvo, David J. Gunkel, Hugo Roger Paz, WEB4™ feedback, external questions, correspondence and future signals.

General example:

```text
EXTERNAL AUTHOR
→ ORIGINAL CRITICISM / QUESTION / SOURCE
→ CREDIT FOR THAT FUNCTION

NEO0™
→ RECEPTION / DISCOVERY
→ MANUAL INGESTION
→ CURATION
→ RELATION WITH THE FRAMEWORK
→ OPENING / FIXING SYNTHESIS
→ CREDIT FOR THOSE FUNCTIONS

NEODIALECTICAL AI
→ SCRUTINY / STRUCTURING / IMPLEMENTATION WHERE APPLICABLE
→ CREDIT FOR THOSE FUNCTIONS
```

The existence of Neo0™ work inside an event does not reduce the external author's credit for what they actually contributed.

## 7. Migration of existing flat tokens

The former `NC-2026-0001...0009` identifiers are preserved in `contributions.json` as **migration history**, not as the active model.

The Casal case is specifically marked `deprecated-misattribution`.

The others are marked `deprecated-flat-model`: they were not necessarily false regarding signal origin, but they were incomplete because they reduced a multi-role event to one attribution.

```text
CORRECTING GENEALOGY
≠ ERASING THE PREVIOUS ERROR

CORRECTING GENEALOGY
= PRESERVING WHAT WAS ATTRIBUTED
+ EXPLAINING WHY IT WAS INSUFFICIENT
+ FIXING THE NEW RELATION
```

## 8. Minimum data model v0.3

```text
event_id                       # NC-EVT-*
date
ingestion_mode                 # manual-neo0 / direct-web4 / api / imported / automated
source_url
title.es
title.en
event_delta.es
event_delta.en
umbral_x
san_state
economic_state
credits[]
  credit_token_id              # NC-CR-*
  actor
  visibility
  roles[]
  work_es
  work_en
  token_state
```

Later phases may add:

```text
started_at
ended_at
neocronos_session
source_references[]
related_manifestos[]
related_neoaxioms[]
related_projects[]
delta_commits[]
assessment_history[]
implementation_evidence[]
economic_eligibility
privacy_notes
```

## 9. Trace token and economy remain separate

```text
TRACE CREDIT / TOKEN
= GENEALOGICAL RECOGNITION
+ FUNCTION
+ DEMONSTRABLE WORK
+ HISTORY

ECONOMIC RETURN
= LATER LAYER
+ VALUATION
+ RULES
+ MATERIAL BACKING
+ LEGALITY / ACCOUNTING
+ GOVERNANCE
```

Therefore:

```text
TRACE TOKEN
≠ TRUTH
≠ SOVEREIGNTY
≠ HUMAN RANK
≠ AUTOMATIC EURO
≠ EQUITY
```

## 10. Gamified WEB4™

WEB4™ must represent the **complete event** and allow its internal credits to be expanded.

A card may display:

1. `NC-EVT-*` event;
2. title and date;
3. ingestion mode;
4. event delta;
5. Umbral-X™ and SAN™;
6. participating actors;
7. each actor's functions;
8. `NC-CR-*` credits;
9. original source;
10. Issue, document and commits;
11. reassessments;
12. separate economic state.

Gamification must not turn a single number into a measure of dignity, authority or truth.

## 11. Retrospective audit rule

For every historical case:

```text
WHAT EXISTED BEFORE?
+ WHO ORIGINATED THE SIGNAL?
+ WHO DISCOVERED OR RECEIVED IT?
+ WHO INGESTED IT?
+ WHO ESTABLISHED THE RELATION?
+ WHO PERFORMED SCRUTINY?
+ WHO PRODUCED THE DELTA?
+ WHO IMPLEMENTED IT?
+ WHO FIXED IT?
= EVENT + ROLE CREDITS
```

If a function cannot be demonstrated, it is not attributed.

## 12. Traceability source

During this phase:

```text
ISSUE = ENTRY AND SCRUTINY
DOCUMENT = VERSIONED SYNTHESIS
COMMIT = FIXATION AND DELTA
NEOCRONOS™ = EVENT + CREDITS + TIME + GENEALOGY
WEB4™ = EXPERIENCE / GAME / VISUALISATION
```
