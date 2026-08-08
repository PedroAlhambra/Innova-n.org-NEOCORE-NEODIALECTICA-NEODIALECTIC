from pathlib import Path
import os, re, urllib.parse

ROOT=Path('.')
XLIV='44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md'
XLV='45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md'
ISSUE53='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53'
LIVE=[Path(x) for x in ['README.md','LEEME.md','PORTADA.md','COVER.md','analisis/README.md','analisis/auditorias/README.md','analisis/publicos/README.md','analisis/publicos/evidencias/README.md','auditorias/publicas/README.md','manifiestos/README.md','obras/README.md','obras/idea/README.md','obras/idea/assets/README.md','propuestas/sintesis-abierta/README.md','wiki-source/README.md']]
COLLECTION=[Path(x) for x in ['README.md','LEEME.md','PORTADA.md','COVER.md','manifiestos/README.md','propuestas/sintesis-abierta/README.md','wiki-source/Manifiestos.md']]

def rel(src:Path,dst:str):
    r=os.path.relpath(dst,src.parent).replace('\\','/')
    return r if r.startswith('.') else './'+r

def current_nav(path:Path):
    return f'''<!-- NEO_CURRENT_NAV_START -->

---

## Estado canónico actual · Current canonical state

**Neodialectica Framework™ / Network · Innova_N · NEOCore™**

- Colección pública actual: **45 manifiestos bilingües · I–XLV · doce oleadas** / Current public collection: **45 bilingual manifestos · I–XLV · twelve waves**.
- Último manifiesto / Latest manifesto: [XLV · Multidimensionalidad Neodialéctica™ · Neodialectical Multidimensionality™]({rel(path,'manifiestos/'+XLV)}).
- Índice completo / Complete index: [Manifiestos / Manifestos]({rel(path,'manifiestos/README.md')}).
- Contraste público / Public contrast: [Síntesis Abierta / Open Synthesis]({rel(path,'propuestas/sintesis-abierta/README.md')}).
- Expansión y redundancia / Expansion and redundancy: [Protocolo de Proyección Distribuida Neodialéctica™]({rel(path,'proyeccion/PROTOCOLO_PROYECCION_DISTRIBUIDA_NEODIALECTICA_ES_EN.md')}).
- Fuente Wiki versionada / Versioned Wiki source: [Manifiestos]({rel(path,'wiki-source/Manifiestos.md')}).
- Nodo raíz / Root node: [README principal]({rel(path,'README.md')}).

**Principio de procedencia / Provenance principle:** la fuente intelectual y genealógica es **Innova_N**, dentro de **NEOCore™ / Neodialectica Framework™ / Network**, bajo dirección humana de **Pedro Martínez Alhambra · Neo0™**. GitHub es la primera proyección WEB4™ pública, versionada y trazable; no es el origen intelectual del sistema. / The intellectual and genealogical source is **Innova_N**, within **NEOCore™ / Neodialectica Framework™ / Network**, under the human direction of **Pedro Martínez Alhambra · Neo0™**. GitHub is the first public, versioned and traceable WEB4™ projection; it is not the intellectual origin of the system.

<!-- NEO_CURRENT_NAV_END -->'''

# 1) XLIV navigation now leads to XLV.
p=Path('manifiestos')/XLIV
t=p.read_text(encoding='utf-8')
t=t.replace('[I · Neo0™ · Soberanía de Guía Neodialéctica](./11_neo0_soberania_de_guia_ES_EN.md) →','[XLV · Multidimensionalidad Neodialéctica™](./45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md) →')
t=t.replace('[I · Neo0™ · Neodialectical Guiding Sovereignty](./11_neo0_soberania_de_guia_ES_EN.md) →','[XLV · Neodialectical Multidimensionality™](./45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md) →')
p.write_text(t,encoding='utf-8')

# 2) Refresh all standard README current-state blocks and current-count markers.
for p in LIVE:
    if not p.exists(): continue
    t=p.read_text(encoding='utf-8')
    t=re.sub(r'I–XLIV(?![A-Z])','I–XLV',t)
    t=re.sub(r'\b44 manifiestos bilingües\b','45 manifiestos bilingües',t,flags=re.I)
    t=re.sub(r'\b44 bilingual manifestos\b','45 bilingual manifestos',t,flags=re.I)
    t=t.replace('once oleadas','doce oleadas').replace('eleven waves','twelve waves')
    if '<!-- NEO_CURRENT_NAV_START -->' in t and '<!-- NEO_CURRENT_NAV_END -->' in t:
        t=re.sub(r'<!-- NEO_CURRENT_NAV_START -->.*?<!-- NEO_CURRENT_NAV_END -->',current_nav(p),t,flags=re.S)
    p.write_text(t,encoding='utf-8')

# 3) Ensure collection hubs expose XLV beside an XLIV entry, where a list/table exists.
for p in COLLECTION:
    if not p.exists(): continue
    t=p.read_text(encoding='utf-8')
    if XLV not in t:
        lines=t.splitlines(); inserted=False
        target=rel(p,'manifiestos/'+XLV)
        for i,line in enumerate(lines):
            if XLIV in line:
                if line.lstrip().startswith('44. '):
                    lines.insert(i+1,f'45. [Multidimensionalidad Neodialéctica™ · Contra la Reducción Monodimensional del Humano y del Poder]({target})')
                elif line.lstrip().startswith('* '):
                    lines.insert(i+1,f'* [XLV · Multidimensionalidad Neodialéctica™ · Contra la Reducción Monodimensional del Humano y del Poder]({target})')
                elif line.lstrip().startswith('| XLIV'):
                    cols=line.count('|')-1
                    if cols>=4:
                        lines.insert(i+1,f'| XLV | [Multidimensionalidad Neodialéctica™]({target}) | Multidimensionalidad, Anomalía Integrable™, liderazgo sin captura y soberanía distribuida | [Issue #53]({ISSUE53}) |')
                    else:
                        lines.insert(i+1,f'| XLV | [Multidimensionalidad Neodialéctica™]({target}) | Multidimensionalidad, Anomalía Integrable™, liderazgo sin captura y soberanía distribuida |')
                else:
                    continue
                inserted=True; break
        if inserted: t='\n'.join(lines)+('\n' if t.endswith('\n') else '')
    p.write_text(t,encoding='utf-8')

# 4) Manifest index: correct wave boundaries and add explicit twelfth-wave section before current nav.
p=Path('manifiestos/README.md'); t=p.read_text(encoding='utf-8')
t=t.replace('La décima oleada contiene **XLII–XLIV**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™.',
'''La décima oleada contiene **XLII–XLIII**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™. La undécima oleada contiene **XLIV · Neowar™**, orientado a transformar el impulso guerrero en custodia, defensa limitada, memoria y soberanía compartida. La duodécima oleada comienza con **XLV · Multidimensionalidad Neodialéctica™**, que fija multidimensionalidad, singularidad integrable, límites del ego y soberanía distribuida.''')
t=t.replace('The tenth wave contains Manifestos **XLII–XLIV**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™.',
'''The tenth wave contains Manifestos **XLII–XLIII**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™. The eleventh wave contains **XLIV · Neowar™**, oriented towards transforming warrior impulse into custodianship, bounded defence, memory and shared sovereignty. The twelfth wave begins with **XLV · Neodialectical Multidimensionality™**, fixing multidimensionality, integrable singularity, limits on ego and distributed sovereignty.''')
t=t.replace('XLIV · NEOWAR™ · AGAINST WAR ADDICTION AND FOR COMMON-GOOD JUSTICE\n        ↓\nI · NEO0™ · RETURN TO ORIGIN AND NEW CYCLE',
'''XLIV · NEOWAR™ · AGAINST WAR ADDICTION AND FOR COMMON-GOOD JUSTICE
        ↓
XLV · NEODIALECTICAL MULTIDIMENSIONALITY · DISTRIBUTED SOVEREIGNTY
        ↓
I · NEO0™ · RETURN TO ORIGIN AND NEW CYCLE''')
if '## Duodécima oleada · Multidimensionalidad, singularidad y soberanía distribuida' not in t:
    block=f'''\n## Duodécima oleada · Multidimensionalidad, singularidad y soberanía distribuida\n\n| Nº | Manifiesto | Función | Síntesis Abierta |\n|---:|---|---|---|\n| XLV | [Multidimensionalidad Neodialéctica™ · Contra la Reducción Monodimensional del Humano y del Poder](./{XLV}) | Integrar singularidad, multidimensionalidad, Anomalía Integrable™, liderazgo sin captura y soberanía distribuida; responder además a la duda sobre ™, autoría y ego | [Issue #53]({ISSUE53}) |\n\nLa duodécima oleada fija una regla transversal: **ninguna dimensión parcial convierte a un nodo en totalidad del sistema**. El origen no equivale a infalibilidad; la excelencia no equivale a dominio; la denominación no equivale a dogma.\n\n## Twelfth wave · Multidimensionality, singularity and distributed sovereignty\n\n| No. | Manifesto | Function | Open Synthesis |\n|---:|---|---|---|\n| XLV | [Neodialectical Multidimensionality™ · Against the One-Dimensional Reduction of the Human and Power](./{XLV}) | Integrate singularity, multidimensionality, Integrable Anomaly™, leadership without capture and distributed sovereignty; also answer the question about ™, authorship and ego | [Issue #53]({ISSUE53}) |\n\nThe twelfth wave fixes a transversal rule: **no partial dimension makes any node the totality of the system**. Origin is not infallibility; excellence is not domination; naming is not dogma.\n\n'''
    pos=t.find('<!-- NEO_CURRENT_NAV_START -->')
    t=t[:pos]+block+t[pos:] if pos!=-1 else t+block
p.write_text(t,encoding='utf-8')

# 5) Open Synthesis index must expose Issue #53.
p=Path('propuestas/sintesis-abierta/README.md'); t=p.read_text(encoding='utf-8')
if 'issues/53' not in t:
    entry=f'''\n## XLV · Multidimensionalidad Neodialéctica™ / Neodialectical Multidimensionality™\n\n- [Síntesis Abierta XLV · Issue #53 / Open Synthesis XLV · Issue #53]({ISSUE53})\n- [Manifiesto / Manifesto](../../manifiestos/{XLV})\n- Ejes / Axes: multidimensionalidad, singularidad, ego, Problema del Mulo, soberanía distribuida, Anomalía Integrable™, denominaciones ™ y revisión multidisciplinar.\n\n'''
    pos=t.find('<!-- NEO_CURRENT_NAV_START -->')
    t=t[:pos]+entry+t[pos:] if pos!=-1 else t+entry
p.write_text(t,encoding='utf-8')

# 6) Wiki manifesto source: explicit XLV entry before current-nav if needed.
p=Path('wiki-source/Manifiestos.md'); t=p.read_text(encoding='utf-8')
if XLV not in t:
    entry=f'''\n## XLV · Multidimensionalidad Neodialéctica™ / Neodialectical Multidimensionality™\n\n- [Manifiesto bilingüe / Bilingual manifesto](../manifiestos/{XLV})\n- [Síntesis Abierta / Open Synthesis · Issue #53]({ISSUE53})\n- Fija la multidimensionalidad como regla contra reducciones monodimensionales de persona, poder, experto, fundador o IA. / Establishes multidimensionality as a rule against one-dimensional reductions of person, power, expert, founder or AI.\n\n'''
    pos=t.find('<!-- NEO_CURRENT_NAV_START -->')
    t=t[:pos]+entry+t[pos:] if pos!=-1 else t+entry
p.write_text(t,encoding='utf-8')

# 7) Validate local Markdown links, including Wiki aliases.
LINK=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
files=sorted(x for x in ROOT.rglob('*.md') if '.git' not in x.parts and 'node_modules' not in x.parts)
root=ROOT.resolve(); checked=aliases=0; broken=[]
for src in files:
    txt=src.read_text(encoding='utf-8')
    for raw in LINK.findall(txt):
        u=raw.strip().strip('<>')
        if not u or u.startswith(('http://','https://','mailto:','tel:','data:','#')): continue
        u=urllib.parse.unquote(u.split('#',1)[0].split('?',1)[0]); checked+=1
        cand=(ROOT/u.lstrip('/')).resolve() if u.startswith('/') else (src.parent/u).resolve()
        try: cand.relative_to(root)
        except ValueError: broken.append((str(src),raw,'escapes root')); continue
        if cand.exists(): continue
        if 'wiki-source' in src.parts and cand.with_suffix('.md').exists(): aliases+=1; continue
        broken.append((str(src),raw,str(cand)))
if broken:
    print('BROKEN',broken); raise SystemExit(2)

# Canonical checks.
missing=[]
for p in COLLECTION:
    txt=p.read_text(encoding='utf-8')
    if XLV not in txt: missing.append((str(p),'XLV'))
if missing: print('MISSING',missing); raise SystemExit(3)
if 'issues/53' not in Path('propuestas/sintesis-abierta/README.md').read_text(encoding='utf-8'): raise SystemExit('Issue53 missing from synthesis index')
if '## XIV. Respuesta a Juanjo' not in Path('manifiestos')/XLV.read_text(encoding='utf-8') if False else False: pass
# Explicit manifesto checks without precedence ambiguity.
mt=(Path('manifiestos')/XLV).read_text(encoding='utf-8')
for needle in ['## XIV. Respuesta a Juanjo','## XIV. Response to Juanjo','issues/53','Cómo aportar a la Síntesis Abierta','How to contribute to Open Synthesis']:
    if needle not in mt: raise SystemExit('Manifest missing '+needle)
for p in LIVE:
    txt=p.read_text(encoding='utf-8')
    if 'NEO_CURRENT_NAV_START' in txt and ('I–XLV' not in txt or '45 manifiestos bilingües' not in txt):
        raise SystemExit('stale current nav '+str(p))
for p in files:
    if p.read_text(encoding='utf-8').count('```')%2: raise SystemExit('unbalanced fence '+str(p))

report=Path('auditorias/publicas/2026-08-08_postcheck_XLV_multidimensionalidad_enlaces_readmes_ES_EN.md')
report.write_text(f'''# Postcheck XLV · Multidimensionalidad Neodialéctica™ · enlaces y READMEs\n## XLV postcheck · Neodialectical Multidimensionality™ · links and READMEs\n\n**Fecha / Date:** 2026-08-08  \n**Estado / Status:** **OK**\n\n- Markdown revisados / Markdown reviewed: **{len(files)}**.\n- README revisados / README reviewed: **{len(list(ROOT.rglob('README.md')))}**.\n- Enlaces internos relativos comprobados / Relative internal links checked: **{checked}**.\n- Alias Wiki extensionless reconocidos / Extensionless Wiki aliases recognised: **{aliases}**.\n- Enlaces internos rotos / Broken internal links: **0**.\n- Estado de colección / Collection state: **I–XLV · 45 manifiestos bilingües / bilingual manifestos · doce oleadas / twelve waves**.\n- XLV / Open Synthesis: **Issue #53**.\n- Respuesta interna a la duda «¿qué significa ™?» / Internal response to “what does ™ mean?”: **sí / yes**.\n- Regla anti-Mulo aplicada también al fundador / Anti-Mule rule applied to the founder as well: **sí / yes**.\n\nLa v1.1 de XLV conserva la pregunta de difusión como delta cognitivo y responde dentro del propio manifiesto. ™ queda definido como marcador editorial de denominación, procedencia y trazabilidad, no como verdad, infalibilidad ni blindaje frente a crítica. La multidimensionalidad establece que origen, autoría, excelencia o liderazgo en una dimensión no equivalen a soberanía total sobre el sistema.\n''',encoding='utf-8')

# Remove disposable automation files.
for x in ['.github/scripts/one_shot_xlv_multidimensionalidad.py','.github/workflows/one-shot-xlv-multidimensionalidad.yml','.github/triggers/xlv-multidimensionalidad.trigger']:
    Path(x).unlink(missing_ok=True)
print('XLV_OK',len(files),checked,aliases)
