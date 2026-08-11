from pathlib import Path
import json
import re

ROOT=Path('.').resolve()
REG=ROOT/'manifiestos/CANONICAL_FILENAMES.json'
NEO=ROOT/'neoaxiomas/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

ES_MARK=re.compile(r'^# ES · (?:Castellano|Español)\s*$',re.M)
EN_MARK=re.compile(r'^# EN · English\s*$',re.M)
CHEAD=re.compile(r'^##\s+(?:[IVXLCDM]+|\d+)\.\s+(C-NAX-(\d+)) · (.+?)\s*$',re.M)
ISSUE=re.compile(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)')
QUOTE=re.compile(r'^> \*\*(.+?)\*\*\s*$',re.M)


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v<prev: total-=v
        else: total+=v; prev=v
    return total


def subsection(body,m):
    rest=body[m.end():]
    nxt=re.search(r'^##\s+',rest,re.M)
    return rest[:nxt.start()] if nxt else rest

entries=json.loads(REG.read_text(encoding='utf-8')).get('entries',{})
latest=max(entries,key=roman_to_int)
found={}
for roman,entry in sorted(entries.items(),key=lambda kv:roman_to_int(kv[0])):
    p=ROOT/entry['legacy']
    text=p.read_text(encoding='utf-8',errors='replace')
    es=ES_MARK.search(text); en=EN_MARK.search(text)
    if not es or not en or en.start()<es.start():
        continue
    esbody=text[es.end():en.start()]; enbody=text[en.end():]
    eh={m.group(1):m for m in CHEAD.finditer(esbody)}
    nh={m.group(1):m for m in CHEAD.finditer(enbody)}
    for ident,em in eh.items():
        nm=nh.get(ident)
        if not nm:
            continue
        es_sec=subsection(esbody,em); en_sec=subsection(enbody,nm)
        eq=QUOTE.search(es_sec); nq=QUOTE.search(en_sec)
        issue_candidates=ISSUE.findall(es_sec)+ISSUE.findall(en_sec)
        if not eq or not nq or not issue_candidates:
            continue
        front=text.split('# ES ·',1)[0]
        manifesto_issues=ISSUE.findall(front)
        found[ident]={
            'num':int(em.group(2)),'roman':roman,'path':p.relative_to(ROOT).as_posix(),
            'es_title':em.group(3).strip(),'en_title':nm.group(3).strip(),
            'es_formula':eq.group(1).strip(),'en_formula':nq.group(1).strip(),
            'issue':issue_candidates[0],
            'manifesto_issue':manifesto_issues[0] if manifesto_issues else None,
        }

neo=NEO.read_text(encoding='utf-8')
for ident,c in sorted(found.items(),key=lambda kv:kv[1]['num']):
    if not re.search(r'^\| \*\*'+re.escape(ident)+r' · ',neo,re.M):
        row=(f'| **{ident} · {c["es_title"]} / {c["en_title"]}** | '
             f'[{c["roman"]}](../{c["path"]}) | '
             f'**Candidato explícito · SAN #{c["issue"]}**; no canonizado / '
             f'**Explicit candidate · SAN #{c["issue"]}**; not canonicalised |')
        boundary='\n\n### C-NAX-19 ·'
        if boundary not in neo:
            raise SystemExit('Cannot locate Neoaxiom candidate table boundary')
        neo=neo.replace(boundary,'\n'+row+boundary,1)
        print(f'NEOAXIOM_CANDIDATE_ROW_ADDED {ident}')

    if not re.search(r'^### '+re.escape(ident)+r' · ',neo,re.M):
        detail=(f'\n\n### {ident} · {c["es_title"]} / {c["en_title"]}\n\n'
                f'> **ES:** {c["es_formula"]}\n\n'
                f'> **EN:** {c["en_formula"]}\n\n'
                f'**Procedencia / Provenance:** [{c["roman"]}](../{c["path"]}).  \n'
                f'**Síntesis / Synthesis:** [#{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]}) · '
                f'**CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**\n')
        marker='\n<!-- NEOAXIOM_CANDIDATES_72_END -->'
        if marker not in neo:
            raise SystemExit('Cannot locate Neoaxiom candidate block end')
        neo=neo.replace(marker,detail+marker,1)
        print(f'NEOAXIOM_CANDIDATE_DETAIL_ADDED {ident}')

all_nums=sorted(set(int(x) for x in re.findall(r'C-NAX-(\d+)',neo)))
if all_nums:
    min_c=min(all_nums); max_c=max(all_nums); count=len([x for x in all_nums if x>=15])
    neo=re.sub(r'## Candidatos neoaxiomáticos detectados en el repaso I–[IVXLCDM]+ / Neoaxiomatic candidates detected in the I–[IVXLCDM]+ review',
               f'## Candidatos neoaxiomáticos detectados en el repaso I–{latest} / Neoaxiomatic candidates detected in the I–{latest} review',neo,count=1)
NEO.write_text(neo,encoding='utf-8')

syn=SYN.read_text(encoding='utf-8')
for ident,c in sorted(found.items(),key=lambda kv:kv[1]['num']):
    if re.search(r'^\| \*\*'+re.escape(ident)+r' · ',syn,re.M):
        continue
    extra=''
    if c['manifesto_issue']:
        extra=(f' · [{c["roman"]} #{c["manifesto_issue"]}]'
               f'(https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["manifesto_issue"]})')
    row=(f'| **{ident} · {c["es_title"]} / {c["en_title"]} · candidato / candidate** | '
         f'[#{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]}){extra} |')
    boundary='\n\n**Regla de estado / State rule:**'
    if boundary not in syn:
        raise SystemExit('Cannot locate candidate table boundary in complete synthesis index')
    syn=syn.replace(boundary,'\n'+row+boundary,1)
    print(f'SYNTHESIS_CANDIDATE_ROW_ADDED {ident}')

if all_nums:
    max_c=max(all_nums); candidate_nums=sorted(x for x in all_nums if x>=15); count=len(candidate_nums)
    syn=re.sub(r'C-NAX-15–C-NAX-\d+',f'C-NAX-15–C-NAX-{max_c}',syn)
    syn=re.sub(r'\b\d+ candidatos C-NAX-15–C-NAX-\d+',f'{count} candidatos C-NAX-15–C-NAX-{max_c}',syn)
    syn=re.sub(r'\b\d+ candidates C-NAX-15–C-NAX-\d+',f'{count} candidates C-NAX-15–C-NAX-{max_c}',syn)
finite=len(entries)
syn=re.sub(r'\*\*Cobertura / Coverage:\*\* \*\*\d+ manifiestos finitos I–[IVXLCDM]+',
           f'**Cobertura / Coverage:** **{finite} manifiestos finitos I–{latest}',syn,count=1)
syn=re.sub(r'/ \d+ finite manifestos I–[IVXLCDM]+',f'/ {finite} finite manifestos I–{latest}',syn,count=1)
syn=re.sub(r'Todo manifiesto finito I–[IVXLCDM]+ dispone',f'Todo manifiesto finito I–{latest} dispone',syn)
syn=re.sub(r'Every finite manifesto I–[IVXLCDM]+ has',f'Every finite manifesto I–{latest} has',syn)
SYN.write_text(syn,encoding='utf-8')

print(f'NEOAXIOM_CANDIDATE_SYNC found={len(found)} latest_manifesto={latest}')
