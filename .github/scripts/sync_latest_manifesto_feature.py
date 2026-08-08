from pathlib import Path
import os,re,sys

root=Path('.').resolve()
latest=root/'manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md'
index=root/'manifiestos/README.md'
protocol=root/'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index=root/'propuestas/sintesis-abierta/README.md'
issue59='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64'

for p in (latest,index,protocol,synth_index):
    if not p.exists(): raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

start='<!-- NEO_LATEST_MANIFESTO_START -->

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional**  
> **LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging**
>
> La propuesta está **abierta a crítica, objeciones, contraejemplos, fuentes, correcciones y propuestas de mejora**. No se pide adhesión: se pide contraste. / The proposal is **open to criticism, objections, counterexamples, sources, corrections and improvement proposals**. Endorsement is not required: scrutiny is.
>
> **[Leer manifiesto LII / Read manifesto LII](../../manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) · [Participar en la Síntesis Abierta LII · Issue #64 / Join Open Synthesis LII · Issue #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64)**  
> [Cómo aportar / How to contribute](../../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md) · [Índice de Síntesis Abierta / Open Synthesis index](../../propuestas/sintesis-abierta/README.md) · [52 manifiestos I–LII / 52 manifestos I–LII](../../manifiestos/README.md)

<!-- NEO_LATEST_MANIFESTO_END -->'

def rel(f,target):
    return os.path.relpath(target,start=f.parent).replace(os.sep,'/')

def block(f):
    return f'''{start}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional**  
> **LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging**
>
> La propuesta está **abierta a crítica, objeciones, contraejemplos, fuentes, correcciones y propuestas de mejora**. No se pide adhesión: se pide contraste. / The proposal is **open to criticism, objections, counterexamples, sources, corrections and improvement proposals**. Endorsement is not required: scrutiny is.
>
> **[Leer manifiesto LI / Read manifesto LI]({rel(f,latest)}) · [Participar en la Síntesis Abierta LI · Issue #64 / Join Open Synthesis LI · Issue #64]({issue59})**  
> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Índice de Síntesis Abierta / Open Synthesis index]({rel(f,synth_index)}) · [52 manifiestos I–LII / 52 manifestos I–LII]({rel(f,index)})

{end}'''

readmes=sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme=root/'LEEME.md'
if leeme.exists(): readmes.append(leeme)
readmes=sorted(set(readmes))
if not readmes: raise SystemExit('No README/LEEME targets found')

changed=[]
for f in readmes:
    text=f.read_text(encoding='utf-8')
    old=text
    b=block(f)
    if start in text and end in text:
        text=re.sub(re.escape(start)+r'.*?'+re.escape(end),b,text,count=1,flags=re.S)
    else:
        # Put it visibly near the top: after language selector when present, otherwise after first title block.
        m=re.search(r'^\[ES[^\n]*\]\([^\n]+\)\s*·\s*\[EN[^\n]*\]\([^\n]+\)\s*$',text,re.M)
        if m:
            pos=m.end(); text=text[:pos]+'\n\n'+b+text[pos:]
        else:
            lines=text.splitlines(True)
            insert=1 if lines and lines[0].lstrip().startswith('#') else 0
            lines.insert(insert,'\n'+b+'\n\n')
            text=''.join(lines)
    if text!=old:
        f.write_text(text,encoding='utf-8'); changed.append(f)

# Validate latest feature in every README/LEEME and local targets.
fail=[]
link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for f in readmes:
    text=f.read_text(encoding='utf-8')
    if text.count(start)!=1 or text.count(end)!=1:
        fail.append(f'{f.relative_to(root)}: latest-manifesto markers invalid')
        continue
    m=re.search(re.escape(start)+r'(.*?)'+re.escape(end),text,re.S)
    blk=m.group(1)
    if 'Issue #64' not in blk or '52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md' not in blk:
        fail.append(f'{f.relative_to(root)}: LI/Issue #64 feature incomplete')
    for href in link_re.findall(blk):
        h=href.split('#',1)[0].strip()
        if not h or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',h): continue
        if not (f.parent/h).resolve().exists(): fail.append(f'{f.relative_to(root)}: broken featured local link {href}')

# Canonical manifesto index must still expose exactly I..LI, 51 unique canonical files.
idx=index.read_text(encoding='utf-8')
net=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',idx,re.S)
if not net: fail.append('manifiestos/README.md: canonical network block missing')
else:
    items=re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)',net.group(1))
    unique=[]; seen=set()
    for roman,href in items:
        p=(index.parent/href).resolve()
        if p not in seen: seen.add(p); unique.append((roman,p))
    if len(unique)!=51 or unique[0][0]!='I' or unique[-1][0]!='LI':
        fail.append(f'manifiestos/README.md: canonical sequence invalid ({len(unique)} items)')
    for roman,p in unique:
        if not p.exists(): fail.append(f'manifesto {roman}: missing target')

print(f'README_LEEME_TARGETS={len(readmes)}')
print(f'FILES_CHANGED={len(changed)}')
for p in changed: print('CHANGED',p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    for x in fail: print(x)
    sys.exit(1)
print('POSTCHECK OK: latest LI + Open Synthesis #59 featured near top of every README/LEEME; canonical I-LI network intact')
