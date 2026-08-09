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

idx = index.read_text(encoding='utf-8')
entries = []
seen = set()
for roman, title, href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', idx, re.M):
    p = (mdir / href).resolve()
    if p in seen or not p.exists():
        continue
    seen.add(p)
    entries.append((roman, title.strip(), p))

if not entries:
    raise SystemExit('No canonical manifestos found in manifiestos/README.md')

roman, title, latest = entries[-1]
count = len(entries)
latest_text = latest.read_text(encoding='utf-8')
issue_match = re.search(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)', latest_text)
if issue_match:
    issue_num = issue_match.group(1)
else:
    # Transitional mapping for manifestos created before the issue URL was embedded in-file.
    issue_num = {'LVII':'77', 'LVIII':'78', 'LIX':'79'}.get(roman)
if not issue_num:
    raise SystemExit(f'Cannot resolve Open Synthesis issue for latest manifesto {roman}')
issue_url = f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue_num}'

START='<!-- NEO_LATEST_MANIFESTO_START -->'
END='<!-- NEO_LATEST_MANIFESTO_END -->'

def rel(f,target):
    return os.path.relpath(target,start=f.parent).replace(os.sep,'/')

def block(f):
    return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(f,latest)}) · [Síntesis Abierta {roman} · #{issue_num} / Open Synthesis {roman} · #{issue_num}]({issue_url})**  
> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Leónidas™]({rel(f,leonidas)}) · [Auditorías públicas / Public audits]({rel(f,audits)}) · [{count} manifiestos / manifestos · I–{roman}]({rel(f,index)})

{END}'''

readmes = sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
leeme = root / 'LEEME.md'
if leeme.exists():
    readmes.append(leeme)
readmes = sorted(set(readmes))
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
        if not m or latest.name not in m.group(1):
            fail.append(f'{f.relative_to(root)} latest path')
        if not m or f'#{issue_num}' not in m.group(1):
            fail.append(f'{f.relative_to(root)} latest issue')

print(f'CANONICAL_MANIFESTOS={count}')
print(f'LATEST={roman} {latest.name} ISSUE=#{issue_num}')
print('README_LEEME_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(changed))
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print(f'POSTCHECK OK: latest {roman} + Open Synthesis #{issue_num}; count={count}')
