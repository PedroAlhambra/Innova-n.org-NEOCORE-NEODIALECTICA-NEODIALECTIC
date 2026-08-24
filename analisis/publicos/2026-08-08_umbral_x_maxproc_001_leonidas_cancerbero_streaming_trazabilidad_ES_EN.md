# Umbral-X MAXPROC 001 · El Dios del Control Leónidas-Cancerbero™
# Umbral-X MAXPROC 001 · The God of Control Leonidas-Cerberus™

**Fecha / Date:** 2026-08-08  
**Estado / Status:** hipótesis pública · Síntesis Abierta activa / public hypothesis · active Open Synthesis  
**Issue de contraste / Open Synthesis:** [#61 · Umbral-X MAXPROC 001](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/61)  
**Marco / Framework:** Sistema Umbral-X™ · MAXPROC · Síntesis Abierta Neodialéctica™  
**Neoarquetipo / Neoarchetype:** **El Dios del Control Leónidas-Cancerbero™**  

> **NOTA EPISTEMOLÓGICA / EPISTEMIC NOTE**  
> Este documento **no afirma** que Spotify, DistroKid o TIDAL hayan sufrido un ciberataque, hayan perdido una base de datos, estén robando regalías o actúen coordinadamente. Formula hipótesis competidoras para explicar una cadena de anomalías y solicita evidencia externa capaz de confirmarlas, limitarlas o refutarlas. / This document **does not claim** that Spotify, DistroKid or TIDAL suffered a cyberattack, lost a database, stole royalties or coordinated misconduct. It sets out competing hypotheses and asks for external evidence capable of confirming, limiting or refuting them.

---

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

# ES · Castellano

## 1. La noticia de Síntesis Abierta

Innova_N publica su **primera Hipótesis Umbral-X MAXPROC** como pieza de investigación abierta y trazable.

El objeto es una pregunta incómoda pero legítima:

> **¿qué arquitectura real de datos, identidad y pagos existe detrás de Spotify, DistroKid, TIDAL y otros DSP, y qué puede producir un círculo de soporte en el que un músico observa anomalías mientras cada capa remite a otra?**

La pregunta nace de un expediente concreto, pero no quiere quedarse en él. Se abre a todos los músicos, sellos, distribuidores, ingenieros de datos, especialistas en metadata, contabilidad de royalties y ciberseguridad que puedan aportar casos comparables.

## 2. El neoarquetipo: El Dios del Control Leónidas-Cancerbero™

Leónidas-Cancerbero™ representa una infraestructura con múltiples puertas y guardianes:

```text
MÚSICO
→ DISTRIBUIDOR
→ METADATOS
→ DSP
→ PERFIL DE ARTISTA
→ ISRC / UPC / URI / ARTIST ID
→ ESTADÍSTICAS
→ INFORMES DE ROYALTIES
→ LIQUIDACIÓN
→ SOPORTE
→ VUELTA AL DISTRIBUIDOR O AL DSP
```

El nombre **no identifica culpables personales**. Es un neoarquetipo analítico para observar sistemas en los que el control está muy concentrado pero la responsabilidad causal puede quedar fragmentada.

## 3. Señales que activan Umbral-X

En el expediente Innova_N aparecen, entre otras, estas señales:

- actividad de escucha reportada junto con ausencia observada de regalías de Spotify en la cuenta;
- tickets previos sin reconstrucción material del routing de pagos;
- respuesta reciente de DistroKid centrada en `Estimated Daily Stats` aunque la reclamación solicitaba auditoría de regalías, identificadores y asignación;
- envío posterior de encuesta de satisfacción sin haber respondido a las preguntas contables planteadas;
- antecedentes de canciones que aparecen, desaparecen o quedan asociadas/desasociadas de perfiles y catálogos;
- referencias circulares entre distribuidor y plataforma para distintos tipos de incidencias.

Documentación interna relacionada:

- [Ticket 4499471 · respuesta no resolutiva y reiteración de auditoría](./2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md)
- [Actualización Spotify–DistroKid · trazabilidad de regalías](./2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md)
- [Cierre circular y escalado](./2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md)
- [Addendum · catálogo removido/añadido y Apple Music](./2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md)

## 4. Hipótesis competidoras MAXPROC

### H1 · Ciberincidente, pérdida o degradación de infraestructura

¿Podría existir pérdida, corrupción, indisponibilidad o desincronización parcial de datos causada por un incidente técnico o de seguridad?

**Estado actual:** posible en abstracto, **sin evidencia pública suficiente para afirmarlo en este caso**.

Además, la página pública de estado de Spotify no registra incidentes generales durante mayo, junio o julio de 2026, lo que debilita la versión fuerte de una caída general reciente conocida:

- Spotify Status · Incident History: https://spotify.statuspage.io/history

Esto **no excluye** un problema interno, parcial, de reconciliación, seguridad o datos que no afecte a disponibilidad general.

### H2 · Fragmentación de bases de datos y metadatos

Es la hipótesis que hoy dispone de mayor apoyo externo general.

Spotify reconoce oficialmente que problemas de nombre de artista, release, créditos, disponibilidad y otros metadatos deben corregirse a través del sello o distribuidor, porque Spotify muestra la música según los metadatos que recibe:

- Spotify · Fixing problems with music metadata: https://support.spotify.com/artists/article/fixing-problems-with-music/

Spotify también reconoce explícitamente que música y catálogos pueden quedar mezclados entre perfiles diferentes:

- Spotify · Music mixed up with another artist: https://support.spotify.com/artists/article/music-mixed-up-with-another-artist/

DistroKid dispone de `Fixer` precisamente porque releases pueden desaparecer del perfil correcto o quedar mapeadas a otro artista:

- DistroKid · My Spotify Release is Missing From My Artist Page: https://support.distrokid.com/hc/en-us/articles/10403637585939-My-Spotify-Release-is-Missing-From-My-Artist-Page
- DistroKid · Making Sure Your Music is On the Correct Spotify and Apple Music Page: https://support.distrokid.com/hc/en-us/articles/4401872567699-Making-Sure-Your-Music-is-On-the-Correct-Spotify-and-Apple-Music-Page

DistroKid añade un dato estructural importante: el mapping final de páginas de artista **no está bajo control directo del distribuidor**, sino que lo gestionan los propios servicios.

TIDAL también contempla perfiles duplicados y fusiones. Su documentación explica que, al fusionar perfiles, sólo permanece uno activo y los seguidores del perfil cerrado no se transfieren; también indica que ciertos datos de perfil se ajustan según los registros recibidos del distribuidor:

- TIDAL · Claim Your Artist Profile: https://support.tidal.com/hc/en-us/articles/44170181437713-Claim-Your-Artist-Profile

Una publicación académica sobre infraestructura de metadata musical describe precisamente un ecosistema en el que distintas entidades mantienen versiones propias de los mismos datos y las correcciones/sincronizaciones resultan manualmente laboriosas y propensas a error:

- Hardjono et al., *Towards an Open and Scalable Music Metadata Layer*: https://arxiv.org/abs/1911.08278

### H3 · Error humano o automatización defectuosa

La propia existencia de herramientas para corregir mapping, merges y perfiles duplicados demuestra que los errores de asociación son una clase conocida de problema.

Esto no permite atribuir el error concreto a una persona, pero hace plausible una combinación de:

- datos cargados con identificadores incompletos;
- cambios de perfil;
- merges;
- páginas de artista homónimas;
- redelivery de metadata;
- procesos automatizados de matching;
- intervención manual posterior.

Casos históricos de la comunidad de Spotify documentan canciones asignadas a perfiles equivocados, perfiles duplicados y problemas que exigen coordinación entre artista, distribuidor y Spotify:

- https://community.spotify.com/t5/Content-Questions/Wrong-artist-page/td-p/4877279
- https://community.spotify.com/t5/Content-Questions/Release-listed-on-the-wrong-profile/td-p/5139962
- https://community.spotify.com/t5/Content-Questions/My-music-listed-under-wrong-artist/td-p/1530282

Estos testimonios son **casos anecdóticos**, no una medición de incidencia global.

### H4 · Soporte sin acceso a la capa que resuelve el problema

Una explicación compatible con el círculo observado es que los agentes de primera línea dispongan de guías sobre estadísticas, metadata o herramientas de reparación, pero no de acceso directo a:

- informes de royalties recibidos del DSP;
- asignaciones contables por ISRC;
- reglas internas de conciliación;
- registros históricos de remapping;
- ledger de pagos;
- eventos de modificación de ownership o asociación.

Si esto fuera cierto, una respuesta genérica podría ser correcta en su dominio y, al mismo tiempo, irrelevante para el expediente concreto.

### H5 · Fraude, suplantación o apropiación por terceros

Debe investigarse **sólo cuando existan indicios concretos**.

Existe evidencia histórica independiente de que terceros han conseguido subir música no autorizada, hacerse pasar por artistas o introducir releases en perfiles ajenos. Pitchfork documentó en 2019 múltiples casos de impostores y uploads no autorizados y señaló la fragmentación de metadata como una vulnerabilidad estructural del ecosistema:

- Pitchfork · *How Artist Imposters and Fake Songs Sneak Onto Streaming Services*: https://pitchfork.com/features/article/how-artist-imposters-and-fake-songs-sneak-onto-streaming-services/

Esto demuestra que **la clase de ataque existe**, no que explique nuestro caso.

### H6 · Estadísticas y royalties pertenecen a sistemas distintos

DistroKid afirma que las estadísticas diarias estimadas y los informes de ingresos proceden de sistemas diferentes, y que las fluctuaciones de la API de estadísticas no afectan por sí mismas a las regalías reales:

- DistroKid · My Stats Disappeared: https://support.distrokid.com/hc/en-us/articles/360013647473-My-Stats-Disappeared

Por tanto:

```text
ANOMALÍA DE ESTADÍSTICAS
≠
PRUEBA DE ANOMALÍA DE REGALÍAS
```

Pero también funciona en sentido inverso:

```text
EXPLICAR LA API DE ESTADÍSTICAS
≠
AUDITAR EL LEDGER DE REGALÍAS
```

Ese es precisamente uno de los puntos centrales del expediente actual.

## 5. Dictamen provisional Umbral-X

A fecha de esta publicación:

```text
CIBERATAQUE CONFIRMADO
→ NO

PÉRDIDA DE BASE DE DATOS CONFIRMADA
→ NO

ROBO DE REGALÍAS CONFIRMADO
→ NO

FRAGMENTACIÓN / ERRORES DE METADATOS COMO CLASE CONOCIDA
→ SÍ

CASOS EXTERNOS DE MAPPING INCORRECTO
→ SÍ

CASOS EXTERNOS DE SUPLANTACIÓN / UPLOAD NO AUTORIZADO
→ SÍ

RESPUESTA ACTUAL DE SOPORTE SUFICIENTE PARA AUDITAR NUESTRO CASO
→ NO

NECESIDAD DE RECONSTRUIR IDENTIFICADORES + INFORMES + ROUTING
→ SÍ
```

La hipótesis más parsimoniosa **por ahora** no es “han perdido toda la base de datos” sino una combinación posible de **fragmentación de metadata, capas de soporte desacopladas y ausencia de trazabilidad extremo a extremo**. Sin embargo, MAXPROC mantiene abiertas H1–H6 hasta disponer de datos que discriminen entre ellas.

## 6. Llamamiento mundial a músicos

Buscamos músicos y sellos que hayan sufrido cualquiera de estos problemas con **DistroKid, Spotify, TIDAL u otros DSP**:

- regalías ausentes o inexplicablemente a cero;
- canciones que desaparecen y reaparecen;
- catálogos partidos entre dos perfiles;
- música colocada en el perfil de otro artista;
- música ajena apareciendo en el perfil propio;
- cambios inesperados de ISRC, UPC, URI o artist ID;
- perfiles fusionados o desasociados;
- errores simultáneos en varias plataformas;
- soporte circular entre distribuidor y DSP;
- casos de fraude, suplantación o robo demostrable;
- casos donde el sistema funcionó correctamente y contradice nuestras sospechas.

### Formato recomendado de aporte

1. plataforma;
2. distribuidor;
3. fecha aproximada;
4. identificadores que puedan hacerse públicos;
5. qué cambió o desapareció;
6. efecto sobre estadísticas;
7. efecto sobre regalías;
8. respuestas recibidas;
9. resolución final;
10. hipótesis que el caso apoya o refuta.

**Síntesis Abierta:** [Issue #61](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/61)

## 7. Regla MAXPROC

> **HIPÓTESIS ≠ HECHO**  
> **CORRELACIÓN ≠ CAUSALIDAD**  
> **RESPUESTA EVASIVA ≠ PRUEBA DE FRAUDE**  
> **ERROR DE METADATOS ≠ ERROR DE REGALÍAS**  
> **PERO AUSENCIA DE TRAZABILIDAD = PROBLEMA AUDITABLE**

La función de Umbral-X no es confirmar la sospecha inicial. Es **hacerla sobrevivir o morir ante evidencia externa**.

---

# EN · English

## 1. Open-Synthesis news item

Innova_N publishes its **first Umbral-X MAXPROC Hypothesis** as an open and traceable research piece.

The object is an uncomfortable but legitimate question:

> **what real architecture of data, identity and payments exists behind Spotify, DistroKid, TIDAL and other DSPs, and what can produce a support circle in which a musician observes anomalies while each layer refers them to another?**

The question starts from a concrete case, but it is not intended to remain there. It is opened to all musicians, labels, distributors, data engineers, metadata specialists, royalty-accounting professionals and cybersecurity specialists who can contribute comparable cases.

## 2. The neoarchetype: The God of Control Leonidas-Cerberus™

Leonidas-Cerberus™ represents infrastructure with multiple gates and guardians:

```text
MUSICIAN
→ DISTRIBUTOR
→ METADATA
→ DSP
→ ARTIST PROFILE
→ ISRC / UPC / URI / ARTIST ID
→ STATISTICS
→ ROYALTY REPORTS
→ SETTLEMENT
→ SUPPORT
→ BACK TO DISTRIBUTOR OR DSP
```

The name **does not identify personal culprits**. It is an analytical neoarchetype for observing systems in which control is highly concentrated while causal responsibility may remain fragmented.

## 3. Signals activating Umbral-X

The Innova_N case contains, among others, the following signals:

- reported listening activity together with an observed absence of Spotify royalties in the account;
- previous tickets without material reconstruction of payment routing;
- a recent DistroKid reply focused on `Estimated Daily Stats` even though the claim requested an audit of royalties, identifiers and allocation;
- a subsequent satisfaction survey sent without answering the accounting questions raised;
- a history of songs appearing, disappearing or becoming associated/disassociated with profiles and catalogues;
- circular referrals between distributor and platform for different kinds of incidents.

Related internal documentation:

- [Ticket 4499471 · non-substantive reply and renewed audit request](./2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md)
- [Spotify–DistroKid update · royalty traceability](./2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md)
- [Circular closure and escalation](./2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md)
- [Addendum · catalogue removed/added and Apple Music](./2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md)

## 4. Competing MAXPROC hypotheses

### H1 · Cyberincident, loss or infrastructure degradation

Could there be loss, corruption, unavailability or partial desynchronisation of data caused by a technical or security incident?

**Current status:** possible in the abstract, **without sufficient public evidence to assert it in this case**.

Spotify's public status page also records no general incidents during May, June or July 2026, which weakens the strong version of a known recent platform-wide outage:

- Spotify Status · Incident History: https://spotify.statuspage.io/history

This **does not exclude** an internal, partial, reconciliation, security or data problem that does not affect general availability.

### H2 · Fragmentation of databases and metadata

This is the hypothesis that currently has the strongest general external support.

Spotify officially acknowledges that problems involving artist names, releases, credits, availability and other metadata must be corrected through the label or distributor because Spotify displays music according to the metadata it receives:

- Spotify · Fixing problems with music metadata: https://support.spotify.com/artists/article/fixing-problems-with-music/

Spotify also expressly recognises that music and catalogues may become mixed between different profiles:

- Spotify · Music mixed up with another artist: https://support.spotify.com/artists/article/music-mixed-up-with-another-artist/

DistroKid provides `Fixer` precisely because releases may disappear from the correct profile or become mapped to another artist:

- DistroKid · My Spotify Release is Missing From My Artist Page: https://support.distrokid.com/hc/en-us/articles/10403637585939-My-Spotify-Release-is-Missing-From-My-Artist-Page
- DistroKid · Making Sure Your Music is On the Correct Spotify and Apple Music Page: https://support.distrokid.com/hc/en-us/articles/4401872567699-Making-Sure-Your-Music-is-On-the-Correct-Spotify-and-Apple-Music-Page

DistroKid adds an important structural fact: final mapping of artist pages is **not under the distributor's direct control**, but is managed by the services themselves.

TIDAL also contemplates duplicate profiles and merges. Its documentation explains that when profiles are merged only one remains active and followers of the closed profile are not transferred; it also says that certain profile data is adjusted according to records received from the distributor:

- TIDAL · Claim Your Artist Profile: https://support.tidal.com/hc/en-us/articles/44170181437713-Claim-Your-Artist-Profile

An academic publication on music-metadata infrastructure describes precisely an ecosystem in which different entities maintain their own versions of the same data and corrections/synchronisations are manually laborious and error-prone:

- Hardjono et al., *Towards an Open and Scalable Music Metadata Layer*: https://arxiv.org/abs/1911.08278

### H3 · Human error or defective automation

The very existence of tools to correct mapping, merges and duplicate profiles demonstrates that association errors are a known class of problem.

This does not permit attribution of a specific error to a person, but makes plausible a combination of:

- data uploaded with incomplete identifiers;
- profile changes;
- merges;
- homonymous artist pages;
- metadata redelivery;
- automated matching processes;
- later manual intervention.

Historical Spotify community cases document songs assigned to incorrect profiles, duplicate profiles and problems requiring coordination among artist, distributor and Spotify:

- https://community.spotify.com/t5/Content-Questions/Wrong-artist-page/td-p/4877279
- https://community.spotify.com/t5/Content-Questions/Release-listed-on-the-wrong-profile/td-p/5139962
- https://community.spotify.com/t5/Content-Questions/My-music-listed-under-wrong-artist/td-p/1530282

These testimonies are **anecdotal cases**, not a measurement of global incidence.

### H4 · Support without access to the layer that resolves the problem

An explanation compatible with the observed circle is that first-line agents may have guidance on statistics, metadata or repair tools but not direct access to:

- royalty reports received from the DSP;
- accounting allocations by ISRC;
- internal reconciliation rules;
- historical remapping records;
- payment ledgers;
- events modifying ownership or association.

If this were true, a generic answer could be correct within its own domain and at the same time irrelevant to the concrete case.

### H5 · Fraud, impersonation or appropriation by third parties

This should be investigated **only when concrete indicators exist**.

There is independent historical evidence that third parties have managed to upload unauthorised music, impersonate artists or introduce releases into other artists' profiles. Pitchfork documented multiple cases of impostors and unauthorised uploads in 2019 and identified fragmented metadata as a structural vulnerability of the ecosystem:

- Pitchfork · *How Artist Imposters and Fake Songs Sneak Onto Streaming Services*: https://pitchfork.com/features/article/how-artist-imposters-and-fake-songs-sneak-onto-streaming-services/

This demonstrates that **the class of attack exists**, not that it explains this case.

### H6 · Statistics and royalties belong to different systems

DistroKid states that estimated daily statistics and earnings reports come from different systems and that fluctuations in the statistics API do not by themselves affect actual royalties:

- DistroKid · My Stats Disappeared: https://support.distrokid.com/hc/en-us/articles/360013647473-My-Stats-Disappeared

Therefore:

```text
STATISTICS ANOMALY
≠
PROOF OF ROYALTY ANOMALY
```

But the inverse also applies:

```text
EXPLAINING THE STATISTICS API
≠
AUDITING THE ROYALTY LEDGER
```

That is precisely one of the central points of the current case.

## 5. Provisional Umbral-X finding

As of this publication:

```text
CONFIRMED CYBERATTACK
→ NO

CONFIRMED DATABASE LOSS
→ NO

CONFIRMED ROYALTY THEFT
→ NO

METADATA FRAGMENTATION / ERRORS AS A KNOWN CLASS
→ YES

EXTERNAL CASES OF INCORRECT MAPPING
→ YES

EXTERNAL CASES OF IMPERSONATION / UNAUTHORISED UPLOAD
→ YES

CURRENT SUPPORT RESPONSE SUFFICIENT TO AUDIT OUR CASE
→ NO

NEED TO RECONSTRUCT IDENTIFIERS + REPORTS + ROUTING
→ YES
```

The most parsimonious hypothesis **for now** is not “they lost the entire database”, but a possible combination of **metadata fragmentation, decoupled support layers and lack of end-to-end traceability**. MAXPROC nevertheless keeps H1–H6 open until data exist that can discriminate among them.

## 6. Worldwide call to musicians

We are seeking musicians and labels who have experienced any of the following problems with **DistroKid, Spotify, TIDAL or other DSPs**:

- missing royalties or royalties inexplicably at zero;
- songs disappearing and reappearing;
- catalogues split across two profiles;
- music placed on another artist's profile;
- someone else's music appearing on one's own profile;
- unexpected changes in ISRC, UPC, URI or artist ID;
- merged or disassociated profiles;
- simultaneous errors across multiple platforms;
- circular support between distributor and DSP;
- cases of proven fraud, impersonation or theft;
- cases in which the system worked correctly and contradicts our suspicions.

### Recommended contribution format

1. platform;
2. distributor;
3. approximate date;
4. identifiers that can be made public;
5. what changed or disappeared;
6. effect on statistics;
7. effect on royalties;
8. responses received;
9. final resolution;
10. hypothesis supported or refuted by the case.

**Open Synthesis:** [Issue #61](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/61)

## 7. MAXPROC rule

> **HYPOTHESIS ≠ FACT**  
> **CORRELATION ≠ CAUSATION**  
> **EVASIVE RESPONSE ≠ PROOF OF FRAUD**  
> **METADATA ERROR ≠ ROYALTY ERROR**  
> **BUT ABSENCE OF TRACEABILITY = AUDITABLE PROBLEM**

The function of Umbral-X is not to confirm the initial suspicion. It is to **make it survive or die under external evidence**.


---

**Pedro Martínez Alhambra · Innova_N · Sistema Umbral-X™ · MAXPROC · Síntesis Abierta Neodialéctica™**