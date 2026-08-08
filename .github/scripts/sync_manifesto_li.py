from pathlib import Path
import os,re,sys

ROOT=Path('.')
MAN=ROOT/'manifiestos'
IDX=MAN/'README.md'
LI=MAN/'51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md'
if not LI.exists():
    raise SystemExit('LI manifesto missing')

idx=IDX.read_text(encoding='utf-8')
idx=idx.replace('50 manifiestos bilingües · I–L · 17 oleadas','51 manifiestos bilingües · I–LI · 18 oleadas')
idx=idx.replace('50 bilingual manifestos · I–L · 17 waves','51 bilingual manifestos · I–LI · 18 waves')
idx=idx.replace('I–L · 50 manifiestos bilingües / 50 bilingual manifestos','I–LI · 51 manifiestos bilingües / 51 bilingual manifestos')
idx=idx.replace('I–L · 50 manifiestos / 50 manifestos','I–LI · 51 manifiestos / 51 manifestos')
idx=idx.replace('## Arquitectura actual · 17 oleadas','## Arquitectura actual · 18 oleadas')
idx=idx.replace('## Current architecture · 17 waves','## Current architecture · 18 waves')

li_es='18. **LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™:** accesibilidad institucional, inteligencia cívica distribuida, formación pública no capturante y revisión democrática de funciones públicas.\n'
li_en='18. **LI · Open Synthesis as Complementary or Substitutive Civic Power™:** institutional accessibility, distributed civic intelligence, non-capturing public formation and democratic review of public functions.\n'
if li_es not in idx:
    marker='17. **L · Inteligencia Compartida, no Única™:** invitación abierta a las IAs para comprender, enseñar, criticar y participar en la Síntesis Abierta mediante interoperabilidad cognitiva y responsabilidad humana.\n'
    if marker not in idx: raise SystemExit('ES architecture marker missing')
    idx=idx.replace(marker,marker+li_es,1)
if li_en not in idx:
    marker='17. **L · Shared, Not Singular Intelligence™:** cognitive interoperability, plurality of models, anti-dogmatic training and AI participation in Open Synthesis.\n'
    if marker not in idx: raise SystemExit('EN architecture marker missing')
    idx=idx.replace(marker,marker+li_en,1)

es_row='| LI | [Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™](./51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md) | Accesibilidad institucional, inteligencia cívica distribuida, formación pública no capturante y revisión democrática de instituciones | [#59](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59) |'
en_row='| LI | [Open Synthesis as Complementary or Substitutive Civic Power™](./51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md) | Institutional accessibility, distributed civic intelligence, non-capturing public formation and democratic institutional review | [#59](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59) |'
if es_row not in idx:
    marker='## Relación entre principios y trabajo aplicado'
    block='''## Decimoctava oleada · Poder cívico e instituciones · LI\n\n| Nº | Manifiesto | Función | Síntesis Abierta |\n|---:|---|---|---|\n'''+es_row+'\n\n'
    if marker not in idx: raise SystemExit('ES insertion marker missing')
    idx=idx.replace(marker,block+marker,1)
if en_row not in idx:
    marker='## Relation between principles and applied work'
    block='''## Eighteenth wave · Civic power and institutions · LI\n\n| No. | Manifesto | Function | Open Synthesis |\n|---:|---|---|---|\n'''+en_row+'\n\n'
    if marker not in idx: raise SystemExit('EN insertion marker missing')
    idx=idx.replace(marker,block+marker,1)

# update canonical navigation latest
idx=re.sub(r'- Último manifiesto / Latest manifesto: \[[^\]]+\]\([^\)]+\)', '- Último manifiesto / Latest manifesto: [LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™](./51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md)', idx)
IDX.write_text(idx,encoding='utf-8')

# update L forward navigation
lp=MAN/'50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md'
lt=lp.read_text(encoding='utf-8')
# if navigation closes to I, add LI as forward destination
lt=lt.replace('← [XLIX · Punto de Encuentro entre Culturas™](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md) · [Índice](./README.md) · [I · Neo0™](./11_neo0_soberania_de_guia_ES_EN.md) →','← [XLIX · Punto de Encuentro entre Culturas™](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md) · [Índice](./README.md) · [LI · Poder Cívico y Síntesis Abierta™](./51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md) →')
lp.write_text(lt,encoding='utf-8')

# Build entries directly from manifesto H1 + filenames 1..51 using current canonical managed list plus LI
canon=IDX.read_text(encoding='utf-8')
managed_re=re.compile(r'<!-- NEO_ALL_MANIFESTOS_START -->.*?<!-- NEO_ALL_MANIFESTOS_END -->',re.S)
oldm=managed_re.search(canon)
if not oldm: raise SystemExit('canonical managed network missing')
# extract existing list paths/romans from managed block
rows=[]
for roman,title,path in re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)',oldm.group(0)):
    if roman!='LI': rows.append((roman,title,MAN/path))
# force 50 existing unique by roman
uniq=[]; seen=set()
for x in rows:
    if x[0] not in seen: uniq.append(x);seen.add(x[0])
rows=uniq
if len(rows)!=50: raise SystemExit(f'expected 50 prior entries, got {len(rows)}')
rows.append(('LI','Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™ / Open Synthesis as Complementary or Substitutive Civic Power™',LI))

start='<!-- NEO_ALL_MANIFESTOS_START -->'; end='<!-- NEO_ALL_MANIFESTOS_END -->'
br=re.compile(re.escape(start)+r'.*?'+re.escape(end),re.S)
readmes=sorted({*ROOT.rglob('README.md'),*ROOT.rglob('LEEME.md')})
readmes=[p for p in readmes if not any(a in {'.git','node_modules','dist','build','.astro'} for a in p.parts)]
changed=[]
for p in readmes:
    old=p.read_text(encoding='utf-8')
    idxrel=os.path.relpath(IDX,p.parent).replace(os.sep,'/')
    lines=[start,'','## Red completa de manifiestos / Complete manifesto network','',
      '**Estado canónico / Canonical state:** **51 manifiestos bilingües · I–LI · 18 oleadas / 51 bilingual manifestos · I–LI · 18 waves**  ',
      f'**Índice canónico / Canonical index:** [{idxrel}]({idxrel})','',
      '<details>','<summary><strong>I–LI · 51 manifiestos / 51 manifestos</strong></summary>','']
    for roman,title,target in rows:
        rel=os.path.relpath(target,p.parent).replace(os.sep,'/')
        lines.append(f'- **{roman}** · [{title}]({rel})')
    lines += ['', '</details>', '', '> **Regla de lectura / Reading rule:** ningún manifiesto equivale por sí solo al marco completo. Esta navegación mantiene los 51 manifiestos accesibles desde cualquier README sin sustituir el contexto propio de cada nodo. / No single manifesto equals the complete framework. This navigation keeps all 51 manifestos accessible from every README without replacing each node’s own context.', '',end]
    block='\n'.join(lines)
    new=br.sub(block,old,count=1) if start in old and end in old else old
    for a,b in {
      '50 manifiestos bilingües · I–L · 17 oleadas':'51 manifiestos bilingües · I–LI · 18 oleadas',
      '50 bilingual manifestos · I–L · 17 waves':'51 bilingual manifestos · I–LI · 18 waves',
      'I–L · 50 manifiestos bilingües / 50 bilingual manifestos':'I–LI · 51 manifiestos bilingües / 51 bilingual manifestos',
      'I–L · 50 manifiestos / 50 manifestos':'I–LI · 51 manifiestos / 51 manifestos'}.items(): new=new.replace(a,b)
    if new!=old:
        p.write_text(new,encoding='utf-8'); changed.append(str(p))

# validate managed networks
errors=[]
for p in readmes:
    t=p.read_text(encoding='utf-8')
    m=br.search(t)
    if not m: errors.append(f'{p}: missing managed block'); continue
    mm=m.group(0)
    if '51 manifiestos bilingües · I–LI · 18 oleadas' not in mm: errors.append(f'{p}: stale state')
    for roman,_,target in rows:
        if mm.count(f'- **{roman}** · ')!=1: errors.append(f'{p}: missing/duplicate {roman}')
    links=re.findall(r'\[[^\]]*\]\(([^)]+)\)',mm)
    local=[x for x in links if not x.startswith(('http://','https://','mailto:','#'))]
    if len(local)!=52: errors.append(f'{p}: expected 52 local links got {len(local)}')
    for x in local:
        base=x.split('#',1)[0]
        if base and not (p.parent/base).resolve().exists(): errors.append(f'{p}: broken {x}')

# verify LI references and issue
for needed in [str(LI.name),'issues/59','Decimoctava oleada','Eighteenth wave']:
    if needed not in IDX.read_text(encoding='utf-8'): errors.append('canonical missing '+needed)
if errors:
    print('\n'.join('ERROR '+x for x in errors)); sys.exit(1)
print('READMES_TOTAL=',len(readmes))
print('READMES_CHANGED=',len(changed))
for x in changed: print('CHANGED',x)
print('POSTCHECK OK: 51/51 manifestos linked from every README/LEEME; LI integrated')
