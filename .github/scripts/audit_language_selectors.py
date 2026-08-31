from pathlib import Path
from datetime import datetime, timezone
import re
import sys

ROOT = Path('.').resolve()
REPORT = ROOT / 'auditorias' / 'publicas' / '2026-08-24_auditoria_global_selectores_idioma_ES_EN.md'

# Immutable genealogy is not a live navigation surface.
EXCLUDED_PARTS = {'.git', 'wiki-legacy-archive'}
EXCLUDED_PREFIXES = ('.github/',)

ES_GATE = re.compile(r'^#{1,4}\s+ES(?:\s+·\s+[^\n]+)?\s*$', re.M)
EN_GATE = re.compile(r'^#{1,4}\s+EN(?:\s+·\s+[^\n]+)?\s*$', re.M)
ES_LINK = re.compile(r'\[\s*ES(?:\s+·\s+[^\]]+)?\s*\]\(\s*(#[^)\s]+)\s*\)', re.I)
EN_LINK = re.compile(r'\[\s*EN(?:\s+·\s+[^\]]+)?\s*\]\(\s*(#[^)\s]+)\s*\)', re.I)


def active_markdown(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in EXCLUDED_PARTS for part in path.parts):
        return False
    if rel.startswith(EXCLUDED_PREFIXES):
        return False
    return True


def github_anchor_from_heading(line: str) -> str:
    """Approximate GitHub's Markdown heading anchor for the house ES/EN gates."""
    title = re.sub(r'^#{1,6}\s+', '', line.strip()).strip().lower()
    # GitHub removes punctuation but preserves the spaces around it; those spaces become
    # separate hyphens, hence `ES · Castellano` -> `#es--castellano`.
    title = re.sub(r'[^\w\s-]', '', title, flags=re.UNICODE)
    title = re.sub(r'\s', '-', title)
    return '#' + title


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
    es_link = ES_LINK.search(prefix)
    en_link = EN_LINK.search(prefix)
    missing = []
    if not es_link:
        missing.append('ES selector')
    if not en_link:
        missing.append('EN selector')
    if missing:
        return (rel, 'LANGUAGE_NAVIGATION_FAILURE', ', '.join(missing))

    expected_es = github_anchor_from_heading(es.group(0))
    expected_en = github_anchor_from_heading(en.group(0))
    actual_es = es_link.group(1).lower()
    actual_en = en_link.group(1).lower()
    anchor_errors = []
    if actual_es != expected_es:
        anchor_errors.append(f'ES anchor {actual_es} != {expected_es}')
    if actual_en != expected_en:
        anchor_errors.append(f'EN anchor {actual_en} != {expected_en}')
    if anchor_errors:
        return (rel, 'LANGUAGE_ANCHOR_FAILURE', '; '.join(anchor_errors))

    return (rel, 'OK', '')


def render_report(checked: int, failures: list[tuple[str, str, str]]) -> str:
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    status = 'FAIL' if failures else 'PASS'
    detail_es = '\n'.join(
        f'- `{rel}` · `{kind}` · {detail}' for rel, kind, detail in failures
    ) or '- Ningún fallo detectado. / No failures detected.'
    detail_en = '\n'.join(
        f'- `{rel}` · `{kind}` · {detail}' for rel, kind, detail in failures
    ) or '- No failures detected. / Ningún fallo detectado.'
    return f'''# Auditoría global de selectores de idioma ES/EN\n# Global ES/EN language-selector audit\n\n**Generada / Generated:** {now}  \n**Páginas ES/EN explícitas auditadas / Explicit ES/EN split pages audited:** **{checked}**  \n**Fallos / Failures:** **{len(failures)}**  \n**LANGUAGE_SELECTOR_GATE:** **{status}**\n\n[ES · Castellano](#es--castellano) · [EN · English](#en--english)\n\n---\n\n# ES · Castellano\n\n## Regla\n\nToda superficie Markdown pública y activa que exponga capas explícitas `ES` y `EN` debe incluir, antes del cuerpo español, un selector visible que permita saltar directamente a ambas capas. Los destinos deben coincidir con los anchors reales derivados de los encabezados.\n\n`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. Un selector ausente o un anchor incorrecto bloquea el PASS global.\n\n## Resultado\n\n- Páginas auditadas: **{checked}**.\n- Fallos: **{len(failures)}**.\n- Estado: **{status}**.\n\n## Detalle de fallos\n\n{detail_es}\n\n---\n\n# EN · English\n\n## Rule\n\nEvery active public Markdown surface exposing explicit `ES` and `EN` layers must include, before the Spanish body, a visible selector linking directly to both language layers. Link targets must match the real anchors derived from those headings.\n\n`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. A missing selector or incorrect anchor blocks the global PASS.\n\n## Result\n\n- Pages audited: **{checked}**.\n- Failures: **{len(failures)}**.\n- Status: **{status}**.\n\n## Failure detail\n\n{detail_en}\n'''


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

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(render_report(checked, failures).replace('  \n', '\n'), encoding='utf-8')

print(f'Explicit ES/EN split pages checked: {checked}')
print(f'Language-navigation failures: {len(failures)}')
for rel, status, detail in failures:
    print(f'FAIL | {status} | {rel} | {detail}')

if failures:
    print('\nLANGUAGE_SELECTOR_GATE = FAIL')
    print('Content symmetry PASS cannot override language navigation FAIL.')
    sys.exit(1)

print('LANGUAGE_SELECTOR_GATE = PASS')
