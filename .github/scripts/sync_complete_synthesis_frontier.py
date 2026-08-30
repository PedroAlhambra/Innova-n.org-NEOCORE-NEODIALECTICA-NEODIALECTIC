from __future__ import annotations

from datetime import date
from pathlib import Path
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
MANIFESTO_INDEX = MAN / 'README.md'
SYNTHESIS_INDEX = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
BASE_ISSUE_URL = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/'
COLLECTION_START = '## Colección canónica / Canonical collection'
COLLECTION_END = '> Ningún manifiesto equivale por sí solo al marco completo. / No single manifesto equals the complete framework.'
CANON_ROW = re.compile(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', re.M)
INDEX_ROW = re.compile(
    r'^\|\s*([IVXLCDM]+)\s*\|\s*\[([^\]]+)\]\((\.\./\.\./manifiestos/([^)]+\.md))\)\s*\|\s*'
    r'\[#(\d+)\]\((https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/\5)\)\s*\|$',
    re.M,
)
EXPLICIT_ISSUE = re.compile(
    r'\*\*Síntesis Abierta / Open Synthesis:\*\*\s*'
    r'\[#(\d+)\]\((https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/\1)\)'
)
TABLE_HEADER = '| Nº | Manifiesto / Manifesto | Síntesis / Synthesis |\n|---:|---|---|\n'
RULE_MARKER = '\n\n**Regla ∞ / ∞ rule:**'


def canonical_rows() -> list[tuple[str, str, Path]]:
    text = MANIFESTO_INDEX.read_text(encoding='utf-8')
    if COLLECTION_START not in text or COLLECTION_END not in text:
        raise SystemExit('CANONICAL_COLLECTION_BLOCK_UNRESOLVED')
    block = text.split(COLLECTION_START, 1)[1].split(COLLECTION_END, 1)[0]
    out: list[tuple[str, str, Path]] = []
    seen: set[str] = set()
    for roman, label, href in CANON_ROW.findall(block):
        if roman in seen:
            raise SystemExit(f'DUPLICATE_CANONICAL_ORDINAL={roman}')
        seen.add(roman)
        path = MAN / href
        if not path.exists():
            raise SystemExit(f'CANONICAL_MANIFESTO_MISSING={path.as_posix()}')
        out.append((roman, label.strip(), path))
    if not out:
        raise SystemExit('NO_CANONICAL_MANIFESTOS')
    return out


def existing_synthesis_map(text: str) -> dict[str, tuple[str, str, str]]:
    """Return only already explicit, internally coherent table mappings."""
    out: dict[str, tuple[str, str, str]] = {}
    for roman, _label, _href, filename, issue_num, issue_url in INDEX_ROW.findall(text):
        if roman in out:
            raise SystemExit(f'DUPLICATE_SYNTHESIS_INDEX_ORDINAL={roman}')
        out[roman] = (filename, issue_num, issue_url)
    return out


def resolve_issue(
    roman: str,
    path: Path,
    existing: dict[str, tuple[str, str, str]],
) -> tuple[str, str]:
    prior = existing.get(roman)
    if prior and prior[0] == path.name:
        return prior[1], prior[2]

    source = path.read_text(encoding='utf-8')
    explicit = EXPLICIT_ISSUE.search(source)
    if explicit:
        return explicit.group(1), explicit.group(2)

    if prior and prior[0] != path.name:
        raise SystemExit(
            f'SYNTHESIS_INDEX_TARGET_MISMATCH={roman}:index={prior[0]}:canonical={path.name}'
        )
    raise SystemExit(f'OPEN_SYNTHESIS_ISSUE_UNRESOLVED={roman}:{path.as_posix()}')


def sync() -> tuple[bool, list[tuple[str, str, Path, str, str]]]:
    canon = canonical_rows()
    text = SYNTHESIS_INDEX.read_text(encoding='utf-8').replace('\r\n', '\n')
    old = text
    existing = existing_synthesis_map(text)

    resolved: list[tuple[str, str, Path, str, str]] = []
    for roman, label, path in canon:
        issue_num, issue_url = resolve_issue(roman, path, existing)
        resolved.append((roman, label, path, issue_num, issue_url))

    count = len(resolved)
    latest_roman = resolved[-1][0]

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

    header_pos = text.find(TABLE_HEADER)
    rule_pos = text.find(RULE_MARKER, header_pos + len(TABLE_HEADER)) if header_pos >= 0 else -1
    if header_pos < 0 or rule_pos < 0:
        raise SystemExit('COMPLETE_SYNTHESIS_TABLE_UNRESOLVED')

    table_body = text[header_pos + len(TABLE_HEADER):rule_pos]
    inf = re.search(r'^\|\s*∞\s*\|.*$', table_body, re.M)
    if not inf:
        raise SystemExit('INFINITY_SYNTHESIS_ROW_UNRESOLVED')

    rows = [
        f'| {roman} | [{label}](../../manifiestos/{path.name}) | [#{issue_num}]({issue_url}) |'
        for roman, label, path, issue_num, issue_url in resolved
    ]
    rows.append(inf.group(0))
    rebuilt = TABLE_HEADER + '\n'.join(rows)
    text = text[:header_pos] + rebuilt + text[rule_pos:]

    post = existing_synthesis_map(text)
    for roman, _label, path, issue_num, issue_url in resolved:
        got = post.get(roman)
        expected = (path.name, issue_num, issue_url)
        if got != expected:
            raise SystemExit(f'SYNTHESIS_ROW_POSTCHECK_FAIL={roman}:got={got}:expected={expected}')

    if f'{count} manifiestos finitos I–{latest_roman} + Manifiesto ∞' not in text:
        raise SystemExit('SYNTHESIS_COVERAGE_ES_POSTCHECK_FAIL')
    if f'{count} finite manifestos I–{latest_roman} + Manifesto ∞' not in text:
        raise SystemExit('SYNTHESIS_COVERAGE_EN_POSTCHECK_FAIL')

    changed = text != old
    if changed:
        SYNTHESIS_INDEX.write_text(text, encoding='utf-8')
    return changed, resolved


def main() -> int:
    changed, resolved = sync()
    latest = resolved[-1]
    print(f'CANONICAL_MANIFESTOS={len(resolved)}')
    print(f'LATEST={latest[0]} ISSUE=#{latest[3]}')
    print(f'COMPLETE_SYNTHESIS_INDEX_CHANGED={changed}')
    print('POSTCHECK_OK: complete Open Synthesis index follows canonical manifesto frontier')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
