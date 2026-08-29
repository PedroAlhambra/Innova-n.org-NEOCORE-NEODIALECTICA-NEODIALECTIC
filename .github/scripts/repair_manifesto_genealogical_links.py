from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
CANON = MAN / 'CANONICAL_FILENAMES.json'

# Conservative, explicit alias registry. Add only aliases whose canonical target is verified.
# The repairer never guesses a target from textual similarity.
ALIASES = {
    'Neoego™': 'XL',
    'Misericordia Universal Recíproca™': 'XXVI',
    'Neofraternidad™': 'XXXVII',
    'Multidimensionalidad Neodialéctica™': 'XLV',
    'Cerrar la Herida™': 'XLVI',
    'Persistencia de la Memoria™': 'XIX',
    'Inteligencia Humana Expandida™': 'XLIII',
}

GENEALOGY_PREFIX = '**Relación genealógica / Genealogical relation:**'
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
TM_RE = re.compile(r'([A-ZÁÉÍÓÚÜÑa-záéíóúüñ0-9][^,;:.\n]*?™)')


def load_entries() -> dict[str, dict[str, str]]:
    data = json.loads(CANON.read_text(encoding='utf-8'))
    return data['entries']


def relative_target(source: Path, canonical_repo_path: str) -> str:
    target = ROOT / canonical_repo_path
    return Path(__import__('os').path.relpath(target, start=source.parent)).as_posix()


def link_aliases_in_line(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    if not line.startswith(GENEALOGY_PREFIX):
        return line, []

    linked_spans = {m.group(1) for m in MD_LINK_RE.finditer(line)}
    unresolved: list[str] = []
    new_line = line

    # Longest aliases first, to avoid accidental partial overlap.
    for alias in sorted(ALIASES, key=len, reverse=True):
        if alias in linked_spans:
            continue
        if alias not in new_line:
            continue
        roman = ALIASES[alias]
        entry = entries.get(roman)
        if not entry:
            unresolved.append(alias)
            continue
        canonical = entry.get('canonical')
        if not canonical or not (ROOT / canonical).exists():
            unresolved.append(alias)
            continue
        href = relative_target(source, canonical)
        new_line = re.sub(rf'(?<!\[){re.escape(alias)}(?!\]\()', f'[{alias}]({href})', new_line)

    # Anything trademarked and still raw is unresolved unless it is prose outside a named relation.
    residual = MD_LINK_RE.sub('', new_line.split(':**', 1)[-1])
    for raw in TM_RE.findall(residual):
        candidate = raw.strip(' *`')
        # Strip common connective/prose prefixes while preserving the named trademark.
        for marker in ('profundiza ', 'deepens ', 'integra ', 'integrates ', 'y ', 'e ', 'and '):
            if candidate.startswith(marker):
                candidate = candidate[len(marker):].strip()
        if candidate.endswith('™') and candidate not in unresolved:
            unresolved.append(candidate)

    return new_line, unresolved


def manifest_files(entries: dict[str, dict[str, str]]) -> list[Path]:
    paths: set[Path] = set()
    for entry in entries.values():
        for key in ('legacy', 'canonical'):
            value = entry.get(key)
            if value:
                p = ROOT / value
                if p.exists():
                    paths.add(p)
    inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
    if inf.exists():
        paths.add(inf)
    return sorted(paths)


def main() -> int:
    check_only = '--check' in sys.argv
    entries = load_entries()
    changed: list[str] = []
    unresolved_rows: list[str] = []

    for path in manifest_files(entries):
        text = path.read_text(encoding='utf-8')
        out: list[str] = []
        touched = False
        for lineno, line in enumerate(text.splitlines(), 1):
            repaired, unresolved = link_aliases_in_line(line, path, entries)
            if repaired != line:
                touched = True
            out.append(repaired)
            for item in unresolved:
                unresolved_rows.append(f'{path}:{lineno}: UNRESOLVED_GENEALOGICAL_TARGET: {item}')

        if touched:
            changed.append(str(path))
            if not check_only:
                suffix = '\n' if text.endswith('\n') else ''
                path.write_text('\n'.join(out) + suffix, encoding='utf-8')

    print(f'GENEALOGICAL_REPAIR_CHANGED={len(changed)}')
    for item in changed:
        print(f'REPAIRED: {item}')
    for item in unresolved_rows:
        print(item)

    if check_only and changed:
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
