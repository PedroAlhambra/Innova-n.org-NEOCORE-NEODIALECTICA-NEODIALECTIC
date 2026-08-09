from pathlib import Path
import os,re,sys
ROOT=Path('.').resolve(); IDX=ROOT/'manifiestos/README.md'; MDIR=IDX.parent
idx=IDX.read_text(encoding='utf-8')
items=[];seen=set()
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(MDIR/href).resolve()
    if p.exists() and p not in seen:seen.add(p);items.append((roman,title.strip(),p))
if len(items)!=59 or items[-1][0]!='LIX':raise SystemExit(f'Unexpected corpus: {len(items)}')
A='<!-- NEO_MANIFESTO_NAV_START -->';B='<!-- NEO_MANIFESTO_NAV_END -->'
def rel(f,t):return os.path.relpath(t,start=f.parent).replace(os.sep,'/')
def block(i,f):
    prev=items[i-1] if i else None; nxt=items[i+1] if i+1<len(items) else None
    left=f'← **{prev[0]}** · [{prev[1]}]({rel(f,prev[2])})' if prev else '← **Inicio de la colección / Start of collection**'
    right=f'**{nxt[0]}** · [{nxt[1]}]({rel(f,nxt[2])}) →' if nxt else '**Fin provisional de la colección / Provisional end of collection** →'
    return f'''{A}

## Navegación canónica / Canonical navigation

{left}  
· [Índice I–LIX / I–LIX index]({rel(f,IDX)}) · [Síntesis Abierta / Open Synthesis]({rel(f,ROOT/'propuestas/sintesis-abierta/README.md')}) · [Neoaxiomas™]({rel(f,ROOT/'neoaxiomas/README.md')}) ·  
{right}

> Este bloque es navegación aditiva. No sustituye ni resume el cuerpo del manifiesto. / This is an additive navigation block. It does not replace or summarise the manifesto body.

{B}'''
changed=[]
for i,(_,_,f) in enumerate(items):
    t=f.read_text(encoding='utf-8'); old=t; b=block(i,f)
    if A in t and B in t:t=re.sub(re.escape(A)+r'.*?'+re.escape(B),b,t,count=1,flags=re.S)
    else:t=t.rstrip()+'\n\n'+b+'\n'
    if t!=old:f.write_text(t,encoding='utf-8');changed.append(f)
# Fix the exact obsolete generated top-anchor fragment wherever it survived; this is navigation only.
anchor_changes=[]
for f in ROOT.rglob('*.md'):
    if '.git' in f.parts:continue
    t=f.read_text(encoding='utf-8',errors='replace'); old=t
    t=t.replace('#innova_n--neocore-70--','#innova_n--neocore-71--')
    if t!=old:f.write_text(t,encoding='utf-8');anchor_changes.append(f)
# postcheck
fail=[]
for i,(_,_,f) in enumerate(items):
    t=f.read_text(encoding='utf-8')
    if t.count(A)!=1 or t.count(B)!=1:fail.append(f'{f}: marker count')
    m=re.search(re.escape(A)+r'(.*?)'+re.escape(B),t,re.S)
    if not m or 'README.md' not in m.group(1) or 'propuestas/sintesis-abierta/README.md' not in m.group(1):fail.append(f'{f}: links')
for f in ROOT.rglob('*.md'):
    if '.git' not in f.parts and '#innova_n--neocore-70--' in f.read_text(encoding='utf-8',errors='replace'):fail.append(f'{f}: stale root anchor')
print('MANIFESTOS',len(items),'NAV_CHANGED',len(changed),'ANCHOR_CHANGED',len(anchor_changes))
if fail:print('POSTCHECK FAIL');print('\n'.join(fail));sys.exit(1)
print('POSTCHECK OK: 59/59 managed canonical nav; stale 7.0 root anchors removed')
