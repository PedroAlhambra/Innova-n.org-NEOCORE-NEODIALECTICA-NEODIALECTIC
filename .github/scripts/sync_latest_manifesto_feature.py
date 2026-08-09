from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
latest = root / 'manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md'
index = root / 'manifiestos/README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
leonidas = root / 'propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md'
issue76 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/76'

for p in (latest, index, protocol, synth_index, audits, leonidas):
    if not p.exists():
        raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

START='<!-- NEO_LATEST_MANIFESTO_START -->'
END='<!-- NEO_LATEST_MANIFESTO_END -->'

def rel(f,target):
    return os.path.relpath(target,start=f.parent).replace(os.sep,'/')

def block(f):
    return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LVI · NO-CONTROL™ · Síntesis Previa a la Potencia**  
> **LVI · NO-CONTROL™ · Synthesis Before Power**
>
> Distingue perturbación funcional de ataque intencional y riesgo de doble uso de acusación. La potencia tecnológica no debe crecer por delante de la capacidad colectiva de comprenderla, limitarla, auditarla y detenerla. / It separates functional disruption from intentional attack and dual-use risk from accusation. Technological power should not outrun the collective capacity to understand, limit, audit and stop it.
>
> **[Leer LVI / Read LVI]({rel(f,latest)}) · [Síntesis Abierta LVI · #76 / Open Synthesis LVI · #76]({issue76})**  
> [Cómo aportar]({rel(f,protocol)}) · [Leónidas™ · auditorías externas]({rel(f,leonidas)}) · [Auditorías públicas]({rel(f,audits)}) · [56 manifiestos I–LVI]({rel(f,index)})

{END}'''

readmes=sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme=root/'LEEME.md'
if leeme.exists():
    readmes.append(leeme)
readmes=sorted(set(readmes))
changed=[]
for f in readmes:
    text=f.read_text(encoding='utf-8'); old=text
    if START in text and END in text:
        text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block(f),text,count=1,flags=re.S)
    if text!=old:
        f.write_text(text,encoding='utf-8'); changed.append(f)

fail=[]
for f in readmes:
    text=f.read_text(encoding='utf-8')
    if START in text:
        m=re.search(re.escape(START)+r'(.*?)'+re.escape(END),text,re.S)
        if not m or 'Issue #76' not in m.group(1) and '#76' not in m.group(1):
            fail.append(f'{f.relative_to(root)} latest issue')
        if not m or latest.name not in m.group(1):
            fail.append(f'{f.relative_to(root)} latest path')
idx=index.read_text(encoding='utf-8')
net=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',idx,re.S)
if not net:
    fail.append('canonical block missing')
else:
    items=re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)',net.group(1)); unique=[]; seen=set()
    for roman,href in items:
        p=(index.parent/href).resolve()
        if p not in seen:
            seen.add(p); unique.append((roman,p))
    if len(unique)!=56 or unique[-1][0]!='LVI':
        fail.append(f'canonical sequence invalid {len(unique)}')
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(changed))
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print('POSTCHECK OK: latest LVI + Open Synthesis #76 featured; canonical I-LVI network intact')
