from pathlib import Path
import os,re,sys

ROOT=Path('.').resolve()
MIDX=ROOT/'manifiestos/README.md'
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
NEO=ROOT/'neoaxiomas/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
AUD=ROOT/'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md'
REL_ISSUE='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/98'
MENU_A='<!-- NEO_RELATIONAL_MENU_START -->';MENU_B='<!-- NEO_RELATIONAL_MENU_END -->'
FOOT_A='<!-- NEO_RELATIONAL_FOOTER_START -->';FOOT_B='<!-- NEO_RELATIONAL_FOOTER_END -->'

def rel(f,t):return os.path.relpath(t,start=f.parent).replace(os.sep,'/')
def replace_block(t,a,b,block):
    if a in t and b in t:return re.sub(re.escape(a)+r'.*?'+re.escape(b),block,t,count=1,flags=re.S)
    return t

def menu(f):
    return f'''{MENU_A}

### Mapa relacional vivo / Living relational map

[Manifiestos / Manifestos]({rel(f,MIDX)}) · [Relaciones y trabajo aplicado / Relations and applied work]({rel(f,REL)}) · [Neoaxiomas™]({rel(f,NEO)}) · [Síntesis Abierta / Open Synthesis]({rel(f,SYN)}) · [Síntesis relacional / Relational synthesis #98]({REL_ISSUE}) · [Auditoría MAXPROC / MAXPROC audit]({rel(f,AUD)})

{MENU_B}'''

def footer(f):
    return f'''{FOOT_A}

## Relaciones y contexto / Relations and context

[Mapa transversal]({rel(f,REL)}) · [Síntesis relacional #98]({REL_ISSUE}) · [Mapa relacional MAXPROC]({rel(f,AUD)}) · [Neoaxiomas™]({rel(f,NEO)}) · [Índice de Síntesis Abierta]({rel(f,SYN)})

> Este bloque añade navegación y relaciones; no sustituye, resume ni reduce el cuerpo del manifiesto. / This block adds navigation and relations; it does not replace, summarise or reduce the manifesto body.

{FOOT_B}'''

readmes=sorted({p for p in ROOT.rglob('README*.md') if '.git' not in p.parts})
idx=MIDX.read_text(encoding='utf-8'); mans=[];seen=set()
for href in re.findall(r'^- \*\*[IVXLCDM]+\*\* · \[[^\]]+\]\(([^)]+\.md)\)',idx,re.M):
    p=(MIDX.parent/href).resolve()
    if p.exists() and p not in seen:seen.add(p);mans.append(p)
changed=[]
for f in readmes:
    t=f.read_text(encoding='utf-8');old=t;b=menu(f)
    if MENU_A in t and MENU_B in t:t=replace_block(t,MENU_A,MENU_B,b)
    else:
        anchor='<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'
        if anchor in t:t=t.replace(anchor,anchor+'\n\n'+b,1)
        else:t=t.rstrip()+'\n\n'+b+'\n'
    if t!=old:f.write_text(t,encoding='utf-8');changed.append(f)
for f in mans:
    t=f.read_text(encoding='utf-8');old=t;b=footer(f)
    if FOOT_A in t and FOOT_B in t:t=replace_block(t,FOOT_A,FOOT_B,b)
    else:t=t.rstrip()+'\n\n'+b+'\n'
    if t!=old:f.write_text(t,encoding='utf-8');changed.append(f)
fail=[]
for f in readmes:
    t=f.read_text(encoding='utf-8')
    if t.count(MENU_A)!=1 or t.count(MENU_B)!=1 or REL_ISSUE not in re.search(re.escape(MENU_A)+r'.*?'+re.escape(MENU_B),t,re.S).group(0):fail.append(f'{f}: menu')
for f in mans:
    t=f.read_text(encoding='utf-8')
    if t.count(FOOT_A)!=1 or t.count(FOOT_B)!=1 or REL_ISSUE not in re.search(re.escape(FOOT_A)+r'.*?'+re.escape(FOOT_B),t,re.S).group(0):fail.append(f'{f}: footer')
print('README',len(readmes),'MANIFESTOS',len(mans),'CHANGED',len(set(changed)))
if fail:print('POSTCHECK FAIL');print('\n'.join(fail));sys.exit(1)
print('POSTCHECK OK: relational navigation exposes map, audit and Open Synthesis #98 without touching source bodies')
