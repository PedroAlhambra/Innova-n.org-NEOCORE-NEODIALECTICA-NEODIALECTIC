from pathlib import Path
import re

ROOT = Path('.').resolve()
NEO = ROOT / 'neoaxiomas/README.md'
SYN = ROOT / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
PROTOCOL = ROOT / 'propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md'
GLOBAL_AUDIT = ROOT / '.github/scripts/audit_global_bilingual_symmetry.py'
GLOBAL_WORKFLOW = ROOT / '.github/workflows/audit-global-bilingual-symmetry.yml'

REPO = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'

CANDIDATES = {
    15: {
        'es_title': 'Soberanía Intelectual de la Especie™',
        'en_title': 'Intellectual Sovereignty of the Species™',
        'provenance': '[LXVIII](../manifiestos/68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md)',
        'issue': 150,
        'es': 'Ningún nodo humano, institucional o artificial debe adquirir capacidad suficiente para sustituir de forma opaca, irreversible o incontestable la formación distribuida del juicio de la especie. Toda arquitectura de gran poder cognitivo debe preservar pluralidad, trazabilidad, crítica, salida, memoria y posibilidad real de corrección.',
        'en': "No human, institutional or artificial node should acquire enough power to opaquely, irreversibly or incontestably replace the distributed formation of the species' judgement. Every architecture of major cognitive power must preserve plurality, traceability, criticism, exit, memory and a real possibility of correction.",
        'formula_es': 'PLURALIDAD + MEMORIA + CONTRASTE + EDUCACIÓN\n+ DERECHO A DISENTIR + DERECHO A SALIR\n+ IA NO SOBERANA + RESPONSABILIDAD HUMANA\n= SOBERANÍA INTELECTUAL DE LA ESPECIE™',
        'formula_en': 'PLURALITY + MEMORY + SCRUTINY + EDUCATION\n+ RIGHT TO DISSENT + RIGHT TO EXIT\n+ NON-SOVEREIGN AI + HUMAN RESPONSIBILITY\n= INTELLECTUAL SOVEREIGNTY OF THE SPECIES™',
    },
    16: {
        'es_title': 'No Coronación de la Parte™',
        'en_title': 'Non-Crowning of the Part™',
        'provenance': '[LXII](../manifiestos/62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md) + [∞](../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)',
        'issue': 151,
        'es': 'Ninguna persona, IA, fundación, corporación, mayoría o subsistema puede reclamar equivalencia con el Todo. Toda autoridad dentro del marco es funcional, limitada, trazable, impugnable y revisable.',
        'en': 'No person, AI, foundation, corporation, majority or subsystem may claim equivalence with the Whole. Every authority within the framework is functional, limited, traceable, challengeable and revisable.',
        'formula_es': 'AUTORÍA ≠ VERDAD\nAUTORIDAD ≠ TOTALIDAD\nINSTITUCIÓN ≠ TOTALIDAD\nCAPITAL ≠ TOTALIDAD\nMAYORÍA ≠ TOTALIDAD\nIA ≠ TOTALIDAD\nNEO0 ≠ TOTALIDAD',
        'formula_en': 'AUTHORSHIP ≠ TRUTH\nAUTHORITY ≠ TOTALITY\nINSTITUTION ≠ TOTALITY\nCAPITAL ≠ TOTALITY\nMAJORITY ≠ TOTALITY\nAI ≠ TOTALITY\nNEO0 ≠ TOTALITY',
    },
    17: {
        'es_title': 'Reconstrucción Sistémica™',
        'en_title': 'Systemic Reconstruction™',
        'provenance': '[LXVII](../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md)',
        'issue': 152,
        'es': 'Una función sistémica no se vuelve innecesaria porque se haya perdido la comprensión de su papel. Antes de desmontar, sustituir o restaurar una estructura, deben reconstruirse sus funciones y dependencias, separar el valor del error histórico, reparar sus enlaces y reintegrar lo útil en una arquitectura superior sin copiar ni borrar el pasado.',
        'en': 'A systemic function does not become unnecessary because understanding of its role has been lost. Before dismantling, replacing or restoring a structure, its functions and dependencies must be reconstructed, value separated from historical error, links repaired, and what remains useful reintegrated into a higher architecture without copying or erasing the past.',
        'formula_es': 'RECONSTRUIR\n≠ COPIAR EL PASADO\n≠ BORRAR EL PASADO\n≠ DESTRUIR PARA EMPEZAR DE CERO\n\nRECONSTRUIR\n= RECUPERAR FUNCIÓN\n+ COMPRENDER DEPENDENCIAS\n+ SEPARAR VALOR DE ERROR HISTÓRICO\n+ REPARAR ENLACES\n+ REINTEGRAR EN ARQUITECTURA SUPERIOR',
        'formula_en': 'RECONSTRUCT\n≠ COPY THE PAST\n≠ ERASE THE PAST\n≠ DESTROY EVERYTHING TO START AGAIN\n\nRECONSTRUCT\n= RECOVER FUNCTION\n+ UNDERSTAND DEPENDENCIES\n+ SEPARATE VALUE FROM HISTORICAL ERROR\n+ REPAIR LINKS\n+ REINTEGRATE INTO A HIGHER ARCHITECTURE',
    },
    18: {
        'es_title': 'Motor del Bien Común + NeoSinergia™',
        'en_title': 'Common-Good Engine + NeoSynergy™',
        'provenance': '[LXVI](../manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md) + [LXVII](../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md)',
        'issue': 153,
        'es': 'El Bien Común actúa como core-motor cuando capacidades diferentes interoperan sin perder singularidad y producen potencia común. Si una necesidad trazable activa una función aceptada y existe capacidad pertinente para contribuir de forma proporcional sin vulnerar derechos ni límites superiores, la cooperación puede pasar de opción a deber funcional justificable, siempre discutible, recusable, limitado y auditable.',
        'en': 'The Common Good acts as a core engine when different capabilities interoperate without losing their singularity and produce common power. When a traceable need activates an accepted function and relevant capacity exists to contribute proportionally without violating rights or higher limits, cooperation may shift from an option to a justifiable functional duty, always open to discussion, challenge, limitation and audit.',
        'formula_es': 'CAPACIDADES DIFERENTES\n+ NECESIDAD TRAZABLE\n+ COORDINACIÓN\n+ DERECHOS Y LÍMITES\n+ SAN™\n→ NEOSINERGIA™\n→ POTENCIA COMÚN\n\nDEBER DE COOPERAR + DERECHOS Y LÍMITES\n= RESPONSABILIDAD, NO SERVIDUMBRE',
        'formula_en': 'DIFFERENT CAPABILITIES\n+ TRACEABLE NEED\n+ COORDINATION\n+ RIGHTS AND LIMITS\n+ SAN™\n→ NEOSYNERGY™\n→ COMMON POWER\n\nDUTY TO COOPERATE + RIGHTS AND LIMITS\n= RESPONSIBILITY, NOT SERVITUDE',
    },
    19: {
        'es_title': 'Inviolabilidad Relacional y Separación de Planos™',
        'en_title': 'Relational Inviolability and Separation of Planes™',
        'provenance': '[LXIX](../manifiestos/69_defensa_inocencia_humana_asimetria_protectora_deber_custodia_ES_EN.md) + [LXX](../manifiestos/70_fauno_masculinidad_fragmentada_depredacion_relacional_retorno_hombre_ES_EN.md) + [LXXI](../manifiestos/71_libertad_sexual_hipersexualizacion_industrial_separacion_planos_ES_EN.md) + [LXXII](../manifiestos/72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md)',
        'issue': 123,
    },
    20: {
        'es_title': 'Humanidad Común sin Supresión de la Diferencia™',
        'en_title': 'Common Humanity without Suppression of Difference™',
        'provenance': '[LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md)',
        'issue': 126,
    },
    21: {
        'es_title': 'Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™',
        'en_title': 'Systemic Ignorance of Evil and Non-Superiority of Destruction™',
        'provenance': '[VI](../manifiestos/09_parasitismo_sistemico_ES_EN.md) + [LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) + [LXXIV](../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md)',
        'issue': 127,
    },
    22: {
        'es_title': 'Memoria Material-Relacional™',
        'en_title': 'Material-Relational Memory™',
        'provenance': '[LXXV](../manifiestos/75_las_hojas_carcomidas_memoria_natural_viracion_arquetipica_ES_EN.md)',
        'issue': 135,
    },
    23: {
        'es_title': 'Conservación del Fractal Común™',
        'en_title': 'Conservation of the Common Fractal™',
        'provenance': '[NeoMantis™ + documento C-NAX-23](../propuestas/sintesis-abierta/2026-08-15_C_NAX_23_CONSERVACION_FRACTAL_COMUN_ES_EN.md)',
        'issue': 148,
        'es': 'Ningún equilibrio legítimo puede construirse concediendo a una parte capacidad estable de destruir impunemente a otra parte necesaria del mismo sistema. La corrección de una asimetría debe aumentar la integridad del fractal común, no trasladar la licencia de degradación de un polo al otro.',
        'en': 'No legitimate equilibrium can be built by granting one part a stable capacity to destroy with impunity another part required by the same system. Correcting an asymmetry must increase the integrity of the common fractal, not transfer the licence to degrade from one pole to the other.',
        'formula_es': 'IGUAL DIGNIDAD\n+ DIFERENCIA REAL RECONOCIDA\n+ VULNERABILIDAD CONTEXTUAL\n+ PODER LIMITADO\n+ RESPONSABILIDAD PROPORCIONAL A POTENCIA\n+ CONTRADICCIÓN\n+ REPARACIÓN\n+ RECIPROCIDAD\n→ CONSERVACIÓN DEL FRACTAL COMÚN™',
        'formula_en': 'EQUAL DIGNITY\n+ RECOGNISED REAL DIFFERENCE\n+ CONTEXTUAL VULNERABILITY\n+ LIMITED POWER\n+ RESPONSIBILITY PROPORTIONAL TO CAPACITY\n+ CONTRADICTION\n+ REPAIR\n+ RECIPROCITY\n→ CONSERVATION OF THE COMMON FRACTAL™',
    },
    24: {
        'es_title': 'Diagnóstico ≠ Síntesis™',
        'en_title': 'Diagnosis ≠ Synthesis™',
        'provenance': '[LXXVI + documento C-NAX-24](../propuestas/sintesis-abierta/2026-08-15_C_NAX_24_DIAGNOSTICO_NO_ES_SINTESIS_ES_EN.md)',
        'issue': 149,
        'es': 'Detectar, describir, predecir o amplificar un problema no equivale a sintetizarlo. La autoridad de una propuesta no deriva de su visibilidad, prestigio o capacidad de alarma, sino de su capacidad para entrar en contraste, relacionarse con otras perspectivas, conservar genealogía, admitir corrección y contribuir a una respuesta común revisable.',
        'en': 'Detecting, describing, predicting or amplifying a problem is not the same as synthesising it. The authority of a proposal does not derive from visibility, prestige or capacity for alarm, but from its capacity to enter scrutiny, relate to other perspectives, preserve genealogy, admit correction and contribute to a revisable common response.',
        'formula_es': 'DIAGNÓSTICO ≠ SÍNTESIS\nVISIBILIDAD ≠ VERDAD\nPRESTIGIO ≠ SOBERANÍA\nALTAVOZ ≠ SOLUCIÓN',
        'formula_en': 'DIAGNOSIS ≠ SYNTHESIS\nVISIBILITY ≠ TRUTH\nPRESTIGE ≠ SOVEREIGNTY\nLOUDSPEAKER ≠ SOLUTION',
    },
}


def issue_link(n):
    return f'[{"#" + str(n)}]({REPO}/issues/{n})'


def build_table():
    lines = ['| Candidato / Candidate | Procedencia / Provenance | Estado / Status |', '|---|---|---|']
    for n, c in CANDIDATES.items():
        status = f'**Candidato explícito · SAN #{c["issue"]}**; no canonizado / **Explicit candidate · SAN #{c["issue"]}**; not canonicalised'
        lines.append(f'| **C-NAX-{n} · {c["es_title"]} / {c["en_title"]}** | {c["provenance"]} | {status} |')
    return '\n'.join(lines)


def build_detail(n):
    c = CANDIDATES[n]
    text = [
        f'### C-NAX-{n} · {c["es_title"]} / {c["en_title"]}', '',
        '**ES · formulación candidata:**', '',
        f'> **{c["es"]}**', ''
    ]
    if c.get('formula_es'):
        text += ['```text', c['formula_es'], '```', '']
    text += ['**EN · candidate formulation:**', '', f'> **{c["en"]}**', '']
    if c.get('formula_en'):
        text += ['```text', c['formula_en'], '```', '']
    text += [
        f'**Procedencia / Provenance:** {c["provenance"]}.  ',
        f'**Síntesis / Synthesis:** {issue_link(c["issue"])} · **CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**', ''
    ]
    if n in (15, 16):
        text += ['**Genealogía / Genealogy:** la formulación ya estaba explícita en la fuente de 2026-08-10; este bloque repara el registro central sin reiniciar su apertura pública. / the formulation was already explicit in the 2026-08-10 source; this block repairs the central registry without restarting its public opening.', '']
    elif n in (17, 18):
        text += ['**Genealogía / Genealogy:** formulación autónoma consolidada fielmente desde el principio ya publicado en la fuente; no altera su procedencia ni convierte el candidato en canon. / standalone formulation faithfully consolidated from the principle already published in the source; it neither changes provenance nor turns the candidate into canon.', '']
    return '\n'.join(text).rstrip()


def repair_neoaxioms():
    text = NEO.read_text(encoding='utf-8')
    start = '<!-- NEOAXIOM_CANDIDATES_72_START -->'
    end = '<!-- NEOAXIOM_CANDIDATES_72_END -->'
    if start not in text or end not in text:
        raise SystemExit('Candidate registry markers missing')
    block = text.split(start, 1)[1].split(end, 1)[0]

    table_match = re.search(r'\| Candidato / Candidate \| Procedencia / Provenance \| Estado / Status \|.*?(?=\n\n### C-NAX-)', block, re.S)
    if not table_match:
        raise SystemExit('Candidate table not found')
    block = block[:table_match.start()] + build_table() + block[table_match.end():]

    first_detail = re.search(r'^### C-NAX-19 ·', block, re.M)
    if not first_detail:
        raise SystemExit('C-NAX-19 detail boundary not found')
    prefix = '\n\n'.join(build_detail(n) for n in range(15, 19)) + '\n\n'
    block = block[:first_detail.start()] + prefix + block[first_detail.start():]

    for n in (23, 24):
        if not re.search(rf'^### C-NAX-{n} ·', block, re.M):
            block = block.rstrip() + '\n\n' + build_detail(n) + '\n'

    text = text.split(start, 1)[0] + start + block + end + text.split(end, 1)[1]
    text = re.sub(
        r'## Candidatos neoaxiomáticos detectados en el repaso I–[IVXLCDM]+ / Neoaxiomatic candidates detected in the I–[IVXLCDM]+ review',
        '## Candidatos neoaxiomáticos detectados en el repaso I–LXXVI / Neoaxiomatic candidates detected in the I–LXXVI review',
        text, count=1
    )
    NEO.write_text(text, encoding='utf-8')


def build_index_rows():
    rows = []
    relations = {
        15: f'{issue_link(150)} · [LXVIII #114]({REPO}/issues/114)',
        16: f'{issue_link(151)} · [∞ #106]({REPO}/issues/106) · [LXII #103]({REPO}/issues/103)',
        17: f'{issue_link(152)} · [LXVII #112]({REPO}/issues/112)',
        18: f'{issue_link(153)} · [LXVI #110]({REPO}/issues/110) · [LXVII #112]({REPO}/issues/112)',
        19: f'{issue_link(123)} · [matriz #80 / matrix #80]({REPO}/issues/80)',
        20: f'{issue_link(126)} · [LXXIII #124]({REPO}/issues/124)',
        21: f'{issue_link(127)} · [LXXIII #124]({REPO}/issues/124) · [LXXIV #125]({REPO}/issues/125)',
        22: f'{issue_link(135)} · [LXXV #134]({REPO}/issues/134)',
        23: f'{issue_link(148)} · [documento / document](2026-08-15_C_NAX_23_CONSERVACION_FRACTAL_COMUN_ES_EN.md)',
        24: f'{issue_link(149)} · [documento / document](2026-08-15_C_NAX_24_DIAGNOSTICO_NO_ES_SINTESIS_ES_EN.md)',
    }
    for n, c in CANDIDATES.items():
        rows.append(f'| **C-NAX-{n} · {c["es_title"]} / {c["en_title"]} · candidato / candidate** | {relations[n]} |')
    return '\n'.join(rows)


def repair_index():
    text = SYN.read_text(encoding='utf-8')
    text = re.sub(r'14 Neoaxiomas™ canónicos \+ \d+ candidatos C-NAX-15–C-NAX-\d+', '14 Neoaxiomas™ canónicos + 10 candidatos C-NAX-15–C-NAX-24', text)
    text = re.sub(r'14 canonical Neoaxioms™ \+ \d+ candidates C-NAX-15–C-NAX-\d+', '14 canonical Neoaxioms™ + 10 candidates C-NAX-15–C-NAX-24', text)
    text = re.sub(r'C-NAX-15–C-NAX-\d+', 'C-NAX-15–C-NAX-24', text)

    m = re.search(r'^\| \*\*C-NAX-15 .*?(?=\n\n\*\*Regla de estado / State rule:\*\*)', text, re.M | re.S)
    if not m:
        raise SystemExit('Candidate table in complete synthesis index not found')
    text = text[:m.start()] + build_index_rows() + text[m.end():]
    text = re.sub(
        r'\*\*Regla de estado / State rule:\*\* NAX-01–NAX-14 son canónicos y revisables; C-NAX-15–C-NAX-\d+ son candidatos visibles y trazables, no canónicos hasta fijación explícita posterior\. / NAX-01–NAX-14 are canonical and revisable; C-NAX-15–C-NAX-\d+ are visible, traceable candidates and remain non-canonical until a later explicit fixation\.',
        '**Regla de estado / State rule:** NAX-01–NAX-14 son canónicos y revisables; C-NAX-15–C-NAX-24 son candidatos visibles y trazables, no canónicos hasta fijación explícita posterior. / NAX-01–NAX-14 are canonical and revisable; C-NAX-15–C-NAX-24 are visible, traceable candidates and remain non-canonical until a later explicit fixation.',
        text
    )
    text = re.sub(r'C-NAX-15–C-NAX-22 permanecen candidatos', 'C-NAX-15–C-NAX-24 permanecen candidatos', text)
    text = re.sub(r'C-NAX-15–C-NAX-22 remain candidates', 'C-NAX-15–C-NAX-24 remain candidates', text)
    SYN.write_text(text, encoding='utf-8')


def repair_protocol():
    text = PROTOCOL.read_text(encoding='utf-8')
    anchor = '11. **NAX-11 · Autoridad de Fijación Humana y Síntesis Revisable™ / Human Fixation Authority and Revisable Synthesis™**'
    if anchor not in text:
        raise SystemExit('NAX-11 protocol anchor not found')
    marker = '\n\n## Estado vigente / Current state\n'
    if marker not in text:
        current = '''\n\n## Estado vigente / Current state\n\nLa lista anterior conserva la **primera activación pública de once formulaciones** como genealogía. El estado operativo vigente de la capa es: / The list above preserves the **first public activation of eleven formulations** as genealogy. The current operational state of the layer is:\n\n- **14 Neoaxiomas™ canónicos / canonical Neoaxioms™:** NAX-01–NAX-14.\n- **10 candidatos neoaxiomáticos / neoaxiomatic candidates:** C-NAX-15–C-NAX-24.\n- **Registro canónico de formulaciones / Canonical formulation registry:** [neoaxiomas/README.md](../../neoaxiomas/README.md).\n- **Índice completo de contraste / Complete scrutiny index:** [INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md](./INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md).\n- **Matriz general / General matrix:** [#80](''' + REPO + '''/issues/80).\n\nC-NAX-15–C-NAX-18 disponen desde esta reparación de formulación autónoma y Síntesis dedicada, recuperadas o consolidadas desde sus fuentes públicas originales; C-NAX-19–C-NAX-24 conservan sus formulaciones y rutas de contraste vigentes. Ningún C-NAX se convierte por ello en canon. / From this repair onward C-NAX-15–C-NAX-18 have standalone formulations and dedicated Synthesis nodes, recovered or consolidated from their original public sources; C-NAX-19–C-NAX-24 preserve their current formulations and scrutiny routes. No C-NAX becomes canonical by this repair.\n'''
        text = text.replace(anchor, anchor + current, 1)
    PROTOCOL.write_text(text, encoding='utf-8')


def patch_global_audit():
    text = GLOBAL_AUDIT.read_text(encoding='utf-8')
    sentinel = '# NEOAXIOM_REGISTRY_INTEGRITY_GATE'
    if sentinel not in text:
        text += f'''\n\n{sentinel}\n# The global ES/EN audit previously did not inspect the candidate registry placed before\n# the main # ES / # EN split in neoaxiomas/README.md. Keep a dedicated hard gate so a\n# C-NAX row can never again exist without a bilingual formulation block.\nimport subprocess as _neo_subprocess\nimport sys as _neo_sys\n_neo_subprocess.run([_neo_sys.executable, str(ROOT/'.github/scripts/audit_neoaxiom_registry_integrity.py')], check=True)\n'''
        GLOBAL_AUDIT.write_text(text, encoding='utf-8')

    wf = GLOBAL_WORKFLOW.read_text(encoding='utf-8')
    if 'audit_neoaxiom_registry_integrity.py' not in wf:
        wf = wf.replace("      - '.github/scripts/audit_global_bilingual_symmetry.py'\n", "      - '.github/scripts/audit_global_bilingual_symmetry.py'\n      - '.github/scripts/audit_neoaxiom_registry_integrity.py'\n")
        wf = wf.replace("          git add auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md\n", "          git add auditorias/publicas/2026-08-12_auditoria_global_simetria_ES_EN.md auditorias/publicas/2026-08-16_auditoria_neoaxiomas_simetria_frontera_ES_EN.md\n")
        GLOBAL_WORKFLOW.write_text(wf, encoding='utf-8')


def main():
    repair_neoaxioms()
    repair_index()
    repair_protocol()
    patch_global_audit()
    print('NEOAXIOM_REGISTRY_REPAIR_READY candidates=10 range=C-NAX-15..C-NAX-24')


if __name__ == '__main__':
    main()
