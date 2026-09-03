# KDP / Amazon — matriz de casos abiertos y reescalado temporal

**Fecha de corte:** 2026-09-03  
**Ámbito:** IDEA · ediciones multilingües · vinculación idioma/formato · rutas de escalado Amazon  
**Estado:** traza operativa pública; no sustituye el estado interno de los sistemas de Amazon/KDP.

## Regla de conservación del caso

Mientras una incidencia material siga sin resolución verificable, se mantendrá seguimiento temporal para evitar que el silencio o la falta de actividad aparente se confundan con resolución.

- Si la última comunicación de KDP/Amazon solicita una acción o información nuestra, se responde sin demora una vez reconciliada la evidencia.
- Si la última comunicación es nuestra y seguimos esperando respuesta, se realiza recordatorio/re-escalado tras 72 horas sin novedad, evitando duplicados y spam; no más de un reescalado por caso cada 72 horas salvo urgencia material nueva.
- Cada reescalado debe recordar expresamente que la cuestión permanece abierta y pedir que no se cierre por inactividad mientras siga pendiente la investigación, comprobación pública o identificación del equipo competente.
- Un caso cerrado o sustituido por otro no se reactiva artificialmente: permanece en genealogía y se enlaza con el caso sucesor.
- Una etiqueta de correo (`UNREAD`, `IMPORTANT`, etc.) no determina el estado real del expediente: **GMAIL_LABEL != CASE_STATE**.
- Silencio operativo no implica por sí solo intención deliberada de ignorar una solicitud.

## Matriz reconciliada

| Caso / ruta | Materia principal | Último estado verificable | Estado operativo 2026-09-03 | Acción anti-caducidad |
|---|---|---|---|---|
| **51071689** | Genealogía inicial: idiomas, formatos, Author Central, metadatos, propuestas de mejora | Fue cerrado expresamente y posteriormente usado como antecedente de nuevas incidencias | `HISTORICO_SUPERSEDIDO` | No reabrir por rutina; conservar como raíz genealógica y referenciar desde casos sucesores |
| **51425188** | Tapa blanda inglesa vinculada erróneamente a familia española | KDP informó el 2026-08-28 de desvinculación/corrección y plazo de hasta 7 días | `SUPERSEDIDO_POR_51425302_Y_51454627` | No duplicar reescalado; conservar evidencia de la corrección parcial y la recurrencia posterior |
| **51425302** | Formatos ES/EN y asociación multilingüe transversal | El 2026-08-29 se confirmó resuelta la tapa blanda inglesa, pero se pidió mantener abierto hasta resolver la asociación completa entre traducciones; sin respuesta posterior localizada | `OPEN_WAITING_KDP` | Reescalar si pasan 72 h sin respuesta; pedir mantenimiento explícito del caso y resolución/comprobación pública |
| **51454599** | Diagnóstico global de agrupación idioma/formato y auditoría de todas las familias de IDEA | KDP pidió el 2026-08-29 conformidad con las acciones propuestas y lista completa de ASIN/ISBN para auditoría exhaustiva; no consta respuesta posterior en ese hilo | `OPEN_ACTION_REQUIRED_US` | Prioridad alta: responder/reconciliar datos para impedir cierre por falta de respuesta y enlazar con la evolución posterior del caso 51454627 |
| **51454627** | Vinculación multilingüe global; regresión y contradicción sobre capacidad de intervención | 29-08: KDP afirmó haber revisado/enlazado globalmente. 01-09: tras la regresión comunicada, un supervisor indicó que la asociación entre idiomas es automática y no gestionable manualmente desde KDP | `OPEN_ESCALATION_REQUIRED` | Reescalar tras 72 h sin respuesta hacia el propietario técnico/catálogo competente; mantener la contradicción como cuestión abierta hasta identificar causa/propietario o criterio de cierre verificable |
| **51454666** | Propuesta de colaboración/auditoría aplicada | KDP indicó el 2026-08-29 que soporte no puede evaluar ni enrutar propuestas de consultoría y remitió a canales públicos | `ROUTING_SUPERSEDED` | No insistir rutinariamente en KDP; conservar genealogía y continuar por la ruta Amazon Research/partnership correspondiente |
| **AMAZON-RESEARCH-ROUTING-2026-08-29** | Ruta competente para evaluar colaboración y auditoría sistémica | Amazon Research Awards respondió el 31-08 que no era su ámbito; el 01-09 se pidieron rutas públicas concretas y se añadió la contradicción del caso 51454627; sin respuesta posterior localizada | `OPEN_WAITING_AMAZON` | Reescalar tras 72 h sin respuesta, solicitando exclusivamente identificación/ruta del equipo competente y evitando convertir Research Awards en soporte del caso KDP |

## Relación entre expedientes

La secuencia debe leerse como genealogía y no como tickets aislados:

`51071689 → 51425188 → 51425302 / 51454599 → 51454627 → escalado técnico Amazon`

La ruta de colaboración sigue en paralelo:

`51071689 (hallazgos y mejoras) → 51454666 (KDP sin competencia de routing) → AMAZON-RESEARCH-ROUTING-2026-08-29 → ruta competente pendiente`

## Criterio de cierre

Un caso técnico no debe marcarse como resuelto por una mera declaración interna cuando el problema relevante es público y reproducible. El cierre requiere, según el caso: corrección visible estable, comprobación de formatos dentro de cada idioma, aclaración de la relación entre traducciones, ausencia de regresión durante el periodo razonable de propagación, o identificación documentada del equipo competente cuando KDP carezca de control sobre esa capa.

---

# EN — KDP / Amazon open-case matrix and timed re-escalation

**Cut-off:** 2026-09-03. This is a public operational trace, not a representation of Amazon/KDP's internal ticket state.

## Anti-expiry rule

A materially unresolved issue remains under timed follow-up. If Amazon/KDP is waiting for information from us, the required response is prepared after evidence reconciliation. If we are waiting for Amazon/KDP, a concise reminder/re-escalation is due after 72 hours without a reply, with no more than one routine re-escalation per case every 72 hours unless new material evidence creates urgency. Each follow-up should state that the matter remains unresolved and ask that it not be closed for inactivity while investigation, public verification or competent-team routing remains pending.

Closed or superseded cases are not artificially revived; they remain in genealogy. Mailbox labels do not define the real case state: **GMAIL_LABEL != CASE_STATE**. Operational silence alone is not evidence of deliberate intent to ignore a request.

## Reconciled status

- **51071689** — historical root; explicitly closed and later reused as genealogy. `HISTORICAL_SUPERSEDED`.
- **51425188** — ES/EN paperback cross-link correction; later developments superseded it. `SUPERSEDED_BY_51425302_AND_51454627`.
- **51425302** — English paperback fixed, multilingual association explicitly left open on 2026-08-29; no later KDP reply located. `OPEN_WAITING_KDP`.
- **51454599** — KDP requested confirmation of the proposed corrective actions plus the complete ASIN/ISBN set for an exhaustive audit; no later reply from us is present in that thread. `OPEN_ACTION_REQUIRED_US` and high anti-expiry priority.
- **51454627** — global multilingual linking/regression. KDP stated on 2026-08-29 that it had reviewed and linked the editions globally; on 2026-09-01 a supervisor stated that cross-language association is automated and cannot be manually managed by KDP Support. `OPEN_ESCALATION_REQUIRED`.
- **51454666** — paid collaboration/routing request; KDP Support declined scope and pointed to public Amazon channels. `ROUTING_SUPERSEDED`; do not spam the KDP ticket.
- **AMAZON-RESEARCH-ROUTING-2026-08-29** — Research Awards declined scope on 2026-08-31; two follow-ups on 2026-09-01 requested a concrete competent route and documented the 51454627 contradiction. No later reply located. `OPEN_WAITING_AMAZON`.

## Closure principle

For public-facing catalogue defects, closure requires evidence appropriate to the claim: stable public correction, correct within-language format families, clarification of cross-language relationships, no observed regression after a reasonable propagation window, or documented identification of the competent owner when KDP Support does not control the affected catalogue layer.
