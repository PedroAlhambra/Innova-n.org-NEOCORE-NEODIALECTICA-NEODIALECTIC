from pathlib import Path
import re
import sys

ROOT = Path('.').resolve()

# Immutable genealogy is not a live navigation surface.
EXCLUDED_PARTS = {'.git', 'wiki-legacy-archive'}
EXCLUDED_PREFIXES = ('.github/',)

ES_GATE = re.compile(r'^#{1,4}\s+ES(?:\s+·\s+[^\n]+)?\s*$', re.M)
EN_GATE = re.compile(r'^#{1,4}\s+EN(?:\s+·\s+[^\n]+)?\s*$', re.M)
ES_LINK = re.compile(r'\[\s*ES(?:\s+·\s+[^\]]+)?\s*\]\(\s*#es[^)\s]*\s*\)', re.I)
EN_LINK = re.compile(r'\[\s*EN(?:\s+·\s+[^\]]+)?\s*\]\(\s*#en[^)\s]*\s*\)', re.I)


def active_markdown(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in EXCLUDED_PARTS for part in path.parts):
        return False
    if rel.startswith(EXCLUDED_PREFIXES):
        return False
    return True


def audit_file(path: Path):
    text = path.read_text(encoding='utf-8', errors='replace')
    es = ES_GATE.search(text)
    en = EN_GATE.search(text)
    if not es and not en:
        return None
    rel = path.relative_to(ROOT).as_posix()
    if not es or not en or en.start() < es.start():
        return (rel, 'BROKEN_LANGUAGE_GATES', 'faltan gates ES/EN ordenados / ordered ES/EN gates missing')

    # Selector must be visible before the Spanish body, not buried at the bottom.
    prefix = text[:es.start()]
    missing = []
    if not ES_LINK.search(prefix):
        missing.append('ES selector')
    if not EN_LINK.search(prefix):
        missing.append('EN selector')
    if missing:
        return (rel, 'LANGUAGE_NAVIGATION_FAILURE', ', '.join(missing))
    return (rel, 'OK', '')


checked = 0
failures = []
for path in sorted(ROOT.rglob('*.md')):
    if not active_markdown(path):
        continue
    result = audit_file(path)
    if result is None:
        continue
    checked += 1
    if result[1] != 'OK':
        failures.append(result)

print(f'Explicit ES/EN split pages checked: {checked}')
print(f'Language-navigation failures: {len(failures)}')
for rel, status, detail in failures:
    print(f'FAIL | {status} | {rel} | {detail}')

if failures:
    print('\nLANGUAGE_SELECTOR_GATE = FAIL')
    print('Content symmetry PASS cannot override language navigation FAIL.')
    sys.exit(1)

print('LANGUAGE_SELECTOR_GATE = PASS')
