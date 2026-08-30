from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
CANON = MAN / 'CANONICAL_FILENAMES.json'

REGISTRY = json.loads(CANON.read_text(encoding='utf-8'))
ENTRIES = REGISTRY.get('entries', {})
VALID_NUMERALS = set(ENTRIES)

RELATION_PREFIXES = (
    '**Relación genealógica / Genealogical relation:**',
    '**Genealogía / Genealogy:**',
    '**Relaciones principales / Main relations:**',
    '**Relaciones raíz / Root relations:**',
)

LINK_RE = re.compile(r'\[[^\]]+\]\([^)]+\)')
ROMAN_RE = re.compile(r'(?<![A-Z0-9-])([IVXLCDM]+|∞)(?![A-Z0-9-])')


def manifest_files() -> list[Path]:
    paths: set[Path] = set(MAN.glob('[0-9][0-9]_*.md'))
    paths.update((MAN / 'canonicos').glob('*_ES_EN.md'))
    inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
    if inf.exists():
        paths.add(inf)
    return sorted(paths)


def href_for(path: Path, numeral: str) -> str | None:
    entry = ENTRIES.get(numeral)
    if not entry:
        return None
    canonical = ROOT / entry['canonical']
    try:
        return canonical.relative_to(path.parent).as_posix()
    except ValueError:
        return canonical.as_posix()


def link_segment(path: Path, segment: str) -> str:
    def repl(match: re.Match[str]) -> str:
        numeral = match.group(1)
        if numeral not in VALID_NUMERALS:
            return numeral
        href = href_for(path, numeral)
        return f'[{numeral}]({href})' if href else numeral
    return ROMAN_RE.sub(repl, segment)


def repair_line(path: Path, line: str) -> str:
    if not line.startswith(RELATION_PREFIXES):
        return line
    out: list[str] = []
    pos = 0
    for match in LINK_RE.finditer(line):
        out.append(link_segment(path, line[pos:match.start()]))
        out.append(match.group(0))
        pos = match.end()
    out.append(link_segment(path, line[pos:]))
    return ''.join(out)


changed: list[str] = []
for path in manifest_files():
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)
    repaired = []
    dirty = False
    for raw in lines:
        ending = '\n' if raw.endswith('\n') else ''
        body = raw[:-1] if ending else raw
        fixed = repair_line(path, body)
        if fixed != body:
            dirty = True
        repaired.append(fixed + ending)
    if dirty:
        path.write_text(''.join(repaired), encoding='utf-8')
        changed.append(path.as_posix())

print(f'REPAIRED_MANIFEST_RELATIONAL_FILES={len(changed)}')
for item in changed:
    print(item)
