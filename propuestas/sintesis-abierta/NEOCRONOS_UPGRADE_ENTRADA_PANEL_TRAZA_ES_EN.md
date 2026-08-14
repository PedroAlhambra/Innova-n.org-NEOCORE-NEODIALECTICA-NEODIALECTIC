# NeoCronos™ · Upgrade de entrada, traza de aporte y panel de visualización
# NeoCronos™ · Entry Upgrade, Contribution Trace and Visualisation Panel

**Fecha / Date:** 2026-08-10  
**Estado / Status:** SÍNTESIS ABIERTA · especificación funcional v0.2 / OPEN SYNTHESIS · functional specification v0.2  
**Síntesis específica / Dedicated synthesis:** [Issue #107](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/107)

## ES · Corrección funcional

**NeoCronos™ es el sistema de medición del Juego de la Síntesis Abierta™.**

No es solamente un registro de horas ni una capa económica posterior. Debe activarse desde la **entrada al juego**, abrir una traza de aporte y acompañar el recorrido del participante hasta que el aporte sea contrastado, clasificado y, cuando proceda, recompensado.

```text
ENTRAR EN LA SÍNTESIS
        ↓
IDENTIFICAR OBJETO / RETO
        ↓
INICIAR NEOCRONOS™
        ↓
TRAZA NC-*
        ↓
LEER / CONTRASTAR / CREAR / REPARAR / SINTETIZAR
        ↓
REGISTRAR EVIDENCIA Y DELTA
        ↓
CIERRE DE SESIÓN
        ↓
VALIDACIÓN SAN™
        ↓
VALOR DE APORTE
        ↓
TOKENIZACIÓN / RETORNO / MEMORIA
```

### Entrada v0.2

La puerta pública de Síntesis debe permitir, con el mínimo coste cognitivo:

1. **Entrar sin minar**: leer, explorar y aprender sin iniciar ninguna traza.
2. **Entrar a aportar**: iniciar voluntariamente una sesión NeoCronos™.
3. Elegir o indicar el **objeto de Síntesis**: issue, manifiesto, neoaxioma, problema, auditoría, código, traducción, propuesta u otro nodo.
4. Declarar un **alias/identidad de aporte** compatible con la futura capa de identidad del sistema.
5. Elegir el **tipo inicial de aporte**: contradicción, evidencia, fuente, idea, código, prueba, traducción, mantenimiento, cuidado, síntesis, reparación u otro.
6. Iniciar una traza `NC-*` con fecha/hora de comienzo y objeto.
7. Mostrar claramente que **tiempo ≠ token automático** y que toda recompensa depende de aporte validado y reglas vigentes.

### Traza NeoCronos™

La traza debe ser event-sourced: en vez de guardar sólo un total final, registra hitos suficientes para reconstruir el proceso sin vigilancia continua.

Eventos candidatos:

```text
NC_SESSION_OPENED
SOURCE_OPENED
OBJECT_SELECTED
SOURCE_ADDED
NOTE_ADDED
HYPOTHESIS_ADDED
CONTRADICTION_FOUND
DELTA_PROPOSED
EVIDENCE_ADDED
COMMIT_LINKED
ISSUE_LINKED
PAUSE
RESUME
SESSION_CLOSED
SAN_REVIEWED
VALUE_ASSIGNED
TOKEN_ELIGIBLE
TOKEN_ASSIGNED
REWARD_PAID
REOPENED
```

### Panel NeoCronos™

El participante debe poder ver su contribución como proceso, no como simple puntuación.

Panel mínimo:

```text
┌────────────────────────────────────────────────────┐
│ NEOCRONOS™ · JUEGO DE LA SÍNTESIS                 │
├────────────────────────────────────────────────────┤
│ Sesión activa        00:42:16                      │
│ Traza                NC-20260810-...               │
│ Objeto               Síntesis #...                 │
│ Estado               EN CONTRASTE                  │
├────────────────────────────────────────────────────┤
│ Tiempo trazado       42 min                        │
│ Evidencias           3                             │
│ Fuentes              2                             │
│ Deltas               1                             │
│ Relaciones nuevas    4                             │
├────────────────────────────────────────────────────┤
│ Valor SAN            PENDIENTE                     │
│ Token elegible       PENDIENTE                     │
│ Recompensa           NO ASIGNADA                   │
└────────────────────────────────────────────────────┘
```

La interfaz no debe fabricar una falsa precisión de valor antes de validación. Durante el trabajo pueden mostrarse **métricas descriptivas**, nunca una recompensa prometida.

### Panel colectivo

Una segunda vista debe mostrar el estado agregado del Juego sin convertirlo en ranking adictivo:

- sesiones abiertas/cerradas;
- tiempo útil validado agregado;
- aportes pendientes de contraste;
- aportes aceptados, parciales y rechazados;
- tipos de contribución;
- nodos con mayor necesidad de contraste;
- deltas producidos;
- reparaciones realizadas;
- tokens elegibles/asignados cuando exista esa capa;
- fondo de retorno disponible cuando legal y operacionalmente proceda.

**No usar por defecto:** leaderboard de personas por horas, rachas compulsivas, FOMO, recompensas aleatorias, multiplicadores opacos o patrones de casino.

### Unidad de juego

La unidad básica no es la hora; es la **sesión de aporte trazable**.

```text
SESIÓN NEOCRONOS™ =
IDENTIDAD/ALIAS
+ OBJETO
+ INTERVALO TEMPORAL
+ EVENTOS
+ EVIDENCIAS
+ RESULTADO
+ ESTADO SAN
+ DELTA
+ RETORNO SI PROCEDE
```

Una sesión puede durar cinco minutos y ser extraordinariamente valiosa; otra puede durar horas y no generar aporte validado.

### Encaje con Registro de Entrada Trazable

NeoCronos™ no sustituye el Registro de Entrada Trazable y Derivación existente. Lo **instrumenta temporalmente**.

```text
REGISTRO DE ENTRADA
= qué llegó + de dónde + a qué nodo se deriva

NEOCRONOS™
= quién dedica tiempo + a qué objeto + qué proceso realiza + qué resultado deja

SAN™
= qué parte del resultado resiste contraste

ECONOMÍA DEL APORTE™
= qué reconocimiento/retorno corresponde
```

### Privacidad

- cronometraje explícito y voluntario;
- pausa real;
- edición declarativa del tiempo cuando sea necesario;
- trazabilidad de correcciones;
- sin keylogging;
- sin captura de pantalla permanente;
- sin vigilancia biométrica;
- posibilidad de trabajar sin sesión NeoCronos™;
- separar identidad pública, alias y datos necesarios para eventual pago.

### Fases de implementación

**v0.2 · DEMO WEB4™**  
Panel local en navegador. Inicia/pausa/cierra sesión, guarda trazas localmente y permite exportar JSON. No emite tokens ni realiza pagos.

**v0.3 · GitHub bridge**  
Vinculación voluntaria de Issue/commit/PR/documento y generación de prueba de aporte.

**v0.4 · SAN validator**  
Estados `pending / accepted / partial / rejected`, evaluación relacional y trazabilidad de revisiones.

**v0.5 · Token eligibility**  
Transformación de aporte validado en elegibilidad según tokenomics aprobada mediante Síntesis Abierta.

**v1.0 · Fondo de Retorno**  
Recompensa material únicamente cuando exista infraestructura jurídica, financiera, contable y técnica validada.

---

## EN · Functional correction

**NeoCronos™ is the measurement system of the Open Synthesis Game™.**

It is not merely a log of hours or a later economic layer. It should activate from the **entry into the game**, open a contribution trace and accompany the participant's path until the contribution has been challenged, classified and, where appropriate, rewarded.

```text
ENTER THE SYNTHESIS
        ↓
IDENTIFY OBJECT / CHALLENGE
        ↓
START NEOCRONOS™
        ↓
NC-* TRACE
        ↓
READ / CHALLENGE / CREATE / REPAIR / SYNTHESISE
        ↓
REGISTER EVIDENCE AND DELTA
        ↓
SESSION CLOSURE
        ↓
SAN™ VALIDATION
        ↓
CONTRIBUTION VALUE
        ↓
TOKENISATION / RETURN / MEMORY
```

### Entry v0.2

The public Synthesis gateway should allow, with minimal cognitive cost:

1. **Enter without mining**: read, explore and learn without starting any trace.
2. **Enter to contribute**: voluntarily start a NeoCronos™ session.
3. Choose or indicate the **Synthesis object**: issue, manifesto, neoaxiom, problem, audit, code, translation, proposal or another node.
4. Declare a **contribution alias/identity** compatible with the future identity layer of the system.
5. Choose the **initial contribution type**: contradiction, evidence, source, idea, code, test, translation, maintenance, care, synthesis, repair or other.
6. Start an `NC-*` trace with start date/time and object.
7. Clearly display that **time ≠ automatic token** and that any reward depends on validated contribution and the rules in force.

### NeoCronos™ trace

The trace should be event-sourced: rather than storing only a final total, it records enough milestones to reconstruct the process without continuous surveillance.

Candidate events:

```text
NC_SESSION_OPENED
SOURCE_OPENED
OBJECT_SELECTED
SOURCE_ADDED
NOTE_ADDED
HYPOTHESIS_ADDED
CONTRADICTION_FOUND
DELTA_PROPOSED
EVIDENCE_ADDED
COMMIT_LINKED
ISSUE_LINKED
PAUSE
RESUME
SESSION_CLOSED
SAN_REVIEWED
VALUE_ASSIGNED
TOKEN_ELIGIBLE
TOKEN_ASSIGNED
REWARD_PAID
REOPENED
```

### NeoCronos™ panel

The participant should be able to see the contribution as a process, not as a simple score.

Minimum panel:

```text
┌────────────────────────────────────────────────────┐
│ NEOCRONOS™ · SYNTHESIS GAME                       │
├────────────────────────────────────────────────────┤
│ Active session       00:42:16                      │
│ Trace                NC-20260810-...               │
│ Object               Synthesis #...                │
│ Status               UNDER CHALLENGE               │
├────────────────────────────────────────────────────┤
│ Traced time          42 min                        │
│ Evidence             3                             │
│ Sources              2                             │
│ Deltas               1                             │
│ New relations        4                             │
├────────────────────────────────────────────────────┤
│ SAN value            PENDING                       │
│ Token eligible       PENDING                       │
│ Reward               NOT ASSIGNED                  │
└────────────────────────────────────────────────────┘
```

The interface should not manufacture false precision of value before validation. During the work it may display **descriptive metrics**, never a promised reward.

### Collective panel

A second view should show the aggregate state of the Game without turning it into an addictive ranking:

- open/closed sessions;
- aggregate validated useful time;
- contributions pending challenge;
- accepted, partial and rejected contributions;
- contribution types;
- nodes with the greatest need for scrutiny;
- deltas produced;
- repairs completed;
- eligible/assigned tokens when that layer exists;
- available return fund when legally and operationally appropriate.

**Do not use by default:** people leaderboards by hours, compulsive streaks, FOMO, random rewards, opaque multipliers or casino patterns.

### Unit of play

The basic unit is not the hour; it is the **traceable contribution session**.

```text
NEOCRONOS™ SESSION =
IDENTITY/ALIAS
+ OBJECT
+ TIME INTERVAL
+ EVENTS
+ EVIDENCE
+ RESULT
+ SAN STATUS
+ DELTA
+ RETURN IF APPLICABLE
```

A session may last five minutes and be extraordinarily valuable; another may last hours and generate no validated contribution.

### Fit with the Traceable Entry Register

NeoCronos™ does not replace the existing Traceable Entry and Derivation Register. It **instruments it temporally**.

```text
ENTRY REGISTER
= what arrived + where from + to which node it is derived

NEOCRONOS™
= who devotes time + to which object + what process they perform + what result they leave

SAN™
= what part of the result survives challenge

CONTRIBUTION ECONOMY™
= what recognition/return corresponds
```

### Privacy

- explicit and voluntary timing;
- real pause;
- declarative editing of time when necessary;
- traceability of corrections;
- no keylogging;
- no permanent screenshot capture;
- no biometric surveillance;
- possibility of working without a NeoCronos™ session;
- separation of public identity, alias and data necessary for any eventual payment.

### Implementation phases

**v0.2 · WEB4™ DEMO**  
Local browser panel. Starts/pauses/closes a session, stores traces locally and allows JSON export. It issues no tokens and makes no payments.

**v0.3 · GitHub bridge**  
Voluntary linkage of Issue/commit/PR/document and generation of contribution proof.

**v0.4 · SAN validator**  
States `pending / accepted / partial / rejected`, relational evaluation and traceability of reviews.

**v0.5 · Token eligibility**  
Transformation of validated contribution into eligibility according to tokenomics approved through Open Synthesis.

**v1.0 · Return Fund**  
Material reward only when validated legal, financial, accounting and technical infrastructure exists.

---

**Regla / Rule:** `TIEMPO TRAZADO ≠ VALOR VALIDADO ≠ TOKEN ≠ DINERO / TRACED TIME ≠ VALIDATED VALUE ≠ TOKEN ≠ MONEY`, pero sin tiempo y genealogía no existe una contabilidad completa del aporte humano / but without time and genealogy there is no complete accounting of human contribution.
