from pathlib import Path

# Fix accidental Roman-numeral expansion in current documentation.
for rel in [
    'README.md','LEEME.md','PORTADA.md','COVER.md','manifiestos/README.md',
    'propuestas/sintesis-abierta/README.md','wiki-source/Manifiestos.md'
]:
    p=Path(rel)
    t=p.read_text(encoding='utf-8')
    t=t.replace('XLIIII','XLIII')
    p.write_text(t,encoding='utf-8')

# Complete manifesto index wording for tenth wave and functions.
p=Path('manifiestos/README.md')
t=p.read_text(encoding='utf-8')
t=t.replace(
'* **Tenth wave · XLII:** **End of the Manipulated Human Era™**, focused on cognitive sovereignty, critical awakening and AI as a bifurcation between augmented capture and augmented understanding under memory, sources, contrast and traceability.',
'* **Tenth wave · XLII–XLIII:** **End of the Manipulated Human Era™ and Human Expanded Intelligence™**, focused on cognitive sovereignty, critical awakening and the distinction among captured, substitutive and human-expansive AI under memory, sources, contrast, peer review and traceability.'
)
needle='* and protective force limited by necessity, proportionality, distinction, responsibility and cessation.'
replacement='* protective force limited by necessity, proportionality, distinction, responsibility and cessation;\n* cognitive sovereignty and the possible end of the manipulated-human era;\n* Human Expanded Intelligence™ through human-expansive AI;\n* and Augmented Peer Review™ under human judgement and traceable sources.'
t=t.replace(needle,replacement)
needle_es='* y fuerza protectora limitada por necesidad, proporcionalidad, distinción, responsabilidad y cese.'
replacement_es='* fuerza protectora limitada por necesidad, proporcionalidad, distinción, responsabilidad y cese;\n* soberanía cognitiva y fin posible de la era del hombre manipulado;\n* Inteligencia Humana Expandida™ mediante IA humano-expansiva;\n* y Revisión de Pares Aumentada™ bajo criterio humano y fuentes trazables.'
t=t.replace(needle_es,replacement_es)
p.write_text(t,encoding='utf-8')

# Add XLIII + issue #51 to root priority access in both languages.
p=Path('README.md')
t=p.read_text(encoding='utf-8')
es42='* [XLII · Fin de la Era del Hombre Manipulado™](./manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md)\n* [Síntesis Abierta XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)'
es43='* [XLII · Fin de la Era del Hombre Manipulado™](./manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md)\n* [Síntesis Abierta XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)\n* [XLIII · Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)\n* [Síntesis Abierta XLIII · Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51)'
if 'XLIII · Contra la Incomprensión Reductiva de la IA™' not in t.split('# EN · English')[0]:
    t=t.replace(es42,es43,1)
en42='* [XLII · End of the Manipulated Human Era™](./manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md)\n* [Open Synthesis XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)'
en43='* [XLII · End of the Manipulated Human Era™](./manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md)\n* [Open Synthesis XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)\n* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)\n* [Open Synthesis XLIII · Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51)'
if 'XLIII · Against the Reductive Misunderstanding of AI™' not in t.split('# EN · English',1)[1]:
    t=t.replace(en42,en43,1)
p.write_text(t,encoding='utf-8')

# Sanity checks of current canonical surfaces.
checks={
 'manifiestos/README.md':['XLII–XLIII','43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md','issues/51','I–XLIII'],
 'README.md':['43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md','issues/51','I–XLIII'],
 'propuestas/sintesis-abierta/README.md':['43 manifiestos I–XLIII','43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md','issues/51'],
 'wiki-source/Manifiestos.md':['I–XLIII','43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md','issues/51'],
}
for rel,tokens in checks.items():
    data=Path(rel).read_text(encoding='utf-8')
    if 'XLIIII' in data:
        raise SystemExit(f'Roman numeral corruption remains in {rel}')
    missing=[x for x in tokens if x not in data]
    if missing:
        raise SystemExit(f'{rel} missing {missing}')

# Remove temporary automation machinery before commit.
Path('.github/scripts/one_shot_finalize_xliii_index.py').unlink(missing_ok=True)
Path('.github/workflows/one-shot-finalize-xliii-index.yml').unlink(missing_ok=True)
print('XLIII_FINAL_INDEX_OK')
