from pathlib import Path
import re

ROOT=Path('.').resolve()
M=ROOT/'manifiestos/README.md'
LI=ROOT/'manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md'
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'

changed=[]

def write(p,t,old):
    if t!=old:
        p.write_text(t,encoding='utf-8'); changed.append(p.relative_to(ROOT).as_posix())

# Canonical README: complete 19-wave architecture and explicit LII wave tables.
old=M.read_text(encoding='utf-8'); t=old
es18='18. **LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™:** accesibilidad institucional, inteligencia cívica distribuida, formación pública no capturante y revisión democrática de funciones públicas.'
es19='19. **LII · Ciudadanía Humana Neodialéctica™:** igualdad de pertenencia, ciudadanía multiescala, protección universal y transición desde sangre/suelo hacia pertenencia cívica funcional.'
if es19 not in t and es18 in t: t=t.replace(es18,es18+'\n'+es19,1)
en18='18. **LI · Open Synthesis as Complementary or Substitutive Civic Power™:** institutional accessibility, distributed civic intelligence, non-capturing public formation and democratic review of public functions.'
en19='19. **LII · Neodialectical Human Citizenship™:** equality of belonging, multiscale citizenship, universal protection and transition from blood/soil toward functional civic belonging.'
if en19 not in t and en18 in t: t=t.replace(en18,en18+'\n'+en19,1)

es_sec='''\n## Decimonovena oleada · Ciudadanía humana y pertenencia multiescala · LII

| Nº | Manifiesto | Función | Síntesis Abierta |
|---:|---|---|---|
| LII | [Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) | Igualdad de pertenencia, ciudadanía multiescala, protección universal y pertenencia cívica funcional | [#64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64) |
\n'''
if '## Decimonovena oleada · Ciudadanía humana y pertenencia multiescala · LII' not in t:
    anchor='\n## Relación entre principios y trabajo aplicado'
    if anchor in t: t=t.replace(anchor,'\n'+es_sec+anchor,1)

en_sec='''\n## Nineteenth wave · Human citizenship and multiscale belonging · LII

| No. | Manifesto | Function | Open Synthesis |
|---:|---|---|---|
| LII | [Neodialectical Human Citizenship™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) | Equality of belonging, multiscale citizenship, universal protection and functional civic belonging | [#64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64) |
\n'''
if '## Nineteenth wave · Human citizenship and multiscale belonging · LII' not in t:
    anchor='\n## Relation between principles and applied work'
    if anchor in t: t=t.replace(anchor,'\n'+en_sec+anchor,1)

t=re.sub(r'- Último manifiesto / Latest manifesto: \[LI · Síntesis Abierta como Poder Cívico Complementario o Sustitutivo™\]\([^\n]+\)', '- Último manifiesto / Latest manifesto: [LII · Ciudadanía Humana Neodialéctica™](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)', t)
write(M,t,old)

# LI must point forward to LII in the managed canonical navigation.
old=LI.read_text(encoding='utf-8'); t=old
nav='''<!-- NEO_MANIFESTO_NAV_START -->

## Navegación canónica / Canonical navigation

← **L** · [Por una Inteligencia Compartida, no Única™ · Invitación Abierta a las IAs / For Shared, Not Singular Intelligence™](50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)
· [Índice I–LII / I–LII index](README.md) ·
**LII** · [Ciudadanía Humana Neodialéctica™ · de la sangre y el suelo a la pertenencia cívica funcional / Neodialectical Human Citizenship™ · from blood and soil to functional civic belonging](52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md) →

> La navegación canónica mantiene la colección conectada sin convertir ningún manifiesto aislado en equivalente del marco completo. / Canonical navigation keeps the collection connected without treating any single manifesto as equivalent to the complete framework.

<!-- NEO_MANIFESTO_NAV_END -->'''
t=re.sub(r'<!-- NEO_MANIFESTO_NAV_START -->.*?<!-- NEO_MANIFESTO_NAV_END -->',nav,t,flags=re.S)
write(LI,t,old)

# Transversal relation map: current coverage and explicit LII relation.
old=REL.read_text(encoding='utf-8'); t=old
t=t.replace('**Cobertura / Coverage:** I–LI · 51 manifiestos / 51 manifestos','**Cobertura / Coverage:** I–LII · 52 manifiestos / 52 manifestos')
t=t.replace('## Matriz completa I–LI / Complete I–LI matrix','## Matriz completa I–LII / Complete I–LII matrix')
if '## LII · Ciudadanía Humana Neodialéctica™ · relación aplicada' not in t:
    t += '''\n\n## LII · Ciudadanía Humana Neodialéctica™ · relación aplicada
## LII · Neodialectical Human Citizenship™ · applied relation

**Relaciones genealógicas principales / Main genealogical relations:** II · Síntesis Abierta / Open Synthesis; III · Derecho Humano de Aporte / Human Right to Contribute; IV · Bien Común / Common Good; IX · Memoria, Genealogía y Trazabilidad / Memory, Genealogy and Traceability; XXXVII · Neofraternidad™; XLIX · Interoperabilidad Cultural™ / Cultural Interoperability; LI · Poder Cívico Complementario o Sustitutivo™ / Complementary or Substitutive Civic Power.

- [Manifiesto LII / Manifesto LII](./52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md)
- [Análisis público / Public analysis](../analisis/publicos/2026-08-08_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_funcional_ES_EN.md)
- [Síntesis Abierta #64 / Open Synthesis #64](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/64)

**Regla de relación / Relation rule:** igualdad humana universal no elimina administración territorial; aporte no equivale a riqueza; pertenencia funcional no puede convertirse en filtro de valor humano. / Universal human equality does not erase territorial administration; contribution is not equivalent to wealth; functional belonging must not become a filter of human worth.
'''
write(REL,t,old)

# Verify current-state README/LEEME blocks.
fail=[]
for p in sorted({x for x in ROOT.rglob('README*.md') if '.git' not in x.parts}|{ROOT/'LEEME.md'}):
    if not p.exists(): continue
    s=p.read_text(encoding='utf-8')
    if '<!-- NEO_LATEST_MANIFESTO_START -->' in s:
        m=re.search(r'<!-- NEO_LATEST_MANIFESTO_START -->(.*?)<!-- NEO_LATEST_MANIFESTO_END -->',s,re.S)
        if not m or 'LII · Ciudadanía Humana Neodialéctica™' not in m.group(1) or 'issues/64' not in m.group(1): fail.append(f'{p.relative_to(ROOT)} latest')
    if '<!-- MANIFESTOS_CURRENT_START -->' in s and 'I–LII · 52 manifiestos bilingües / 52 bilingual manifestos' not in s: fail.append(f'{p.relative_to(ROOT)} current-count')
    if '<!-- NEO_ALL_MANIFESTOS_START -->' in s:
        b=re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->',s,re.S)
        if not b or '- **LII** ·' not in b.group(1) or 'I–LII · 52 manifiestos / 52 manifestos' not in b.group(1): fail.append(f'{p.relative_to(ROOT)} network')

ms=M.read_text(encoding='utf-8')
for needle in [es19,en19,'## Decimonovena oleada · Ciudadanía humana y pertenencia multiescala · LII','## Nineteenth wave · Human citizenship and multiscale belonging · LII']:
    if needle not in ms: fail.append('manifiestos/README.md missing '+needle[:40])
if 'I–LII / I–LII index' not in LI.read_text(encoding='utf-8') or '52_ciudadania_humana' not in LI.read_text(encoding='utf-8'): fail.append('LI navigation')

print('FILES_CHANGED',len(changed))
for p in changed: print('CHANGED',p)
if fail:
    print('POSTCHECK FAIL')
    for x in fail: print(x)
    raise SystemExit(1)
print('POSTCHECK OK: LII / 52 manifestos / 19 waves synchronized; LI↔LII navigation and relation map verified')
