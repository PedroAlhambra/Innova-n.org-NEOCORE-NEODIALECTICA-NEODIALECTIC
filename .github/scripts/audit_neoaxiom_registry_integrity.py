from pathlib import Path
import re

ROOT = Path('.').resolve()
NEO = ROOT / 'neoaxiomas/README.md'
SYN = ROOT / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
PORTAL = ROOT / 'propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md'
REPORT = ROOT / 'auditorias/publicas/2026-08-16_auditoria_neoaxiomas_simetria_frontera_ES_EN.md'

START = '<!-- NEOAXIOM_CANDIDATES_72_START -->'
END = '<!-- NEOAXIOM_CANDIDATES_72_END -->'


def candidate_blocks(block):
    matches = list(re.finditer(r'^###\s+C-NAX-(\d+)\s+·\s+(.+?)\s*$', block, re.M))
    out = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(block)
        out[int(m.group(1))] = block[m.start():end]
    return out


def main():
    problems = []
    neo = NEO.read_text(encoding='utf-8')
    syn = SYN.read_text(encoding='utf-8')
    portal = PORTAL.read_text(encoding='utf-8')

    if START not in neo or END not in neo:
        problems.append('Faltan marcadores del registro C-NAX / C-NAX registry markers missing')
        block = ''
    else:
        block = neo.split(START, 1)[1].split(END, 1)[0]

    es_m = re.search(r'^# ES · (?:Castellano|Español)\s*$', neo, re.M)
    en_m = re.search(r'^# EN · English\s*$', neo, re.M)
    es_ids = []
    en_ids = []
    if not es_m or not en_m or en_m.start() < es_m.start():
        problems.append('No se localiza correctamente el split canónico ES/EN de neoaxiomas/README.md / canonical ES/EN split not found')
    else:
        es_body = neo[es_m.end():en_m.start()]
        en_body = neo[en_m.end():]
        es_ids = sorted(set(int(x) for x in re.findall(r'^##\s+NAX-(\d+)\s+·', es_body, re.M)))
        en_ids = sorted(set(int(x) for x in re.findall(r'^##\s+NAX-(\d+)\s+·', en_body, re.M)))
        if es_ids != list(range(1, 15)):
            problems.append(f'NAX canónicos ES inesperados / unexpected canonical ES NAX: {es_ids}')
        if en_ids != list(range(1, 15)):
            problems.append(f'NAX canónicos EN inesperados / unexpected canonical EN NAX: {en_ids}')
        if es_ids != en_ids:
            problems.append(f'IDs NAX ES/EN no coinciden / ES/EN NAX IDs differ: ES={es_ids} EN={en_ids}')

    row_ids = [int(x) for x in re.findall(r'^\| \*\*C-NAX-(\d+) ·', block, re.M)]
    details = candidate_blocks(block)
    detail_ids = sorted(details)
    unique_rows = sorted(set(row_ids))
    if row_ids != unique_rows:
        problems.append(f'Filas C-NAX duplicadas o fuera de orden / duplicate or unordered C-NAX rows: {row_ids}')
    if unique_rows:
        expected = list(range(15, max(unique_rows) + 1))
        if unique_rows != expected:
            problems.append(f'Frontera C-NAX no contigua / non-contiguous C-NAX frontier: rows={unique_rows} expected={expected}')
    else:
        problems.append('No existen filas C-NAX / no C-NAX rows found')
    if detail_ids != unique_rows:
        problems.append(f'Cada fila C-NAX debe tener bloque desarrollado / every C-NAX row needs a developed block: rows={unique_rows} details={detail_ids}')

    for n in detail_ids:
        b = details[n]
        has_es = bool(re.search(r'(?:\*\*ES · formulación candidata:\*\*|> \*\*ES:)', b))
        has_en = bool(re.search(r'(?:\*\*EN · candidate formulation:\*\*|> \*\*EN:)', b))
        if not has_es or not has_en:
            problems.append(f'C-NAX-{n} no declara ambas formulaciones ES/EN / does not declare both ES/EN formulations')
        if 'CANDIDATO ≠ CANON / CANDIDATE ≠ CANON' not in b:
            problems.append(f'C-NAX-{n} carece de salvaguarda candidato≠canon / lacks candidate≠canon safeguard')
        required_access = [r'\*\*ES · en sencillo:\*\*', r'\*\*ES · ejemplo:\*\*', r'\*\*EN · in plain language:\*\*', r'\*\*EN · example:\*\*']
        if any(not re.search(pattern, b) for pattern in required_access):
            problems.append(f'C-NAX-{n} carece de lectura sencilla y ejemplo simétricos ES/EN / lacks symmetric ES/EN plain-language reading and example')

    dedicated = set()
    for p in (ROOT / 'propuestas/sintesis-abierta').glob('*C_NAX_*_ES_EN.md'):
        text = p.read_text(encoding='utf-8', errors='replace')
        m = re.search(r'^#\s+C-NAX-(\d+)\s+·', text, re.M)
        if m:
            dedicated.add(int(m.group(1)))
    missing_dedicated = sorted(dedicated - set(unique_rows))
    if missing_dedicated:
        problems.append(f'Documentos C-NAX dedicados ausentes del registro central / dedicated C-NAX docs missing from central registry: {missing_dedicated}')

    candidate_count = len(unique_rows)
    max_candidate = max(unique_rows) if unique_rows else None
    if unique_rows and unique_rows[0] != 15:
        problems.append(f'La frontera C-NAX debe comenzar en 15 / C-NAX frontier must begin at 15, found {unique_rows[0]}')

    if max_candidate is not None:
        es_coverage = f'{candidate_count} candidatos C-NAX-15–C-NAX-{max_candidate}'
        en_coverage = f'{candidate_count} candidates C-NAX-15–C-NAX-{max_candidate}'
        if es_coverage not in syn:
            problems.append(f'Índice de Síntesis no declara {es_coverage} / synthesis index missing Spanish dynamic coverage')
        if en_coverage not in syn:
            problems.append(f'Synthesis index English coverage does not declare {en_coverage}')
    syn_ids = sorted(set(int(x) for x in re.findall(r'^\| \*\*C-NAX-(\d+) ·', syn, re.M)))
    if syn_ids != unique_rows:
        problems.append(f'Índice C-NAX no refleja registro central / C-NAX synthesis index does not mirror central registry: index={syn_ids} registry={unique_rows}')

    portal_state = ''
    stale_current_state = False
    if max_candidate is not None:
        portal_state = f'**{candidate_count} candidatos neoaxiomáticos / neoaxiomatic candidates:** C-NAX-15–C-NAX-{max_candidate}.'
        if portal_state not in portal:
            problems.append(f'Portal de Síntesis Neoaxiomática desactualizado / Neoaxiom Synthesis portal frontier mismatch: expected {portal_state}')
        # Genealogical subranges such as C-NAX-15–18 are legitimate. Only an old
        # operational declaration of the previous frontier must fail the gate.
        stale_current_state = bool(re.search(r'^- \*\*\d+ candidatos neoaxiomáticos / neoaxiomatic candidates:\*\* C-NAX-15[–-]C-NAX-(?!'+str(max_candidate)+r'\b)\d+\.$', portal, re.M))
        if stale_current_state:
            problems.append('Portal de Síntesis Neoaxiomática conserva una declaración operativa de frontera antigua / Neoaxiom Synthesis portal retains a stale operational frontier declaration')

    status = 'OK' if not problems else 'FAIL'
    frontier_label = f'C-NAX-15–C-NAX-{max_candidate}' if max_candidate is not None else 'C-NAX-∅'
    portal_ok = max_candidate is not None and portal_state in portal and not stale_current_state
    lines = [
        '# Auditoría de integridad neoaxiomática ES/EN y frontera C-NAX',
        '# Neoaxiomatic ES/EN integrity and C-NAX frontier audit',
        '',
        '**Fecha / Date:** 2026-08-16  ',
        f'**Estado / Status:** **{status}**  ',
        f'**Frontera dinámica / Dynamic frontier:** **{frontier_label}**  ',
        '**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, capa de claridad ES/EN, documentos dedicados, índice vivo y portal público de Síntesis Neoaxiomática. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, ES/EN clarity layer, dedicated documents, the live index and the public Neoaxiom Synthesis portal.',
        '',
        '## Resultado / Result',
        '',
        f'- NAX canónicos ES / canonical ES NAX: **{len(es_ids)}** · `{es_ids}`.',
        f'- NAX canónicos EN / canonical EN NAX: **{len(en_ids)}** · `{en_ids}`.',
        f'- C-NAX registrados / registered C-NAX: **{len(unique_rows)}** · `{unique_rows}`.',
        f'- C-NAX con bloque desarrollado / C-NAX with developed block: **{len(detail_ids)}** · `{detail_ids}`.',
        f'- Documentos C-NAX dedicados detectados / dedicated C-NAX documents detected: `{sorted(dedicated)}`.',
        f'- Portal público de Síntesis Neoaxiomática / public Neoaxiom Synthesis portal: **{"OK" if portal_ok else "REVISAR / REVIEW"}**.',
        '',
        '## Regla endurecida / Hardened rule',
        '',
        '- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**',
        '- **Todo C-NAX debe incluir lectura sencilla y ejemplo simétricos ES/EN, subordinados a la formulación formal. / Every C-NAX must include symmetric ES/EN plain-language reading and an example, subordinate to the formal formulation.**',
        '- **Un documento C-NAX dedicado ausente del registro central es fallo de frontera. / A dedicated C-NAX document missing from the central registry is an integrity failure.**',
        '- **El portal público de Síntesis Neoaxiomática debe reflejar la misma frontera dinámica que el registro central y el índice vivo. / The public Neoaxiom Synthesis portal must mirror the same dynamic frontier as the central registry and live index.**',
        '- **Las subfronteras genealógicas legítimas no se confunden con la declaración operativa vigente. / Legitimate genealogical subranges are not confused with the current operational declaration.**',
        '- **La frontera C-NAX se deriva dinámicamente del registro; ningún máximo queda codificado a mano. / The C-NAX frontier is derived dynamically from the registry; no maximum is hard-coded.**',
        '- **NAX/C-NAX quedan fuera de cualquier excepción genérica de encabezados: esta auditoría los comprueba por identificador. / NAX/C-NAX are outside any generic heading exception: this audit checks them by identifier.**',
        '',
        '## Incidencias / Findings',
        ''
    ]
    if problems:
        lines += [f'- {p}' for p in problems]
    else:
        lines.append('- Ninguna / None.')
    lines += [
        '',
        '## Genealogía de la reparación / Repair genealogy',
        '',
        '- La auditoría global anterior podía omitir el bloque C-NAX porque se encontraba antes del split principal `# ES / # EN` y porque el chequeo genérico toleraba encabezados `NAX-`/`C-NAX-`. / The previous global audit could miss the C-NAX block because it sat before the main `# ES / # EN` split and because the generic checker tolerated `NAX-`/`C-NAX-` headings.',
        '- C-NAX-15–18 quedaron desarrollados y reconciliados conservando su genealogía. / C-NAX-15–18 were developed and reconciled while preserving their genealogy.',
        '- C-NAX-23 y C-NAX-24 se incorporaron mediante documentos dedicados y registro central. / C-NAX-23 and C-NAX-24 were incorporated through dedicated documents and the central registry.',
        '- C-NAX-25 y C-NAX-26 amplían la frontera mediante documentos bilingües dedicados y Síntesis #155/#156; la auditoría deja de fijar un máximo manual para que futuras ampliaciones no queden silenciosamente fuera. / C-NAX-25 and C-NAX-26 extend the frontier through dedicated bilingual documents and Syntheses #155/#156; the audit no longer hard-codes a maximum so future extensions cannot silently fall outside it.',
        '- El portal `NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md` queda incluido en el gate para impedir que un portal secundario conserve un recuento o frontera operativa obsoletos. / The `NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md` portal is now included in the gate so a secondary portal cannot retain a stale operational count or frontier.',
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'NEOAXIOM_INTEGRITY status={status} canonical={len(es_ids)}/{len(en_ids)} candidates={len(unique_rows)} details={len(detail_ids)} dedicated={sorted(dedicated)} frontier={frontier_label} portal={"OK" if portal_ok else "REVIEW"}')
    if problems:
        for p in problems:
            print('FAIL:', p)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
