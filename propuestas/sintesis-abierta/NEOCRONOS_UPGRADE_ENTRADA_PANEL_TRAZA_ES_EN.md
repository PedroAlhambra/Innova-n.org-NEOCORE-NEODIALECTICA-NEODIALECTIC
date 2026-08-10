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

## EN · Functional correction

**NeoCronos™ is the measurement system of the Open Synthesis Game™.** It starts at the entry into the game, opens an `NC-*` contribution trace and follows the participant's path until the contribution is challenged, classified and, where appropriate, rewarded.

The basic unit is not an hour but a **traceable contribution session** combining identity/alias, object, temporal interval, events, evidence, result, SAN status, delta and possible return.

The public entry should offer **Explore without mining** and **Start contributing with NeoCronos™**. The first WEB4™ implementation should remain a DEMO: local browser trace, timer, event/evidence counters, session history and JSON export, with no token issuance or payment promises.

The dashboard should display descriptive process metrics while SAN validation remains pending, and must avoid addictive ranking, opaque multipliers, gambling mechanics or hour-based prestige.

---

**Regla / Rule:** `TIEMPO TRAZADO ≠ VALOR VALIDADO ≠ TOKEN ≠ DINERO`, pero sin tiempo y genealogía no existe una contabilidad completa del aporte humano.