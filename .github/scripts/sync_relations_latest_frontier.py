from pathlib import Path
import json
import re

ROOT = Path('.').resolve()
REL = ROOT / 'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
REG = ROOT / 'manifiestos/CANONICAL_FILENAMES.json'
START = '<!-- NEO_RELATIONS_LATEST_FRONTIER_START -->'
END = '<!-- NEO_RELATIONS_LATEST_FRONTIER_END -->'


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


entries = json.loads(REG.read_text(encoding='utf-8'))['entries']
latest = max(entries, key=roman_to_int)
count = len(entries)
latest_path = entries[latest]['legacy']
text = REL.read_text(encoding='utf-8')

# Header and matrix labels are living inventory metadata and must never lag the registry.
text = re.sub(
    r'^\*\*Cobertura / Coverage:\*\*.*$',
    f'**Cobertura / Coverage:** I–{latest} · {count} manifiestos finitos + ∞ como continuidad abierta / {count} finite manifestos I–{latest} + ∞ as open continuity  ',
    text,
    count=1,
    flags=re.M,
)
text = re.sub(
    r'^## Matriz completa I–[IVXLCDM]+ / Complete I–[IVXLCDM]+ matrix$',
    f'## Matriz completa I–{latest} / Complete I–{latest} matrix',
    text,
    count=1,
    flags=re.M,
)

# LXXVII is the first frontier whose relation is maintained here. Future frontier
# additions still receive dynamic inventory metadata even before a curated block
# is authored; the relational audit will continue to require documentary coverage.
if latest == 'LXXVII' or roman_to_int(latest) >= roman_to_int('LXXVII'):
    block = f'''{START}

## LXXVII · Contra la Polarización Binaria y la Radicalización Recíproca™ / Against Binary Polarisation and Reciprocal Radicalisation™

- **Manifiesto / Manifesto:** [LXXVII · Contra la Polarización Binaria y la Radicalización Recíproca™ · Derecho a Reconocer el Problema sin Heredar su Narrativa / Against Binary Polarisation and Reciprocal Radicalisation™ · The Right to Recognise a Problem without Inheriting its Narrative](./77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md).
- **Relación / Relation:** B–C · separación entre fenómeno, causalidad y narrativa; radicalización recíproca; polarización; custodia epistemológica de IA y medios / separation of phenomenon, causality and narrative; reciprocal radicalisation; polarisation; epistemic custodianship of AI and media.
- **Síntesis Abierta / Open Synthesis:** [#154](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/154).
- **Candidato neoaxiomático derivado / Derived neoaxiomatic candidate:** [C-NAX-25 · Fenómeno ≠ Narrativa™ / Phenomenon ≠ Narrative™](../propuestas/sintesis-abierta/2026-08-16_C_NAX_25_FENOMENO_NO_ES_NARRATIVA_ES_EN.md) · [Síntesis #155 / Synthesis #155](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/155).
- **Delta transversal relacionado / Related transversal delta:** [Poder, Trazabilidad, Escrutinio y Evidencia™ / Power, Traceability, Scrutiny and Evidence™](../propuestas/sintesis-abierta/2026-08-16_DELTA_PODER_TRAZABILIDAD_ESCRUTINIO_EVIDENCIA_ES_EN.md) · [C-NAX-26](../propuestas/sintesis-abierta/2026-08-16_C_NAX_26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md) · [Síntesis #156 / Synthesis #156](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/156).
- **Interconexiones / Interconnections:** [XXII · Contra la Reducción y la Captura Intelectual™](./22_contra_reduccion_captura_intelectual_ES_EN.md) · [XXXV · Contra la Ridiculez Mediática y la Economía del Conflicto™](./35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md) · [XLII · Fin de la Era del Hombre Manipulado™](./42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md) · [LIII · Leónidas™](./53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md) · [LXIII · Contra la Simplificación Burda del Marco™](./63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md) · [LXXII · El Hombre Custodio™](./72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md) · [LXXIV · Asimetría de la Destrucción™](./74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [LXXVI · El Altavoz sin Síntesis™](./76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md).

**Regla probatoria / Evidentiary rule:** reconocer un fenómeno no valida automáticamente una causalidad o narrativa; refutar una causalidad no borra automáticamente el fenómeno. El poder incrementa la necesidad de trazabilidad, no la presunción de culpabilidad; la gravedad de una acusación incrementa la evidencia requerida. / recognising a phenomenon does not automatically validate a causality or narrative; refuting a causality does not automatically erase the phenomenon. Power increases the need for traceability, not presumed guilt; the seriousness of an accusation increases the evidence required.

{END}'''
    if START in text and END in text:
        text = re.sub(re.escape(START) + r'.*?' + re.escape(END), block, text, count=1, flags=re.S)
    else:
        marker = '## Regla de mantenimiento / Maintenance rule'
        if marker in text:
            text = text.replace(marker, block + '\n\n---\n\n' + marker, 1)
        else:
            text = text.rstrip() + '\n\n' + block + '\n'

REL.write_text(text, encoding='utf-8')
print(f'RELATIONS_LATEST_FRONTIER count={count} latest={latest} source={latest_path}')
