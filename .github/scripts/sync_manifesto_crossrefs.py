from pathlib import Path
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
START = '<!-- NEO_CROSS_REFERENCES_START -->'
END = '<!-- NEO_CROSS_REFERENCES_END -->'
LEGACY_START = '<!-- NEO_CANONICAL_CROSSREFS_START -->'
LEGACY_END = '<!-- NEO_CANONICAL_CROSSREFS_END -->'


def roman_to_int(s):
    if s == '∞':
        return 10**9
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = prev = 0
    for ch in reversed(s):
        v = vals.get(ch, 0)
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def strip_generated(text):
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\s*', '', text, flags=re.S)
    text = re.sub(re.escape(LEGACY_START) + r'.*?' + re.escape(LEGACY_END) + r'\s*', '', text, flags=re.S)
    return text


def first_titles(text):
    hs = re.findall(r'^#\s+([IVXLCDM]+|∞)\s*·\s*(.+?)\s*$', text, re.M)
    if not hs:
        return None
    ordinal = hs[0][0]
    es = hs[0][1].strip()
    en = hs[1][1].strip() if len(hs) > 1 and hs[1][0] == ordinal else es
    return ordinal, es, en


def display_title(es, en):
    a = es.strip(); b = en.strip()
    if not b or a.casefold() == b.casefold():
        return a
    if b.casefold() in a.casefold() or a.casefold() in b.casefold():
        return a if len(a) >= len(b) else b
    return f'{a} / {b}'


files = sorted(MAN.glob('[0-9][0-9]_*.md'))
inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
if inf.exists():
    files.append(inf)

catalog = {}
path_to_ord = {}
for p in files:
    text = p.read_text(encoding='utf-8')
    info = first_titles(text)
    if not info:
        continue
    ordinal, es, en = info
    catalog[ordinal] = {'path': p, 'es': es, 'en': en}
    path_to_ord[p.name] = ordinal

ALIASES = {
    'Síntesis Abierta Neodialéctica': 'II', 'Neodialectical Open Synthesis': 'II',
    'Derecho Humano de Aporte': 'III', 'Human Right to Contribute': 'III',
    'Economía del Aporte': 'VII', 'Contribution Economy': 'VII',
    'Memoria, Genealogía y Trazabilidad': 'IX', 'Memory, Genealogy and Traceability': 'IX',
    'WEB4': 'X', 'SistemaTrazable': 'X', 'NeoPandora': 'XIII',
    'Refragmentación Arquetípica': 'XVI', 'Archetypal Refragmentation': 'XVI',
    'Persistencia de la Memoria': 'XIX', 'Persistence of Memory': 'XIX',
    'UMBRAL-X': 'XX', 'Umbral-X': 'XX',
    'Reconocimiento Neodialéctico': 'XXI', 'Neodialectical Recognition': 'XXI',
    'Soberanía del Tiempo Cognitivo': 'XXIII', 'Sovereignty of Cognitive Time': 'XXIII',
    'Pulido de la Piedra': 'XXV', 'Polishing of the Stone': 'XXV',
    'Los Tesla': 'XXVIII', 'The Teslas': 'XXVIII',
    'Idolatría del Dinero': 'XXIX', 'Idolatry of Money': 'XXIX',
    'Honor Relacional': 'XL', 'Relational Honor': 'XL', 'Neowar': 'XLIV',
    'Multidimensionalidad Neodialéctica': 'XLV', 'Neodialectical Multidimensionality': 'XLV',
    'Cerrar la Herida': 'XLVI', 'Close the Wound': 'XLVI', 'Closing the Wound': 'XLVI',
    'La Síntesis Todo lo Ve': 'XLVIII', 'Synthesis Sees Everything': 'XLVIII',
    'Leónidas': 'LIII', 'Leonidas': 'LIII', 'NO-CONTROL': 'LVI',
    'Inteligencia Civilizatoria': 'LVIII', 'Civilisational Intelligence': 'LVIII',
    'Custodia Cognitiva Distribuida': 'LIX', 'Distributed Cognitive Custodianship': 'LIX',
    'Relevancia Humana Necesaria': 'LX', 'Necessary Human Relevance': 'LX',
    'Custodia Experimental Multiescalar': 'LXI', 'Multiscale Experimental Custodianship': 'LXI',
    'Juego por la Síntesis y el Honor': 'LXII', 'Game for Synthesis and Honor': 'LXII',
    'Simplificación Burda': 'LXIII', 'Crude Simplification': 'LXIII',
    'NeoCronos': 'LXIV', 'NeoJuego': 'LXV', 'NeoGame': 'LXV',
    'NeoSinergia': 'LXVI', 'NeoSynergy': 'LXVI',
    'MÉDICI': 'LXVI', 'MEDICI': 'LXVI',
    'NeoGalaxia': 'LXVI', 'NeoGalaxy': 'LXVI',
    'pensamiento de Andrómeda': 'LXVI', 'thought from Andromeda': 'LXVI',
    'NeoTitanes': 'LXVII', 'NeoTitans': 'LXVII',
    'Soberanía Intelectual de la Especie': 'LXVIII', 'Intellectual Sovereignty of the Species': 'LXVIII',
    'Defensa de la Inocencia Humana': 'LXIX', 'Defence of Human Innocence': 'LXIX',
    'Fauno': 'LXX', 'Faun': 'LXX',
    'Separación de Planos': 'LXXI', 'Separation of Planes': 'LXXI',
    'Hipersexualización Industrial': 'LXXI', 'Industrial Hypersexualisation': 'LXXI',
    'Hombre Custodio': 'LXXII', 'Custodian Man': 'LXXII',
}

SPECIAL_DOCS = [
    (re.compile(r'\bIDEA\b'), 'IDEA · obra / work', '../obras/idea/README.md'),
    (re.compile(r'\b(?:Neoaxiomas?|Neoaxioms?|(?:C-)?NAX-\d{2})\b', re.I), 'Neoaxiomas™ / Neoaxioms™', '../neoaxiomas/README.md'),
    (re.compile(r'\bNEOCore™?\b', re.I), 'NEOCore™ · marco / framework', '../README.md'),
]

DEDICATED_SYNTHESIS = {
    'LXIX': 119,
    'LXX': 120,
    'LXXI': 121,
    'LXXII': 122,
}


def detect_refs(text, own_ord):
    refs = set()
    for ord_ in re.findall(r'\b([IVXLCDM]+)\s*·', text):
        if ord_ in catalog and ord_ != own_ord:
            refs.add(ord_)
    for ord_ in re.findall(r'\b(?:Manifiesto|Manifesto)\s+([IVXLCDM]+)\b', text, re.I):
        ord_ = ord_.upper()
        if ord_ in catalog and ord_ != own_ord:
            refs.add(ord_)
    for m in re.finditer(r'^\*\*Relaciones principales / Main relations:\*\*\s*(.+)$', text, re.M):
        for ord_ in re.findall(r'(?<![A-Z])(?:[IVXLCDM]+|∞)(?![A-Z])', m.group(1)):
            if ord_ in catalog and ord_ != own_ord:
                refs.add(ord_)
    for target in re.findall(r'\((?:\./)?([^/()]+\.md)(?:#[^)]*)?\)', text):
        ord_ = path_to_ord.get(Path(target).name)
        if ord_ and ord_ != own_ord:
            refs.add(ord_)
    low = text.casefold()
    for alias, ord_ in ALIASES.items():
        if ord_ != own_ord and alias.casefold() in low and ord_ in catalog:
            refs.add(ord_)
    return refs


def neoaxiom_ids(text):
    found = set(m.upper() for m in re.findall(r'\b(?:C-)?NAX-\d{2}\b', text, re.I))
    def key(s):
        return (1 if s.startswith('C-') else 0, int(re.search(r'\d+', s).group()))
    return sorted(found, key=key)


def block_for(text, own_ord):
    refs = detect_refs(text, own_ord)
    lines = [
        START, '',
        '## Referencias cruzadas canónicas / Canonical cross-references', '',
        '> **Norma / Rule:** las menciones cruzadas pueden permanecer en el cuerpo como texto para no sobrecargar la lectura; este bloque concentra los hipervínculos canónicos detectados y permite retorno explícito a fuente. / Cross-references may remain as prose in the body to avoid visual overload; this block concentrates detected canonical hyperlinks and preserves explicit return to source.', ''
    ]
    if refs:
        for ord_ in sorted(refs, key=roman_to_int):
            item = catalog[ord_]
            rel = './' + item['path'].name
            label = display_title(item['es'], item['en'])
            lines.append(f'- **{ord_}** · [{label}]({rel})')
    else:
        lines.append('- Sin referencias cruzadas a otros manifiestos detectadas / No cross-references to other manifestos detected.')

    specials = []
    for rx, label, href in SPECIAL_DOCS:
        if rx.search(text):
            specials.append((label, href))
    if specials:
        lines += ['', '### Capas y fuentes relacionadas / Related layers and sources', '']
        seen = set()
        for label, href in specials:
            if href not in seen:
                lines.append(f'- [{label}]({href})')
                seen.add(href)

    naxes = neoaxiom_ids(text)
    if naxes:
        lines += ['', '**Neoaxiomas mencionados / Mentioned Neoaxioms:** ' + ' · '.join(f'`{n}`' for n in naxes) + ' → [Neoaxiomas™](../neoaxiomas/README.md)']

    issue = DEDICATED_SYNTHESIS.get(own_ord)
    if issue:
        lines += [
            '', '### Síntesis y delta / Synthesis and delta', '',
            f'- [Síntesis Abierta {own_ord} / Open Synthesis {own_ord} · #{issue}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue})',
            '- [C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™ / Relational Inviolability and Separation of Planes™ · #123](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/123)',
            '- [Delta relacional íntegro / Full relational delta](../propuestas/sintesis-abierta/2026-08-11_DELTA_DEFENSA_INOCENCIA_FAUNO_SEPARACION_PLANOS_HOMBRE_CUSTODIO_ES_EN.md)',
        ]

    lines += ['', END, '']
    return '\n'.join(lines)

changed = []
for p in files:
    original = p.read_text(encoding='utf-8')
    clean = strip_generated(original).rstrip() + '\n\n'
    info = first_titles(clean)
    if not info:
        continue
    own_ord = info[0]
    new = clean + block_for(clean, own_ord)
    if new != original:
        p.write_text(new, encoding='utf-8')
        changed.append(p.as_posix())

print(f'CROSSREF_SYNC manifests={len(files)} changed={len(changed)}')
for p in changed:
    print(p)
