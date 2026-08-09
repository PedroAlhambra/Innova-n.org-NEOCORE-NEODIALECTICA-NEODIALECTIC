from pathlib import Path
import os,re,sys

ROOT=Path('.').resolve()
IDX=ROOT/'manifiestos/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
PROTO=ROOT/'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
AUD=ROOT/'auditorias/publicas/README.md'
LEON=ROOT/'propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md'
ENTRY=ROOT/'propuestas/sintesis-abierta/REGISTRO_ENTRADA_TRAZABLE_DERIVACION_ES_EN.md'
FOLLOW=ROOT/'proyeccion/SEGUIR_MARCO_SINTESIS_ES_EN.md'

idx=IDX.read_text(encoding='utf-8')
items=[]; seen=set()
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(IDX.parent/href).resolve()
    if p.exists() and p not in seen:
        seen.add(p);items.append((roman,title.strip(),p))
if not items: raise SystemExit('no canonical manifestos')
roman,title,latest=items[-1]; count=len(items)
lt=latest.read_text(encoding='utf-8',errors='replace')
# Prefer the manifesto's explicitly labelled dedicated synthesis; fall back to first issue URL.
m=re.search(r'(?:Síntesis Abierta|Open Synthesis)[^\n]{0,80}#(\d+)',lt,re.I)
if not m: m=re.search(r'/issues/(\d+)',lt)
if not m: raise SystemExit('cannot resolve latest synthesis issue')
issue=m.group(1)
if roman!='LX' or count!=60 or issue!='99':
    raise SystemExit(f'unexpected canonical state: {count} I-{roman} issue={issue}')

def rel(frm,target): return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')
def block(f):
    return f'''<!-- NEO_LATEST_MANIFESTO_START -->

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(f,latest)}) · [Síntesis Abierta {roman} · #{issue} / Open Synthesis {roman} · #{issue}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue})**  
> [Seguir marco / Follow framework]({rel(f,FOLLOW)}) · [Registrar entrada / Register entry]({rel(f,ENTRY)}) · [Cómo aportar / How to contribute]({rel(f,PROTO)}) · [Leónidas™]({rel(f,LEON)}) · [Auditorías públicas / Public audits]({rel(f,AUD)}) · [{count} manifiestos / manifestos · I–{roman}]({rel(f,IDX)})

<!-- NEO_LATEST_MANIFESTO_END -->'''

changed=[]
targets=sorted({p for p in ROOT.rglob('README*.md') if '.git' not in p.parts}|({ROOT/'LEEME.md'} if (ROOT/'LEEME.md').exists() else set()))
for f in targets:
    s=f.read_text(encoding='utf-8',errors='replace'); old=s
    if '<!-- NEO_LATEST_MANIFESTO_START -->' in s and '<!-- NEO_LATEST_MANIFESTO_END -->' in s:
        s=re.sub(r'<!-- NEO_LATEST_MANIFESTO_START -->.*?<!-- NEO_LATEST_MANIFESTO_END -->',block(f),s,count=1,flags=re.S)
    if s!=old:
        f.write_text(s,encoding='utf-8');changed.append(f.relative_to(ROOT).as_posix())

# Open Synthesis landing page has a historical unmarked latest-card plus current coverage.
s=SYN.read_text(encoding='utf-8'); old=s
s=re.sub(r'\*\*Cobertura en este commit / Coverage at this commit:\*\* \*\*\d+ manifiestos · I–[IVXLCDM]+ / \d+ manifestos · I–[IVXLCDM]+\*\*',
         f'**Cobertura en este commit / Coverage at this commit:** **{count} manifiestos · I–{roman} / {count} manifestos · I–{roman}**',s,count=1)
card=f'''> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(SYN,latest)}) · [Síntesis Abierta {roman} · #{issue} / Open Synthesis {roman} · #{issue}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue})**  
> [Cómo aportar / How to contribute]({rel(SYN,PROTO)}) · [Leónidas™]({rel(SYN,LEON)}) · [Auditorías públicas / Public audits]({rel(SYN,AUD)}) · [Índice de manifiestos / Manifesto index]({rel(SYN,IDX)})'''
s=re.sub(r'> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS.*?(?=\n> El número de manifiestos)',card+'\n',s,count=1,flags=re.S)
s=re.sub(r'## Índice canónico · I–[IVXLCDM]+',f'## Índice canónico · I–{roman}',s)
s=re.sub(r'## Canonical index · I–[IVXLCDM]+',f'## Canonical index · I–{roman}',s)
if s!=old:
    SYN.write_text(s,encoding='utf-8');changed.append(SYN.relative_to(ROOT).as_posix())

# Verify all managed latest blocks are synchronized.
bad=[]
for f in targets:
    s=f.read_text(encoding='utf-8',errors='replace')
    if '<!-- NEO_LATEST_MANIFESTO_START -->' in s:
        m=re.search(r'<!-- NEO_LATEST_MANIFESTO_START -->(.*?)<!-- NEO_LATEST_MANIFESTO_END -->',s,re.S)
        body=m.group(1) if m else ''
        if 'LX' not in body or 'issues/99' not in body: bad.append(f.relative_to(ROOT).as_posix())
ss=SYN.read_text(encoding='utf-8')
if '60 manifiestos · I–LX / 60 manifestos · I–LX' not in ss or latest.name not in ss or 'issues/99' not in ss:
    bad.append('propuestas/sintesis-abierta/README.md')
if bad:
    raise SystemExit('unsynchronized: '+', '.join(bad))
print('SYNC OK',len(changed),'files; latest LX #99; corpus 60 I-LX')
