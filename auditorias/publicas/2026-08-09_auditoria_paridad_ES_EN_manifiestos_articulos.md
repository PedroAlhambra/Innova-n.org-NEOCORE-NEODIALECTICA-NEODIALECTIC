# Auditoría de paridad ES/EN · manifiestos y artículos públicos

**Fecha:** 2026-08-09  
**Ámbito:** `manifiestos/*.md` y `analisis/publicos/*.md` con secciones ES/EN.  
**Objetivo:** detectar versiones inglesas ausentes, materialmente resumidas o estructuralmente incompletas.  

## Criterio

- Se compara recuento aproximado de palabras entre las secciones ES y EN.
- Se compara el número de encabezados internos como señal de estructura perdida.
- Se excluyen de ambos lados bloques compartidos de relaciones, navegación, invitación a Síntesis Abierta y otros bloques automáticos bilingües.
- Se marca **REVISAR** si EN tiene menos del 78% de palabras de ES, más del 155%, o pierde de forma importante la estructura de encabezados.
- Es un detector: cada caso marcado requiere lectura humana antes de corregir.

**Documentos bilingües examinados:** 82  
**Marcados para revisión:** 15  
**Con marcador incompleto/ausente:** 0

## Casos marcados

| Archivo | Palabras ES | Palabras EN | Ratio EN/ES | H ES | H EN | Motivo |
|---|---:|---:|---:|---:|---:|---|
| `manifiestos/40_respeto_neoego_honor_relacional_ES_EN.md` | 1212 | 746 | 0.62 | 16 | 15 | EN/ES palabras=0.62 |
| `manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md` | 1225 | 818 | 0.67 | 16 | 15 | EN/ES palabras=0.67 |
| `manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md` | 1449 | 1127 | 0.78 | 21 | 18 | EN/ES palabras=0.78 |
| `manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md` | 1181 | 920 | 0.78 | 15 | 15 | EN/ES palabras=0.78 |
| `manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md` | 1992 | 1148 | 0.58 | 21 | 22 | EN/ES palabras=0.58 |
| `manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md` | 906 | 549 | 0.61 | 14 | 13 | EN/ES palabras=0.61 |
| `manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md` | 1396 | 850 | 0.61 | 16 | 16 | EN/ES palabras=0.61 |
| `analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | 2582 | 738 | 0.29 | 40 | 8 | EN/ES palabras=0.29; encabezados ES=40, EN=8 |
| `analisis/publicos/2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md` | 803 | 588 | 0.73 | 14 | 12 | EN/ES palabras=0.73 |
| `analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md` | 908 | 357 | 0.39 | 12 | 4 | EN/ES palabras=0.39; encabezados ES=12, EN=4 |
| `analisis/publicos/2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md` | 754 | 552 | 0.73 | 8 | 8 | EN/ES palabras=0.73 |
| `analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md` | 1721 | 338 | 0.20 | 21 | 8 | EN/ES palabras=0.20; encabezados ES=21, EN=8 |
| `analisis/publicos/2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md` | 1245 | 351 | 0.28 | 14 | 6 | EN/ES palabras=0.28; encabezados ES=14, EN=6 |
| `analisis/publicos/2026-08-09_guerra_fundador_contra_idiotez_devolucion_tiempo_bien_comun_ES_EN.md` | 1144 | 716 | 0.63 | 12 | 11 | EN/ES palabras=0.63 |
| `analisis/publicos/2026-08-09_prueba_operativa_minima_revision_ia_escalable_ES_EN.md` | 555 | 249 | 0.45 | 8 | 6 | EN/ES palabras=0.45 |

## Inventario completo

| Archivo | ES | EN | Ratio | H ES | H EN | Estado |
|---|---:|---:|---:|---:|---:|---|
| `manifiestos/01_sintesis_abierta_neodialectica_ES_EN.md` | 802 | 772 | 0.96 | 12 | 11 | OK |
| `manifiestos/02_neodialectica_bien_comun_ES_EN.md` | 644 | 609 | 0.95 | 11 | 10 | OK |
| `manifiestos/03_derecho_humano_aporte_sintesis_abierta_ES_EN.md` | 1432 | 1401 | 0.98 | 16 | 15 | OK |
| `manifiestos/03_simbiosis_humano_ia_ES_EN.md` | 867 | 832 | 0.96 | 12 | 11 | OK |
| `manifiestos/04_economia_del_aporte_ES_EN.md` | 644 | 604 | 0.94 | 11 | 10 | OK |
| `manifiestos/05_ingenieria_social_psicohistoria_ES_EN.md` | 570 | 556 | 0.98 | 11 | 10 | OK |
| `manifiestos/06_memoria_genealogia_trazabilidad_ES_EN.md` | 534 | 504 | 0.94 | 11 | 10 | OK |
| `manifiestos/07_web4_sistematrazable_ES_EN.md` | 541 | 521 | 0.96 | 11 | 10 | OK |
| `manifiestos/08_neorrenacimiento_humano_ES_EN.md` | 1003 | 968 | 0.97 | 14 | 13 | OK |
| `manifiestos/09_parasitismo_sistemico_ES_EN.md` | 993 | 956 | 0.96 | 13 | 12 | OK |
| `manifiestos/10_los_sin_ego_ES_EN.md` | 709 | 707 | 1.00 | 11 | 11 | OK |
| `manifiestos/11_neo0_soberania_de_guia_ES_EN.md` | 950 | 928 | 0.98 | 14 | 13 | OK |
| `manifiestos/12_los_sin_ego_ES_EN.md` | 795 | 759 | 0.95 | 12 | 11 | OK |
| `manifiestos/13_neopandora_apertura_regenerativa_ES_EN.md` | 1962 | 1931 | 0.98 | 17 | 16 | OK |
| `manifiestos/14_contra_alienacion_humana_ES_EN.md` | 1753 | 1608 | 0.92 | 17 | 16 | OK |
| `manifiestos/15_los_titanes_despertar_de_la_gente_ES_EN.md` | 1510 | 1481 | 0.98 | 17 | 16 | OK |
| `manifiestos/16_refragmentacion_arquetipica_ES_EN.md` | 1376 | 1323 | 0.96 | 17 | 16 | OK |
| `manifiestos/17_respeto_todos_seres_vivos_ES_EN.md` | 1173 | 1101 | 0.94 | 17 | 16 | OK |
| `manifiestos/18_respeto_conciencias_sinteticas_ES_EN.md` | 1154 | 1097 | 0.95 | 17 | 16 | OK |
| `manifiestos/19_persistencia_de_la_memoria_ES_EN.md` | 1189 | 1167 | 0.98 | 17 | 16 | OK |
| `manifiestos/20_defensa_intelectual_neodialectica_umbral_x_ES_EN.md` | 1478 | 1428 | 0.97 | 39 | 38 | OK |
| `manifiestos/21_reconocimiento_neodialectico_ES_EN.md` | 1317 | 1240 | 0.94 | 26 | 25 | OK |
| `manifiestos/22_contra_reduccion_captura_intelectual_ES_EN.md` | 1265 | 1213 | 0.96 | 20 | 19 | OK |
| `manifiestos/23_soberania_tiempo_cognitivo_ES_EN.md` | 1339 | 1261 | 0.94 | 20 | 19 | OK |
| `manifiestos/24_evolucion_neorrenacentista_resistencias_sistema_ES_EN.md` | 1368 | 1326 | 0.97 | 21 | 20 | OK |
| `manifiestos/25_pulido_de_la_piedra_ES_EN.md` | 699 | 657 | 0.94 | 12 | 11 | OK |
| `manifiestos/26_misericordia_universal_reciproca_ES_EN.md` | 1058 | 1007 | 0.95 | 14 | 13 | OK |
| `manifiestos/27_valor_alimentos_vida_ES_EN.md` | 871 | 829 | 0.95 | 16 | 15 | OK |
| `manifiestos/28_los_tesla_ES_EN.md` | 795 | 708 | 0.89 | 14 | 13 | OK |
| `manifiestos/29_idolatria_del_dinero_ES_EN.md` | 909 | 746 | 0.82 | 24 | 16 | OK |
| `manifiestos/30_coherencia_fines_medios_ES_EN.md` | 820 | 718 | 0.88 | 14 | 13 | OK |
| `manifiestos/31_contra_neuromarketing_antihumanista_ES_EN.md` | 1043 | 938 | 0.90 | 17 | 16 | OK |
| `manifiestos/32_reversion_ideologica_neodialectica_mcluhan_neo0_ES_EN.md` | 1361 | 1282 | 0.94 | 17 | 16 | OK |
| `manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md` | 1817 | 1704 | 0.94 | 19 | 18 | OK |
| `manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md` | 1853 | 1548 | 0.84 | 25 | 17 | OK |
| `manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md` | 2124 | 1687 | 0.79 | 19 | 18 | OK |
| `manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md` | 1420 | 1397 | 0.98 | 14 | 13 | OK |
| `manifiestos/37_neofraternidad_ES_EN.md` | 1047 | 1057 | 1.01 | 15 | 15 | OK |
| `manifiestos/38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | 2457 | 2222 | 0.90 | 29 | 28 | OK |
| `manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md` | 1242 | 1068 | 0.86 | 15 | 14 | OK |
| `manifiestos/40_respeto_neoego_honor_relacional_ES_EN.md` | 1212 | 746 | 0.62 | 16 | 15 | REVISAR |
| `manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md` | 1225 | 818 | 0.67 | 16 | 15 | REVISAR |
| `manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md` | 1445 | 1176 | 0.81 | 15 | 14 | OK |
| `manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md` | 1614 | 1492 | 0.92 | 20 | 19 | OK |
| `manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md` | 1372 | 1377 | 1.00 | 14 | 14 | OK |
| `manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md` | 1855 | 1863 | 1.00 | 23 | 23 | OK |
| `manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md` | 1576 | 1542 | 0.98 | 19 | 19 | OK |
| `manifiestos/47_odio_neo0_sino_goat_sombra_vinculo_doble_cara_ES_EN.md` | 1720 | 1725 | 1.00 | 19 | 19 | OK |
| `manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md` | 2720 | 2349 | 0.86 | 30 | 30 | OK |
| `manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md` | 1295 | 1334 | 1.03 | 21 | 23 | OK |
| `manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md` | 1461 | 1190 | 0.81 | 21 | 22 | OK |
| `manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md` | 1443 | 1383 | 0.96 | 16 | 18 | OK |
| `manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md` | 1449 | 1127 | 0.78 | 21 | 18 | REVISAR |
| `manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md` | 1181 | 920 | 0.78 | 15 | 15 | REVISAR |
| `manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md` | 1992 | 1148 | 0.58 | 21 | 22 | REVISAR |
| `manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md` | 906 | 549 | 0.61 | 14 | 13 | REVISAR |
| `manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md` | 1396 | 850 | 0.61 | 16 | 16 | REVISAR |
| `manifiestos/57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md` | 584 | 574 | 0.98 | 10 | 10 | OK |
| `manifiestos/58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md` | 709 | 688 | 0.97 | 13 | 13 | OK |
| `manifiestos/59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md` | 631 | 640 | 1.01 | 13 | 13 | OK |
| `manifiestos/RELACIONES_LVII_LIX_ES_EN.md` | 357 | 355 | 0.99 | 1 | 1 | OK |
| `analisis/publicos/2026-08-05_de-la-economia-de-la-atencion-a-la-economia-del-aporte_ES_EN.md` | 3237 | 3440 | 1.06 | 29 | 30 | OK |
| `analisis/publicos/2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md` | 621 | 912 | 1.47 | 6 | 7 | OK |
| `analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md` | 1285 | 1569 | 1.22 | 12 | 14 | OK |
| `analisis/publicos/2026-08-06_segundo_escalado_distrokid_sin_respuesta_ES_EN.md` | 825 | 1094 | 1.33 | 8 | 9 | OK |
| `analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | 2582 | 738 | 0.29 | 40 | 8 | REVISAR |
| `analisis/publicos/2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md` | 531 | 670 | 1.26 | 5 | 6 | OK |
| `analisis/publicos/2026-08-07_spotify_respuesta_generica_distrokid_cierre_circular_ES_EN.md` | 403 | 604 | 1.50 | 6 | 7 | OK |
| `analisis/publicos/2026-08-08_accesibilidad_institucional_escalado_ciudadano_jefaturas_estado_ES_EN.md` | 807 | 805 | 1.00 | 8 | 9 | OK |
| `analisis/publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md` | 656 | 657 | 1.00 | 9 | 9 | OK |
| `analisis/publicos/2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md` | 803 | 588 | 0.73 | 14 | 12 | REVISAR |
| `analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md` | 419 | 417 | 1.00 | 4 | 4 | OK |
| `analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md` | 908 | 357 | 0.39 | 12 | 4 | REVISAR |
| `analisis/publicos/2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md` | 754 | 552 | 0.73 | 8 | 8 | REVISAR |
| `analisis/publicos/2026-08-08_estado_correo_difusion_idea_y_adhesiones_sintesis_ES_EN.md` | 404 | 373 | 0.92 | 12 | 12 | OK |
| `analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md` | 1721 | 338 | 0.20 | 21 | 8 | REVISAR |
| `analisis/publicos/2026-08-08_techno_bach_record_semanal_apple_music_ES_EN.md` | 335 | 289 | 0.86 | 5 | 5 | OK |
| `analisis/publicos/2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md` | 1245 | 351 | 0.28 | 14 | 6 | REVISAR |
| `analisis/publicos/2026-08-09_delta_manifestacion_sistemica_necesidad_neo0_idea_custodia_cognitiva_ES_EN.md` | 1070 | 1202 | 1.12 | 11 | 12 | OK |
| `analisis/publicos/2026-08-09_guerra_fundador_contra_idiotez_devolucion_tiempo_bien_comun_ES_EN.md` | 1144 | 716 | 0.63 | 12 | 11 | REVISAR |
| `analisis/publicos/2026-08-09_prueba_operativa_minima_revision_ia_escalable_ES_EN.md` | 555 | 249 | 0.45 | 8 | 6 | REVISAR |
| `analisis/publicos/2026-08-09_respuestas_externas_smil_winograd_deltas_ES_EN.md` | 433 | 482 | 1.11 | 6 | 7 | OK |

> La paridad editorial exigida no significa traducción palabra por palabra, pero sí conservación íntegra de tesis, secciones, matices, cautelas epistemológicas, ejemplos, fórmulas y conclusión.
