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

idx_text = index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx_text, re.S)
if not net:
    raise SystemExit('Canonical manifesto network block missing')

links=[]
seen=set()
for roman,title,href in re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', net.group(1)):
    p=(mdir/href).resolve()
    if p in seen:
        continue
    if not p.exists():
        raise SystemExit(f'Missing canonical manifesto: {href}')
    seen.add(p)
    links.append((roman,title.strip(),p))
if len(links)!=53 or links[0][0]!='I' or links[-1][0]!='LIII':
    raise SystemExit(f'Canonical manifesto set invalid: {len(links)} {links[0][0] if links else None}..{links[-1][0] if links else None}')

def rel(frm,target):
    return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')

invite_start='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'
invite_end='<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'
nav_start='<!-- NEO_MANIFESTO_NAV_START -->'
nav_end='<!-- NEO_MANIFESTO_NAV_END -->'

def invite(f):
    return f'''{invite_start}

## Participa en la Síntesis Abierta / Join the Open Synthesis

**Este marco no pide adhesión ciega.** Puedes aportar una crítica, objeción, contraejemplo, fuente, experiencia, verificación, implementación o propuesta de delta. Con **Leónidas™** también puedes aportar pruebas a una Auditoría Pública existente o proponer un problema externo para nueva auditoría trazable.

**Puerta actual:** [LIII · Leónidas™]({rel(f,links[52][2])}) · [Síntesis Abierta LIII · Issue #69]({issue69})  
**Cómo aportar:** [Protocolo general]({rel(f,protocol)}) · [Protocolo Leónidas™]({rel(f,leonidas)})  
**Auditorías Públicas:** [portal y pruebas]({rel(f,audits)}) · [Índice de Síntesis Abierta]({rel(f,synth_index)})

**This framework does not ask for blind endorsement.** You may contribute criticism, objections, counterexamples, sources, experience, verification, implementation or a proposed delta. With **Leónidas™**, you may also contribute evidence to an existing Public Audit or bring an external problem for a new traceable audit.

**Current gate:** [LIII · Leónidas™]({rel(f,links[52][2])}) · [Open Synthesis LIII · Issue #69]({issue69})  
**How to contribute:** [general protocol]({rel(f,protocol)}) · [Leónidas™ protocol]({rel(f,leonidas)})  
**Public Audits:** [portal and evidence]({rel(f,audits)}) · [Open Synthesis index]({rel(f,synth_index)})

{invite_end}'''

def replace_or_append(text,start,end,block,anchor=None):
    if start in text and end in text:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end),block,text,count=1,flags=re.S)
    if anchor and anchor in text:
        return text.replace(anchor,anchor+'\n\n'+block,1)
    return text.rstrip()+'\n\n'+block+'\n'

readmes=sorted(set(root.rglob('README.md'))|set(root.rglob('README_*.md'))|{root/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]
changed=[]

for f in readmes:
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_or_append(s,invite_start,invite_end,invite(f),'<!-- NEO_ALL_MANIFESTOS_END -->')
    replacements=[
        ('Índice navegable de manifiestos I–LII','Índice navegable de manifiestos I–LIII'),
        ('Navigable manifesto index I–LII','Navigable manifesto index I–LIII'),
        ('I–LII · 52 manifiestos bilingües','I–LIII · 53 manifiestos bilingües'),
        ('I–LII · 52 bilingual manifestos','I–LIII · 53 bilingual manifestos'),
        ('52 manifiestos bilingües · I–LII · 19 oleadas','53 manifiestos bilingües · I–LIII · 20 oleadas'),
        ('52 bilingual manifestos · I–LII · 19 waves','53 bilingual manifestos · I–LIII · 20 waves'),
        ('52 manifiestos · I–LII','53 manifiestos · I–LIII'),
        ('52 manifestos · I–LII','53 manifestos · I–LIII')]
    for a,b in replacements:
        s=s.replace(a,b)
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8'); old=s
    s=replace_or_append(s,invite_start,invite_end,invite(f))
    prev=links[i-1] if i else None
    nxt=links[i+1] if i+1<len(links) else None
    nav=[nav_start,'','## Navegación canónica / Canonical navigation','']
    nav.append(f'← **{prev[0]}** · [{prev[1]}]({rel(f,prev[2])})' if prev else '← **Inicio de la colección / Start of collection**')
    nav.append(f'· [Índice I–LIII / I–LIII index]({rel(f,index)}) ·')
    nav.append(f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin de la colección / End of collection** →')
    nav += ['','> La navegación canónica mantiene la colección conectada sin convertir ningún manifiesto aislado en equivalente del marco completo. / Canonical navigation keeps the collection connected without treating any single manifesto as equivalent to the complete framework.','',nav_end]
    s=replace_or_append(s,nav_start,nav_end,'\n'.join(nav))
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

fail=[]
for f in readmes:
    s=f.read_text(encoding='utf-8')
    if s.count(invite_start)!=1 or s.count(invite_end)!=1:
        fail.append(f'{f.relative_to(root)} invitation markers')
    if 'LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md' not in s or 'issues/69' not in s:
        fail.append(f'{f.relative_to(root)} Leónidas invitation links')

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8')
    if s.count(invite_start)!=1 or s.count(invite_end)!=1: fail.append(f'{f.relative_to(root)} invite')
    if s.count(nav_start)!=1 or s.count(nav_end)!=1: fail.append(f'{f.relative_to(root)} nav')
    n=re.search(re.escape(nav_start)+r'(.*?)'+re.escape(nav_end),s,re.S)
    if n:
        if 'I–LIII' not in n.group(1): fail.append(f'{f.relative_to(root)} index label')
        if i and rel(f,links[i-1][2]) not in n.group(1): fail.append(f'{f.relative_to(root)} prev')
        if i+1<len(links) and rel(f,links[i+1][2]) not in n.group(1): fail.append(f'{f.relative_to(root)} next')

print('CANONICAL_MANIFESTOS=',len(links))
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(set(changed)))
for p in sorted(set(changed)): print('CHANGED',p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    print('\n'.join(fail))
    sys.exit(1)
print('POSTCHECK OK: 53 manifestos I-LIII connected; README/LEEME targets expose Leónidas, Open Synthesis and Public Audits')
