# Auditoría de paridad ES/EN · manifiestos y artículos públicos

**Fecha:** 2026-08-10  
**Ámbito:** `manifiestos/*.md` y `analisis/publicos/*.md` con secciones ES/EN.  
**Objetivo:** detectar traducciones ausentes o materialmente recortadas sin confundir automáticamente diferencias legítimas de maquetación con pérdida semántica.  

## Criterio

- Se compara volumen global, encabezados y secuencia de secciones principales H2 numeradas.
- Se compara sección por sección el volumen material y la conservación de fórmulas/bloques.
- Las diferencias de listas o citas se marcan como **ADVERTENCIA estructural** si el volumen de la sección sigue siendo razonablemente equivalente; pasan a **REVISAR** cuando coinciden con compresión material.
- Los bloques generados de navegación y referencias cruzadas no se contabilizan como traducción.
- `REVISAR` bloquea la publicación automática de manifiestos; `ADVERTENCIA` exige inspección editorial pero no demuestra por sí sola recorte.

**Documentos bilingües examinados:** 93  
**Recortes/materialmente asimétricos para revisión:** 17  
**Advertencias estructurales sin prueba suficiente de recorte:** 18  
**Con marcador incompleto/ausente:** 0

## Casos marcados

| Archivo | Palabras ES | Palabras EN | Ratio EN/ES | H ES | H EN | Motivo |
|---|---:|---:|---:|---:|---:|---|
| `manifiestos/28_los_tesla_ES_EN.md` | 795 | 708 | 0.89 | 14 | 13 | sección II EN/ES=0.46 (41/90 palabras); sección II listas ES=8, EN=0; sección V fórmulas/bloques ES=1, EN=0 |
| `manifiestos/29_idolatria_del_dinero_ES_EN.md` | 909 | 746 | 0.82 | 24 | 16 | sección III EN/ES=0.31 (49/160 palabras) |
| `manifiestos/30_coherencia_fines_medios_ES_EN.md` | 820 | 718 | 0.88 | 14 | 13 | sección III listas ES=9, EN=0 |
| `manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md` | 1853 | 1548 | 0.84 | 25 | 17 | sección II listas ES=17, EN=5; sección III fórmulas/bloques ES=1, EN=0; sección IV fórmulas/bloques ES=1, EN=0; sección VII EN/ES=0.52 (66/128 palabras) |
| `manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md` | 2124 | 1687 | 0.79 | 19 | 18 | sección II listas ES=13, EN=0; sección III listas ES=9, EN=0; sección III fórmulas/bloques ES=1, EN=0; sección V fórmulas/bloques ES=2, EN=1; sección VI listas ES=10, EN=0; sección VII listas ES=9, EN=0; sección IX EN/ES=0.51 (53/104 palabras); sección IX listas ES=14, EN=4 |
| `manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md` | 1242 | 1068 | 0.86 | 15 | 14 | sección II fórmulas/bloques ES=1, EN=0; sección III fórmulas/bloques ES=2, EN=1; sección IV EN/ES=0.58 (61/105 palabras); sección IV listas ES=8, EN=0; sección V fórmulas/bloques ES=1, EN=0; sección VII fórmulas/bloques ES=1, EN=0; sección VIII EN/ES=0.64 (61/95 palabras); sección VIII listas ES=13, EN=0; sección X listas ES=5, EN=0; sección X fórmulas/bloques ES=1, EN=0; sección XIII EN/ES=0.48 (48/101 palabras); sección XIII listas ES=11, EN=3 |
| `manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md` | 1445 | 1176 | 0.81 | 15 | 14 | sección III listas ES=8, EN=0; sección IV listas ES=9, EN=0; sección VI EN/ES=0.54 (50/93 palabras); sección VI listas ES=14, EN=0; sección VIII fórmulas/bloques ES=2, EN=1; sección IX fórmulas/bloques ES=1, EN=0; sección XIII EN/ES=0.57 (73/127 palabras); sección XIII listas ES=16, EN=3 |
| `manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md` | 1614 | 1492 | 0.92 | 20 | 19 | sección XV listas ES=15, EN=3 |
| `manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md` | 2720 | 2349 | 0.86 | 30 | 30 | sección IV EN/ES=0.63 (86/136 palabras) |
| `manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md` | 1295 | 1334 | 1.03 | 21 | 23 | sección IV listas ES=15, EN=0; sección V fórmulas/bloques ES=1, EN=0; sección X fórmulas/bloques ES=1, EN=0; sección XIX EN/ES=2.30 (322/140 palabras); sección XIX listas ES=5, EN=16 |
| `manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md` | 1461 | 1190 | 0.81 | 21 | 22 | sección I listas ES=7, EN=0; sección II fórmulas/bloques ES=1, EN=0; sección V listas ES=11, EN=0; sección VI fórmulas/bloques ES=1, EN=0 |
| `manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md` | 1443 | 1383 | 0.96 | 16 | 18 | sección II fórmulas/bloques ES=1, EN=0; sección III fórmulas/bloques ES=1, EN=0; sección VI listas ES=8, EN=0; sección IX fórmulas/bloques ES=1, EN=0 |
| `manifiestos/57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md` | 584 | 656 | 1.12 | 10 | 11 | sección VIII EN/ES=2.49 (137/55 palabras) |
| `manifiestos/58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md` | 709 | 770 | 1.09 | 13 | 14 | sección XI EN/ES=2.29 (144/63 palabras) |
| `manifiestos/59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md` | 631 | 730 | 1.16 | 13 | 14 | sección XI EN/ES=2.56 (146/57 palabras) |
| `manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md` | 1539 | 1524 | 0.99 | 15 | 16 | sección XIV EN/ES=1.82 (167/92 palabras) |
| `manifiestos/61_contra_reduccionismo_matematico_custodia_experimental_multiescalar_ES_EN.md` | 1067 | 1072 | 1.00 | 12 | 14 | sección 12 EN/ES=2.85 (148/52 palabras) |

## Advertencias estructurales

| Archivo | Estado | Advertencia |
|---|---|---|
| `manifiestos/25_pulido_de_la_piedra_ES_EN.md` | ADVERTENCIA | sección VII listas ES=8, EN=0 |
| `manifiestos/27_valor_alimentos_vida_ES_EN.md` | ADVERTENCIA | sección IX listas ES=8, EN=2 |
| `manifiestos/31_contra_neuromarketing_antihumanista_ES_EN.md` | ADVERTENCIA | sección I listas ES=11, EN=3; sección II listas ES=6, EN=0; sección III listas ES=11, EN=0; sección IV listas ES=10, EN=0; sección VI listas ES=7, EN=0; sección VIII listas ES=7, EN=0; sección IX listas ES=13, EN=0; sección XI listas ES=10, EN=0; sección XII listas ES=8, EN=0 |
| `manifiestos/32_reversion_ideologica_neodialectica_mcluhan_neo0_ES_EN.md` | ADVERTENCIA | sección II listas ES=11, EN=3; sección III listas ES=13, EN=5; sección IV listas ES=8, EN=0; sección V listas ES=5, EN=0; sección VI listas ES=7, EN=0; sección VIII listas ES=15, EN=3; sección XI listas ES=13, EN=0; sección XII listas ES=11, EN=1 |
| `manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md` | ADVERTENCIA | sección V listas ES=9, EN=0; sección VI listas ES=7, EN=0; sección VII listas ES=9, EN=0; sección XII listas ES=15, EN=5 |
| `manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md` | ADVERTENCIA | sección VII listas ES=14, EN=4 |
| `manifiestos/38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | ADVERTENCIA | sección III listas ES=14, EN=0; sección IV listas ES=11, EN=0; sección V listas ES=17, EN=3; sección VI listas ES=8, EN=0; sección IX listas ES=11, EN=0; sección X listas ES=16, EN=0; sección XII listas ES=12, EN=0; sección XIII listas ES=12, EN=0; sección XIV listas ES=8, EN=0; sección XV listas ES=9, EN=0; sección XVI listas ES=7, EN=0; sección XVIII listas ES=11, EN=0; sección XIX listas ES=5, EN=0; sección XX listas ES=6, EN=0; sección XXII listas ES=8, EN=0; sección XXIV listas ES=17, EN=0; sección XXV listas ES=14, EN=0 |
| `manifiestos/40_respeto_neoego_honor_relacional_ES_EN.md` | ADVERTENCIA | sección V listas ES=5, EN=0; sección VIII listas ES=5, EN=0; sección X listas ES=7, EN=0; sección XI listas ES=8, EN=0 |
| `manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md` | ADVERTENCIA | sección II listas ES=10, EN=0; sección VI listas ES=6, EN=0; sección VII listas ES=9, EN=0; sección XI listas ES=7, EN=0 |
| `manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md` | ADVERTENCIA | sección XII listas ES=15, EN=3 |
| `manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md` | ADVERTENCIA | sección I listas ES=17, EN=0; sección XII listas ES=10, EN=0; sección XVI listas ES=17, EN=3 |
| `manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md` | ADVERTENCIA | sección I listas ES=12, EN=0; sección IV listas ES=7, EN=0; sección XIV listas ES=8, EN=0; sección XVII listas ES=15, EN=3 |
| `manifiestos/47_odio_neo0_sino_goat_sombra_vinculo_doble_cara_ES_EN.md` | ADVERTENCIA | sección V listas ES=12, EN=0; sección IX listas ES=15, EN=0; sección XVII listas ES=15, EN=3 |
| `manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md` | ADVERTENCIA | sección III listas ES=12, EN=0; sección IV listas ES=11, EN=0; sección V listas ES=8, EN=0; sección VII listas ES=8, EN=0; sección X listas ES=8, EN=0; sección XI listas ES=14, EN=0; sección XII listas ES=8, EN=0 |
| `manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md` | ADVERTENCIA | sección V listas ES=8, EN=0; sección VIII listas ES=9, EN=0; sección IX listas ES=9, EN=0 |
| `manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md` | ADVERTENCIA | sección II listas ES=8, EN=0; sección IV listas ES=20, EN=0; sección VIII listas ES=11, EN=0; sección XIII listas ES=12, EN=0; sección XIV listas ES=9, EN=0; sección XVI listas ES=11, EN=0; sección XVII listas ES=10, EN=0; sección XIX listas ES=9, EN=0 |
| `manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md` | ADVERTENCIA | sección V listas ES=10, EN=0; sección VI listas ES=11, EN=4; sección VIII listas ES=7, EN=0; sección X listas ES=10, EN=0 |
| `manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md` | ADVERTENCIA | sección II listas ES=10, EN=0; sección IV listas ES=9, EN=0; sección IX listas ES=10, EN=0; sección XI listas ES=8, EN=0 |

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
| `manifiestos/25_pulido_de_la_piedra_ES_EN.md` | 699 | 657 | 0.94 | 12 | 11 | ADVERTENCIA |
| `manifiestos/26_misericordia_universal_reciproca_ES_EN.md` | 1058 | 1007 | 0.95 | 14 | 13 | OK |
| `manifiestos/27_valor_alimentos_vida_ES_EN.md` | 871 | 829 | 0.95 | 16 | 15 | ADVERTENCIA |
| `manifiestos/28_los_tesla_ES_EN.md` | 795 | 708 | 0.89 | 14 | 13 | REVISAR |
| `manifiestos/29_idolatria_del_dinero_ES_EN.md` | 909 | 746 | 0.82 | 24 | 16 | REVISAR |
| `manifiestos/30_coherencia_fines_medios_ES_EN.md` | 820 | 718 | 0.88 | 14 | 13 | REVISAR |
| `manifiestos/31_contra_neuromarketing_antihumanista_ES_EN.md` | 1043 | 938 | 0.90 | 17 | 16 | ADVERTENCIA |
| `manifiestos/32_reversion_ideologica_neodialectica_mcluhan_neo0_ES_EN.md` | 1361 | 1282 | 0.94 | 17 | 16 | ADVERTENCIA |
| `manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md` | 1817 | 1704 | 0.94 | 19 | 18 | ADVERTENCIA |
| `manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md` | 1853 | 1548 | 0.84 | 25 | 17 | REVISAR |
| `manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md` | 2124 | 1687 | 0.79 | 19 | 18 | REVISAR |
| `manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md` | 1963 | 1900 | 0.97 | 18 | 17 | ADVERTENCIA |
| `manifiestos/37_neofraternidad_ES_EN.md` | 1047 | 1057 | 1.01 | 15 | 15 | OK |
| `manifiestos/38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | 2457 | 2222 | 0.90 | 29 | 28 | ADVERTENCIA |
| `manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md` | 1242 | 1068 | 0.86 | 15 | 14 | REVISAR |
| `manifiestos/40_respeto_neoego_honor_relacional_ES_EN.md` | 1212 | 1201 | 0.99 | 16 | 16 | ADVERTENCIA |
| `manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md` | 1225 | 1187 | 0.97 | 16 | 16 | ADVERTENCIA |
| `manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md` | 1445 | 1176 | 0.81 | 15 | 14 | REVISAR |
| `manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md` | 1614 | 1492 | 0.92 | 20 | 19 | REVISAR |
| `manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md` | 1372 | 1377 | 1.00 | 14 | 14 | ADVERTENCIA |
| `manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md` | 1855 | 1863 | 1.00 | 23 | 23 | ADVERTENCIA |
| `manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md` | 1576 | 1542 | 0.98 | 19 | 19 | ADVERTENCIA |
| `manifiestos/47_odio_neo0_sino_goat_sombra_vinculo_doble_cara_ES_EN.md` | 1720 | 1725 | 1.00 | 19 | 19 | ADVERTENCIA |
| `manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md` | 2720 | 2349 | 0.86 | 30 | 30 | REVISAR |
| `manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md` | 1295 | 1334 | 1.03 | 21 | 23 | REVISAR |
| `manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md` | 1461 | 1190 | 0.81 | 21 | 22 | REVISAR |
| `manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md` | 1443 | 1383 | 0.96 | 16 | 18 | REVISAR |
| `manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md` | 1449 | 1474 | 1.02 | 21 | 22 | ADVERTENCIA |
| `manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md` | 1181 | 1224 | 1.04 | 15 | 16 | ADVERTENCIA |
| `manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md` | 1992 | 1982 | 0.99 | 21 | 22 | ADVERTENCIA |
| `manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md` | 906 | 926 | 1.02 | 14 | 14 | ADVERTENCIA |
| `manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md` | 1396 | 1356 | 0.97 | 16 | 16 | ADVERTENCIA |
| `manifiestos/57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md` | 584 | 656 | 1.12 | 10 | 11 | REVISAR |
| `manifiestos/58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md` | 709 | 770 | 1.09 | 13 | 14 | REVISAR |
| `manifiestos/59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md` | 631 | 730 | 1.16 | 13 | 14 | REVISAR |
| `manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md` | 1539 | 1524 | 0.99 | 15 | 16 | REVISAR |
| `manifiestos/61_contra_reduccionismo_matematico_custodia_experimental_multiescalar_ES_EN.md` | 1067 | 1072 | 1.00 | 12 | 14 | REVISAR |
| `manifiestos/62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md` | 1125 | 1152 | 1.02 | 14 | 14 | OK |
| `manifiestos/63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md` | 1120 | 1141 | 1.02 | 16 | 16 | OK |
| `manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md` | 838 | 813 | 0.97 | 14 | 14 | OK |
| `manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md` | 882 | 882 | 1.00 | 14 | 14 | OK |
| `manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md` | 1651 | 1636 | 0.99 | 14 | 14 | OK |
| `manifiestos/66_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md` | 1157 | 1188 | 1.03 | 13 | 13 | OK |
| `manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md` | 1234 | 1268 | 1.03 | 10 | 10 | OK |
| `manifiestos/RELACIONES_LVII_LIX_ES_EN.md` | 357 | 355 | 0.99 | 1 | 1 | OK |
| `analisis/publicos/2026-08-05_de-la-economia-de-la-atencion-a-la-economia-del-aporte_ES_EN.md` | 3237 | 3440 | 1.06 | 29 | 30 | OK |
| `analisis/publicos/2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md` | 621 | 912 | 1.47 | 6 | 7 | OK |
| `analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md` | 1285 | 1569 | 1.22 | 12 | 14 | OK |
| `analisis/publicos/2026-08-06_segundo_escalado_distrokid_sin_respuesta_ES_EN.md` | 825 | 1094 | 1.33 | 8 | 9 | OK |
| `analisis/publicos/2026-08-07_maxproc_proteccion_integral_infancia_punto_no_retorno_ES_EN.md` | 2582 | 2799 | 1.08 | 40 | 42 | OK |
| `analisis/publicos/2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md` | 531 | 670 | 1.26 | 5 | 6 | OK |
| `analisis/publicos/2026-08-07_spotify_respuesta_generica_distrokid_cierre_circular_ES_EN.md` | 403 | 604 | 1.50 | 6 | 7 | OK |
| `analisis/publicos/2026-08-08_accesibilidad_institucional_escalado_ciudadano_jefaturas_estado_ES_EN.md` | 807 | 805 | 1.00 | 8 | 9 | OK |
| `analisis/publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md` | 656 | 657 | 1.00 | 9 | 9 | OK |
| `analisis/publicos/2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md` | 803 | 772 | 0.96 | 14 | 14 | OK |
| `analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md` | 419 | 417 | 1.00 | 4 | 4 | OK |
| `analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md` | 908 | 952 | 1.05 | 12 | 13 | OK |
| `analisis/publicos/2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md` | 754 | 713 | 0.95 | 8 | 8 | OK |
| `analisis/publicos/2026-08-08_estado_correo_difusion_idea_y_adhesiones_sintesis_ES_EN.md` | 404 | 373 | 0.92 | 12 | 12 | OK |
| `analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md` | 1721 | 1706 | 0.99 | 21 | 22 | OK |
| `analisis/publicos/2026-08-08_techno_bach_record_semanal_apple_music_ES_EN.md` | 335 | 289 | 0.86 | 5 | 5 | OK |
| `analisis/publicos/2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md` | 1245 | 1208 | 0.97 | 14 | 14 | OK |
| `analisis/publicos/2026-08-09_delta_manifestacion_sistemica_necesidad_neo0_idea_custodia_cognitiva_ES_EN.md` | 1070 | 1202 | 1.12 | 11 | 12 | OK |
| `analisis/publicos/2026-08-09_guerra_fundador_contra_idiotez_devolucion_tiempo_bien_comun_ES_EN.md` | 1144 | 1110 | 0.97 | 12 | 12 | OK |
| `analisis/publicos/2026-08-09_maxproc_registro_entrada_trazabilidad_derivacion_herosion_ES_EN.md` | 754 | 760 | 1.01 | 12 | 12 | OK |
| `analisis/publicos/2026-08-09_prueba_operativa_minima_revision_ia_escalable_ES_EN.md` | 555 | 541 | 0.97 | 8 | 8 | OK |
| `analisis/publicos/2026-08-09_respuestas_externas_smil_winograd_deltas_ES_EN.md` | 433 | 482 | 1.11 | 6 | 7 | OK |
| `analisis/publicos/2026-08-10_LXI_genetica_ADN_neopandora_placa_petri_ES_EN.md` | 417 | 391 | 0.94 | 0 | 0 | OK |

> La paridad editorial exigida no significa traducción palabra por palabra ni idéntica maquetación, pero sí conservación íntegra de tesis, secciones, matices, cautelas epistemológicas, ejemplos, fórmulas, relaciones y conclusión.
