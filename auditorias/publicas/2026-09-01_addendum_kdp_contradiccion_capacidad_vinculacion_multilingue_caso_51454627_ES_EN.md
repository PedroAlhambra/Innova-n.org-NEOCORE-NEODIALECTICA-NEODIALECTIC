# Addendum · Amazon KDP · contradicción sobre capacidad de vinculación multilingüe
# Addendum · Amazon KDP · contradiction about multilingual-linking capability

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

**Fecha:** 1 de septiembre de 2026  
**Obra:** IDEA  
**Caso principal:** `51454627`  
**Estado:** incidencia reabierta · actuación multilingüe declarada ejecutada el 29/08 · ventana de propagación de hasta 7 días aún abierta · contradicción documental interna de KDP · asociación pública degradada/incompleta · causa raíz no resuelta

## 1. Precisión esencial: no era una capacidad hipotética

La secuencia documental obliga a distinguir entre una mera afirmación abstracta de capacidad y una **actuación concreta que KDP declaró haber ejecutado**.

El 29 de agosto de 2026, Shrehitha, desde KDP Support y dentro del caso `51454627`, afirmó expresamente que había revisado los enlaces de todas las ediciones lingüísticas y formatos disponibles de IDEA y que **los había enlazado en cada tienda de Amazon donde se publicaban**. La respuesta especificó que la actuación cubría:

- Kindle ↔ tapa blanda ↔ tapa dura dentro de cada idioma;
- **los enlaces multilingües entre las ediciones**;
- y una propagación pública que podía tardar **hasta siete días**.

Por tanto, la auditoría no registra simplemente «KDP dijo que podía vincular idiomas». Registra algo más fuerte y verificable: **KDP declaró que la intervención multilingüe ya había sido ejecutada y pidió esperar hasta siete días para que el resultado se reflejara plenamente**.

Además, tras esa actuación se observó una mejora parcial de las asociaciones públicas. Esa observación no permite determinar por sí sola qué mecanismo interno produjo la mejora, pero sí forma parte de la cronología material que debe reconciliarse con la respuesta posterior.

## 2. Hecho nuevo y regresión durante la ventana declarada

El 1 de septiembre, todavía dentro de la ventana máxima de siete días comunicada por KDP, se reportó una regresión observable: en la ficha pública de Amazon.es de IDEA, dentro de «Idioma», volvían a aparecer únicamente «Español» y «Finlandés», mientras otras traducciones publicadas habían dejado de mostrarse asociadas.

Christian, supervisor de KDP, respondió entonces que la herramienta de KDP permite verificar/corregir la vinculación de formatos dentro del mismo idioma, pero que la asociación entre ediciones de distintos idiomas depende de un proceso automatizado del catálogo de Amazon y que KDP Support no puede gestionarla ni corregirla manualmente.

La regresión observada **antes de finalizar los siete días no demuestra por sí sola cuál será el estado final una vez agotada la propagación**. La auditoría mantiene abierta esa comprobación. Pero la ventana de propagación tampoco resuelve la contradicción organizativa: debe explicarse cómo pudo KDP declarar el 29/08 una actuación multilingüe ya ejecutada si el 01/09 un supervisor afirma que KDP Support no puede realizar ni corregir esa capa.

## 3. Contradicción documental verificable

```text
29-08-2026 · KDP:
REVISIÓN GLOBAL DECLARADA EJECUTADA
+ EDICIONES DECLARADAS ENLAZADAS EN LAS TIENDAS AMAZON
+ ENLACES MULTILINGÜES INCLUIDOS
+ HASTA 7 DÍAS DE PROPAGACIÓN

29/08 → 01/09:
MEJORA PARCIAL OBSERVADA
→ POSTERIOR REGRESIÓN PÚBLICA DURANTE LA VENTANA DE PROPAGACIÓN

01-09-2026 · KDP supervisor:
VINCULACIÓN ENTRE IDIOMAS = AUTOMÁTICA
+ NO GESTIONABLE/CORREGIBLE MANUALMENTE DESDE KDP SUPPORT

=> CAPACIDAD / ESCALADO / PROCESO INTERNO NO RECONCILIADOS
```

No es metodológicamente correcto sustituir la primera traza por la segunda. Ambas existen y deben conservarse. `NUEVA_TRAZA != ESTADO_RECONCILIADO`.

La cuestión auditable pasa a ser: **¿qué actuación se realizó realmente el 29/08, mediante qué herramienta/equipo/capa, qué parte produjo la mejora observada y por qué el estado público vuelve a degradarse mientras otro supervisor niega capacidad operativa sobre esa misma relación?**

## 4. Consecuencia observable

Mientras no se estabilice la propagación y no se reconcilie la contradicción, el catálogo público puede conservar asociaciones incompletas o desactualizadas respecto del conjunto real de ediciones publicadas.

Esto afecta a:

- descubribilidad de traducciones;
- navegación entre idiomas;
- coherencia del índice público de ediciones;
- posibilidad de compra de versiones existentes pero no expuestas desde la ficha relacionada;
- trazabilidad entre intervención, propagación, mejora y regresión;
- identificación de la capa responsable cuando el estado automatizado se degrada.

La incidencia permanece **ABIERTA** y debe volver a verificarse al agotarse la ventana máxima comunicada por KDP.

## 5. HECHO / INFERENCIA / HIPÓTESIS

### HECHO

1. KDP declaró el 29/08 haber revisado las ediciones lingüísticas y formatos de IDEA y haberlos enlazado en las tiendas correspondientes.
2. KDP incluyó expresamente los enlaces multilingües dentro de la actuación declarada.
3. KDP indicó un plazo de hasta siete días para la propagación pública completa.
4. Se observó posteriormente una mejora parcial de asociaciones.
5. El 01/09, todavía dentro de esa ventana, se reportó una regresión pública a una asociación visible reducida a Español ↔ Finlandés.
6. Christian declaró el 01/09 que KDP Support no puede gestionar ni corregir manualmente la asociación cruzada entre idiomas.
7. Christian ofreció revisar formatos dentro de cada idioma, pero no identificó en su respuesta qué mecanismo/equipo produjo la actuación declarada del 29/08 ni confirmó un nuevo escalado técnico de la regresión multilingüe.

### INFERENCIA

Existe una capa operativa, de escalado, metadatos o catálogo que las respuestas de KDP no describen de forma reconciliada. La actuación del 29/08 pudo implicar una herramienta indirecta, un escalado interno, una intervención sobre metadatos que disparó automatismos, otro equipo de Amazon o una descripción incorrecta de lo realizado.

### HIPÓTESIS DEL FUNDADOR · H1

La negativa actual a corregir o reescalar la vinculación multilingüe puede responder a **comodidad operativa / evitación del trabajo o del escalado**, dado que pocos días antes KDP declaró ejecutada una intervención que incluía expresamente esa capa. Esta es la interpretación del fundador y **no se presenta como intención demostrada de Christian ni de Amazon**.

### HIPÓTESIS RIVALES

- **H2 · información del 29/08 incorrecta:** la respuesta pudo describir como realizada una capacidad que KDP Support realmente no posee.
- **H3 · capacidad indirecta/escalada:** KDP Support puede carecer de herramienta directa pero disponer de una ruta interna capaz de provocar la corrección.
- **H4 · automatismo + intervención auxiliar:** KDP pudo modificar metadatos/relaciones que activaron el sistema automático y describir el resultado como vinculación realizada.
- **H5 · propagación no consolidada:** parte de la regresión del 01/09 puede pertenecer al comportamiento transitorio de la ventana de hasta siete días; esta hipótesis afecta al estado visible final, pero no elimina la necesidad de reconciliar las dos descripciones incompatibles de capacidad/proceso.

## 6. Condiciones de comprobación y cierre

La auditoría separa dos preguntas que no deben mezclarse:

**A. Estado técnico visible:** al agotarse los siete días, ¿la matriz multilingüe completa queda estable, recíproca y navegable?

**B. Trazabilidad organizativa:** independientemente del resultado final de propagación, ¿qué hizo exactamente KDP el 29/08 y cómo se concilia con la afirmación del 01/09 de que KDP Support no puede gestionar esa capa?

Para cerrar completamente el caso se requiere:

1. verificar el estado público al agotarse la ventana declarada;
2. restauración estable de la matriz multilingüe completa si sigue degradada;
3. identificación del equipo/canal responsable si KDP Support no puede intervenir;
4. explicación reconciliada de la actuación declarada el 29/08; o, si aquella comunicación fue incorrecta, reconocimiento explícito de esa incorrección y ruta real de escalado para fallos del índice multilingüe automatizado.

```text
ACTUACIÓN MULTILINGÜE DECLARADA EJECUTADA
→ HASTA 7 DÍAS DE PROPAGACIÓN
→ MEJORA PARCIAL OBSERVADA
→ REGRESIÓN DURANTE LA VENTANA
→ NEGACIÓN POSTERIOR DE CAPACIDAD DIRECTA
→ VERIFICACIÓN AL DÍA 7 + RECONCILIACIÓN DEL PROCESO
```

## 7. Relaciones

- [Addendum 29-08-2026 · revisión global declarada aplicada](./2026-08-29_addendum_kdp_revision_global_aplicada_casos_51454627_51454666_ES_EN.md)
- [Addendum 29-08-2026 · asociación multilingüe](./2026-08-29_addendum_kdp_asociacion_multilingue_caso_51425302_ES_EN.md)
- [Addendum 28-08-2026 · idioma/formato](./2026-08-28_addendum_kdp_vinculacion_idiomas_formatos_caso_51425302_ES_EN.md)
- [Issue #70 · auditoría y contraste](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/70)
- [Índice de Auditorías Públicas](./README.md)
- [IDEA](../../obras/idea/README.md)

---

# EN · English

**Date:** 1 September 2026  
**Work:** IDEA  
**Main case:** `51454627`  
**Status:** incident reopened · multilingual action declared executed on 29 Aug · up-to-seven-day propagation window still open · internal KDP documentary contradiction · public association degraded/incomplete · root cause unresolved

## 1. Essential clarification: this was not a hypothetical capability

The documentary sequence requires a distinction between an abstract claim of capability and a **specific action that KDP stated it had already performed**.

On 29 August 2026, Shrehitha, from KDP Support in case `51454627`, explicitly stated that she had reviewed the links across all available IDEA language editions and formats and **linked them across the Amazon stores where they were published**. The reply specified that the action covered Kindle ↔ paperback ↔ hardcover relationships within each language, **multilingual links among editions**, and that public propagation could take **up to seven days**.

The audit therefore does not merely record “KDP said it could link languages.” It records a stronger verifiable statement: **KDP said the multilingual intervention had already been executed and instructed the customer to allow up to seven days for full public propagation**.

A partial improvement in public associations was subsequently observed. That observation alone does not identify the internal mechanism that caused it, but it is part of the material chronology that must be reconciled with the later response.

## 2. New fact and regression during the declared window

On 1 September, still within KDP's maximum seven-day window, an observable regression was reported: IDEA's Amazon.es public language association again showed only Spanish and Finnish while other published translations were absent.

Christian, a KDP supervisor, then stated that KDP's linking tool can verify/correct formats inside the same language, but cross-language associations depend on an automated Amazon catalogue process and cannot be manually managed or corrected by KDP Support.

A regression **before the seven-day window expires does not by itself establish what the final state will be after propagation completes**. The audit therefore keeps that verification open. But the propagation window does not resolve the organisational contradiction: Amazon still needs to explain how KDP could report a multilingual action as already performed on 29 August if a supervisor states on 1 September that KDP Support cannot perform or correct that layer.

## 3. Verifiable documentary contradiction

```text
29 AUG 2026 · KDP:
GLOBAL REVIEW DECLARED EXECUTED
+ EDITIONS DECLARED LINKED ACROSS AMAZON STORES
+ MULTILINGUAL LINKS EXPRESSLY INCLUDED
+ UP TO 7 DAYS FOR PROPAGATION

29 AUG → 1 SEP:
PARTIAL IMPROVEMENT OBSERVED
→ LATER PUBLIC REGRESSION DURING PROPAGATION WINDOW

1 SEP 2026 · KDP SUPERVISOR:
CROSS-LANGUAGE LINKING = AUTOMATED
+ NOT MANUALLY MANAGEABLE/CORRECTABLE BY KDP SUPPORT

=> CAPABILITY / ESCALATION / INTERNAL PROCESS NOT RECONCILED
```

The second trace cannot simply replace the first. Both must be preserved. `NEW_TRACE != RECONCILED_STATE`.

The auditable question is now: **what action was actually performed on 29 August, through which tool/team/layer, what produced the observed improvement, and why does the public state regress while another supervisor denies operational control over that same relationship?**

## 4. Observable consequence

Until propagation stabilises and the contradiction is reconciled, the public catalogue may retain incomplete or stale associations relative to the actual published editions. This affects translation discoverability, language navigation, edition-index coherence, purchase paths, traceability from intervention through propagation to regression, and identification of the responsible layer when automated state degrades.

The incident remains **OPEN** and must be checked again when KDP's maximum propagation window expires.

## 5. FACT / INFERENCE / HYPOTHESIS

### FACT

1. KDP stated on 29 Aug that it reviewed IDEA's language editions and formats and linked them across the relevant stores.
2. KDP expressly included multilingual links in the declared action.
3. KDP stated that full public propagation could take up to seven days.
4. A partial improvement was subsequently observed.
5. On 1 Sep, still within that window, a public regression to Spanish ↔ Finnish was reported.
6. Christian stated on 1 Sep that KDP Support cannot manually manage or correct cross-language association.
7. Christian offered to verify formats inside each language but did not identify the mechanism/team behind the 29 Aug declared action or confirm a new technical escalation of the multilingual regression.

### INFERENCE

An operational, escalation, metadata or catalogue layer is not being described consistently across KDP responses. The 29 Aug action may have involved an indirect tool, internal escalation, metadata intervention triggering automation, another Amazon team, or an inaccurate description of what was performed.

### FOUNDER HYPOTHESIS · H1

The current refusal to correct or re-escalate multilingual linking may reflect **operational convenience / avoidance of work or escalation**, given that KDP had declared an intervention expressly covering that layer only days earlier. This records the founder's interpretation and **is not presented as a proven intention of Christian or Amazon**.

### RIVAL HYPOTHESES

- **H2 · inaccurate 29 Aug information:** the response may have described as performed a capability KDP Support does not actually possess.
- **H3 · indirect/escalated capability:** KDP Support may lack a direct tool but have an internal route capable of producing the correction.
- **H4 · automation + auxiliary intervention:** KDP may have changed metadata/relationships that triggered automation and described the outcome as linking performed.
- **H5 · propagation not consolidated:** part of the 1 Sep regression may be transient behaviour inside the up-to-seven-day window; this affects the eventual visible state but does not remove the need to reconcile the incompatible descriptions of capability/process.

## 6. Verification and closure conditions

The audit separates two questions:

**A. Visible technical state:** after seven days, is the complete multilingual matrix stable, reciprocal and navigable?

**B. Organisational traceability:** regardless of final propagation, what exactly did KDP do on 29 Aug and how does that reconcile with the 1 Sep statement that KDP Support cannot manage that layer?

Full closure requires checking the public state at the end of the declared window; restoring the complete multilingual matrix if still degraded; identifying the responsible technical route if KDP Support cannot intervene; and reconciling the 29 Aug action. If the earlier communication was inaccurate, that should instead be acknowledged explicitly together with a real escalation route for automated multilingual-index failures.

```text
MULTILINGUAL ACTION DECLARED EXECUTED
→ UP TO 7 DAYS OF PROPAGATION
→ PARTIAL IMPROVEMENT OBSERVED
→ REGRESSION DURING WINDOW
→ LATER DENIAL OF DIRECT CAPABILITY
→ DAY-7 VERIFICATION + PROCESS RECONCILIATION
```

## 7. Relations

- [29 Aug 2026 addendum · global review declared applied](./2026-08-29_addendum_kdp_revision_global_aplicada_casos_51454627_51454666_ES_EN.md)
- [29 Aug 2026 addendum · multilingual association](./2026-08-29_addendum_kdp_asociacion_multilingue_caso_51425302_ES_EN.md)
- [28 Aug 2026 addendum · language/format](./2026-08-28_addendum_kdp_vinculacion_idiomas_formatos_caso_51425302_ES_EN.md)
- [Issue #70 · audit and challenge](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/70)
- [Public Audits index](./README.md)
- [IDEA](../../obras/idea/README.md)
