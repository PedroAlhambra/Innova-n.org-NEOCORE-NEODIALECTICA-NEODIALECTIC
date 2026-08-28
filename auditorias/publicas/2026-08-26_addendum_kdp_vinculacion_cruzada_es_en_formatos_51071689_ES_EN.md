# Addendum auditoría Amazon KDP · vinculación cruzada ES/EN en formatos de IDEA
# Amazon KDP audit addendum · ES/EN cross-linking and missing paperback visibility in IDEA formats

**Fecha / Date:** 2026-08-26  
**Caso KDP relacionado / Related KDP case:** 51071689  
**Estado / Status:** incidencia reproducida · evidencia visual conservada por Neo0™ · comunicada a soporte KDP · pendiente de resolución / reproduced incident · visual evidence retained by Neo0™ · reported to KDP Support · resolution pending  
**Objeto / Object:** IDEA — Pedro Martínez Alhambra

[ES · Castellano](#es--hecho-observado) · [EN · English](#en--observed-fact)

---

## ES · Hecho observado

En Amazon.es, una búsqueda de `idea pedro martinez alhambra` presenta una ficha de **IDEA** que indica **«Opciones: 2 idiomas y 3 formatos»**.

La secuencia reproducida es:

1. El resultado de búsqueda conduce a la ficha de IDEA.
2. Con **Tapa dura** seleccionada, la ficha muestra **Idioma: Español** y ofrece **Versión Kindle / Tapa dura / Tapa blanda**.
3. Sin abandonar esa ficha, al seleccionar **Tapa blanda**, Amazon cambia de portada y muestra explícitamente **«Edición en Inglés»**.
4. Al acceder a la ficha que Amazon identifica explícitamente como **«Edición en Inglés»**, la interfaz visible muestra únicamente **Versión Kindle** y **Tapa dura**; **no aparece la opción Tapa blanda**.
5. En las comprobaciones realizadas, la **tapa blanda en castellano tampoco resulta localizable como edición seleccionable independiente**. Dado que todavía no se ha determinado si está despublicada, oculta, mal vinculada o accesible mediante otra ruta, se registra prudentemente como **no localizada en la interfaz comprobada**, no como desaparición definitiva.

Por tanto, la incidencia no consiste simplemente en que Amazon ofrezca una edición inglesa junto a la española. Existe una incoherencia más amplia en la matriz **idioma × formato**: el selector de formato de una ficha presentada como española conduce a una edición inglesa, mientras que la propia ficha inglesa no muestra tapa blanda y la tapa blanda española no ha podido localizarse por la navegación comprobada.

## ES · Riesgo para el comprador

La interfaz puede inducir al comprador a interpretar que está cambiando únicamente de formato —de tapa dura española a tapa blanda española— cuando en realidad también cambia el idioma de la obra a inglés. Además, la ausencia visible de determinadas combinaciones idioma/formato dificulta saber qué edición se está comprando y si todos los formatos publicados continúan correctamente accesibles.

Esto constituye una regresión o incoherencia de vinculación catálogo/idioma/formato y puede provocar una compra en un idioma distinto del esperado o impedir localizar una edición existente.

## ES · Relación con la auditoría previa

Esta incidencia se incorpora a la genealogía del **caso KDP 51071689**. En el seguimiento anterior KDP/Author Central había confirmado la revisión de las asociaciones de formatos e idiomas de IDEA. La reproducción del 26 de agosto demuestra que la coherencia visible para el comprador no puede considerarse cerrada de forma permanente y requiere postcheck posterior a cualquier corrección.

La estructura esperada es:

- Español: Kindle ↔ tapa blanda ↔ tapa dura.
- Inglés: Kindle ↔ tapa blanda ↔ tapa dura.
- Cada idioma adicional: sus formatos deben permanecer dentro de su propia familia lingüística.

Un selector de formato no debe sustituir silenciosamente el idioma y un formato publicado no debería quedar inaccesible por una asociación incorrecta.

## ES · Evidencia y acción

Se conservaron capturas consecutivas de la interfaz Amazon que documentan: resultado de búsqueda, ficha en tapa dura española, cambio a tapa blanda con rótulo «Edición en Inglés» y ficha identificada como inglesa en la que solo aparecen Kindle y tapa dura.

El **26 de agosto de 2026** se envió a soporte KDP un correo dentro del hilo del **caso 51071689**, adjuntando evidencias y solicitando:

- revisión de la relación ASIN/ISBN ↔ idioma ↔ formato;
- corrección de la vinculación cruzada español/inglés;
- localización/restauración de la tapa blanda española si continúa publicada pero ha quedado oculta o desvinculada;
- comprobación de por qué la ficha inglesa no ofrece tapa blanda;
- comprobación del resto de familias lingüísticas de IDEA;
- preservación de la relación correcta entre formatos de un mismo idioma.

## ES · Ampliación 2026-08-27 · idiomas disponibles incompletos y reciprocidad global

Se detecta una tercera incoherencia de catálogo. Desde la edición en castellano, al consultar las **ediciones/idiomas disponibles**, Amazon muestra únicamente **finlandés** como alternativa lingüística.

Esto no representa la familia real de la obra: **IDEA está publicada en múltiples idiomas**, por lo que la ficha española debería permitir acceder a todas las ediciones lingüísticas correctamente relacionadas que Amazon tenga publicadas y activas, no únicamente a la finlandesa.

Además, esta relación debe ser **recíproca y global**. No basta con corregir la ficha española. Desde **cada edición lingüística publicada de IDEA** deberían aparecer correctamente enlazadas las demás ediciones lingüísticas disponibles de la misma obra. Ningún idioma debería quedar aislado, parcialmente relacionado o visible sólo desde determinadas ediciones.

La matriz esperada es, conceptualmente:

```text
CADA IDIOMA
├─ Kindle (si publicado)
├─ Tapa blanda (si publicada)
└─ Tapa dura (si publicada)

Y DESDE CADA IDIOMA:
→ acceso coherente a TODOS LOS DEMÁS IDIOMAS publicados y activos

FORMATO ≠ IDIOMA
CAMBIO DE FORMATO → permanece en el mismo idioma
CAMBIO DE IDIOMA → conduce expresamente a la edición de ese idioma
RELACIÓN ENTRE IDIOMAS → recíproca, completa y no aislante
```

Por tanto, el problema ya no puede comprobarse únicamente como `ES → otros idiomas`, sino como una matriz completa **idioma × idioma × formato**. Una corrección satisfactoria requiere verificar las asociaciones desde todas las familias lingüísticas publicadas de IDEA.

El **27 de agosto de 2026** se comunicó esta ampliación a soporte KDP solicitando expresamente:

- por qué desde la edición española sólo aparece finlandés como idioma disponible;
- que todas las ediciones lingüísticas publicadas de IDEA estén correctamente relacionadas y accesibles;
- que esa vinculación sea recíproca desde cada edición lingüística hacia las demás;
- que cada idioma mantenga correctamente agrupados sus propios formatos;
- que cambiar de formato no cambie silenciosamente el idioma;
- que cambiar de idioma conduzca explícitamente a la edición correspondiente;
- que ninguna edición lingüística quede aislada u oculta respecto de la familia completa;
- que KDP revise globalmente las asociaciones ASIN/ISBN ↔ idioma ↔ formato y valide el resultado en las páginas públicas de Amazon.

La prioridad de resolución se mantiene alta porque la incidencia afecta simultáneamente a **idioma, formato, reciprocidad y descubribilidad de ediciones**, con riesgo de confusión, compra errónea y pérdida de ventas.

**Estado de síntesis:** abierto. No atribuir todavía causa técnica concreta ni afirmar la retirada definitiva de formatos o idiomas hasta recibir respuesta o evidencia adicional de Amazon KDP.

---

## EN · Observed fact

On Amazon.es, a search for `idea pedro martinez alhambra` displays an **IDEA** listing indicating **“Options: 2 languages and 3 formats”**.

The reproduced sequence is:

1. The search result leads to the IDEA product page.
2. With **Hardcover** selected, the page shows **Language: Spanish** and offers **Kindle / Hardcover / Paperback**.
3. Without leaving that product page, selecting **Paperback** changes the cover and explicitly displays **“English Edition”**.
4. On the product page explicitly identified by Amazon as the **English Edition**, the visible interface shows only **Kindle** and **Hardcover**; **Paperback is not displayed**.
5. During the checks performed, the **Spanish paperback could likewise not be located as an independently selectable edition**. Because it has not yet been established whether it is unpublished, hidden, incorrectly linked, or reachable through another route, the audit records it conservatively as **not located in the checked interface**, rather than definitively disappeared.

The issue is therefore broader than Amazon merely offering an English edition alongside the Spanish edition. There is an inconsistency in the **language × format** matrix: the format selector on a Spanish-presented page leads to an English edition, while the English page itself does not display a paperback and the Spanish paperback cannot currently be located through the checked navigation path.

## EN · Buyer risk

The interface can lead a buyer to believe that only the format is being changed —from Spanish hardcover to Spanish paperback— while the language of the work is also being changed to English. Missing visible language/format combinations also make it difficult to determine which edition is being purchased and whether all published formats remain correctly accessible.

This constitutes a catalogue/language/format linking regression or inconsistency and can result in a purchase in a language different from the one expected, or prevent an existing edition from being found.

## EN · Relation to the previous audit

This incident is incorporated into the genealogy of **KDP case 51071689**. During earlier follow-up, KDP/Author Central had confirmed review of IDEA's format and language associations. The reproduction on 26 August demonstrates that buyer-visible consistency cannot be considered permanently closed and requires a postcheck after any correction.

Expected structure:

- Spanish: Kindle ↔ paperback ↔ hardcover.
- English: Kindle ↔ paperback ↔ hardcover.
- Each additional language: its formats must remain within its own language family.

A format selector must not silently replace the language, and a published format should not become inaccessible because of an incorrect association.

## EN · Evidence and action

Consecutive screenshots of the Amazon interface were retained documenting: search result, Spanish hardcover page, switch to paperback displaying “English Edition”, and the page identified as English where only Kindle and hardcover are visible.

On **26 August 2026**, an email was sent to KDP Support in the thread for **case 51071689**, attaching evidence and requesting:

- review of ASIN/ISBN ↔ language ↔ format relationships;
- correction of the Spanish/English cross-linking;
- location/restoration of the Spanish paperback if it remains published but has become hidden or unlinked;
- investigation of why the English page does not offer paperback;
- verification of the remaining IDEA language families;
- preservation of correct relationships among formats belonging to the same language.

## EN · 2026-08-27 extension · incomplete languages and global reciprocal linking

A third catalogue inconsistency has now been detected. From the Spanish edition, when checking the **available editions/languages**, Amazon currently shows only **Finnish** as an alternative language.

This does not represent the actual language family of the work: **IDEA has been published in multiple languages**, so the Spanish product page should provide access to all correctly linked published and active language editions, rather than only Finnish.

This relationship must also be **global and reciprocal**. Correcting only the Spanish page is insufficient. From **every published language edition of IDEA**, the other available language editions of the same work should be correctly linked. No language should remain isolated, partially related, or discoverable only from selected editions.

The expected conceptual matrix is:

```text
EACH LANGUAGE
├─ Kindle (if published)
├─ Paperback (if published)
└─ Hardcover (if published)

AND FROM EACH LANGUAGE:
→ coherent access to ALL OTHER published and active languages

FORMAT ≠ LANGUAGE
FORMAT CHANGE → remains within the same language
LANGUAGE CHANGE → explicitly opens that language edition
LANGUAGE RELATION → reciprocal, complete and non-isolating
```

The issue therefore can no longer be tested merely as `ES → other languages`; it requires checking the complete **language × language × format** matrix across IDEA's published editions.

On **27 August 2026**, this extension was reported to KDP Support, explicitly requesting:

- investigation of why only Finnish appears as an available language from the Spanish edition;
- correct linking and accessibility of all published IDEA language editions;
- reciprocal linking from every language edition to the remaining language editions;
- correct grouping of each language's own formats;
- assurance that changing format does not silently change language;
- assurance that changing language explicitly opens the corresponding language edition;
- assurance that no language edition remains isolated or hidden from the complete family;
- global review of ASIN/ISBN ↔ language ↔ format associations and validation in Amazon's public product pages.

Resolution remains high priority because the incident simultaneously affects **language, format, reciprocity and edition discoverability**, creating risk of customer confusion, wrong-language purchases and lost sales.

**Synthesis status:** open. No specific technical cause or definitive removal of any format or language should be asserted until Amazon KDP provides a response or further evidence is obtained.
