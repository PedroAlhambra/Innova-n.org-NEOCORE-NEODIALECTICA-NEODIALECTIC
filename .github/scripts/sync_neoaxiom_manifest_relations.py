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
    print("NEOAXIOM_MANIFEST_RELATIONS_SYNCED NAX-01..NAX-14")
