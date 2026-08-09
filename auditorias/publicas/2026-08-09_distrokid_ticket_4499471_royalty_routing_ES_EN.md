# Auditoría pública · DistroKid · Ticket 4499471
## Missing / potentially misrouted Spotify royalties · royalty-routing review

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Estado:** abierto / open  
**Fecha de actualización:** 2026-08-09  
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

Se ha enviado un nuevo seguimiento solicitando:

1. confirmación de que el ticket 4499471 ha sido asignado a revisión humana de registros subyacentes;
2. mantenimiento del ticket abierto hasta contestación punto por punto;
3. resultado de auditoría o, en su defecto, estado de escalado y equipo responsable.

## 6. Criterio de cierre

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

1. confirmation that ticket 4499471 has been assigned for human review of the underlying records;
2. that the ticket remain open until the questions are answered point by point;
3. the audit result or, failing that, the escalation status and responsible team.

## 6. Closure criterion

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
