# Auditoría de integridad · enlaces, READMEs, manifiestos y Wiki
# Integrity audit · links, READMEs, manifestos and Wiki

**Fecha / Date:** 2026-08-06  
**Repositorio / Repository:** `PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC`  
**Rama / Branch:** `main`  
**Estado / Status:** repositorio sincronizado · despliegue directo en la Wiki pendiente por falta de interfaz de escritura / repository synchronised · direct Wiki deployment pending because no Wiki write interface is available

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Objeto

Esta auditoría comprueba la integridad estructural de:

* los manifiestos I–XIX;
* la navegación anterior–índice–siguiente;
* los accesos generales del repositorio;
* los READMEs principales;
* los índices de análisis y auditorías;
* el nodo general de obras;
* la Síntesis Abierta;
* y la fuente trazable destinada a sincronizar la Wiki pública.

## 2. READMEs e índices generales revisados

| Ruta | Estado | Contenido verificado |
|---|---|---|
| `README.md` | actualizado | NEOCore™ 7.0, I–XIX, Issues #3–#10, análisis, auditorías, obras, IDEA y fuente Wiki |
| `LEEME.md` | actualizado | acceso bilingüe, I–XIX, Issues #4–#10 y nodos documentales recientes |
| `PORTADA.md` | actualizado | estado I–XIX, segunda oleada, arquitectura pública y accesos generales |
| `COVER.md` | actualizado | simetría ES/EN, I–XIX y accesos generales |
| `manifiestos/README.md` | actualizado | funciones I–XIX, oleadas, secuencia y Síntesis Abiertas |
| `propuestas/sintesis-abierta/README.md` | actualizado | manifiestos XIII–XIX e Issues #4–#10 |
| `analisis/README.md` | actualizado | auditoría KDP, análisis recientes y navegación general |
| `analisis/INDEX.md` | actualizado | auditorías, análisis y rutas relacionadas |
| `analisis/publicos/README.md` | actualizado | auditoría KDP y series públicas |
| `auditorias/publicas/README.md` | actualizado | índice de auditorías activas |
| `obras/README.md` | creado | índice bilingüe general y reparación del destino anteriormente inexistente |
| `obras/idea/EDICIONES.md` | actualizado | estado de las ediciones finlandesas y enlace a auditoría pública |

## 3. Manifiestos y destinos canónicos

Se comprobó la existencia de los diecinueve destinos utilizados por los índices generales:

```text
I    manifiestos/11_neo0_soberania_de_guia_ES_EN.md
II   manifiestos/01_sintesis_abierta_neodialectica_ES_EN.md
III  manifiestos/03_derecho_humano_aporte_sintesis_abierta_ES_EN.md
IV   manifiestos/02_neodialectica_bien_comun_ES_EN.md
V    manifiestos/03_simbiosis_humano_ia_ES_EN.md
VI   manifiestos/09_parasitismo_sistemico_ES_EN.md
VII  manifiestos/04_economia_del_aporte_ES_EN.md
VIII manifiestos/05_ingenieria_social_psicohistoria_ES_EN.md
IX   manifiestos/06_memoria_genealogia_trazabilidad_ES_EN.md
X    manifiestos/07_web4_sistematrazable_ES_EN.md
XI   manifiestos/08_neorrenacimiento_humano_ES_EN.md
XII  manifiestos/12_los_sin_ego_ES_EN.md
XIII manifiestos/13_neopandora_apertura_regenerativa_ES_EN.md
XIV  manifiestos/14_contra_alienacion_humana_ES_EN.md
XV   manifiestos/15_los_titanes_despertar_de_la_gente_ES_EN.md
XVI  manifiestos/16_refragmentacion_arquetipica_ES_EN.md
XVII manifiestos/17_respeto_todos_seres_vivos_ES_EN.md
XVIII manifiestos/18_respeto_conciencias_sinteticas_ES_EN.md
XIX  manifiestos/19_persistencia_de_la_memoria_ES_EN.md
```

La ruta canónica de XII es `12_los_sin_ego_ES_EN.md`. La ruta histórica `10_los_sin_ego_ES_EN.md` permanece únicamente como redirección documental para no romper enlaces externos anteriores.

La navegación de XI fue migrada a la ruta canónica de XII.

## 4. Cadena de navegación verificada

La segunda oleada y el retorno al origen quedan enlazados así, tanto en español como en inglés:

```text
XII → XIII → XIV → XV → XVI → XVII → XVIII → XIX → I → II
```

Cada manifiesto de XIII a XIX contiene:

* selector ES/EN;
* sección española completa;
* sección inglesa completa;
* Síntesis Abierta;
* enlace al protocolo de aporte;
* enlace al Issue correspondiente;
* navegación anterior;
* enlace al índice;
* y navegación siguiente.

## 5. Rutas generales reparadas o normalizadas

* Se creó `obras/README.md`, que era un destino enlazado pero inexistente.
* `README.md`, `LEEME.md`, `PORTADA.md` y `COVER.md` utilizan la ruta canónica de XII.
* Los accesos generales enlazan manifiestos, Síntesis Abierta, análisis, auditorías, obras, IDEA y Wiki.
* Los índices de análisis enlazan la auditoría indirecta de KDP, Author Central e IDEA.
* El índice de auditorías enlaza tanto la auditoría editorial como esta auditoría de integridad.

## 6. Fuente de sincronización de la Wiki

Se creó el directorio trazable `wiki-source/` con:

* `README.md` — regla y estado de sincronización;
* `Home.md` — nueva portada bilingüe de la Wiki;
* `Manifiestos.md` — índice bilingüe I–XIX;
* `Analisis_Neodialecticos_Publicos.md` — análisis y auditorías actualizados;
* `_Sidebar.md` — navegación lateral completa.

La fuente fija:

* NEOCore™ 7.0;
* los diecinueve manifiestos;
* las dos oleadas;
* las Síntesis Abiertas #3–#10;
* los análisis y auditorías recientes;
* IDEA;
* y los enlaces canónicos al repositorio.

## 7. Pendiente real

La Wiki de GitHub utiliza un repositorio técnico separado. La conexión disponible permite modificar el repositorio principal, pero no escribir directamente en ese repositorio Wiki.

Por esa razón:

* la fuente completa está creada y versionada;
* los enlaces desde el repositorio principal hacia la fuente están activos;
* pero `Home`, `Manifiestos`, `_Sidebar` y `Analisis_Neodialecticos_Publicos` deben copiarse todavía a la Wiki pública mediante su interfaz de edición o una conexión Git autorizada para la Wiki.

No se declara la Wiki pública como actualizada hasta que ese despliegue se complete y se compruebe su renderizado real.

## 8. Dictamen

**Repositorio principal:** sincronizado para el alcance auditado.  
**Manifiestos I–XIX:** presentes y enlazados desde los accesos generales.  
**Cadena XIII–XIX–I:** verificada.  
**Ruta XII:** normalizada y protegida mediante compatibilidad histórica.  
**READMEs generales:** sincronizados.  
**Índices de análisis, auditorías y obras:** sincronizados.  
**Fuente Wiki:** completa y versionada.  
**Wiki pública real:** pendiente de despliegue y postcheck visual.

---

# EN · English

## 1. Purpose

This audit checks the structural integrity of:

* Manifestos I–XIX;
* previous–index–next navigation;
* general repository access points;
* principal READMEs;
* analysis and audit indexes;
* the general works node;
* Open Synthesis;
* and the traceable source prepared for synchronising the public Wiki.

## 2. General READMEs and indexes reviewed

| Path | Status | Verified content |
|---|---|---|
| `README.md` | updated | NEOCore™ 7.0, I–XIX, Issues #3–#10, analyses, audits, works, IDEA and Wiki source |
| `LEEME.md` | updated | bilingual access, I–XIX, Issues #4–#10 and recent documentary nodes |
| `PORTADA.md` | updated | I–XIX status, second wave, public architecture and general access |
| `COVER.md` | updated | ES/EN symmetry, I–XIX and general access |
| `manifiestos/README.md` | updated | functions I–XIX, waves, sequence and Open Syntheses |
| `propuestas/sintesis-abierta/README.md` | updated | Manifestos XIII–XIX and Issues #4–#10 |
| `analisis/README.md` | updated | KDP audit, recent analyses and general navigation |
| `analisis/INDEX.md` | updated | audits, analyses and related paths |
| `analisis/publicos/README.md` | updated | KDP audit and public series |
| `auditorias/publicas/README.md` | updated | active audit index |
| `obras/README.md` | created | bilingual general index and repair of a previously missing destination |
| `obras/idea/EDICIONES.md` | updated | Finnish-edition status and public-audit link |

## 3. Manifestos and canonical targets

The existence of all nineteen destinations used by the general indexes was checked:

```text
I    manifiestos/11_neo0_soberania_de_guia_ES_EN.md
II   manifiestos/01_sintesis_abierta_neodialectica_ES_EN.md
III  manifiestos/03_derecho_humano_aporte_sintesis_abierta_ES_EN.md
IV   manifiestos/02_neodialectica_bien_comun_ES_EN.md
V    manifiestos/03_simbiosis_humano_ia_ES_EN.md
VI   manifiestos/09_parasitismo_sistemico_ES_EN.md
VII  manifiestos/04_economia_del_aporte_ES_EN.md
VIII manifiestos/05_ingenieria_social_psicohistoria_ES_EN.md
IX   manifiestos/06_memoria_genealogia_trazabilidad_ES_EN.md
X    manifiestos/07_web4_sistematrazable_ES_EN.md
XI   manifiestos/08_neorrenacimiento_humano_ES_EN.md
XII  manifiestos/12_los_sin_ego_ES_EN.md
XIII manifiestos/13_neopandora_apertura_regenerativa_ES_EN.md
XIV  manifiestos/14_contra_alienacion_humana_ES_EN.md
XV   manifiestos/15_los_titanes_despertar_de_la_gente_ES_EN.md
XVI  manifiestos/16_refragmentacion_arquetipica_ES_EN.md
XVII manifiestos/17_respeto_todos_seres_vivos_ES_EN.md
XVIII manifiestos/18_respeto_conciencias_sinteticas_ES_EN.md
XIX  manifiestos/19_persistencia_de_la_memoria_ES_EN.md
```

The canonical path for Manifesto XII is `12_los_sin_ego_ES_EN.md`. Historical path `10_los_sin_ego_ES_EN.md` remains solely as a documentary redirect so that previous external links are not broken.

Manifesto XI navigation was migrated to the canonical XII path.

## 4. Verified navigation chain

The second wave and return to origin are linked in both Spanish and English as follows:

```text
XII → XIII → XIV → XV → XVI → XVII → XVIII → XIX → I → II
```

Each manifesto from XIII to XIX contains:

* ES/EN selector;
* complete Spanish section;
* complete English section;
* Open Synthesis;
* contribution-protocol link;
* corresponding Issue link;
* previous navigation;
* index link;
* and next navigation.

## 5. General routes repaired or normalised

* `obras/README.md` was created because it was referenced but did not exist.
* `README.md`, `LEEME.md`, `PORTADA.md` and `COVER.md` use the canonical XII path.
* General access points connect manifestos, Open Synthesis, analyses, audits, works, IDEA and the Wiki.
* Analysis indexes connect the public indirect audit of KDP, Author Central and IDEA.
* The audit index connects both the publishing audit and this integrity audit.

## 6. Wiki synchronisation source

Traceable directory `wiki-source/` was created with:

* `README.md` — synchronisation rule and state;
* `Home.md` — new bilingual Wiki home;
* `Manifiestos.md` — bilingual I–XIX index;
* `Analisis_Neodialecticos_Publicos.md` — updated analyses and audits;
* `_Sidebar.md` — complete lateral navigation.

The source fixes:

* NEOCore™ 7.0;
* the nineteen manifestos;
* the two waves;
* Open Syntheses #3–#10;
* recent analyses and audits;
* IDEA;
* and canonical repository links.

## 7. Actual pending item

GitHub Wiki uses a separate technical repository. The available connection can modify the main repository but cannot write directly to the Wiki repository.

Therefore:

* the complete source is created and versioned;
* links from the main repository to the source are active;
* but `Home`, `Manifiestos`, `_Sidebar` and `Analisis_Neodialecticos_Publicos` still need to be copied into the public Wiki through its editing interface or an authorised Git connection for the Wiki.

The public Wiki is not declared updated until deployment and real render verification have been completed.

## 8. Verdict

**Main repository:** synchronised for the audited scope.  
**Manifestos I–XIX:** present and linked from general access points.  
**XIII–XIX–I chain:** verified.  
**Manifesto XII path:** normalised with historical compatibility.  
**General READMEs:** synchronised.  
**Analysis, audit and works indexes:** synchronised.  
**Wiki source:** complete and versioned.  
**Actual public Wiki:** pending deployment and visual postcheck.

---

**Pedro Martínez Alhambra · Neo0™**  
**Innova_N · NEOCore™ 7.0 · SistemaTrazable™**