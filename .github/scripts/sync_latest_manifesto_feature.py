"""Synchronise only existing NEO_LATEST_MANIFESTO blocks.

The latest finite manifesto is derived from manifiestos/README.md. This script
is deliberately narrow: it does not migrate versions, inject Neoaxiom content,
or alter any text outside the marked latest-manifesto block.
"""

from pathlib import Path
import os
import re


ROOT = Path('.').resolve()
MIDX = ROOT / 'manifiestos/README.md'
START = '<!-- NEO_LATEST_MANIFESTO_START -->'
END = '<!-- NEO_LATEST_MANIFESTO_END -->'
ROW = re.compile(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)(.*)$', re.M)
ISSUE = re.compile(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)')

FOLLOW = ROOT / 'proyeccion/SEGUIR_MARCO_SINTESIS_ES_EN.md'
ENTRY = ROOT / 'propuestas/sintesis-abierta/REGISTRO_ENTRADA_TRAZABLE_DERIVACION_ES_EN.md'
CONTRIBUTE = ROOT / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
LEONIDAS = ROOT / 'propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md'
AUDITS = ROOT / 'auditorias/publicas/README.md'


def rel(source, target):
    return os.path.relpath(target, start=source.parent).replace(os.sep, '/')


def main():
    index_text = MIDX.read_text(encoding='utf-8')
    rows = ROW.findall(index_text)
    if not rows:
        raise SystemExit('CANONICAL_STATE_FAILURE: no finite manifesto rows in manifiestos/README.md')
    roman, title, href, suffix = rows[-1]
    count = len(rows)
    latest = ROOT / 'manifiestos' / href
    if not latest.exists():
        raise SystemExit(f'CANONICAL_STATE_FAILURE: latest manifesto target missing: {latest}')
    issues = ISSUE.findall(suffix)
    if len(issues) != 1:
        raise SystemExit(f'CANONICAL_STATE_FAILURE: expected one SAN issue for {roman}, found {issues}')
    issue = issues[0]
    issue_url = f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue}'

    def block(source):
        return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(source, latest)}) · [Síntesis Abierta {roman} · #{issue} / Open Synthesis {roman} · #{issue}]({issue_url})**
> [Seguir marco / Follow framework]({rel(source, FOLLOW)}) · [Registrar entrada / Register entry]({rel(source, ENTRY)}) · [Cómo aportar / How to contribute]({rel(source, CONTRIBUTE)}) · [Leónidas™]({rel(source, LEONIDAS)}) · [Auditorías públicas / Public audits]({rel(source, AUDITS)}) · [{count} manifiestos / manifestos · I–{roman}]({rel(source, MIDX)})

{END}'''

    changed = []
    targets = []
    for path in sorted(ROOT.rglob('README*.md')):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        starts = text.count(START)
        ends = text.count(END)
        if not starts and not ends:
            continue
        if starts != 1 or ends != 1:
            raise SystemExit(f'LINK_INTEGRITY_FAILURE: malformed latest block markers in {path.relative_to(ROOT)}')
        targets.append(path)
        updated = re.sub(re.escape(START) + r'.*?' + re.escape(END), block(path), text, count=1, flags=re.S)
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            changed.append(path)

    if not targets:
        raise SystemExit('LINK_INTEGRITY_FAILURE: no NEO_LATEST_MANIFESTO blocks found')
    for path in targets:
        body = path.read_text(encoding='utf-8').split(START, 1)[1].split(END, 1)[0]
        if roman not in body or f'issues/{issue}' not in body or rel(path, latest) not in body:
            raise SystemExit(f'LINK_INTEGRITY_FAILURE: unsynchronised latest block in {path.relative_to(ROOT)}')

    print(f'LATEST_MANIFESTO_SYNC latest={roman} issue=#{issue} count={count} targets={len(targets)} changed={len(changed)}')
    for path in changed:
        print('CHANGED', path.relative_to(ROOT).as_posix())


if __name__ == '__main__':
    main()
