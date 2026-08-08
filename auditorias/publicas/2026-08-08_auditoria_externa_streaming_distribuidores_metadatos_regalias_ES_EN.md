# Auditoría externa · Streaming, distribuidores, metadatos, perfiles y regalías
# External audit · Streaming, distributors, metadata, profiles and royalties

**Fecha / Date:** 2026-08-08  
**Vinculada a / Linked to:** Umbral-X MAXPROC 001 · Leónidas-Cancerbero™  
**Síntesis Abierta / Open Synthesis:** https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/61

> **Nota epistemológica.** Esta auditoría reúne documentación oficial, artículos técnicos, periodismo y testimonios públicos. Las quejas de usuarios y foros son señales, no pruebas automáticas de fraude. No se atribuye conducta delictiva a Spotify, DistroKid, TIDAL, Apple, Amazon, YouTube, Deezer, SoundCloud, TuneCore, CD Baby, Ditto ni a artistas concretos sin evidencia verificable.

---

# ES · Castellano

## 1. Dictamen provisional

El patrón externo **sí existe** y no está limitado a una plataforma ni a un distribuidor. Hay documentación oficial y casos públicos sobre:

- música asignada al artista equivocado;
- perfiles duplicados o fusionados incorrectamente;
- catálogos partidos;
- releases que desaparecen o reaparecen;
- metadatos inconsistentes;
- dependencia de distribuidor/sello para corregir datos;
- estadísticas y liquidaciones en capas distintas;
- soporte circular entre DSP y distribuidor;
- reclamaciones sobre regalías retenidas o no explicadas;
- fraude, suplantación y subidas no autorizadas por terceros;
- pérdidas de métricas sociales cuando una corrección mueve contenido entre perfiles.

Lo que **no** aparece demostrado de forma general es una única causa coordinada o una pérdida masiva de base de datos. La explicación que mejor encaja hoy con el conjunto es una cadena fragmentada de DDEX/metadata + reconciliación de identidades + automatización + revisión humana + sistemas de reporting y pagos separados. Esa arquitectura abre además superficie para error, abuso y fraude de terceros.

## 2. Evidencia oficial por plataforma

### Spotify

Spotify declara que los metadatos controlan cómo aparece la música y que los recibe del sello o distribuidor. Los problemas de metadata deben corregirse mediante una actualización del distribuidor:

- https://support.spotify.com/ws/artists/article/metadata-formatting-guidelines/
- https://support.spotify.com/es/artists/article/music-mixed-up-with-another-artist/
- https://support.spotify.com/pw/article/faulty-inaccurate-metadata/

La propia comunidad oficial de Spotify documentó un fallo de Release Radar causado por uploads que se asociaban inicialmente al artista homónimo equivocado. Spotify explicó que el problema estaba profundamente ligado a una combinación de error humano, metadata recibida de distribuidores y limitaciones técnicas, y reconoció que no existía una solución preventiva completa en ese momento:

- https://community.spotify.com/t5/Your-Library/Release-Radar-includes-wrong-artist-with-same-name-as-desired/td-p/4883304/page/10
- https://community.spotify.com/t5/Content-Questions/My-music-listed-under-wrong-artist/td-p/1530282/page/2

### Apple Music

Casos en Apple Support Communities muestran música asociada al artista homónimo equivocado, perfiles fusionados o enlaces incorrectos. En respuestas oficiales se remite al distribuidor porque la publicación y los cambios de artist information dependen de Music Partners/distribuidores:

- https://discussions.apple.com/thread/255994441
- https://discussions.apple.com/thread/254162589
- https://discussions.apple.com/thread/254860671
- https://discussions.apple.com/thread/251614042
- https://discussions.apple.com/thread/256193428
- https://discussions.apple.com/thread/252522614

### TIDAL

TIDAL reconoce perfiles duplicados, procesos de merge y dependencia de los datos del distribuidor. En una fusión, los seguidores del perfil cerrado no se transfieren, lo que demuestra que una reparación de identidad puede tener costes de continuidad:

- https://support.tidal.com/hc/en-us/articles/44170181437713-Claim-Your-Artist-Profile
- https://support.tidal.com/hc/es/articles/44170181437713-C%C3%B3mo-reclamar-tu-perfil-de-artista
- https://support.tidal.com/hc/en-us/articles/44745598330385-Delete-Your-Tidal-Account-or-Artist-Data
- https://support.tidal.com/hc/en-us/articles/15724815813137-Artist-Resources

### YouTube / YouTube Music

YouTube explica que Art Tracks y páginas de artista se construyen a partir de metadata enviada por partners/distribuidores mediante DDEX y que errores de asociación, artista primario, visibilidad o discografía requieren corrección/redelivery:

- https://support.google.com/youtube/answer/6082427?hl=en
- https://support.google.com/youtube/answer/6082726?hl=en
- https://support.google.com/youtubemusic/answer/13420518?hl=en
- https://support.google.com/youtubemusic/answer/9105565?hl=en

Casos públicos recientes:

- DistroKid + canciones en canal equivocado durante semanas: https://support.google.com/youtubemusic/thread/425763799/my-music-is-on-the-wrong-channel?hl=en
- Amuse + OAC aprobado pero releases fusionados con otro artista durante meses: https://support.google.com/youtubemusic/thread/381267948/my-oac-official-artist-channel-is-approved-but-my-songs-are-merged-with-another-artist%E2%80%99s-channel-b?hl=en
- otros artistas apareciendo en un canal y nombres incompletos: https://support.google.com/youtubemusic/thread/388623661/youtube-music-channel-issue-wrong-artist-names-extra-tracks?hl=en

### Amazon Music

Amazon ofrece una admisión particularmente clara: el feed DDEX es complejo y, aunque muy fiable, las señales que identifican perfiles pueden no comunicarse correctamente. Enumera explícitamente música de otros artistas en un perfil, contenido ausente y nombres incorrectos:

- https://intercom.help/amazon-music-for-artists/en/articles/7231422-amazon-music-artist-profiles
- https://intercom.help/amazon-music-for-artists/en/articles/10223779-artist-profile-issues-incorrect-or-missng-content
- https://artists.amazonmusic.com/faqs

### SoundCloud

SoundCloud reconoce que nombres comunes, símbolos, múltiples rightsholders o perfiles eliminados pueden causar mapping incorrecto. Si el contenido se mueve al perfil correcto, **se pierden métricas de reproducción, comentarios y likes** por limitaciones actuales:

- https://help.soundcloud.com/hc/en-us/articles/41068594103195-Why-are-my-tracks-on-the-wrong-profile
- https://help.soundcloud.com/hc/en-us/articles/41070281134235-I-ve-found-an-Auto-Generated-Profile-What-do-I-do

### TikTok

CD Baby documenta que una pista puede faltar, ser silenciada o quedar limitada por restricciones territoriales, conflictos de derechos o decisiones de plataforma; la cadena de monetización y reporting tiene además calendario propio:

- https://support.cdbaby.com/hc/en-us/articles/360038700071-How-TikTok-Monetization-Works

## 3. Distribuidores: patrón de reclamaciones externas

### DistroKid

Better Business Bureau contiene múltiples reclamaciones recientes de 2025-2026 sobre:

- royalties de Spotify supuestamente ausentes o infrarreportadas;
- dashboards que pasan a cero;
- retiradas de catálogo;
- fondos bloqueados;
- acusaciones de artificial streaming;
- tickets cerrados o respuestas genéricas;
- peticiones expresas de auditoría de royalty files sin respuesta concreta.

Fuentes:

- https://www.bbb.org/us/ny/new-york/profile/music-distribution-companies/distrokid-0121-87139284/complaints
- https://www.bbb.org/us/ny/new-york/profile/music-distribution-companies/distrokid-0121-87139284/complaints?page=12
- https://www.bbb.org/us/ny/new-york/profile/music-distribution-companies/distrokid-0121-87139284/complaints?page=1

Estas son alegaciones de clientes. Algunas figuran como resueltas, otras contestadas y otras sin respuesta. No constituyen por sí solas prueba de apropiación de fondos, pero muestran que el patrón de soporte/royalties que estamos investigando **no es aislado**.

### TuneCore

BBB recoge casos recientes sobre holds de retiradas, artificial streaming, royalties retenidas, cierres de cuenta y explicaciones contradictorias sobre catálogo aún activo:

- https://www.bbb.org/us/ny/brooklyn/profile/music-publishing-companies/tunecore-0121-100992/complaints
- https://www.bbb.org/us/ny/brooklyn/profile/music-publishing-companies/tunecore-0121-100992/complaints?page=1
- https://www.bbb.org/us/ny/brooklyn/profile/music-publishing-companies/tunecore-0121-100992/customer-reviews

### CD Baby

BBB muestra reclamaciones recientes por distribución no completada, acceso bloqueado, royalties retenidas, contenido que sigue activo tras cierre y presuntas asignaciones incorrectas de derechos. BBB además marcó un **Pattern of Complaints** y en abril de 2026 solicitó aclaraciones sobre determinadas afirmaciones publicitarias de CD Baby:

- https://www.bbb.org/us/or/portland/profile/music-distribution-companies/cd-baby-1296-37002534/complaints
- https://www.bbb.org/us/or/portland/profile/music-distribution-companies/cd-baby-1296-37002534/complaints?page=2
- https://www.bbb.org/us/or/portland/profile/music-distribution-companies/cd-baby-1296-37002534/customer-reviews?page=1
- https://www.bbb.org/us/or/portland/profile/music-distribution-companies/cd-baby-1296-37002534

### Ditto Music

BBB recoge reclamaciones sobre suspensión por artificial streaming, royalties retenidas y solicitudes de evidencia granular. También existen respuestas de Ditto defendiendo sus decisiones en algunos expedientes:

- https://www.bbb.org/us/tn/nashville/profile/music-distribution-companies/ditto-music-0573-37066042/complaints
- https://www.bbb.org/us/tn/nashville/profile/music-distribution-companies/ditto-music-0573-37066042/customer-reviews

## 4. Fraude, suplantación y subidas no autorizadas

Pitchfork documentó en 2019 cómo impostores y leakers podían subir música ajena o no publicada a Spotify y Apple Music mediante distribuidores de bajo umbral, generando regalías antes de que el contenido fuera detectado. El artículo incluye ejemplos vinculados a artistas de gran tamaño y explica que la ausencia de una base universal de metadata agrava el problema:

- https://pitchfork.com/features/article/how-artist-imposters-and-fake-songs-sneak-onto-streaming-services

Esto prueba que **la clase de ataque existe**. No prueba que sea la causa del expediente Innova_N ni que exista una red concreta detrás de él.

## 5. Evidencia técnica estructural

El trabajo académico `Towards an Open and Scalable Music Metadata Layer` describe un problema basal: múltiples participantes de la cadena crean versiones propias de la metadata, con reentrada manual y sincronización difícil y propensa a errores:

- https://arxiv.org/abs/1911.08278

Esto encaja con lo que reconocen Amazon, Spotify, YouTube, TIDAL y SoundCloud desde sus propias capas.

## 6. Sobre grandes artistas, majors y sesgo de exposición

No se ha encontrado evidencia que permita afirmar que **Bad Bunny**, otro artista concreto o una “mafia” esté recibiendo regalías pertenecientes al expediente analizado. Esa acusación queda fuera de la auditoría mientras no aparezca un identificador, royalty statement, ISRC, payment routing, rights claim o cuenta receptora que lo demuestre.

Sí existe investigación académica sobre **popularity bias** en sistemas de recomendación musical: los algoritmos pueden sobreexponer sistemáticamente a proveedores/artistas populares frente a otros. Eso es un problema diferente de desviar regalías:

- https://arxiv.org/abs/2003.11634

Por tanto:

**sesgo de exposición ≠ apropiación de royalties**  
**dominio comercial ≠ prueba de fraude**

## 7. Matriz causal MAXPROC actualizada

| Hipótesis | Evidencia externa | Estado provisional |
|---|---|---|
| H1 · ciberincidente/pérdida de base de datos | existe como posibilidad técnica, pero sin evidencia pública específica | débil/no demostrada |
| H2 · fragmentación y reconciliación defectuosa de metadata | reconocida por múltiples DSP y literatura técnica | fuerte |
| H3 · error humano/automatización/mapping | reconocida por Spotify, Amazon, SoundCloud, YouTube | fuerte |
| H4 · soporte sin acceso a capa contable/routing | patrón compatible con numerosos testimonios | media; requiere evidencia interna |
| H5 · fraude/suplantación de terceros | casos periodísticos documentados | real como clase; no probado en nuestro caso |
| H6 · estadísticas y royalties en sistemas distintos | reconocido por distribuidores/DSP y por la propia arquitectura de reporting | fuerte |
| H7 · holds antifraude/artificial streaming | reclamaciones repetidas en DistroKid, TuneCore, Ditto, CD Baby | fuerte como fenómeno; legitimidad debe verse caso por caso |
| H8 · concentración/popularity bias | documentada en investigación de recomendadores | real para exposición; no prueba desvío de pagos |

## 8. Qué necesitamos de músicos afectados

Para convertir testimonios en evidencia comparable se pide aportar:

1. distribuidor;
2. DSP;
3. artista y URL de perfil correcto/incorrecto;
4. ISRC y UPC;
5. artist ID / URI antes y después;
6. capturas de Spotify for Artists / Apple / TIDAL / YouTube / Amazon;
7. royalty statement del distribuidor;
8. mes exacto y territorio;
9. takedown/re-delivery/merge si existió;
10. ticket de soporte y respuesta;
11. fecha de resolución;
12. si las métricas o regalías cambiaron tras reparar el mapping.

El objetivo es construir una matriz que permita distinguir:

`ERROR DE IDENTIDAD` → `ERROR DE METADATA` → `ERROR DE CATÁLOGO` → `ERROR DE REPORTING` → `ERROR DE LIQUIDACIÓN` → `FRAUDE DE TERCERO` → `HOLD ANTIFRAUDE`

sin colapsarlos prematuramente en una sola explicación.

---

# EN · English

## Provisional finding

External evidence shows that wrong-artist mapping, duplicate profiles, split catalogues, missing/reappearing releases, metadata inconsistencies, distributor dependency, separate analytics/royalty layers, circular support, withheld-payment complaints and third-party impersonation are **cross-platform phenomena**.

The strongest current structural explanation is fragmented DDEX/metadata and identity reconciliation across distributors and DSPs, combined with human/automated mapping and separate reporting/payment systems. Fraud and unauthorized uploads are documented as a real class of attack, but no evidence currently ties the Innova_N case to a specific artist, major label, criminal group or coordinated diversion scheme.

All links and the Spanish causal matrix above are part of the same open audit. Contributions and contradictory evidence should be added to Open Synthesis #61.
