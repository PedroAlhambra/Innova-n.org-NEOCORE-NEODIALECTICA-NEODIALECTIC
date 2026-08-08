from pathlib import Path
import re
import urllib.parse

ROOT = Path('.')

MAIN_AUDIT = 'analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md'
ADDENDUM_07 = 'auditorias/publicas/2026-08-07_addendum_reapertura_caso_51071689_ES_EN.md'
ADDENDUM_08 = 'auditorias/publicas/2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md'
REPORT = Path('auditorias/publicas/2026-08-08_auditoria_global_readmes_enlaces_y_trazabilidad_kdp_ES_EN.md')

TRACE_TARGETS = {
    'README.md': (
        './' + MAIN_AUDIT,
        './' + ADDENDUM_07,
        './' + ADDENDUM_08,
    ),
    'analisis/README.md': (
        './publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md',
        '../' + ADDENDUM_07,
        '../' + ADDENDUM_08,
    ),
    'analisis/INDEX.md': (
        './publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md',
        '../' + ADDENDUM_07,
        '../' + ADDENDUM_08,
    ),
    'analisis/publicos/README.md': (
        './2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md',
        '../../' + ADDENDUM_07,
        '../../' + ADDENDUM_08,
    ),
    'analisis/auditorias/README.md': (
        '../publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md',
        '../../' + ADDENDUM_07,
        '../../' + ADDENDUM_08,
    ),
    'auditorias/publicas/README.md': (
        '../../' + MAIN_AUDIT,
        './2026-08-07_addendum_reapertura_caso_51071689_ES_EN.md',
        './2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md',
    ),
    'obras/idea/README.md': (
        '../../' + MAIN_AUDIT,
        '../../' + ADDENDUM_07,
        '../../' + ADDENDUM_08,
    ),
    'wiki-source/Analisis_Neodialecticos_Publicos.md': (
        '../' + MAIN_AUDIT,
        '../' + ADDENDUM_07,
        '../' + ADDENDUM_08,
    ),
}

START = '<!-- KDP_51071689_TRACE_START -->'
END = '<!-- KDP_51071689_TRACE_END -->'


def make_block(main, a07, a08):
    return f'''{START}\n\n## Trazabilidad KDP 51071689 · estado actual / KDP 51071689 traceability · current state\n\n**Estado 2026-08-08 / Status 2026-08-08:** KDP confirmó que mantener el estado «cambios sin publicar» sin tocar no afecta a la disponibilidad actual; la causa raíz, el campo pendiente y la relación con correcciones internas previas continúan sin explicación técnica. El seguimiento fue solicitado de nuevo por el autor. / KDP confirmed that leaving the “unpublished changes” state untouched does not affect current availability; the root cause, pending field and relation to earlier internal corrections remain technically unexplained. Continued follow-up was requested by the author.\n\n- [Auditoría maestra / Master audit]({main})\n- [Reapertura · 2026-08-07 / Reopening · 2026-08-07]({a07})\n- [Respuesta KDP y estado actual · 2026-08-08 / KDP response and current state · 2026-08-08]({a08})\n\n{END}'''


def upsert_block(path_str, links):
    p = Path(path_str)
    if not p.exists():
        return False, f'missing target: {path_str}'
    text = p.read_text(encoding='utf-8')
    block = make_block(*links)
    pat = re.compile(re.escape(START) + r'.*?' + re.escape(END), re.S)
    if pat.search(text):
        new = pat.sub(block, text)
    else:
        nav = '<!-- NEO_CURRENT_NAV_START -->'
        if nav in text:
            new = text.replace(nav, block + '\n\n' + nav, 1)
        else:
            new = text.rstrip() + '\n\n---\n\n' + block + '\n'
    if new != text:
        p.write_text(new, encoding='utf-8')
        return True, None
    return False, None


def add_forward_link_to_07():
    p = Path(ADDENDUM_07)
    if not p.exists():
        return False
    text = p.read_text(encoding='utf-8')
    link_es = '- [Continuación · respuesta KDP y estado actual · 8 de agosto](./2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md)'
    link_en = '- [Continuation · KDP response and current state · 8 August](./2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md)'
    new = text
    if link_es not in new:
        new = new.replace('- [Índice de auditorías públicas](./README.md)', link_es + '\n- [Índice de auditorías públicas](./README.md)', 1)
    if link_en not in new:
        new = new.replace('- [Public audit index](./README.md)', link_en + '\n- [Public audit index](./README.md)', 1)
    if new != text:
        p.write_text(new, encoding='utf-8')
        return True
    return False


def repo_md_files():
    skip_parts = {'.git', 'node_modules', '.venv', 'venv'}
    out = []
    for p in ROOT.rglob('*.md'):
        if any(part in skip_parts for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def readmes():
    return sorted([p for p in ROOT.rglob('README.md') if '.git' not in p.parts])

LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')


def clean_target(raw):
    t = raw.strip().strip('<>')
    if not t:
        return None
    if t.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:', '#')):
        return None
    # Handle optional title after URL: (path "title")
    if ' ' in t and not t.startswith('./') and not t.startswith('../'):
        # Keep spaces in legitimate file names; only strip quoted title forms.
        m = re.match(r'^(.*?)(?:\s+["\'].*["\'])$', t)
        if m:
            t = m.group(1)
    t = t.split('#', 1)[0].split('?', 1)[0]
    t = urllib.parse.unquote(t)
    return t or None


def resolve_link(src, target):
    if target.startswith('/'):
        candidate = ROOT / target.lstrip('/')
    else:
        candidate = src.parent / target
    return candidate.resolve()


def is_inside_root(p):
    try:
        p.relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


def check_internal_links(files):
    checked = 0
    broken = []
    root_abs = ROOT.resolve()
    for src in files:
        try:
            text = src.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        for raw in LINK_RE.findall(text):
            target = clean_target(raw)
            if target is None:
                continue
            checked += 1
            candidate = resolve_link(src, target)
            if not is_inside_root(candidate):
                broken.append((str(src), raw, 'escapes repository root'))
                continue
            if candidate.exists():
                continue
            # GitHub permits links to directory paths if directory exists; handled above.
            broken.append((str(src), raw, str(candidate.relative_to(root_abs))))
    return checked, broken


def live_hubs():
    paths = set(TRACE_TARGETS)
    paths.update({
        'LEEME.md', 'PORTADA.md', 'COVER.md',
        'manifiestos/README.md', 'propuestas/sintesis-abierta/README.md',
        'wiki-source/README.md', 'obras/README.md', 'obras/idea/assets/README.md',
        'analisis/publicos/evidencias/README.md',
    })
    return [Path(p) for p in sorted(paths) if Path(p).exists()]


def stale_markers(paths):
    findings = []
    patterns = [
        ('XLIIII', re.compile(r'XLIIII')),
        ('I–XLII', re.compile(r'I–XLII')),
        ('42 manifiestos', re.compile(r'42\s+manifiestos', re.I)),
        ('42 bilingual manifestos', re.compile(r'42\s+bilingual\s+manifestos', re.I)),
    ]
    for p in paths:
        text = p.read_text(encoding='utf-8')
        for label, pat in patterns:
            if pat.search(text):
                findings.append((str(p), label))
    return findings


def required_kdp_links_ok():
    missing = []
    for path_str, links in TRACE_TARGETS.items():
        p = Path(path_str)
        if not p.exists():
            missing.append((path_str, 'file missing'))
            continue
        text = p.read_text(encoding='utf-8')
        for link in links:
            if link not in text:
                missing.append((path_str, link))
    return missing


def manifesto_checks():
    mdir = Path('manifiestos')
    nums = []
    for p in mdir.glob('*_ES_EN.md'):
        m = re.match(r'^(\d+)_', p.name)
        if m:
            nums.append(int(m.group(1)))
    # Numeric filenames are not canonical Roman ordering because foundational files use legacy numbers,
    # so validate the canonical index instead of numeric file count alone.
    idx = (mdir / 'README.md').read_text(encoding='utf-8')
    required = [
        'I–XLIII',
        '43 manifiestos',
        '43 bilingual manifestos',
        '43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md',
        'issues/51',
    ]
    missing = [r for r in required if r not in idx]
    return len(list(mdir.glob('*.md'))), missing


def write_report(md_count, readme_count, link_count, broken, stale, kdp_missing, manifesto_missing, changed_hubs):
    broken_es = 'Ninguno.' if not broken else '\n'.join(f'- `{s}` → `{r}` → {why}' for s, r, why in broken)
    stale_es = 'Ninguno en los hubs vivos comprobados.' if not stale else '\n'.join(f'- `{p}` → `{m}`' for p, m in stale)
    kdp_es = 'Completa en todos los hubs definidos.' if not kdp_missing else '\n'.join(f'- `{p}` → falta `{x}`' for p, x in kdp_missing)
    man_es = 'Correcto: índice canónico I–XLIII, 43 manifiestos y XLIII/Issue #51 presentes.' if not manifesto_missing else 'Faltan: ' + ', '.join(manifesto_missing)
    report = f'''# Auditoría global de README, enlaces y trazabilidad KDP 51071689\n## Global README, links and KDP 51071689 traceability audit\n\n**Fecha / Date:** 2026-08-08  \n**Ámbito / Scope:** repositorio completo · Markdown interno · hubs documentales · estado canónico de manifiestos · cadena pública KDP\n\n[ES · Castellano](#es--castellano) · [EN · English](#en--english)\n\n---\n\n# ES · Castellano\n\n## Dictamen\n\n- Archivos Markdown revisados: **{md_count}**.\n- README.md detectados: **{readme_count}**.\n- Enlaces Markdown internos relativos comprobados: **{link_count}**.\n- Enlaces internos rotos: **{len(broken)}**.\n- Hubs actualizados o normalizados con la cadena KDP: **{changed_hubs}**.\n- Marcadores canónicos obsoletos detectados en hubs vivos: **{len(stale)}**.\n\n## Trazabilidad KDP\n\n{kdp_es}\n\nCadena canónica actual:\n\n```text\nAUDITORÍA MAESTRA\n→ HITO OPERATIVO DEL 6 DE AGOSTO\n→ REAPERTURA DEL 7 DE AGOSTO\n→ RESPUESTA KDP DEL 8 DE AGOSTO\n→ SEGUIMIENTO TÉCNICO ABIERTO\n```\n\nKDP confirmó que dejar el estado «cambios sin publicar» sin tocar no afecta a la disponibilidad actual. La causa raíz, el campo pendiente y la relación con correcciones internas previas siguen sin explicación técnica.\n\n## Enlaces internos rotos\n\n{broken_es}\n\n## Estado canónico de manifiestos\n\n{man_es}\n\n## Marcadores obsoletos en hubs vivos\n\n{stale_es}\n\n## Alcance y límite\n\nLa validación comprueba rutas internas relativas contra el árbol real del repositorio y coherencia de los hubs definidos. No convierte la disponibilidad de URLs externas de terceros en una garantía permanente y no valida semánticamente todos los anclajes de GitHub generados a partir de encabezados Unicode.\n\n---\n\n# EN · English\n\n## Determination\n\n- Markdown files reviewed: **{md_count}**.\n- README.md files detected: **{readme_count}**.\n- Relative internal Markdown links checked: **{link_count}**.\n- Broken internal links: **{len(broken)}**.\n- Hubs updated or normalised with the KDP trace: **{changed_hubs}**.\n- Stale canonical markers found in live hubs: **{len(stale)}**.\n\nKDP traceability is {'complete across all defined hubs' if not kdp_missing else 'incomplete; see Spanish section'}.\n\nThe current KDP state is: prior multilingual correction preserved as an operational milestone; later unpublished-changes state acknowledged by KDP; current availability confirmed as unaffected when left untouched; technical root cause and pending field still unexplained; follow-up reopened.\n\nBroken internal links: **{len(broken)}**. Canonical manifesto index: {'OK' if not manifesto_missing else 'requires attention'}.\n\nThis validation checks repository-local relative paths and selected documentary consistency. It does not guarantee permanent third-party external URL availability or fully validate every GitHub-generated Unicode heading anchor.\n\n---\n\n## Enlaces canónicos / Canonical links\n\n- [Auditoría maestra / Master audit](../../analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md)\n- [Reapertura / Reopening · 2026-08-07](./2026-08-07_addendum_reapertura_caso_51071689_ES_EN.md)\n- [Respuesta KDP / KDP response · 2026-08-08](./2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md)\n- [Índice de auditorías / Audit index](./README.md)\n- [Repositorio / Repository](../../README.md)\n'''
    REPORT.write_text(report, encoding='utf-8')


def main():
    changed = 0
    errors = []
    for path_str, links in TRACE_TARGETS.items():
        did, err = upsert_block(path_str, links)
        changed += int(did)
        if err:
            errors.append(err)
    if add_forward_link_to_07():
        changed += 1

    files = repo_md_files()
    md_count = len(files)
    readme_count = len(readmes())
    link_count, broken = check_internal_links(files)
    stale = stale_markers(live_hubs())
    kdp_missing = required_kdp_links_ok()
    _, manifesto_missing = manifesto_checks()

    write_report(md_count, readme_count, link_count, broken, stale, kdp_missing, manifesto_missing, changed)

    print(f'Markdown files: {md_count}')
    print(f'READMEs: {readme_count}')
    print(f'Internal links checked: {link_count}')
    print(f'Broken links: {len(broken)}')
    print(f'Stale live-hub markers: {len(stale)}')
    print(f'KDP missing hub links: {len(kdp_missing)}')
    print(f'Manifesto missing requirements: {len(manifesto_missing)}')
    if errors:
        print('Update errors:', errors)

    # Remove one-shot machinery so the final commit leaves no disposable automation behind.
    for q in [
        Path('.github/workflows/one-shot-kdp-global-docs-audit.yml'),
        Path('.github/triggers/kdp-global-docs-audit.trigger'),
        Path('.github/scripts/one_shot_kdp_global_docs_audit.py'),
    ]:
        if q.exists():
            q.unlink()

    if errors or broken or stale or kdp_missing or manifesto_missing:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
