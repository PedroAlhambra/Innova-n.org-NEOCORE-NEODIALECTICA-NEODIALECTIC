from pathlib import Path

p = Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md')
text = p.read_text(encoding='utf-8')
start = '<!-- NEO_RELATIONS_LXXVII_START -->'
end = '<!-- NEO_RELATIONS_LXXVII_END -->'
block = '''<!-- NEO_RELATIONS_LXXVII_START -->

### LXXVII · [Contra la Polarización Binaria y la Radicalización Recíproca™ · Derecho a Reconocer el Problema sin Heredar su Narrativa / Against Binary Polarisation and Reciprocal Radicalisation™ · The Right to Recognise a Problem without Inheriting its Narrative](./77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md)
- **Relación / Relation:** B–C · despolarización cognitiva, separación fenómeno–narrativa, radicalización recíproca y custodia epistemológica humano–IA / cognitive depolarisation, phenomenon–narrative separation, reciprocal radicalisation and human–AI epistemic custodianship.
- **Síntesis Abierta / Open Synthesis:** [#154](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/154).
- **Interconexiones / Interconnections:** [XXII · Reducción y Captura Intelectual™](./22_contra_reduccion_captura_intelectual_ES_EN.md) · [XXXV · Ridiculez Mediática y Economía del Conflicto™](./35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md) · [XLII · Fin de la Era del Hombre Manipulado™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [LXIII · Simplificación Burda™](./63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md) · [LXXVI · Altavoz sin Síntesis™](./76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md) · [C-NAX-24 · Diagnóstico ≠ Síntesis™](../propuestas/sintesis-abierta/2026-08-15_C_NAX_24_DIAGNOSTICO_NO_ES_SINTESIS_ES_EN.md) · [C-NAX-25 · Fenómeno ≠ Narrativa™](../propuestas/sintesis-abierta/2026-08-16_C_NAX_25_FENOMENO_NO_ES_NARRATIVA_ES_EN.md).

<!-- NEO_RELATIONS_LXXVII_END -->'''

if start in text and end in text:
    a = text.index(start)
    b = text.index(end, a) + len(end)
    new = text[:a] + block + text[b:]
else:
    new = text.rstrip() + '\n\n' + block + '\n'

if new != text:
    p.write_text(new, encoding='utf-8')
    print('LXXVII_RELATIONS_SYNC changed')
else:
    print('LXXVII_RELATIONS_SYNC unchanged')
