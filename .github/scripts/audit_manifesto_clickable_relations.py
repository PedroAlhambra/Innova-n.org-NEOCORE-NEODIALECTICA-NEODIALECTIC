from pathlib import Path
import re
import sys

MAN = Path('manifiestos')
files = sorted(MAN.glob('[0-9][0-9]_*.md'))
inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
if inf.exists():
    files.append(inf)

failures = []
relation_lines = 0
synthesis_lines = 0


def remove_md_links(s):
    # Remove already navigable relations entirely before looking for raw leftovers.
    return re.sub(r'\[[^\]]+\]\([^)]+\)', '', s)


for p in files:
    text = p.read_text(encoding='utf-8')
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.startswith('**Relaciones principales / Main relations:**'):
            relation_lines += 1
            raw = line.split(':**', 1)[-1]
            residual = remove_md_links(raw)
            missing = set()

            # Modern raw relation: `II · Title`.
            missing.update(re.findall(r'(?<![A-Z])([IVXLCDM]+|∞)\s*·', residual))
            # Legacy raw list: `XIV, XVI, ...` (only at list boundaries, not words such as MÉDICI).
            missing.update(re.findall(r'(?:^|,)\s*([IVXLCDM]+|∞)\s*(?=,|·|$)', residual))

            if missing:
                failures.append(f'{p}:{lineno}: MAIN_RELATIONS_NOT_CLICKABLE: {sorted(missing)}')

        if line.startswith('**Síntesis Abierta / Open Synthesis:**'):
            synthesis_lines += 1
            issue_numbers = set(re.findall(r'#(\d+)\b', line))
            issue_numbers |= set(re.findall(r'/issues/(\d+)', line))
            if issue_numbers:
                linked = set(re.findall(r'\[[^\]]*#(\d+)[^\]]*\]\(https://github\.com/[^)]+/issues/\1\)', line))
                missing = sorted(issue_numbers - linked, key=int)
                if missing:
                    failures.append(f'{p}:{lineno}: OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE: {missing}')

for p in files:
    text = p.read_text(encoding='utf-8')
    if '<!-- NEO_CROSS_REFERENCES_START -->' not in text or '<!-- NEO_CROSS_REFERENCES_END -->' not in text:
        failures.append(f'{p}: CANONICAL_CROSSREF_BLOCK_MISSING')

if failures:
    print('CLICKABLE_RELATIONS=FAIL')
    for item in failures:
        print(item)
    sys.exit(1)

print(f'CLICKABLE_RELATIONS=PASS manifests={len(files)} relation_lines={relation_lines} synthesis_lines={synthesis_lines}')
