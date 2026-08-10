from pathlib import Path
import re

root = Path('.').resolve()
index = root / 'manifiestos/README.md'
synth = root / 'propuestas/sintesis-abierta/README.md'

idx = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
# The managed network block is a compact summary and may intentionally omit
# the itemised list. Always recover the canonical item list from the complete
# index when the compact block does not contain entries.
source = net.group(1) if net else idx
items = re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', source)
if not items:
    items = re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', idx)

seen = set(); canonical = []
for roman, title, href in items:
    p = (index.parent / href).resolve()
    if p in seen or not p.exists():
        continue
    seen.add(p)
    canonical.append((roman, title.strip(), p))

if not canonical:
    raise SystemExit('No canonical manifestos found in manifiestos/README.md')

last, latest_title, latest_path = canonical[-1]
count = len(canonical)
latest_name = latest_path.name

s = synth.read_text(encoding='utf-8')

# Normalise all explicit current-coverage surfaces without touching historical
# statements whose wording does not claim to be current.
s = re.sub(
    r'\*\*Cobertura canónica / Canonical coverage:\*\* \*\*\d+ manifiestos · I–[IVXLCDM]+ / \d+ manifestos · I–[IVXLCDM]+\*\*',
    f'**Cobertura canónica / Canonical coverage:** **{count} manifiestos · I–{last} / {count} manifestos · I–{last}**',
    s,
)
s = re.sub(
    r'\*\*Cobertura actual / Current coverage:\*\* \*\*\d+ manifiestos finitos · I–[IVXLCDM]+ \+ Manifiesto ∞ · 14 Neoaxiomas™ · síntesis transversales, auditorías y proyectos / \d+ finite manifestos · I–[IVXLCDM]+ \+ Manifesto ∞ · 14 Neoaxioms™ · transversal syntheses, audits and projects\*\*',
    f'**Cobertura actual / Current coverage:** **{count} manifiestos finitos · I–{last} + Manifiesto ∞ · 14 Neoaxiomas™ · síntesis transversales, auditorías y proyectos / {count} finite manifestos · I–{last} + Manifesto ∞ · 14 Neoaxioms™ · transversal syntheses, audits and projects**',
    s,
)
s = re.sub(r'^## Índice canónico · I–[IVXLCDM]+$', f'## Índice canónico · I–{last}', s, flags=re.M)
s = re.sub(
    r'Open Synthesis currently covers \*\*\d+ bilingual manifestos I–[IVXLCDM]+\*\*',
    f'Open Synthesis currently covers **{count} bilingual manifestos I–{last}**',
    s,
)

# The old index used a manually written “latest finite manifesto” block whose
# heading differs from the generic synchroniser. Repair it here rather than
# failing merely because a new manifesto was added.
latest_text = latest_path.read_text(encoding='utf-8')
issue_match = re.search(
    r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',
    latest_text,
)
issue_num = issue_match.group(1) if issue_match else {
    'LVII':'77', 'LVIII':'78', 'LIX':'79',
    'LX':'99', 'LXI':'101', 'LXII':'103', 'LXIII':'105',
    'LXIV':'107', 'LXV':'109', 'LXVI':'110', 'LXVII':'112', 'LXVIII':'114',
}.get(last)
if not issue_num:
    raise SystemExit(f'Cannot resolve Open Synthesis issue for {last}')

issue_url = f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue_num}'
latest_block = f'''> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS
>
> **{last} · {latest_title}**
>
> **[Leer {last} / Read {last}](../../manifiestos/{latest_name}) · [Síntesis {last} · #{issue_num} / Synthesis {last} · #{issue_num}]({issue_url})**
'''

finite_block_re = re.compile(
    r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>.*?(?=\n> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',
    re.S,
)
if finite_block_re.search(s):
    s = finite_block_re.sub(latest_block.rstrip() + '\n', s, count=1)
elif latest_name not in s:
    infinity_marker = '> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR'
    if infinity_marker in s:
        s = s.replace(infinity_marker, latest_block + '\n' + infinity_marker, 1)
    else:
        raise SystemExit('Cannot place latest finite manifesto in Open Synthesis index')

if latest_name not in s:
    raise SystemExit(f'Latest manifesto missing from Open Synthesis index after repair: {latest_name}')

synth.write_text(s, encoding='utf-8')
print(f'NORMALIZED: {count} manifestos I–{last}; latest={latest_name}; synthesis index aligned')
