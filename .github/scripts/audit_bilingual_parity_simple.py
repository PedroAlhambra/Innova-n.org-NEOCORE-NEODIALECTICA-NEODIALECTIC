from pathlib import Path
import re,json
ROOT=Path('.').resolve(); IDX=ROOT/'manifiestos/README.md'; NEO=ROOT/'neoaxiomas/README.md'
OUT=ROOT/'auditorias/publicas/2026-08-09_auditoria_paridad_bilingue_manifiestos_neoaxiomas_ES_EN.md'
J=ROOT/'auditorias/publicas/2026-08-09_auditoria_paridad_bilingue_manifiestos_neoaxiomas.json'
WORD=re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9’'\-]*")

def clean(t):
    # Remove every managed NEO_* block and MANIFESTOS_CURRENT so navigation/relations never masquerade as prose.
    old=None
    while old!=t:
        old=t
        t=re.sub(r'<!-- ([A-Z0-9_]+)_START -->.*?<!-- \1_END -->','',t,flags=re.S)
    t=re.sub(r'<!-- MANIFESTOS_CURRENT_START -->.*?<!-- MANIFESTOS_CURRENT_END -->','',t,flags=re.S)
    return t

def parts(t):
    t=clean(t); a=re.search(r'^# ES ·[^\n]*\n',t,re.M); b=re.search(r'^# EN ·[^\n]*\n',t,re.M)
    if not a or not b:return None,None
    if a.start()<b.start():return t[a.end():b.start()],t[b.end():]
    return t[a.end():],t[b.end():a.start()]
def wc(t):return len(WORD.findall(t or ''))

idx=IDX.read_text(encoding='utf-8'); rows=[];seen=set()
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(IDX.parent/href).resolve()
    if not p.exists() or p in seen:continue
    seen.add(p); es,en=parts(p.read_text(encoding='utf-8',errors='replace'))
    ew,nw=wc(es),wc(en); ratio=round(nw/max(ew,1),3) if es is not None and en is not None else None
    rows.append({'id':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),'es':ew,'en':nw,'ratio':ratio})
flags=[r for r in rows if r['ratio'] is None or r['ratio']<0.72 or r['ratio']>1.39]

# NAX parity: stop section bodies at the next NAX or at the structural relation/open-synthesis headings.
nt=NEO.read_text(encoding='utf-8',errors='replace'); nes,nen=parts(nt)
def secs(t):
    out={}; txt=t or ''; hits=list(re.finditer(r'^## (NAX-\d{2}) · [^\n]+',txt,re.M))
    structural=[m.start() for m in re.finditer(r'^## (?:\d+\.|Open Synthesis)',txt,re.M)]
    for i,m in enumerate(hits):
        candidates=[hits[i+1].start()] if i+1<len(hits) else []
        candidates += [x for x in structural if x>m.start()]
        end=min(candidates) if candidates else len(txt)
        out[m.group(1)]=txt[m.end():end]
    return out
a,b=secs(nes),secs(nen); nrows=[]
for k in sorted(set(a)|set(b),key=lambda x:int(x.split('-')[1])):
    ew,nw=wc(a.get(k,'')),wc(b.get(k,''));ratio=round(nw/max(ew,1),3) if k in a and k in b else None
    nrows.append({'id':k,'es':ew,'en':nw,'ratio':ratio})
nflags=[r for r in nrows if r['ratio'] is None or r['ratio']<0.72 or r['ratio']>1.39]

lines=['# Auditoría de paridad bilingüe no reductiva','## Non-reductive bilingual parity audit','',f'**Manifiestos examinados / Manifestos:** {len(rows)}  ',f'**Neoaxiomas / Neoaxioms:** {len(nrows)}  ','**Regla:** la longitud es sólo señal de auditoría; nunca autoriza resumir ni borrar. Todos los bloques gestionados de navegación, relaciones, menús e índices quedan fuera del recuento. La reparación, cuando proceda, amplía el idioma reducido desde la fuente completa. / **Rule:** length is only an audit signal; it never authorises summarising or deletion. All managed navigation, relation, menu and index blocks are excluded. Repair, where needed, expands the reduced language from the complete source.','', '## Manifiestos con asimetría fuerte / Strong manifesto asymmetry','', '| Nº | ES | EN | EN/ES | Archivo |','|---:|---:|---:|---:|---|']
for r in flags:lines.append(f'| {r["id"]} | {r["es"]} | {r["en"]} | {r["ratio"] if r["ratio"] is not None else "N/A"} | `{r["path"]}` |')
if not flags:lines.append('| — | — | — | — | Ninguno / None |')
lines+=['','## Neoaxiomas / Neoaxioms','', '| ID | ES | EN | EN/ES | Estado |','|---|---:|---:|---:|---|']
for r in nrows:
    st='REVISAR / REVIEW' if r in nflags else 'OK'
    lines.append(f'| {r["id"]} | {r["es"]} | {r["en"]} | {r["ratio"] if r["ratio"] is not None else "N/A"} | {st} |')
lines+=['','## Regla de conservación','', '- Mantener siempre la versión más completa como fuente de reparación.','- No reducir un idioma para igualarlo al otro.','- Conservar ejemplos, excepciones, estructura, matices y límites epistemológicos.','- Registrar cualquier divergencia intencional como delta, no como sustitución silenciosa.','']
OUT.write_text('\n'.join(lines),encoding='utf-8');J.write_text(json.dumps({'manifestos':rows,'flags':flags,'neoaxioms':nrows,'nax_flags':nflags},ensure_ascii=False,indent=2),encoding='utf-8')
print('MANIFESTOS',len(rows),'FLAGS',len(flags),'NAX',len(nrows),'NAX_FLAGS',len(nflags));print('POSTCHECK OK')
