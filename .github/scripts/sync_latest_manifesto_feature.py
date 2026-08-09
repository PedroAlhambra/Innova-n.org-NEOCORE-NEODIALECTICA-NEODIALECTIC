from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
latest = root / 'manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md'
index = root / 'manifiestos/README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
issue72 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/72'

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
> **LIV · Riqueza y Chatarra™ · El Chatarrero™ como arquetipo de restauración civilizatoria**  
> **LIV · Wealth and Scrap™ · The Scrapworker™ as an archetype of civilisational restoration**
>
> La propuesta eleva reparación, restauración, reutilización, remanufactura y transformación del residuo a infraestructura civilizatoria, sin romantizar precariedad ni sustituir evidencia ambiental por metáfora. / The proposal elevates repair, restoration, reuse, remanufacturing and transformation of residue into civilisational infrastructure without romanticising precarity or replacing environmental evidence with metaphor.
>
> **[Leer manifiesto LIV / Read manifesto LIV]({rel(f, latest)}) · [Síntesis Abierta LIV · Issue #72 / Open Synthesis LIV · Issue #72]({issue72})**  
> [Cómo aportar / How to contribute]({rel(f, protocol)}) · [Índice de Síntesis Abierta / Open Synthesis index]({rel(f, synth_index)}) · [Auditorías públicas / Public audits]({rel(f, audits)}) · [54 manifiestos I–LIV / 54 manifestos I–LIV]({rel(f, index)})

{END}'''

readmes = sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme = root / 'LEEME.md'
if leeme.exists():
    readmes.append(leeme)
readmes = sorted(set(readmes))
changed = []
for f in readmes:
    text = f.read_text(encoding='utf-8')
    old = text
    b = block(f)
    if START in text and END in text:
        text = re.sub(re.escape(START) + r'.*?' + re.escape(END), b, text, count=1, flags=re.S)
    if text != old:
        f.write_text(text, encoding='utf-8')
        changed.append(f)

fail = []
for f in readmes:
    text = f.read_text(encoding='utf-8')
    if START in text:
        m = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, re.S)
        if not m or 'Issue #72' not in m.group(1) or latest.name not in m.group(1):
            fail.append(f'{f.relative_to(root)}: LIV/Issue #72 feature incomplete')

idx = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
if not net:
    fail.append('manifiestos/README.md: canonical network block missing')
else:
    items = re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', net.group(1))
    unique=[]; seen=set()
    for roman,href in items:
        p=(index.parent/href).resolve()
        if p not in seen:
            seen.add(p); unique.append((roman,p))
    if len(unique)!=54 or unique[0][0]!='I' or unique[-1][0]!='LIV':
        fail.append(f'manifiestos/README.md: canonical sequence invalid ({len(unique)} items)')

print(f'README_LEEME_TARGETS={len(readmes)}')
print(f'FILES_CHANGED={len(changed)}')
for p in changed: print('CHANGED', p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    print('\n'.join(fail))
    sys.exit(1)
print('POSTCHECK OK: latest LIV + Open Synthesis #72 featured; canonical I-LIV network intact')
