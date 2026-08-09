from pathlib import Path
import re

root = Path('.').resolve()
index = root / 'manifiestos/README.md'
synth = root / 'propuestas/sintesis-abierta/README.md'

idx = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
# The main synchronizer may rewrite the managed block before this normalizer runs.
# Prefer the canonical block when present, but fall back to the complete index text.
source = net.group(1) if net else idx

items = re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', source)
seen = set(); canonical = []
for roman, href in items:
    p = (index.parent / href).resolve()
    if p in seen or not p.exists():
        continue
    seen.add(p); canonical.append((roman, p))

if not canonical:
    raise SystemExit('No canonical manifestos found in manifiestos/README.md')
count = len(canonical)
last = canonical[-1][0]

s = synth.read_text(encoding='utf-8')
s = re.sub(r'\*\*Cobertura canónica / Canonical coverage:\*\* \*\*\d+ manifiestos · I–[IVXLCDM]+ / \d+ manifestos · I–[IVXLCDM]+\*\*',
           f'**Cobertura canónica / Canonical coverage:** **{count} manifiestos · I–{last} / {count} manifestos · I–{last}**', s)
s = re.sub(r'^## Índice canónico · I–[IVXLCDM]+$', f'## Índice canónico · I–{last}', s, flags=re.M)
s = re.sub(r'Open Synthesis currently covers \*\*\d+ bilingual manifestos I–[IVXLCDM]+\*\*',
           f'Open Synthesis currently covers **{count} bilingual manifestos I–{last}**', s)

latest_name = canonical[-1][1].name
if latest_name not in s:
    raise SystemExit(f'Latest manifesto missing from Open Synthesis index: {latest_name}')

synth.write_text(s, encoding='utf-8')
print(f'NORMALIZED: {count} manifestos I–{last}; synthesis index aligned')
