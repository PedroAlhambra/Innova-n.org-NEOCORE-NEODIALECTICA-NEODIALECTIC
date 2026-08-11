from pathlib import Path
import re, json
from collections import defaultdict
from itertools import combinations

ROOT = Path('.').resolve()
EXCLUDED_TOP_LEVEL = {'wiki-legacy-archive'}
MD = [
    p for p in ROOT.rglob('*.md')
    if '.git' not in p.parts
    and not (p.relative_to(ROOT).parts and p.relative_to(ROOT).parts[0] in EXCLUDED_TOP_LEVEL)
]
ARCHIVED_MD = [
    p for p in ROOT.rglob('*.md')
    if p.relative_to(ROOT).parts and p.relative_to(ROOT).parts[0] in EXCLUDED_TOP_LEVEL
]

MDIR = ROOT / 'manifiestos'
MIDX = MDIR / 'README.md'
REL = MDIR / 'RELACIONES_TRABAJO_APLICADO_ES_EN.md'
NEO = ROOT / 'neoaxiomas/README.md'
SYN = ROOT / 'propuestas/sintesis-abierta/README.md'
REPORT = ROOT / 'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md'
JSON_OUT = ROOT / 'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones.json'

MANAGED = [
    ('<!-- NEO_LATEST_MANIFESTO_START -->','<!-- NEO_LATEST_MANIFESTO_END -->'),
    ('<!-- NEOAXIOMAS_GLOBAL_LINK_START -->','<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'),
    ('<!-- MANIFESTOS_CURRENT_START -->','<!-- MANIFESTOS_CURRENT_END -->'),
    ('<!-- NEO_ALL_MANIFESTOS_START -->','<!-- NEO_ALL_MANIFESTOS_END -->'),
    ('<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->','<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'),
    ('<!-- NEO_MANIFESTO_NAV_START -->','<!-- NEO_MANIFESTO_NAV_END -->'),
    ('<!-- NEO_RELATIONAL_FOOTER_START -->','<!-- NEO_RELATIONAL_FOOTER_END -->'),
    ('<!-- NEO_RELATIONAL_MENU_START -->','<!-- NEO_RELATIONAL_MENU_END -->'),
]
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
WORD = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9’'\-]*")


def strip_managed(t):
    for a,b in MANAGED:
        t = re.sub(re.escape(a)+r'.*?'+re.escape(b),'',t,flags=re.S)
    return t


def local_target(src, href):
    h = href.split('#',1)[0].strip()
    if not h or h.startswith('/') or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',h):
        return None
    t = (src.parent / h).resolve()
    if t.exists():
        return t
    if 'wiki-source' in src.parts and not Path(h).suffix:
        alt = (src.parent / (h+'.md')).resolve()
        if alt.exists():
            return alt
    return t


idx = MIDX.read_text(encoding='utf-8')
manifestos=[]
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(MDIR/href).resolve()
    if p.exists() and p not in [x[2] for x in manifestos]:
        manifestos.append((roman,title.strip(),p))
if not manifestos:
    raise SystemExit('No canonical manifestos found')

MSET={p for _,_,p in manifestos}
BYPATH={p:(r,t) for r,t,p in manifestos}

outbound=defaultdict(set)
inbound=defaultdict(set)
broken=[]
for f in MD:
    t=f.read_text(encoding='utf-8',errors='replace')
    for href in LINK.findall(t):
        target=local_target(f,href)
        if target is None:
            continue
        if target.exists():
            outbound[f.resolve()].add(target)
            inbound[target].add(f.resolve())
        else:
            broken.append((f,href))

metrics=[]
for roman,title,p in manifestos:
    body=strip_managed(p.read_text(encoding='utf-8',errors='replace'))
    w=len(WORD.findall(body))
    h=sum(1 for x in body.splitlines() if x.lstrip().startswith('#'))
    para=sum(1 for x in re.split(r'\n\s*\n',body) if len(WORD.findall(x))>=8 and not x.lstrip().startswith('#'))
    metrics.append({
        'roman':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),
        'words':w,'headings':h,'paragraphs':para,
        'words_per_heading':round(w/max(h,1),1)
    })
short=[m for m in metrics if m['words']<900 or m['words_per_heading']<55]

reltext=REL.read_text(encoding='utf-8',errors='replace') if REL.exists() else ''
covered=[]
missing=[]
for roman,title,p in manifestos:
    if p.name in reltext:
        covered.append(roman)
    else:
        missing.append((roman,title,p))

# Canonical Neoaxioms NAX-01..NAX-14 must keep a dedicated synthesis in
# addition to the general matrix #80. Candidates C-NAX are audited elsewhere
# because candidate status is intentionally different from canon.
naxraw=NEO.read_text(encoding='utf-8',errors='replace')
nd=defaultdict(lambda:{'titles':set(),'issues':set()})
pat=re.compile(r'^## (NAX-\d{2}) · ([^\n]+)\n(.*?)(?=^## NAX-\d{2} ·|^## \d+\.|^## Open Synthesis|^# EN ·|\Z)',re.M|re.S)
for ident,title,body in pat.findall(naxraw):
    nd[ident]['titles'].add(title.strip())
    nd[ident]['issues'].update(re.findall(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',body))
neoaxioms=[]
for ident in sorted(nd,key=lambda x:int(x.split('-')[1])):
    vals=nd[ident]
    issues=sorted(vals['issues'],key=int)
    dedicated=[x for x in issues if x!='80']
    neoaxioms.append({'id':ident,'titles':sorted(vals['titles']),'issues':issues,'dedicated':dedicated})
nax_missing=[x for x in neoaxioms if not x['dedicated']]


def is_publication(p):
    try:
        r=p.relative_to(ROOT)
    except ValueError:
        return False
    if p in MSET:
        return False
    return bool(r.parts and r.parts[0] in {
        'analisis','auditorias','propuestas','obras','anuncios','difusion','proyeccion','wiki-source'
    })

pubs=[]
pub_inbound=defaultdict(set)
pair_sources=defaultdict(set)
for f in MD:
    fr=f.resolve()
    if not is_publication(fr):
        continue
    linked=sorted([x for x in outbound[fr] if x in MSET],key=lambda p:BYPATH[p][0])
    if linked:
        rr=f.relative_to(ROOT).as_posix()
        pubs.append({'path':rr,'manifestos':[BYPATH[p][0] for p in linked]})
        for p in linked:
            pub_inbound[p].add(fr)
        for a,b in combinations(linked,2):
            pair_sources[tuple(sorted((a,b),key=lambda p:BYPATH[p][0]))].add(fr)
weak=[
    {'roman':r,'title':t,'path':p.relative_to(ROOT).as_posix(),'publication_links':len(pub_inbound[p])}
    for r,t,p in manifestos if len(pub_inbound[p])==0
]
co=[]
for (a,b),srcs in pair_sources.items():
    if len(srcs)>=2:
        co.append({
            'a':BYPATH[a][0],'b':BYPATH[b][0],'sources':len(srcs),
            'examples':[p.relative_to(ROOT).as_posix() for p in sorted(srcs)[:8]]
        })
co.sort(key=lambda x:(-x['sources'],x['a'],x['b']))


def group(paths):
    g=defaultdict(list)
    for p in sorted(paths,key=lambda x:x.as_posix().lower()):
        try:
            r=p.relative_to(ROOT)
        except ValueError:
            continue
        if p in MSET: k='manifiestos'
        elif r.parts[:2]==('analisis','publicos'): k='analisis/publicos'
        elif r.parts[:2]==('auditorias','publicas'): k='auditorias/publicas'
        elif r.parts[:2]==('propuestas','sintesis-abierta'): k='sintesis-abierta'
        elif r.parts and r.parts[0]=='obras': k='obras'
        elif r.parts and r.parts[0]=='proyeccion': k='proyeccion'
        elif r.parts and r.parts[0]=='neoaxiomas': k='neoaxiomas'
        else: k='otros'
        g[k].append(r.as_posix())
    return dict(g)

graph=[
    {'roman':r,'title':t,'path':p.relative_to(ROOT).as_posix(),
     'outbound':group(outbound[p]),'inbound':group(inbound[p])}
    for r,t,p in manifestos
]

entry=[ROOT/'README.md',MIDX,SYN,NEO,REL]
menu=[]
for p in entry:
    t=p.read_text(encoding='utf-8',errors='replace') if p.exists() else ''
    menu.append({
        'path':p.relative_to(ROOT).as_posix(),
        'neoaxiomas':('neoaxiomas/README.md' in t or p==NEO),
        'sintesis':('propuestas/sintesis-abierta/README.md' in t or p==SYN),
        'relations':('RELACIONES_TRABAJO_APLICADO_ES_EN.md' in t or p==REL),
        'manifestos':('manifiestos/README.md' in t or p==MIDX),
        'audit':('2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md' in t or p==REPORT)
    })

lines=[
'# Auditoría relacional MAXPROC · Manifiestos ↔ Neoaxiomas ↔ publicaciones ↔ Síntesis Abierta',
'## MAXPROC relational audit · Manifestos ↔ Neoaxioms ↔ publications ↔ Open Synthesis','',
'**Fecha / Date:** 2026-08-12  ',
f'**Manifiestos canónicos / Canonical manifestos:** {len(manifestos)} · I–{manifestos[-1][0]}  ',
f'**Markdown activo examinado / Active Markdown scanned:** {len(MD)}  ',
f'**Archivo histórico excluido del estado vivo / Historical archive excluded from living state:** {len(ARCHIVED_MD)} archivos / files  ',
'**Regla de integridad:** esta auditoría no resume, acorta ni reescribe cuerpos fuente. Detecta relaciones documentales y candidatos a revisión; las relaciones semánticas o causales siguen requiriendo SAN/revisión humana. / **Integrity rule:** this audit never summarises, shortens or rewrites source bodies. It detects documentary relations and review candidates; semantic or causal relations still require SAN/human review.','',
'## 1. Estado estructural / Structural state','',
f'- Cobertura del mapa curado: **{len(covered)}/{len(manifestos)}**.',
f'- Ausentes del mapa curado: **{", ".join(x[0] for x in missing) if missing else "ninguno / none"}**.',
f'- Neoaxiomas sin Síntesis específica: **{", ".join(x["id"] for x in nax_missing) if nax_missing else "ninguno / none"}**.',
f'- Enlaces locales realmente no resueltos: **{len(broken)}**.',
f'- Manifiestos sin enlace entrante desde publicaciones/documentos aplicados: **{len(weak)}**.',
f'- Pares de manifiestos cocitados por ≥2 publicaciones: **{len(co)}**.','',
'## 2. Densidad documental · sólo alarma, nunca reducción','',
'| Nº | Archivo | Palabras | Encabezados | Párrafos | Palabras/encabezado |',
'|---:|---|---:|---:|---:|---:|'
]
for m in short:
    lines.append(f'| {m["roman"]} | `{m["path"]}` | {m["words"]} | {m["headings"]} | {m["paragraphs"]} | {m["words_per_heading"]} |')
lines += [
'',
'> Una bandera de densidad no autoriza a reescribir. Debe compararse con fuentes e historial; si falta desarrollo previo, se restaura o amplía sin borrar el texto vigente.','',
'## 3. Neoaxiomas ↔ Síntesis específica','',
'| Neoaxioma | Issues detectados | Síntesis específica |','|---|---|---|'
]
for x in neoaxioms:
    lines.append(f'| {x["id"]} | {", ".join("#"+i for i in x["issues"])} | {", ".join("#"+i for i in x["dedicated"]) if x["dedicated"] else "**FALTA**"} |')

lines += ['', '## 4. Cobertura de publicaciones','']
if weak:
    lines.append('**Sin relación entrante directa desde documentos aplicados / Without direct inbound applied-document relation:**')
    for x in weak:
        lines.append(f'- **{x["roman"]}** · `{x["path"]}`')
else:
    lines.append('- Todos los manifiestos tienen al menos una relación documental entrante desde publicaciones/documentos aplicados. / Every manifesto has at least one inbound documentary relation from applied publications/documents.')

lines += [
'', '### Cocitación documental · candidatos de relación para revisión SAN','',
'> Cocitación significa que dos manifiestos son enlazados por los mismos documentos. Es evidencia de relación documental, no de equivalencia ni causalidad.','',
'| Par | Nº fuentes | Ejemplos |','|---|---:|---|'
]
for x in co[:100]:
    lines.append(f'| **{x["a"]} ↔ {x["b"]}** | {x["sources"]} | ' + '<br>'.join(f'`{e}`' for e in x['examples'][:4]) + ' |')

lines += ['', '## 5. Menús y puertas','',
'| Superficie | Neoaxiomas | Síntesis | Relaciones | Manifiestos | Auditoría |','|---|:---:|:---:|:---:|:---:|:---:|']
for x in menu:
    q=lambda b:'✓' if b else '✗'
    lines.append(f'| `{x["path"]}` | {q(x["neoaxiomas"])} | {q(x["sintesis"])} | {q(x["relations"])} | {q(x["manifestos"])} | {q(x["audit"])} |')

lines += ['', '## 6. Enlaces locales no resueltos','']
if broken:
    for f,h in broken:
        lines.append(f'- `{f.relative_to(ROOT).as_posix()}` → `{h}`')
else:
    lines.append('- Ninguno / None.')

lines += ['', '## 7. Grafo directo completo por manifiesto','']
for x in graph:
    lines += [f'### {x["roman"]} · {x["title"]}',f'`{x["path"]}`']
    for label,data in [('Salientes / Outbound',x['outbound']),('Entrantes / Inbound',x['inbound'])]:
        lines.append(f'**{label}:**')
        if not data:
            lines.append('- ninguna / none')
        else:
            for k,vals in data.items():
                lines.append(f'- **{k}:** '+' · '.join(f'`{v}`' for v in vals))
    lines.append('')

lines += [
'## 8. Regla permanente de mantenimiento','',
'1. Ninguna automatización puede sustituir un manifiesto, Neoaxioma u otro cuerpo fuente por un resumen ni reducir deliberadamente su contenido.',
'2. Toda nueva publicación debe declarar o descubrir relaciones con manifiestos, Neoaxiomas, auditorías y Síntesis Abierta cuando existan.',
'3. Toda pieza canónica debe exponer retorno a índices y Síntesis relacionadas sin convertir navegación en sustituto del texto.',
'4. Las relaciones por enlace y cocitación son documentales; las relaciones semánticas/causales requieren SAN.',
'5. Las ilustraciones se añaden como capa expresiva con alt/procedencia, sin sustituir texto ni genealogía.',''
]

REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines),encoding='utf-8')
JSON_OUT.write_text(json.dumps({
    'metrics':metrics,
    'density_flags':short,
    'relation_missing':[x[0] for x in missing],
    'neoaxioms':neoaxioms,
    'neoaxioms_missing_dedicated':[x['id'] for x in nax_missing],
    'broken':[{'source':f.relative_to(ROOT).as_posix(),'href':h} for f,h in broken],
    'weak_publication_relations':weak,
    'co_citation':co,
    'publication_hubs':pubs,
    'graph':graph,
    'menu':menu,
    'archived_markdown_excluded':len(ARCHIVED_MD),
},ensure_ascii=False,indent=2),encoding='utf-8')

print('MANIFESTOS',len(manifestos),'MAP',len(covered),'/',len(manifestos),'NAX_MISSING',len(nax_missing),'BROKEN',len(broken),'WEAK_PUB',len(weak),'COCITATION',len(co),'ARCHIVED_EXCLUDED',len(ARCHIVED_MD))
print('POSTCHECK OK: non-reductive relational audit generated')
