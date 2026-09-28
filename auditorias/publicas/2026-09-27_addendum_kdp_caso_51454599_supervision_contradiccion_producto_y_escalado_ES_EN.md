# Addendum · KDP / IDEA · caso 51454599 · supervisión, reconciliación funcional y escalado de producto
# Addendum · KDP / IDEA · case 51454599 · supervisor review, functional reconciliation and product escalation

**Fecha / Date:** 2026-09-27 · actualización / update 2026-09-28  
**Estado / Status:** AUDITORÍA DOCUMENTAL CERRADA · INCIDENCIA MATERIAL ABIERTA · RESPUESTA A SUPERVISIÓN ENVIADA / DOCUMENTARY AUDIT CLOSED · MATERIAL INCIDENT OPEN · REPLY TO SUPERVISOR SENT  
**Issue público / Public Issue:** [#70](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/70)  
**Antecedente inmediato / Immediate predecessor:** [24-09 · matriz ASIN completa y escalado de visibilidad interna](./2026-09-24_addendum_kdp_caso_51454599_matriz_asin_y_escalado_visibilidad_interna_ES_EN.md)  
**Mapa genealógico / Genealogy map:** [KDP · IDEA · casos, documentos, Issues y deltas](./KDP_IDEA_GENEALOGIA_TRAZABLE_CASOS_ISSUES_DELTAS_ES_EN.md)

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Respuesta de supervisión recibida el 26-09-2026

Dentro del caso `51454599`, Haniefa se identifica expresamente como **supervisora de KDP** y comunica dos elementos que requieren reconciliación con el historial del expediente:

1. KDP indica que no puede vincular los 13 idiomas diferentes de la misma obra en una única página de detalles.
2. En el mismo mensaje indica que, al coincidir exactamente autor y título, el sistema **mantiene las ediciones enlazadas** para ayudar a los clientes a descubrir y comparar versiones.

La auditoría no interpreta por sí sola cuál es la implementación interna de Amazon. Registra que la descripción funcional de esta respuesta no explica de forma verificable cómo se materializa ese “enlace” para el usuario ni cómo se reconcilia con el estado público observado.

### 2. Antecedentes que la nueva respuesta debe reconciliar

La nueva comunicación no se evalúa de forma aislada. El expediente ya contenía, entre otros, estos hitos:

- **13-09:** KDP comunica que el enlace entre formatos ha sido corregido y describe la asociación multilingüe como un proceso automático dependiente de metadatos coincidentes.
- **14-09:** verificación manual pública: la ficha principal continúa mostrando **«2 idiomas y 3 formatos»** y varias traducciones siguen apareciendo como resultados independientes.
- **15-09:** Sameer confirma expresamente que portugués, inglés, finés, alemán, polaco, sueco, danés y noruego (Bokmål) siguen apareciendo de forma independiente en Amazon.es y comunica que vuelve a consultar con su equipo específicamente sobre la vinculación entre idiomas.
- **18-09:** nueva verificación material conserva el estado **ES + FI** como asociación visible y mantiene abierta la incidencia.
- **21-09 y 23-09:** Syed solicita en dos comunicaciones sucesivas la misma matriz completa de idioma, formato, ASIN, ISBN y tienda para las 13 ediciones lingüísticas.
- **24-09:** para no bloquear la investigación, el autor reconstruye y entrega manualmente la matriz completa de **13 idiomas y 36 ediciones/formato con ASIN propio**, dejando constancia de que esos metadatos ya existen en KDP/Amazon y solicitando escalado a catálogo/producto/desarrollo si soporte no puede recuperarlos internamente.
- **26-09:** respuesta de supervisión de Haniefa descrita en el apartado anterior.
- **27-09:** el autor responde solicitando una reconciliación técnica explícita del historial completo.

### 3. Doble petición de metadatos y carga trasladada al usuario

La auditoría registra como hecho de proceso que la misma matriz fue solicitada por soporte en dos correos sucesivos antes de la respuesta del 24-09.

No se afirma desde fuera por qué las herramientas internas de KDP requieren esa recopilación ni qué arquitectura de datos utiliza Amazon. Sí se documenta que:

- la información de idioma, formato, ASIN, ISBN y cuenta editorial es información ya necesaria para publicar y gestionar las ediciones;
- el usuario tuvo que reconstruir manualmente una matriz extensa para que soporte continuara una investigación técnica;
- en la respuesta del 27-09 se solicita que no vuelva a pedirse información ya entregada o recuperable internamente salvo que se identifique un dato concreto que el equipo técnico no pueda obtener.

Este punto se mantiene separado de la incidencia multilingüe: es una cuestión adicional de **continuidad operativa y visibilidad interna del soporte**.

### 4. Funcionalidad existente frente a limitación de producto

La respuesta del 27-09 introduce una precisión importante: Innova_N no solicita una excepción manual permanente ni una función ajena a KDP.

El propio historial del caso documenta mecanismos existentes de:

- vinculación entre formatos;
- relación/selector de idiomas y ediciones;
- automatización basada en metadatos;
- actuaciones o escalados previos sobre catálogo/producto.

Por ello, si la plataforma no puede representar de forma completa y persistente una misma obra publicada en 13 traducciones, la cuestión se formula como una **limitación reproducible de una funcionalidad existente**.

La solicitud remitida a la supervisora es que, si esa limitación es estructural del producto actual, se registre y escale formalmente como mejora de producto/catálogo en lugar de cerrarse como una mera imposibilidad operativa o una preferencia del autor.

### 5. Preguntas técnicas remitidas el 27-09

La respuesta enviada solicita aclaración sobre:

1. si KDP/Amazon puede o no relacionar traducciones distintas de una misma obra mediante el selector o mecanismo público de idiomas;
2. qué significa exactamente que el sistema “los mantiene enlazados” y dónde puede verificarlo un cliente;
3. si el mecanismo existe, por qué las 13 ediciones no aparecen relacionadas de forma equivalente y qué actuación queda pendiente;
4. cómo se reconcilia la respuesta de supervisión con la comprobación de Sameer y los escalados previos;
5. qué resultado tuvo la investigación técnica para la que se solicitó dos veces la matriz completa;
6. si se escaló a catálogo/producto/desarrollo la falta de visibilidad interna de metadatos y la inconsistencia observada;
7. si una limitación estructural puede registrarse formalmente como mejora de producto.

### 6. Estado epistemológico y condición de cierre

- **HECHO DOCUMENTAL:** Haniefa se identifica como supervisora de KDP.
- **HECHO DOCUMENTAL:** KDP afirma simultáneamente que no puede vincular los 13 idiomas en una misma página y que el sistema los mantiene enlazados por coincidencia de título/autor.
- **HECHO DOCUMENTAL:** Sameer había verificado previamente múltiples traducciones como resultados independientes y reabierto consulta con su equipo.
- **HECHO DOCUMENTAL:** KDP solicitó la misma matriz completa el 21 y el 23 de septiembre.
- **HECHO DOCUMENTAL:** la matriz de 13 idiomas / 36 ediciones-formato fue entregada el 24 de septiembre.
- **HECHO DOCUMENTAL:** el 27 de septiembre se envió respuesta solicitando reconciliación técnica y escalado de producto si procede.
- **OBSERVACIÓN PREVIA:** la asociación pública completa y persistente no había sido verificada materialmente.
- **NO AFIRMAR:** mala fe, intención de bloquear, arquitectura interna concreta o causa técnica no demostrada.

Estado reconciliado:

`AUDIT_PHASE=CLOSED / INCIDENT=OPEN / SUPERVISOR_RESPONSE_RECEIVED / FUNCTIONAL_DESCRIPTION_UNRECONCILED / DUPLICATE_METADATA_REQUESTS_DOCUMENTED / FULL_ASIN_MATRIX_SENT / PRODUCT_LIMITATION_ESCALATION_REQUESTED / AUTHOR_REPLY_SENT_2026-09-27 / SUPERVISOR_REITERATION_RECEIVED_2026-09-27 / AUTHOR_FOLLOWUP_SENT_2026-09-28 / WAITING_FINAL_CLARIFICATION`

### 7. Actualización 28-09 · reiteración de supervisión y respuesta final de aclaración

El 27-09 se recibe una nueva comunicación de Haniefa, ya como continuación de la respuesta de supervisión. Su contenido sustantivo se limita a reiterar que **«No se pueden vincular libros en diferentes idiomas»**, sin responder individualmente a las preguntas técnicas remitidas anteriormente ni explicar el resultado de la investigación para la que se solicitó la matriz completa.

El 28-09 el autor responde dejando constancia de que toma nota de esa posición, pero solicita dos aclaraciones finales y acotadas:

1. si la imposibilidad indicada constituye la posición definitiva de KDP, que se confirme de forma inequívoca y se indique si la limitación ha sido registrada y trasladada a catálogo/producto/desarrollo;
2. que se comunique el resultado de la investigación técnica para la que KDP solicitó la matriz completa de las 13 ediciones lingüísticas.

La respuesta incluye un enlace directo a esta auditoría pública para que KDP pueda consultar la traza documental y su genealogía sin reproducir de nuevo todo el expediente en el correo.

**Trazabilidad Gmail:** respuesta enviada el 28-09-2026; `message_id=1a0e66e5e2dd6c39`; `thread_id=1a0e50344a451f32`; estado verificado `SENT`.

La nueva comunicación no se interpreta como resolución material del problema. El estado queda en espera de esas dos aclaraciones o, en su defecto, de una confirmación final inequívoca de la limitación del producto.

La incidencia podrá cerrarse cuando exista una asociación multilingüe material, correcta y persistente; un mecanismo alternativo fiable; o una explicación técnica verificable que identifique con claridad la limitación de producto y su tratamiento.

---

## EN · English

### 1. Supervisor response received on 26 Sep 2026

Within case `51454599`, Haniefa explicitly identifies herself as a **KDP supervisor** and communicates two elements that require reconciliation with the existing case history:

1. KDP states that it cannot link the 13 different language editions of the same work on a single detail page.
2. In the same message, it states that because author and title match exactly, the system **keeps the editions linked** to help customers discover and compare versions.

The audit does not infer Amazon's internal implementation. It records that this functional description does not provide a verifiable explanation of how that “link” is exposed to customers or how it reconciles with the observed public state.

### 2. Prior evidence that must be reconciled

The supervisor response is not evaluated in isolation. The case already contained these milestones:

- **13 Sep:** KDP states that the format-linking issue has been corrected and describes multilingual association as an automated metadata-based process.
- **14 Sep:** public manual verification still shows **“2 languages and 3 formats”**, with multiple translations appearing independently.
- **15 Sep:** Sameer explicitly confirms that Portuguese, English, Finnish, German, Polish, Swedish, Danish and Norwegian (Bokmål) remain independent results on Amazon.es and says he is consulting his team again specifically about cross-language linking.
- **18 Sep:** a further material verification preserves **ES + FI** as the visible association and keeps the incident open.
- **21 Sep and 23 Sep:** Syed asks in two successive communications for the same complete matrix of language, format, ASIN, ISBN and store across all 13 language editions.
- **24 Sep:** to avoid blocking the investigation, the author manually reconstructs and provides the complete matrix of **13 languages and 36 format editions with their own ASINs**, while asking for catalogue/product/development escalation if support cannot retrieve metadata already held inside KDP/Amazon.
- **26 Sep:** Haniefa's supervisor response described above.
- **27 Sep:** the author replies requesting explicit technical reconciliation of the complete case history.

### 3. Repeated metadata request and user-side workload

The audit records as a process fact that support requested the same matrix in two successive messages before the 24 Sep reply.

No claim is made about why KDP's internal tools required the collection or what Amazon's data architecture is. The trace records that:

- language, format, ASIN, ISBN and publishing-account relations are data already required to publish and manage the editions;
- the user had to manually reconstruct a substantial matrix so that technical investigation could continue;
- the 27 Sep reply asks that already-provided or internally retrievable information not be requested again unless a specific unavailable data item is identified.

This remains a separate issue from multilingual linking: it concerns **operational continuity and support-side internal visibility**.

### 4. Existing functionality versus product limitation

The 27 Sep reply adds an important distinction: Innova_N is not asking for a permanent manual exception or for functionality foreign to KDP.

The documented history already includes mechanisms for:

- format linking;
- language/edition relationships and selectors;
- metadata-driven automation;
- prior catalogue/product action or escalation.

Accordingly, if the platform cannot completely and persistently represent one work published in 13 translations, the matter is framed as a **reproducible limitation of existing functionality**.

The supervisor was asked that, if this is a structural limitation of the current product, it be formally recorded and escalated as a product/catalogue improvement rather than closed as a mere operational impossibility or author preference.

### 5. Technical questions sent on 27 Sep

The reply asks KDP to clarify:

1. whether KDP/Amazon can relate translations of the same work through a public language selector or equivalent mechanism;
2. what exactly “the system keeps them linked” means and where a customer can verify it;
3. if the mechanism exists, why all 13 editions are not equivalently related and what action remains pending;
4. how the supervisor response reconciles with Sameer's prior verification and earlier escalations;
5. what result came from the technical investigation for which the complete matrix was requested twice;
6. whether the internal metadata-visibility gap and observed inconsistency were escalated to catalogue/product/development;
7. whether a structural limitation can be formally registered as a product improvement.

### 6. Epistemic status and closure condition

- **DOCUMENTARY FACT:** Haniefa identifies herself as a KDP supervisor.
- **DOCUMENTARY FACT:** KDP states both that it cannot link all 13 languages on one detail page and that the system keeps them linked through matching title/author metadata.
- **DOCUMENTARY FACT:** Sameer had previously verified multiple translations as independent results and reopened consultation with his team.
- **DOCUMENTARY FACT:** KDP requested the same complete matrix on 21 and 23 September.
- **DOCUMENTARY FACT:** the 13-language / 36-format-edition matrix was supplied on 24 September.
- **DOCUMENTARY FACT:** a reply requesting technical reconciliation and product escalation where applicable was sent on 27 September.
- **PRIOR OBSERVATION:** complete and persistent public multilingual association had not been materially verified.
- **DO NOT CLAIM:** bad faith, intent to block, any specific internal architecture or any unproven technical cause.

Reconciled state:

`AUDIT_PHASE=CLOSED / INCIDENT=OPEN / SUPERVISOR_RESPONSE_RECEIVED / FUNCTIONAL_DESCRIPTION_UNRECONCILED / DUPLICATE_METADATA_REQUESTS_DOCUMENTED / FULL_ASIN_MATRIX_SENT / PRODUCT_LIMITATION_ESCALATION_REQUESTED / AUTHOR_REPLY_SENT_2026-09-27 / SUPERVISOR_REITERATION_RECEIVED_2026-09-27 / AUTHOR_FOLLOWUP_SENT_2026-09-28 / WAITING_FINAL_CLARIFICATION`

### 7. 28 Sep update · supervisor reiteration and final clarification request

On 27 Sep a further message is received from Haniefa as a continuation of the supervisor response. Its substantive content reiterates that **“books in different languages cannot be linked”**, without individually answering the technical questions previously submitted or explaining the result of the investigation for which the complete matrix had been requested.

On 28 Sep the author replies, recording that this stated position has been noted while requesting two final, narrowly scoped clarifications:

1. if this impossibility is KDP's definitive position, that it be confirmed unequivocally and that KDP state whether the limitation has been registered and escalated to catalogue/product/development;
2. that KDP communicate the result of the technical investigation for which it requested the complete matrix of the 13 language editions.

The reply includes a direct link to this public audit so KDP can inspect the documentary trace and genealogy without reproducing the entire case history again in the email.

**Gmail traceability:** reply sent on 28 Sep 2026; `message_id=1a0e66e5e2dd6c39`; `thread_id=1a0e50344a451f32`; verified state `SENT`.

The new communication is not treated as material resolution of the issue. The state remains pending those two clarifications or, failing that, an unequivocal final confirmation of the product limitation.

The incident may close when there is materially correct and persistent multilingual association, a reliable alternative mechanism, or a technically verifiable explanation that clearly identifies the product limitation and how it will be handled.
