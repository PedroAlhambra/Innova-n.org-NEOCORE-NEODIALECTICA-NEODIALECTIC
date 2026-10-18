# Addendum auditoría Amazon KDP · caso 51454599 · cierre sin resolución material y reapertura mediante nuevo caso
# Amazon KDP audit addendum · case 51454599 · closure without material resolution and reopening through a new case

**Fecha / Date:** 2026-10-15  
**Entidad / Entity:** Amazon Kindle Direct Publishing (KDP)  
**Obra / Work:** IDEA  
**Caso anterior / Previous case:** `51454599`  
**Nuevo caso KDP / New KDP case:** `PENDIENTE_DE_CREACIÓN / PENDING_CREATION`  
**Estado / Status:** `AUDIT_CLOSED_WITH_CATASTROPHIC_PROCESS_FAILURE / MATERIAL_INCIDENT_OPEN / NEW_CASE_REQUIRED_BY_KDP`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

### 1. Objeto de este addendum

Este documento cierra la fase de auditoría correspondiente al caso KDP `51454599` y abre una nueva traza de continuidad porque KDP cerró administrativamente el expediente mientras la incidencia material seguía sin resolución.

La clasificación **FALLO CATASTRÓFICO DE PROCESO** es una calificación de auditoría de Innova_N sobre la gobernanza del expediente y su trazabilidad. No implica atribución de mala fe, intención ni responsabilidad personal a ningún agente individual de KDP.

### 2. Hechos verificados

1. El caso `51454599` acumuló una investigación prolongada sobre la asociación multilingüe de `IDEA`, incluida la entrega de una matriz completa de **13 idiomas / 36 ediciones-formato** solicitada por KDP para continuar la investigación.
2. Distintos responsables y supervisores de KDP ofrecieron respuestas no plenamente compatibles sobre la capacidad de vinculación entre idiomas, la automatización del selector multilingüe, la posibilidad de intervención manual y el carácter experimental o limitado de la función.
3. El 29 de septiembre de 2026, un supervisor de KDP reconoció expresamente que las respuestas recibidas durante el expediente no habían sido consistentes y comunicó como posición final de soporte que la vinculación estable y permanente entre ediciones en diferentes idiomas no está actualmente soportada de forma garantizable.
4. El 15 de octubre de 2026 se respondió al mismo expediente dejando constancia de que la finalización de una investigación de soporte no equivale a resolución material, reiterando la disponibilidad de Innova_N para colaborar con catálogo, producto o ingeniería y solicitando trazabilidad concreta de lo investigado, de la limitación real y de cualquier escalado técnico o de producto.
5. KDP respondió inmediatamente mediante un mensaje automático indicando que el caso ya estaba cerrado y que, para recibir más ayuda, debía crearse **un nuevo caso** mediante el formulario de contacto.
6. En el momento de esta fijación pública, la incidencia material continúa sin una corrección completa y persistente ni una referencia técnica/producto que permita seguirla fuera del expediente de soporte cerrado.

### 3. Dictamen de auditoría

```text
PREVIOUS_CASE = 51454599
CASE_ADMIN_STATE = CLOSED_BY_KDP
MATERIAL_INCIDENT = OPEN
FULL_MATRIX = PROVIDED
SUPERVISOR_INCONSISTENCIES = ACKNOWLEDGED
MATERIAL_RESOLUTION = NOT_ACHIEVED
TECHNICAL_OR_PRODUCT_TRACE = NOT_CONFIRMED
REPLY_CONTINUITY = BLOCKED_BY_CASE_CLOSURE
KDP_INSTRUCTION = CREATE_NEW_CASE
AUDIT_CLASSIFICATION = CATASTROPHIC_PROCESS_FAILURE
```

Se considera **fallo catastrófico de proceso** porque la cadena de soporte terminó administrativamente antes de cerrar la cadena causal, técnica y de producto que el propio expediente había abierto. El problema no es sólo que una funcionalidad pueda tener una limitación: el fallo de proceso consiste en que el expediente deja de aceptar continuidad precisamente cuando siguen existiendo preguntas materiales no reconciliadas y cuando KDP obliga a comenzar un nuevo caso para continuar un problema ya extensamente documentado.

Esto rompe la continuidad natural de:

```text
EVIDENCIA
→ INVESTIGACIÓN
→ RESULTADO TÉCNICO
→ RESPONSABLE / EQUIPO COMPETENTE
→ CORRECCIÓN O LIMITACIÓN DOCUMENTADA
→ VERIFICACIÓN
→ CIERRE
```

La secuencia observada queda, en cambio:

```text
EVIDENCIA
→ INVESTIGACIÓN
→ MATRIZ COMPLETA
→ RESPUESTAS CONTRADICTORIAS
→ RECONOCIMIENTO DE INCONSISTENCIAS
→ LIMITACIÓN DECLARADA
→ PREGUNTAS TÉCNICAS ABIERTAS
→ CIERRE ADMINISTRATIVO
→ RESPUESTA BLOQUEADA
→ OBLIGACIÓN DE CREAR OTRO CASO
```

### 4. Reapertura genealógica

El caso `51454599` **no se borra ni se sustituye**. Queda conservado como nodo cerrado administrativamente y no resuelto materialmente.

La continuidad correcta es:

```text
51454599
[CLOSED_ADMIN / UNRESOLVED_MATERIAL]
→ NUEVO CASO KDP
[PENDING_CREATION]
→ referencia explícita a 51454599
→ reutilización de la matriz 13 idiomas / 36 ediciones-formato
→ no reiniciar diagnóstico desde cero
→ exigir continuidad técnica/producto
```

`NUEVA_TRAZA != BORRADO_DE_LA_ANTERIOR`  
`CIERRE_ADMINISTRATIVO != RESOLUCIÓN_MATERIAL`

### 5. Texto de apertura preparado para el nuevo caso KDP

**Asunto sugerido:**  
`Reapertura por cierre sin resolución material del caso 51454599 — IDEA · 13 idiomas / 36 ediciones-formato`

**Cuerpo sugerido:**

> Solicito la apertura de este nuevo caso como continuidad expresa del expediente KDP 51454599, que ha sido cerrado administrativamente aunque la incidencia material continúa sin resolución. No se trata de una consulta nueva ni de una petición de reiniciar el diagnóstico.
>
> El expediente anterior contiene una investigación prolongada sobre la asociación multilingüe de IDEA y una matriz completa de 13 idiomas / 36 ediciones-formato facilitada a petición de KDP. Distintos responsables ofrecieron respuestas contradictorias sobre la capacidad de vinculación, la automatización del selector de idiomas, la intervención manual y el carácter experimental o limitado de la función. El 29 de septiembre un supervisor reconoció expresamente esas inconsistencias y comunicó una limitación actual de plataforma.
>
> El 15 de octubre respondimos solicitando únicamente continuidad técnica: qué se investigó exactamente, si existe incidencia de producto o ingeniería, qué comportamiento está realmente soportado y qué prueba adicional podemos aportar. El sistema rechazó la continuidad porque el caso 51454599 ya estaba cerrado y nos indicó crear un caso nuevo.
>
> Pedimos que este nuevo expediente quede vinculado expresamente al 51454599 y que el equipo que lo gestione lea su historial completo antes de solicitar de nuevo datos ya entregados. La incidencia debe continuar desde el punto técnico/producto alcanzado, no desde una fase inicial de soporte.
>
> Innova_N mantiene su oferta de colaboración para reproducir el problema de forma controlada, aportar capturas o ASIN concretos, contrastar marketplaces y verificar cualquier corrección antes y después de aplicarla.
>
> Necesitamos como resultado verificable uno de estos dos cierres: (a) corrección completa y persistente de la asociación aplicable, o (b) documentación inequívoca de la limitación real de producto, con trazabilidad hacia el equipo competente y un mecanismo alternativo fiable si existe.

### 6. Estado de la reapertura

En el momento de este commit no se fija ningún número de caso nuevo porque KDP exige autenticación en su formulario `contact-us` para crearlo. El identificador del nuevo expediente se añadirá aquí cuando exista materialmente.

```text
NEW_KDP_CASE = PENDING_CREATION_AUTHENTICATION_REQUIRED
PUBLIC_AUDIT_TRACE = OPEN
PREVIOUS_CASE = PRESERVED
MATERIAL_INCIDENT = OPEN
NEXT = CREATE_NEW_KDP_CASE_AND_BACKLINK_TO_51454599
```

---

## EN · English

### 1. Purpose of this addendum

This document closes the audit phase associated with KDP case `51454599` and opens a new continuity trace because KDP administratively closed the case while the material incident remained unresolved.

The classification **CATASTROPHIC PROCESS FAILURE** is an Innova_N audit classification concerning case governance and traceability. It does not attribute bad faith, intent or personal responsibility to any individual KDP agent.

### 2. Verified facts

1. Case `51454599` accumulated a prolonged investigation into the multilingual association of `IDEA`, including a complete **13-language / 36-format-edition** matrix requested by KDP to continue the investigation.
2. Different KDP agents and supervisors provided responses that were not fully compatible regarding cross-language linking capability, multilingual-selector automation, manual intervention and whether the feature was experimental or structurally limited.
3. On 29 September 2026, a KDP supervisor expressly acknowledged that the responses received throughout the case had not been consistent and stated the support position that stable and permanent linking across different-language editions is not currently a guaranteed capability.
4. On 15 October 2026, a reply was sent to the same case stating that completion of a support investigation is not equivalent to material resolution, reiterating Innova_N's availability to collaborate with catalogue, product or engineering, and requesting concrete traceability of what had been investigated, the actual limitation and any technical/product escalation.
5. KDP immediately answered through an automated message stating that the case had already been closed and that further assistance required creating **a new case** through the contact form.
6. At the time of this public fixation, the material incident still lacks a complete and persistent correction or a technical/product tracking reference that can continue outside the closed support case.

### 3. Audit verdict

```text
PREVIOUS_CASE = 51454599
CASE_ADMIN_STATE = CLOSED_BY_KDP
MATERIAL_INCIDENT = OPEN
FULL_MATRIX = PROVIDED
SUPERVISOR_INCONSISTENCIES = ACKNOWLEDGED
MATERIAL_RESOLUTION = NOT_ACHIEVED
TECHNICAL_OR_PRODUCT_TRACE = NOT_CONFIRMED
REPLY_CONTINUITY = BLOCKED_BY_CASE_CLOSURE
KDP_INSTRUCTION = CREATE_NEW_CASE
AUDIT_CLASSIFICATION = CATASTROPHIC_PROCESS_FAILURE
```

This is classified as a **catastrophic process failure** because the support chain ended administratively before closing the causal, technical and product chains opened by the case itself. The problem is not simply that a platform feature may have a limitation. It is that the file stopped accepting further clarification while essential technical questions remained unresolved, compelling the author to initiate another case for an already extensively documented issue.

That breaks the expected continuity:

```text
EVIDENCE
→ INVESTIGATION
→ TECHNICAL RESULT
→ ACCOUNTABLE TEAM
→ FIX OR DOCUMENTED LIMITATION
→ VERIFICATION
→ CLOSURE
```

The actual observable sequence was instead:

```text
EVIDENCE
→ INVESTIGATION
→ COMPLETE ASIN MATRIX
→ CONTRADICTORY SUPPORT ANSWERS
→ ACKNOWLEDGEMENT OF INCONSISTENCIES
→ DECLARED PRODUCT LIMITATION
→ UNANSWERED TECHNICAL QUESTIONS
→ ADMINISTRATIVE CLOSURE
→ REPLY REJECTED
→ INSTRUCTION TO OPEN ANOTHER CASE
```

### 4. Genealogical reopening

Case `51454599` **is neither deleted nor replaced**. It remains the original node, closed administratively but materially unresolved.

The correct continuity is:

```text
51454599
[CLOSED_ADMIN / UNRESOLVED_MATERIAL]
→ NEW KDP CASE
[PENDING_CREATION]
→ explicit reference to 51454599
→ reuse the 13-language / 36-format-edition matrix
→ no repetition of the initial diagnosis
→ require product/technical continuity
```

`NEW_TRACE != ERASURE_OF_PREVIOUS_TRACE`  
`ADMINISTRATIVE_CLOSURE != MATERIAL_RESOLUTION`

### 5. New KDP case opening text prepared

**Suggested subject:**  
`Reopening after unresolved closure of case 51454599 — IDEA · 13 languages / 36 format-editions`

**Suggested body:**

> Please open this new case as an explicit continuation of KDP case 51454599, which was closed administratively although the underlying incident remains unresolved. This is not a new request and we are not asking for the diagnosis to restart.
>
> The previous case contains a lengthy investigation into the multilingual association of IDEA and the complete 13-language / 36-format-edition matrix supplied at KDP's request. Different agents provided inconsistent explanations concerning linking capability, automatic language selection, manual intervention and the experimental or limited nature of the functionality. On 29 September a supervisor expressly acknowledged the inconsistency and stated a current platform limitation.
>
> On 15 October we replied requesting only technical continuity: what exactly was investigated, whether a product or engineering issue exists, what behaviour is actually supported and what further evidence we can provide. The system rejected that continuation because case 51454599 was already closed and instructed us to open a new case.
>
> Please explicitly link this case to 51454599 and ensure the team reviews its complete history before requesting any information already supplied. The issue must resume at the technical/product stage reached, not begin again with first-line support.
>
> Innova_N remains available to help reproduce the problem in a controlled manner, provide screenshots or specific ASINs, compare marketplaces and verify changes before and after implementation.
>
> We require one of two verifiable outcomes: (a) a complete, persistent correction of the applicable associations, or (b) clear documentation of the actual product limitation, an accountable technical/product reference and a reliable alternative procedure if one exists.

### 6. Reopening status

No new KDP case number is recorded in this commit because KDP requires authentication in its `contact-us` form before a new case can be created. The new identifier will be appended when it materially exists.

```text
NEW_KDP_CASE = PENDING_CREATION_AUTHENTICATION_REQUIRED
PUBLIC_AUDIT_TRACE = OPEN
PREVIOUS_CASE = PRESERVED
MATERIAL_INCIDENT = OPEN
NEXT = CREATE_NEW_KDP_CASE_AND_BACKLINK_TO_51454599
```

---

## Trazabilidad / Traceability

- Auditoría pública principal / Main public audit: Issue `#70`.
- Mapa genealógico / Genealogy map: `auditorias/publicas/KDP_IDEA_GENEALOGIA_TRAZABLE_CASOS_ISSUES_DELTAS_ES_EN.md`.
- Nodo anterior / Previous node: `auditorias/publicas/2026-09-27_addendum_kdp_caso_51454599_supervision_contradiccion_producto_y_escalado_ES_EN.md`.
- Este addendum conserva el caso cerrado y abre una rama nueva sin inventar todavía un identificador KDP inexistente.
