from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
mdir = root / 'manifiestos'
index = mdir / 'README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
issue56 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/56'

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
if len(links)!=51 or links[0][0]!='I' or links[-1][0]!='LI':
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

**Este marco no pide adhesión ciega.** La Síntesis Abierta está abierta a cualquier persona que quiera aportar una **adhesión razonada o parcial, crítica, objeción, contraejemplo, fuente, experiencia, verificación, traducción, implementación o propuesta de delta**. Toda aportación debe poder discutirse, contrastarse y revisarse.

**Puerta de entrada recomendada:** [XLVIII · La Síntesis Todo lo Ve™]({rel(f,links[47][2])}) · [Síntesis Abierta XLVIII · Issue #56]({issue56})  
**Cómo aportar:** [Protocolo de aporte a la Síntesis Abierta]({rel(f,protocol)})  
**Todas las síntesis abiertas:** [Índice operativo de Síntesis Abierta]({rel(f,synth_index)})

**This framework does not ask for blind endorsement.** Open Synthesis is open to anyone willing to contribute a **reasoned or partial endorsement, criticism, objection, counterexample, source, experience, verification, translation, implementation or proposed delta**. Every contribution must remain open to discussion, checking and revision.

**Recommended entry point:** [XLVIII · The Synthesis Sees Everything™]({rel(f,links[47][2])}) · [Open Synthesis XLVIII · Issue #56]({issue56})  
**How to contribute:** [Open Synthesis contribution protocol]({rel(f,protocol)})  
**All open syntheses:** [Open Synthesis operational index]({rel(f,synth_index)})

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
    for a,b in [
        ('Índice navegable de manifiestos I–L','Índice navegable de manifiestos I–LI'),
        ('Navigable manifesto index I–L','Navigable manifesto index I–LI'),
        ('I–L · 50 manifiestos bilingües','I–LI · 51 manifiestos bilingües'),
        ('I–L · 50 bilingual manifestos','I–LI · 51 bilingual manifestos'),
        ('50 manifiestos bilingües · I–L · 17 oleadas','51 manifiestos bilingües · I–LI · 18 oleadas'),
        ('50 bilingual manifestos · I–L · 17 waves','51 bilingual manifestos · I–LI · 18 waves')]:
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
    nav.append(f'· [Índice I–LI / I–LI index]({rel(f,index)}) ·')
    nav.append(f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin de la colección / End of collection** →')
    nav += ['','> La navegación canónica mantiene la colección conectada sin convertir ningún manifiesto aislado en equivalente del marco completo. / Canonical navigation keeps the collection connected without treating any single manifesto as equivalent to the complete framework.','',nav_end]
    s=replace_or_append(s,nav_start,nav_end,'\n'.join(nav))
    if s!=old:
        f.write_text(s,encoding='utf-8'); changed.append(f)

link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
fail=[]
for f in readmes:
    s=f.read_text(encoding='utf-8')
    if s.count(invite_start)!=1 or s.count(invite_end)!=1:
        fail.append(f'{f.relative_to(root)} invitation markers')
    if 'APORTAR_A_LA_SINTESIS_ES_EN.md' not in s or 'issues/56' not in s:
        fail.append(f'{f.relative_to(root)} invitation links')
    n=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',s,re.S)
    if n:
        got=set()
        for href in link_re.findall(n.group(1)):
            h=href.split('#',1)[0].strip()
            if not h or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',h): continue
            t=(f.parent/h).resolve()
            if t in seen: got.add(t)
        if len(got)!=51: fail.append(f'{f.relative_to(root)} network {len(got)}/51')
    elif rel(f,index) not in s:
        fail.append(f'{f.relative_to(root)} canonical index missing')

for i,(roman,title,f) in enumerate(links):
    s=f.read_text(encoding='utf-8')
    if s.count(invite_start)!=1 or s.count(invite_end)!=1: fail.append(f'{f.relative_to(root)} invite')
    if s.count(nav_start)!=1 or s.count(nav_end)!=1: fail.append(f'{f.relative_to(root)} nav')
    n=re.search(re.escape(nav_start)+r'(.*?)'+re.escape(nav_end),s,re.S)
    if n:
        expected={index.resolve()}
        if i: expected.add(links[i-1][2].resolve())
        if i+1<len(links): expected.add(links[i+1][2].resolve())
        got=set()
        for href in link_re.findall(n.group(1)):
            h=href.split('#',1)[0].strip()
            if not h or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',h): continue
            t=(f.parent/h).resolve()
            if t.exists(): got.add(t)
        if not expected.issubset(got): fail.append(f'{f.relative_to(root)} prev/index/next incomplete')

for f in readmes+[x[2] for x in links]:
    s=f.read_text(encoding='utf-8')
    for a,b in [(invite_start,invite_end),(nav_start,nav_end),('<!-- NEO_ALL_MANIFESTOS_START -->','<!-- NEO_ALL_MANIFESTOS_END -->')]:
        m=re.search(re.escape(a)+r'(.*?)'+re.escape(b),s,re.S)
        if not m: continue
        for href in link_re.findall(m.group(1)):
            h=href.split('#',1)[0].strip()
            if not h or h.startswith('/') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',h): continue
            if not (f.parent/h).resolve().exists(): fail.append(f'{f.relative_to(root)} broken {href}')

print('CANONICAL_MANIFESTOS=',len(links))
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(set(changed)))
for p in sorted(set(changed)): print('CHANGED',p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    print('\n'.join(fail))
    sys.exit(1)
print('POSTCHECK OK: 51 manifestos connected; all README/LEEME targets expose Open Synthesis; managed links resolve')
