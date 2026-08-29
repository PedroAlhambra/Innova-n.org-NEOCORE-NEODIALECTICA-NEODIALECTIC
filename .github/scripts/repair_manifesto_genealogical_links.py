from __future__ import annotations

from pathlib import Path
import json
import os
import re
import sys

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
CANON = MAN / 'CANONICAL_FILENAMES.json'
NEOAX = ROOT / 'neoaxiomas'

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
RELATION_PREFIXES = (
    '**Relaciones principales / Main relations:**',
    '**Relaciones raíz / Root relations:**',
    GENEALOGY_PREFIX,
)
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
TM_RE = re.compile(r'([A-ZÁÉÍÓÚÜÑa-záéíóúüñ0-9][^,;:.\n]*?™)')
# Never consume an already-linked title: '[' and ']' are excluded from the title span.
ROMAN_TARGET_RE = re.compile(r'(?<!\[)(?<![A-Z])([IVXLCDM]+)\s*·\s*([^,;.\[\]\n]*?™)')
BARE_ROMAN_RE = re.compile(r'(?<!\[)(?<![A-Z])([IVXLCDM]+)(?![A-Z\]])(?=\s*(?:,|·|$))')
RAW_INFINITY_RE = re.compile(r'(?<!\[)∞(?!\])')
RAW_NEOAX_RE = re.compile(r'(?<!\[)(?<![A-Z0-9-])(C-NAX-\d+|NAX-\d+)(?![A-Z0-9-])(?!\])')
# Defensive cleanup for the exact malformed form produced by an earlier repair iteration.
NESTED_SAME_LINK_RE = re.compile(r'\[([IVXLCDM]+\s*·\s*)\[([^\]]+)\]\(([^)]+)\)\]\(\3\)')


def load_entries() -> dict[str, dict[str, str]]:
    data = json.loads(CANON.read_text(encoding='utf-8'))
    return data['entries']


def relative_target(source: Path, repo_path: str | Path) -> str:
    target = ROOT / repo_path
    return Path(os.path.relpath(target, start=source.parent)).as_posix()


def verified_href(source: Path, roman: str, entries: dict[str, dict[str, str]]) -> str | None:
    entry = entries.get(roman)
    if not entry:
        return None
    canonical = entry.get('canonical')
    if not canonical or not (ROOT / canonical).exists():
        return None
    return relative_target(source, canonical)


def verified_infinity_href(source: Path) -> str | None:
    target = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
    if not target.exists():
        return None
    return relative_target(source, target)


def verified_neoaxiom_href(source: Path, identifier: str) -> str | None:
    # NAX-10 has its own canonical document. The canonical Neoaxiom registry README is
    # the verified destination for all other NAX/C-NAX identifiers until/if they gain
    # dedicated files. We deliberately do not invent per-heading anchors.
    if identifier == 'NAX-10':
        target = NEOAX / 'NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md'
    else:
        target = NEOAX / 'README.md'
    if not target.exists():
        return None
    return relative_target(source, target)


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


def link_bare_roman_targets(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    unresolved: list[str] = []

    def repl(match: re.Match[str]) -> str:
        roman = match.group(1)
        href = verified_href(source, roman, entries)
        if not href:
            unresolved.append(roman)
            return roman
        return f'[{roman}]({href})'

    return BARE_ROMAN_RE.sub(repl, line), unresolved


def link_infinity(line: str, source: Path) -> tuple[str, list[str]]:
    if '∞' not in line:
        return line, []
    href = verified_infinity_href(source)
    if not href:
        return line, ['∞']
    return RAW_INFINITY_RE.sub(f'[∞]({href})', line), []


def link_neoaxioms(line: str, source: Path) -> tuple[str, list[str]]:
    unresolved: list[str] = []

    def repl(match: re.Match[str]) -> str:
        identifier = match.group(1)
        href = verified_neoaxiom_href(source, identifier)
        if not href:
            unresolved.append(identifier)
            return identifier
        return f'[{identifier}]({href})'

    return RAW_NEOAX_RE.sub(repl, line), unresolved


def repair_declared_relation_line(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    if not line.startswith(RELATION_PREFIXES):
        return line, []

    unresolved: list[str] = []
    new_line = normalize_nested_links(line)
    new_line, explicit_unresolved = link_explicit_roman_targets(new_line, source, entries)
    unresolved.extend(explicit_unresolved)
    new_line, bare_unresolved = link_bare_roman_targets(new_line, source, entries)
    unresolved.extend(bare_unresolved)
    new_line, infinity_unresolved = link_infinity(new_line, source)
    unresolved.extend(infinity_unresolved)
    new_line, neoax_unresolved = link_neoaxioms(new_line, source)
    unresolved.extend(neoax_unresolved)

    # Genealogical surfaces additionally resolve verified named aliases.
    if line.startswith(GENEALOGY_PREFIX):
        linked_spans = {m.group(1) for m in MD_LINK_RE.finditer(new_line)}
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
            repaired, unresolved = repair_declared_relation_line(line, path, entries)
            if repaired != line:
                touched = True
            out.append(repaired)
            for item in unresolved:
                code = 'UNRESOLVED_GENEALOGICAL_TARGET' if line.startswith(GENEALOGY_PREFIX) else 'UNRESOLVED_RELATIONAL_TARGET'
                unresolved_rows.append(f'{path}:{lineno}: {code}: {item}')

        if touched:
            changed.append(str(path))
            if not check_only:
                suffix = '\n' if text.endswith('\n') else ''
                path.write_text('\n'.join(out) + suffix, encoding='utf-8')

    print(f'RELATIONAL_REPAIR_CHANGED={len(changed)}')
    for item in changed:
        print(f'REPAIRED: {item}')
    for item in unresolved_rows:
        print(item)

    if check_only and changed:
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
