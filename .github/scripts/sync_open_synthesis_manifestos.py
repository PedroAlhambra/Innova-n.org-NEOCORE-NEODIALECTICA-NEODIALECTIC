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

for p in (index, protocol, synth_index, audits, leonidas):
    if not p.exists():
        raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

# Canonical order is the explicit order in manifiestos/README.md.
idx = index.read_text(encoding='utf-8')
links=[]
seen=set()
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(mdir/href).resolve()
    if p in seen or not p.exists():
        continue
    seen.add(p)
    links.append((roman,title.strip(),p))
if not links:
    raise SystemExit('No canonical manifestos found')

count=len(links)
roman,title,LATEST=links[-1]
# Waves are documentary groupings, not the source of manifesto count.
# Current public grouping: LVII-LIX forms wave 24.
waves=24 if count >= 59 else 23 if count >= 56 else max(1,count)

latest_text=LATEST.read_text(encoding='utf-8')
im=re.search(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',latest_text)
issue_num=im.group(1) if im else {'LVII':'77','LVIII':'78','LIX':'79'}.get(roman)
if not issue_num:
    raise SystemExit(f'Cannot resolve Open Synthesis issue for {roman}')
issue_url=f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue_num}'

LATEST_START='<!-- NEO_LATEST_MANIFESTO_START -->'; LATEST_END='<!-- NEO_LATEST_MANIFESTO_END -->'
CURRENT_START='<!-- MANIFESTOS_CURRENT_START -->'; CURRENT_END='<!-- MANIFESTOS_CURRENT_END -->'
NETWORK_START='<!-- NEO_ALL_MANIFESTOS_START -->'; NETWORK_END='<!-- NEO_ALL_MANIFESTOS_END -->'
INVITE_START='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'; INVITE_END='<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'
NAV_START='<!-- NEO_MANIFESTO_NAV_START -->'; NAV_END='<!-- NEO_MANIFESTO_NAV_END -->'

def rel(frm,target):
    return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')

def replace_block(text,start,end,block):
    if start in text and end in text:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end),block,text,count=1,flags=re.S)
    return text

def latest_block(f):
    return f'''{LATEST_START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(f,LATEST)}) · [Síntesis Abierta {roman} · #{issue_num} / Open Synthesis {roman} · #{issue_num}]({issue_url})**  
> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Leónidas™]({rel(f,leonidas)}) · [Auditorías públicas / Public audits]({rel(f,audits)}) · [{count} manifiestos / manifestos · I–{roman}]({rel(f,index)})

{LATEST_END}'''

def current_block(f):
    return f'''{CURRENT_START}

**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:** **I–{roman} · {count} manifiestos bilingües / {count} bilingual manifestos** · [índice canónico / canonical index]({rel(f,index)})

{CURRENT_END}'''

def compact_network_block(f):
    return f'''{NETWORK_START}

## Manifiestos / Manifestos

**I–{roman} · {count} manifiestos bilingües · {waves} oleadas / {count} bilingual manifestos · {waves} waves.**  
Los manifiestos son pilares públicos del marco, no equivalentes al marco completo. / The manifestos are public pillars of the framework, not equivalents of the complete framework.

**[Abrir índice canónico y navegable / Open canonical navigable index →]({rel(f,index)})**

{NETWORK_END}'''

def invite_block(f):
    return f'''{INVITE_START}

## Participa en la Síntesis Abierta / Join the Open Synthesis

Puedes aportar crítica, objeciones, contraejemplos, fuentes, experiencia, verificación, implementación o delta. / You may contribute criticism, objections, counterexamples, sources, experience, verification, implementation or a delta.

**Última síntesis / Latest synthesis:** [{roman} · {title}]({rel(f,LATEST)}) · [Issue #{issue_num}]({issue_url})  
**Auditorías / Audits:** [LIII · Leónidas™]({rel(f,links[52][2]) if len(links)>52 else rel(f,leonidas)}) · [protocolo / protocol]({rel(f,leonidas)})  
**Cómo aportar / How to contribute:** [protocolo general / general protocol]({rel(f,protocol)}) · [portal de auditorías / audit portal]({rel(f,audits)}) · [índice / index]({rel(f,synth_index)})

{INVITE_END}'''

def nav_block(i,f):
    prev=links[i-1] if i else None
    nxt=links[i+1] if i+1<len(links) else None
    a=f'← **{prev[0]}** · [{prev[1]}]({rel(f,prev[2])})' if prev else '← **Inicio de la colección / Start of collection**'
    b=f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin provisional de la colección / Provisional end of collection** →'
    return f'''{NAV_START}

## Navegación canónica / Canonical navigation

{a}  
· [Índice I–{roman} / I–{roman} index]({rel(f,index)}) ·  
{b}

{NAV_END}'''

readmes=sorted(set(root.rglob('README.md'))|set(root.rglob('README_*.md'))|{root/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]
changed=[]
for f in readmes:
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_block(s,LATEST_START,LATEST_END,latest_block(f))
    s=replace_block(s,CURRENT_START,CURRENT_END,current_block(f))
    if NETWORK_START in s and NETWORK_END in s and f.resolve()!=index.resolve():
        s=replace_block(s,NETWORK_START,NETWORK_END,compact_network_block(f))
    if INVITE_START in s and INVITE_END in s:
        s=replace_block(s,INVITE_START,INVITE_END,invite_block(f))

    # Remove stale hard-coded corpus references left outside managed blocks.
    s=re.sub(r'Índice navegable de manifiestos I–[IVXLCDM]+',f'Índice navegable de manifiestos I–{roman}',s)
    s=re.sub(r'Navigable manifesto index I–[IVXLCDM]+',f'Navigable manifesto index I–{roman}',s)
    s=re.sub(r'I–[IVXLCDM]+ · \d+ manifiestos bilingües · \d+ oleadas',f'I–{roman} · {count} manifiestos bilingües · {waves} oleadas',s)
    s=re.sub(r'\d+ bilingual manifestos · I–[IVXLCDM]+ · \d+ waves',f'{count} bilingual manifestos · I–{roman} · {waves} waves',s)
    s=re.sub(r'I–[IVXLCDM]+ · \d+ manifiestos bilingües',f'I–{roman} · {count} manifiestos bilingües',s)
    s=re.sub(r'I–[IVXLCDM]+ · \d+ bilingual manifestos',f'I–{roman} · {count} bilingual manifestos',s)
    s=re.sub(r'\d+ manifiestos I–[IVXLCDM]+',f'{count} manifiestos I–{roman}',s)
    s=re.sub(r'\d+ manifestos I–[IVXLCDM]+',f'{count} manifestos I–{roman}',s)

    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

# Keep manifesto navigation dynamic when managed navigation markers exist.
for i,(_,_,f) in enumerate(links):
    s=f.read_text(encoding='utf-8'); old=s
    if NAV_START in s and NAV_END in s:
        s=replace_block(s,NAV_START,NAV_END,nav_block(i,f))
    if INVITE_START in s and INVITE_END in s:
        s=replace_block(s,INVITE_START,INVITE_END,invite_block(f))
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

# Validate the three canonical entry points without assuming the corpus is final.
fail=[]
for p in (root/'README.md', index, synth_index):
    s=p.read_text(encoding='utf-8')
    if f'I–{roman}' not in s or str(count) not in s:
        fail.append(f'{p.relative_to(root)} stale count')
if LATEST.name not in (root/'README.md').read_text(encoding='utf-8'):
    fail.append('README.md stale latest manifesto')

print(f'CANONICAL_MANIFESTOS={count}')
print(f'LATEST={roman} ISSUE=#{issue_num}')
print(f'WAVES={waves}')
print('FILES_CHANGED=',len(set(changed)))
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print('POSTCHECK OK: dynamic Open Synthesis network retained')
