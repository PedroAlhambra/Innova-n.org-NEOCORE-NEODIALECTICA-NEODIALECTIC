from pathlib import Path
import json
import re

ROOT=Path('.').resolve()
REG=ROOT/'manifiestos/CANONICAL_FILENAMES.json'
NEO=ROOT/'neoaxiomas/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

ES_MARK=re.compile(r'^# ES · (?:Castellano|Español)\s*$',re.M)
EN_MARK=re.compile(r'^# EN · English\s*$',re.M)
CHEAD=re.compile(r'^##\s+(?:[IVXLCDM]+|\d+)\.\s+(C-NAX-(\d+) · (.+?))\s*$',re.M)
ISSUE=re.compile(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)')
QUOTE=re.compile(r'^> \*\*(.+?)\*\*\s*$',re.M)


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v<prev: total-=v
        else: total+=v; prev=v
    return total


def section_after(body, match):
    nxt=re.search(r'^##\s+',body[match.end():],re.M)
    end=match.end()+(nxt.start() if nxt else len(body)-match.end())
    return body[match.end():end]

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
        if ident not in nh:
            continue
        num=int(em.group(2)); nm=nh[ident]
        es_title=em.group(3).strip(); en_title=nm.group(3).strip()
        es_sec=section_after(esbody,em); en_sec=section_after(enbody,nm)
        eq=QUOTE.search(es_sec); nq=QUOTE.search(en_sec)
        issues=ISSUE.findall(es_sec)+ISSUE.findall(en_sec)
        if not eq or not nq or not issues:
            continue
        found[ident]={
            'num':num,'roman':roman,'path':p.relative_to(ROOT).as_posix(),
            'es_title':es_title,'en_title':en_title,
            'es_formula':eq.group(1).strip(),'en_formula':nq.group(1).strip(),
            'issue':issues[0],
        }

neo=NEO.read_text(encoding='utf-8')
changed=False
for ident,c in sorted(found.items(),key=lambda kv:kv[1]['num']):
    # Existing candidate entries remain authoritative. This synchronizer adds
    # only genuinely missing, explicitly formulated candidates.
    if re.search(r'^\| \*\*'+re.escape(ident)+r' · ',neo,re.M):
        continue
    row=(f'| **{ident} · {c["es_title"]} / {c["en_title"]}** | '
         f'[{c["roman"]}](../{c["path"]}) | '
         f'**Candidato explícito · SAN #{c["issue"]}**; no canonizado / '
         f'**Explicit candidate · SAN #{c["issue"]}**; not canonicalised |')
    # Candidate table ends before the first detailed C-NAX subsection.
    detail_marker='\n\n### C-NAX-19 ·'
    if detail_marker not in neo:
        raise SystemExit('Cannot locate candidate table/detail boundary in neoaxiomas/README.md')
    neo=neo.replace(detail_marker,'\n'+row+detail_marker,1)

    detail=(f'\n\n### {ident} · {c["es_title"]} / {c["en_title"]}\n\n'
            f'> **ES:** {c["es_formula"]}\n\n'
            f'> **EN:** {c["en_formula"]}\n\n'
            f'**Procedencia / Provenance:** [{c["roman"]}](../{c["path"]}).  \n'
            f'**Síntesis / Synthesis:** [#{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]}) · '
            f'**CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**\n')
    marker='\n<!-- NEOAXIOM_CANDIDATES_72_END -->'
    if marker not in neo:
        raise SystemExit('Cannot locate candidate block end marker')
    neo=neo.replace(marker,detail+marker,1)
    changed=True
    print(f'NEOAXIOM_CANDIDATE_ADDED {ident} source={c["roman"]} issue=#{c["issue"]}')

if found:
    max_c=max(c['num'] for c in found.values())
    # Include pre-existing candidates even if not parseable from manifest sections.
    all_nums=[int(x) for x in re.findall(r'C-NAX-(\d+)',neo)]
    max_c=max(all_nums) if all_nums else max_c
    min_c=min(all_nums) if all_nums else 15
    count=max_c-min_c+1
    neo=re.sub(r'## Candidatos neoaxiomáticos detectados en el repaso I–[IVXLCDM]+ / Neoaxiomatic candidates detected in the I–[IVXLCDM]+ review',
               f'## Candidatos neoaxiomáticos detectados en el repaso I–{latest} / Neoaxiomatic candidates detected in the I–{latest} review',neo,count=1)
    NEO.write_text(neo,encoding='utf-8')

    syn=SYN.read_text(encoding='utf-8')
    # Synchronise missing candidate rows from the newly complete Neoaxiom layer.
    for ident,c in sorted(found.items(),key=lambda kv:kv[1]['num']):
        if re.search(r'^\| \*\*'+re.escape(ident)+r' · ',syn,re.M):
            continue
        row=(f'| **{ident} · {c["es_title"]} / {c["en_title"]} · candidato / candidate** | '
             f'[#{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]}) · '
             f'[{c["roman"]} #{ISSUE.findall((ROOT/c["path"]).read_text(encoding="utf-8").split("# ES ·",1)[0])[0]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{ISSUE.findall((ROOT/c["path"]).read_text(encoding="utf-8").split("# ES ·",1)[0])[0]}) |')
        boundary='\n\n**Regla de estado / State rule:**'
        if boundary not in syn:
            raise SystemExit('Cannot locate candidate-table boundary in complete synthesis index')
        syn=syn.replace(boundary,'\n'+row+boundary,1)
    syn=re.sub(r'C-NAX-15–C-NAX-\d+',f'C-NAX-15–C-NAX-{max_c}',syn)
    syn=re.sub(r'\b7 candidatos C-NAX-15–C-NAX-\d+',f'{count} candidatos C-NAX-15–C-NAX-{max_c}',syn)
    syn=re.sub(r'\b7 candidates C-NAX-15–C-NAX-\d+',f'{count} candidates C-NAX-15–C-NAX-{max_c}',syn)
    # Coverage of manifestos is synchronised here too because this file is a
    # single public inventory surface.
    finite=len(entries)
    syn=re.sub(r'\*\*Cobertura / Coverage:\*\* \*\*\d+ manifiestos finitos I–[IVXLCDM]+',
               f'**Cobertura / Coverage:** **{finite} manifiestos finitos I–{latest}',syn,count=1)
    syn=re.sub(r'/ \d+ finite manifestos I–[IVXLCDM]+',f'/ {finite} finite manifestos I–{latest}',syn,count=1)
    syn=re.sub(r'Todo manifiesto finito I–[IVXLCDM]+ dispone',f'Todo manifiesto finito I–{latest} dispone',syn)
    syn=re.sub(r'Every finite manifesto I–[IVXLCDM]+ has',f'Every finite manifesto I–{latest} has',syn)
    SYN.write_text(syn,encoding='utf-8')

print(f'NEOAXIOM_CANDIDATE_SYNC found={len(found)} latest_manifesto={latest}')
