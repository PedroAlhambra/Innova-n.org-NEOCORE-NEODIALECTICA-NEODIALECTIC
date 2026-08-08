from pathlib import Path
import os,re

ROOT=Path('.').resolve()
MANIFESTO=Path('manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md')
ISSUE='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64'
TITLE_ES='LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional'
TITLE_EN='LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging'

TARGETS=[]
for p in ROOT.rglob('README.md'):
    if '.git' not in p.parts:
        TARGETS.append(p)
for rel in ['LEEME.md','analisis/INDEX.md','wiki-source/Manifiestos.md','manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md']:
    p=ROOT/rel
    if p.exists(): TARGETS.append(p)
for p in (ROOT/'.github/scripts').glob('*.py'):
    TARGETS.append(p)


def rel(doc:Path,target:Path)->str:
    return os.path.relpath(ROOT/target, doc.parent).replace('\\','/')


def latest_block(doc:Path)->str:
    m=rel(doc,MANIFESTO)
    contrib=rel(doc,Path('propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'))
    synth=rel(doc,Path('propuestas/sintesis-abierta/README.md'))
    idx=rel(doc,Path('manifiestos/README.md'))
    return f'''<!-- NEO_LATEST_MANIFESTO_START -->

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional**  
> **LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging**
>
> La propuesta está **abierta a crítica, objeciones, contraejemplos, fuentes, correcciones y propuestas de mejora**. No se pide adhesión: se pide contraste. / The proposal is **open to criticism, objections, counterexamples, sources, corrections and improvement proposals**. Endorsement is not required: scrutiny is.
>
> **[Leer manifiesto LII / Read manifesto LII](../../manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) · [Participar en la Síntesis Abierta LII · Issue #64 / Join Open Synthesis LII · Issue #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64)**  
> [Cómo aportar / How to contribute](../../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md) · [Índice de Síntesis Abierta / Open Synthesis index](../../propuestas/sintesis-abierta/README.md) · [52 manifiestos I–LII / 52 manifestos I–LII](../../manifiestos/README.md)

<!-- NEO_LATEST_MANIFESTO_END -->'''


def current_block(doc:Path)->str:
    idx=rel(doc,Path('manifiestos/README.md'))
    return f'''<!-- MANIFESTOS_CURRENT_START -->

**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:** **I–LII · 52 manifiestos bilingües / 52 bilingual manifestos** · [índice canónico / canonical index](../../manifiestos/README.md)

<!-- MANIFESTOS_CURRENT_END -->'''


def sync_all_block(text:str,doc:Path)->str:
    pat=re.compile(r'<!-- NEO_ALL_MANIFESTOS_START -->.*?<!-- NEO_ALL_MANIFESTOS_END -->',re.S)
    ma=pat.search(text)
    if not ma: return text
    b=ma.group(0)
    reps={
      '52 manifiestos bilingües · I–LII · 19 oleadas':'52 manifiestos bilingües · I–LII · 19 oleadas',
      '52 bilingual manifestos · I–LII · 19 waves':'52 bilingual manifestos · I–LII · 19 waves',
      'I–LII · 52 manifiestos / 52 manifestos':'I–LII · 52 manifiestos / 52 manifestos',
      'mantiene los 51 manifiestos':'mantiene los 52 manifiestos',
      'keeps all 51 manifestos':'keeps all 52 manifestos',
    }
    for a,z in reps.items(): b=b.replace(a,z)
    if '- **LII** ·' not in b:
        link=rel(doc,MANIFESTO)
        line=f'- **LII** · [Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional / Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging]({link})'
        li=list(re.finditer(r'^- \*\*LI\*\* · .*$',b,re.M))
        if li:
            x=li[-1]
            b=b[:x.end()]+'\n'+line+b[x.end():]
        else:
            b=b.replace('\n</details>',f'\n{line}\n\n</details>',1)
    return text[:ma.start()]+b+text[ma.end():]


def add_citizenship_block(text:str,doc:Path)->str:
    if doc.relative_to(ROOT).as_posix() not in {'analisis/README.md','analisis/publicos/README.md','analisis/INDEX.md','propuestas/sintesis-abierta/README.md'}:
        return text
    marker='<!-- NEO_CITIZENSHIP_LII_START -->'
    if marker in text: return text
    analysis=rel(doc,Path('analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md'))
    manifesto=rel(doc,MANIFESTO)
    block=f'''\n\n<!-- NEO_CITIZENSHIP_LII_START -->
> ## 🟠 LII · CIUDADANÍA HUMANA NEODIALÉCTICA™ / NEODIALECTICAL HUMAN CITIZENSHIP™
> Sangre = genealogía. Suelo = localización y vínculo. Dignidad humana = común. La propuesta abre una transición hacia pertenencia cívica funcional y multiescala sin confundir igualdad humana con ausencia de administración territorial.  
> [Manifiesto LII / Manifesto LII]({manifesto}) · [Análisis / Analysis]({analysis}) · [Síntesis Abierta #64 / Open Synthesis #64]({ISSUE})
<!-- NEO_CITIZENSHIP_LII_END -->\n'''
    # after first heading block, before existing feature markers if possible
    pos=text.find('<!-- NEO_')
    if pos>=0: return text[:pos]+block+'\n'+text[pos:]
    first_nl=text.find('\n')
    return text[:first_nl+1]+block+text[first_nl+1:]


def sync_canonical_readme(text:str)->str:
    if '## Arquitectura actual · 18 oleadas' in text:
        text=text.replace('## Arquitectura actual · 18 oleadas','## Arquitectura actual · 19 oleadas')
    if '## Current architecture · 18 waves' in text:
        text=text.replace('## Current architecture · 18 waves','## Current architecture · 19 waves')
    es19='19. **LII · Ciudadanía Humana Neodialéctica™:** igualdad de pertenencia, ciudadanía multiescala, protección universal y transición desde sangre/suelo hacia pertenencia cívica funcional.'
    if es19 not in text and '18. **LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™:' in text:
        text=text.replace('18. **LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™: accesibilidad institucional, inteligencia cívica distribuida, formación pública no capturante y revisión democrática de funciones públicas.','18. **LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™:** accesibilidad institucional, inteligencia cívica distribuida, formación pública no capturante y revisión democrática de funciones públicas.\n'+es19)
    en19='19. **LII · Neodialectical Human Citizenship™:** equality of belonging, multiscale citizenship, universal protection and transition from blood/soil toward functional civic belonging.'
    if en19 not in text and '18. **LI · Open Synthesis as Complementary or Substitutive Civic Power™:' in text:
        text=text.replace('18. **LI · Open Synthesis as Complementary or Substitutive Civic Power™: institutional accessibility, distributed civic intelligence, non-capturing public formation and democratic review of public functions.','18. **LI · Open Synthesis as Complementary or Substitutive Civic Power™:** institutional accessibility, distributed civic intelligence, non-capturing public formation and democratic review of public functions.\n'+en19)
    if '## Decimonovena oleada · Ciudadanía humana y pertenencia multiescala · LII' not in text:
        sec='''\n\n## Decimonovena oleada · Ciudadanía humana y pertenencia multiescala · LII

| Nº | Manifiesto | Función | Síntesis Abierta |
|---:|---|---|---|
| LII | [Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) | Igualdad de pertenencia, ciudadanía multiescala, protección universal y pertenencia cívica funcional | [#64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64) |
'''
        pos=text.find('\n## Relación entre principios y trabajo aplicado')
        if pos>=0: text=text[:pos]+sec+text[pos:]
    if '## Nineteenth wave · Human citizenship and multiscale belonging · LII' not in text:
        sec='''\n\n## Nineteenth wave · Human citizenship and multiscale belonging · LII

| No. | Manifesto | Function | Open Synthesis |
|---:|---|---|---|
| LII | [Neodialectical Human Citizenship™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) | Equality of belonging, multiscale citizenship, universal protection and functional civic belonging | [#64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64) |
'''
        pos=text.find('\n## Relation between principles and applied work')
        if pos>=0: text=text[:pos]+sec+text[pos:]
    # canonical navigation
    text=re.sub(r'- Último manifiesto / Latest manifesto: \[LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™\]\([^\n]+\)', '- Último manifiesto / Latest manifesto: [LII · Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)', text)
    return text


def add_relation_block(text:str)->str:
    if 'LII · Ciudadanía Humana Neodialéctica™ · relación aplicada' in text: return text
    return text+'''\n\n## LII · Ciudadanía Humana Neodialéctica™ · relación aplicada
## LII · Neodialectical Human Citizenship™ · applied relation

**Relaciones genealógicas principales:** II · Síntesis Abierta; III · Derecho Humano de Aporte; IV · Bien Común; IX · Memoria, Genealogía y Trazabilidad; XXXVII · Neofraternidad™; XLIX · Interoperabilidad Cultural™; LI · Poder Cívico Complementario o Sustitutivo™.  
**Main genealogical relations:** II · Open Synthesis; III · Human Right to Contribute; IV · Common Good; IX · Memory, Genealogy and Traceability; XXXVII · Neofraternity™; XLIX · Cultural Interoperability™; LI · Complementary or Substitutive Civic Power™.

- [Manifiesto LII / Manifesto LII](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)
- [Análisis público / Public analysis](../analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md)
- [Síntesis Abierta #64 / Open Synthesis #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64)

**Regla de relación:** igualdad humana universal no elimina administración territorial; aporte no equivale a riqueza; pertenencia funcional no puede convertirse en filtro de valor humano. / **Relation rule:** universal human equality does not erase territorial administration; contribution is not equivalent to wealth; functional belonging must not become a filter of human worth.
'''

changed=[]
for p in dict.fromkeys(TARGETS):
    old=p.read_text(encoding='utf-8')
    t=old
    if '<!-- NEO_LATEST_MANIFESTO_START -->

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional**  
> **LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging**
>
> La propuesta está **abierta a crítica, objeciones, contraejemplos, fuentes, correcciones y propuestas de mejora**. No se pide adhesión: se pide contraste. / The proposal is **open to criticism, objections, counterexamples, sources, corrections and improvement proposals**. Endorsement is not required: scrutiny is.
>
> **[Leer manifiesto LII / Read manifesto LII](../../manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) · [Participar en la Síntesis Abierta LII · Issue #64 / Join Open Synthesis LII · Issue #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64)**  
> [Cómo aportar / How to contribute](../../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md) · [Índice de Síntesis Abierta / Open Synthesis index](../../propuestas/sintesis-abierta/README.md) · [52 manifiestos I–LII / 52 manifestos I–LII](../../manifiestos/README.md)

<!-- NEO_LATEST_MANIFESTO_END -->',latest_block(p),t,flags=re.S)
    if '<!-- MANIFESTOS_CURRENT_START -->

**Manifiestos de la Filosofía Arquetípica Neodialéctica™ / Manifestos of Archetypal Neodialectical Philosophy™:** **I–LII · 52 manifiestos bilingües / 52 bilingual manifestos** · [índice canónico / canonical index](../../manifiestos/README.md)

<!-- MANIFESTOS_CURRENT_END -->',current_block(p),t,flags=re.S)
    t=sync_all_block(t,p)
    exact={
      '52 manifiestos bilingües · I–LII · 19 oleadas':'52 manifiestos bilingües · I–LII · 19 oleadas',
      '52 bilingual manifestos · I–LII · 19 waves':'52 bilingual manifestos · I–LII · 19 waves',
      'I–LII · 52 manifiestos bilingües / 52 bilingual manifestos':'I–LII · 52 manifiestos bilingües / 52 bilingual manifestos',
      'I–LII · 52 manifiestos / 52 manifestos':'I–LII · 52 manifiestos / 52 manifestos',
      '52 manifiestos I–LII / 52 manifestos I–LII':'52 manifiestos I–LII / 52 manifestos I–LII',
    }
    for a,z in exact.items(): t=t.replace(a,z)
    t=add_citizenship_block(t,p)
    rp=p.relative_to(ROOT).as_posix()
    if rp=='manifiestos/README.md': t=sync_canonical_readme(t)
    if rp=='manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md': t=add_relation_block(t)
    # keep persistent synchronizers current
    if rp=='.github/scripts/sync_latest_manifesto_feature.py':
        t=t.replace('51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md','52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md')
        t=t.replace('Issue #59','Issue #64').replace('/issues/59','/issues/64')
        t=t.replace('LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™','LII · Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional')
        t=t.replace('LI · Open Synthesis as Complementary or Substitutive Civic Power™','LII · Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging')
    if t!=old:
        p.write_text(t,encoding='utf-8')
        changed.append(rp)

print('UPDATED',len(changed))
for x in changed: print(x)
