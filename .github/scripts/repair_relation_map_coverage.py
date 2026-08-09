from pathlib import Path
import re,sys
p=Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md')
t=p.read_text(encoding='utf-8')
t=t.replace('**Estado / Status:** público · relacional · 2026-08-08 / public · relational · 2026-08-08','**Estado / Status:** público · relacional · 2026-08-09 / public · relational · 2026-08-09')
old='''### LVII–LIX · Refugio → Inteligencia Civilizatoria → Custodia Cognitiva
- [Mapa específico LVII–LIX](./RELACIONES_LVII_LIX_ES_EN.md)
- [LVII · #77](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/77) · [LVIII · #78](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/78) · [LIX · #79](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/79)
- La secuencia conecta cuidado basal, capacidad cognitiva pública y custodia distribuida sin monopolio de conciencia.'''
new='''### LVII–LIX · Refugio → Inteligencia Civilizatoria → Custodia Cognitiva
- [Mapa específico LVII–LIX](./RELACIONES_LVII_LIX_ES_EN.md)
- [LVII · Madre, Refugio y Retorno Consciente™](./57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md) · [Síntesis #77](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/77)
- [LVIII · Inteligencia Civilizatoria™](./58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md) · [Síntesis #78](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/78)
- [LIX · Custodia Cognitiva Distribuida™](./59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md) · [Síntesis #79](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/79)
- La secuencia conecta cuidado basal, capacidad cognitiva pública y custodia distribuida sin monopolio de conciencia.'''
if old in t:t=t.replace(old,new,1)
elif '57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md' not in t:
    raise SystemExit('LVII-LIX relation block not found for safe patch')
# Add an explicit English mirror for the appended extension without replacing Spanish.
A='<!-- NEO_RELATIONS_EXTENSION_EN_START -->';B='<!-- NEO_RELATIONS_EXTENSION_EN_END -->'
en=f'''{A}

## LIII–LIX · Current relational extension

- **LIII · Leónidas™:** [Manifesto](./53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md) · [Open Synthesis #69](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/69). Main relations: II · Open Synthesis; III · Right of Contribution; IX · Memory/Genealogy/Traceability; XX · Umbral-X; XXXIV · Joint Audit; XLVIII · The Synthesis Sees Everything; LI · Civic Power.
- **LIV · Wealth and Scrap™:** [Manifesto](./54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md) · [Open Synthesis #72](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/72). Repair, reparability, second life, remanufacture, recovery and dignity of repair work; related to VII, XXIII, XXV, XXVII, XXX and XLV.
- **LV · Attack of the Micromachines™:** [Manifesto](./55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md) · [Open Synthesis #74](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/74) · [Evidence state](../analisis/publicos/2026-08-09_micromaquinas_plagas_escala_invisible_estado_real_ES_EN.md). Related to IX, XX, XXX, XXXVIII, XLV and LVI.
- **LVI · NO-CONTROL™:** [Manifesto](./56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md) · [Open Synthesis #76](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/76). Related to IV, IX, XXX, XXXIV, XLIV, XLV and LIX; dual-use capability is not evidence of hostile intent.
- **LVII · Mother, Refuge and Conscious Return™:** [Manifesto](./57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md) · [#77](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/77).
- **LVIII · Civilisational Intelligence™:** [Manifesto](./58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md) · [#78](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/78).
- **LIX · Distributed Cognitive Custodianship™:** [Manifesto](./59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md) · [#79](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/79).

## Neoaxioms™ ↔ Manifestos ↔ applied work

- [Neoaxioms™](../neoaxiomas/README.md) · [General matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80).
- **NAX-01 / NAX-08 / NAX-14** ↔ V, VII, L, LVIII, LIX.
- **NAX-02–06** ↔ II, IX, XIX, XLVIII.
- **NAX-07** ↔ X, XLIII, LIX.
- **NAX-09** ↔ XXX, LIV, LVI.
- **NAX-10** ↔ XXV, XXXVI.
- **NAX-11** ↔ I, IX, XXXIV.
- **NAX-12** ↔ IX, X, XXXIV.
- **NAX-13** ↔ VII, XXI, XXIII.
- **NAX-14** ↔ V, XIV, XXXVIII, XLII–XLIII, LVIII–LIX.

**Rule:** these are structural/documentary relations open to SAN; conceptual proximity is not causal proof.

{B}'''
if A in t and B in t:t=re.sub(re.escape(A)+r'.*?'+re.escape(B),en,t,count=1,flags=re.S)
else:t=t.rstrip()+'\n\n'+en+'\n'
p.write_text(t,encoding='utf-8')
for f in ['49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md','53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md','54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md','55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md','56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md','57_madre_refugio_seguridad_basal_retorno_consciente_ES_EN.md','58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md','59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md']:
    if f not in t:raise SystemExit('coverage missing '+f)
print('POSTCHECK OK: relation map explicit I-LIX coverage and bilingual extension')
