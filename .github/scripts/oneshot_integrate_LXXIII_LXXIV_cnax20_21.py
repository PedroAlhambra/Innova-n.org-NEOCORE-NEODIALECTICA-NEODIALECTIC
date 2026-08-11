from pathlib import Path
import json, re, subprocess, sys

ROOT=Path('.').resolve()
REPO='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'

mread=ROOT/'manifiestos/README.md'
text=mread.read_text(encoding='utf-8')
row73='- **LXXIII** · [Maduración Invertida™ · Humanidad Común y Degradación Arquetípica Reversible / Inverted Maturation™](73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) · [SAN #124]('+REPO+'/issues/124)'
row74='- **LXXIV** · [Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™](74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [SAN #125]('+REPO+'/issues/125)'
inf='- **∞** · [Neo0™ · Puerta Abierta del Fractal / Open Door of the Fractal](INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)'
for row in (row73,row74):
    if row not in text:
        text=text.replace(inf,row+'\n'+inf,1)
text=text.replace('I–LXXII + Manifiesto ∞','I–LXXIV + Manifiesto ∞').replace('I–LXXII + Manifesto ∞','I–LXXIV + Manifesto ∞')
text=text.replace('72 manifiestos finitos bilingües','74 manifiestos finitos bilingües').replace('72 finite bilingual manifestos','74 finite bilingual manifestos')
mread.write_text(text,encoding='utf-8')

# Canonical filename registry.
regp=ROOT/'manifiestos/CANONICAL_FILENAMES.json'
reg=json.loads(regp.read_text(encoding='utf-8'))
entries=reg.setdefault('entries',{})
entries['LXXIII']={'legacy':'manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md','canonical':'manifiestos/canonicos/LXXIII_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md'}
entries['LXXIV']={'legacy':'manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md','canonical':'manifiestos/canonicos/LXXIV_asimetria_destruccion_trol_humano_bot_ES_EN.md'}
regp.write_text(json.dumps(reg,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Neoaxiom candidate layer.
np=ROOT/'neoaxiomas/README.md'
n=np.read_text(encoding='utf-8')
n=n.replace('I–LXXII / Neoaxiomatic candidates detected in the I–LXXII review','I–LXXIV / Neoaxiomatic candidates detected in the I–LXXIV review')
n=n.replace('I–LXXII / Neoaxiomatic candidates','I–LXXIV / Neoaxiomatic candidates')
n=n.replace('I–LXXII review','I–LXXIV review')
row20='| **C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™** | [LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) | **Candidato explícito · SAN #126**; no canonizado / **Explicit candidate · SAN #126**; not canonicalised |'
row21='| **C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™** | [VI](../manifiestos/09_parasitismo_sistemico_ES_EN.md) + [LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) + [LXXIV](../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md) | **Candidato explícito · SAN #127**; no canonizado / **Explicit candidate · SAN #127**; not canonicalised |'
if 'C-NAX-20 · Humanidad Común' not in n:
    anchor='| **C-NAX-19 · Inviolabilidad Relacional y Separación de Planos™ / Relational Inviolability and Separation of Planes™**'
    lines=n.splitlines(); out=[]; inserted=False
    for line in lines:
        out.append(line)
        if line.startswith(anchor):
            out.extend([row20,row21]); inserted=True
    if not inserted: raise SystemExit('Cannot insert C-NAX-20/21 rows')
    n='\n'.join(out)+'\n'
sections='''\n### C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™\n\n**ES · formulación candidata:**\n\n> **La condición humana común constituye el suelo relacional compartido de toda identidad particular. Ninguna diferencia legítima debe ser borrada, patologizada o forzada a la invisibilidad; ninguna identidad parcial debe coronarse como totalidad de la persona, justificar la deshumanización de otros ni exigir centralidad social permanente como condición de respeto.**\n\n```text\nHUMANIDAD COMÚN\n+ DIFERENCIA LEGÍTIMA\n+ DIGNIDAD IGUAL\n+ LIBERTAD DE EXPRESIÓN\n+ NO INVISIBILIZACIÓN FORZADA\n+ NO CENTRALIDAD FORZADA\n+ RESPONSABILIDAD RELACIONAL\n= PLURALIDAD HUMANA INTEGRADA™\n```\n\n**EN · candidate formulation:**\n\n> **Common humanity constitutes the shared relational ground of every particular identity. No legitimate difference should be erased, pathologised or forced into invisibility; no partial identity should be crowned as the totality of the person, justify the dehumanisation of others or demand permanent social centrality as a condition of respect.**\n\n```text\nCOMMON HUMANITY\n+ LEGITIMATE DIFFERENCE\n+ EQUAL DIGNITY\n+ FREEDOM OF EXPRESSION\n+ NO FORCED INVISIBILITY\n+ NO FORCED CENTRALITY\n+ RELATIONAL RESPONSIBILITY\n= INTEGRATED HUMAN PLURALITY™\n```\n\n**Síntesis específica / Dedicated synthesis:** [#126]('''+REPO+'''/issues/126). **CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**\n\n### C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™\n\n**ES · formulación candidata:**\n\n> **La capacidad de destruir, someter, extraer o dañar no demuestra superioridad ni comprensión del sistema. Incluso cuando el daño es deliberado, una acción que corona un objetivo parcial y degrada injustificadamente las relaciones o condiciones que sostienen el conjunto opera desde ignorancia sistémica. El Bien Común exige una comprensión capaz de integrar efectos, dependencias, límites, reparación y continuidad.**\n\n```text\nINTELIGENCIA LOCAL ≠ SABIDURÍA SISTÉMICA\nDESTRUIR ≠ SUPERIORIDAD\nCONSTRUIR ≠ BIEN AUTOMÁTICO\n```\n\n**EN · candidate formulation:**\n\n> **The capacity to destroy, dominate, extract or harm does not demonstrate superiority or understanding of the system. Even when harm is deliberate, an action that crowns a partial objective and unjustifiably degrades the relations or conditions sustaining the whole operates from systemic ignorance. The Common Good requires understanding capable of integrating effects, dependencies, limits, repair and continuity.**\n\n```text\nLOCAL INTELLIGENCE ≠ SYSTEMIC WISDOM\nDESTROYING ≠ SUPERIORITY\nBUILDING ≠ AUTOMATIC GOOD\n```\n\n**Síntesis específica / Dedicated synthesis:** [#127]('''+REPO+'''/issues/127). **CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**\n\n'''
if '### C-NAX-20 · Humanidad Común' not in n:
    marker='**Regla 7.2 / 7.2 rule:**'
    if marker not in n: raise SystemExit('Cannot locate candidate insertion marker')
    n=n.replace(marker,sections+marker,1)
np.write_text(n,encoding='utf-8')

# Complete Open Synthesis index.
ip=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
s=ip.read_text(encoding='utf-8')
s=re.sub(r'\*\*Cobertura / Coverage:\*\*.*?\n', '**Cobertura / Coverage:** **74 manifiestos finitos I–LXXIV + Manifiesto ∞ · 14 Neoaxiomas™ canónicos + 7 candidatos C-NAX-15–C-NAX-21 · síntesis transversales, auditorías y proyectos de sistema / 74 finite manifestos I–LXXIV + Manifesto ∞ · 14 canonical Neoaxioms™ + 7 candidates C-NAX-15–C-NAX-21 · cross-cutting syntheses, audits and system projects**.\n', s, count=1)
idx73='| LXXIII | [Maduración Invertida™ · Humanidad Común y Degradación Arquetípica Reversible](../../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) | [#124]('+REPO+'/issues/124) |'
idx74='| LXXIV | [Asimetría de la Destrucción™ · Del Trol Humano al Bot](../../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md) | [#125]('+REPO+'/issues/125) |'
infrow='| ∞ | [Neo0™ · Puerta Abierta del Fractal](../../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md) | [#106]('+REPO+'/issues/106) |'
for row in (idx73,idx74):
    if row not in s: s=s.replace(infrow,row+'\n'+infrow,1)
c20='| **C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™ · candidato / candidate** | [#126]('+REPO+'/issues/126) · [LXXIII #124]('+REPO+'/issues/124) |'
c21='| **C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™ · candidato / candidate** | [#127]('+REPO+'/issues/127) · [LXXIII #124]('+REPO+'/issues/124) · [LXXIV #125]('+REPO+'/issues/125) |'
if 'C-NAX-20 · Humanidad Común' not in s:
    anchor=re.search(r'^\| \*\*C-NAX-19 .*$',s,re.M)
    if not anchor: raise SystemExit('Cannot locate C-NAX-19 index row')
    pos=anchor.end(); s=s[:pos]+'\n'+c20+'\n'+c21+s[pos:]
s=s.replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21').replace('5 candidatos','7 candidatos').replace('5 candidates','7 candidates')
s=s.replace('Every finite manifesto I–LXV has a dedicated Open Synthesis issue.','Every finite manifesto I–LXXIV has a dedicated Open Synthesis issue.')
ip.write_text(s,encoding='utf-8')

# Applied relational map: append a complete bilingual living delta.
rp=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
r=rp.read_text(encoding='utf-8')
if 'LXXIII–LXXIV · Humanidad Común' not in r:
    r += '''\n\n---\n\n## LXXIII–LXXIV · Humanidad Común™, Maduración Invertida™, Trol™ y Bot / Common Humanity™, Inverted Maturation™, Troll™ and Bot\n\n**ES:** la nueva constelación enlaza VI · Parasitismo Sistémico™, VII · Economía del Aporte™, XXXI · Neuromarketing Antihumanista™, XXXV · Economía del Conflicto™, LV · Micromáquinas™, LXVIII · Soberanía Intelectual de la Especie™ y LXIX–LXXII. Distingue Faunismo™, Orquismo™, Trolismo™ y Parasitismo™ como funciones, no identidades; introduce Maduración Invertida™, Microagencia Digital Distribuida™ y dos candidatos: C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ y C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™.\n\n**EN:** the new constellation links VI · Systemic Parasitism™, VII · Contribution Economy™, XXXI · Anti-Humanist Neuromarketing™, XXXV · Conflict Economy™, LV · Micromachines™, LXVIII · Intellectual Sovereignty of the Species™ and LXIX–LXXII. It distinguishes Faunism™, Orcism™, Trollism™ and Parasitism™ as functions rather than identities; introduces Inverted Maturation™, Distributed Digital Micro-Agency™ and two candidates: C-NAX-20 · Common Humanity without Suppression of Difference™ and C-NAX-21 · Systemic Ignorance of Evil and Non-Superiority of Destruction™.\n\n[Delta íntegro / Full delta](../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md) · [LXXIII #124]('''+REPO+'''/issues/124) · [LXXIV #125]('''+REPO+'''/issues/125) · [C-NAX-20 #126]('''+REPO+'''/issues/126) · [C-NAX-21 #127]('''+REPO+'''/issues/127)\n'''
rp.write_text(r,encoding='utf-8')

# WEB4 manifesto reader: keep static fallback registry in sync.
wp=ROOT/'web4/manifiestos/index.html'
w=wp.read_text(encoding='utf-8')
w=w.replace('I–LXXII + ∞','I–LXXIV + ∞')
needle="['LXXII','El Hombre Custodio™','72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md'],['∞'"
repl="['LXXII','El Hombre Custodio™','72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md'],['LXXIII','Maduración Invertida™ · Humanidad Común','73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md'],['LXXIV','Asimetría de la Destrucción™ · Trol Humano y Bot','74_asimetria_destruccion_trol_humano_bot_ES_EN.md'],['∞'"
if needle in w: w=w.replace(needle,repl,1)
wp.write_text(w,encoding='utf-8')

# Current README surfaces: update candidate frontier; the canonical sync below updates latest manifesto/count blocks.
for p in sorted(set(ROOT.rglob('README.md'))|set(ROOT.rglob('README_*.md'))|{ROOT/'LEEME.md'}):
    if not p.exists() or '.git' in p.parts: continue
    t=p.read_text(encoding='utf-8')
    t=t.replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21').replace('C-NAX-15–19','C-NAX-15–21')
    t=t.replace('5 candidatos C-NAX-15–C-NAX-19','7 candidatos C-NAX-15–C-NAX-21').replace('5 candidates C-NAX-15–C-NAX-19','7 candidates C-NAX-15–C-NAX-21')
    p.write_text(t,encoding='utf-8')

# Run canonical synchronizers in safe order.
def run(script):
    p=subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,text=True,capture_output=True)
    print(p.stdout)
    if p.returncode:
        print(p.stderr,file=sys.stderr); raise SystemExit(f'FAILED {script}: {p.returncode}')

for script in [
    '.github/scripts/sync_open_synthesis_manifestos.py',
    '.github/scripts/normalize_manifesto_indices.py',
    '.github/scripts/sync_root_navigation.py',
    '.github/scripts/sync_canonical_manifestos.py',
    '.github/scripts/sync_manifesto_crossrefs.py',
    '.github/scripts/audit_markdown_links_readmes.py',
]:
    if (ROOT/script).exists(): run(script)

# Update WEB4 README after synchronization if present.
wr=ROOT/'web4/README.md'
if wr.exists():
    t=wr.read_text(encoding='utf-8')
    t=t.replace('I–LXXII','I–LXXIV').replace('72 manifiestos','74 manifiestos').replace('72 manifestos','74 manifestos').replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21')
    if 'Maduración Invertida™' not in t:
        t += '\n\n## Delta 2026-08-11 · LXXIII–LXXIV / 2026-08-11 delta · LXXIII–LXXIV\n\nWEB4™ incorpora como nueva frontera documental **Maduración Invertida™, Humanidad Común, Faunismo™, Orquismo™, Trolismo™, Microagencia Digital Distribuida™ y Asimetría de la Destrucción™**, con C-NAX-20 y C-NAX-21 como candidatos abiertos a SAN™. / WEB4™ incorporates as its new documentary frontier **Inverted Maturation™, Common Humanity, Faunism™, Orcism™, Trollism™, Distributed Digital Micro-Agency™ and Asymmetry of Destruction™**, with C-NAX-20 and C-NAX-21 as candidates open to SAN™.\n'
    wr.write_text(t,encoding='utf-8')

# Postcheck specific to this integration.
checks={}
def C(name,cond): checks[name]=bool(cond)
C('manifesto_73', (ROOT/'manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md').exists())
C('manifesto_74', (ROOT/'manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md').exists())
C('delta', (ROOT/'propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md').exists())
mr=mread.read_text(encoding='utf-8')
C('index_LXXIV', 'LXXIV' in mr and '#125' in mr)
C('infinity_after_LXXIV', mr.find('LXXIV') < mr.rfind('**∞**'))
n=np.read_text(encoding='utf-8')
C('cnax20', 'C-NAX-20' in n and 'issues/126' in n)
C('cnax21', 'C-NAX-21' in n and 'issues/127' in n)
idx=ip.read_text(encoding='utf-8')
C('synthesis_index', 'LXXIV' in idx and 'C-NAX-21' in idx and '#127' in idx)
web=wp.read_text(encoding='utf-8')
C('web4_reader', 'LXXIII' in web and 'LXXIV' in web)
linkreport=ROOT/'auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN.md'
C('links_ok', linkreport.exists() and '**Estado / Status:** **OK**' in linkreport.read_text(encoding='utf-8'))
status='OK' if all(checks.values()) else 'REQUIERE CORRECCIÓN / NEEDS CORRECTION'
report=ROOT/'auditorias/publicas/2026-08-11_postcheck_LXXIII_LXXIV_C_NAX_20_21_ES_EN.md'
lines=['# Postcheck · LXXIII–LXXIV · C-NAX-20–C-NAX-21','# Postcheck · LXXIII–LXXIV · C-NAX-20–C-NAX-21','',f'**Estado / Status:** **{status}**','', '## ES · Resultado','']
for k,v in checks.items(): lines.append(f'- {k}: **{"OK" if v else "FAIL"}**')
lines += ['','**Frontera viva:** 74 manifiestos finitos · I–LXXIV + ∞ · NAX-01–NAX-14 canónicos · C-NAX-15–C-NAX-21 candidatos.','', '## EN · Result','']
for k,v in checks.items(): lines.append(f'- {k}: **{"OK" if v else "FAIL"}**')
lines += ['','**Living frontier:** 74 finite manifestos · I–LXXIV + ∞ · NAX-01–NAX-14 canonical · C-NAX-15–C-NAX-21 candidates.','']
report.write_text('\n'.join(lines),encoding='utf-8')
if status!='OK': raise SystemExit(status)
print('INTEGRATION_POSTCHECK=OK')
