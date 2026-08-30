from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
CANON = MAN / 'CANONICAL_FILENAMES.json'

failures: list[str] = []
relation_lines = 0
genealogy_lines = 0
synthesis_lines = 0

MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
RELATION_PREFIXES = ('**Relaciones principales / Main relations:**', '**Relaciones raíz / Root relations:**')
GENEALOGY_PREFIXES = (
    '**Relación genealógica / Genealogical relation:**',
    '**Genealogía / Genealogy:**',
)

REGISTRY = json.loads(CANON.read_text(encoding='utf-8')) if CANON.exists() else {'entries': {}}
LEGACY_TO_CANONICAL = {
    (ROOT / entry['legacy']).resolve(): (ROOT / entry['canonical']).resolve()
    for entry in REGISTRY.get('entries', {}).values()
    if entry.get('legacy') and entry.get('canonical')
}


def manifest_files() -> list[Path]:
    paths: set[Path] = set(MAN.glob('[0-9][0-9]_*.md'))
    paths.update((MAN / 'canonicos').glob('*_ES_EN.md'))
    if CANON.exists():
        data = json.loads(CANON.read_text(encoding='utf-8'))
        for entry in data.get('entries', {}).values():
            for key in ('legacy', 'canonical'):
                value = entry.get(key)
                if value and (ROOT / value).exists(): paths.add(ROOT / value)
    inf = MAN / 'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
    if inf.exists(): paths.add(inf)
    return sorted(paths)


def remove_md_links(s: str) -> str:
    return MD_LINK_RE.sub('', s)


def raw_trademark_relations(s: str) -> list[str]:
    residual = remove_md_links(s); found = []
    for m in re.finditer(r'(?:(?<=^)|(?<=[,:;]))\s*([^,;:.\n]*?™)', residual):
        value = m.group(1).strip(' *`')
        for prefix in ('profundiza ', 'deepens ', 'integra ', 'integrates ', 'continúa ', 'continues ', 'desarrolla ', 'develops ', 'deriva del conjunto del ', 'formula ', 'Formula ', 'Se relaciona directamente con ', 'la ', 'y ', 'e ', 'and '):
            if value.startswith(prefix): value = value[len(prefix):].strip()
        if value: found.append(value)
    return sorted(set(found))


def raw_named_manifesto_relations(s: str) -> list[str]:
    """Find canonical manifesto references left as plain text after real links are removed.

    A genealogy such as "Manifiesto XLVII" / "Manifesto XLVII" is itself a
    navigation declaration.  It must therefore be clickable at the point where
    it is named, even when the title has no trademark marker and even when the
    same target is linked later in the cross-reference block.
    """
    residual = remove_md_links(s)
    found = {
        f'{label} {number}'
        for label, number in re.findall(
            r'\b(Manifiesto|Manifesto)\s+([IVXLCDM]+|∞)\b', residual, flags=re.IGNORECASE
        )
    }
    return sorted(found)


def validate_local_links(path: Path, line: str, lineno: int) -> None:
    for label, href in MD_LINK_RE.findall(line):
        if href.startswith(('http://', 'https://', '#', 'mailto:')): continue
        target = (path.parent / href.split('#', 1)[0]).resolve()
        if not target.exists():
            failures.append(f'{path}:{lineno}: BROKEN_RELATIONAL_TARGET: [{label}]({href})')
            continue
        canonical = LEGACY_TO_CANONICAL.get(target)
        if canonical and target != canonical:
            failures.append(
                f'{path}:{lineno}: NONCANONICAL_RELATIONAL_TARGET: '
                f'[{label}]({href}) -> {canonical.relative_to(ROOT.resolve())}'
            )


def validate_relation_markdown(path: Path, line: str, lineno: int) -> None:
    """Reject pseudo-links and true nested-link debris in declared relation surfaces."""
    residual = remove_md_links(line)
    defects: set[str] = set()
    for token in re.findall(r'\[(?:[IVXLCDM]+|∞|(?:C-)?NAX-\d+)', residual): defects.add(token)
    for token in re.findall(r'(?:[IVXLCDM]+|∞|(?:C-)?NAX-\d+)\]\(', residual): defects.add(token)
    # Keep this deliberately local: the outer label may not cross another complete
    # Markdown link. The previous greedy pattern mistook any two links on one line
    # for nesting, producing false positives across otherwise valid relation lists.
    if re.search(r'\[[^\[\]\n]*\[[^\]\n]+\]\([^)\n]+\)[^\[\]\n]*\]\([^)\n]+\)', line):
        defects.add('NESTED_LINK')
    if defects: failures.append(f'{path}:{lineno}: RELATIONAL_MARKDOWN_SYNTAX_FAILURE: {sorted(defects)}')


def has_crossref_block(text: str) -> bool:
    return '<!-- NEO_CROSS_REFERENCES_START -->' in text and '<!-- NEO_CROSS_REFERENCES_END -->' in text


def audit_declared_relations(path: Path, line: str, lineno: int) -> None:
    validate_relation_markdown(path, line, lineno)
    raw = line.split(':**', 1)[-1]; residual = remove_md_links(raw); missing = set()
    missing.update(re.findall(r'(?<![A-Z])([IVXLCDM]+|∞)\s*·', residual))
    missing.update(re.findall(r'(?:^|,)\s*([IVXLCDM]+|∞)\s*(?=,|·|$|\by\b|\be\b|\band\b)', residual))
    if missing: failures.append(f'{path}:{lineno}: MAIN_RELATIONS_NOT_CLICKABLE: {sorted(missing)}')
    neoaxioms = sorted(set(re.findall(r'(?<![A-Z0-9-])(C-NAX-\d+|NAX-\d+)(?![A-Z0-9-])', residual)))
    if neoaxioms: failures.append(f'{path}:{lineno}: NEOAXIOM_RELATIONS_NOT_CLICKABLE: {neoaxioms}')
    validate_local_links(path, line, lineno)


files = manifest_files()
for p in files:
    text = p.read_text(encoding='utf-8')
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.startswith(RELATION_PREFIXES):
            relation_lines += 1; audit_declared_relations(p, line, lineno)
        if line.startswith(GENEALOGY_PREFIXES):
            genealogy_lines += 1; raw = line.split(':**', 1)[-1]
            missing = raw_trademark_relations(raw)
            if missing: failures.append(f'{p}:{lineno}: GENEALOGICAL_NAVIGATION_FAILURE: {missing}')
            bare_manifestos = raw_named_manifesto_relations(raw)
            if bare_manifestos:
                failures.append(f'{p}:{lineno}: GENEALOGICAL_NAMED_MANIFESTO_NOT_CLICKABLE: {bare_manifestos}')
            audit_declared_relations(p, line, lineno)
        if line.startswith('**Síntesis Abierta / Open Synthesis:**'):
            synthesis_lines += 1
            issue_numbers = set(re.findall(r'#(\d+)\b', line)) | set(re.findall(r'/issues/(\d+)', line))
            if issue_numbers:
                linked = set(re.findall(r'\[[^\]]*#(\d+)[^\]]*\]\(https://github\.com/[^)]+/issues/\1\)', line))
                missing = sorted(issue_numbers - linked, key=int)
                if missing: failures.append(f'{p}:{lineno}: OPEN_SYNTHESIS_ISSUE_NOT_CLICKABLE: {missing}')
            validate_local_links(p, line, lineno)
    if not has_crossref_block(text): failures.append(f'{p}: CANONICAL_CROSSREF_BLOCK_MISSING')

if failures:
    print('CLICKABLE_RELATIONS=FAIL'); print(f'MANIFEST_SURFACES_AUDITED={len(files)}')
    for item in failures: print(item)
    sys.exit(1)
print(f'CLICKABLE_RELATIONS=PASS manifests={len(files)} relation_lines={relation_lines} genealogy_lines={genealogy_lines} synthesis_lines={synthesis_lines}')
