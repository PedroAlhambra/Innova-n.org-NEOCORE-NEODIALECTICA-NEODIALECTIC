from pathlib import Path
import os,re,sys

idx=Path('manifiestos/README.md')
text=idx.read_text(encoding='utf-8')
es,en=text.split('# EN · English',1)
xlix='./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md'
if xlix not in es:
    marker='## Relación entre principios y trabajo aplicado'
    block="""## Decimosexta oleada · Interoperabilidad cultural · XLIX

| Nº | Manifiesto | Función | Síntesis Abierta |
|---:|---|---|---|
| XLIX | [La Neodialéctica como Punto de Encuentro entre Culturas™](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md) | Unidad sin uniformidad, interoperabilidad cultural, traducción de sentido y cooperación sin desaparición de la singularidad | [#57](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/57) |

"""
    if marker not in es:
        raise SystemExit('Spanish XLIX insertion marker missing')
    es=es.replace(marker,block+marker,1)

en=en.replace('## Current architecture · 15 waves','## Current architecture · 17 waves')
if '16. **XLIX · Meeting Point between Cultures™:' not in en:
    needle='15. **XLVIII · The Synthesis Sees Everything™:** distributed observation, Universal Petri Dish™, powers of ten, micro–macro scales and Fractal Time Machine™ as a model of evolutionary memory of the joint organism.\n'
    if needle not in en:
        raise SystemExit('English architecture insertion marker missing')
    en=en.replace(needle,needle+'16. **XLIX · Meeting Point between Cultures™:** unity without uniformity, cultural interoperability, translation of meaning and cooperation without erasing singularity.\n17. **L · Shared, Not Singular Intelligence™:** cognitive interoperability, plurality of models, anti-dogmatic training and AI participation in Open Synthesis.\n',1)

# Fix stale canonical latest-manifesto pointer if present.
en=en.replace('- Último manifiesto / Latest manifesto: [XLVIII · La Síntesis Todo lo Ve™](./48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)', '- Último manifiesto / Latest manifesto: [L · Por una Inteligencia Compartida, no Única™ / For Shared, Not Singular Intelligence™](./50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)')
idx.write_text(es+'# EN · English'+en,encoding='utf-8')

canon=idx.read_text(encoding='utf-8')
en=canon.split('# EN · English',1)[1]
row_re=re.compile(r'^\|\s*([IVXLCDM]+)\s*\|\s*\[([^\]]+)\]\((\.\/[^)]+\.md)\)\s*\|',re.M)
rows=[]; seen=set()
for roman,title,rel in row_re.findall(en):
    if roman not in seen:
        rows.append((roman,title,rel)); seen.add(roman)
if len(rows)!=50:
    raise SystemExit(f'EN manifesto count {len(rows)} != 50')

entries=[]
for roman,en_title,rel in rows:
    mf=Path('manifiestos')/rel[2:]
    if not mf.exists():
        raise SystemExit(f'Missing manifesto {roman}: {mf}')
    h1=mf.read_text(encoding='utf-8').splitlines()[0].strip()
    pref=f'# {roman} · '
    es_title=h1[len(pref):] if h1.startswith(pref) else h1.lstrip('# ').strip()
    entries.append((roman,es_title,en_title,mf))

es_part=idx.read_text(encoding='utf-8').split('# EN · English',1)[0]
es_seen={r for r,_,_ in row_re.findall(es_part)}
if len(es_seen)!=50:
    raise SystemExit(f'ES manifesto count {len(es_seen)} != 50')

start='<!-- NEO_ALL_MANIFESTOS_START -->'; end='<!-- NEO_ALL_MANIFESTOS_END -->'
br=re.compile(re.escape(start)+r'.*?'+re.escape(end),re.S)
readmes=sorted({*Path('.').rglob('README.md'),*Path('.').rglob('LEEME.md')})
readmes=[p for p in readmes if not any(a in {'.git','node_modules','dist','build','.astro'} for a in p.parts)]
changed=[]
for p in readmes:
    idxrel=os.path.relpath(idx,p.parent).replace(os.sep,'/')
    b=[start,'','## Red completa de manifiestos / Complete manifesto network','',
       '**Estado canónico / Canonical state:** **50 manifiestos bilingües · I–L · 17 oleadas / 50 bilingual manifestos · I–L · 17 waves**  ',
       f'**Índice canónico / Canonical index:** [{idxrel}]({idxrel})','',
       '<details>','<summary><strong>I–L · 50 manifiestos / 50 manifestos</strong></summary>','']
    for roman,est,ent,mf in entries:
        rel=os.path.relpath(mf,p.parent).replace(os.sep,'/')
        b.append(f'- **{roman}** · [{est} / {ent}]({rel})')
    b += ['', '</details>', '', '> **Regla de lectura / Reading rule:** ningún manifiesto equivale por sí solo al marco completo. Esta navegación mantiene los 50 manifiestos accesibles desde cualquier README sin sustituir el contexto propio de cada nodo. / No single manifesto equals the complete framework. This navigation keeps all 50 manifestos accessible from every README without replacing each node’s own context.', '',end]
    block='\n'.join(b)
    old=p.read_text(encoding='utf-8')
    if start in old and end in old:
        new=br.sub(block,old,count=1)
    else:
        sep=old.find('\n---\n')
        pos=sep+1 if sep!=-1 and sep<1800 else (old.find('\n')+1 if '\n' in old else len(old))
        new=old[:pos]+'\n'+block+'\n\n'+old[pos:]
    replacements={
       'I–XLVIII · 48 manifiestos bilingües / 48 bilingual manifestos':'I–L · 50 manifiestos bilingües / 50 bilingual manifestos',
       '49 manifiestos bilingües · I–XLIX · 16 oleadas':'50 manifiestos bilingües · I–L · 17 oleadas',
       '49 bilingual manifestos · I–XLIX · 16 waves':'50 bilingual manifestos · I–L · 17 waves',
       '50 manifiestos bilingües · I–L · dieciséis oleadas':'50 manifiestos bilingües · I–L · diecisiete oleadas',
       '50 bilingual manifestos · I–L · sixteen waves':'50 bilingual manifestos · I–L · seventeen waves',
       'Current architecture · 15 waves':'Current architecture · 17 waves'}
    for a,c in replacements.items():
        new=new.replace(a,c)
    if new!=old:
        p.write_text(new,encoding='utf-8'); changed.append(str(p))

errors=[]
for p in readmes:
    s=p.read_text(encoding='utf-8')
    if s.count(start)!=1 or s.count(end)!=1:
        errors.append(f'{p}: managed block count != 1'); continue
    m=br.search(s).group(0)
    for roman,_,_,_ in entries:
        if m.count(f'- **{roman}** · ')!=1:
            errors.append(f'{p}: missing/duplicate {roman}')
    links=re.findall(r'\[[^\]]*\]\(([^)]+)\)',m)
    local=[x for x in links if not x.startswith(('http://','https://','mailto:','#'))]
    if len(local)!=51:
        errors.append(f'{p}: managed links {len(local)} != 51')
    for x in local:
        base=x.split('#',1)[0]
        if base and not (p.parent/base).resolve().exists():
            errors.append(f'{p}: broken managed link {x}')

canon=idx.read_text(encoding='utf-8')
for x in ['## Arquitectura actual · 17 oleadas','## Current architecture · 17 waves','## Decimosexta oleada','## Decimoséptima oleada','## Sixteenth wave','## Seventeenth wave','16. **XLIX','17. **L ·']:
    if x not in canon:
        errors.append('canonical missing '+x)

print('READMES_TOTAL=',len(readmes))
print('READMES_CHANGED=',len(changed))
for x in changed:
    print('CHANGED',x)
if errors:
    print('\n'.join('ERROR '+x for x in errors))
    sys.exit(1)
print('POSTCHECK OK: 50/50 manifestos linked from every README/LEEME')
