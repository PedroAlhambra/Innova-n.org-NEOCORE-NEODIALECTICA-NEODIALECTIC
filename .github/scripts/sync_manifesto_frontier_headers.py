from pathlib import Path
import re

ROOT=Path('.').resolve()
MIDX=ROOT/'manifiestos/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
FULL=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
ROW=re.compile(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)(.*)$',re.M)
ISSUE=re.compile(r'https://github\.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)')
DATE=re.compile(r'^\*\*Fecha / Date:\*\*\s*(\d{4}-\d{2}-\d{2})\s*$',re.M)

idx=MIDX.read_text(encoding='utf-8')
rows=ROW.findall(idx)
if not rows:
    raise SystemExit('No finite manifesto rows found')
roman,label,href,suffix=rows[-1]
count=len(rows)
p=ROOT/'manifiestos'/href
front=p.read_text(encoding='utf-8').split('# ES ·',1)[0]
# Prefer the canonical issue already registered in the manifesto index row.
# Fall back to the manifesto front matter for compatibility with older files.
# 2026-08-18: retrigger marker after canonical-index issue fix.
issues=ISSUE.findall(suffix) or ISSUE.findall(front)
if not issues:
    raise SystemExit(f'No manifesto synthesis issue found for {roman}')
issue=issues[0]
dates=DATE.findall(front)
if not dates:
    raise SystemExit(f'No manifesto date found for {roman}')
latest_date=dates[0]
issue_url=f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue}'

latest=(f'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n'
        f'> **{roman} · {label}**\n>\n'
        f'> **[{label}]({href}) · [Síntesis Abierta {roman} · #{issue} / Open Synthesis {roman} · #{issue}]({issue_url})**')

idx=re.sub(r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>.*?(?=\n> ## ∞)',latest+'\n',idx,count=1,flags=re.S)
idx=re.sub(r'^\*\*(?:Estado en este commit / State at this commit|Frontera canónica vigente / Current canonical frontier):\*\*.*$',
           f'**Frontera canónica vigente / Current canonical frontier:** **{count} manifiestos finitos bilingües · I–{roman} + Manifiesto ∞ / {count} finite bilingual manifestos · I–{roman} + Manifesto ∞**  ',idx,count=1,flags=re.M)
idx=re.sub(r'Índice completo I–[IVXLCDM]+ \+ ∞',f'Índice completo I–{roman} + ∞',idx)
idx=re.sub(r'Complete index I–[IVXLCDM]+ \+ ∞',f'Complete index I–{roman} + ∞',idx)
idx=re.sub(r'^\*\*Última síntesis finita / Latest finite synthesis:\*\*.*$',
           f'**Última síntesis finita / Latest finite synthesis:** [{label}]({href}) · [Issue #{issue}]({issue_url})  ',
           idx,count=1,flags=re.M)
idx=re.sub(r'^\*\*(?:Fecha / Date|Fecha de fijación de esta frontera / Frontier fixation date):\*\*.*$',
           f'**Fecha de fijación de esta frontera / Frontier fixation date:** {latest_date}',idx,count=1,flags=re.M)
MIDX.write_text(idx,encoding='utf-8')

syn=SYN.read_text(encoding='utf-8')
syn=re.sub(r'^\*\*Cobertura actual / Current coverage:\*\*.*$',
           f'**Cobertura actual / Current coverage:** **{count} manifiestos finitos · I–{roman} + Manifiesto ∞ · 14 Neoaxiomas™ · síntesis transversales, auditorías y proyectos / {count} finite manifestos · I–{roman} + Manifesto ∞ · 14 Neoaxioms™ · transversal syntheses, audits and projects**',syn,count=1,flags=re.M)
slatest=(f'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n'
         f'> **{roman} · {label}**\n>\n'
         f'> **[Leer {roman} / Read {roman}](../../manifiestos/{href}) · [Síntesis {roman} · #{issue} / Synthesis {roman} · #{issue}]({issue_url})**')
syn=re.sub(r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>.*?(?=\n> ## ∞)',slatest+'\n',syn,count=1,flags=re.S)
SYN.write_text(syn,encoding='utf-8')

full=FULL.read_text(encoding='utf-8')
full=re.sub(r'^\*\*Fecha / Date:\*\*.*$',f'**Fecha / Date:** {latest_date}',full,count=1,flags=re.M)
FULL.write_text(full,encoding='utf-8')

print(f'MANIFESTO_FRONTIER_HEADERS count={count} latest={roman} issue=#{issue} date={latest_date}')
