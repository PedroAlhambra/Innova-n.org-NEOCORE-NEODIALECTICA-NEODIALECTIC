from pathlib import Path
import re

ROOT = Path('.').resolve()
REL = ROOT / 'manifiestos' / 'RELACIONES_TRABAJO_APLICADO_ES_EN.md'
MIDX = ROOT / 'manifiestos' / 'README.md'
SYNIDX = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
NEO = ROOT / 'neoaxiomas' / 'README.md'
DELTA = ROOT / 'propuestas' / 'sintesis-abierta' / '2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'
START='<!-- NEO_RELATIONS_LXI_LXXIV_START -->'
END='<!-- NEO_RELATIONS_LXI_LXXIV_END -->'

ROMANS=['LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX','LXXI','LXXII','LXXIII','LXXIV']


def parse_manifest_index():
    text=MIDX.read_text(encoding='utf-8')
    out={}
    for roman,label,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',text,re.M):
        out[roman]={'label':label.strip(),'href':href.strip()}
    return out


def parse_synthesis_index():
    text=SYNIDX.read_text(encoding='utf-8')
    out={}
    for roman,href,issue in re.findall(r'^\|\s*([IVXLCDM]+)\s*\|\s*\[[^\]]+\]\((?:\.\./\.\./manifiestos/)?([^)]+\.md)\)\s*\|\s*\[#(\d+)\]',text,re.M):
        out[roman]={'href':href.strip(),'issue':issue}
    return out

manifest=parse_manifest_index()
synth=parse_synthesis_index()
missing=[r for r in ROMANS if r not in manifest or r not in synth]
if missing:
    raise SystemExit('Cannot sync relational frontier; missing canonical rows: '+', '.join(missing))

# Relations here are intentionally explicit and conservative. They cite existing
# canonical nodes/deltas; they do not claim causal equivalence.
RELATIONS={
'LXI': {
    'kind':'B–C · método experimental, límites del formalismo y contraste multiescalar / experimental method, limits of formalism and multiscale scrutiny',
    'links':[
        ('XX · Umbral-X™','./20_defensa_intelectual_neodialectica_umbral_x_ES_EN.md'),
        ('XLV · Multidimensionalidad Neodialéctica™','./45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md'),
        ('LVIII · Inteligencia Civilizatoria™','./58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md'),
        ('NeoGenealogía™','../propuestas/sintesis-abierta/NEOGENEALOGIA_DETECCION_ANTECEDENTES_CONVERGENCIAS_ES_EN.md'),
    ]},
'LXII': {
    'kind':'C · arquitectura de juego, honor, no coronación de la parte y continuidad abierta / game architecture, honor, non-coronation of the part and open continuity',
    'links':[
        ('XLIV · Neowar™','./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md'),
        ('∞ · Puerta Abierta del Fractal','./INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'),
        ('C-NAX-16 · No Coronación de la Parte™','../neoaxiomas/README.md'),
    ]},
'LXIII': {
    'kind':'A–C · fidelidad de compresión, integridad documental y acceso sin mutilación / compression fidelity, documentary integrity and access without mutilation',
    'links':[
        ('IX · Memoria, Genealogía y Trazabilidad','./06_memoria_genealogia_trazabilidad_ES_EN.md'),
        ('XXXIV · Auditoría Conjunta Perpetua™','./34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md'),
        ('Auditoría ES/EN','../auditorias/publicas/2026-08-09_auditoria_paridad_ES_EN_manifiestos_articulos.md'),
        ('Auditoría estructural bilingüe','../auditorias/publicas/2026-08-12_auditoria_estructura_bilingue_manifiestos_ES_EN.md'),
    ]},
'LXIV': {
    'kind':'A–C · tiempo de aporte, medición trazable y entrada en Síntesis Abierta / contribution time, traceable measurement and Open-Synthesis entry',
    'links':[
        ('VII · Economía del Aporte','./04_economia_del_aporte_ES_EN.md'),
        ('X · WEB4™ · SistemaTrazable™','./07_web4_sistematrazable_ES_EN.md'),
        ('NeoCronos™ · upgrade de entrada/panel/traza','../propuestas/sintesis-abierta/NEOCRONOS_UPGRADE_ENTRADA_PANEL_TRAZA_ES_EN.md'),
        ('NeoCronos™ · retorno temporal/tokenización','../propuestas/sintesis-abierta/NEOCRONOS_RETORNO_TEMPORAL_TOKENIZACION_ES_EN.md'),
        ('NAX-13 · Liberación del Tiempo de Control hacia Creación y Aporte™','../neoaxiomas/README.md'),
    ]},
'LXV': {
    'kind':'B–C · incentivo, reconocimiento y juego subordinados al Bien Común / incentive, recognition and game subordinated to the Common Good',
    'links':[
        ('VII · Economía del Aporte','./04_economia_del_aporte_ES_EN.md'),
        ('LXIV · NeoCronos™','./64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md'),
        ('XL · Respeto, Neoego y Honor Relacional™','./40_respeto_neoego_honor_relacional_ES_EN.md'),
    ]},
'LXVI': {
    'kind':'B–C · cooperación, NeoSinergia™ y coordinación bajo tensión / cooperation, NeoSynergy™ and coordination under tension',
    'links':[
        ('NAX-08 · Cooperación de Excelencia frente a Competencia Depredadora™','../neoaxiomas/README.md'),
        ('C-NAX-18 · Motor del Bien Común + NeoSinergia™','../neoaxiomas/README.md'),
        ('LXVII · NeoTitanes™','./67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md'),
        ('LIII · Leónidas™','./53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md'),
    ]},
'LXVII': {
    'kind':'B–C · reconstrucción sistémica, cooperación y motor del Bien Común / systemic reconstruction, cooperation and Common-Good engine',
    'links':[
        ('C-NAX-17 · Reconstrucción Sistémica™','../neoaxiomas/README.md'),
        ('C-NAX-18 · Motor del Bien Común + NeoSinergia™','../neoaxiomas/README.md'),
        ('LXVI · NeoSinergia™','./66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md'),
        ('XXXIV · Auditoría Conjunta Perpetua™','./34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md'),
    ]},
'LXVIII': {
    'kind':'B–C · soberanía intelectual, atribución y separación entre conflicto ajeno y juicio propio / intellectual sovereignty, attribution and separation between inherited conflict and independent judgement',
    'links':[
        ('IX · Memoria, Genealogía y Trazabilidad','./06_memoria_genealogia_trazabilidad_ES_EN.md'),
        ('XXII · Contra la Reducción y Captura Intelectual™','./22_contra_reduccion_captura_intelectual_ES_EN.md'),
        ('C-NAX-15 · Soberanía Intelectual de la Especie™','../neoaxiomas/README.md'),
        ('NeoGenealogía™','../propuestas/sintesis-abierta/NEOGENEALOGIA_DETECCION_ANTECEDENTES_CONVERGENCIAS_ES_EN.md'),
    ]},
'LXIX': {
    'kind':'B–C · protección proporcional, inocencia y asimetría de poder / proportional protection, innocence and power asymmetry',
    'links':[
        ('XXXVIII · Protección Integral de la Infancia™','./38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md'),
        ('C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™','../neoaxiomas/README.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
'LXX': {
    'kind':'B–C · arquetipo funcional, depredación relacional y no reducción de persona a conducta / functional archetype, relational predation and non-reduction of person to conduct',
    'links':[
        ('XVI · Refragmentación Arquetípica™','./16_refragmentacion_arquetipica_ES_EN.md'),
        ('C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™','../neoaxiomas/README.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
'LXXI': {
    'kind':'B–C · libertad adulta, hipersexualización industrial y separación de planos / adult freedom, industrial hypersexualisation and separation of planes',
    'links':[
        ('XXXI · Neuromarketing Antihumanista™','./31_contra_neuromarketing_antihumanista_ES_EN.md'),
        ('XXXVIII · Protección Integral de la Infancia™','./38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md'),
        ('C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™','../neoaxiomas/README.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
'LXXII': {
    'kind':'B–C · fuerza, deseo y poder convertidos en responsabilidad de custodia / strength, desire and power converted into custodial responsibility',
    'links':[
        ('XXXVI · Corona, Águila y Custodia™','./36_corona_aguila_custodia_edad_del_hombre_ES_EN.md'),
        ('XLI · Fuerza Protectora™','./41_martillo_limitado_talion_fuerza_protectora_ES_EN.md'),
        ('C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™','../neoaxiomas/README.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
'LXXIII': {
    'kind':'B–C · maduración invertida, humanidad común y reversibilidad arquetípica / inverted maturation, common humanity and archetypal reversibility',
    'links':[
        ('C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™','../neoaxiomas/README.md'),
        ('C-NAX-21 · Ignorancia Sistémica del Mal™','../neoaxiomas/README.md'),
        ('LXXIV · Asimetría de la Destrucción™','./74_asimetria_destruccion_trol_humano_bot_ES_EN.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
'LXXIV': {
    'kind':'B–C · asimetría de coste del daño, trolismo, microagencia digital y reparación / asymmetry in the cost of harm, trollism, digital micro-agency and repair',
    'links':[
        ('VI · Parasitismo Sistémico','./09_parasitismo_sistemico_ES_EN.md'),
        ('LV · Micromáquinas™','./55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md'),
        ('C-NAX-21 · Ignorancia Sistémica del Mal™','../neoaxiomas/README.md'),
        ('Delta relacional LXXIII–LXXIV','../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md'),
    ]},
}

lines=[START,'','---','',
'## LXI–LXXIV · frontera relacional vigente / current relational frontier','',
'> Esta sección completa el mapa curado hasta el último manifiesto finito vigente. Las relaciones indican afinidad funcional, genealogía, aplicación o contraste documental; no prueban causalidad, identidad conceptual ni validación automática. / This section completes the curated map up to the current latest finite manifesto. Relations indicate functional affinity, genealogy, application or documentary scrutiny; they do not prove causation, conceptual identity or automatic validation.','']

for roman in ROMANS:
    m=manifest[roman]; s=synth[roman]; spec=RELATIONS[roman]
    lines += [
        f'### {roman} · [{m["label"]}](./{m["href"]})',
        f'- **Relación / Relation:** {spec["kind"]}.',
        f'- **Síntesis Abierta / Open Synthesis:** [#{s["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{s["issue"]}).',
        '- **Interconexiones / Interconnections:** ' + ' · '.join(f'[{label}]({href})' for label,href in spec['links']) + '.',
        ''
    ]

lines += [
'### Neoaxiomas relacionados / Related Neoaxioms','',
'- **LXVIII → C-NAX-15 · Soberanía Intelectual de la Especie™ / Intellectual Sovereignty of the Species™.**',
'- **LXII + ∞ → C-NAX-16 · No Coronación de la Parte™ / Non-Coronation of the Part™.**',
'- **LXVII → C-NAX-17 · Reconstrucción Sistémica™ / Systemic Reconstruction™.**',
'- **LXVI + LXVII → C-NAX-18 · Motor del Bien Común + NeoSinergia™ / Common-Good Engine + NeoSynergy™.**',
'- **LXIX–LXXII → C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™ / Relational Inviolability and Separation of Planes™.**',
'- **LXXIII → C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™.**',
'- **VI + LXXIII + LXXIV → C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™.**','',
'[Abrir capa neoaxiomática completa / Open full Neoaxiomatic layer](../neoaxiomas/README.md) · [Matriz general SAN #80 / General SAN matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80)','',
END
]
block='\n'.join(lines)
text=REL.read_text(encoding='utf-8')
old=text

# Keep the coverage statement dynamic and bilingual.
text=re.sub(
    r'^\*\*Estado / Status:\*\*.*$',
    '**Estado / Status:** público · relacional · vivo / public · relational · living  ',
    text, count=1, flags=re.M
)
text=re.sub(
    r'^\*\*Cobertura / Coverage:\*\*.*$',
    '**Cobertura / Coverage:** I–LXXIV · 74 manifiestos finitos + ∞ como continuidad abierta / 74 finite manifestos I–LXXIV + ∞ as open continuity  ',
    text, count=1, flags=re.M
)

if START in text and END in text:
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block,text,flags=re.S)
else:
    # Place the living frontier immediately before the maintenance rule when possible.
    marker='## Regla de mantenimiento / Maintenance rule'
    if marker in text:
        text=text.replace(marker,block+'\n\n---\n\n'+marker,1)
    else:
        text=text.rstrip()+'\n\n'+block+'\n'

if text!=old:
    REL.write_text(text,encoding='utf-8')
    print('RELATIONS_FRONTIER_SYNC changed=1 coverage=I-LXXIV entries=14')
else:
    print('RELATIONS_FRONTIER_SYNC changed=0 coverage=I-LXXIV entries=14')
