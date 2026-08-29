from __future__ import annotations

from pathlib import Path
import json
import os
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
    'Coherencia entre Fines y Medios™': 'XXX',
}

GENEALOGY_PREFIX = '**Relación genealógica / Genealogical relation:**'
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
TM_RE = re.compile(r'([A-ZÁÉÍÓÚÜÑa-záéíóúüñ0-9][^,;:.\n]*?™)')
# Never consume an already-linked title: '[' and ']' are excluded from the title span.
ROMAN_TARGET_RE = re.compile(r'(?<!\[)(?<![A-Z])([IVXLCDM]+)\s*·\s*([^,;.\[\]\n]*?™)')
# Defensive cleanup for the exact malformed form produced by an earlier repair iteration.
NESTED_SAME_LINK_RE = re.compile(r'\[([IVXLCDM]+\s*·\s*)\[([^\]]+)\]\(([^)]+)\)\]\(\3\)')


def load_entries() -> dict[str, dict[str, str]]:
    data = json.loads(CANON.read_text(encoding='utf-8'))
    return data['entries']


def relative_target(source: Path, canonical_repo_path: str) -> str:
    target = ROOT / canonical_repo_path
    return Path(os.path.relpath(target, start=source.parent)).as_posix()


def verified_href(source: Path, roman: str, entries: dict[str, dict[str, str]]) -> str | None:
    entry = entries.get(roman)
    if not entry:
        return None
    canonical = entry.get('canonical')
    if not canonical or not (ROOT / canonical).exists():
        return None
    return relative_target(source, canonical)


def normalize_nested_links(line: str) -> str:
    return NESTED_SAME_LINK_RE.sub(lambda m: f'[{m.group(1)}{m.group(2)}]({m.group(3)})', line)


def link_explicit_roman_targets(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    unresolved: list[str] = []

    def repl(match: re.Match[str]) -> str:
        roman, title = match.group(1), match.group(2).strip()
        label = f'{roman} · {title}'
        href = verified_href(source, roman, entries)
        if not href:
            unresolved.append(label)
            return match.group(0)
        return f'[{label}]({href})'

    return ROMAN_TARGET_RE.sub(repl, line), unresolved


def link_aliases_in_line(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    if not line.startswith(GENEALOGY_PREFIX):
        return line, []

    unresolved: list[str] = []
    new_line = normalize_nested_links(line)
    new_line, roman_unresolved = link_explicit_roman_targets(new_line, source, entries)
    unresolved.extend(roman_unresolved)
    linked_spans = {m.group(1) for m in MD_LINK_RE.finditer(new_line)}

    # Longest aliases first, to avoid accidental partial overlap.
    for alias in sorted(ALIASES, key=len, reverse=True):
        if alias in linked_spans or alias not in new_line:
            continue
        roman = ALIASES[alias]
        href = verified_href(source, roman, entries)
        if not href:
            unresolved.append(alias)
            continue
        new_line = re.sub(rf'(?<!\[){re.escape(alias)}(?!\]\()', f'[{alias}]({href})', new_line)

    # Anything trademarked and still raw is unresolved. It is reported, never guessed.
    residual = MD_LINK_RE.sub('', new_line.split(':**', 1)[-1])
    for raw in TM_RE.findall(residual):
        candidate = raw.strip(' *`')
        for marker in (
            'profundiza ', 'deepens ', 'integra ', 'integrates ', 'continúa ', 'continues ',
            'desarrolla ', 'develops ', 'deriva del conjunto del ', 'formula ', 'Formula ',
            'Se relaciona directamente con ', 'la ', 'y ', 'e ', 'and '
        ):
            if candidate.startswith(marker):
                candidate = candidate[len(marker):].strip()
        if candidate.endswith('™') and candidate not in unresolved:
            unresolved.append(candidate)

    return new_line, unresolved


def manifest_files(entries: dict[str, dict[str, str]]) -> list[Path]:
    # Union registry + on-disk surfaces: newly added manifestos cannot escape repair/audit
    # merely because CANONICAL_FILENAMES.json has not yet been reconciled.
    paths: set[Path] = set(MAN.glob('[0-9][0-9]_*.md'))
    paths.update((MAN / 'canonicos').glob('*_ES_EN.md'))
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
