from pathlib import Path
import os, re, urllib.parse

ROOT=Path('.')
XLV='manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md'
XLVI='manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md'
ISSUE54='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/54'
LIVE=[Path(x) for x in ['README.md','LEEME.md','PORTADA.md','COVER.md','manifiestos/README.md','propuestas/sintesis-abierta/README.md','wiki-source/README.md','wiki-source/Manifiestos.md']]

def rel(src:Path,target:str):
    r=os.path.relpath(target,src.parent).replace('\\','/')
    return r if r.startswith('.') else './'+r

def write_if(p,t):
    old=p.read_text(encoding='utf-8')
    if old!=t:
        p.write_text(t,encoding='utf-8'); return 1
    return 0

changed=0

# 1. XLV navigation must now continue to XLVI.
p=Path(XLV); t=p.read_text(encoding='utf-8')
t=t.replace('← [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) · [Índice](./README.md) · [I · Neo0™ · Soberanía de Guía Neodialéctica](./11_neo0_soberania_de_guia_ES_EN.md) →',
            '← [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) · [Índice](./README.md) · [XLVI · Cerrar la Herida™](./46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md) →')
t=t.replace('← [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) · [Index](./README.md) · [I · Neo0™ · Neodialectical Guiding Sovereignty](./11_neo0_soberania_de_guia_ES_EN.md) →',
            '← [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) · [Index](./README.md) · [XLVI · Closing the Wound™](./46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md) →')
changed+=write_if(p,t)

# 2. Update standardized current-state blocks and current counts in live hubs.
for p in LIVE:
    if not p.exists(): continue
    t=p.read_text(encoding='utf-8'); old=t
    t=re.sub(r'I–XLV(?!I)', 'I–XLVI', t)
    t=re.sub(r'\b45 manifiestos bilingües\b', '46 manifiestos bilingües', t, flags=re.I)
    t=re.sub(r'\b45 bilingual manifestos\b', '46 bilingual manifestos', t, flags=re.I)
    t=t.replace('doce oleadas','trece oleadas').replace('twelve waves','thirteen waves')
    if '<!-- NEO_CURRENT_NAV_START -->' in t and '<!-- NEO_CURRENT_NAV_END -->' in t:
        a,b=t.split('<!-- NEO_CURRENT_NAV_START -->',1); mid,c=b.split('<!-- NEO_CURRENT_NAV_END -->',1)
        target=rel(p,XLVI)
        mid=re.sub(r'- Último manifiesto / Latest manifesto: .*?\n',
                   f'- Último manifiesto / Latest manifesto: [XLVI · Cerrar la Herida™ / Closing the Wound™]({target}).\n',mid, count=1)
        if 'Último manifiesto / Latest manifesto:' not in mid:
            marker='**Neodialectica Framework™ / Network · Innova_N · NEOCore™**\n\n'
            if marker in mid:
                mid=mid.replace(marker,marker+f'- Último manifiesto / Latest manifesto: [XLVI · Cerrar la Herida™ / Closing the Wound™]({target}).\n',1)
        t=a+'<!-- NEO_CURRENT_NAV_START -->'+mid+'<!-- NEO_CURRENT_NAV_END -->'+c
    if t!=old:
        p.write_text(t,encoding='utf-8'); changed+=1

# 3. Manifesto index: correct wave taxonomy and add XII/XIII sections in both languages.
p=Path('manifiestos/README.md'); t=p.read_text(encoding='utf-8')
t=t.replace('La colección se organiza desde el 8 de agosto de 2026 en diez oleadas relacionadas:', 'La colección se organiza desde el 8 de agosto de 2026 en trece oleadas relacionadas:')
t=t.replace('Since 8 August 2026, the collection has been organised into ten related waves:', 'Since 8 August 2026, the collection has been organised into thirteen related waves:')
t=re.sub(r'\* \*\*Décima oleada · XLII–XLV:\*\*[^\n]*', '* **Décima oleada · XLII–XLIII:** Fin de la Era del Hombre Manipulado™, soberanía cognitiva e Inteligencia Humana Expandida™.', t)
t=re.sub(r'\* \*\*Tenth wave · XLII–XLV:\*\*[^\n]*', '* **Tenth wave · XLII–XLIII:** End of the Manipulated Human Era™, cognitive sovereignty and Human Expanded Intelligence™.', t)
# Add introductory wave bullets if absent in the corresponding intro section.
if '# ES · Castellano' in t and 'Los manifiestos establecen' in t:
    pre,rest=t.split('Los manifiestos establecen',1)
    additions=[]
    if '**Undécima oleada · XLIV:**' not in pre: additions.append('* **Undécima oleada · XLIV:** Neowar™, justicia civilizatoria y soberanía compartida.')
    if '**Duodécima oleada · XLV:**' not in pre: additions.append('* **Duodécima oleada · XLV:** Multidimensionalidad Neodialéctica™, singularidad y soberanía distribuida.')
    if '**Decimotercera oleada · XLVI:**' not in pre: additions.append('* **Decimotercera oleada · XLVI:** Cerrar la Herida™, comprensión evolutiva, memoria y reconciliación civilizatoria.')
    if additions: pre=pre.rstrip()+"\n"+'\n'.join(additions)+"\n\n"
    t=pre+'Los manifiestos establecen'+rest
if '# EN · English' in t and 'The manifestos establish' in t:
    a,eng=t.split('# EN · English',1)
    ep,er=eng.split('The manifestos establish',1)
    adds=[]
    if '**Eleventh wave · XLIV:**' not in ep: adds.append('* **Eleventh wave · XLIV:** Neowar™, civilisational justice and shared sovereignty.')
    if '**Twelfth wave · XLV:**' not in ep: adds.append('* **Twelfth wave · XLV:** Neodialectical Multidimensionality™, singularity and distributed sovereignty.')
    if '**Thirteenth wave · XLVI:**' not in ep: adds.append('* **Thirteenth wave · XLVI:** Closing the Wound™, evolutionary understanding, memory and civilisational reconciliation.')
    if adds: ep=ep.rstrip()+"\n"+'\n'.join(adds)+"\n\n"
    t=a+'# EN · English'+ep+'The manifestos establish'+er
# Add explicit Spanish wave sections before EN.
if '## Duodécima oleada · Multidimensionalidad' not in t:
    section='''\n## Duodécima oleada · Multidimensionalidad, singularidad y soberanía distribuida\n\n| Nº | Manifiesto | Función | Síntesis Abierta |\n|---:|---|---|---|\n| XLV | [Multidimensionalidad Neodialéctica™](./45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md) | Integrar singularidad, excelencia, liderazgo, métricas y conocimiento experto dentro de una arquitectura multidimensional sin soberanía total de ningún nodo | [Issue #53](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53) |\n\n'''
    t=t.replace('\n---\n\n# EN · English',section+'---\n\n# EN · English',1)
if '## Decimotercera oleada · Cerrar la Herida' not in t:
    section='''## Decimotercera oleada · Cerrar la Herida™, comprensión evolutiva y reconciliación\n\n| Nº | Manifiesto | Función | Síntesis Abierta |\n|---:|---|---|---|\n| XLVI | [Cerrar la Herida™ · Comprensión Evolutiva, Memoria y Reconciliación Civilizatoria](./46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md) | Comprender el origen del daño sin justificarlo; conservar verdad y responsabilidad orientando memoria y reparación hacia integración y futuro | [Issue #54](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/54) |\n\n> **Principio transversal:** nada es contra personas. El lenguaje de oposición del corpus debe leerse como análisis y transformación de mecanismos, no como fabricación de enemigos esenciales.\n\n'''
    t=t.replace('\n---\n\n# EN · English', '\n'+section+'---\n\n# EN · English',1)
# Add English sections before current nav.
anchor='<!-- NEO_CURRENT_NAV_START -->'
if '## Twelfth wave · Multidimensionality' not in t:
    sec='''\n## Twelfth wave · Multidimensionality, singularity and distributed sovereignty\n\n| No. | Manifesto | Function | Open Synthesis |\n|---:|---|---|---|\n| XLV | [Neodialectical Multidimensionality™](./45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md) | Integrate singularity, excellence, leadership, metrics and expertise within a multidimensional architecture without total sovereignty of any node | [Issue #53](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53) |\n\n'''
    t=t.replace(anchor,sec+anchor,1)
if '## Thirteenth wave · Closing the Wound' not in t:
    sec='''## Thirteenth wave · Closing the Wound™, evolutionary understanding and reconciliation\n\n| No. | Manifesto | Function | Open Synthesis |\n|---:|---|---|---|\n| XLVI | [Closing the Wound™ · Evolutionary Understanding, Memory and Civilisational Reconciliation](./46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md) | Understand the origins of harm without justifying it; preserve truth and responsibility while orienting memory and repair toward integration and future | [Issue #54](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/54) |\n\n> **Transversal principle:** nothing is against persons. Oppositional language in the corpus should be read as analysis and transformation of mechanisms, not as manufacture of essential enemies.\n\n'''
    t=t.replace(anchor,sec+anchor,1)
# Reading sequence
if 'XLVI · CERRAR LA HERIDA' not in t:
    t=t.replace('XLV · NEODIALECTICAL MULTIDIMENSIONALITY\n        ↓\nI · NEO0™', 'XLV · NEODIALECTICAL MULTIDIMENSIONALITY\n        ↓\nXLVI · CLOSING THE WOUND · EVOLUTIONARY UNDERSTANDING, MEMORY AND RECONCILIATION\n        ↓\nI · NEO0™')
# Documentary status corrections.
t=t.replace('The tenth wave contains **XLII–XLV**', 'The tenth wave contains **XLII–XLIII**')
if 'The eleventh wave contains **XLIV**' not in t:
    needle='The tenth wave contains **XLII–XLIII**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™.'
    repl=needle+' The eleventh wave contains **XLIV · Neowar™**. The twelfth wave contains **XLV · Neodialectical Multidimensionality™**. The thirteenth wave contains **XLVI · Closing the Wound™**, oriented toward evolutionary understanding, memory, repair and civilisational reconciliation.'
    t=t.replace(needle,repl)
if 'La decimotercera oleada contiene **XLVI' not in t:
    needle='La décima oleada contiene **XLII–XLIII**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™.'
    if needle in t:
        t=t.replace(needle,needle+' La undécima oleada contiene **XLIV · Neowar™**. La duodécima oleada contiene **XLV · Multidimensionalidad Neodialéctica™**. La decimotercera oleada contiene **XLVI · Cerrar la Herida™**, orientado a comprensión evolutiva, memoria, reparación y reconciliación civilizatoria.')
write_if(p,t)

# 4. Open Synthesis index: ensure XLVI is directly visible.
p=Path('propuestas/sintesis-abierta/README.md'); t=p.read_text(encoding='utf-8')
if 'issues/54' not in t:
    entry=f'''\n## XLVI · Cerrar la Herida™ / Closing the Wound™\n\n- [Manifiesto / Manifesto XLVI](../../manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md)\n- [Síntesis Abierta / Open Synthesis · Issue #54]({ISSUE54})\n- [Cómo aportar / How to contribute](./APORTAR_A_LA_SINTESIS_ES_EN.md)\n\n'''
    t=t.replace('<!-- NEO_CURRENT_NAV_START -->',entry+'<!-- NEO_CURRENT_NAV_START -->',1)
write_if(p,t)

# 5. Wiki-source Manifestos: explicit XLVI bridge.
p=Path('wiki-source/Manifiestos.md'); t=p.read_text(encoding='utf-8')
if '46_cerrar_la_herida' not in t:
    entry=f'''\n## XLVI · Cerrar la Herida™ / Closing the Wound™\n\n- [Manifiesto versionado / Versioned manifesto](../{XLVI})\n- [Síntesis Abierta / Open Synthesis · Issue #54]({ISSUE54})\n\n**Principio transversal / Transversal principle:** nada es contra personas; comprender origen no equivale a justificar daño. / Nothing is against persons; understanding origins does not mean justifying harm.\n\n'''
    t=t.replace('<!-- NEO_CURRENT_NAV_START -->',entry+'<!-- NEO_CURRENT_NAV_START -->',1)
write_if(p,t)

# 6. Root/cover hubs: if no explicit XLVI outside current nav, add a compact current-access line before nav.
for name in ['README.md','LEEME.md','PORTADA.md','COVER.md']:
    p=Path(name); t=p.read_text(encoding='utf-8')
    if '46_cerrar_la_herida' not in t:
        entry=f'\n- [XLVI · Cerrar la Herida™ · Closing the Wound™]({rel(p,XLVI)}) · [Síntesis Abierta / Open Synthesis #54]({ISSUE54})\n'
        t=t.replace('<!-- NEO_CURRENT_NAV_START -->',entry+'\n<!-- NEO_CURRENT_NAV_START -->',1)
    write_if(p,t)

# 7. Audit index entry.
p=Path('auditorias/publicas/README.md')
if p.exists():
    t=p.read_text(encoding='utf-8')
    report='./2026-08-08_postcheck_XLVI_cerrar_herida_enlaces_readmes_ES_EN.md'
    if 'postcheck_XLVI_cerrar_herida' not in t:
        entry=f'''\n* [2026-08-08 · Postcheck XLVI · Cerrar la Herida™]({report})\n\n  Verifica propagación I–XLVI, Síntesis Abierta #54, navegación, READMEs y enlaces internos tras fijar comprensión evolutiva, memoria y reconciliación como decimotercera oleada.\n\n'''
        anchor='### Integridad documental / Documentary integrity\n'
        t=t.replace(anchor,anchor+entry,1) if anchor in t else t+entry
    write_if(p,t)

# 8. Validate internal relative Markdown links, with wiki extensionless aliases.
LINK_RE=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
files=sorted(x for x in ROOT.rglob('*.md') if '.git' not in x.parts and 'node_modules' not in x.parts)
root=ROOT.resolve(); checked=aliases=0; broken=[]
for src in files:
    txt=src.read_text(encoding='utf-8')
    for raw in LINK_RE.findall(txt):
        u=raw.strip().strip('<>')
        if not u or u.startswith(('http://','https://','mailto:','tel:','data:','#')): continue
        u=urllib.parse.unquote(u.split('#',1)[0].split('?',1)[0]);
        if not u: continue
        checked+=1
        cand=(ROOT/u.lstrip('/')).resolve() if u.startswith('/') else (src.parent/u).resolve()
        try: cand.relative_to(root)
        except ValueError: broken.append((str(src),raw,'escapes root')); continue
        if cand.exists(): continue
        if 'wiki-source' in src.parts and cand.with_suffix('.md').exists(): aliases+=1; continue
        broken.append((str(src),raw,str(cand)))
if broken:
    print('BROKEN',broken[:30]); raise SystemExit(2)

# 9. Canonical checks.
required=[Path(XLVI),Path(XLV),Path('manifiestos/README.md'),Path('propuestas/sintesis-abierta/README.md'),Path('wiki-source/Manifiestos.md')]
for q in required:
    if not q.exists(): raise SystemExit(f'missing {q}')
if 'issues/54' not in Path(XLVI).read_text(encoding='utf-8'): raise SystemExit('XLVI missing issue 54')
if '46_cerrar_la_herida' not in Path(XLV).read_text(encoding='utf-8'): raise SystemExit('XLV next nav missing XLVI')
for q in LIVE:
    if q.exists():
        x=q.read_text(encoding='utf-8')
        if 'I–XLV' in x and 'I–XLVI' not in x: raise SystemExit(f'stale range {q}')

# 10. Write postcheck report.
report=Path('auditorias/publicas/2026-08-08_postcheck_XLVI_cerrar_herida_enlaces_readmes_ES_EN.md')
report.write_text(f'''# Postcheck XLVI · Cerrar la Herida™ · enlaces, READMEs y navegación\n## XLVI postcheck · Closing the Wound™ · links, READMEs and navigation\n\n**Fecha / Date:** 2026-08-08  \n**Estado / Status:** **OK**\n\n- Markdown revisados / Markdown reviewed: **{len(files)}**.\n- README revisados / README reviewed: **{len(list(ROOT.rglob('README.md')))}**.\n- Enlaces internos relativos comprobados / Relative internal links checked: **{checked}**.\n- Alias Wiki extensionless reconocidos / Extensionless Wiki aliases recognised: **{aliases}**.\n- Enlaces internos rotos / Broken internal links: **0**.\n- Estado de colección / Collection state: **I–XLVI · 46 manifiestos bilingües / bilingual manifestos · trece oleadas / thirteen waves**.\n- XLVI / Open Synthesis: **Issue #54**.\n- Navegación / Navigation: **XLV → XLVI → I**.\n\nLa decimotercera oleada fija una corrección transversal: el lenguaje de oposición del corpus no debe convertirse en enemistad contra personas. Comprender el origen evolutivo, histórico, material o cultural de un mecanismo no lo justifica; permite distinguir origen, responsabilidad, reparación y transformación. / The thirteenth wave fixes a transversal correction: oppositional language in the corpus must not become enmity against persons. Understanding the evolutionary, historical, material or cultural origin of a mechanism does not justify it; it enables distinction among origin, responsibility, repair and transformation.\n''',encoding='utf-8')

# 11. Remove one-shot machinery.
Path('.github/scripts/one_shot_xlvi_close_wound.py').unlink(missing_ok=True)
Path('.github/workflows/one-shot-xlvi-close-wound.yml').unlink(missing_ok=True)
Path('.github/triggers/xlvi-close-wound.trigger').unlink(missing_ok=True)
print('XLVI_OK',len(files),checked,aliases,changed)
