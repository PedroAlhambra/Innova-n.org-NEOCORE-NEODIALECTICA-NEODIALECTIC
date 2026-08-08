from pathlib import Path
import os, re, urllib.parse

ROOT=Path('.')
XLIII='43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md'
XLIV='44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md'
ISSUE52='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/52'


def rel(src:Path, target:str):
    r=os.path.relpath(target, src.parent).replace('\\','/')
    return r if r.startswith('.') else './'+r


def canonical_replace(t:str):
    t=re.sub(r'I–XLIII(?!I)', 'I–XLIV', t)
    t=re.sub(r'\b43 manifiestos bilingües\b', '44 manifiestos bilingües', t, flags=re.I)
    t=re.sub(r'\b43 bilingual manifestos\b', '44 bilingual manifestos', t, flags=re.I)
    t=re.sub(r'\b43 manifiestos\b', '44 manifiestos', t, flags=re.I)
    t=re.sub(r'\b43 manifestos\b', '44 manifestos', t, flags=re.I)
    t=t.replace('diez oleadas', 'once oleadas').replace('ten waves', 'eleven waves')
    return t


def insert_after_xliii(path:Path, t:str):
    if XLIV in t:
        return t
    target=rel(path, 'manifiestos/'+XLIV)
    lines=t.splitlines()
    for i,line in enumerate(lines):
        if XLIII not in line:
            continue
        if line.lstrip().startswith('|'):
            cols=line.count('|')-1
            spanish=any(x in line for x in ['Incomprensión','Inteligencia Humana'])
            title='Neowar™ · Contra la Adicción a la Guerra y por la Justicia del Bien Común' if spanish else 'Neowar™ · Against War Addiction and for Common-Good Justice'
            func='Transformar el impulso guerrero en custodia, defensa limitada, memoria, justicia y soberanía compartida' if spanish else 'Transform warrior impulse into custodianship, bounded defence, memory, justice and shared sovereignty'
            row=f'| XLIV | [{title}]({target}) | {func} | [Issue #52]({ISSUE52}) |' if cols>=4 else f'| XLIV | [{title}]({target}) | {func} |'
            lines.insert(i+1,row); return '\n'.join(lines)+'\n'
        if re.match(r'^\s*43\.\s+\[',line):
            spanish='Incomprensión' in line
            title='Neowar™ · Contra la Adicción a la Guerra y por la Justicia del Bien Común' if spanish else 'Neowar™ · Against War Addiction and for Common-Good Justice'
            lines.insert(i+1,f'44. [{title}]({target})'); return '\n'.join(lines)+'\n'
        if line.lstrip().startswith(('* [','- [')):
            prefix='*' if line.lstrip().startswith('*') else '-'
            spanish='Incomprensión' in line or 'Inteligencia Humana' in line
            title='XLIV · Neowar™ · Contra la Adicción a la Guerra y por la Justicia del Bien Común' if spanish else 'XLIV · Neowar™ · Against War Addiction and for Common-Good Justice'
            lines.insert(i+1,f'{prefix} [{title}]({target})'); return '\n'.join(lines)+'\n'
    return t


def patch_readme_nav(path:Path,t:str):
    if '<!-- NEO_CURRENT_NAV_START -->' not in t:
        return t
    target=rel(path,'manifiestos/'+XLIV)
    latest_es=f'- Último manifiesto / Latest manifesto: [XLIV · Neowar™ · Contra la Adicción a la Guerra y por la Justicia del Bien Común / Against War Addiction and for Common-Good Justice]({target}).'
    t=re.sub(r'- Último manifiesto / Latest manifesto: .*?\n',latest_es+'\n',t)
    return t


def patch_manifest_index(p:Path,t:str):
    t=canonical_replace(t)
    t=t.replace('La colección se organiza desde el 8 de agosto de 2026 en diez oleadas relacionadas:', 'La colección se organiza desde el 8 de agosto de 2026 en once oleadas relacionadas:')
    tenth='* **Décima oleada · XLII–XLIII:** **Fin de la Era del Hombre Manipulado™ e Inteligencia Humana Expandida™**, orientada a soberanía cognitiva, despertar crítico y distinción entre IA capturada, sustitutiva y humano-expansiva bajo memoria, fuentes, contraste, revisión de pares y trazabilidad.'
    eleventh='* **Undécima oleada · XLIV:** **Neowar™**, orientada a transformar la energía guerrera en custodia, defensa limitada, memoria, justicia civilizatoria y soberanía compartida sin autorizar venganza privada, deshumanización ni violencia ilimitada.'
    if eleventh not in t and tenth in t: t=t.replace(tenth,tenth+'\n'+eleventh,1)
    if '* Neowar™' not in t:
        t=t.replace('* y Revisión de Pares Aumentada™ bajo criterio humano y fuentes trazables.', '* Revisión de Pares Aumentada™ bajo criterio humano y fuentes trazables;\n* Neowar™ como transformación del impulso guerrero en custodia y defensa limitada;\n* y soberanía compartida: cada persona gobierna su propia conciencia sin dominar la ajena.',1)
    t=t.replace('La décima oleada contiene **XLII–XLIII**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™.', 'La décima oleada contiene **XLII–XLIII**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™. La undécima oleada comienza con **XLIV · Neowar™**, fijado como versión 1.0 el 8 de agosto de 2026, y desarrolla custodia, memoria, justicia civilizatoria, defensa limitada y soberanía compartida.')
    t=t.replace('The tenth wave contains **XLII–XLIII**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™.', 'The tenth wave contains **XLII–XLIII**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™. The eleventh wave begins with **XLIV · Neowar™**, fixed as version 1.0 on 8 August 2026, and develops custodianship, memory, civilisational justice, bounded defence and shared sovereignty.')
    t=t.replace('XLIII · AGAINST THE REDUCTIVE MISUNDERSTANDING OF AI · HUMAN EXPANDED INTELLIGENCE\n        ↓\nI · NEO0™', 'XLIII · AGAINST THE REDUCTIVE MISUNDERSTANDING OF AI · HUMAN EXPANDED INTELLIGENCE\n        ↓\nXLIV · NEOWAR™ · AGAINST WAR ADDICTION AND FOR COMMON-GOOD JUSTICE\n        ↓\nI · NEO0™')
    t=t.replace('XLIII · CONTRA LA INCOMPRENSIÓN REDUCTIVA DE LA IA · INTELIGENCIA HUMANA EXPANDIDA\n        ↓\nI · NEO0™', 'XLIII · CONTRA LA INCOMPRENSIÓN REDUCTIVA DE LA IA · INTELIGENCIA HUMANA EXPANDIDA\n        ↓\nXLIV · NEOWAR™ · CONTRA LA ADICCIÓN A LA GUERRA Y POR LA JUSTICIA DEL BIEN COMÚN\n        ↓\nI · NEO0™')
    # Add dedicated Spanish and English wave sections if missing.
    essec='''\n## Undécima oleada · Neowar™, justicia civilizatoria y soberanía compartida\n\n| Nº | Manifiesto | Función | Síntesis Abierta |\n|---:|---|---|---|\n| XLIV | [Neowar™ · Contra la Adicción a la Guerra y por la Justicia del Bien Común](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) | Transformar el impulso guerrero en custodia, defensa limitada, memoria, justicia civilizatoria y soberanía compartida | [Issue #52](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/52) |\n\nNeowar™ no autoriza violencia privada ni amenazas contra personas: dirige la energía de defensa contra estructuras de tiranía, explotación, propaganda, impunidad y destrucción bajo necesidad, proporcionalidad, responsabilidad y cese.\n'''
    ensec='''\n## Eleventh wave · Neowar™, civilisational justice and shared sovereignty\n\n| No. | Manifesto | Function | Open Synthesis |\n|---:|---|---|---|\n| XLIV | [Neowar™ · Against War Addiction and for Common-Good Justice](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) | Transform warrior impulse into custodianship, bounded defence, memory, civilisational justice and shared sovereignty | [Issue #52](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/52) |\n\nNeowar™ does not authorise private violence or threats against persons: it directs defensive energy against structures of tyranny, exploitation, propaganda, impunity and destruction under necessity, proportionality, responsibility and cessation.\n'''
    if '## Undécima oleada · Neowar™' not in t:
        marker='\n---\n\n# EN · English'
        if marker in t: t=t.replace(marker,essec+marker,1)
    if '## Eleventh wave · Neowar™' not in t:
        marker='\n<!-- NEO_CURRENT_NAV_START -->'
        if marker in t: t=t.replace(marker,ensec+marker,1)
        else: t=t.rstrip()+ensec+'\n'
    return t


def patch_prev_nav():
    p=Path('manifiestos')/XLIII
    t=p.read_text(encoding='utf-8')
    t=t.replace('← [XLII · Fin de la Era del Hombre Manipulado™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [Índice](./README.md) · [I · Neo0™ · Soberanía de Guía Neodialéctica](./11_neo0_soberania_de_guia_ES_EN.md) →', '← [XLII · Fin de la Era del Hombre Manipulado™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [Índice](./README.md) · [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) →')
    t=t.replace('← [XLII · End of the Manipulated Human Era™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [Index](./README.md) · [I · Neo0™ · Neodialectical Guiding Sovereignty](./11_neo0_soberania_de_guia_ES_EN.md) →', '← [XLII · End of the Manipulated Human Era™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [Index](./README.md) · [XLIV · Neowar™](./44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md) →')
    p.write_text(t,encoding='utf-8')


def patch_synthesis():
    p=Path('propuestas/sintesis-abierta/README.md')
    if not p.exists(): return
    t=canonical_replace(p.read_text(encoding='utf-8'))
    if 'issues/52' not in t:
        line_es=f'* [XLIV · Neowar™ · Síntesis Abierta · Issue #52]({ISSUE52})'
        line_en=f'* [XLIV · Neowar™ · Open Synthesis · Issue #52]({ISSUE52})'
        # add near end in both-language neutral form
        t=t.rstrip()+f'\n\n## XLIV · Neowar™\n\n{line_es}\n{line_en}\n* [Manifiesto / Manifesto](../../manifiestos/{XLIV})\n'
    p.write_text(t,encoding='utf-8')


def validate():
    link_re=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
    root=ROOT.resolve(); checked=aliases=0; broken=[]
    files=[p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'node_modules' not in p.parts]
    for src in files:
        txt=src.read_text(encoding='utf-8')
        for raw in link_re.findall(txt):
            u=raw.strip().strip('<>')
            if not u or u.startswith(('http://','https://','mailto:','tel:','data:','#')): continue
            u=urllib.parse.unquote(u.split('#',1)[0].split('?',1)[0]); checked+=1
            cand=(ROOT/u.lstrip('/')).resolve() if u.startswith('/') else (src.parent/u).resolve()
            try: cand.relative_to(root)
            except ValueError: broken.append((str(src),raw)); continue
            if cand.exists(): continue
            if 'wiki-source' in src.parts and cand.with_suffix('.md').exists(): aliases+=1; continue
            broken.append((str(src),raw))
    if broken: raise SystemExit('Broken internal links: '+repr(broken[:30]))
    return len(files), len(list(ROOT.rglob('README.md'))), checked, aliases


def main():
    patch_prev_nav()
    patch_synthesis()
    for p in [Path('README.md'),Path('LEEME.md'),Path('PORTADA.md'),Path('COVER.md'),Path('wiki-source/Manifiestos.md')]:
        if not p.exists(): continue
        t=canonical_replace(p.read_text(encoding='utf-8'))
        t=insert_after_xliii(p,t)
        p.write_text(t,encoding='utf-8')
    p=Path('manifiestos/README.md'); p.write_text(patch_manifest_index(p,p.read_text(encoding='utf-8')),encoding='utf-8')
    p=Path('wiki-source/README.md')
    if p.exists():
        t=canonical_replace(p.read_text(encoding='utf-8'))
        t=t.replace('XLI → XLII → XLIII → I → II','XLII → XLIII → XLIV → I → II')
        t=re.sub(r'\* Último manifiesto / Latest manifesto:.*', '* Último manifiesto / Latest manifesto: [XLIV · Neowar™](../manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md)', t)
        p.write_text(t,encoding='utf-8')
    # all README canonical nav blocks
    for p in ROOT.rglob('README.md'):
        if '.git' in p.parts: continue
        t=canonical_replace(p.read_text(encoding='utf-8'))
        t=patch_readme_nav(p,t)
        p.write_text(t,encoding='utf-8')
    md,readmes,links,aliases=validate()
    report=Path('auditorias/publicas/2026-08-08_postcheck_XLIV_neowar_enlaces_readmes_ES_EN.md')
    report.write_text(f'''# Postcheck XLIV · Neowar™ · enlaces y READMEs\n## XLIV postcheck · Neowar™ · links and READMEs\n\n**Fecha / Date:** 2026-08-08  \n**Estado / Status:** OK\n\n- Markdown revisados / Markdown reviewed: **{md}**.\n- README revisados / README reviewed: **{readmes}**.\n- Enlaces internos relativos comprobados / Relative internal links checked: **{links}**.\n- Alias Wiki extensionless reconocidos / Extensionless Wiki aliases recognised: **{aliases}**.\n- Enlaces internos rotos / Broken internal links: **0**.\n- Estado de colección / Collection state: **I–XLIV · 44 manifiestos bilingües / bilingual manifestos · once oleadas / eleven waves**.\n- XLIV / Open Synthesis: **Issue #52**.\n\nLa publicación integra la fórmula de soberanía compartida: cada persona puede gobernar su propia conciencia; nadie recibe autoridad sobre la conciencia ajena. “Todos unidos / All united” se conserva como fórmula abierta de adhesión colectiva y no como atribución ficticia de firmas individuales.\n''',encoding='utf-8')
    # self-cleanup
    Path('.github/workflows/one-shot-publish-xliv-neowar.yml').unlink(missing_ok=True)
    Path('.github/triggers/publish-xliv-neowar.trigger').unlink(missing_ok=True)
    Path('.github/scripts/one_shot_publish_xliv_neowar.py').unlink(missing_ok=True)
    print('XLIV_OK',md,readmes,links,aliases)

if __name__=='__main__': main()
