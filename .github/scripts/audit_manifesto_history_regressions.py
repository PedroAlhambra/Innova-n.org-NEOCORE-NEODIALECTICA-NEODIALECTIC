from pathlib import Path
import subprocess,re,json,sys

ROOT=Path('.').resolve(); IDX=ROOT/'manifiestos/README.md'
OUT=ROOT/'auditorias/publicas/2026-08-09_auditoria_regresiones_historicas_manifiestos_ES_EN.md'
JOUT=ROOT/'auditorias/publicas/2026-08-09_auditoria_regresiones_historicas_manifiestos.json'
WORD=re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9’'\-]*")
MANAGED=[
('<!-- NEO_LATEST_MANIFESTO_START -->','<!-- NEO_LATEST_MANIFESTO_END -->'),
('<!-- NEOAXIOMAS_GLOBAL_LINK_START -->','<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'),
('<!-- MANIFESTOS_CURRENT_START -->','<!-- MANIFESTOS_CURRENT_END -->'),
('<!-- NEO_ALL_MANIFESTOS_START -->','<!-- NEO_ALL_MANIFESTOS_END -->'),
('<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->','<!-- NEO_OPEN_SYNTHESIS_INVITATION_END -->'),
('<!-- NEO_MANIFESTO_NAV_START -->','<!-- NEO_MANIFESTO_NAV_END -->'),
('<!-- NEO_RELATIONAL_FOOTER_START -->','<!-- NEO_RELATIONAL_FOOTER_END -->')]

def clean(t):
    for a,b in MANAGED:t=re.sub(re.escape(a)+r'.*?'+re.escape(b),'',t,flags=re.S)
    return t

def words(t):return len(WORD.findall(clean(t)))
def sh(*args):return subprocess.run(args,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout

idx=IDX.read_text(encoding='utf-8')
mans=[]
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(IDX.parent/href).resolve()
    if p.exists() and p not in [x[2] for x in mans]:mans.append((roman,title,p))

rows=[]
for roman,title,p in mans:
    rel=p.relative_to(ROOT).as_posix(); cur=p.read_text(encoding='utf-8',errors='replace'); cw=words(cur)
    commits=[x.strip() for x in sh('git','log','--format=%H','--',rel).splitlines() if x.strip()]
    maxw=cw; maxsha='CURRENT'; valid=0
    for sha in commits:
        proc=subprocess.run(['git','show',f'{sha}:{rel}'],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
        if proc.returncode:continue
        valid+=1; w=words(proc.stdout)
        if w>maxw:maxw=w;maxsha=sha
    ratio=round(cw/max(maxw,1),3)
    rows.append({'id':roman,'title':title,'path':rel,'current_words':cw,'historical_max_words':maxw,'ratio':ratio,'max_sha':maxsha,'versions_checked':valid})

# Strong regression only: current source body below 82% of largest historical body.
flags=[r for r in rows if r['historical_max_words']>=500 and r['ratio']<0.82]
lines=['# Auditoría histórica no reductiva de manifiestos','## Non-reductive historical manifesto audit','',
'**Fecha / Date:** 2026-08-09  ',f'**Manifiestos / Manifestos:** {len(rows)}  ',
'**Objeto:** detectar si el cuerpo actual de un manifiesto es materialmente más corto que alguna versión anterior del mismo archivo. Los bloques automáticos de navegación, menús y relaciones se excluyen del recuento. / **Purpose:** detect whether the current manifesto body is materially shorter than an earlier version of the same file. Automated navigation, menu and relation blocks are excluded.','',
'> Una regresión de longitud es una alarma documental, no prueba automática de pérdida semántica. Si aparece, la reparación exige comparar diffs y restaurar contenido faltante sin borrar desarrollos posteriores. / A length regression is a documentary alarm, not automatic proof of semantic loss. Repair requires diff comparison and restoration without deleting later developments.','',
'## Regresiones fuertes detectadas / Strong regressions detected','',
'| Nº | Archivo | Actual | Máximo histórico | Ratio | Commit máximo | Versiones revisadas |','|---:|---|---:|---:|---:|---|---:|']
for r in flags:lines.append(f'| {r["id"]} | `{r["path"]}` | {r["current_words"]} | {r["historical_max_words"]} | {r["ratio"]} | `{r["max_sha"]}` | {r["versions_checked"]} |')
if not flags:lines.append('| — | Ninguna / None | — | — | — | — | — |')
lines+=['','## Inventario completo / Full inventory','',
'| Nº | Actual | Máximo | Ratio | Historial | Archivo |','|---:|---:|---:|---:|---:|---|']
for r in rows:lines.append(f'| {r["id"]} | {r["current_words"]} | {r["historical_max_words"]} | {r["ratio"]} | {r["versions_checked"]} | `{r["path"]}` |')
lines+=['','## Regla permanente / Permanent rule','',
'- Ningún mantenimiento automático puede reducir deliberadamente el cuerpo fuente de un manifiesto. / No automated maintenance may deliberately reduce a manifesto source body.',
'- Antes de aceptar una reducción sustantiva, debe existir delta explícito que justifique la eliminación; por defecto se conserva y amplía. / Before accepting substantive reduction, an explicit delta must justify deletion; preservation and expansion are the default.',
'- Las versiones históricas sirven como red de seguridad de memoria y genealogía. / Historical versions act as a memory and genealogy safety net.','']
OUT.write_text('\n'.join(lines),encoding='utf-8')
JOUT.write_text(json.dumps({'manifestos':rows,'strong_regressions':flags},ensure_ascii=False,indent=2),encoding='utf-8')
print('MANIFESTOS',len(rows),'STRONG_REGRESSIONS',len(flags))
for r in flags:print('FLAG',r['id'],r['ratio'],r['max_sha'],r['path'])
print('POSTCHECK OK: read-only source audit')
