from __future__ import annotations

from datetime import date
from pathlib import Path
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
README = MAN / 'README.md'
START = '<!-- NEO_CROSS_REFERENCES_START -->'
END = '<!-- NEO_CROSS_REFERENCES_END -->'
HEADING = '## Referencias cruzadas canónicas / Canonical cross-references'


def latest_manifesto() -> tuple[int, Path]:
    candidates = []
    for path in MAN.glob('[0-9][0-9]_*.md'):
        m = re.match(r'^(\d{2})_', path.name)
        if m:
            candidates.append((int(m.group(1)), path))
    if not candidates:
        raise SystemExit('NO_NUMBERED_MANIFESTOS')
    return max(candidates, key=lambda item: item[0])


def ensure_crossref_markers(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    if START in text and END in text:
        return False
    pos = text.find(HEADING)
    if pos < 0:
        print(f'LATEST_CROSSREF_HEADING_MISSING={path}')
        return False
    text = text[:pos] + START + '\n\n' + text[pos:]
    after = text.find('\n## ', pos + len(START) + len(HEADING))
    if after < 0:
        text = text.rstrip() + '\n\n' + END + '\n'
    else:
        text = text[:after] + '\n\n' + END + text[after:]
    path.write_text(text, encoding='utf-8')
    return True


def reconcile_readme(number: int, path: Path) -> bool:
    text = README.read_text(encoding='utf-8')
    source = path.read_text(encoding='utf-8')
    lines = source.splitlines()
    if len(lines) < 2:
        raise SystemExit('LATEST_MANIFESTO_HEADER_INCOMPLETE')
    m_es = re.match(r'^#\s+([IVXLCDM]+)\s+·\s+(.+)$', lines[0])
    m_en = re.match(r'^#\s+([IVXLCDM]+)\s+·\s+(.+)$', lines[1])
    issue = re.search(r'\*\*Síntesis Abierta / Open Synthesis:\*\*\s*\[#(\d+)\]\((https://github\.com/[^)]+/issues/\1)\)', source)
    if not (m_es and m_en and issue):
        raise SystemExit('LATEST_MANIFESTO_METADATA_UNRESOLVED')
    roman = m_es.group(1)
    if m_en.group(1) != roman:
        raise SystemExit('LATEST_MANIFESTO_ROMAN_MISMATCH')
    es_title = m_es.group(2)
    en_title = m_en.group(2)
    issue_num, issue_url = issue.group(1), issue.group(2)

    current = re.search(r'\*\*Frontera canónica vigente / Current canonical frontier:\*\* \*\*(\d+) manifiestos finitos', text)
    current_num = int(current.group(1)) if current else -1
    if current_num == number and f'**{roman} · {es_title} / {en_title}**' in text:
        return False

    latest_block = (
        '> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n'
        f'> **{roman} · {es_title} / {en_title}**\n>\n'
        f'> **[Manifiesto {roman} / Manifesto {roman}]({path.name}) · '
        f'[Síntesis Abierta {roman} · #{issue_num} / Open Synthesis {roman} · #{issue_num}]({issue_url})**\n\n'
    )
    pattern = re.compile(
        r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n.*?(?=> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',
        re.S,
    )
    if not pattern.search(text):
        raise SystemExit('README_LATEST_BLOCK_UNRESOLVED')
    text = pattern.sub(latest_block, text, count=1)

    frontier_line = (
        f'**Frontera canónica vigente / Current canonical frontier:** **{number} manifiestos finitos bilingües · '
        f'I–{roman} + Manifiesto ∞ / {number} finite bilingual manifestos · I–{roman} + Manifesto ∞**  '
    )
    text, count = re.subn(
        r'\*\*Frontera canónica vigente / Current canonical frontier:\*\* \*\*.*?\*\*  ',
        frontier_line,
        text,
        count=1,
    )
    if count != 1:
        raise SystemExit('README_FRONTIER_LINE_UNRESOLVED')
    text = re.sub(
        r'\*\*Fecha de fijación de esta frontera / Frontier fixation date:\*\* \d{4}-\d{2}-\d{2}',
        f'**Fecha de fijación de esta frontera / Frontier fixation date:** {date.today().isoformat()}',
        text,
        count=1,
    )
    README.write_text(text, encoding='utf-8')
    return True


def main() -> int:
    number, path = latest_manifesto()
    marker_change = ensure_crossref_markers(path)
    readme_change = reconcile_readme(number, path)
    print(f'LATEST_MANIFESTO={number}:{path}')
    print(f'LATEST_CROSSREF_MARKERS_CHANGED={marker_change}')
    print(f'README_FRONTIER_CHANGED={readme_change}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
