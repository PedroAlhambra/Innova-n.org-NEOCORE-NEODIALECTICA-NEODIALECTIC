from pathlib import Path
import os,re,sys

root=Path('.').resolve()
manifestos=root/'manifiestos'
latest=manifestos/'52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md'
prev=manifestos/'51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md'
index=manifestos/'README.md'
protocol=root/'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index=root/'propuestas/sintesis-abierta/README.md'
analysis_cit=root/'analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md'
debate=root/'propuestas/sintesis-abierta/2026-08-08_LII_ciudadania_humana_neodialectica_debate_ES_EN.md'
delta_power=root/'analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md'
history=root/'analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md'
history_add=root/'analisis/publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md'
issue64='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64'

for p in (latest,prev,index,protocol,synth_index,analysis_cit,debate,delta_power,history,history_add):
    if not p.exists(): raise SystemExit(f'Missing target: {p.relative_to(root)}')

changed=[]
def write(p,text):
    old=p.read_text(encoding='utf-8')
    if text!=old:
        p.write_text(text,encoding='utf-8'); changed.append(p)

def rel(f,target):
    return os.path.relpath(target,start=f.parent).replace(os.sep,'/')

# 1) Correct newly created LII genealogy/canonical English naming if needed.
t=latest.read_text(encoding='utf-8')
t=t.replace('XXVII · Neofraternidad™','XXXVII · Neofraternidad™')
t=t.replace('Neodialectical Archetypal Philosophy™ separates','Archetypal Neodialectical Philosophy™ separates')
write(latest,t)

# 2) Canonical manifesto index -> 52 / I-LII / 19 waves and add LII item.
t=index.read_text(encoding='utf-8')
repls={
'51 manifiestos bilingües · I–LI · 18 oleadas':'52 manifiestos bilingües · I–LII · 19 oleadas',
'51 bilingual manifestos · I–LI · 18 waves':'52 bilingual manifestos · I–LII · 19 waves',
'I–LI · 51 manifiestos bilingües':'I–LII · 52 manifiestos bilingües',
'I–LI · 51 bilingual manifestos':'I–LII · 52 bilingual manifestos',
'I–LI · 51 manifiestos / 51 manifestos':'I–LII · 52 manifiestos / 52 manifestos',
'los 51 manifiestos accesibles':'los 52 manifiestos accesibles',
'all 51 manifestos accessible':'all 52 manifestos accessible',
}
for a,b in repls.items(): t=t.replace(a,b)
li_line='- **LI** · [Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™ / Open Synthesis as Complementary or Substitutive Civic Power™](51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md)'
lii_line='- **LII** · [Manifiesto de la Ciudadanía Humana Neodialéctica™ / Manifesto of Neodialectical Human Citizenship™](52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)'
if lii_line not in t:
    if li_line not in t: raise SystemExit('LI index line not found')
    t=t.replace(li_line,li_line+'\n'+lii_line,1)
write(index,t)

# 3) Update previous LI navigation and add material relations to LII + incentive delta.
t=prev.read_text(encoding='utf-8')
t=t.replace('← [L · Inteligencia Compartida, no Única™](./50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md) · [Índice](./README.md) · [I · Neo0™](./11_neo0_soberania_de_guia_ES_EN.md) →',
            '← [L · Inteligencia Compartida, no Única™](./50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md) · [Índice](./README.md) · [LII · Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) →')
nav_start='<!-- NEO_MANIFESTO_NAV_START -->'; nav_end='<!-- NEO_MANIFESTO_NAV_END -->'
new_nav=f'''{nav_start}\n\n## Navegación canónica / Canonical navigation\n\n← **L** · [Por una Inteligencia Compartida, no Única™ · Invitación Abierta a las IAs / For Shared, Not Singular Intelligence™](50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)\n· [Índice I–LII / I–LII index](README.md) ·\n**LII** · [Ciudadanía Humana Neodialéctica™ / Neodialectical Human Citizenship™](52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) →\n\n> La navegación canónica mantiene la colección conectada sin convertir ningún manifiesto aislado en equivalente del marco completo. / Canonical navigation keeps the collection connected without treating any single manifesto as equivalent to the complete framework.\n\n{nav_end}'''
t=re.sub(re.escape(nav_start)+r'.*?'+re.escape(nav_end),new_nav,t,count=1,flags=re.S)
marker='<!-- NEO_LII_RELATION_START -->'
if marker not in t:
    block=f'''\n\n{marker}\n## Relaciones nuevas · ciudadanía e incentivos / New relations · citizenship and incentives\n\n- [LII · Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) · [Síntesis #64]({issue64})\n- [Delta · Poder, incentivos, tokenización y transición](../analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md)\n\nLI aporta la capa institucional; LII desarrolla pertenencia cívica multiescala; el delta de incentivos conecta capacidad cívica con mecanismos económicos y de adopción. / LI provides the institutional layer; LII develops multiscale civic belonging; the incentives delta connects civic capacity with economic and adoption mechanisms.\n<!-- NEO_LII_RELATION_END -->'''
    t=t.replace('<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->',block+'\n\n<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->',1)
write(prev,t)

# 4) Add backlink from XLIX to LII.
p49=manifestos/'49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md'
t=p49.read_text(encoding='utf-8')
if '<!-- NEO_LII_CULTURAL_RELATION_START -->' not in t:
    block=f'''\n\n<!-- NEO_LII_CULTURAL_RELATION_START -->\n## Relación con Ciudadanía Humana Neodialéctica™ / Relation to Neodialectical Human Citizenship™\n\nLa interoperabilidad cultural encuentra una derivación cívica en [LII · Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md): conservar identidad y memoria sin convertir origen, sangre o nacimiento en jerarquía humana. Debate: [Síntesis Abierta #64]({issue64}).\n\nCultural interoperability gains a civic derivation in [LII · Neodialectical Human Citizenship™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md): preserving identity and memory without turning origin, blood or birthplace into human hierarchy. Debate: [Open Synthesis #64]({issue64}).\n<!-- NEO_LII_CULTURAL_RELATION_END -->'''
    anchor='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'
    t=t.replace(anchor,block+'\n\n'+anchor,1) if anchor in t else t+block
write(p49,t)

# 5) Backlinks from XLII to incentive delta.
p42=manifestos/'42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'
t=p42.read_text(encoding='utf-8')
if '<!-- NEO_INCENTIVE_DELTA_START -->' not in t:
    block='''\n\n<!-- NEO_INCENTIVE_DELTA_START -->\n## Delta de implementación · incentivos y transición / Implementation delta · incentives and transition\n\nLa dirección cognitiva de XLII se conecta con [Poder, incentivos, tokenización y transición](../analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md), que relaciona soberanía cognitiva con Economía del Aporte, futura Proof of Usefulness, tokenización futura, fiscalidad, alternativa técnica y capacidad cívica distribuida.\n\nThe cognitive direction of XLII is connected to [Power, incentives, tokenisation and transition](../analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md), relating cognitive sovereignty to the Contribution Economy, future Proof of Usefulness, future tokenisation, taxation, technical alternatives and distributed civic capacity.\n<!-- NEO_INCENTIVE_DELTA_END -->'''
    anchor='<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->'
    t=t.replace(anchor,block+'\n\n'+anchor,1) if anchor in t else t+block
write(p42,t)

# 6) Add LII + recent analyses to analysis indexes/readmes.
analysis_targets=[root/'analisis/README.md',root/'analisis/publicos/README.md',root/'analisis/INDEX.md']
for f in analysis_targets:
    t=f.read_text(encoding='utf-8')
    es_line=f'* [2026-08-08 · Ciudadanía Humana Neodialéctica™ · sangre, suelo y pertenencia cívica funcional]({rel(f,analysis_cit)})\n  * [Manifiesto LII]({rel(f,latest)}) · [Síntesis Abierta #64]({issue64})\n* [2026-08-08 · Delta · Poder, incentivos, tokenización y transición]({rel(f,delta_power)})\n'
    en_line=f'* [2026-08-08 · Neodialectical Human Citizenship™ · blood, soil and functional civic belonging]({rel(f,analysis_cit)})\n  * [Manifesto LII]({rel(f,latest)}) · [Open Synthesis #64]({issue64})\n* [2026-08-08 · Delta · Power, incentives, tokenisation and transition]({rel(f,delta_power)})\n'
    if 'Ciudadanía Humana Neodialéctica™ · sangre, suelo y pertenencia cívica funcional' not in t:
        m=re.search(r'## Análisis públicos\s*\n',t)
        if m: t=t[:m.end()]+'\n'+es_line+t[m.end():]
        else: t+='\n\n## Análisis públicos\n\n'+es_line
    if 'Neodialectical Human Citizenship™ · blood, soil and functional civic belonging' not in t:
        m=list(re.finditer(r'## Public analyses\s*\n',t))
        if m:
            x=m[-1]; t=t[:x.end()]+'\n'+en_line+t[x.end():]
    write(f,t)

# 7) Root/LEEME recent-incorporation backlinks (latest blocks handled later).
for f in [root/'README.md',root/'LEEME.md']:
    if not f.exists(): continue
    t=f.read_text(encoding='utf-8')
    es=f'* [2026-08-08 · Ciudadanía Humana Neodialéctica™]({rel(f,latest)}) · [Síntesis #64]({issue64})\n* [2026-08-08 · Delta · Poder, incentivos, tokenización y transición]({rel(f,delta_power)})\n'
    en=f'* [2026-08-08 · Neodialectical Human Citizenship™]({rel(f,latest)}) · [Open Synthesis #64]({issue64})\n* [2026-08-08 · Delta · Power, incentives, tokenisation and transition]({rel(f,delta_power)})\n'
    if '2026-08-08 · Ciudadanía Humana Neodialéctica™]' not in t:
        m=re.search(r'## Incorporaciones recientes\s*\n',t)
        if m: t=t[:m.end()]+'\n'+es+t[m.end():]
    if '2026-08-08 · Neodialectical Human Citizenship™]' not in t:
        m=list(re.finditer(r'## Recent incorporations\s*\n',t))
        if m:
            x=m[-1]; t=t[:x.end()]+'\n'+en+t[x.end():]
    write(f,t)

# 8) Open Synthesis index: add dedicated LII feature and counts.
t=synth_index.read_text(encoding='utf-8')
feature_start='<!-- NEO_LII_CITIZENSHIP_SYNTHESIS_START -->'; feature_end='<!-- NEO_LII_CITIZENSHIP_SYNTHESIS_END -->'
feature=f'''{feature_start}\n\n> ## 🟢 LII · CIUDADANÍA HUMANA NEODIALÉCTICA™ / NEODIALECTICAL HUMAN CITIZENSHIP™\n>\n> **Sangre = genealogía · suelo = vínculo · dignidad humana = común / Blood = genealogy · soil = relation · human dignity = common**\n>\n> [Manifiesto LII / Manifesto LII]({rel(synth_index,latest)}) · [Análisis / Analysis]({rel(synth_index,analysis_cit)}) · [Ficha de debate / Debate brief]({rel(synth_index,debate)}) · [Síntesis Abierta #64 / Open Synthesis #64]({issue64})\n\n{feature_end}'''
if feature_start not in t:
    marker='<!-- NEO_FORGOTTEN_HISTORY_SYNTHESIS_START -->'
    pos=t.find(marker)
    t=t[:pos]+feature+'\n\n'+t[pos:] if pos!=-1 else feature+'\n\n'+t
for a,b in {
'51 manifiestos · I–LI':'52 manifiestos · I–LII',
'51 manifestos · I–LI':'52 manifestos · I–LII',
'I–LI · 51 manifiestos bilingües':'I–LII · 52 manifiestos bilingües',
'I–LI · 51 bilingual manifestos':'I–LII · 52 bilingual manifestos',
'51 manifiestos bilingües · I–LI · 18 oleadas':'52 manifiestos bilingües · I–LII · 19 oleadas',
'51 bilingual manifestos · I–LI · 18 waves':'52 bilingual manifestos · I–LII · 19 waves',
'I–LI · 51 manifiestos / 51 manifestos':'I–LII · 52 manifiestos / 52 manifestos',
}.items(): t=t.replace(a,b)
if lii_line not in t:
    # Canonical-network items in this README use ../../manifiestos links.
    sli='- **LI** · [Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™ / Open Synthesis as Complementary or Substitutive Civic Power™](../../manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md)'
    sl2='- **LII** · [Manifiesto de la Ciudadanía Humana Neodialéctica™ / Manifesto of Neodialectical Human Citizenship™](../../manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)'
    if sli in t: t=t.replace(sli,sli+'\n'+sl2,1)
write(synth_index,t)

# 9) Transversal relation map: coverage + new block for recent work.
relmap=manifestos/'RELACIONES_TRABAJO_APLICADO_ES_EN.md'
t=relmap.read_text(encoding='utf-8')
t=t.replace('I–LI · 51 manifiestos / 51 manifestos','I–LII · 52 manifiestos / 52 manifestos')
if '<!-- NEO_LII_APPLIED_RELATIONS_START -->' not in t:
    block='''\n\n<!-- NEO_LII_APPLIED_RELATIONS_START -->\n## Ciudadanía, pertenencia e incentivos de transición / Citizenship, belonging and transition incentives\n\n- **A/B · LII · Ciudadanía Humana Neodialéctica™** ↔ [Análisis de base](../analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md) ↔ [Síntesis Abierta #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64). Desarrolla igualdad de pertenencia, no mercantilización, multiescala y continuidad de protección.\n- **B · III/VII/XXI/XLII/LI** ↔ [Delta · Poder, incentivos, tokenización y transición](../analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md). Relaciona registro de aporte, Economía del Aporte, Reconocimiento/PoU, soberanía cognitiva y capacidad cívica.\n- **B/C · IX/XIII/XVI/XIX/XX/XLVIII/LI** ↔ [Historia Olvidada™](../analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md) ↔ [Autodemostración Neodialéctica™](../analisis/publicos/2026-08-08_addendum_autodemostracion_creacion_neodialectica_historia_olvidada_ES_EN.md) ↔ [Síntesis #63](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/63).\n\nLa relación documental no convierte hipótesis históricas en hechos ni propuestas normativas en derecho vigente. / Documentary relation does not turn historical hypotheses into facts or normative proposals into current law.\n<!-- NEO_LII_APPLIED_RELATIONS_END -->'''
    t+='\n'+block+'\n'
write(relmap,t)

# 10) wiki-source/Manifiestos and wiki-source README references.
wmanifest=root/'wiki-source/Manifiestos.md'
if wmanifest.exists():
    t=wmanifest.read_text(encoding='utf-8')
    t=t.replace('51 manifiestos','52 manifiestos').replace('51 manifestos','52 manifestos').replace('I–LI','I–LII')
    if '52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md' not in t:
        t+='\n\n## LII · Ciudadanía Humana Neodialéctica™\n\n- [Manifiesto LII](../manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)\n- [Síntesis Abierta #64]('+issue64+')\n'
    write(wmanifest,t)

# 11) Update every README/LEEME latest-manifesto feature and canonical count phrases.
start='<!-- NEO_LATEST_MANIFESTO_START -->'; end='<!-- NEO_LATEST_MANIFESTO_END -->'
def latest_block(f):
    return f'''{start}\n\n> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS\n>\n> **LII · Ciudadanía Humana Neodialéctica™**  \n> **LII · Neodialectical Human Citizenship™**\n>\n> La propuesta está **abierta a crítica, objeciones, contraejemplos, fuentes, correcciones y propuestas de mejora**. No se pide adhesión: se pide contraste. / The proposal is **open to criticism, objections, counterexamples, sources, corrections and improvement proposals**. Endorsement is not required: scrutiny is.\n>\n> **[Leer manifiesto LII / Read manifesto LII]({rel(f,latest)}) · [Participar en la Síntesis Abierta LII · Issue #64 / Join Open Synthesis LII · Issue #64]({issue64})**  \n> [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Índice de Síntesis Abierta / Open Synthesis index]({rel(f,synth_index)}) · [52 manifiestos I–LII / 52 manifestos I–LII]({rel(f,index)})\n\n{end}'''

readmes=sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
if (root/'LEEME.md').exists(): readmes.append(root/'LEEME.md')
readmes=sorted(set(readmes))
for f in readmes:
    t=f.read_text(encoding='utf-8'); old=t
    b=latest_block(f)
    if start in t and end in t:
        t=re.sub(re.escape(start)+r'.*?'+re.escape(end),b,t,count=1,flags=re.S)
    else:
        m=re.search(r'^\[ES[^\n]*\]\([^\n]+\)\s*·\s*\[EN[^\n]*\]\([^\n]+\)\s*$',t,re.M)
        if m: t=t[:m.end()]+'\n\n'+b+t[m.end():]
        else:
            lines=t.splitlines(True); ins=1 if lines and lines[0].lstrip().startswith('#') else 0
            lines.insert(ins,'\n'+b+'\n\n'); t=''.join(lines)
    for a,b2 in {
        '51 manifiestos bilingües · I–LI · 18 oleadas':'52 manifiestos bilingües · I–LII · 19 oleadas',
        '51 bilingual manifestos · I–LI · 18 waves':'52 bilingual manifestos · I–LII · 19 waves',
        'I–LI · 51 manifiestos bilingües':'I–LII · 52 manifiestos bilingües',
        'I–LI · 51 bilingual manifestos':'I–LII · 52 bilingual manifestos',
        'I–LI · 51 manifiestos / 51 manifestos':'I–LII · 52 manifiestos / 52 manifestos',
        '51 manifiestos I–LI':'52 manifiestos I–LII',
        '51 manifestos I–LI':'52 manifestos I–LII',
        '51 manifiestos · I–LI':'52 manifiestos · I–LII',
        '51 manifestos · I–LI':'52 manifestos · I–LII',
    }.items(): t=t.replace(a,b2)
    if t!=old: f.write_text(t,encoding='utf-8'); changed.append(f)

# 12) Update reusable latest-manifesto synchronizer so it cannot revert LII later.
sync=root/'.github/scripts/sync_latest_manifesto_feature.py'
if sync.exists():
    t=sync.read_text(encoding='utf-8')
    t=t.replace("latest=root/'manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md'", "latest=root/'manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md'")
    t=t.replace("issue59='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59'", "issue64='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64'")
    t=t.replace('**LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™**', '**LII · Ciudadanía Humana Neodialéctica™**')
    t=t.replace('**LI · Open Synthesis as Complementary or Substitutive Civic Power™**', '**LII · Neodialectical Human Citizenship™**')
    t=t.replace('Leer manifiesto LI / Read manifesto LI', 'Leer manifiesto LII / Read manifesto LII')
    t=t.replace('Participar en la Síntesis Abierta LI · Issue #59 / Join Open Synthesis LI · Issue #59]({issue59})', 'Participar en la Síntesis Abierta LII · Issue #64 / Join Open Synthesis LII · Issue #64]({issue64})')
    t=t.replace('[51 manifiestos I–LI / 51 manifestos I–LI]', '[52 manifiestos I–LII / 52 manifestos I–LII]')
    t=t.replace("if 'Issue #59' not in blk or '51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md' not in blk:", "if 'Issue #64' not in blk or '52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md' not in blk:")
    t=t.replace("fail.append(f'{f.relative_to(root)}: LI/Issue #59 feature incomplete')", "fail.append(f'{f.relative_to(root)}: LII/Issue #64 feature incomplete')")
    t=t.replace('exactly I..LI, 51 unique canonical files','exactly I..LII, 52 unique canonical files')
    t=t.replace("if len(unique)!=51 or unique[0][0]!='I' or unique[-1][0]!='LI':", "if len(unique)!=52 or unique[0][0]!='I' or unique[-1][0]!='LII':")
    t=t.replace("POSTCHECK OK: latest LI + Open Synthesis #59 featured near top of every README/LEEME; canonical I-LI network intact", "POSTCHECK OK: latest LII + Open Synthesis #64 featured near top of every README/LEEME; canonical I-LII network intact")
    write(sync,t)

wf=root/'.github/workflows/sync-latest-manifesto-feature.yml'
if wf.exists():
    t=wf.read_text(encoding='utf-8')
    t=t.replace("docs: feature manifesto LI and Open Synthesis 59 across all READMEs", "docs: feature manifesto LII and Open Synthesis 64 across all READMEs")
    write(wf,t)

# 13) Postcheck.
fail=[]
idx=index.read_text(encoding='utf-8')
if idx.count(lii_line)!=1: fail.append('manifiestos/README.md: LII item missing/duplicated')
if '52 manifiestos bilingües · I–LII · 19 oleadas' not in idx: fail.append('manifiestos/README.md: canonical state not 52/I-LII/19')
for f in readmes:
    t=f.read_text(encoding='utf-8')
    if t.count(start)!=1 or t.count(end)!=1: fail.append(f'{f.relative_to(root)}: latest markers invalid')
    m=re.search(re.escape(start)+r'(.*?)'+re.escape(end),t,re.S)
    if not m or 'Issue #64' not in m.group(1) or '52_ciudadania_humana' not in m.group(1): fail.append(f'{f.relative_to(root)}: LII latest block incomplete')
for p in [latest,analysis_cit,debate,delta_power,history,history_add]:
    if not p.exists(): fail.append(f'missing {p.relative_to(root)}')
if 'XXXVII · Neofraternidad™' not in latest.read_text(encoding='utf-8'): fail.append('LII genealogy Neofraternity numeral incorrect')
if '52_ciudadania_humana' not in prev.read_text(encoding='utf-8'): fail.append('LI backlink to LII missing')
if '52_ciudadania_humana' not in p49.read_text(encoding='utf-8'): fail.append('XLIX backlink to LII missing')
if 'delta_poder_incentivos' not in p42.read_text(encoding='utf-8'): fail.append('XLII backlink to incentives delta missing')
print('FILES_CHANGED',len(set(changed)))
for p in sorted(set(changed)): print('CHANGED',p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL')
    for x in fail: print(x)
    sys.exit(1)
print('POSTCHECK OK: LII/64 canonical, recent research linked, README/LEEME synchronized')
