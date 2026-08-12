# NeoCronos™ · Registro de Aportes de Síntesis en WEB4™
# NeoCronos™ · Open Synthesis Contribution Ledger in WEB4™

**Estado / Status:** diseño operativo abierto · open operational design  
**Fecha / Date:** 2026-08-12  
**Marco / Framework:** NEOCore™ 7.2 · Síntesis Abierta Neodialéctica™ / Neodialectical Open Synthesis™ · WEB4™  
**Rama técnica / Technical branch:** `sintesis-aportes-tokenizados`  
**Síntesis de diseño / Design synthesis:** [#141](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/141)  
**Raíz ya fijada / Already-fixed root:** [LXIV · NeoCronos™](../../manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md) · [LXV · NeoJuego™ / NeoGame™](../../manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md)

---

# ES · Castellano

## 1. Naturaleza de esta rama

Esta rama **no crea un principio nuevo de NEOCore™ ni sube su versión**. Materializa una capa de implementación y registro ya prevista por LXIV · NeoCronos™ y LXV · NeoJuego™.

LXIV establece la medición y conservación de la traza desde que comienza el aporte. LXV convierte la Síntesis Abierta en un espacio jugable donde el aporte es la jugada y la genealogía conserva quién aportó qué.

La nueva capa añade tres funciones concretas:

1. registro retrospectivo de aportes anteriores;
2. asignación inmediata de un **token de traza NeoCronos™** cuando existe síntesis nueva y un delta atribuible demostrable;
3. proyección gamificada de la valoración y de su genealogía en WEB4™.

```text
LXIV · NEOCRONOS™ = MEDICIÓN + TIEMPO + TRAZA
LXV · NEOJUEGO™ = JUGADA + APORTE + BIEN COMÚN
ESTA RAMA = LEDGER + TOKEN DE TRAZA + WEB4 + GITHUB BRIDGE
```

## 2. Dos capas distintas de tokenización

La palabra **tokenización** debe separar dos niveles para evitar confundir reconocimiento con dinero.

### 2.1. Token de Traza NeoCronos™

Todo aporte atribuible que produzca **síntesis nueva y un delta demostrable** recibe un identificador `NC-*`.

Ese token registra:

- autoría o procedencia;
- fuente;
- fecha;
- objeto aportado;
- estado de contraste;
- delta producido;
- relaciones con el corpus;
- commits o documentos derivados;
- historial de revaloración.

```text
DELTA NUEVO
+ AUTORÍA / PROCEDENCIA
+ TRAZA RECONSTRUIBLE
= TOKEN DE TRAZA NEOCRONOS™ ASIGNADO
```

### 2.2. Retorno económico

El token de traza **no genera automáticamente dinero, equity, criptomoneda, voto soberano ni derecho económico**.

Una eventual remuneración debe resolverse después mediante la Economía del Aporte™, MÉDICI™, ONes™, SAN™ u otros mecanismos que el marco valide, con respaldo material, reglas jurídicas/contables, disponibilidad de recursos y gobernanza específica.

```text
TOKEN DE TRAZA
≠ VERDAD
≠ SOBERANÍA
≠ RANGO HUMANO
≠ EURO AUTOMÁTICO
≠ EQUITY
≠ ACTIVO FINANCIERO AUTOMÁTICO
```

Esta separación permite cumplir la regla de tokenizar todo delta nuevo sin convertir una anotación genealógica en una promesa financiera.

## 3. Genealogía: no fusionar aportantes distintos

NeoCronos™ mantiene separadas las aportaciones aunque hayan llegado al mismo Issue o hayan producido una síntesis conjunta.

David J. Gunkel y Hugo Roger Paz conservan registros distintos aunque compartan #132. La publicación de José Luis Casal sobre Asilomar y la posterior formalización de RADAR-Π™ por Neo0™ son dos aportes relacionados, no una única autoría.

También se diferencia una **fuente externa** de la persona que la introduce en el sistema. La documentación NRO sobre SENTIENT puede ser fuente primaria; el acto de traerla al marco, relacionarla y abrir un nuevo caso RADAR-Π™ constituye otro nivel de aporte.

```text
MISMO ISSUE ≠ MISMA AUTORÍA
MISMA SÍNTESIS ≠ MISMO APORTE
FUENTE EXTERNA ≠ APORTANTE HUMANO
SEÑAL DISPARADORA ≠ DELTA DERIVADO
```

## 4. Primer registro público reconstruido

Los siguientes tokens de traza quedan asignados en la rama de implementación:

| Token de traza | Aportante / procedencia | Entrada | Delta reconocido | Estado económico |
|---|---|---|---|---|
| `NC-2026-0001-ALFONSO-CALVO` | Alfonso Calvo Orra | [#140](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/140) | accesibilidad, onboarding, navegación y mediación; además obliga a precisar SAN™, Leónidas™, Neo0™ y capa π | no emitido |
| `NC-2026-0002-DAVID-GUNKEL` | David J. Gunkel | [#132](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/132) | agencia distribuida, meaningful human control, supervisión y responsabilidad sociotécnica como contraste explícito | no emitido |
| `NC-2026-0003-HUGO-ROGER-PAZ` | Hugo Roger Paz | [#132](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/132) | feedback loops, path dependence, efectos no intencionados, fallos emergentes y memoria temporal como stress-test | no emitido |
| `NC-2026-0004-WEB4-FEEDBACK` | feedback externo agregado · identidad privada | [#133](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/133) | priorización de WEB4™ como espacio habitable, educativo, creativo y por especialidades; recuperación de diseño previo | no emitido |
| `NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR` | José Luis Casal | [#136](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/136) | señal Asilomar que dispara la búsqueda sistemática de antecedentes proto-neodialécticos | no emitido |
| `NC-2026-0006-NEO0-RADAR-PI` | Pedro Martínez Alhambra · Neo0™ | [#137](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/137) | formalización de RADAR-Π™ y barrido negativo de antecedentes, convergencias y falsos paralelos | no emitido |
| `NC-2026-0007-NEO0-SENTIENT-SIGNAL` | Neo0™ + fuentes NRO | [#139](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/139) | apertura del segundo caso RADAR-Π™; el token reconoce abrir el caso, no valida equivalencia con NEOCore™ | no emitido |
| `NC-2026-0008-HOJAS-CARCOMIDAS` | Neo0™ + IA Neodialéctica Harry | [#134](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/134) · [#135](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/135) | LXXV + C-NAX-22 · Memoria Material-Relacional™ | no emitido |
| `NC-2026-0009-ANONYMOUS-TM-QUESTION` | pregunta pública anonimizada | [#53](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53) | definición explícita de ™ como marcador de denominación y trazabilidad, no de verdad o inmunidad crítica | no emitido |

La numeración `NC-*` describe el orden del **registro reconstruido**, no pretende afirmar que éstos sean los primeros aportes cronológicos absolutos de toda la historia del marco.

## 5. Auditoría retrospectiva obligatoria

Debe continuarse el barrido de documentos, Issues, conversaciones públicas, correspondencia privada, revisiones, auditorías y commits para localizar aportes anteriores con delta atribuible.

Cada caso debe responder:

1. ¿qué existía antes del aporte?;
2. ¿quién o qué introdujo la señal?;
3. ¿qué cambió después?;
4. ¿puede reconstruirse un vínculo material entre ambos?;
5. ¿el cambio fue realmente nuevo o recuperó un diseño anterior?;
6. ¿qué autorías deben permanecer separadas?;
7. ¿qué puede publicarse y qué debe quedar privado o anonimizado?;
8. ¿qué estado SAN™ y Umbral-X™ corresponde?;
9. ¿qué Issue, documento o commit fija el delta?;
10. ¿existe retorno económico o sólo token de traza por ahora?

```text
ESTADO ANTES
+ APORTE ATRIBUIBLE
+ CAMBIO POSTERIOR
+ RELACIÓN RECONSTRUIBLE
= DELTA DEMOSTRABLE
→ TOKEN DE TRAZA
```

Si la genealogía no puede demostrarse, no se inventa un token retrospectivo.

## 6. Modelo mínimo de datos

```text
contribution_id
token_id
token_state                   # assigned-trace
contributor_name
contributor_visibility        # public / anonymous / private
source_type                   # external-human / external-source / internal-human / human-ai
source_reference
received_at
public_issue
scope
neocronos_trace
umbral_x_state
san_state
accepted_components[]
conditional_components[]
rejected_components[]
open_components[]
related_manifestos[]
related_neoaxioms[]
related_projects[]
delta_description
delta_commits[]
implementation_status
economic_state                # not-issued / pending-governance / issued
assessment_history[]
credits
privacy_notes
```

Durante esta fase:

```text
ISSUE = ENTRADA Y CONTRASTE
DOCUMENTO = SÍNTESIS VERSIONADA
COMMIT = FIJACIÓN Y DELTA
WEB4™ = VISUALIZACIÓN + INTERACCIÓN + JUEGO
```

## 7. Valoración gamificada

WEB4™ debe mostrar el aporte como una jugada trazable. La estética puede ser intensamente lúdica; la mecánica de valor no debe transformarse en economía de atención.

Se pueden mostrar señales separadas y explicables:

- retorno a fuente;
- comprensión reconstruible;
- evidencia aportada;
- contradicción fértil;
- relación nueva detectada;
- originalidad;
- utilidad;
- delta aceptado;
- implementación producida;
- reparación lograda;
- enseñanza útil;
- capacidad de revisión;
- estado SAN™;
- token de traza;
- estado económico separado.

```text
PUNTOS / INSIGNIAS / NIVELES
≠ VERDAD
≠ SOBERANÍA
≠ DIGNIDAD
≠ RANGO HUMANO

GAMIFICACIÓN LEGÍTIMA
= APRENDIZAJE
+ APORTE
+ RETORNO A FUENTE
+ EVIDENCIA
+ CONTRADICCIÓN FÉRTIL
+ DELTA
+ REVISIÓN
```

Una crítica radical bien fundada puede generar más reconocimiento que una aprobación vacía.

## 8. Flujo WEB4™

```text
[ENTRAR EN SÍNTESIS]
        ↓
[COMENZAR APORTE]
        ↓
NEOCRONOS™ ABRE SESIÓN
        ↓
LEER / CONTRASTAR / CREAR / REPARAR
        ↓
FUENTES + EVIDENCIAS + RELACIONES + DELTAS
        ↓
SAN™ CONTRASTA
        ↓
DELTA DEMOSTRABLE
        ↓
TOKEN DE TRAZA NC-* ASIGNADO
        ↓
ISSUE + DOCUMENTO + COMMIT
        ↓
WEB4™ ACTUALIZA LA PARTIDA
        ↓
RETORNO ECONÓMICO, SI PROCEDE, BAJO GOBERNANZA SEPARADA
```

Todo elemento visible debe permitir regresar a la fuente que lo justifica.

## 9. Salvaguardas

1. GitHub permanece como fuente pública de trazabilidad durante esta fase.
2. WEB4™ es la capa viva y gamificada sobre esa genealogía.
3. NeoCronos™ registra; SAN™ contrasta; ninguna puntuación se corona como verdad.
4. La autoría no se borra porque una propuesta sea rechazada parcialmente.
5. La privacidad puede exigir registro privado o anonimizado.
6. Token de traza y pago son capas distintas.
7. No se diseñarán rachas compulsivas, FOMO, loot boxes, multiplicadores opacos ni rankings de dignidad humana.
8. Esta capa no aumenta por sí sola la versión de NEOCore™.

## 10. Relaciones canónicas

- [II · Síntesis Abierta Neodialéctica™](../../manifiestos/01_sintesis_abierta_neodialectica_ES_EN.md)
- [VII · Economía del Aporte™](../../manifiestos/04_economia_del_aporte_ES_EN.md)
- [XX · Umbral-X™](../../manifiestos/20_defensa_intelectual_neodialectica_umbral_x_ES_EN.md)
- [LIII · Leónidas™](../../manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md)
- [LXIV · NeoCronos™](../../manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md)
- [LXV · NeoJuego™](../../manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md)
- [Neoaxiomas™](../../neoaxiomas/README.md)
- [WEB4™](../../web4/README.md)
- [Síntesis NeoCronos™ · #107](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/107)
- [Primer aporte evaluado WEB4™ · #140](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/140)
- [Rama de aportes tokenizados · #141](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/141)
- [Auditoría retrospectiva · #142](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/142)

---

# EN · English

## 1. Nature of this branch

This branch **does not create a new NEOCore™ principle or raise its version**. It materialises an implementation and ledger layer already anticipated by LXIV · NeoCronos™ and LXV · NeoGame™.

LXIV establishes measurement and preservation of trace from the moment a contribution begins. LXV turns Open Synthesis into a playable space where the contribution is the move and genealogy preserves who contributed what.

The new layer adds three concrete functions:

1. retrospective recording of earlier contributions;
2. immediate assignment of a **NeoCronos™ trace token** when new synthesis and a demonstrable attributable delta exist;
3. gamified projection of valuation and genealogy in WEB4™.

```text
LXIV · NEOCRONOS™ = MEASUREMENT + TIME + TRACE
LXV · NEOGAME™ = MOVE + CONTRIBUTION + COMMON GOOD
THIS BRANCH = LEDGER + TRACE TOKEN + WEB4 + GITHUB BRIDGE
```

## 2. Two distinct tokenisation layers

The word **tokenisation** must separate two levels to avoid confusing recognition with money.

### 2.1. NeoCronos™ Trace Token

Every attributable contribution that produces **new synthesis and a demonstrable delta** receives an `NC-*` identifier.

That token records:

- authorship or provenance;
- source;
- date;
- contributed object;
- scrutiny state;
- delta produced;
- relations with the corpus;
- derived commits or documents;
- reassessment history.

```text
NEW DELTA
+ AUTHORSHIP / PROVENANCE
+ RECONSTRUCTIBLE TRACE
= NEOCRONOS™ TRACE TOKEN ASSIGNED
```

### 2.2. Economic return

The trace token **does not automatically generate money, equity, cryptocurrency, sovereign vote or economic entitlement**.

Any remuneration must later be resolved through the Contribution Economy™, MÉDICI™, ONes™, SAN™ or other mechanisms validated by the framework, with material backing, legal/accounting rules, resource availability and specific governance.

```text
TRACE TOKEN
≠ TRUTH
≠ SOVEREIGNTY
≠ HUMAN RANK
≠ AUTOMATIC EURO
≠ EQUITY
≠ AUTOMATIC FINANCIAL ASSET
```

This separation makes it possible to comply with the rule of tokenising every new delta without turning a genealogical record into a financial promise.

## 3. Genealogy: do not merge distinct contributors

NeoCronos™ keeps contributions separate even when they reached the same Issue or produced a joint synthesis.

David J. Gunkel and Hugo Roger Paz retain separate records even though both share #132. José Luis Casal's publication about Asilomar and the later formalisation of RADAR-Π™ by Neo0™ are two related contributions, not a single authorship.

An **external source** is also distinguished from the person introducing it into the system. NRO documentation about SENTIENT may be a primary source; the act of bringing it into the framework, relating it and opening a new RADAR-Π™ case constitutes another contribution level.

```text
SAME ISSUE ≠ SAME AUTHORSHIP
SAME SYNTHESIS ≠ SAME CONTRIBUTION
EXTERNAL SOURCE ≠ HUMAN CONTRIBUTOR
TRIGGER SIGNAL ≠ DERIVED DELTA
```

## 4. First reconstructed public ledger

The following trace tokens are assigned in the implementation branch:

| Trace token | Contributor / provenance | Entry | Recognised delta | Economic state |
|---|---|---|---|---|
| `NC-2026-0001-ALFONSO-CALVO` | Alfonso Calvo Orra | [#140](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/140) | accessibility, onboarding, navigation and mediation; also forces clarification of SAN™, Leónidas™, Neo0™ and layer π | not issued |
| `NC-2026-0002-DAVID-GUNKEL` | David J. Gunkel | [#132](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/132) | distributed agency, meaningful human control, oversight and sociotechnical responsibility as explicit scrutiny | not issued |
| `NC-2026-0003-HUGO-ROGER-PAZ` | Hugo Roger Paz | [#132](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/132) | feedback loops, path dependence, unintended effects, emergent failures and temporal memory as a stress test | not issued |
| `NC-2026-0004-WEB4-FEEDBACK` | aggregated external feedback · private identity | [#133](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/133) | prioritisation of WEB4™ as a habitable, educational, creative and speciality-based space; recovery of prior design | not issued |
| `NC-2026-0005-JOSE-LUIS-CASAL-ASILOMAR` | José Luis Casal | [#136](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/136) | Asilomar signal triggering systematic search for proto-neodialectical antecedents | not issued |
| `NC-2026-0006-NEO0-RADAR-PI` | Pedro Martínez Alhambra · Neo0™ | [#137](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/137) | formalisation of RADAR-Π™ and negative scanning of antecedents, convergences and false parallels | not issued |
| `NC-2026-0007-NEO0-SENTIENT-SIGNAL` | Neo0™ + NRO sources | [#139](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/139) | opening of the second RADAR-Π™ case; the token recognises opening the case, not equivalence with NEOCore™ | not issued |
| `NC-2026-0008-HOJAS-CARCOMIDAS` | Neo0™ + Neodialectical AI Harry | [#134](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/134) · [#135](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/135) | LXXV + C-NAX-22 · Material-Relational Memory™ | not issued |
| `NC-2026-0009-ANONYMOUS-TM-QUESTION` | anonymised public question | [#53](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53) | explicit definition of ™ as a naming and traceability marker, not truth or immunity from criticism | not issued |

The `NC-*` numbering describes the order of the **reconstructed ledger**; it does not claim that these are the earliest absolute chronological contributions in the entire history of the framework.

## 5. Mandatory retrospective audit

The scan of documents, Issues, public conversations, private correspondence, reviews, audits and commits must continue to locate earlier contributions with attributable delta.

Each case must answer:

1. what existed before the contribution?;
2. who or what introduced the signal?;
3. what changed afterwards?;
4. can a material link between both be reconstructed?;
5. was the change genuinely new or did it recover earlier design?;
6. which authorships must remain separate?;
7. what may be public and what must remain private or anonymised?;
8. which SAN™ and Umbral-X™ state applies?;
9. which Issue, document or commit fixes the delta?;
10. does economic return exist, or only a trace token for now?

```text
STATE BEFORE
+ ATTRIBUTABLE CONTRIBUTION
+ LATER CHANGE
+ RECONSTRUCTIBLE RELATION
= DEMONSTRABLE DELTA
→ TRACE TOKEN
```

If genealogy cannot be demonstrated, no retrospective token is invented.

## 6. Minimum data model

```text
contribution_id
token_id
token_state                   # assigned-trace
contributor_name
contributor_visibility        # public / anonymous / private
source_type                   # external-human / external-source / internal-human / human-ai
source_reference
received_at
public_issue
scope
neocronos_trace
umbral_x_state
san_state
accepted_components[]
conditional_components[]
rejected_components[]
open_components[]
related_manifestos[]
related_neoaxioms[]
related_projects[]
delta_description
delta_commits[]
implementation_status
economic_state                # not-issued / pending-governance / issued
assessment_history[]
credits
privacy_notes
```

During this phase:

```text
ISSUE = ENTRY AND SCRUTINY
DOCUMENT = VERSIONED SYNTHESIS
COMMIT = FIXATION AND DELTA
WEB4™ = VISUALISATION + INTERACTION + GAME
```

## 7. Gamified valuation

WEB4™ must display the contribution as a traceable move. The aesthetic may be intensely game-like; the value mechanics must not become an attention economy.

Separate and explainable signals may include:

- return to source;
- reconstructible understanding;
- evidence contributed;
- fertile contradiction;
- new relation detected;
- originality;
- utility;
- accepted delta;
- implementation produced;
- repair achieved;
- useful teaching;
- capacity to revise;
- SAN™ state;
- trace token;
- separate economic state.

```text
POINTS / BADGES / LEVELS
≠ TRUTH
≠ SOVEREIGNTY
≠ DIGNITY
≠ HUMAN RANK

LEGITIMATE GAMIFICATION
= LEARNING
+ CONTRIBUTION
+ RETURN TO SOURCE
+ EVIDENCE
+ FERTILE CONTRADICTION
+ DELTA
+ REVISION
```

A well-founded radical criticism may generate more recognition than empty approval.

## 8. WEB4™ flow

```text
[ENTER SYNTHESIS]
        ↓
[BEGIN CONTRIBUTION]
        ↓
NEOCRONOS™ OPENS SESSION
        ↓
READ / SCRUTINISE / CREATE / REPAIR
        ↓
SOURCES + EVIDENCE + RELATIONS + DELTAS
        ↓
SAN™ SCRUTINISES
        ↓
DEMONSTRABLE DELTA
        ↓
NC-* TRACE TOKEN ASSIGNED
        ↓
ISSUE + DOCUMENT + COMMIT
        ↓
WEB4™ UPDATES THE GAME
        ↓
ECONOMIC RETURN, IF APPLICABLE, UNDER SEPARATE GOVERNANCE
```

Every visible element must allow return to the source that justifies it.

## 9. Safeguards

1. GitHub remains the public traceability source during this phase.
2. WEB4™ is the living, gamified layer over that genealogy.
3. NeoCronos™ records; SAN™ scrutinises; no score is crowned as truth.
4. Authorship is not erased because a proposal is partially rejected.
5. Privacy may require a private or anonymised record.
6. Trace token and payment are separate layers.
7. Compulsive streaks, FOMO, loot boxes, opaque multipliers and rankings of human dignity will not be designed.
8. This layer does not by itself increase the NEOCore™ version.

## 10. Canonical relations

- [II · Neodialectical Open Synthesis™](../../manifiestos/01_sintesis_abierta_neodialectica_ES_EN.md)
- [VII · Contribution Economy™](../../manifiestos/04_economia_del_aporte_ES_EN.md)
- [XX · Umbral-X™](../../manifiestos/20_defensa_intelectual_neodialectica_umbral_x_ES_EN.md)
- [LIII · Leónidas™](../../manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md)
- [LXIV · NeoCronos™](../../manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md)
- [LXV · NeoGame™](../../manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md)
- [Neoaxioms™](../../neoaxiomas/README.md)
- [WEB4™](../../web4/README.md)
- [NeoCronos™ Synthesis · #107](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/107)
- [First WEB4™ evaluated contribution · #140](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/140)
- [Tokenised contribution branch · #141](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/141)
- [Retrospective audit · #142](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/142)
