from pathlib import Path
import re

root = Path('.').resolve()
index = root / 'manifiestos/README.md'
synth = root / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

idx = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
# The managed network block may be compact. Recover the canonical item list
# from the complete manifesto index when needed.
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
latest_text = latest_path.read_text(encoding='utf-8')
issue_match = re.search(
    r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',
    latest_text,
)
if not issue_match:
    raise SystemExit(f'Cannot resolve Open Synthesis issue for {last}')
issue_num = issue_match.group(1)

s = synth.read_text(encoding='utf-8')

# This file is the canonical complete inventory. Update only its explicitly
# current coverage surface; preserve candidate/audit/project wording already
# maintained by their own synchronisers.
s, n = re.subn(
    r'(\*\*Cobertura / Coverage:\*\* \*\*)\d+ manifiestos finitos I–[IVXLCDM]+( \+ Manifiesto ∞.*? / )\d+ finite manifestos I–[IVXLCDM]+( \+ Manifesto ∞.*?\*\*)',
    rf'\g<1>{count} manifiestos finitos I–{last}\g<2>{count} finite manifestos I–{last}\g<3>',
    s,
    count=1,
)
if n == 0:
    raise SystemExit('Cannot locate current coverage line in complete Open Synthesis index')

# register_manifesto_frontier.py owns insertion of new finite rows. Here we
# verify that the complete index actually contains the current frontier and
# its associated Synthesis issue instead of trying to recreate another table.
row_re = re.compile(
    r'^\|\s*' + re.escape(last) + r'\s*\|.*?' + re.escape(latest_name) +
    r'.*?issues/' + re.escape(issue_num) + r'.*?\|\s*$',
    re.M,
)
if not row_re.search(s):
    raise SystemExit(
        f'Complete Open Synthesis index missing current frontier row: {last} {latest_name} issue #{issue_num}'
    )
if not re.search(r'^\|\s*∞\s*\|', s, re.M):
    raise SystemExit('Complete Open Synthesis index missing permanent ∞ row')

synth.write_text(s, encoding='utf-8')
print(
    f'NORMALIZED: complete synthesis index aligned with {count} manifestos I–{last}; '
    f'latest={latest_name}; issue=#{issue_num}'
)
