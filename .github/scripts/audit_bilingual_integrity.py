from pathlib import Path
import re, json, sys

ROOT=Path('.').resolve()
IDX=ROOT/'manifiestos/README.md'
NEO=ROOT/'neoaxiomas/README.md'
OUT=ROOT/'auditorias/publicas/2026-08-09_auditoria_integridad_bilingue_no_reductiva_ES_EN.md'
JOUT=ROOT/'auditorias/publicas/2026-08-09_auditoria_integridad_bilingue_no_reductiva.json'
WORD=re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9’'\-]*")
MANAGED=[
('<!-- NEO_LATEST_MANIFESTO_START -->','<!-- NEO_LATEST_MANIFESTO_END -->'),
('<!-- NEOAXIOMAS_GLOBAL_LINK_START -->','<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'),
('<!-- MANIFESTOS_CURRENT_START -->','<!-- MANIFESTOS_CURRENT_END -->'),
('<!-- NEO_ALL_MANIFESTOS_START -->','<!-- NEO_ALL_MANIFESTOS_END -->'),
('<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->','<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'),
('<!-- NEO_MANIFESTO_NAV_START -->','<!-- NEO_MANIFESTO_NAV_END -->'),
('<!-- NEO_RELATIONAL_FOOTER_START -->','<!-- NEO_RELATIONAL_FOOTER_END -->'),
('<!-- NEO_RELATIONAL_MENU_START -->','<!-- NEO_RELATIONAL_MENU_END -->'),
]
def clean(t):
    for a,b in MANAGED:t=re.sub(re.escape(a)+r'.*?'+re.escape(b),'',t,flags=re.S)
    return t

def split_bilingual(t):
    t=clean(t)
    # Supports the main heading styles used by the corpus.
    es=re.search(r'^# ES ·[^\n]*\n',t,re.M)
    en=re.search(r'^# EN ·[^\n]*\n',t,re.M)
    if not es or not en:return None,None
    if es.start()<en.start(): return t[es.end():en.start()],t[en.end():]
    return t[es.end():],t[en.end():es.start()]

def metrics(txt):
    if txt is None:return None
    return {'words':len(WORD.findall(txt)), 'headings':sum(1 for x in txt.splitlines() if x.lstrip().startswith('#')), 'paragraphs':sum(1 for x in re.split(r'\n\s*\n',txt) if len(WORD.findall(x))>=8 and not x.lstrip().startswith('#'))}

idx=IDX.read_text(encoding='utf-8')
mans=[]
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(IDX.parent/href).resolve()
    if p.exists() and p not in [x[2] for x in mans]:mans.append((roman,title,p))
rows=[]
for roman,title,p in mans:
    t=p.read_text(encoding='utf-8',errors='replace'); es,en=split_bilingual(t); me,mi=metrics(es),metrics(en)
    if not me or not mi:
        rows.append({'id':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),'missing_split':True});continue
    ratio=round(mi['words']/max(me['words'],1),3)
    rows.append({'id':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),'es':me,'en':mi,'en_es_ratio':ratio})

# Neoaxioms: compare each ES NAX section to matching EN NAX section.
nt=clean(NEO.read_text(encoding='utf-8',errors='replace'))
espart,enpart=split_bilingual(nt)
ndef nax_sections(txt):
    d={}
    if txt is None:return d
    hits=list(re.finditer(r'^## (NAX-\d{2}) · ([^\n]+)',txt,re.M))
    for i,m in enumerate(hits):
        end=hits[i+1].start() if i+1<len(hits) else len(txt)
        d[m.group(1)]={'title':m.group(2).strip(),'text':txt[m.end():end]}
    return d
nes=nax_sections(espart); nen=nax_sections(enpart)
nax=[]
for k in sorted(set(nes)|set(nen)):
    a,b=nes.get(k),nen.get(k)
    if not a or not b:nax.append({'id':k,'missing_language':True});continue
    ma,mb=metrics(a['text']),metrics(b['text']); ratio=round(mb['words']/max(ma['words'],1),3)
    nax.append({'id':k,'es_title':a['title'],'en_title':b['title'],'es':ma,'en':mb,'en_es_ratio':ratio})

# Conservative parity flags. Translation length naturally varies, so flag only large asymmetry.
flags=[r for r in rows if not r.get('missing_split') and (r['en_es_ratio']<0.68 or r['en_es_ratio']>1.47)]
nflags=[r for r in nax if not r.get('missing_language') and (r['en_es_ratio']<0.68 or r['en_es_ratio']>1.47)]
missing=[r for r in rows if r.get('missing_split')]

lines=['# Auditoría de integridad bilingüe no reductiva','## Non-reductive bilingual integrity audit','',
'**Fecha / Date:** 2026-08-09  ',f'**Manifiestos examinados / Manifestos examined:** {len(rows)}  ',f'**Neoaxiomas examinados / Neoaxioms examined:** {len(nax)}  ',
'**Regla:** una diferencia de longitud no demuestra por sí sola que exista un resumen. La auditoría sólo identifica asimetrías que requieren lectura comparada; no modifica ningún cuerpo fuente. / **Rule:** length difference alone does not prove summarisation. This audit only identifies asymmetries requiring comparative reading and changes no source body.','',
'---','','## 1. Asimetrías fuertes en manifiestos / Strong manifesto asymmetries','',
'| Nº | Archivo | ES palabras | EN words | EN/ES |','|---:|---|---:|---:|---:|']
for r in flags:lines.append(f'| {r["id"]} | `{r["path"]}` | {r["es"]["words"]} | {r["en"]["words"]} | {r["en_es_ratio"]} |')
if not flags:lines.append('| — | Ninguna / None | — | — | — |')
lines+=['','## 2. Neoaxiomas · comparación ES/EN','', '| Neoaxioma | ES palabras | EN words | EN/ES | Estado |','|---|---:|---:|---:|---|']
for r in nax:
    if r.get('missing_language'):lines.append(f'| {r["id"]} | — | — | — | **FALTA IDIOMA / MISSING LANGUAGE** |')
    else:
        status='**REVISAR / REVIEW**' if r in nflags else 'OK cuantitativo / quantitative OK'
        lines.append(f'| {r["id"]} | {r["es"]["words"]} | {r["en"]["words"]} | {r["en_es_ratio"]} | {status} |')
lines+=['','## 3. Archivos sin división bilingüe reconocible / Files without recognised bilingual split','']
if missing:
    lines += [f'- `{r["path"]}`' for r in missing]
else:lines.append('- Ninguno / None.')
lines+=['','## 4. Regla de reparación / Repair rule','',
'1. Nunca se sustituye el idioma más completo por el más corto. / Never replace the fuller language with the shorter one.',
'2. La reparación se realiza ampliando la versión reducida mediante traducción fiel del contenido fuente, conservando estructura, matices, excepciones, ejemplos y límites. / Repair expands the reduced version through faithful translation of the source, preserving structure, nuances, exceptions, examples and limits.',
'3. Si la asimetría procede de genealogías distintas o contenido añadido en un solo idioma, se conserva la evidencia y se registra el delta antes de sincronizar. / If asymmetry comes from different genealogies or one-language additions, preserve evidence and record the delta before synchronising.',
'4. Menús, índices y bloques técnicos quedan fuera de la comparación para no confundir navegación con contenido. / Menus, indexes and technical blocks are excluded so navigation is not confused with content.','']
OUT.write_text('\n'.join(lines),encoding='utf-8')
JOUT.write_text(json.dumps({'manifestos':rows,'manifesto_flags':flags,'neoaxioms':nax,'neoaxiom_flags':nflags},ensure_ascii=False,indent=2),encoding='utf-8')
print('MANIFESTOS',len(rows),'FLAGS',len(flags),'NEOAXIOMS',len(nax),'NAX_FLAGS',len(nflags),'MISSING_SPLIT',len(missing))
print('POSTCHECK OK: audit only; no source text modified')
