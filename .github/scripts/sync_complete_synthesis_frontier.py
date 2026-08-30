from __future__ import annotations

from datetime import date
from pathlib import Path
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
MANIFESTO_INDEX = MAN / 'README.md'
SYNTHESIS_INDEX = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

COLLECTION_START = '## Colección canónica / Canonical collection'
COLLECTION_END = '> Ningún manifiesto equivale por sí solo al marco completo. / No single manifesto equals the complete framework.'
ROW = re.compile(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', re.M)
EXPLICIT_ISSUE = re.compile(
    r'\*\*Síntesis Abierta / Open Synthesis:\*\*\s*'
    r'\[#(\d+)\]\((https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/\1)\)'
)
GENERIC_ISSUE = re.compile(
    r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)'
)
TABLE = re.compile(
    r'(\| Nº \| Manifiesto / Manifesto \| Síntesis / Synthesis \|\r?\n\|---:\|---\|---\|\r?\n).*?'
    r'(\r?\n\r?\n\*\*Regla ∞ / ∞ rule:\*\*)',
    re.S,
)
BASE_ISSUE_URL = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/'


def resolve_open_synthesis(source: str, roman: str, path: Path) -> tuple[str, str]:
    """Resolve SAN conservatively from manifesto-owned metadata.

    Newer manifestos use the explicit bilingual metadata field. Historical
    manifestos are accepted only when an Issue URL is present in their
    pre-body metadata (before `# ES ·`), matching the pre-existing frontier
    registration rule. We never infer an Issue from a related manifesto.
    """
    explicit = EXPLICIT_ISSUE.search(source)
    if explicit:
        return explicit.group(1), explicit.group(2)

    front = source.split('# ES ·', 1)[0]
    issue_numbers = GENERIC_ISSUE.findall(front)
    unique = list(dict.fromkeys(issue_numbers))
    if len(unique) == 1:
        issue_num = unique[0]
        return issue_num, BASE_ISSUE_URL + issue_num
    if len(unique) > 1:
        raise SystemExit(
            f'OPEN_SYNTHESIS_ISSUE_AMBIGUOUS={roman}:{path.as_posix()}:' + ','.join(unique)
        )
    raise SystemExit(f'OPEN_SYNTHESIS_ISSUE_UNRESOLVED={roman}:{path.as_posix()}')


def canonical_manifestos() -> list[tuple[str, str, Path, str, str]]:
    text = MANIFESTO_INDEX.read_text(encoding='utf-8')
    if COLLECTION_START not in text or COLLECTION_END not in text:
        raise SystemExit('CANONICAL_COLLECTION_BLOCK_UNRESOLVED')
    block = text.split(COLLECTION_START, 1)[1].split(COLLECTION_END, 1)[0]
    out: list[tuple[str, str, Path, str, str]] = []
    seen: set[str] = set()
    for roman, label, href in ROW.findall(block):
        if roman in seen:
            raise SystemExit(f'DUPLICATE_CANONICAL_ORDINAL={roman}')
        seen.add(roman)
        path = MAN / href
        if not path.exists():
            raise SystemExit(f'CANONICAL_MANIFESTO_MISSING={path.as_posix()}')
        source = path.read_text(encoding='utf-8')
        issue_num, issue_url = resolve_open_synthesis(source, roman, path)
        out.append((roman, label.strip(), path, issue_num, issue_url))
    if not out:
        raise SystemExit('NO_CANONICAL_MANIFESTOS')
    return out


def sync() -> bool:
    manifestos = canonical_manifestos()
    count = len(manifestos)
    latest_roman = manifestos[-1][0]
    text = SYNTHESIS_INDEX.read_text(encoding='utf-8')
    old = text

    text = re.sub(
        r'^\*\*Fecha / Date:\*\* \d{4}-\d{2}-\d{2}$',
        f'**Fecha / Date:** {date.today().isoformat()}',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r'\d+ manifiestos finitos I–[IVXLCDM]+ \+ Manifiesto ∞',
        f'{count} manifiestos finitos I–{latest_roman} + Manifiesto ∞',
        text,
        count=1,
    )
    text = re.sub(
        r'\d+ finite manifestos I–[IVXLCDM]+ \+ Manifesto ∞',
        f'{count} finite manifestos I–{latest_roman} + Manifesto ∞',
        text,
        count=1,
    )

    rows = []
    for roman, label, path, issue_num, issue_url in manifestos:
        rows.append(
            f'| {roman} | [{label}](../../manifiestos/{path.name}) | '
            f'[#{issue_num}]({issue_url}) |'
        )

    inf = re.search(r'^\|\s*∞\s*\|.*$', text, re.M)
    if not inf:
        raise SystemExit('INFINITY_SYNTHESIS_ROW_UNRESOLVED')
    rows.append(inf.group(0))

    replacement = r'\1' + '\n'.join(rows) + r'\2'
    text, replacements = TABLE.subn(replacement, text, count=1)
    if replacements != 1:
        raise SystemExit('COMPLETE_SYNTHESIS_TABLE_UNRESOLVED')

    for roman, _label, path, issue_num, issue_url in manifestos:
        expected_path = f'../../manifiestos/{path.name}'
        row_re = re.compile(
            rf'^\|\s*{re.escape(roman)}\s*\|.*\]\({re.escape(expected_path)}\).*'
            rf'\[#{re.escape(issue_num)}\]\({re.escape(issue_url)}\)\s*\|$',
            re.M,
        )
        if not row_re.search(text):
            raise SystemExit(f'SYNTHESIS_ROW_POSTCHECK_FAIL={roman}')

    if f'{count} manifiestos finitos I–{latest_roman} + Manifiesto ∞' not in text:
        raise SystemExit('SYNTHESIS_COVERAGE_ES_POSTCHECK_FAIL')
    if f'{count} finite manifestos I–{latest_roman} + Manifesto ∞' not in text:
        raise SystemExit('SYNTHESIS_COVERAGE_EN_POSTCHECK_FAIL')

    if text != old:
        SYNTHESIS_INDEX.write_text(text, encoding='utf-8')
        return True
    return False


def main() -> int:
    manifestos = canonical_manifestos()
    changed = sync()
    latest = manifestos[-1]
    print(f'CANONICAL_MANIFESTOS={len(manifestos)}')
    print(f'LATEST={latest[0]} ISSUE=#{latest[3]}')
    print(f'COMPLETE_SYNTHESIS_INDEX_CHANGED={changed}')
    print('POSTCHECK_OK: complete Open Synthesis index follows canonical manifesto frontier')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
