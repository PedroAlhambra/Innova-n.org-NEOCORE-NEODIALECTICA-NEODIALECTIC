from __future__ import annotations

from pathlib import Path
import json
import os
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
CANON = MAN / 'CANONICAL_FILENAMES.json'
NEOAX = ROOT / 'neoaxiomas'
PREFIXES = (
    '**Relaciones principales / Main relations:**',
    '**Relaciones raíz / Root relations:**',
    '**Relación genealógica / Genealogical relation:**',
)

# Historical repair debris: [label](href)](href)
DUP_SUFFIX_RE = re.compile(r'(\[[^\]]+\]\(([^)]+)\))\]\(\2\)')
# Same href repeated after bilingual/prose continuation:
# [X · ES](href) / EN](href) -> [X · ES / EN](href)
EXTENDED_SUFFIX_RE = re.compile(r'\[([IVXLCDM]+\s*·\s*[^\]]+)\]\(([^)]+)\)([^,\n]*?)\]\(\2\)')
# Nested same-target link: [outer [inner](href)](href)
NESTED_SAME_RE = re.compile(r'\[([^\[\]]*?)\[([^\]]+)\]\(([^)]+)\)([^\[\]]*?)\]\(\3\)')
NEOAX_ID_RE = re.compile(r'(?<![A-Z0-9-])(C-NAX-\d+|NAX-\d+)(?![A-Z0-9-])')


def rel(source: Path, target: Path) -> str:
    return Path(os.path.relpath(target, start=source.parent)).as_posix()


def neoax_link(source: Path, ident: str) -> str:
    target = NEOAX / ('NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md' if ident == 'NAX-10' else 'README.md')
    return f'[{ident}]({rel(source, target)})'


def clean_nax_segments(line: str, source: Path) -> str:
    # Relation headers use middle-dot separators for Neoaxiom tails. Reconstruct only
    # segments whose visible content begins with a NAX/C-NAX identifier; this avoids
    # touching prose that merely discusses a Neoaxiom elsewhere.
    parts = line.split(' · ')
    out: list[str] = []
    for part in parts:
        stripped = part.strip()
        visible = re.sub(r'^\[', '', stripped)
        if re.match(r'^(?:C-)?NAX-\d+', visible):
            ids: list[str] = []
            for ident in NEOAX_ID_RE.findall(stripped):
                if ident not in ids:
                    ids.append(ident)
            if ids:
                lead = part[:len(part) - len(part.lstrip())]
                trail = part[len(part.rstrip()):]
                part = lead + ' · '.join(neoax_link(source, ident) for ident in ids) + trail
        out.append(part)
    return ' · '.join(out)


def clean_line(line: str, source: Path) -> str:
    if not line.startswith(PREFIXES):
        return line
    previous = None
    while previous != line:
        previous = line
        line = NESTED_SAME_RE.sub(lambda m: f'[{m.group(1)}{m.group(2)}{m.group(4)}]({m.group(3)})', line)
        line = EXTENDED_SUFFIX_RE.sub(lambda m: f'[{m.group(1)}{m.group(3)}]({m.group(2)})', line)
        line = DUP_SUFFIX_RE.sub(lambda m: m.group(1), line)
    return clean_nax_segments(line, source)


def files() -> list[Path]:
    paths = set(MAN.glob('[0-9][0-9]_*.md')) | set((MAN / 'canonicos').glob('*_ES_EN.md'))
    if CANON.exists():
        data = json.loads(CANON.read_text(encoding='utf-8'))
        for entry in data.get('entries', {}).values():
            for key in ('legacy', 'canonical'):
                v = entry.get(key)
                if v and (ROOT / v).exists(): paths.add(ROOT / v)
    inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
    if inf.exists(): paths.add(inf)
    return sorted(paths)


def main() -> int:
    changed = []
    for path in files():
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        out = [clean_line(line, path) for line in lines]
        if out != lines:
            path.write_text('\n'.join(out) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
            changed.append(str(path))
    print(f'RELATIONAL_MARKDOWN_SANITIZED={len(changed)}')
    for p in changed: print(f'SANITIZED: {p}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
