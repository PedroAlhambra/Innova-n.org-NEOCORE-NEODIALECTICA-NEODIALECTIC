from pathlib import Path
import re

ROOT = Path('.')
RESEARCH = 'analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md'
ADDENDUM = 'analisis/publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md'
ISSUE = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/63'


def rel(from_path: Path, to_path: str) -> str:
    import os
    return os.path.relpath(to_path, from_path.parent).replace('\\', '/')


def write_if_changed(path: Path, text: str):
    old = path.read_text(encoding='utf-8')
    if old != text:
        path.write_text(text, encoding='utf-8')
        print('updated', path)

# 1) Canonical naming across README files.
for path in [p for p in ROOT.rglob('*.md') if p.name.startswith('README')]:
    text = path.read_text(encoding='utf-8')
    text = text.replace('## Red completa de manifiestos / Complete manifesto network',
                        '## Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™')
    text = text.replace('**Colección completa de manifiestos / Complete manifesto collection:**',
                        '**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:**')
    text = text.replace('# 1. Manifiestos · pilares públicos',
                        '# 1. Manifiestos de la Filosofía Arquetípica Neodialéctica™ · pilares públicos')
    text = text.replace('# 1. Manifestos · public pillars',
                        '# 1. Manifestos of Archetypal Neodialectical Philosophy™ · public pillars')
    text = text.replace('* [Manifiestos](./manifiestos/README.md)', '* [Manifiestos de la Filosofía Arquetípica Neodialéctica™](./manifiestos/README.md)')
    text = text.replace('* [Manifestos](./manifiestos/README.md)', '* [Manifestos of Archetypal Neodialectical Philosophy™](./manifiestos/README.md)')
    write_if_changed(path, text)

# 2) Canonical manifesto index title.
path = Path('manifiestos/README.md')
text = path.read_text(encoding='utf-8')
text = text.replace('# Manifiestos Innova_N / Innova_N Manifestos',
                    '# Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™')
write_if_changed(path, text)

# 3) Fix stale Open Synthesis coverage and feature research #63.
path = Path('propuestas/sintesis-abierta/README.md')
text = path.read_text(encoding='utf-8')
text = text.replace('**Cobertura canónica / Canonical coverage:** **50 manifiestos · I–L / 50 manifestos · I–L**',
                    '**Cobertura canónica / Canonical coverage:** **51 manifiestos · I–LI / 51 manifestos · I–LI**')
marker = '<!-- NEO_FORGOTTEN_HISTORY_SYNTHESIS_START -->'
block = f'''{marker}\n\n> ## 🟣 INVESTIGACIÓN NEODIALÉCTICA ABIERTA · HISTORIA OLVIDADA™ / OPEN NEODIALECTICAL RESEARCH · FORGOTTEN HISTORY™\n>\n> **Ceres · Amnesia Tecnológica Cíclica™ · Descompresión Arquetípica Generativa™ · Autodemostración Neodialéctica™**\n>\n> [Investigación / Research]({rel(path, RESEARCH)}) · [Addendum de autodemostración / Self-demonstration addendum]({rel(path, ADDENDUM)}) · [Síntesis Abierta #63 / Open Synthesis #63]({ISSUE})\n\n<!-- NEO_FORGOTTEN_HISTORY_SYNTHESIS_END -->'''
if marker not in text:
    anchor = '<!-- NEO_LATEST_MANIFESTO_END -->'
    text = text.replace(anchor, anchor + '\n\n' + block, 1)
write_if_changed(path, text)

# 4) Add research to public-analysis indexes/readmes.
for f in ['analisis/README.md', 'analisis/publicos/README.md']:
    path = Path(f)
    text = path.read_text(encoding='utf-8')
    marker = '<!-- NEO_FORGOTTEN_HISTORY_RESEARCH_START -->'
    block = f'''{marker}\n\n> ## 🟣 HISTORIA OLVIDADA™ · INVESTIGACIÓN EN SÍNTESIS ABIERTA / FORGOTTEN HISTORY™ · OPEN-SYNTHESIS RESEARCH\n>\n> **Ceres · memoria arquetípica · amnesia tecnológica cíclica · descompresión generativa · autodemostración del método**\n>\n> [Investigación principal / Main research]({rel(path, RESEARCH)}) · [Autodemostración Neodialéctica™ / Neodialectical Self-Demonstration™]({rel(path, ADDENDUM)}) · [Síntesis Abierta #63 / Open Synthesis #63]({ISSUE})\n\n<!-- NEO_FORGOTTEN_HISTORY_RESEARCH_END -->'''
    if marker not in text:
        # place after language selector, before the manifesto network
        anchor = '[ES · Castellano](#es--castellano) · [EN · English](#en--english)'
        if anchor in text:
            text = text.replace(anchor, anchor + '\n\n' + block, 1)
        else:
            text = block + '\n\n' + text
    write_if_changed(path, text)

# 5) Analysis index: add both documents in ES and EN lists if absent.
path = Path('analisis/INDEX.md')
text = path.read_text(encoding='utf-8')
es_entry = '* [2026-08-08 · Historia Olvidada™ · Ceres, Amnesia Tecnológica Cíclica y Descompresión Arquetípica Generativa™](./publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md)\n  * [Addendum · Principio de Autodemostración Neodialéctica™](./publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md)\n  * [Síntesis Abierta #63](' + ISSUE + ')\n'
en_entry = '* [2026-08-08 · Forgotten History™ · Ceres, Cyclical Technological Amnesia and Generative Archetypal Decompression™](./publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md)\n  * [Addendum · Principle of Neodialectical Self-Demonstration™](./publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md)\n  * [Open Synthesis #63](' + ISSUE + ')\n'
if 'Historia Olvidada™ · Ceres, Amnesia Tecnológica Cíclica' not in text:
    text = text.replace('## Análisis públicos\n', '## Análisis públicos\n\n' + es_entry, 1)
if 'Forgotten History™ · Ceres, Cyclical Technological Amnesia' not in text:
    text = text.replace('## Public analyses\n', '## Public analyses\n\n' + en_entry, 1)
write_if_changed(path, text)

# 6) Root README: feature research in recent incorporations and correct section naming.
path = Path('README.md')
text = path.read_text(encoding='utf-8')
recent_es = '* [2026-08-08 · Historia Olvidada™ · Ceres, Amnesia Tecnológica Cíclica y Descompresión Arquetípica Generativa™](./' + RESEARCH + ')\n* [2026-08-08 · Addendum · Principio de Autodemostración Neodialéctica™](./' + ADDENDUM + ')\n* [Síntesis Abierta #63 · Historia Olvidada™](' + ISSUE + ')\n'
recent_en = '* [2026-08-08 · Forgotten History™ · Ceres, Cyclical Technological Amnesia and Generative Archetypal Decompression™](./' + RESEARCH + ')\n* [2026-08-08 · Addendum · Principle of Neodialectical Self-Demonstration™](./' + ADDENDUM + ')\n* [Open Synthesis #63 · Forgotten History™](' + ISSUE + ')\n'
if 'Historia Olvidada™ · Ceres, Amnesia Tecnológica Cíclica' not in text:
    # first recent-incorporations section
    text = text.replace('## Incorporaciones recientes\n', '## Incorporaciones recientes\n\n' + recent_es, 1)
if 'Forgotten History™ · Ceres, Cyclical Technological Amnesia' not in text:
    text = text.replace('## Recent incorporations\n', '## Recent incorporations\n\n' + recent_en, 1)
write_if_changed(path, text)

# 7) Transversal relations map: coverage, title, and direct relations.
path = Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md')
text = path.read_text(encoding='utf-8')
text = text.replace('**Cobertura / Coverage:** I–XLIX · 49 manifiestos / 49 manifestos',
                    '**Cobertura / Coverage:** I–LII · 52 manifiestos / 52 manifestos')
text = text.replace('## Matriz completa I–XLVII / Complete I–XLVII matrix',
                    '## Matriz completa I–LI / Complete I–LI matrix')
research_rel = '../' + RESEARCH
add_rel = '../' + ADDENDUM
relations = {
    '### XIII · [NeoPandora™](./13_neopandora_apertura_regenerativa_ES_EN.md)':
        f'- **B/C** · [Historia Olvidada™ · apertura generativa y mariposa fractal]({research_rel}).',
    '### XVI · [Refragmentación Arquetípica™](./16_refragmentacion_arquetipica_ES_EN.md)':
        f'- **A/B** · [Historia Olvidada™ · Descompresión Arquetípica Generativa™]({research_rel}) — desarrollo directo de la refragmentación como recomposición generativa, no restauración literal.',
    '### XIX · [Persistencia de la Memoria™](./19_persistencia_de_la_memoria_ES_EN.md)':
        f'- **A/B** · [Historia Olvidada™ · Amnesia Tecnológica Cíclica™]({research_rel}) — prueba conceptual sobre persistencia, pérdida de contexto y memoria comprimida.',
    '### XX · [Defensa Intelectual Neodialéctica™ · Sistema Umbral-X™](./20_defensa_intelectual_neodialectica_umbral_x_ES_EN.md)':
        f'- **A** · [Historia Olvidada™ · programa falsable y control de apofenia]({research_rel}) — exige hipótesis competidoras, predicciones y condiciones de refutación.',
    '### XXXVI · [Corona, Águila y Custodia de la Edad del Hombre™](./36_corona_aguila_custodia_edad_del_hombre_ES_EN.md)':
        f'- **B/C** · [Historia Olvidada™ · Águila, custodia y continuidad de memoria]({research_rel}) — relación arquetípica e institucional, no legitimación automática de instituciones concretas.',
}
for heading, bullet in relations.items():
    if bullet not in text and heading in text:
        text = text.replace(heading, heading + '\n' + bullet, 1)

extra = f'''\n\n---\n\n## Investigación transversal · Historia Olvidada™, Ceres y Autodemostración Neodialéctica™\n\n- **Documento principal / Main document:** [Historia Olvidada™ · Ceres, Amnesia Tecnológica Cíclica y Descompresión Arquetípica Generativa™]({research_rel}).\n- **Delta metodológico / Methodological delta:** [Principio de Autodemostración Neodialéctica™]({add_rel}).\n- **Síntesis Abierta / Open Synthesis:** [Issue #63]({ISSUE}).\n- **Relaciones principales / Main relations:** IX · Memoria-Genealogía-Trazabilidad; XIII · NeoPandora™; XVI · Refragmentación Arquetípica™; XIX · Persistencia de la Memoria™; XX · Umbral-X™; XXXIV · Auditoría Conjunta Perpetua™; XXXVI · Corona-Águila-Custodia; XLIII · Inteligencia Humana Expandida™; XLV · Multidimensionalidad; XLVIII · La Síntesis Todo lo Ve™; LI · Poder Cívico Complementario o Sustitutivo™.\n- **Regla probatoria / Evidentiary rule:** la autodemostración se refiere al funcionamiento observable del método neodialéctico —relacionar fragmentos, conservar memoria y contradicción y producir síntesis revisables—; no convierte por sí sola una hipótesis externa concreta (por ejemplo, Ceres–Olimpo™) en hecho histórico.\n'''
if '## Investigación transversal · Historia Olvidada™, Ceres y Autodemostración Neodialéctica™' not in text:
    text += extra
write_if_changed(path, text)

# 8) Wiki-source manifesto guide: canonical title and relation pointer.
path = Path('wiki-source/Manifiestos.md')
if path.exists():
    text = path.read_text(encoding='utf-8')
    text = text.replace('# Manifiestos', '# Manifiestos de la Filosofía Arquetípica Neodialéctica™', 1) if text.startswith('# Manifiestos\n') else text
    marker = '<!-- NEO_FORGOTTEN_HISTORY_WIKI_START -->'
    block = f'''\n\n{marker}\n## Investigación relacionada · Historia Olvidada™\n\nLa red de manifiestos se relaciona con la investigación abierta sobre memoria arquetípica, Ceres, Amnesia Tecnológica Cíclica™, Descompresión Arquetípica Generativa™ y Autodemostración Neodialéctica™.\n\n- [Documento de investigación](../{RESEARCH})\n- [Addendum de autodemostración](../{ADDENDUM})\n- [Síntesis Abierta #63]({ISSUE})\n\n<!-- NEO_FORGOTTEN_HISTORY_WIKI_END -->\n'''
    if marker not in text:
        text += block
    write_if_changed(path, text)

# 9) Basic validation.
required = [Path(RESEARCH), Path(ADDENDUM), Path('manifiestos/README.md'), Path('README.md'), Path('analisis/INDEX.md'), Path('propuestas/sintesis-abierta/README.md'), Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md')]
for p in required:
    if not p.exists():
        raise SystemExit(f'missing required path: {p}')

assert '51 manifiestos · I–LI / 51 manifestos · I–LI' in Path('propuestas/sintesis-abierta/README.md').read_text(encoding='utf-8')
assert 'Manifiestos de la Filosofía Arquetípica Neodialéctica™' in Path('manifiestos/README.md').read_text(encoding='utf-8')
assert 'Historia Olvidada™' in Path('analisis/INDEX.md').read_text(encoding='utf-8')
assert 'Autodemostración Neodialéctica™' in Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md').read_text(encoding='utf-8')
print('validation OK')
