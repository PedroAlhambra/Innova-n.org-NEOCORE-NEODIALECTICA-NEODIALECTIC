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

Innova_N publishes its **first Umbral-X MAXPROC Hypothesis** as an open, traceable investigation.

The question is whether the observed circularity among artist, distributor and DSP is best explained by a cyberincident, fragmented metadata, human or automated mapping error, support-layer limitations, third-party fraud, accounting/reporting separation, or some combination of these.

## 2. Leonidas-Cerberus™ as neoarchetype

**The God of Control Leonidas-Cerberus™** names a system in which access, identity, catalogue, metadata and payment pass through multiple controlled gates while causal responsibility may remain fragmented. It is an analytical neoarchetype, not an accusation against any individual.

## 3. Current evidence

Official Spotify and DistroKid documentation confirms that artist-profile mapping and metadata errors are a known class of problem and often require coordination between service and distributor. TIDAL documents profile merging and distributor-dependent profile data. Academic work describes music metadata as fragmented across multiple proprietary or independently maintained records. Historical reporting also documents unauthorized uploads and artist impersonation.

At the same time, Spotify's public status history reports no general incidents for May–July 2026. This weakens the strong hypothesis of a known platform-wide outage, while not ruling out internal, partial, security, reconciliation or data-layer problems.

## 4. Working hypotheses

- **H1:** cyberincident or infrastructure/data degradation;
- **H2:** fragmented databases and metadata reconciliation;
- **H3:** human or automated mapping error;
- **H4:** support agents without access to the relevant accounting/routing layer;
- **H5:** third-party fraud, impersonation or unauthorized upload;
- **H6:** separation between audience-statistics systems and royalty-reporting systems.

No hypothesis is treated as established fact.

## 5. Call to musicians and technical specialists

We invite musicians, labels, distributors, metadata engineers, cybersecurity specialists and royalty-accounting professionals to contribute comparable cases involving missing royalties, disappearing releases, split artist profiles, wrong mappings, changed identifiers, circular support, unauthorized uploads, proven fraud, or evidence showing that these suspicions are wrong.

**Open Synthesis:** [Issue #61](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/61)

## 6. MAXPROC rule

> **HYPOTHESIS ≠ FACT**  
> **CORRELATION ≠ CAUSATION**  
> **EVASIVE SUPPORT ≠ PROOF OF FRAUD**  
> **METADATA ERROR ≠ ROYALTY ERROR**  
> **BUT MISSING TRACEABILITY = AN AUDITABLE PROBLEM**

Umbral-X exists not to confirm an initial suspicion, but to make it **survive or fail under external evidence**.

---

**Pedro Martínez Alhambra · Innova_N · Sistema Umbral-X™ · MAXPROC · Síntesis Abierta Neodialéctica™**