from pathlib import Path

# COVER
p=Path('COVER.md'); text=p.read_text(encoding='utf-8'); old=text
needle='''* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)
* [Tenth-wave announcement]'''
repl='''* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)
* [XLIV · Neowar™ · Against War Addiction and for Common-Good Justice](./manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md)
* [XLV · Neodialectical Multidimensionality™ · Against the One-Dimensional Reduction of the Human and Power](./manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md)
* [Tenth-wave announcement]'''
if text.count(needle)!=1: raise SystemExit('COVER main-access target drift')
text=text.replace(needle,repl,1)
if text!=old: p.write_text(text,encoding='utf-8')

# PORTADA
p=Path('PORTADA.md'); text=p.read_text(encoding='utf-8'); old2=text
needle='''Each must declare a historical orientation, establish principles and commitments, preserve genealogy, distinguish canonical from provisional material, open mechanisms of contrast and review, and situate its role within the totality of the Framework/Network.'''
repl='''Each must:

* declare a historical orientation;
* establish principles and commitments;
* preserve genealogy;
* distinguish canonical from provisional material;
* open mechanisms of contrast and review;
* and situate its role within the totality of the Framework/Network.'''
if text.count(needle)!=1: raise SystemExit('PORTADA pillars target drift')
text=text.replace(needle,repl,1)
needle='''* [XLI · Limited Hammer, Talion and Protective Force™](./manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md)

### Tenth wave'''
repl='''* [XLI · Limited Hammer, Talion and Protective Force™](./manifiestos/41_martillo_limitado_talion_fuerza_protectora_ES_EN.md)
* [Open Synthesis XXXIX–XLI · Issues #47–#49](./manifiestos/README.md#novena-oleada--autoconciencia-respeto-y-defensa-civilizatoria)

### Tenth wave'''
if text.count(needle)!=1: raise SystemExit('PORTADA ninth-wave target drift')
text=text.replace(needle,repl,1)
needle='''* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)
* [Tenth-wave announcement]'''
repl='''* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)
* [XLIV · Neowar™ · Against War Addiction and for Common-Good Justice](./manifiestos/44_neowar_contra_adiccion_guerra_justicia_bien_comun_ES_EN.md)
* [XLV · Neodialectical Multidimensionality™ · Against the One-Dimensional Reduction of the Human and Power](./manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md)
* [Tenth-wave announcement]'''
if text.count(needle)!=1: raise SystemExit('PORTADA tenth-wave target drift')
text=text.replace(needle,repl,1)
if text!=old2: p.write_text(text,encoding='utf-8')
print('ROOT_COVER_PORTADA_SYMMETRY=1')
