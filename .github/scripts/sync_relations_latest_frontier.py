from pathlib import Path
import json
import re

ROOT = Path('.').resolve()
REL = ROOT / 'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
REG = ROOT / 'manifiestos/CANONICAL_FILENAMES.json'
START = '<!-- NEO_RELATIONS_LATEST_FRONTIER_START -->'
END = '<!-- NEO_RELATIONS_LATEST_FRONTIER_END -->'


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


entries = json.loads(REG.read_text(encoding='utf-8'))['entries']
latest = max(entries, key=roman_to_int)
count = len(entries)
latest_path = entries[latest]['legacy']
text = REL.read_text(encoding='utf-8')

# Header and matrix labels are living inventory metadata and must never lag the registry.
text = re.sub(
    r'^\*\*Cobertura / Coverage:\*\*.*$',
    f'**Cobertura / Coverage:** I–{latest} · {count} manifiestos finitos + ∞ como continuidad abierta / {count} finite manifestos I–{latest} + ∞ as open continuity  ',
    text,
    count=1,
    flags=re.M,
)
text = re.sub(
    r'^## Matriz completa I–[IVXLCDM]+ / Complete I–[IVXLCDM]+ matrix$',
    f'## Matriz completa I–{latest} / Complete I–{latest} matrix',
    text,
    count=1,
    flags=re.M,
)

# Curated frontier. Each new finite manifesto must become explicitly present in
# the relational map; inventory metadata alone is not enough. The relational
# audit intentionally fails when a new frontier node has not yet been curated.
SPECS = [
    {
        'roman':'LXXVII',
        'title':'Contra la Polarización Binaria y la Radicalización Recíproca™ / Against Binary Polarisation and Reciprocal Radicalisation™',
        'file':'77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md',
        'issue':154,
        'relation':'B–C · separación entre fenómeno, causalidad y narrativa; radicalización recíproca; polarización; custodia epistemológica de IA y medios / separation of phenomenon, causality and narrative; reciprocal radicalisation; polarisation; epistemic custodianship of AI and media.',
        'links':[
            ('XXII · Contra la Reducción y la Captura Intelectual™','22_contra_reduccion_captura_intelectual_ES_EN.md'),
            ('XXXV · Contra la Ridiculez Mediática y la Economía del Conflicto™','35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md'),
            ('XLII · Fin de la Era del Hombre Manipulado™','42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'),
            ('LIII · Leónidas™','53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md'),
            ('LXIII · Contra la Simplificación Burda del Marco™','63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md'),
            ('LXXIV · Asimetría de la Destrucción™','74_asimetria_destruccion_trol_humano_bot_ES_EN.md'),
            ('LXXVI · El Altavoz sin Síntesis™','76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md'),
        ],
        'extra':'- **Candidato neoaxiomático derivado / Derived neoaxiomatic candidate:** [C-NAX-25 · Fenómeno ≠ Narrativa™ / Phenomenon ≠ Narrative™](../propuestas/sintesis-abierta/2026-08-16_C_NAX_25_FENOMENO_NO_ES_NARRATIVA_ES_EN.md) · [Síntesis #155 / Synthesis #155](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/155).\n- **Delta transversal relacionado / Related transversal delta:** [Poder, Trazabilidad, Escrutinio y Evidencia™ / Power, Traceability, Scrutiny and Evidence™](../propuestas/sintesis-abierta/2026-08-16_DELTA_PODER_TRAZABILIDAD_ESCRUTINIO_EVIDENCIA_ES_EN.md) · [C-NAX-26](../propuestas/sintesis-abierta/2026-08-16_C_NAX_26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md) · [Síntesis #156 / Synthesis #156](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/156).',
    },
    {
        'roman':'LXXVIII',
        'title':'Incontrolabilidad Intrínseca y Necesidad del Neorrenacimiento Humano™ / Intrinsic Uncontrollability and the Necessity of the Human Neo-Renaissance™',
        'file':'78_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md',
        'issue':157,
        'relation':'A–B–C · genealogía del Neorrenacimiento anterior a la Neodialéctica; límites del control de sistemas humanos complejos; educación, criterio, responsabilidad y reconstrucción cultural / genealogy of the Neo-Renaissance prior to Neodialectics; limits of control in complex human systems; education, criterion, responsibility and cultural reconstruction.',
        'links':[
            ('XI · Neorrenacimiento Humano','08_neorrenacimiento_humano_ES_EN.md'),
            ('XXIV · Evolución Neorrenacentista','24_evolucion_neorrenacentista_resistencias_sistema_ES_EN.md'),
            ('XXX · Coherencia entre Fines y Medios','30_coherencia_fines_medios_ES_EN.md'),
            ('LVI · NO-CONTROL™','56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md'),
            ('LVIII · Inteligencia Civilizatoria™','58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md'),
            ('LIX · Custodia Cognitiva Distribuida™','59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md'),
            ('LXXVII · Polarización Binaria','77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md'),
        ],
        'extra':'',
    },
    {
        'roman':'LXXIX',
        'title':'Contra el Alarmismo sin Síntesis™ · Advertir obliga a construir / Against Alarmism without Synthesis™ · Warning Creates a Duty to Build',
        'file':'79_contra_alarmismo_sin_sintesis_responsabilidad_alternativa_ES_EN.md',
        'issue':158,
        'relation':'B–C · separación entre señal de riesgo y prueba; deber de construir alternativas verificables; proporcionalidad entre advertencia, evidencia, incertidumbre y respuesta / separation between risk signal and proof; duty to build verifiable alternatives; proportionality among warning, evidence, uncertainty and response.',
        'links':[
            ('XXXV · Economía del Conflicto™','35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md'),
            ('XLII · Soberanía Cognitiva','42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'),
            ('LIII · Leónidas™','53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md'),
            ('LVI · NO-CONTROL™','56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md'),
            ('LXIII · Contra la Simplificación Burda','63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md'),
            ('LXXIV · Asimetría de la Destrucción™','74_asimetria_destruccion_trol_humano_bot_ES_EN.md'),
            ('LXXVI · Altavoz sin Síntesis™','76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md'),
            ('LXXVII · Polarización Binaria','77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md'),
        ],
        'extra':'',
    },
    {
        'roman':'LXXX',
        'title':'Neotrama™ · Hojas reconstruidas, agua recuperada y Fuego de Agua™ / Neotrama™ · Reconstructed Leaves, Recovered Water and Fire of Water™',
        'file':'80_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md',
        'issue':159,
        'relation':'A–B–C · reconstrucción de criterio, memoria y tejido relacional; recuperación frente a degradación; integración entre naturaleza, cultura, símbolo y acción verificable / reconstruction of criterion, memory and relational fabric; recovery from degradation; integration of nature, culture, symbol and verifiable action.',
        'links':[
            ('IX · Memoria, Genealogía y Trazabilidad','06_memoria_genealogia_trazabilidad_ES_EN.md'),
            ('XVI · Refragmentación Arquetípica™','16_refragmentacion_arquetipica_ES_EN.md'),
            ('XXV · Pulido de la Piedra™','25_pulido_de_la_piedra_ES_EN.md'),
            ('XLVI · Cerrar la Herida™','46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md'),
            ('LXVII · NeoTitanes™','67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md'),
            ('LXXV · Hojas Carcomidas™','75_las_hojas_carcomidas_memoria_natural_viracion_arquetipica_ES_EN.md'),
            ('LXXVIII · Neorrenacimiento e Incontrolabilidad','78_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md'),
        ],
        'extra':'',
    },
    {
        'roman':'LXXXI',
        'title':'Ultralujo como Bien Común™ · La élite del aporte / Ultraluxury as Common Good™ · The elite of contribution',
        'file':'81_ultralujo_bien_comun_elite_neodialectica_aporte_ES_EN.md',
        'issue':160,
        'relation':'A–B–C · Economía del Aporte, reconocimiento no jerárquico, capital como capacidad material sin compra de verdad, reciprocidad y prevención de castas mediante tokenización / Contribution Economy, non-hierarchical recognition, capital as material capacity without purchase of truth, reciprocity and prevention of tokenised castes.',
        'links':[
            ('III · Derecho Humano de Aporte','03_derecho_humano_aporte_sintesis_abierta_ES_EN.md'),
            ('VII · Economía del Aporte','04_economia_del_aporte_ES_EN.md'),
            ('XXI · Reconocimiento Neodialéctico™','21_reconocimiento_neodialectico_ES_EN.md'),
            ('XXIX · Contra la Idolatría del Dinero™','29_idolatria_del_dinero_ES_EN.md'),
            ('LX · Relevancia Humana Necesaria™','60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md'),
            ('LXIV · NeoCronos™','64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md'),
            ('LXV · NeoJuego™','65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md'),
            ('LXVI · NeoSinergia™ / MÉDICI™','66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md'),
            ('LXXX · Neotrama™','80_neotrama_hojas_reconstruidas_agua_recuperada_fuego_de_agua_ES_EN.md'),
        ],
        'extra':'',
    },
]

blocks=[]
for spec in SPECS:
    if roman_to_int(spec['roman']) > roman_to_int(latest):
        continue
    links=' · '.join(f'[{label}](./{path})' for label,path in spec['links'])
    issue=spec['issue']
    block=f'''## {spec['roman']} · {spec['title']}

- **Manifiesto / Manifesto:** [{spec['roman']} · {spec['title']}](./{spec['file']}).
- **Relación / Relation:** {spec['relation']}
- **Síntesis Abierta / Open Synthesis:** [#{issue}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue}).
'''
    if spec['extra']:
        block += spec['extra']+'\n'
    block += f'- **Interconexiones / Interconnections:** {links}.\n'
    blocks.append(block.rstrip())

managed = START + '\n\n' + '\n\n'.join(blocks) + '\n\n' + END
if START in text and END in text:
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END), managed, text, count=1, flags=re.S)
else:
    marker = '## Regla de mantenimiento / Maintenance rule'
    if marker in text:
        text = text.replace(marker, managed + '\n\n---\n\n' + marker, 1)
    else:
        text = text.rstrip() + '\n\n' + managed + '\n'

REL.write_text(text, encoding='utf-8')
print(f'RELATIONS_LATEST_FRONTIER count={count} latest={latest} curated_through=LXXXI source={latest_path}')
