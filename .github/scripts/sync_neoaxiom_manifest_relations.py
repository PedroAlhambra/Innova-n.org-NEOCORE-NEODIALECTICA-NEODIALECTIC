from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
NEO = ROOT / "neoaxiomas"
README = NEO / "README.md"

START = "<!-- NEOAXIOM_MANIFEST_RELATIONS_START -->"
END = "<!-- NEOAXIOM_MANIFEST_RELATIONS_END -->"

# Relaciones documentales/conceptuales explícitas. NO son una declaración de
# procedencia exclusiva ni de causalidad. El objetivo es hacer navegable la red
# NAX <-> Manifiestos sin confundir relación con fuente genealógica.
REL = {
    "NAX-01": [
        ("I", "Manifiesto Neo0™ de la Soberanía de Guía Neodialéctica", "Neo0™ Manifesto of Neodialectical Guiding Sovereignty", "11_neo0_soberania_de_guia_ES_EN.md"),
        ("IV", "Manifiesto de la Neodialéctica™ y el Bien Común", "Manifesto of Neodialectics™ and the Common Good", "02_neodialectica_bien_comun_ES_EN.md"),
        ("XLV", "Multidimensionalidad Neodialéctica™", "Neodialectical Multidimensionality™", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"),
    ],
    "NAX-02": [
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
        ("XLV", "Multidimensionalidad Neodialéctica™", "Neodialectical Multidimensionality™", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"),
        ("LIX", "Custodia Cognitiva Distribuida™", "Distributed Cognitive Custody™", "59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md"),
    ],
    "NAX-03": [
        ("II", "Síntesis Abierta Neodialéctica™", "Neodialectical Open Synthesis™", "01_sintesis_abierta_neodialectica_ES_EN.md"),
        ("XLV", "Multidimensionalidad Neodialéctica™", "Neodialectical Multidimensionality™", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"),
    ],
    "NAX-04": [
        ("II", "Síntesis Abierta Neodialéctica™", "Neodialectical Open Synthesis™", "01_sintesis_abierta_neodialectica_ES_EN.md"),
        ("XLV", "Multidimensionalidad Neodialéctica™", "Neodialectical Multidimensionality™", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"),
    ],
    "NAX-05": [
        ("II", "Síntesis Abierta Neodialéctica™", "Neodialectical Open Synthesis™", "01_sintesis_abierta_neodialectica_ES_EN.md"),
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
    ],
    "NAX-06": [
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
        ("XIX", "Persistencia de la Memoria™", "Persistence of Memory™", "19_persistencia_de_la_memoria_ES_EN.md"),
    ],
    "NAX-07": [
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
        ("X", "WEB4™ · SistemaTrazable™", "WEB4™ · SistemaTrazable™", "07_web4_sistematrazable_ES_EN.md"),
        ("LIX", "Custodia Cognitiva Distribuida™", "Distributed Cognitive Custody™", "59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md"),
    ],
    "NAX-08": [
        ("IV", "Neodialéctica™ y Bien Común", "Neodialectics™ and the Common Good", "02_neodialectica_bien_comun_ES_EN.md"),
        ("VII", "Economía del Aporte", "Contribution Economy", "04_economia_del_aporte_ES_EN.md"),
    ],
    "NAX-09": [
        ("XVII", "Respeto a Todos los Seres Vivos™", "Respect for All Living Beings™", "17_respeto_todos_seres_vivos_ES_EN.md"),
        ("XLV", "Multidimensionalidad Neodialéctica™", "Neodialectical Multidimensionality™", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"),
    ],
    "NAX-10": [
        ("I", "Soberanía de Guía Neodialéctica", "Neodialectical Guiding Sovereignty", "11_neo0_soberania_de_guia_ES_EN.md"),
        ("XVI", "Refragmentación Arquetípica™", "Archetypal Refragmentation™", "16_refragmentacion_arquetipica_ES_EN.md"),
    ],
    "NAX-11": [
        ("I", "Soberanía de Guía Neodialéctica", "Neodialectical Guiding Sovereignty", "11_neo0_soberania_de_guia_ES_EN.md"),
        ("II", "Síntesis Abierta Neodialéctica™", "Neodialectical Open Synthesis™", "01_sintesis_abierta_neodialectica_ES_EN.md"),
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
    ],
    "NAX-12": [
        ("IX", "Memoria, Genealogía y Trazabilidad", "Memory, Genealogy and Traceability", "06_memoria_genealogia_trazabilidad_ES_EN.md"),
        ("X", "WEB4™ · SistemaTrazable™", "WEB4™ · SistemaTrazable™", "07_web4_sistematrazable_ES_EN.md"),
    ],
    "NAX-13": [
        ("VII", "Economía del Aporte", "Contribution Economy", "04_economia_del_aporte_ES_EN.md"),
        ("XXIII", "Soberanía del Tiempo Cognitivo™", "Sovereignty of Cognitive Time™", "23_soberania_tiempo_cognitivo_ES_EN.md"),
    ],
    "NAX-14": [
        ("V", "Simbiosis Humano–IA", "Human–AI Symbiosis", "03_simbiosis_humano_ia_ES_EN.md"),
        ("XIV", "Contra la Alienación Humana™", "Against Human Alienation™", "14_contra_alienacion_humana_ES_EN.md"),
        ("LIX", "Custodia Cognitiva Distribuida™", "Distributed Cognitive Custody™", "59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md"),
    ],
}


# NAX-15–NAX-29: relaciones recuperadas de sus propios documentos ya publicados.
# No crea relaciones doctrinales nuevas; sólo normaliza la misma red tras la
# fijación procedimental del backlog C-NAX-15–C-NAX-29.
EXTRA_REL_FILES = {
    "NAX-15": ["68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md"],
    "NAX-16": ["62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md", "INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md"],
    "NAX-17": ["67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md"],
    "NAX-18": ["66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md", "67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md"],
    "NAX-19": ["69_defensa_inocencia_humana_asimetria_protectora_deber_custodia_ES_EN.md", "70_fauno_masculinidad_fragmentada_depredacion_relacional_retorno_hombre_ES_EN.md", "71_libertad_sexual_hipersexualizacion_industrial_separacion_planos_ES_EN.md", "72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md"],
    "NAX-20": ["73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md"],
    "NAX-21": ["09_parasitismo_sistemico_ES_EN.md", "73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md", "74_asimetria_destruccion_trol_humano_bot_ES_EN.md"],
    "NAX-22": ["75_las_hojas_carcomidas_memoria_natural_viracion_arquetipica_ES_EN.md"],
    "NAX-23": ["73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md", "74_asimetria_destruccion_trol_humano_bot_ES_EN.md", "76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md"],
    "NAX-24": ["01_sintesis_abierta_neodialectica_ES_EN.md", "22_contra_reduccion_captura_intelectual_ES_EN.md", "35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md", "68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md", "76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md"],
    "NAX-25": ["22_contra_reduccion_captura_intelectual_ES_EN.md", "35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md", "42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md", "63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md", "76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md", "77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md"],
    "NAX-26": ["53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md", "72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md", "74_asimetria_destruccion_trol_humano_bot_ES_EN.md", "77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md"],
    "NAX-27": ["01_sintesis_abierta_neodialectica_ES_EN.md", "04_economia_del_aporte_ES_EN.md", "07_web4_sistematrazable_ES_EN.md", "11_neo0_soberania_de_guia_ES_EN.md", "38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md", "56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md", "58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md", "62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md", "69_defensa_inocencia_humana_asimetria_protectora_deber_custodia_ES_EN.md"],
    "NAX-28": ["11_neo0_soberania_de_guia_ES_EN.md", "16_refragmentacion_arquetipica_ES_EN.md", "45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md"],
    "NAX-29": ["86_federacion_neodialectica_network_framework_ES_EN.md"],
}

def _manifest_titles(filename):
    path = ROOT / "manifiestos" / filename
    headings = [x[2:].strip() for x in path.read_text(encoding="utf-8", errors="replace").splitlines() if x.startswith("# ")][:2]
    if len(headings) < 2:
        raise RuntimeError(f"Missing bilingual titles in {filename}")
    def clean(x):
        return re.sub(r"^(?:[IVXLCDM]+|∞)\s+·\s+", "", x)
    return clean(headings[0]), clean(headings[1])

for _ident, _files in EXTRA_REL_FILES.items():
    _items=[]
    for _filename in _files:
        _path=ROOT / "manifiestos" / _filename
        _head=next((x[2:].strip() for x in _path.read_text(encoding="utf-8", errors="replace").splitlines() if x.startswith("# ")), "")
        _m=re.match(r"^([IVXLCDM]+|∞)\s+·\s+", _head)
        if not _m:
            raise RuntimeError(f"Cannot resolve manifesto ordinal for {_filename}")
        _es,_en=_manifest_titles(_filename)
        _items.append((_m.group(1),_es,_en,_filename))
    REL[_ident]=_items


MANIFEST_REL_START = "<!-- NEO_MANIFEST_NEOAXIOM_RELATIONS_START -->"
MANIFEST_REL_END = "<!-- NEO_MANIFEST_NEOAXIOM_RELATIONS_END -->"

def _manifest_neo_block(items):
    rows=[]
    for ident, filename in sorted(items, key=lambda x:int(x[0].split('-')[1])):
        path=NEO/filename
        heads=[x[2:].strip() for x in path.read_text(encoding="utf-8", errors="replace").splitlines() if re.match(r"^# NAX-\d+ ·",x)][:2]
        es=heads[0].split(" · ",1)[1]; en=heads[1].split(" · ",1)[1]
        rows.append(f"- [{ident} · {es} / {en}](../neoaxiomas/{filename})")
    return f"""{MANIFEST_REL_START}

## Relaciones neoaxiomáticas recíprocas / Reciprocal Neoaxiomatic relations

> **Relación documental/conceptual, no identidad ni causalidad.** Este bloque es la inversa navegable de las relaciones NAX→Manifiesto y mantiene simetría de navegación. / **Documentary/conceptual relation, not identity or causality.** This block is the navigable inverse of NAX→Manifesto relations and preserves navigational symmetry.

{chr(10).join(rows)}

{MANIFEST_REL_END}
"""

def update_manifest_reciprocity():
    reverse={}
    for ident, rels in REL.items():
        filename=DOC_NAMES[ident]
        for _,_,_,manifest in rels:
            reverse.setdefault(manifest,[]).append((ident,filename))
    pattern=re.compile(re.escape(MANIFEST_REL_START)+r".*?"+re.escape(MANIFEST_REL_END)+r"\n?",re.S)
    changed=[]
    for manifest,items in sorted(reverse.items()):
        path=ROOT/"manifiestos"/manifest
        old=path.read_text(encoding="utf-8")
        block=_manifest_neo_block(items)
        if pattern.search(old):
            new=pattern.sub(block.rstrip()+"\n",old)
        else:
            marker="<!-- NEO_CROSS_REFERENCES_START -->"
            if marker in old:
                new=old.replace(marker,block+"\n"+marker,1)
            else:
                new=old.rstrip()+"\n\n"+block
        if new!=old:
            path.write_text(new,encoding="utf-8"); changed.append(manifest)
    return changed

DOC_NAMES = {
    "NAX-01": "NAX-01_UNIDAD_SENTIDO_DISTRIBUCION_POTENCIA_ES_EN.md",
    "NAX-02": "NAX-02_PRIMERA_CAPA_FRACTAL_MULTICABEZA_ES_EN.md",
    "NAX-03": "NAX-03_NO_HOMOGENEIZACION_PREVIA_ES_EN.md",
    "NAX-04": "NAX-04_DOBLE_PIRAMIDE_FRACTAL_ES_EN.md",
    "NAX-05": "NAX-05_DIFERENCIAL_MONADICO_RETORNO_FUENTE_ES_EN.md",
    "NAX-06": "NAX-06_MEMORIA_AUSENCIA_ES_EN.md",
    "NAX-07": "NAX-07_RED_NEOREAL_ACTORES_OPERATIVOS_ES_EN.md",
    "NAX-08": "NAX-08_COOPERACION_EXCELENCIA_COMPETENCIA_DEPREDADORA_ES_EN.md",
    "NAX-09": "NAX-09_COMPUTACION_DISTRIBUIDA_LOCAL_VERIFICACION_ECOLOGICA_ES_EN.md",
    "NAX-10": "NAX-10_GRAMATICA_ARQUETIPICA_CUSTODIA_ES_EN.md",
    "NAX-11": "NAX-11_AUTORIDAD_FIJACION_HUMANA_SINTESIS_REVISABLE_ES_EN.md",
    "NAX-12": "NAX-12_TRAZABILIDAD_SUSTITUTIVA_BUROCRACIA_REDUNDANTE_ES_EN.md",
    "NAX-13": "NAX-13_LIBERACION_TIEMPO_CONTROL_CREACION_APORTE_ES_EN.md",
    "NAX-14": "NAX-14_PREVENCION_BIFURCACION_SIMBIOTICA_ES_EN.md",
}


for _n in range(15,30):
    _matches=list(NEO.glob(f"NAX-{_n}_*_ES_EN.md"))
    if len(_matches) != 1:
        raise RuntimeError(f"NAX-{_n}: expected one current document, found {_matches}")
    DOC_NAMES[f"NAX-{_n}"]=_matches[0].name

def links(ident, from_readme=False):
    prefix = "../manifiestos/" if from_readme else "../manifiestos/"
    return " · ".join(
        f"[{roman} · {es} / {en}]({prefix}{path})"
        for roman, es, en, path in REL[ident]
    )


def block(ident):
    items = "\n".join(
        f"- [{roman} · {es} / {en}](../manifiestos/{path})"
        for roman, es, en, path in REL[ident]
    )
    return f"""{START}

## Relaciones con manifiestos / Relations with Manifestos

> **Relación documental/conceptual, no procedencia exclusiva.** Estos vínculos hacen explícita la red vigente del Neoaxioma con manifiestos que desarrollan, aplican, limitan o contextualizan su función. Un enlace no declara identidad, subordinación ni causalidad. / **Documentary/conceptual relation, not exclusive provenance.** These links make explicit the Neoaxiom's current network with Manifestos that develop, apply, limit or contextualise its function. A link does not assert identity, subordination or causality.

{items}

{END}
"""


def replace_managed(text, new_block):
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
    if pat.search(text):
        return pat.sub(new_block.rstrip() + "\n", text)
    marker = "**Síntesis / Synthesis:**"
    if marker not in text:
        raise RuntimeError("No synthesis marker in neoaxiom document")
    return text.replace(marker, new_block + "\n" + marker, 1)


def update_docs():
    for ident, filename in DOC_NAMES.items():
        path = NEO / filename
        if not path.exists():
            raise RuntimeError(f"Missing canonical Neoaxiom document: {path}")
        for _, _, _, manifest in REL[ident]:
            target = ROOT / "manifiestos" / manifest
            if not target.exists():
                raise RuntimeError(f"Missing manifesto target for {ident}: {target}")
        old = path.read_text(encoding="utf-8")
        new = replace_managed(old, block(ident))
        if new != old:
            path.write_text(new, encoding="utf-8")


def update_readme():
    text = README.read_text(encoding="utf-8")
    # Both ES and EN fixed-NAX tables use the same Markdown row shape. Keep
    # NAX name -> own document, then state/SAN, then explicit manifesto links.
    text = text.replace("| Neoaxioma | Estado | SAN |\n|---|---|---|", "| Neoaxioma | Estado | SAN | Manifiestos relacionados / Related Manifestos |\n|---|---|---|---|")
    text = text.replace("| Neoaxiom | Status | Synthesis |\n|---|---|---|", "| Neoaxiom | Status | Synthesis | Related Manifestos / Manifiestos relacionados |\n|---|---|---|---|")

    lines = []
    row_re = re.compile(r"^\| \[\*\*(NAX-\d{2}) ·")
    for line in text.splitlines():
        m = row_re.match(line)
        if m and m.group(1) in REL:
            ident = m.group(1)
            # Normalize an existing 4th column if the script is rerun.
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 3:
                line = "| " + " | ".join(cells[:3] + [links(ident, from_readme=True)]) + " |"
        lines.append(line)
    README.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    update_docs()
    update_readme()
    changed = update_manifest_reciprocity()
    print(f"NEOAXIOM_MANIFEST_RELATIONS_SYNCED NAX-01..NAX-{max(int(x.split('-')[1]) for x in DOC_NAMES)} reciprocal_manifests={len(changed)}")
