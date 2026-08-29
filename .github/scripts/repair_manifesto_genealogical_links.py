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

# Conservative registry: every alias below points to a destination verified in
# CANONICAL_FILENAMES.json. Variants are explicit; no fuzzy title inference is used.
ALIASES = {
    'Síntesis Abierta Neodialéctica™': 'II',
    'Neodialectical Open Synthesis™': 'II',
    'Derecho Humano de Aporte™': 'III',
    'Neodialéctica y Bien Común™': 'IV',
    'Parasitismo Sistémico™': 'VI',
    'Memoria, Genealogía y Trazabilidad™': 'IX',
    'Memoria-Genealogía-Trazabilidad™': 'IX',
    'Memory, Genealogy and Traceability™': 'IX',
    'WEB4™': 'X',
    'SistemaTrazable™': 'X',
    'Neorrenacimiento Humano™': 'XI',
    'Human Neo-Renaissance™': 'XI',
    'Refragmentación Arquetípica™': 'XVI',
    'Persistencia de la Memoria™': 'XIX',
    'Persistence of Memory™': 'XIX',
    'Umbral-X™': 'XX',
    'Reconocimiento Neodialéctico™': 'XXI',
    'Neodialectical Recognition™': 'XXI',
    'Soberanía del Tiempo Cognitivo™': 'XXIII',
    'Sovereignty of Cognitive Time™': 'XXIII',
    'Misericordia Universal Recíproca™': 'XXVI',
    'Universal Reciprocal Mercy™': 'XXVI',
    'Coherencia entre Fines y Medios™': 'XXX',
    'Coherence between Ends and Means™': 'XXX',
    'Contra el Neuromarketing Antihumanista™': 'XXXI',
    'Against Anti-Humanist Neuromarketing™': 'XXXI',
    'Reversión Ideológica Neodialéctica™': 'XXXII',
    'Reversión Ideológica™': 'XXXII',
    'Utilidad Operativa y Auditoría Conjunta Perpetua™': 'XXXIV',
    'Contra la Ridiculez Mediática y la Economía del Conflicto™': 'XXXV',
    'Águila y Custodia de la Edad del Hombre™': 'XXXVI',
    'Corona, Águila y Custodia de la Edad del Hombre™': 'XXXVI',
    'Neofraternidad™': 'XXXVII',
    'Neofraternity™': 'XXXVII',
    'Protección Integral de la Infancia™': 'XXXVIII',
    'Integral Protection of Childhood™': 'XXXVIII',
    'Autoconciencia de la Necesidad Vital Neodialéctica™': 'XXXIX',
    'Neoego™': 'XL',
    'Martillo Limitado™': 'XLI',
    'Martillo Limitado-Talión-Fuerza Protectora™': 'XLI',
    'Fin de la Era del Hombre Manipulado™': 'XLII',
    'Inteligencia Humana Expandida™': 'XLIII',
    'Expanded Human Intelligence™': 'XLIII',
    'Neowar™': 'XLIV',
    'Multidimensionalidad Neodialéctica™': 'XLV',
    'Neodialectical Multidimensionality™': 'XLV',
    'Cerrar la Herida™': 'XLVI',
    'Close the Wound™': 'XLVI',
    'La Síntesis Todo lo Ve™': 'XLVIII',
    'La Neodialéctica como Punto de Encuentro entre Culturas™': 'XLIX',
    'Inteligencia Compartida, no Única™': 'L',
    'Inteligencia Compartida™': 'L',
    'Poder Cívico de la Síntesis Abierta™': 'LI',
}

GENEALOGY_PREFIX = '**Relación genealógica / Genealogical relation:**'
RELATION_PREFIXES = (
    '**Relaciones principales / Main relations:**',
    '**Relaciones raíz / Root relations:**',
    GENEALOGY_PREFIX,
)
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
TM_RE = re.compile(r'([A-ZÁÉÍÓÚÜÑa-záéíóúüñ0-9][^,;:.\n]*?™)')
ROMAN_TARGET_RE = re.compile(r'(?<!\[)(?<![A-Z])([IVXLCDM]+)\s*·\s*([^,;.\[\]\n]*?™)')
BARE_ROMAN_RE = re.compile(r'(?<!\[)(?<![A-Z])([IVXLCDM]+)(?![A-Z\]])(?=\s*(?:,|·|$))')
RAW_INFINITY_RE = re.compile(r'(?<!\[)∞(?!\])')
RAW_NEOAX_RE = re.compile(r'(?<!\[)(?<![A-Z0-9-])(C-NAX-\d+|NAX-\d+)(?![A-Z0-9-])(?!\])')
NESTED_SAME_LINK_RE = re.compile(r'\[([IVXLCDM]+\s*·\s*)\[([^\]]+)\]\(([^)]+)\)\]\(\3\)')
# Regression created by a previous non-idempotent pass: an already linked NAX-10
# was linked again inside its own href. Normalize it before any new transforms.
MALFORMED_NAX10_RE = re.compile(
    r'\[NAX-10\]\([^)]*?\[NAX-10\]\(([^)]+NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN\.md)\)'
    r'_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN\.md\)'
)
MALFORMED_TRAILING_NEOAX_RE = re.compile(r'(?<!\[)(C-NAX-\d+|NAX-\d+)\]\([^)]+\)')


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
    return relative_target(source, target) if target.exists() else None


def verified_neoaxiom_href(source: Path, identifier: str) -> str | None:
    target = NEOAX / ('NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md' if identifier == 'NAX-10' else 'README.md')
    return relative_target(source, target) if target.exists() else None


def protect_links(line: str) -> tuple[str, list[str]]:
    spans: list[str] = []
    def repl(m: re.Match[str]) -> str:
        spans.append(m.group(0))
        return f'@@MDLINK_{len(spans)-1}@@'
    return MD_LINK_RE.sub(repl, line), spans


def restore_links(line: str, spans: list[str]) -> str:
    for i, value in enumerate(spans):
        line = line.replace(f'@@MDLINK_{i}@@', value)
    return line


def normalize_malformed_links(line: str) -> str:
    line = NESTED_SAME_LINK_RE.sub(lambda m: f'[{m.group(1)}{m.group(2)}]({m.group(3)})', line)
    line = MALFORMED_NAX10_RE.sub(lambda m: f'[NAX-10]({m.group(1)})', line)
    # A historic malformed tail such as C-NAX-19](./14_...) must first become
    # plain C-NAX-19; the verified linker will then attach the canonical target.
    line = MALFORMED_TRAILING_NEOAX_RE.sub(lambda m: m.group(1), line)
    return line


def transform_outside_links(line: str, transform) -> str:
    protected, spans = protect_links(line)
    protected = transform(protected)
    return restore_links(protected, spans)


def link_explicit_roman_targets(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    unresolved: list[str] = []
    def do(text: str) -> str:
        def repl(match: re.Match[str]) -> str:
            roman, title = match.group(1), match.group(2).strip()
            label = f'{roman} · {title}'
            href = verified_href(source, roman, entries)
            if not href:
                unresolved.append(label)
                return match.group(0)
            return f'[{label}]({href})'
        return ROMAN_TARGET_RE.sub(repl, text)
    return transform_outside_links(line, do), unresolved


def link_bare_roman_targets(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    unresolved: list[str] = []
    def do(text: str) -> str:
        def repl(match: re.Match[str]) -> str:
            roman = match.group(1)
            href = verified_href(source, roman, entries)
            if not href:
                unresolved.append(roman)
                return roman
            return f'[{roman}]({href})'
        return BARE_ROMAN_RE.sub(repl, text)
    return transform_outside_links(line, do), unresolved


def link_infinity(line: str, source: Path) -> tuple[str, list[str]]:
    if '∞' not in line:
        return line, []
    href = verified_infinity_href(source)
    if not href:
        return line, ['∞']
    return transform_outside_links(line, lambda text: RAW_INFINITY_RE.sub(f'[∞]({href})', text)), []


def link_neoaxioms(line: str, source: Path) -> tuple[str, list[str]]:
    unresolved: list[str] = []
    def do(text: str) -> str:
        def repl(match: re.Match[str]) -> str:
            identifier = match.group(1)
            href = verified_neoaxiom_href(source, identifier)
            if not href:
                unresolved.append(identifier)
                return identifier
            return f'[{identifier}]({href})'
        return RAW_NEOAX_RE.sub(repl, text)
    return transform_outside_links(line, do), unresolved


def link_aliases(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    unresolved: list[str] = []
    protected, spans = protect_links(line)
    for alias in sorted(ALIASES, key=len, reverse=True):
        if alias not in protected:
            continue
        href = verified_href(source, ALIASES[alias], entries)
        if not href:
            unresolved.append(alias)
            continue
        protected = protected.replace(alias, f'[{alias}]({href})')
    return restore_links(protected, spans), unresolved


def repair_declared_relation_line(line: str, source: Path, entries: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    if not line.startswith(RELATION_PREFIXES):
        return line, []
    unresolved: list[str] = []
    new_line = normalize_malformed_links(line)
    new_line, xs = link_explicit_roman_targets(new_line, source, entries); unresolved.extend(xs)
    new_line, xs = link_bare_roman_targets(new_line, source, entries); unresolved.extend(xs)
    new_line, xs = link_infinity(new_line, source); unresolved.extend(xs)
    new_line, xs = link_neoaxioms(new_line, source); unresolved.extend(xs)

    if line.startswith(GENEALOGY_PREFIX):
        new_line, xs = link_aliases(new_line, source, entries); unresolved.extend(xs)
        residual = MD_LINK_RE.sub('', new_line.split(':**', 1)[-1])
        for raw in TM_RE.findall(residual):
            candidate = raw.strip(' *`')
            for marker in (
                'profundiza ', 'deepens ', 'integra ', 'integrates ', 'continúa ', 'continues ',
                'desarrolla ', 'develops ', 'deriva del conjunto del ', 'formula ', 'Formula ',
                'Se relaciona directamente con ', 'la ', 'y ', 'e ', 'and ',
                'Abre la cuarta oleada trasladando la '
            ):
                if candidate.startswith(marker):
                    candidate = candidate[len(marker):].strip()
            if candidate.endswith('™') and candidate not in unresolved:
                unresolved.append(candidate)
    return new_line, unresolved


def manifest_files(entries: dict[str, dict[str, str]]) -> list[Path]:
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
