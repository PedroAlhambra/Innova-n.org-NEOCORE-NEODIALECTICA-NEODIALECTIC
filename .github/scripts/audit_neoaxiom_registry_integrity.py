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


def is_historical_candidate(path):
    if not path.name.startswith('C-NAX-'):
        return False
    text = path.read_text(encoding='utf-8', errors='replace')
    status = next((line for line in text.splitlines() if line.startswith('**Estado / Status:**')), '')
    return 'HISTÓRICO' in status and 'FIXED AS NAX-' in status


def primary_documents(prefix, active_candidates_only=False):
    out = {}
    for path in sorted(NEO_DIR.glob(f'{prefix}-*_ES_EN.md')):
        match = DOC_RE.match(path.name)
        if not match:
            continue
        if active_candidates_only and is_historical_candidate(path):
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

    es_gate = re.search(r'^#\s+ES\s+·\s+Castellano\s*$', readme, re.M)
    en_gate = re.search(r'^#\s+EN\s+·\s+English\s*$', readme, re.M)
    if not es_gate or not en_gate or en_gate.start() < es_gate.start():
        problems.append('NEOAXIOM_READABILITY_FAILURE: README sin capas ES/EN ordenadas / ordered ES/EN layers missing')
        readme_es = readme_en = ''
    else:
        readme_es = readme[es_gate.end():en_gate.start()]
        readme_en = readme[en_gate.end():]

    canonical = primary_documents('NAX')
    candidates = primary_documents('C-NAX', active_candidates_only=True)
    historical_candidates = {n: ps for n, ps in primary_documents('C-NAX').items() if n not in candidates}
    canonical_ids = sorted(canonical)
    candidate_ids = sorted(candidates)

    expected_canonical = list(range(1, max(canonical_ids) + 1)) if canonical_ids else []
    if canonical_ids != expected_canonical or not canonical_ids:
        problems.append(f'Frontera NAX documental no contigua / non-contiguous documentary NAX frontier: {canonical_ids}')
    for number, paths in canonical.items():
        if len(paths) != 1:
            problems.append(f'NAX-{number:02d}: documentos primarios duplicados / duplicate primary documents: {[p.name for p in paths]}')

    source_candidates = {}
    for path in sorted(SOURCE_DIR.glob('*C_NAX_*_ES_EN.md')):
        source_text = path.read_text(encoding='utf-8', errors='replace')
        match = re.search(r'^#\s+C-NAX-(\d+)\s+·', source_text, re.M)
        if not match:
            # Candidate extensions such as EXTENSION_C_NAX_20 are also depth-bearing
            # source documents and must not disappear from the primary C-NAX page.
            match = re.search(r'C_NAX_(\d+)', path.name)
        if match:
            source_candidates[int(match.group(1))] = path
    expected_candidates = list(range(max(canonical_ids) + 1, max(candidate_ids) + 1)) if candidate_ids else []
    if candidate_ids != expected_candidates:
        problems.append(f'NEOAXIOM_READABILITY_FAILURE: active C-NAX documents {candidate_ids}; expected {expected_candidates}')
    for number, paths in historical_candidates.items():
        if number not in canonical:
            problems.append(f'C-NAX-{number}: historical snapshot lacks promoted NAX-{number} / falta NAX promovido')
        for path in paths:
            text = path.read_text(encoding='utf-8', errors='replace')
            if f'HISTÓRICO · FIJADO COMO NAX-{number}' not in text or f'./NAX-{number}_' not in text:
                problems.append(f'C-NAX-{number}: historical fixation redirect incomplete / redirección genealógica incompleta')
    for number, paths in candidates.items():
        if len(paths) != 1:
            problems.append(f'C-NAX-{number}: documentos primarios duplicados / duplicate primary documents: {[p.name for p in paths]}')

    for number, paths in sorted(canonical.items()):
        if len(paths) == 1:
            validate_document(paths[0], f'NAX-{number:02d}', False, problems)
    for number, paths in sorted(candidates.items()):
        if len(paths) == 1:
            validate_document(paths[0], f'C-NAX-{number}', True, problems)

    # Source-backed candidates must not be compressed when copied into neoaxiomas/.
    # The target may adapt navigation and add material, but it must preserve at least
    # the structural depth already published in its dedicated source document.
    generic_source_headings = {
        'en sencillo', 'ejemplo', 'in plain language', 'example',
    }
    for number, source in sorted(source_candidates.items()):
        paths = candidates.get(number, []) or canonical.get(number, [])
        if len(paths) != 1:
            problems.append(f'NEOAXIOM_SOURCE_DEPTH_FAILURE: source C-NAX-{number} has no unique current NAX/C-NAX target')
            continue
        target = paths[0]
        source_text = source.read_text(encoding='utf-8', errors='replace')
        target_text = target.read_text(encoding='utf-8', errors='replace')
        source_size = len(re.sub(r'\s+', '', source_text))
        target_size = len(re.sub(r'\s+', '', target_text))
        if source_size and target_size < int(source_size * 0.85):
            problems.append(
                f'NEOAXIOM_SOURCE_DEPTH_FAILURE: NAX/C-NAX-{number} conserva sólo '
                f'{target_size/source_size:.0%} del volumen estructural de {source.name}'
            )
        source_fences = source_text.count('```')
        target_fences = target_text.count('```')
        if target_fences < source_fences:
            problems.append(
                f'NEOAXIOM_SOURCE_DEPTH_FAILURE: NAX/C-NAX-{number} pierde bloques estructurales/código '
                f'frente a {source.name}: {target_fences} < {source_fences}'
            )
        for heading in re.findall(r'^###\s+(.+?)\s*$', source_text, re.M):
            if heading.strip().lower() in generic_source_headings:
                continue
            if not re.search(r'^###\s+' + re.escape(heading.strip()) + r'\s*$', target_text, re.M):
                problems.append(
                    f'NEOAXIOM_SOURCE_DEPTH_FAILURE: NAX/C-NAX-{number} pierde la sección «{heading.strip()}» '
                    f'de {source.name}'
                )

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
        for language, layer in (('ES', readme_es), ('EN', readme_en)):
            if len(pattern.findall(layer)) != 1:
                problems.append(f'NEOAXIOM_LANGUAGE_INDEX_FAILURE: {ident} debe enlazar una vez en la capa {language}')

    for number, paths in sorted(candidates.items()):
        if len(paths) != 1:
            continue
        ident = f'C-NAX-{number}'
        pattern = re.compile(r'\[\*\*' + re.escape(ident) + r'\s+·[^\]]+\*\*\]\(\./' + re.escape(paths[0].name) + r'\)')
        if not pattern.search(readme):
            problems.append(f'NEOAXIOM_READABILITY_FAILURE: {ident} no enlaza primero a su documento propio')
        for language, layer in (('ES', readme_es), ('EN', readme_en)):
            if len(pattern.findall(layer)) != 1:
                problems.append(f'NEOAXIOM_LANGUAGE_INDEX_FAILURE: {ident} debe enlazar una vez en la capa {language}')

    required_headings = {
        'ES': ('Cómo leer esta capa', 'Neoaxiomas vigentes', 'Candidatos neoaxiomáticos', 'Relación estructural', 'Cómo participar'),
        'EN': ('How to read this layer', 'Current Neoaxioms', 'Neoaxiomatic candidates', 'Structural relation', 'How to participate'),
    }
    for language, layer in (('ES', readme_es), ('EN', readme_en)):
        for heading in required_headings[language]:
            if not re.search(r'^#{2,3}\s+' + re.escape(heading), layer, re.M):
                problems.append(f'NEOAXIOM_LANGUAGE_INDEX_FAILURE: falta «{heading}» en la capa {language}')

    candidate_count = len(expected_candidates)
    if candidate_count == 1:
        frontier = f'C-NAX-{expected_candidates[0]}'
        coverage_es = f'1 candidato C-NAX-{expected_candidates[0]}'
        coverage_en = f'1 candidate C-NAX-{expected_candidates[0]}'
        portal_state = f'**1 candidato neoaxiomático / neoaxiomatic candidate:** {frontier}.'
    elif candidate_count > 1:
        frontier = f'C-NAX-{expected_candidates[0]}–C-NAX-{expected_candidates[-1]}'
        coverage_es = f'{candidate_count} candidatos {frontier}'
        coverage_en = f'{candidate_count} candidates {frontier}'
        portal_state = f'**{candidate_count} candidatos neoaxiomáticos / neoaxiomatic candidates:** {frontier}.'
    else:
        frontier = 'C-NAX-∅'
        coverage_es = '0 candidatos C-NAX'
        coverage_en = '0 candidates C-NAX'
        portal_state = '**0 candidatos neoaxiomáticos / neoaxiomatic candidates:** C-NAX-∅.'
    if coverage_es not in syn or coverage_en not in syn:
        problems.append('Índice completo conserva cobertura C-NAX obsoleta / complete index has stale C-NAX coverage')
    if portal_state not in portal:
        problems.append('Portal neoaxiomático conserva frontera obsoleta / Neoaxiom portal has stale frontier')

    syn_ids = sorted(set(int(x) for x in re.findall(r'^\| \*\*(?:\[)?C-NAX-(\d+)\s+·', syn, re.M)))
    if syn_ids != expected_candidates:
        problems.append(f'Índice SAN C-NAX desalineado / C-NAX SAN index mismatch: {syn_ids}')
    syn_nax_ids = sorted(set(int(x) for x in re.findall(r'^\| (?:\*\*\[)?NAX-(\d+)\s+·', syn, re.M)))
    if syn_nax_ids != canonical_ids:
        problems.append(f'Índice SAN NAX desalineado / NAX SAN index mismatch: {syn_nax_ids}')

    status = 'OK' if not problems else 'FAIL'
    lines = [
        '# Auditoría de integridad documental neoaxiomática ES/EN',
        '# Neoaxiomatic ES/EN document integrity audit',
        '',
        '**Fecha / Date:** 2026-09-06',
        f'**Estado / Status:** **{status}**',
        f'**Frontera dinámica / Dynamic frontier:** **{frontier}**',
        '',
        '## Resultado / Result',
        '',
        f'- NAX canónicos con documento propio / canonical NAX with own document: **{len(canonical_ids)}** · `{canonical_ids}`.',
        f'- C-NAX activos con documento propio / active C-NAX with own document: **{len(candidate_ids)}** · `{candidate_ids}`.',
        f'- C-NAX históricos fijados / historical fixed C-NAX snapshots: **{len(historical_candidates)}** · `{sorted(historical_candidates)}`.',
        f'- Fuentes C-NAX detectadas / detected C-NAX sources: **{len(source_candidates)}** · `{sorted(source_candidates)}`.',
        '',
        '## Regla endurecida / Hardened rule',
        '',
        '- **README = índice; NAX/C-NAX = documento doctrinal propio; procedencia y SAN = rutas secundarias. / README = index; NAX/C-NAX = own doctrinal document; provenance and SAN = secondary routes.**',
        '- **Cada capa ES y EN del README debe enlazar exactamente una vez a cada documento NAX/C-NAX y conservar el mismo mapa estructural. / Each ES and EN README layer must link exactly once to every NAX/C-NAX document and preserve the same structural map.**',
        '- **La frontera viva se deriva de los NAX canónicos y C-NAX activos; los C-NAX históricos fijados permanecen como genealogía y no cuentan como candidatos activos. / The live frontier derives from canonical NAX and active C-NAX; fixed historical C-NAX remain as genealogy and do not count as active candidates.**',
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
