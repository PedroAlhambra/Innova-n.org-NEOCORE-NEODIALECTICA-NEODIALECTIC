# Auditoría pública · DistroKid · Ticket 4499471
## Missing / potentially misrouted Spotify royalties · royalty-routing review

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Estado:** abierto / open  
**Fecha de actualización:** 2026-08-16  
**Casos relacionados:** 2901165 · 2941949 · 4499471  
**Ámbito:** Spotify · DistroKid · regalías · catálogo · perfiles · ISRC · routing

> Esta auditoría distingue hechos documentados de hipótesis. La existencia de incidencias de catálogo o de ausencia aparente de pagos no demuestra por sí sola fraude ni desvío de regalías. La finalidad es obtener y reconciliar los registros técnicos necesarios.

---

# ES · Castellano

## 1. Hecho reclamado

Pedro Martínez Alhambra ha comunicado a DistroKid que su cuenta muestra **cero pagos de regalías Spotify desde finales de 2024**, pese a registrar **más de 9.000 reproducciones Spotify** según los datos disponibles para el titular.

La reclamación había sido planteada previamente en los tickets **2901165** y **2941949** sin resolución satisfactoria. El 7 de agosto de 2026 se abrió/escaló el ticket **4499471** solicitando una **auditoría completa de royalty routing**.

## 2. Respuesta de DistroKid del 8 de agosto de 2026

Un agente de soporte respondió explicando las diferencias entre **Estimated Daily Stats** y los informes mensuales de regalías, incluyendo la posibilidad de fluctuaciones temporales de estadísticas.

Esa respuesta no contestaba al objeto concreto del ticket: la ausencia prolongada de pagos Spotify y la petición de revisar los registros de regalías y su enrutamiento.

## 3. Preguntas técnicas remitidas

Se pidió a DistroKid que respondiera específicamente:

- qué informes de regalías Spotify ha recibido para los lanzamientos afectados desde finales de 2024;
- qué importes fueron atribuidos a la cuenta;
- si el importe es cero, en qué datos concretos de reporting Spotify se basa ese cero;
- si los identificadores de artista, releases, UPC e ISRC están correctamente asociados;
- si existen objetos de reporting sin casar, reasignados o dirigidos a otra cuenta/artista;
- si hubo cambios de mapping después de incidencias de catálogo;
- el resultado de una auditoría completa del routing desde finales de 2024 hasta la actualidad.

## 4. Evidencia adicional de integridad de catálogo

Se incorporaron al ticket alertas históricas de **Artist Profile Alerts** de DistroKid con eventos de retirada y reaparición de lanzamientos en 2025 para proyectos como **Techno Bach** y **Yellow Quasar**.

Las listas de títulos retirados y añadidos en días consecutivos no coinciden completamente en varios casos. Se ha pedido a DistroKid que determine, para cada evento:

- DSP o tienda que originó la alerta;
- release, UPC e ISRC afectados;
- si hubo retirada, redelivery, relink o sustitución;
- si cambió algún identificador;
- si cambió algún mapping de cuenta o de objeto de regalías;
- si la incidencia pudo afectar a reconciliación o reporting.

**Importante:** estas alertas se conservan como anomalías documentales que deben reconciliarse; no se presentan como prueba automática de desvío de regalías.

## 5. Seguimiento del 9 de agosto de 2026

Se envió un seguimiento solicitando:

1. confirmación de que el ticket 4499471 había sido asignado a revisión humana de registros subyacentes;
2. mantenimiento del ticket abierto hasta contestación punto por punto;
3. resultado de auditoría o, en su defecto, estado de escalado y equipo responsable.

## 6. Nuevo escalado del 16 de agosto de 2026

Tras revisar de nuevo la respuesta del 8 de agosto, se ha contestado en el propio ticket **4499471** dejando explícito que la incidencia **no es una fluctuación temporal de Estimated Daily Stats ni una caída de estadísticas de 24 horas**.

El objeto pendiente continúa siendo la ausencia histórica de pagos de regalías Spotify desde finales de 2024 pese a las más de 9.000 reproducciones observadas en los datos disponibles para el titular.

Se ha solicitado mantener abierto el ticket y escalarlo al equipo capaz de inspeccionar los registros subyacentes de **royalties/accounting y routing**, pidiendo una reconciliación por lanzamiento/pista y, cuando sea posible, por ISRC que cubra:

1. informes de regalías Spotify recibidos por DistroKid desde finales de 2024 para el catálogo afectado;
2. importes atribuidos a la cuenta desde dichos informes;
3. datos concretos de reporting Spotify que sustentarían un importe cero, si ese fuese el resultado;
4. asociación correcta de artist IDs, releases, UPC, ISRC, cuenta y objetos de regalías;
5. existencia de objetos sin casar, reasignados, duplicados o enrutados de forma distinta;
6. posible efecto de retiradas/reapariciones, redelivery, relinking o cambios de identificadores/mapping sobre la reconciliación;
7. reconstrucción verificable de la cadena:

```text
SPOTIFY STREAMS
→ SPOTIFY REPORTING
→ DISTROKID ROYALTY OBJECT
→ RELEASE / ISRC
→ ARTIST / ACCOUNT
→ AMOUNT
→ PAYMENT / NON-PAYMENT
```

También se ha reiterado que las alertas históricas relativas a proyectos como **Yellow Quasar** y **Techno Bach** no se presentan como prueba de desvío, sino como incidencias documentales que deben contrastarse con los registros de regalías.

Se ha pedido confirmación expresa de asignación a revisión humana de royalties/accounting o technical routing, junto con el resultado de auditoría o el estado del escalado y equipo responsable.

**Estado a 2026-08-16:** pendiente de respuesta de DistroKid al escalado técnico específico. No se considera resuelto por la explicación general sobre Estimated Daily Stats.

## 7. Criterio de cierre

La auditoría podrá cerrarse o reclasificarse cuando exista documentación suficiente para reconciliar:

```text
REPRODUCCIONES
→ REPORTING DEL DSP
→ OBJETO DE REGALÍAS
→ IDENTIFICADORES DEL RELEASE
→ ARTISTA / CUENTA
→ IMPORTE
→ PAGO / NO PAGO
```

Cualquier respuesta técnica verificable de DistroKid que descarte una hipótesis deberá incorporarse al registro con el mismo peso que la evidencia que la originó.

---

# EN · English

## 1. Reported issue

Pedro Martínez Alhambra has reported to DistroKid that his account shows **zero Spotify royalty payments since late 2024**, despite **more than 9,000 Spotify streams** in the available account-side data.

The matter had previously been raised through tickets **2901165** and **2941949** without satisfactory resolution. On 7 August 2026, ticket **4499471** was opened/escalated requesting a **full royalty-routing audit**.

## 2. DistroKid response on 8 August 2026

A support agent replied with a general explanation of the difference between **Estimated Daily Stats** and monthly royalty reports, including possible temporary fluctuations in estimated statistics.

That answer did not address the specific subject of the ticket: the prolonged absence of Spotify royalty payments and the request to inspect royalty records and routing.

## 3. Technical questions submitted

DistroKid was asked to state specifically:

- which Spotify royalty reports it received for the affected releases since late 2024;
- which amounts were attributed to the account;
- if the amount is zero, which exact Spotify reporting data supports that zero;
- whether artist, release, UPC and ISRC identifiers are correctly associated;
- whether any reporting object is unmatched, reassigned or routed to another artist/account;
- whether mapping changed after catalogue incidents;
- the result of a complete routing audit from late 2024 to the present.

## 4. Additional catalogue-integrity evidence

Historical DistroKid **Artist Profile Alerts** documenting removal and re-addition events during 2025 for projects including **Techno Bach** and **Yellow Quasar** were added to the case.

In several instances, the titles listed as removed and added on consecutive days do not fully match. DistroKid has been asked to determine for every event:

- which DSP/store generated the alert;
- affected release, UPC and ISRC values;
- whether the asset was removed, re-delivered, re-linked or replaced;
- whether an identifier changed;
- whether account or royalty-object mapping changed;
- whether the incident could have affected reporting or reconciliation.

**Important:** these alerts are preserved as documentary anomalies requiring reconciliation; they are not presented as automatic proof of royalty misrouting.

## 5. Follow-up on 9 August 2026

A further message requested:

1. confirmation that ticket 4499471 had been assigned for human review of the underlying records;
2. that the ticket remain open until the questions were answered point by point;
3. the audit result or, failing that, the escalation status and responsible team.

## 6. Further escalation on 16 August 2026

After reviewing the 8 August response again, a reply was sent within ticket **4499471** explicitly clarifying that the issue is **not a temporary Estimated Daily Stats fluctuation or a 24-hour statistics drop**.

The unresolved subject remains the historical absence of Spotify royalty payments since late 2024 despite more than 9,000 streams in the account-side data available to the rightsholder.

DistroKid has been asked to keep the ticket open and escalate it to a team able to inspect the underlying **royalty/accounting and routing records**, with reconciliation by release/track and, where possible, by ISRC covering:

1. Spotify royalty reports received by DistroKid since late 2024 for the affected catalogue;
2. amounts attributed to the account from those reports;
3. the specific Spotify reporting data supporting a zero amount, if that is the result;
4. correct association of artist IDs, releases, UPCs, ISRCs, account and royalty objects;
5. any unmatched, reassigned, duplicated or differently routed objects;
6. whether removals/re-additions, redelivery, relinking or identifier/mapping changes affected reconciliation;
7. a verifiable reconstruction of:

```text
SPOTIFY STREAMS
→ SPOTIFY REPORTING
→ DISTROKID ROYALTY OBJECT
→ RELEASE / ISRC
→ ARTIST / ACCOUNT
→ AMOUNT
→ PAYMENT / NON-PAYMENT
```

The message reiterates that historical alerts involving projects such as **Yellow Quasar** and **Techno Bach** are not presented as proof of misrouting, but as documentary anomalies to be reconciled against royalty records.

Explicit confirmation has been requested that the matter is assigned to a human royalties/accounting or technical-routing review, together with the audit result or the escalation status and responsible team.

**Status as of 2026-08-16:** awaiting DistroKid's response to the specific technical escalation. The general Estimated Daily Stats explanation is not considered resolution of the reported issue.

## 7. Closure criterion

The audit can be closed or reclassified when sufficient documentation reconciles:

```text
STREAMS
→ DSP REPORTING
→ ROYALTY OBJECT
→ RELEASE IDENTIFIERS
→ ARTIST / ACCOUNT
→ AMOUNT
→ PAYMENT / NON-PAYMENT
```

Any verifiable technical answer from DistroKid that disproves a hypothesis must be incorporated into the record with the same weight as the evidence that generated it.

---

## Nodos relacionados / Related nodes

- [Auditorías públicas / Public audits](./README.md)
- [MAXPROC 001 · Leónidas-Cancerbero™](../../analisis/publicos/2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md)
- [Análisis histórico DistroKid](../../analisis/2025-12_Evento-Reflejo_Auditoria-Distrokid.md)
