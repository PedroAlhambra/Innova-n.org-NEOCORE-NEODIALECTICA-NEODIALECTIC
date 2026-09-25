from pathlib import Path
import re
import sys
import json

MAN = Path('manifiestos')
README = MAN / 'README.md'
ISSUE_BASE = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/'


def roman_to_int(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = prev = 0
    for ch in reversed(s):
        v = vals[ch]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def first_titles(text):
    hs = re.findall(r'^#\s+([IVXLCDM]+)\s*·\s*(.+?)\s*$', text, re.M)
    if not hs:
        return None
    ordinal = hs[0][0]
    es = hs[0][1].strip()
    en = hs[1][1].strip() if len(hs) > 1 and hs[1][0] == ordinal else es
    return ordinal, es, en


def synthesis_issue(text):
    m = re.search(r'^\*\*Síntesis Abierta / Open Synthesis:\*\*.*?(?:/issues/|#)(\d+)', text, re.M)
    return int(m.group(1)) if m else None


def declared_canonical_route(text):
    m = re.search(r'ruta canónica actual es \[.*?\]\((?:\./)?([^)]+\.md)\)', text, re.I)
    if not m:
        m = re.search(r'current canonical path is \[.*?\]\((?:\./)?([^)]+\.md)\)', text, re.I)
    return Path(m.group(1)).name if m else None


registry = json.loads((MAN / 'CANONICAL_FILENAMES.json').read_text(encoding='utf-8'))['entries']
catalog = {}
for ord_, entry in registry.items():
    p = Path(entry['legacy'])
    if not p.exists():
        raise SystemExit(f'MANIFESTO_INDEX=FAIL registered source missing: {p}')
    text_source = p.read_text(encoding='utf-8')
    info = first_titles(text_source)
    if not info or info[0] != ord_:
        raise SystemExit(f'MANIFESTO_INDEX=FAIL registry/source ordinal mismatch: {ord_} -> {p}')
    _ord, es, en = info
    catalog[ord_] = {'path': p, 'es': es, 'en': en, 'issue': synthesis_issue(text_source)}

if not catalog:
    raise SystemExit('MANIFESTO_INDEX=FAIL empty canonical registry')

ordered = sorted(catalog, key=roman_to_int)
latest_ord = ordered[-1]
latest = catalog[latest_ord]
count = len(ordered)

text = README.read_text(encoding='utf-8')

issue_tail = ''
if latest['issue']:
    issue_tail = f' · [Síntesis Abierta {latest_ord} · #{latest["issue"]} / Open Synthesis {latest_ord} · #{latest["issue"]}]({ISSUE_BASE}{latest["issue"]})'
latest_block = (
    '> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n'
    f'> **{latest_ord} · {latest["es"]} / {latest["en"]}**\n>\n'
    f'> **[Manifiesto {latest_ord} / Manifesto {latest_ord}]({latest["path"].name}){issue_tail}**\n\n'
)
text, n = re.subn(
    r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n.*?(?=> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',
    latest_block,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('MANIFESTO_INDEX=FAIL latest block not found')

frontier = (
    f'**Frontera canónica vigente / Current canonical frontier:** **{count} manifiestos finitos bilingües · I–{latest_ord} + Manifiesto ∞ / '
    f'{count} finite bilingual manifestos · I–{latest_ord} + Manifesto ∞**  \n'
    '**Fecha de fijación de esta frontera / Frontier fixation date:** ' + (re.search(r'\*\*Fecha de fijación de esta frontera / Frontier fixation date:\*\*\s*(\d{4}-\d{2}-\d{2})', text).group(1) if re.search(r'\*\*Fecha de fijación de esta frontera / Frontier fixation date:\*\*\s*(\d{4}-\d{2}-\d{2})', text) else 'UNRESOLVED')
)
text, n = re.subn(
    r'\*\*Frontera canónica vigente / Current canonical frontier:\*\*.*?\n\*\*Fecha de fijación de esta frontera / Frontier fixation date:\*\*\s*\d{4}-\d{2}-\d{2}',
    frontier,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('MANIFESTO_INDEX=FAIL frontier not found')

lines = ['## Colección canónica / Canonical collection', '']
for ord_ in ordered:
    item = catalog[ord_]
    label = item['es'] if item['es'].casefold() == item['en'].casefold() else f'{item["es"]} / {item["en"]}'
    line = f'- **{ord_}** · [{label}]({item["path"].name})'
    if item['issue']:
        line += f' · [SAN #{item["issue"]}]({ISSUE_BASE}{item["issue"]})'
    lines.append(line)
lines.append('- **∞** · [Manifiesto de Neo0™ · Puerta Abierta del Fractal / Neo0™ Manifesto · Open Gate of the Fractal](INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)')
collection = '\n'.join(lines) + '\n\n'
text, n = re.subn(
    r'## Colección canónica / Canonical collection\n.*?(?=> Ningún manifiesto equivale por sí solo al marco completo\.)',
    collection,
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('MANIFESTO_INDEX=FAIL collection block not found')

text = re.sub(r'Índice completo I–[IVXLCDM]+ \+ ∞ \+ Neoaxiomas \+ sistema', f'Índice completo I–{latest_ord} + ∞ + Neoaxiomas + sistema', text)
text = re.sub(r'Complete index I–[IVXLCDM]+ \+ ∞ \+ Neoaxioms \+ system', f'Complete index I–{latest_ord} + ∞ + Neoaxioms + system', text)

latest_synth = f'**Última síntesis finita / Latest finite synthesis:** [{latest["es"]} / {latest["en"]}]({latest["path"].name})'
if latest['issue']:
    latest_synth += f' · [Issue #{latest["issue"]}]({ISSUE_BASE}{latest["issue"]})'
latest_synth += '  '
text = re.sub(r'^\*\*Última síntesis finita / Latest finite synthesis:\*\*.*$', latest_synth, text, count=1, flags=re.M)

README.write_text(text, encoding='utf-8')
print(f'MANIFESTO_INDEX=PASS finite={count} latest={latest_ord} issue={latest["issue"]} source=CANONICAL_FILENAMES.json')
