from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path('.')
MAN_REG = ROOT / 'manifiestos' / 'CANONICAL_FILENAMES.json'
SYN = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'


def roman_to_int(s: str) -> int:
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        v = vals[ch]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


reg = json.loads(MAN_REG.read_text(encoding='utf-8'))['entries']
romans = sorted(reg, key=roman_to_int)
finite_count = len(romans)
last_roman = romans[-1]

nax_ids = sorted({int(m.group(1)) for p in (ROOT / 'neoaxiomas').glob('NAX-*.md') if (m := re.match(r'NAX-(\d+)_', p.name))})
cnax_ids = sorted({int(m.group(1)) for p in (ROOT / 'neoaxiomas').glob('C-NAX-*.md') if (m := re.match(r'C-NAX-(\d+)_', p.name))})
if not nax_ids or not cnax_ids:
    raise SystemExit('FRONTIER_DISCOVERY_FAILURE: missing NAX/C-NAX own documents')
canon_nax_count = len([n for n in nax_ids if n <= 14])
candidate_count = len(cnax_ids)
candidate_first, candidate_last = min(cnax_ids), max(cnax_ids)

text = SYN.read_text(encoding='utf-8')
original = text

coverage = (
    f'**Cobertura / Coverage:** **{finite_count} manifiestos finitos I–{last_roman} + Manifiesto ∞ · '
    f'{canon_nax_count} Neoaxiomas™ canónicos + {candidate_count} candidatos C-NAX-{candidate_first}–C-NAX-{candidate_last} · '
    f'síntesis transversales, auditorías y proyectos de sistema / {finite_count} finite manifestos I–{last_roman} + Manifesto ∞ · '
    f'{canon_nax_count} canonical Neoaxioms™ + {candidate_count} candidates C-NAX-{candidate_first}–C-NAX-{candidate_last} · '
    'cross-cutting syntheses, audits and system projects**.'
)
text = re.sub(r'^\*\*Cobertura / Coverage:\*\*.*$', coverage, text, count=1, flags=re.M)

text = re.sub(
    r'- Todo manifiesto finito I–[IVXLCDM]+ dispone de una Síntesis Abierta dedicada\. / Every finite manifesto I–[IVXLCDM]+ has a dedicated Open Synthesis issue\.',
    f'- Todo manifiesto finito I–{last_roman} dispone de una Síntesis Abierta dedicada. / Every finite manifesto I–{last_roman} has a dedicated Open Synthesis issue.',
    text,
)
text = re.sub(
    r'- C-NAX-\d+–C-NAX-\d+ permanecen candidatos: se muestran con matriz/ruta de síntesis y no se elevan automáticamente a canon\. / C-NAX-\d+–C-NAX-\d+ remain candidates: they are shown with a synthesis matrix/route and are not automatically elevated to canon\.',
    f'- C-NAX-{candidate_first}–C-NAX-{candidate_last} permanecen candidatos: se muestran con matriz/ruta de síntesis y no se elevan automáticamente a canon. / C-NAX-{candidate_first}–C-NAX-{candidate_last} remain candidates: they are shown with a synthesis matrix/route and are not automatically elevated to canon.',
    text,
)

# Gate: the complete index must actually carry every current manifesto and candidate row.
missing_manifestos = [r for r in romans if not re.search(rf'^\|\s*{re.escape(r)}\s*\|', text, flags=re.M)]
missing_candidates = [n for n in cnax_ids if not re.search(rf'C-NAX-{n}\b', text)]
if missing_manifestos or missing_candidates:
    raise SystemExit(f'FRONTIER_TABLE_FAILURE manifestos={missing_manifestos} candidates={missing_candidates}')

if text != original:
    SYN.write_text(text, encoding='utf-8')
    print(f'FRONTIER_RECONCILED finite={finite_count} last={last_roman} candidates={candidate_first}-{candidate_last}')
else:
    print(f'FRONTIER_ALREADY_CURRENT finite={finite_count} last={last_roman} candidates={candidate_first}-{candidate_last}')
