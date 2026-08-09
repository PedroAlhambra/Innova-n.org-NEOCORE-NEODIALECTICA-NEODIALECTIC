from pathlib import Path
import json,re,sys

ROOT=Path('.').resolve()
VERSION='7.1'
MIDX=ROOT/'manifiestos/README.md'
NEO=ROOT/'neoaxiomas/README.md'
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
RELJSON=ROOT/'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones.json'
PARJSON=ROOT/'auditorias/publicas/2026-08-09_auditoria_paridad_bilingue_manifiestos_neoaxiomas.json'
HISTJSON=ROOT/'auditorias/publicas/2026-08-09_auditoria_regresiones_historicas_manifiestos.json'
OUT=ROOT/'auditorias/publicas/2026-08-09_postcheck_neocore_7_1_integridad_relacional_no_reductiva_ES_EN.md'
JOUT=ROOT/'auditorias/publicas/2026-08-09_postcheck_neocore_7_1_integridad_relacional_no_reductiva.json'
ISSUES={f'NAX-{i:02d}':83+i for i in range(1,15)} # 84..97
FAIL=[]; WARN=[]; OK=[]

def ok(label,cond,detail=''):
    if cond: OK.append((label,detail))
    else: FAIL.append((label,detail))

def read(p):
    try:return p.read_text(encoding='utf-8')
    except Exception as e:FAIL.append((f'lectura {p.relative_to(ROOT)}',str(e)));return ''

# 1. Current public surfaces.
readmes=sorted({p for p in ROOT.rglob('README*.md') if '.git' not in p.parts}|({ROOT/'LEEME.md'} if (ROOT/'LEEME.md').exists() else set()))
stale=[]; missing_version=[]; bad_nax=[]; bad_rel=[]
for p in readmes:
    t=read(p)
    if re.search(r'NEOCore(?:™)?\s+(?:v?7\.0|7\.x)',t):stale.append(p.relative_to(ROOT).as_posix())
    if f'NEOCore™ {VERSION}' not in t:missing_version.append(p.relative_to(ROOT).as_posix())
    if t.count('<!-- NEOAXIOMAS_GLOBAL_LINK_START -->')!=1 or t.count('<!-- NEOAXIOMAS_GLOBAL_LINK_END -->')!=1:bad_nax.append(p.relative_to(ROOT).as_posix())
    if t.count('<!-- NEO_RELATIONAL_MENU_START -->')!=1 or t.count('<!-- NEO_RELATIONAL_MENU_END -->')!=1:bad_rel.append(p.relative_to(ROOT).as_posix())
ok('README/LEEME sin versión 7.0/7.x',not stale,', '.join(stale))
ok('README/LEEME declaran NEOCore™ 7.1',not missing_version,', '.join(missing_version))
ok('README/LEEME tienen un bloque Neoaxiomas',not bad_nax,', '.join(bad_nax))
ok('README/LEEME tienen un menú relacional vivo',not bad_rel,', '.join(bad_rel))

# 2. Canonical manifestos.
idx=read(MIDX); mans=[];seen=set()
for roman,title,href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',idx,re.M):
    p=(MIDX.parent/href).resolve()
    if p.exists() and p not in seen:seen.add(p);mans.append((roman,title,p))
ok('Corpus canónico I–LX = 60 manifiestos',len(mans)==60 and mans[0][0]=='I' and mans[-1][0]=='LX',f'{len(mans)} · {mans[0][0] if mans else "?"}–{mans[-1][0] if mans else "?"}')
bad_footer=[];bad_nav=[]
for roman,title,p in mans:
    t=read(p)
    if t.count('<!-- NEO_RELATIONAL_FOOTER_START -->')!=1 or t.count('<!-- NEO_RELATIONAL_FOOTER_END -->')!=1:bad_footer.append(roman)
    if t.count('<!-- NEO_MANIFESTO_NAV_START -->')!=1 or t.count('<!-- NEO_MANIFESTO_NAV_END -->')!=1:bad_nav.append(roman)
ok('60/60 manifiestos tienen pie relacional',not bad_footer,', '.join(bad_footer))
ok('60/60 manifiestos tienen navegación canónica',not bad_nav,', '.join(bad_nav))

# 3. Neoaxioms + dedicated synthesis.
nt=read(NEO)
bad_count=[];bad_issue=[]
for ident,num in ISSUES.items():
    if nt.count('## '+ident+' ·')!=2:bad_count.append(f'{ident}:{nt.count("## "+ident+" ·")}')
    url=f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{num}'
    if nt.count(url)<2 or nt.count('issues/80')<14:bad_issue.append(ident)
ok('NAX-01..14 existen en ES y EN',not bad_count,', '.join(bad_count))
ok('NAX-01..14 enlazan sus Síntesis específicas #84–#97',not bad_issue,', '.join(bad_issue))
m=re.search(r'## 1\. Relación entre los Neoaxiomas vigentes\n\n```text\n(.*?)```',nt,re.S)
ok('Topología NAX no duplica NAX-14',bool(m) and m.group(1).count('NAX-14')==1,str(m.group(1).count('NAX-14') if m else 'árbol no localizado'))
ok('NAX-10 incorpora León y Bandera de Síntesis','León™' in nt and 'Bandera de la Humanidad en Síntesis™' in nt,'')
ok('NAX-12 contiene salvaguarda ISO/regulatoria','requisito ISO' in nt and 'ISO requirement' in nt,'')
ok('Regla no reductiva está fijada en Neoaxiomas','Regla heredada de integridad no reductiva' in nt and 'Inherited non-reductive integrity rule' in nt,'')

# 4. Root access, both languages.
rt=read(ROOT/'README.md')
ok('README raíz ES expone Neoaxiomas y mapa relacional','| **Neoaxiomas™** | [Capa Axiomática Abierta]' in rt and '| **Mapa relacional vivo** |' in rt,'')
ok('README raíz EN expone Neoaxioms y living relational map','| **Neoaxioms™** | [Open Axiomatic Layer]' in rt and '| **Living relational map** |' in rt,'')

# 5. Curated relation map explicit coverage.
relt=read(REL)
ok('Mapa relacional declara I–LX / 60','**Cobertura / Coverage:** I–LX · 60 manifiestos / 60 manifestos' in relt,'')
missing_rel_files=[]
for _,_,p in mans:
    if p.name not in relt:missing_rel_files.append(p.name)
ok('Mapa relacional referencia 60/60 archivos canónicos',not missing_rel_files,', '.join(missing_rel_files))

# 6. Audit ledgers.
def loadj(p):
    try:return json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:FAIL.append((f'JSON {p.relative_to(ROOT)}',str(e)));return {}
rj=loadj(RELJSON); pj=loadj(PARJSON); hj=loadj(HISTJSON)
ok('Auditoría relacional: 0 manifiestos ausentes',rj.get('relation_missing',[])==[],str(rj.get('relation_missing')))
ok('Auditoría relacional: 0 enlaces locales rotos',rj.get('broken',[])==[],str(len(rj.get('broken',[]))))
ok('Auditoría relacional: 0 manifiestos sin publicación entrante',rj.get('weak_publication_relations',[])==[],str(len(rj.get('weak_publication_relations',[]))))
naxs=rj.get('neoaxioms',[])
ok('Auditoría relacional: 14 Neoaxiomas con síntesis específica',len(naxs)==14 and all(x.get('dedicated') for x in naxs),str([(x.get('id'),x.get('dedicated')) for x in naxs if not x.get('dedicated')]))
ok('Auditoría ES/EN: 0 asimetrías fuertes en manifiestos',pj.get('flags',[])==[],str(len(pj.get('flags',[]))))
ok('Auditoría ES/EN: 0 asimetrías fuertes en Neoaxiomas',pj.get('nax_flags',[])==[],str(len(pj.get('nax_flags',[]))))
ok('Auditoría histórica: 0 regresiones fuertes',hj.get('strong_regressions',[])==[],str(len(hj.get('strong_regressions',[]))))

# 7. No temporary/staging mutation machinery from this wave.
temporary=[
'neoaxiomas/NAX-12_14_PROPUESTA_TEMPORAL_ES_EN.md','neoaxiomas/SINTESIS_LINKS_PENDING.md','neoaxiomas/README_SYNTHESIS_PLAN.md','neoaxiomas/.keep']
left=[x for x in temporary if (ROOT/x).exists()]
ok('Sin staging neoaxiomático heredado',not left,', '.join(left))

# 8. Current audit files present.
expected=[RELJSON,PARJSON,HISTJSON,ROOT/'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md',ROOT/'auditorias/publicas/2026-08-09_auditoria_paridad_bilingue_manifiestos_neoaxiomas_ES_EN.md',ROOT/'auditorias/publicas/2026-08-09_auditoria_regresiones_historicas_manifiestos_ES_EN.md']
ok('Informes de auditoría base presentes',all(p.exists() for p in expected),', '.join(p.relative_to(ROOT).as_posix() for p in expected if not p.exists()))

# 9. Density warnings remain warnings, not source mutations.
density=rj.get('density_flags',[])
WARN.append(('Densidad documental a revisar sin reescritura automática',', '.join(x.get('roman','?') for x in density) or 'ninguna'))
WARN.append(('Capa ilustrativa','Pendiente de incorporar las imágenes cuando estén disponibles; deben añadirse con alt/procedencia sin sustituir texto.'))

status='OK' if not FAIL else 'FAIL'
lines=['# Postcheck NEOCore™ 7.1 · integridad relacional y no reductiva','## NEOCore™ 7.1 postcheck · relational and non-reductive integrity','',f'**Fecha / Date:** 2026-08-09  ',f'**Resultado / Result:** **{status}**  ',f'**README/LEEME examinados:** {len(readmes)}  ',f'**Manifiestos canónicos:** {len(mans)}  ',f'**Neoaxiomas:** 14','',
'## Comprobaciones / Checks','']
for label,detail in OK:lines.append(f'- ✅ **{label}**'+(f' — {detail}' if detail else ''))
for label,detail in FAIL:lines.append(f'- ❌ **{label}**'+(f' — {detail}' if detail else ''))
lines+=['','## Advertencias que no bloquean / Non-blocking warnings','']
for label,detail in WARN:lines.append(f'- ⚠️ **{label}:** {detail}')
lines+=['','## Alcance del dictamen','',
'Este postcheck certifica únicamente la coherencia documental y mecánica comprobada por el repositorio: versión, navegación, enlaces gestionados, cobertura relacional explícita, síntesis específicas, paridad cuantitativa ES/EN e historial sin regresiones fuertes. **No afirma que se hayan descubierto todas las relaciones semánticas posibles ni que los textos no puedan crecer mediante nuevas fuentes o Síntesis Abierta.**','',
'This postcheck certifies only the repository-level documentary and mechanical consistency actually checked: version, navigation, managed links, explicit relational coverage, dedicated syntheses, quantitative ES/EN parity and history without strong regressions. **It does not claim that every possible semantic relation has been discovered or that texts cannot grow through new sources or Open Synthesis.**','',
'## Regla de continuidad','',
'La evolución posterior debe ser aditiva y trazable por defecto: **no resumir ni sustituir cuerpos fuente**, ampliar mediante delta cuando aparezca nuevo material, conservar genealogía y tratar imágenes como capa ilustrativa adicional.','']
OUT.write_text('\n'.join(lines),encoding='utf-8')
JOUT.write_text(json.dumps({'status':status,'ok':[{'check':a,'detail':b} for a,b in OK],'fail':[{'check':a,'detail':b} for a,b in FAIL],'warnings':[{'check':a,'detail':b} for a,b in WARN],'readme_targets':len(readmes),'manifestos':len(mans),'neoaxioms':14},ensure_ascii=False,indent=2),encoding='utf-8')
print('STATUS',status,'OK',len(OK),'FAIL',len(FAIL),'WARN',len(WARN))
for x in FAIL:print('FAIL',x[0],x[1])
if FAIL:sys.exit(1)
print('POSTCHECK OK: NEOCore 7.1 documentary relational layer is coherent within checked scope')