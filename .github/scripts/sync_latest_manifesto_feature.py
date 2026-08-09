from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
latest = root / 'manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md'
index = root / 'manifiestos/README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
issue74 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/74'

for p in (latest, index, protocol, synth_index, audits):
    if not p.exists(): raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

START='<!-- NEO_LATEST_MANIFESTO_START -->'; END='<!-- NEO_LATEST_MANIFESTO_END -->'
def rel(f,target): return os.path.relpath(target,start=f.parent).replace(os.sep,'/')
def block(f):
    return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LV · Ataque de las Micromáquinas™ · Las Plagas de la Escala Invisible**  
> **LV · Attack of the Micromachines™ · The Plagues of the Invisible Scale**
>
> Se separan microagentes reales, micro/nanorrobótica experimental y la hipótesis mucho más fuerte de un ataque intencional. / Real micro-agents, experimental micro/nanorobotics and the much stronger hypothesis of intentional attack remain distinct.
>
> **[Leer LV / Read LV]({rel(f,latest)}) · [Síntesis Abierta LV · Issue #74 / Open Synthesis LV · Issue #74]({issue74})**  
> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Índice de Síntesis Abierta / Open Synthesis index]({rel(f,synth_index)}) · [Auditorías públicas / Public audits]({rel(f,audits)}) · [55 manifiestos I–LV / 55 manifestos I–LV]({rel(f,index)})

{END}'''

readmes=sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme=root/'LEEME.md'
if leeme.exists(): readmes.append(leeme)
readmes=sorted(set(readmes)); changed=[]
for f in readmes:
    text=f.read_text(encoding='utf-8'); old=text
    if START in text and END in text:
        text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block(f),text,count=1,flags=re.S)
    if text!=old: f.write_text(text,encoding='utf-8'); changed.append(f)

fail=[]
for f in readmes:
    text=f.read_text(encoding='utf-8')
    if START in text:
        m=re.search(re.escape(START)+r'(.*?)'+re.escape(END),text,re.S)
        if not m or 'Issue #74' not in m.group(1) or latest.name not in m.group(1): fail.append(f'{f.relative_to(root)} latest')
idx=index.read_text(encoding='utf-8')
net=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',idx,re.S)
if not net: fail.append('canonical block missing')
else:
    items=re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)',net.group(1)); unique=[]; seen=set()
    for roman,href in items:
        p=(index.parent/href).resolve()
        if p not in seen: seen.add(p); unique.append((roman,p))
    if len(unique)!=55 or unique[-1][0]!='LV': fail.append(f'canonical sequence invalid {len(unique)}')
print('README_LEEME_TARGETS=',len(readmes)); print('FILES_CHANGED=',len(changed))
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print('POSTCHECK OK: latest LV + Open Synthesis #74 featured; canonical I-LV network intact')
