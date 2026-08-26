from pathlib import Path

ROOT = Path('.').resolve()
MIGRATION_REVISION = 2
# Build the obsolete token without storing it literally in the repository.
OBSOLETE = '7.3-' + 'CANDIDATE'
OLD_MARKER = 'NEOCORE_73_' + 'CANDIDATE'
OLD_SCRIPT = 'sync_neocore_73_' + 'candidate.py'

TEXT_EXTENSIONS = {
    '.md', '.py', '.yml', '.yaml', '.json', '.html', '.js', '.mjs', '.ts', '.tsx',
    '.css', '.txt', '.toml', '.ini', '.cfg', '.xml', '.csv'
}

changed = []
occurrences = 0

for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '.git' in path.parts:
        continue
    if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {'README', 'LICENSE'}:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    old = text
    count_here = text.count(OBSOLETE)
    if count_here:
        occurrences += count_here
        historical = (
            'auditorias' in path.parts
            or 'wiki-legacy-archive' in path.parts
            or ('2026-08-2' in path.name and path.name < '2026-08-26')
        )
        replacement = (
            '7.3 · ESTADO PRE-CANÓNICO HISTÓRICO'
            if historical
            else '7.3 CANON ABIERTO'
        )
        text = text.replace(OBSOLETE, replacement)

    text = text.replace(OLD_MARKER, 'NEOCORE_73_CANON')
    text = text.replace(OLD_SCRIPT, 'sync_neocore_73_canon.py')
    text = text.replace('neocore-73-' + 'candidate', 'neocore-73-canon-abierto')

    # Correct semantic residues produced by old non-canonical wording.
    text = text.replace(
        'NEOCore™ 7.3 CANON ABIERTO · candidata abierta, no canónica / open candidate, non-canonical',
        'NEOCore™ 7.3 CANON ABIERTO · canónico y reabrible / open canon, canonical and reopenable',
    )
    text = text.replace(
        '`7.3 CANON ABIERTO` permanece en Síntesis/evolución y **no equivale a 7.3 canónica ni a una implementación WEB4 final**.',
        '`7.3 CANON ABIERTO` es la base operativa vigente, canónica y reabrible; su canonización **no equivale a una implementación WEB4 final**.',
    )
    text = text.replace(
        '`7.3 CANON ABIERTO` remains under Synthesis/evolution and **does not equal canonical 7.3 or a final WEB4 implementation**.',
        '`7.3 OPEN CANON` is the current canonical and reopenable operating base; its canonisation **does not equal a final WEB4 implementation**.',
    )
    text = text.replace('7.3 CANON ABIERTO / NOT_CANON', '7.3 CANON ABIERTO')
    text = text.replace('7.3 CANON ABIERTO / NOT CANON', '7.3 CANON ABIERTO')
    text = text.replace('CANONICAL_STATE=7.3 CANON ABIERTO/NOT_CANON', 'CANONICAL_STATE=7.3_CANON_OPEN')
    text = text.replace('CANONICAL_STATE = 7.3 CANON ABIERTO', 'CANONICAL_STATE = 7.3_CANON_OPEN')

    if text != old:
        path.write_text(text, encoding='utf-8')
        changed.append(path.relative_to(ROOT).as_posix())

# Hard postcheck: the obsolete 7.3 state label must not remain in any tracked text surface.
residue = []
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '.git' in path.parts:
        continue
    if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {'README', 'LICENSE'}:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    if OBSOLETE in text or OLD_MARKER in text or OLD_SCRIPT in text:
        residue.append(path.relative_to(ROOT).as_posix())

if residue:
    raise SystemExit('STALE_7_3_PRECANON_LABELS=' + repr(residue))

print(f'MIGRATION_REVISION={MIGRATION_REVISION}')
print(f'REPLACED_OCCURRENCES={occurrences}')
print(f'CHANGED_FILES={len(changed)}')
for item in changed:
    print('CHANGED', item)
print('NEOCORE_73_LABEL_MIGRATION=PASS')
