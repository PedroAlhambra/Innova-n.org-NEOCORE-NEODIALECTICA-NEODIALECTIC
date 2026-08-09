from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
mdir = root / 'manifiestos'
index = mdir / 'README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
leonidas = root / 'propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md'
issue69 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/69'

IDX = index.read_text(encoding='utf-8')
net_match = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', IDX, re.S)
if not net_match:
    raise SystemExit('Canonical manifesto network block missing')

links=[]
seen=set()
for roman,title,href in re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', net_match.group(1)):
    p=(mdir/href).resolve()
    if p in seen:
        continue
    if not p.exists():
        raise SystemExit(f'Missing canonical manifesto: {href}')
    seen.add(p)
    links.append((roman,title.strip(),p))
if len(links)!=53 or links[0][0]!='I' or links[-1][0]!='LIII':
    raise SystemExit(f'Canonical manifesto set invalid: {len(links)}')

LATEST = links[-1][2]

LATEST_START='<!-- NEO_LATEST_MANIFESTO_START -->'
LATEST_END='<!-- NEO_LATEST_MANIFESTO_END -->'
CURRENT_START='<!-- MANIFESTOS_CURRENT_START -->'
CURRENT_END='<!-- MANIFESTOS_CURRENT_END -->'
NETWORK_START='<!-- NEO_ALL_MANIFESTOS_START -->'
NETWORK_END='<!-- NEO_ALL_MANIFESTOS_END -->'
INVITE_START='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'
INVITE_END='<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'
NAV_START='<!-- NEO_MANIFESTO_NAV_START -->'
NAV_END='<!-- NEO_MANIFESTO_NAV_END -->'

def rel(frm,target):
    return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')

def replace_block(text,start,end,block,append=False):
    if start in text and end in text:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end),block,text,count=1,flags=re.S)
    if append:
        return text.rstrip()+'\n\n'+block+'\n'
    return text

def latest_block(f):
    return f'''{LATEST_START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LIII · Leónidas™ · Defensor de la Síntesis, la Auditoría Abierta y el Derecho a Traer Problemas**  
> **LIII · Leónidas™ · Defender of Synthesis, Open Audit and the Right to Bring Problems**
>
> Leónidas™ abre la puerta para aportar pruebas a auditorías existentes o proponer problemas y auditorías externas bajo trazabilidad, contradicción, privacidad y separación entre hechos e hipótesis. / Leónidas™ opens the gate for evidence contributions to existing audits or new external problems and audits under traceability, contradiction, privacy and separation between facts and hypotheses.
>
> **[Leer manifiesto LIII / Read manifesto LIII]({rel(f,LATEST)}) · [Síntesis Abierta LIII · Issue #69 / Open Synthesis LIII · Issue #69]({issue69})**  
> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Protocolo Leónidas™]({rel(f,leonidas)}) · [Auditorías públicas / Public audits]({rel(f,audits)}) · [53 manifiestos I–LIII / 53 manifestos I–LIII]({rel(f,index)})

{LATEST_END}'''

def current_block(f):
    return f'''{CURRENT_START}

**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:** **I–LIII · 53 manifiestos bilingües / 53 bilingual manifestos** · [índice canónico / canonical index]({rel(f,index)})

{CURRENT_END}'''

def network_block(f):
    rows=[]
    for roman,title,p in links:
        rows.append(f'- **{roman}** · [{title}]({rel(f,p)})')
    body='\n'.join(rows)
    return f'''{NETWORK_START}

## Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™

**Estado canónico / Canonical state:** **53 manifiestos bilingües · I–LIII · 20 oleadas / 53 bilingual manifestos · I–LIII · 20 waves**  
**Índice canónico / Canonical index:** [{rel(f,index)}]({rel(f,index)})

<details>
<summary><strong>I–LIII · 53 manifiestos / 53 manifestos</strong></summary>

{body}

</details>

> **Regla de lectura / Reading rule:** ningún manifiesto equivale por sí solo al marco completo. Esta navegación mantiene los 53 manifiestos accesibles sin sustituir el contexto propio de cada nodo. / No single manifesto equals the complete framework. This navigation keeps all 53 manifestos accessible without replacing each node's own context.

{NETWORK_END}'''

def invite_block(f):
    return f'''{INVITE_START}

## Participa en la Síntesis Abierta / Join the Open Synthesis

**Este marco no pide adhesión ciega.** Puedes aportar crítica, objeciones, contraejemplos, fuentes, experiencia, verificación, implementación o un delta. Con **Leónidas™** también puedes aportar pruebas a una Auditoría Pública existente o proponer una nueva auditoría trazable.

**Puerta actual:** [LIII · Leónidas™]({rel(f,LATEST)}) · [Síntesis Abierta LIII · #69]({issue69})  
**Cómo aportar:** [protocolo general]({rel(f,protocol)}) · [protocolo Leónidas™]({rel(f,leonidas)})  
**Auditorías:** [portal público]({rel(f,audits)}) · [Índice de Síntesis Abierta]({rel(f,synth_index)})

**This framework does not ask for blind endorsement.** You may contribute criticism, objections, counterexamples, sources, experience, verification, implementation or a delta. With **Leónidas™**, you may also contribute evidence to an existing Public Audit or propose a new traceable audit.

{INVITE_END}'''

def nav_block(i,f):
    prev=links[i-1] if i else None
    nxt=links[i+1] if i+1<len(links) else None
    a=f'← **{prev[0]}** · [{prev[1]}]({rel(f,prev[2])})' if prev else '← **Inicio de la colección / Start of collection**'
    b=f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin de la colección / End of collection** →'
    return f'''{NAV_START}

## Navegación canónica / Canonical navigation

{a}  
· [Índice I–LIII / I–LIII index]({rel(f,index)}) ·  
{b}

> La navegación canónica mantiene la colección conectada sin convertir ningún manifiesto aislado en equivalente del marco completo. / Canonical navigation keeps the collection connected without treating any single manifesto as equivalent to the complete framework.

{NAV_END}'''

readmes=sorted(set(root.rglob('README.md'))|set(root.rglob('README_*.md'))|{root/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]
changed=[]

for f in readmes:
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_block(s,LATEST_START,LATEST_END,latest_block(f))
    s=replace_block(s,CURRENT_START,CURRENT_END,current_block(f))
    if NETWORK_START in s and NETWORK_END in s and f.resolve()!=index.resolve():
        s=replace_block(s,NETWORK_START,NETWORK_END,network_block(f))
    if INVITE_START in s and INVITE_END in s:
        s=replace_block(s,INVITE_START,INVITE_END,invite_block(f))
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_block(s,INVITE_START,INVITE_END,invite_block(f),append=True)
    s=replace_block(s,NAV_START,NAV_END,nav_block(i,f),append=True)
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

fail=[]
idx_now=index.read_text(encoding='utf-8')
canon=re.search(re.escape(NETWORK_START)+r'(.*?)'+re.escape(NETWORK_END),idx_now,re.S)
if not canon or canon.group(1).count('\n- **')<53 or '**LIII**' not in canon.group(1):
    fail.append('manifiestos/README.md canonical network')

for f in readmes:
    s=f.read_text(encoding='utf-8')
    if LATEST_START in s and ('LIII' not in re.search(re.escape(LATEST_START)+r'(.*?)'+re.escape(LATEST_END),s,re.S).group(1) or 'issues/69' not in s):
        fail.append(f'{f.relative_to(root)} latest')
    if CURRENT_START in s:
        blk=re.search(re.escape(CURRENT_START)+r'(.*?)'+re.escape(CURRENT_END),s,re.S).group(1)
        if '53 manifiestos bilingües / 53 bilingual manifestos' not in blk:
            fail.append(f'{f.relative_to(root)} current count')
    if NETWORK_START in s:
        blk=re.search(re.escape(NETWORK_START)+r'(.*?)'+re.escape(NETWORK_END),s,re.S).group(1)
        if 'I–LIII · 53 manifiestos / 53 manifestos' not in blk or '53 bilingual manifestos' not in blk:
            fail.append(f'{f.relative_to(root)} network count')

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8')
    nav=re.search(re.escape(NAV_START)+r'(.*?)'+re.escape(NAV_END),s,re.S)
    if not nav or 'I–LIII' not in nav.group(1):
        fail.append(f'{f.relative_to(root)} nav')
    elif i+1<len(links) and rel(f,links[i+1][2]) not in nav.group(1):
        fail.append(f'{f.relative_to(root)} next')

print('CANONICAL_MANIFESTOS=53')
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(set(changed)))
for p in sorted(set(changed)): print('CHANGED',p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    print('\n'.join(fail))
    sys.exit(1)
print('POSTCHECK OK: I-LIII/53/20 waves synchronized; Leónidas and Public Audits exposed; manifesto navigation complete')
