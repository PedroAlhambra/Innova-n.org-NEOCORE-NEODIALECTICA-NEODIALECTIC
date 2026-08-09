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
latest_path = mdir / '55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md'
issue74 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/74'

# Bootstrap LV into the canonical index if this is the first LV run.
idx = index.read_text(encoding='utf-8')
if latest_path.name not in idx:
    marker = '\n</details>\n'
    row = f'\n- **LV** · [Ataque de las Micromáquinas™ · Las Plagas de la Escala Invisible / Attack of the Micromachines™ · The Plagues of the Invisible Scale]({latest_path.name}) · [Síntesis #74]({issue74})\n'
    start = idx.find('<!-- NEO_ALL_MANIFESTOS_START -->')
    end = idx.find('<!-- NEO_ALL_MANIFESTOS_END -->')
    if start < 0 or end < 0:
        raise SystemExit('Canonical manifesto network block missing')
    pos = idx.rfind(marker, start, end)
    if pos < 0:
        raise SystemExit('Cannot locate canonical manifesto details end')
    idx = idx[:pos] + row + idx[pos:]

for a,b in [
    ('54 manifiestos bilingües · I–LIV · 21 oleadas','55 manifiestos bilingües · I–LV · 22 oleadas'),
    ('54 bilingual manifestos · I–LIV · 21 waves','55 bilingual manifestos · I–LV · 22 waves'),
    ('I–LIV · 54 manifiestos bilingües / 54 bilingual manifestos','I–LV · 55 manifiestos bilingües / 55 bilingual manifestos'),
    ('I–LIV · 54 manifiestos / 54 manifestos','I–LV · 55 manifiestos / 55 manifestos'),
    ('54 manifiestos I–LIV','55 manifiestos I–LV'),
    ('54 manifestos I–LIV','55 manifestos I–LV')]:
    idx = idx.replace(a,b)
index.write_text(idx,encoding='utf-8')

# Bootstrap LV into Open Synthesis index/table if absent.
ss = synth_index.read_text(encoding='utf-8')
ss = ss.replace('54 manifiestos · I–LIV / 54 manifestos · I–LIV','55 manifiestos · I–LV / 55 manifestos · I–LV')
ss = ss.replace('Índice canónico de Síntesis Abierta · I–LIV','Índice canónico de Síntesis Abierta · I–LV')
if latest_path.name not in ss:
    liv_line = None
    lines = ss.splitlines()
    for i,line in enumerate(lines):
        if '| **LIV**' in line or ('54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md' in line and line.lstrip().startswith('|')):
            liv_line = i
    lv_row = f'| **LV** | **[Ataque de las Micromáquinas™ · Plagas de la Escala Invisible](../../manifiestos/{latest_path.name})** | **[#74]({issue74})** |'
    if liv_line is not None:
        lines.insert(liv_line+1,lv_row)
        ss='\n'.join(lines)+'\n'
synth_index.write_text(ss,encoding='utf-8')

IDX=index.read_text(encoding='utf-8')
net_match=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',IDX,re.S)
if not net_match: raise SystemExit('Canonical manifesto network block missing')
links=[]; seen=set()
for roman,title,href in re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',net_match.group(1)):
    p=(mdir/href).resolve()
    if p in seen: continue
    if not p.exists(): raise SystemExit(f'Missing canonical manifesto: {href}')
    seen.add(p); links.append((roman,title.strip(),p))
if len(links)!=55 or links[0][0]!='I' or links[-1][0]!='LV':
    raise SystemExit(f'Canonical manifesto set invalid: {len(links)} {links[-1][0] if links else None}')

LATEST=links[-1][2]
LATEST_START='<!-- NEO_LATEST_MANIFESTO_START -->'; LATEST_END='<!-- NEO_LATEST_MANIFESTO_END -->'
CURRENT_START='<!-- MANIFESTOS_CURRENT_START -->'; CURRENT_END='<!-- MANIFESTOS_CURRENT_END -->'
NETWORK_START='<!-- NEO_ALL_MANIFESTOS_START -->'; NETWORK_END='<!-- NEO_ALL_MANIFESTOS_END -->'
INVITE_START='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'; INVITE_END='<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'
NAV_START='<!-- NEO_MANIFESTO_NAV_START -->'; NAV_END='<!-- NEO_MANIFESTO_NAV_END -->'

def rel(frm,target): return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')
def replace_block(text,start,end,block,append=False):
    if start in text and end in text:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end),block,text,count=1,flags=re.S)
    if append: return text.rstrip()+'\n\n'+block+'\n'
    return text

def latest_block(f):
    return f'''{LATEST_START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LV · Ataque de las Micromáquinas™ · Las Plagas de la Escala Invisible**  
> **LV · Attack of the Micromachines™ · The Plagues of the Invisible Scale**
>
> El marco separa microagentes reales, micro/nanorrobótica experimental y la hipótesis mucho más fuerte de un ataque intencional. Propone defensa antes de escala: detección, apagado, degradación, retirada, trazabilidad y responsabilidad. / The framework separates real micro-agents, experimental micro/nanorobotics and the much stronger hypothesis of intentional attack. It proposes defence before scale: detection, shutdown, degradation, removal, traceability and accountability.
>
> **[Leer LV / Read LV]({rel(f,LATEST)}) · [Síntesis Abierta LV · #74 / Open Synthesis LV · #74]({issue74})**  
> [Cómo aportar]({rel(f,protocol)}) · [Leónidas™ · auditorías externas]({rel(f,leonidas)}) · [Auditorías públicas]({rel(f,audits)}) · [55 manifiestos I–LV]({rel(f,index)})

{LATEST_END}'''

def current_block(f):
    return f'''{CURRENT_START}

**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:** **I–LV · 55 manifiestos bilingües / 55 bilingual manifestos** · [índice canónico / canonical index]({rel(f,index)})

{CURRENT_END}'''

def network_block(f):
    body='\n'.join(f'- **{roman}** · [{title}]({rel(f,p)})' for roman,title,p in links)
    return f'''{NETWORK_START}

## Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™

**Estado canónico / Canonical state:** **55 manifiestos bilingües · I–LV · 22 oleadas / 55 bilingual manifestos · I–LV · 22 waves**  
**Índice canónico / Canonical index:** [{rel(f,index)}]({rel(f,index)})

<details>
<summary><strong>I–LV · 55 manifiestos / 55 manifestos</strong></summary>

{body}

</details>

> Ningún manifiesto equivale por sí solo al marco completo. / No single manifesto equals the complete framework.

{NETWORK_END}'''

def invite_block(f):
    return f'''{INVITE_START}

## Participa en la Síntesis Abierta / Join the Open Synthesis

Puedes aportar crítica, objeciones, contraejemplos, fuentes, experiencia, verificación, implementación o delta. Con **Leónidas™** también puedes aportar pruebas a una Auditoría Pública existente o proponer una nueva auditoría trazable.

**Última síntesis:** [LV · Micromáquinas™]({rel(f,LATEST)}) · [Issue #74]({issue74})  
**Auditorías y problemas externos:** [LIII · Leónidas™]({rel(f,links[52][2])}) · [protocolo Leónidas™]({rel(f,leonidas)})  
**Cómo aportar:** [protocolo general]({rel(f,protocol)}) · [portal de auditorías]({rel(f,audits)}) · [índice]({rel(f,synth_index)})

{INVITE_END}'''

def nav_block(i,f):
    prev=links[i-1] if i else None; nxt=links[i+1] if i+1<len(links) else None
    a=f'← **{prev[0]}** · [{prev[1]}]({rel(f,prev[2])})' if prev else '← **Inicio de la colección / Start of collection**'
    b=f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin de la colección / End of collection** →'
    return f'''{NAV_START}

## Navegación canónica / Canonical navigation

{a}  
· [Índice I–LV / I–LV index]({rel(f,index)}) ·  
{b}

{NAV_END}'''

readmes=sorted(set(root.rglob('README.md'))|set(root.rglob('README_*.md'))|{root/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]
changed=[]
for f in readmes:
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_block(s,LATEST_START,LATEST_END,latest_block(f))
    s=replace_block(s,CURRENT_START,CURRENT_END,current_block(f))
    if NETWORK_START in s and NETWORK_END in s and f.resolve()!=index.resolve(): s=replace_block(s,NETWORK_START,NETWORK_END,network_block(f))
    if INVITE_START in s and INVITE_END in s: s=replace_block(s,INVITE_START,INVITE_END,invite_block(f))
    for a,b in [('54 manifiestos bilingües · I–LIV · 21 oleadas','55 manifiestos bilingües · I–LV · 22 oleadas'),('54 bilingual manifestos · I–LIV · 21 waves','55 bilingual manifestos · I–LV · 22 waves'),('I–LIV · 54 manifiestos bilingües','I–LV · 55 manifiestos bilingües'),('I–LIV · 54 bilingual manifestos','I–LV · 55 bilingual manifestos')]: s=s.replace(a,b)
    if s!=old: f.write_text(s,encoding='utf-8'); changed.append(f)

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_block(s,INVITE_START,INVITE_END,invite_block(f),append=True)
    s=replace_block(s,NAV_START,NAV_END,nav_block(i,f),append=True)
    if s!=old: f.write_text(s,encoding='utf-8'); changed.append(f)

fail=[]
for f in readmes:
    s=f.read_text(encoding='utf-8')
    if CURRENT_START in s:
        blk=re.search(re.escape(CURRENT_START)+r'(.*?)'+re.escape(CURRENT_END),s,re.S).group(1)
        if '55 manifiestos bilingües / 55 bilingual manifestos' not in blk: fail.append(f'{f.relative_to(root)} current')
    if NETWORK_START in s:
        blk=re.search(re.escape(NETWORK_START)+r'(.*?)'+re.escape(NETWORK_END),s,re.S).group(1)
        if 'I–LV · 55 manifiestos / 55 manifestos' not in blk: fail.append(f'{f.relative_to(root)} network')
for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8')
    nav=re.search(re.escape(NAV_START)+r'(.*?)'+re.escape(NAV_END),s,re.S)
    if not nav or 'I–LV' not in nav.group(1): fail.append(f'{f.relative_to(root)} nav')
    elif i+1<len(links) and rel(f,links[i+1][2]) not in nav.group(1): fail.append(f'{f.relative_to(root)} next')

print('CANONICAL_MANIFESTOS=55')
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(set(changed)))
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print('POSTCHECK OK: I-LV/55/22 waves synchronized; LV #74 latest; Leónidas audit gateway preserved')
