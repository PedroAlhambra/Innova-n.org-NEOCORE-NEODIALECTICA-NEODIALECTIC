from pathlib import Path
import os, re, sys, json
from collections import defaultdict

ROOT = Path('.').resolve()
MD = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts]
MANIFEST_DIR = ROOT / 'manifiestos'
MANIFEST_INDEX = MANIFEST_DIR / 'README.md'
REL_MAP = MANIFEST_DIR / 'RELACIONES_TRABAJO_APLICADO_ES_EN.md'
NEOAX = ROOT / 'neoaxiomas' / 'README.md'
REPORT = ROOT / 'auditorias' / 'publicas' / '2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md'
JSON_OUT = ROOT / 'auditorias' / 'publicas' / '2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones.json'

MANAGED = [
    ('<!-- NEO_LATEST_MANIFESTO_START -->','<!-- NEO_LATEST_MANIFESTO_END -->'),
    ('<!-- NEOAXIOMAS_GLOBAL_LINK_START -->','<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'),
    ('<!-- MANIFESTOS_CURRENT_START -->','<!-- MANIFESTOS_CURRENT_END -->'),
    ('<!-- NEO_ALL_MANIFESTOS_START -->','<!-- NEO_ALL_MANIFESTOS_END -->'),
    ('<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->','<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'),
    ('<!-- NEO_MANIFESTO_NAV_START -->','<!-- NEO_MANIFESTO_NAV_END -->'),
]
LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
WORD_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9’'\-]*")


def strip_managed(text):
    for a,b in MANAGED:
        text = re.sub(re.escape(a)+r'.*?'+re.escape(b), '', text, flags=re.S)
    return text


def local_target(src, href):
    h = href.split('#',1)[0].strip()
    if not h or h.startswith('/') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',h):
        return None
    return (src.parent / h).resolve()

idx = MANIFEST_INDEX.read_text(encoding='utf-8')
manifestos=[]
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', idx, re.M):
    p=(MANIFEST_DIR/href).resolve()
    if p.exists() and p not in [x[2] for x in manifestos]:
        manifestos.append((roman,title.strip(),p))
if not manifestos:
    raise SystemExit('No manifestos parsed from canonical index')

manifest_set={p for _,_,p in manifestos}
# direct graph from actual Markdown links only
outbound=defaultdict(set); inbound=defaultdict(set)
broken=[]
for f in MD:
    text=f.read_text(encoding='utf-8', errors='replace')
    for href in LINK_RE.findall(text):
        t=local_target(f,href)
        if t is None: continue
        if not t.exists(): broken.append((f,t,href))
        else:
            outbound[f.resolve()].add(t)
            inbound[t].add(f.resolve())

# Manifesto body metrics. These do not change source content.
metrics=[]
for roman,title,p in manifestos:
    raw=p.read_text(encoding='utf-8',errors='replace')
    body=strip_managed(raw)
    words=len(WORD_RE.findall(body))
    headings=sum(1 for ln in body.splitlines() if ln.lstrip().startswith('#'))
    paras=sum(1 for block in re.split(r'\n\s*\n',body) if len(WORD_RE.findall(block))>=8 and not block.lstrip().startswith('#'))
    prose_per_heading=round(words/max(headings,1),1)
    metrics.append({'roman':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),'words':words,'headings':headings,'paragraphs':paras,'words_per_heading':prose_per_heading})

# Conservative flags: only identify candidates for human/source recovery; never rewrite or summarize.
short=[m for m in metrics if m['words'] < 900 or m['words_per_heading'] < 55]

# Coverage of curated relation map by actual manifesto file link.
rel_text=REL_MAP.read_text(encoding='utf-8',errors='replace') if REL_MAP.exists() else ''
relation_covered=[]; relation_missing=[]
for roman,title,p in manifestos:
    if p.name in rel_text: relation_covered.append(roman)
    else: relation_missing.append((roman,title,p))

# Neoaxiom section / synthesis-link audit.
nax_text=NEOAX.read_text(encoding='utf-8',errors='replace')
sections=[]
pat=re.compile(r'^## (NAX-\d{2}) · ([^\n]+)\n(.*?)(?=^## NAX-\d{2} ·|^## \d+\.|^# EN ·|\Z)',re.M|re.S)
for ident,title,body in pat.findall(nax_text):
    issues=sorted(set(re.findall(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',body)))
    sections.append({'id':ident,'title':title.strip(),'issues':issues})
nax_missing=[x for x in sections if not x['issues']]

# Direct documentary graph per manifesto, grouped by repository domain.
def group_refs(paths):
    g=defaultdict(list)
    for p in sorted(paths,key=lambda x:x.as_posix().lower()):
        try:r=p.relative_to(ROOT)
        except ValueError:continue
        if p in manifest_set: key='manifiestos'
        elif r.parts[:2]==('analisis','publicos'): key='analisis/publicos'
        elif r.parts[:2]==('auditorias','publicas'): key='auditorias/publicas'
        elif r.parts[:2]==('propuestas','sintesis-abierta'): key='sintesis-abierta'
        elif r.parts and r.parts[0]=='obras': key='obras'
        elif r.parts and r.parts[0]=='proyeccion': key='proyeccion'
        elif r.parts and r.parts[0]=='neoaxiomas': key='neoaxiomas'
        else: key='otros'
        g[key].append(r.as_posix())
    return dict(g)

graph=[]
for roman,title,p in manifestos:
    graph.append({
        'roman':roman,'title':title,'path':p.relative_to(ROOT).as_posix(),
        'outbound':group_refs(outbound[p]),
        'inbound':group_refs(inbound[p]),
    })

# Menu/entry-point audit.
entrypoints=[ROOT/'README.md',MANIFEST_INDEX,ROOT/'propuestas/sintesis-abierta/README.md',NEOAX,REL_MAP]
menu=[]
for p in entrypoints:
    if not p.exists():
        menu.append({'path':p.relative_to(ROOT).as_posix(),'missing_file':True}); continue
    t=p.read_text(encoding='utf-8',errors='replace')
    menu.append({
        'path':p.relative_to(ROOT).as_posix(),
        'neoaxiomas': 'neoaxiomas/README.md' in t or p==NEOAX,
        'sintesis': 'propuestas/sintesis-abierta/README.md' in t or p.name=='README.md' and p.parent.name=='sintesis-abierta',
        'relations': 'RELACIONES_TRABAJO_APLICADO_ES_EN.md' in t or p==REL_MAP,
        'manifestos': 'manifiestos/README.md' in t or p==MANIFEST_INDEX,
    })

# Write full non-reductive audit. No source document is shortened or rewritten.
lines=[]
lines += ['# Auditoría relacional MAXPROC · Manifiestos ↔ Neoaxiomas ↔ publicaciones ↔ Síntesis Abierta',
          '## MAXPROC relational audit · Manifestos ↔ Neoaxioms ↔ publications ↔ Open Synthesis','',
          '**Fecha / Date:** 2026-08-09  ',
          f'**Manifiestos canónicos detectados / Canonical manifestos detected:** {len(manifestos)} · I–{manifestos[-1][0]}  ',
          f'**Archivos Markdown examinados / Markdown files scanned:** {len(MD)}  ',
          '**Regla de integridad:** esta auditoría no resume, acorta ni reescribe cuerpos de manifiestos. Las métricas sólo detectan candidatos a recuperación o ampliación desde fuentes, manteniendo íntegro el texto existente. / **Integrity rule:** this audit never summarises, shortens or rewrites manifesto bodies. Metrics only detect candidates for source recovery or expansion while preserving existing text intact.','',
          '---','',
          '## 1. Hallazgos estructurales / Structural findings','',
          f'- Cobertura del mapa curado / Curated-map coverage: **{len(relation_covered)}/{len(manifestos)}**.',
          f'- Manifiestos ausentes del mapa curado / Manifestos missing from curated map: **{", ".join(x[0] for x in relation_missing) if relation_missing else "ninguno / none"}**.',
          f'- Neoaxiomas sin enlace de síntesis en su propia sección / Neoaxioms without a synthesis link in their own section: **{", ".join(x["id"] for x in nax_missing) if nax_missing else "ninguno / none"}**.',
          f'- Enlaces Markdown locales rotos detectados / Broken local Markdown links detected: **{len(broken)}**.',
          f'- Manifiestos candidatos a revisión de densidad textual, sin modificación automática / Manifestos flagged for textual-density review, with no automatic modification: **{len(short)}**.','',
          '---','',
          '## 2. Candidatos a recuperación o ampliación íntegra / Candidates for full source recovery or expansion','',
          '| Nº | Archivo | Palabras aprox. | Encabezados | Párrafos sustantivos | Palabras/encabezado |','|---:|---|---:|---:|---:|---:|']
for m in short:
    lines.append(f'| {m["roman"]} | `{m["path"]}` | {m["words"]} | {m["headings"]} | {m["paragraphs"]} | {m["words_per_heading"]} |')
lines += ['','> La inclusión en esta tabla **no significa que el manifiesto sea conceptualmente insuficiente**. Significa únicamente que su densidad documental es baja frente al resto del corpus y debe compararse con hilos, fuentes, publicaciones y versiones anteriores antes de cualquier ampliación. / Inclusion here does **not** mean conceptual insufficiency; it only marks low documentary density and requires comparison with sources before expansion.','',
          '---','',
          '## 3. Cobertura de relaciones por manifiesto / Per-manifesto relation coverage','']
for node in graph:
    lines += [f'### {node["roman"]} · {node["title"]}',f'`{node["path"]}`','']
    out=node['outbound']; inn=node['inbound']
    if out:
        lines.append('**Salientes directas / Direct outbound:**')
        for k,vals in out.items():
            lines.append(f'- **{k}:** ' + ' · '.join(f'`{v}`' for v in vals))
    else: lines.append('**Salientes directas / Direct outbound:** ninguna / none.')
    if inn:
        lines.append('**Entrantes directas / Direct inbound:**')
        for k,vals in inn.items():
            lines.append(f'- **{k}:** ' + ' · '.join(f'`{v}`' for v in vals))
    else: lines.append('**Entrantes directas / Direct inbound:** ninguna / none.')
    lines.append('')

lines += ['---','','## 4. Neoaxiomas y sus síntesis / Neoaxioms and their syntheses','',
          '| Neoaxioma | Título | Issues enlazados en la sección |','|---|---|---|']
for x in sections:
    val=' · '.join('#'+i for i in x['issues']) if x['issues'] else '**FALTA / MISSING**'
    lines.append(f'| {x["id"]} | {x["title"]} | {val} |')

lines += ['','---','','## 5. Menús y puertas de navegación / Menus and navigation doors','',
          '| Superficie | Neoaxiomas | Síntesis | Relaciones | Manifiestos |','|---|:---:|:---:|:---:|:---:|']
for m in menu:
    if m.get('missing_file'):
        lines.append(f'| `{m["path"]}` | — | — | — | — |'); continue
    yn=lambda v:'✓' if v else '✗'
    lines.append(f'| `{m["path"]}` | {yn(m["neoaxiomas"])} | {yn(m["sintesis"])} | {yn(m["relations"])} | {yn(m["manifestos"])} |')

lines += ['','---','','## 6. Enlaces locales rotos / Broken local links','']
if broken:
    for f,t,href in broken:
        lines.append(f'- `{f.relative_to(ROOT).as_posix()}` → `{href}`')
else:
    lines.append('- Ninguno detectado / None detected.')

lines += ['','---','','## 7. Regla permanente de mantenimiento / Permanent maintenance rule','',
          '1. Ninguna automatización puede sustituir un manifiesto por un resumen ni reducir deliberadamente su cuerpo fuente. / No automation may replace a manifesto with a summary or deliberately reduce its source body.',
          '2. Toda nueva publicación debe declarar o descubrir relaciones con manifiestos, Neoaxiomas, auditorías y Síntesis Abierta cuando existan. / Every new publication should declare or discover relations to manifestos, Neoaxioms, audits and Open Synthesis when they exist.',
          '3. Toda nueva pieza canónica debe exponer menú de retorno al índice correspondiente y, cuando proceda, a su Síntesis Abierta. / Every new canonical piece must expose return navigation to its index and, where applicable, its Open Synthesis.',
          '4. Las relaciones automáticas basadas en enlaces se consideran **documentales**; las relaciones semánticas o causales requieren revisión humana/SAN. / Link-based automatic relations are **documentary**; semantic or causal relations require human/SAN review.',
          '5. Las futuras imágenes de manifiestos y Neoaxiomas deben añadirse como capa ilustrativa sin sustituir texto ni genealogía. / Future manifesto and Neoaxiom images must be added as an illustrative layer without replacing text or genealogy.','']

REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
JSON_OUT.write_text(json.dumps({'metrics':metrics,'short':short,'relation_missing':[x[0] for x in relation_missing],'neoaxioms':sections,'broken':[{'source':f.relative_to(ROOT).as_posix(),'href':h} for f,_,h in broken],'graph':graph,'menu':menu},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

print('MANIFESTOS',len(manifestos),'MARKDOWN',len(MD),'SHORT',len(short),'RELATION_MISSING',len(relation_missing),'NAX_MISSING_SYNTH',len(nax_missing),'BROKEN',len(broken))
print('REPORT',REPORT.relative_to(ROOT))
