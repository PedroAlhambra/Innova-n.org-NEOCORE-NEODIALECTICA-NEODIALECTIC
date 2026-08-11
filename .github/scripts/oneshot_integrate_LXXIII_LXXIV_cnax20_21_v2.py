from pathlib import Path
import json,re
ROOT=Path('.')
REPO='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'

# 1 manifesto index
p=ROOT/'manifiestos/README.md'; s=p.read_text(encoding='utf-8')
inf='- **∞** · [Neo0™ · Puerta Abierta del Fractal / Open Door of the Fractal](INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)'
rows=[
'- **LXXIII** · [Maduración Invertida™ · Humanidad Común y Degradación Arquetípica Reversible / Inverted Maturation™ · Common Humanity and Reversible Archetypal Degradation](73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) · [SAN #124]('+REPO+'/issues/124)',
'- **LXXIV** · [Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™ · From the Human Troll to the Bot](74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [SAN #125]('+REPO+'/issues/125)']
for row in rows:
    if row not in s: s=s.replace(inf,row+'\n'+inf,1)
s=s.replace('72 manifiestos finitos bilingües · I–LXXII','74 manifiestos finitos bilingües · I–LXXIV').replace('72 finite bilingual manifestos · I–LXXII','74 finite bilingual manifestos · I–LXXIV')
s=s.replace('[LXXII · El Hombre Custodio™](72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md) · [Issue #122]('+REPO+'/issues/122)','[LXXIV · Asimetría de la Destrucción™](74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [Issue #125]('+REPO+'/issues/125)')
p.write_text(s,encoding='utf-8')

# 2 canonical registry
p=ROOT/'manifiestos/CANONICAL_FILENAMES.json'; d=json.loads(p.read_text(encoding='utf-8')); e=d.setdefault('entries',{})
e['LXXIII']={'legacy':'manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md','canonical':'manifiestos/canonicos/LXXIII_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md'}
e['LXXIV']={'legacy':'manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md','canonical':'manifiestos/canonicos/LXXIV_asimetria_destruccion_trol_humano_bot_ES_EN.md'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# 3 neoaxiom candidates
p=ROOT/'neoaxiomas/README.md'; s=p.read_text(encoding='utf-8')
s=s.replace('I–LXXII / Neoaxiomatic candidates detected in the I–LXXII review','I–LXXIV / Neoaxiomatic candidates detected in the I–LXXIV review').replace('I–LXXII review','I–LXXIV review').replace('repaso I–LXXII','repaso I–LXXIV')
row20='| **C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™** | [LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) | **Candidato explícito · SAN #126**; no canonizado / **Explicit candidate · SAN #126**; not canonicalised |'
row21='| **C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™** | [VI](../manifiestos/09_parasitismo_sistemico_ES_EN.md) + [LXXIII](../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) + [LXXIV](../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md) | **Candidato explícito · SAN #127**; no canonizado / **Explicit candidate · SAN #127**; not canonicalised |'
if 'C-NAX-20 · Humanidad Común' not in s:
    m=re.search(r'^\| \*\*C-NAX-19 .*$',s,re.M)
    if not m: raise SystemExit('missing C-NAX-19 row')
    s=s[:m.end()]+'\n'+row20+'\n'+row21+s[m.end():]
full='''
### C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™

> **ES:** La condición humana común constituye el suelo relacional compartido de toda identidad particular. Ninguna diferencia legítima debe ser borrada, patologizada o forzada a la invisibilidad; ninguna identidad parcial debe coronarse como totalidad de la persona, justificar la deshumanización de otros ni exigir centralidad social permanente como condición de respeto.

> **EN:** Common humanity constitutes the shared relational ground of every particular identity. No legitimate difference should be erased, pathologised or forced into invisibility; no partial identity should be crowned as the totality of the person, justify the dehumanisation of others or demand permanent social centrality as a condition of respect.

**Síntesis / Synthesis:** [#126]('''+REPO+'''/issues/126) · **CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**

### C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™

> **ES:** La capacidad de destruir, someter, extraer o dañar no demuestra superioridad ni comprensión del sistema. Incluso cuando el daño es deliberado, una acción que corona un objetivo parcial y degrada injustificadamente las relaciones o condiciones que sostienen el conjunto opera desde ignorancia sistémica. El Bien Común exige una comprensión capaz de integrar efectos, dependencias, límites, reparación y continuidad.

> **EN:** The capacity to destroy, dominate, extract or harm does not demonstrate superiority or understanding of the system. Even when harm is deliberate, an action that crowns a partial objective and unjustifiably degrades the relations or conditions sustaining the whole operates from systemic ignorance. The Common Good requires understanding capable of integrating effects, dependencies, limits, repair and continuity.

```text
INTELIGENCIA LOCAL ≠ SABIDURÍA SISTÉMICA / LOCAL INTELLIGENCE ≠ SYSTEMIC WISDOM
DESTRUIR ≠ SUPERIORIDAD / DESTROYING ≠ SUPERIORITY
CONSTRUIR ≠ BIEN AUTOMÁTICO / BUILDING ≠ AUTOMATIC GOOD
```

**Síntesis / Synthesis:** [#127]('''+REPO+'''/issues/127) · **CANDIDATO ≠ CANON / CANDIDATE ≠ CANON.**

'''
if '### C-NAX-20 · Humanidad Común' not in s:
    marker='**Regla 7.2 / 7.2 rule:**'
    if marker not in s: raise SystemExit('missing candidate section marker')
    s=s.replace(marker,full+marker,1)
p.write_text(s,encoding='utf-8')

# 4 complete SAN index
p=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'; s=p.read_text(encoding='utf-8')
s=re.sub(r'\*\*Cobertura / Coverage:\*\*.*?\n','**Cobertura / Coverage:** **74 manifiestos finitos I–LXXIV + Manifiesto ∞ · 14 Neoaxiomas™ canónicos + 7 candidatos C-NAX-15–C-NAX-21 · síntesis transversales, auditorías y proyectos de sistema / 74 finite manifestos I–LXXIV + Manifesto ∞ · 14 canonical Neoaxioms™ + 7 candidates C-NAX-15–C-NAX-21 · cross-cutting syntheses, audits and system projects**.\n',s,count=1)
infrow='| ∞ | [Neo0™ · Puerta Abierta del Fractal](../../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md) | [#106]('+REPO+'/issues/106) |'
for row in [
'| LXXIII | [Maduración Invertida™ · Humanidad Común y Degradación Arquetípica Reversible](../../manifiestos/73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md) | [#124]('+REPO+'/issues/124) |',
'| LXXIV | [Asimetría de la Destrucción™ · Del Trol Humano al Bot](../../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md) | [#125]('+REPO+'/issues/125) |']:
    if row not in s: s=s.replace(infrow,row+'\n'+infrow,1)
if 'C-NAX-20 · Humanidad Común' not in s:
    m=re.search(r'^\| \*\*C-NAX-19 .*$',s,re.M)
    if not m: raise SystemExit('missing C-NAX-19 SAN row')
    add='\n| **C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™ / Common Humanity without Suppression of Difference™ · candidato / candidate** | [#126]('+REPO+'/issues/126) · [LXXIII #124]('+REPO+'/issues/124) |\n| **C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™ / Systemic Ignorance of Evil and Non-Superiority of Destruction™ · candidato / candidate** | [#127]('+REPO+'/issues/127) · [LXXIII #124]('+REPO+'/issues/124) · [LXXIV #125]('+REPO+'/issues/125) |'
    s=s[:m.end()]+add+s[m.end():]
s=s.replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21').replace('5 candidatos','7 candidatos').replace('5 candidates','7 candidates').replace('Every finite manifesto I–LXV has a dedicated Open Synthesis issue.','Every finite manifesto I–LXXIV has a dedicated Open Synthesis issue.')
p.write_text(s,encoding='utf-8')

# 5 relational map
p=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'; s=p.read_text(encoding='utf-8')
if '## LXXIII–LXXIV · Humanidad Común™' not in s:
    s+='''\n\n---\n\n## LXXIII–LXXIV · Humanidad Común™, Maduración Invertida™, Trol™ y Bot / Common Humanity™, Inverted Maturation™, Troll™ and Bot\n\n**ES:** esta constelación une VI · Parasitismo Sistémico™, VII · Economía del Aporte™, XXXI · Neuromarketing Antihumanista™, XXXV · Economía del Conflicto™, LV · Micromáquinas™, LXVIII · Soberanía Intelectual y LXIX–LXXII. Faunismo™, Orquismo™, Trolismo™ y Parasitismo™ se tratan como funciones, no identidades. Se incorporan Maduración Invertida™, Microagencia Digital Distribuida™, C-NAX-20 y C-NAX-21.\n\n**EN:** this constellation links VI · Systemic Parasitism™, VII · Contribution Economy™, XXXI · Anti-Humanist Neuromarketing™, XXXV · Conflict Economy™, LV · Micromachines™, LXVIII · Intellectual Sovereignty and LXIX–LXXII. Faunism™, Orcism™, Trollism™ and Parasitism™ are treated as functions, not identities. Inverted Maturation™, Distributed Digital Micro-Agency™, C-NAX-20 and C-NAX-21 are incorporated.\n\n[Delta / Delta](../propuestas/sintesis-abierta/2026-08-11_DELTA_HUMANIDAD_COMUN_MADURACION_INVERTIDA_TROL_BOT_MAL_SISTEMICO_ES_EN.md) · [#124]('''+REPO+'''/issues/124) · [#125]('''+REPO+'''/issues/125) · [#126]('''+REPO+'''/issues/126) · [#127]('''+REPO+'''/issues/127)\n'''
p.write_text(s,encoding='utf-8')

# 6 web4 reader
p=ROOT/'web4/manifiestos/index.html'; s=p.read_text(encoding='utf-8').replace('I–LXXII + ∞','I–LXXIV + ∞')
needle="['LXXII','El Hombre Custodio™','72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md'],['∞'"
replacement="['LXXII','El Hombre Custodio™','72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md'],['LXXIII','Maduración Invertida™ · Humanidad Común','73_maduracion_invertida_humanidad_comun_degradacion_arquetipica_ES_EN.md'],['LXXIV','Asimetría de la Destrucción™ · Trol Humano y Bot','74_asimetria_destruccion_trol_humano_bot_ES_EN.md'],['∞'"
if needle in s: s=s.replace(needle,replacement,1)
p.write_text(s,encoding='utf-8')

# 7 candidate wording across every README/LEEME; latest/count is handled by existing sync workflow after this commit.
for p in sorted(set(ROOT.rglob('README.md'))|set(ROOT.rglob('README_*.md'))|{ROOT/'LEEME.md'}):
    if not p.exists() or '.git' in p.parts: continue
    s=p.read_text(encoding='utf-8').replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21').replace('C-NAX-15–19','C-NAX-15–21')
    p.write_text(s,encoding='utf-8')
print('INTEGRATION_V2=READY')
