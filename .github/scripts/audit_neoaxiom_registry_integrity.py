from pathlib import Path
import re

ROOT = Path('.').resolve()
NEO_DIR = ROOT / 'neoaxiomas'
README = NEO_DIR / 'README.md'
SYN = ROOT / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
PORTAL = ROOT / 'propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md'
SOURCE_DIR = ROOT / 'propuestas/sintesis-abierta'
REPORT = ROOT / 'auditorias/publicas/2026-08-16_auditoria_neoaxiomas_simetria_frontera_ES_EN.md'

DOC_RE = re.compile(r'^(C-)?NAX-(\d+)_.*_ES_EN\.md$')
ISSUE_RE = re.compile(
    r'https://github\.com/PedroAlhambra/'
    r'Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)'
)


def primary_documents(prefix):
    out = {}
    for path in sorted(NEO_DIR.glob(f'{prefix}-*_ES_EN.md')):
        match = DOC_RE.match(path.name)
        if not match:
            continue
        number = int(match.group(2))
        # This is an explicitly linked extension, not a second NAX-10 primary entry.
        if path.name == 'NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md':
            continue
        out.setdefault(number, []).append(path)
    return out


def markdown_target_exists(source, target):
    if target.startswith(('http://', 'https://', '#')):
        return True
    clean = target.split('#', 1)[0]
    return (source.parent / clean).resolve().exists()


def validate_document(path, ident, candidate, problems):
    text = path.read_text(encoding='utf-8', errors='replace')
    headings = re.findall(r'^#\s+' + re.escape(ident) + r'\s+·\s+.+$', text, re.M)
    if len(headings) < 2:
        problems.append(f'{ident}: faltan títulos ES/EN en {path.name} / missing ES/EN titles')
    if not re.search(r'^##\s+ES\s+·\s+(?:Castellano|Formulación candidata)', text, re.M):
        problems.append(f'{ident}: falta sección ES / missing ES section')
    if not re.search(r'^##\s+EN\s+·\s+(?:English|Candidate formulation)', text, re.M):
        problems.append(f'{ident}: falta sección EN / missing EN section')
    if '[ES · Castellano](' not in text or '[EN · English](' not in text:
        problems.append(f'{ident}: falta selector ES/EN navegable / missing navigable ES/EN selector')
    if '**Estado / Status:**' not in text:
        problems.append(f'{ident}: falta estado bilingüe / missing bilingual status')
    if not ISSUE_RE.search(text):
        problems.append(f'{ident}: falta ruta SAN / missing SAN route')
    if candidate and not (
        'CANDIDATO ≠ CANON / CANDIDATE ≠ CANON' in text
        or ('CANDIDATO' in text and 'NO CANONIZADO' in text and 'CANDIDATE' in text and 'NOT CANONICALISED' in text)
    ):
        problems.append(f'{ident}: falta salvaguarda candidato≠canon / missing candidate≠canon safeguard')
    if not re.search(r'^>\s+\*\*?.+\*\*?\s*$', text, re.M):
        problems.append(f'{ident}: falta formulación destacada / missing explicit formulation')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if not markdown_target_exists(path, target):
            problems.append(f'{ident}: destino local inexistente / missing local target: {target}')


def main():
    problems = []
    readme = README.read_text(encoding='utf-8')
    syn = SYN.read_text(encoding='utf-8')
    portal = PORTAL.read_text(encoding='utf-8')

    canonical = primary_documents('NAX')
    candidates = primary_documents('C-NAX')
    canonical_ids = sorted(canonical)
    candidate_ids = sorted(candidates)

    if canonical_ids != list(range(1, 15)):
        problems.append(f'Frontera NAX documental inesperada / unexpected documentary NAX frontier: {canonical_ids}')
    for number, paths in canonical.items():
        if len(paths) != 1:
            problems.append(f'NAX-{number:02d}: documentos primarios duplicados / duplicate primary documents: {[p.name for p in paths]}')

    source_candidates = {}
    for path in sorted(SOURCE_DIR.glob('*C_NAX_*_ES_EN.md')):
        match = re.search(r'^#\s+C-NAX-(\d+)\s+·', path.read_text(encoding='utf-8', errors='replace'), re.M)
        if match:
            source_candidates[int(match.group(1))] = path
    frontier_ids = set(candidate_ids) | set(source_candidates)
    expected_candidates = list(range(15, max(frontier_ids) + 1)) if frontier_ids else []
    if candidate_ids != expected_candidates:
        problems.append(f'NEOAXIOM_READABILITY_FAILURE: documentos C-NAX {candidate_ids}; esperados / expected {expected_candidates}')
    for number, paths in candidates.items():
        if len(paths) != 1:
            problems.append(f'C-NAX-{number}: documentos primarios duplicados / duplicate primary documents: {[p.name for p in paths]}')

    for number, paths in sorted(canonical.items()):
        if len(paths) == 1:
            validate_document(paths[0], f'NAX-{number:02d}', False, problems)
    for number, paths in sorted(candidates.items()):
        if len(paths) == 1:
            validate_document(paths[0], f'C-NAX-{number}', True, problems)

    # README is a navigable index, never the monolithic doctrinal source.
    if 'README = ÍNDICE' not in readme or 'README = INDEX' not in readme:
        problems.append('NEOAXIOM_MONOLITH_FAILURE: falta la regla README=ÍNDICE / README=INDEX rule missing')
    if len(re.findall(r'^>\s+\*\*(?:La|The) ', readme, re.M)) > 2:
        problems.append('NEOAXIOM_MONOLITH_FAILURE: formulaciones completas reaparecen embebidas en README')

    for number, paths in sorted(canonical.items()):
        if len(paths) != 1:
            continue
        ident = f'NAX-{number:02d}'
        pattern = re.compile(r'\[\*\*' + re.escape(ident) + r'\s+·[^\]]+\*\*\]\(\./' + re.escape(paths[0].name) + r'\)')
        if not pattern.search(readme):
            problems.append(f'NEOAXIOM_READABILITY_FAILURE: {ident} no enlaza primero a su documento propio')

    for number, paths in sorted(candidates.items()):
        if len(paths) != 1:
            continue
        ident = f'C-NAX-{number}'
        pattern = re.compile(r'\[\*\*' + re.escape(ident) + r'\s+·[^\]]+\*\*\]\(\./' + re.escape(paths[0].name) + r'\)')
        if not pattern.search(readme):
            problems.append(f'NEOAXIOM_READABILITY_FAILURE: {ident} no enlaza primero a su documento propio')

    candidate_count = len(expected_candidates)
    max_candidate = max(expected_candidates) if expected_candidates else None
    frontier = f'C-NAX-15–C-NAX-{max_candidate}' if max_candidate else 'C-NAX-∅'
    if max_candidate:
        coverage_es = f'{candidate_count} candidatos C-NAX-15–C-NAX-{max_candidate}'
        coverage_en = f'{candidate_count} candidates C-NAX-15–C-NAX-{max_candidate}'
        if coverage_es not in syn or coverage_en not in syn:
            problems.append('Índice completo conserva cobertura C-NAX obsoleta / complete index has stale C-NAX coverage')
        portal_state = f'**{candidate_count} candidatos neoaxiomáticos / neoaxiomatic candidates:** {frontier}.'
        if portal_state not in portal:
            problems.append('Portal neoaxiomático conserva frontera obsoleta / Neoaxiom portal has stale frontier')

    syn_ids = sorted(set(int(x) for x in re.findall(r'^\| \*\*C-NAX-(\d+)\s+·', syn, re.M)))
    if syn_ids != expected_candidates:
        problems.append(f'Índice SAN C-NAX desalineado / C-NAX SAN index mismatch: {syn_ids}')

    status = 'OK' if not problems else 'FAIL'
    lines = [
        '# Auditoría de integridad documental neoaxiomática ES/EN',
        '# Neoaxiomatic ES/EN document integrity audit',
        '',
        '**Fecha / Date:** 2026-08-30',
        f'**Estado / Status:** **{status}**',
        f'**Frontera dinámica / Dynamic frontier:** **{frontier}**',
        '',
        '## Resultado / Result',
        '',
        f'- NAX canónicos con documento propio / canonical NAX with own document: **{len(canonical_ids)}** · `{canonical_ids}`.',
        f'- C-NAX con documento propio / C-NAX with own document: **{len(candidate_ids)}** · `{candidate_ids}`.',
        f'- Fuentes C-NAX detectadas / detected C-NAX sources: **{len(source_candidates)}** · `{sorted(source_candidates)}`.',
        '',
        '## Regla endurecida / Hardened rule',
        '',
        '- **README = índice; NAX/C-NAX = documento doctrinal propio; procedencia y SAN = rutas secundarias. / README = index; NAX/C-NAX = own doctrinal document; provenance and SAN = secondary routes.**',
        '- **La frontera se deriva de las fuentes públicas C-NAX y debe ser contigua en documentos, README, portal e índice SAN. / The frontier is derived from public C-NAX sources and must remain contiguous across documents, README, portal and SAN index.**',
        '- **El auditor valida la arquitectura documental vigente y no exige restaurar el antiguo README monolítico. / The auditor validates the current document architecture and never requires restoring the former monolithic README.**',
        '',
        '## Incidencias / Findings',
        '',
    ]
    lines += [f'- {problem}' for problem in problems] if problems else ['- Ninguna / None.']
    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'NEOAXIOM_INTEGRITY status={status} canonical={len(canonical_ids)} candidates={len(candidate_ids)} sources={len(source_candidates)} frontier={frontier}')
    if problems:
        for problem in problems:
            print('FAIL:', problem)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
