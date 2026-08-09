from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
latest = root / 'manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md'
index = root / 'manifiestos/README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
issue69 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/69'

for p in (latest, index, protocol, synth_index, audits):
    if not p.exists():
        raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

START = '<!-- NEO_LATEST_MANIFESTO_START -->'
END = '<!-- NEO_LATEST_MANIFESTO_END -->'


def rel(f: Path, target: Path) -> str:
    return os.path.relpath(target, start=f.parent).replace(os.sep, '/')


def block(f: Path) -> str:
    return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LIII · Leónidas™ · Defensor de la Síntesis, la Auditoría Abierta y el Derecho a Traer Problemas**  
> **LIII · Leónidas™ · Defender of Synthesis, Open Audit and the Right to Bring Problems**
>
> Leónidas™ abre la puerta para aportar pruebas a auditorías existentes o proponer nuevos problemas y auditorías externas bajo trazabilidad, contradicción y separación entre hechos e hipótesis. / Leónidas™ opens the gate for evidence contributions to existing audits or new external problems and audits under traceability, contradiction and separation between facts and hypotheses.
>
> **[Leer manifiesto LIII / Read manifesto LIII]({rel(f, latest)}) · [Participar en la Síntesis Abierta LIII · Issue #69 / Join Open Synthesis LIII · Issue #69]({issue69})**  
> [Cómo aportar / How to contribute]({rel(f, protocol)}) · [Índice de Síntesis Abierta / Open Synthesis index]({rel(f, synth_index)}) · [Auditorías públicas / Public audits]({rel(f, audits)}) · [53 manifiestos I–LIII / 53 manifestos I–LIII]({rel(f, index)})

{END}'''


readmes = sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme = root / 'LEEME.md'
if leeme.exists():
    readmes.append(leeme)
readmes = sorted(set(readmes))
if not readmes:
    raise SystemExit('No README/LEEME targets found')

changed = []
for f in readmes:
    text = f.read_text(encoding='utf-8')
    old = text
    b = block(f)
    if START in text and END in text:
        text = re.sub(re.escape(START) + r'.*?' + re.escape(END), b, text, count=1, flags=re.S)
    else:
        m = re.search(r'^\[ES[^\n]*\]\([^\n]+\)\s*·\s*\[EN[^\n]*\]\([^\n]+\)\s*$', text, re.M)
        if m:
            pos = m.end()
            text = text[:pos] + '\n\n' + b + text[pos:]
        else:
            lines = text.splitlines(True)
            insert = 1 if lines and lines[0].lstrip().startswith('#') else 0
            lines.insert(insert, '\n' + b + '\n\n')
            text = ''.join(lines)
    if text != old:
        f.write_text(text, encoding='utf-8')
        changed.append(f)

fail = []
link_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for f in readmes:
    text = f.read_text(encoding='utf-8')
    if text.count(START) != 1 or text.count(END) != 1:
        fail.append(f'{f.relative_to(root)}: latest-manifesto markers invalid')
        continue
    m = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, re.S)
    blk = m.group(1)
    if 'Issue #69' not in blk or latest.name not in blk:
        fail.append(f'{f.relative_to(root)}: LIII/Issue #69 feature incomplete')
    for href in link_re.findall(blk):
        h = href.split('#', 1)[0].strip()
        if not h or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', h):
            continue
        if not (f.parent / h).resolve().exists():
            fail.append(f'{f.relative_to(root)}: broken featured local link {href}')

idx = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
if not net:
    fail.append('manifiestos/README.md: canonical network block missing')
else:
    items = re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', net.group(1))
    unique = []
    seen = set()
    for roman, href in items:
        p = (index.parent / href).resolve()
        if p not in seen:
            seen.add(p)
            unique.append((roman, p))
    if len(unique) != 53 or unique[0][0] != 'I' or unique[-1][0] != 'LIII':
        fail.append(f'manifiestos/README.md: canonical sequence invalid ({len(unique)} items)')
    for roman, p in unique:
        if not p.exists():
            fail.append(f'manifesto {roman}: missing target')

print(f'README_LEEME_TARGETS={len(readmes)}')
print(f'FILES_CHANGED={len(changed)}')
for p in changed:
    print('CHANGED', p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    for x in fail:
        print(x)
    sys.exit(1)
print('POSTCHECK OK: latest LIII + Open Synthesis #69 featured near top of every README/LEEME; canonical I-LIII network intact')
