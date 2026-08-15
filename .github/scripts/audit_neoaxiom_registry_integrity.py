from pathlib import Path
import re

ROOT = Path('.').resolve()
NEO = ROOT / 'neoaxiomas/README.md'
SYN = ROOT / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
REPORT = ROOT / 'auditorias/publicas/2026-08-16_auditoria_neoaxiomas_simetria_frontera_ES_EN.md'

START = '<!-- NEOAXIOM_CANDIDATES_72_START -->'
END = '<!-- NEOAXIOM_CANDIDATES_72_END -->'


def extract_section(text, heading_pattern):
    m = re.search(heading_pattern, text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r'^#{1,3}\s+', rest, re.M)
    return rest[:nxt.start()] if nxt else rest


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

    if START not in neo or END not in neo:
        problems.append('Faltan marcadores del registro C-NAX / C-NAX registry markers missing')
        block = ''
    else:
        block = neo.split(START, 1)[1].split(END, 1)[0]

    # Canonical NAX parity in the main split.
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

    # Candidate rows and detail blocks must be one-to-one and contiguous.
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
        expected = []
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

    # Any dedicated C-NAX document must be represented in the central registry.
    dedicated = set()
    for p in (ROOT / 'propuestas/sintesis-abierta').glob('*C_NAX_*_ES_EN.md'):
        text = p.read_text(encoding='utf-8', errors='replace')
        m = re.search(r'^#\s+C-NAX-(\d+)\s+·', text, re.M)
        if m:
            dedicated.add(int(m.group(1)))
    missing_dedicated = sorted(dedicated - set(unique_rows))
    if missing_dedicated:
        problems.append(f'Documentos C-NAX dedicados ausentes del registro central / dedicated C-NAX docs missing from central registry: {missing_dedicated}')

    # Current expected frontier after the 2026-08-16 repair.
    if unique_rows != list(range(15, 25)):
        problems.append(f'Frontera vigente esperada C-NAX-15–24 / expected current frontier C-NAX-15–24, found {unique_rows}')

    # The live synthesis index must mirror count/range and carry each candidate row.
    if '10 candidatos C-NAX-15–C-NAX-24' not in syn:
        problems.append('Índice de Síntesis no declara 10 candidatos C-NAX-15–24 / synthesis index does not declare 10 candidates C-NAX-15–24')
    if '10 candidates C-NAX-15–C-NAX-24' not in syn:
        problems.append('Synthesis index English coverage does not declare 10 candidates C-NAX-15–24')
    syn_ids = sorted(set(int(x) for x in re.findall(r'^\| \*\*C-NAX-(\d+) ·', syn, re.M)))
    if syn_ids != unique_rows:
        problems.append(f'Índice C-NAX no refleja registro central / C-NAX synthesis index does not mirror central registry: index={syn_ids} registry={unique_rows}')

    status = 'OK' if not problems else 'FAIL'
    lines = [
        '# Auditoría de integridad neoaxiomática ES/EN y frontera C-NAX',
        '# Neoaxiomatic ES/EN integrity and C-NAX frontier audit',
        '',
        '**Fecha / Date:** 2026-08-16  ',
        f'**Estado / Status:** **{status}**  ',
        '**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, documentos dedicados e índice vivo de Síntesis. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, dedicated documents and the live Synthesis index.',
        '',
        '## Resultado / Result',
        '',
        f'- NAX canónicos ES / canonical ES NAX: **{len(es_ids)}** · `{es_ids}`.',
        f'- NAX canónicos EN / canonical EN NAX: **{len(en_ids)}** · `{en_ids}`.',
        f'- C-NAX registrados / registered C-NAX: **{len(unique_rows)}** · `{unique_rows}`.',
        f'- C-NAX con bloque desarrollado / C-NAX with developed block: **{len(detail_ids)}** · `{detail_ids}`.',
        f'- Documentos C-NAX dedicados detectados / dedicated C-NAX documents detected: `{sorted(dedicated)}`.',
        '',
        '## Regla endurecida / Hardened rule',
        '',
        '- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**',
        '- **Un documento C-NAX dedicado ausente del registro central es fallo de frontera. / A dedicated C-NAX document missing from the central registry is a frontier failure.**',
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
        '- C-NAX-15 y C-NAX-16 recuperan formulaciones ya explícitas en sus fuentes públicas. / C-NAX-15 and C-NAX-16 recover formulations already explicit in their public sources.',
        '- C-NAX-17 y C-NAX-18 reciben formulación autónoma consolidada fielmente desde los principios publicados en LXVII y LXVI+LXVII, conservando la genealogía. / C-NAX-17 and C-NAX-18 receive standalone formulations faithfully consolidated from the principles published in LXVII and LXVI+LXVII, preserving genealogy.',
        '- C-NAX-23 y C-NAX-24 se incorporan al registro central sin cambiar su condición de candidatos. / C-NAX-23 and C-NAX-24 are incorporated into the central registry without changing their candidate status.',
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'NEOAXIOM_INTEGRITY status={status} canonical={len(es_ids)}/{len(en_ids)} candidates={len(unique_rows)} details={len(detail_ids)} dedicated={sorted(dedicated)}')
    if problems:
        for p in problems:
            print('FAIL:', p)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
