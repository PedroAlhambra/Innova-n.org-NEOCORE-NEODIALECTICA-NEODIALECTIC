from pathlib import Path

ROOT = Path('.')


def replace_once(path, old, new):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'expected block not found in {path}: {old[:120]!r}')
    if text.count(old) != 1:
        raise SystemExit(f'expected unique block in {path}, found {text.count(old)}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')
    print(f'patched {path}')

# L · restore the two canonical links present in ES but compressed out of EN.
replace_once(
    'manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md',
    '* [V · Human–AI Symbiosis](./03_simbiosis_humano_ia_ES_EN.md)\n* [Manifesto index](./README.md)',
    '* [V · Human–AI Symbiosis](./03_simbiosis_humano_ia_ES_EN.md)\n* [IX · Memory, Genealogy and Traceability](./06_memoria_genealogia_trazabilidad_ES_EN.md)\n* [X · WEB4™ · SistemaTrazable™](./07_web4_sistematrazable_ES_EN.md)\n* [Manifesto index](./README.md)'
)

# LI · EN must preserve the same six Open Synthesis links as ES.
replace_once(
    'manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md',
    '* [Open Synthesis · Issue #59](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59)\n* [Analysis · Institutional accessibility and citizen escalation](../analisis/publicos/2026-08-08_accesibilidad_institucional_escalado_ciudadano_jefaturas_estado_ES_EN.md)\n* [L · Shared, Not Singular Intelligence™](./50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)\n* [XXXVI · Crown, Eagle and Custodianship of the Age of Man™](./36_corona_aguila_custodia_edad_del_hombre_ES_EN.md)\n* [Manifesto index](./README.md)',
    '* [Open Synthesis · Issue #59](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59)\n* [Analysis · Institutional accessibility and citizen escalation](../analisis/publicos/2026-08-08_accesibilidad_institucional_escalado_ciudadano_jefaturas_estado_ES_EN.md)\n* [L · Shared, Not Singular Intelligence™](./50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)\n* [XXXVI · Crown, Eagle and Custodianship of the Age of Man™](./36_corona_aguila_custodia_edad_del_hombre_ES_EN.md)\n* [X · WEB4™ · SistemaTrazable™](./07_web4_sistematrazable_ES_EN.md)\n* [II · Neodialectical Open Synthesis™](./01_sintesis_abierta_neodialectica_ES_EN.md)'
)

# LII · restore documentary granularity and lists without changing semantics.
path52 = 'manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md'
replace_once(
    path52,
    'Blood preserves memory. Soil preserves location and bond. Neither makes one person more human than another.',
    'Blood preserves memory.\n\nSoil preserves location and bond.\n\nNeither makes one person more human than another.'
)
replace_once(
    path52,
    'This basic equality does not erase identities, families, languages, cultures, peoples or territories. It prevents them from becoming scales of human value.',
    'This basic equality does not erase identities, families, languages, cultures, peoples or territories.\n\nIt prevents them from becoming scales of human value.'
)
replace_once(
    path52,
    'They answered concrete needs: determining legal membership, assigning responsibilities, ordering transmission of rights, registering populations, organising diplomatic protection and structuring taxation, residence and political participation.',
    'They answered concrete needs:\n\n- determining legal membership;\n- assigning responsibilities;\n- ordering transmission of rights;\n- registering populations;\n- organising diplomatic protection;\n- structuring taxation, residence and political participation.'
)
replace_once(
    path52,
    'The distinction must prevent two symmetrical errors: turning nationality into the key to all dignity, and turning human equality into denial of all concrete responsibility.',
    'The distinction must prevent two symmetrical errors:\n\n- turning nationality into the key to all dignity;\n- turning human equality into denial of all concrete responsibility.'
)
replace_once(
    path52,
    "Children should not lose protection because of their parents' decisions. Statelessness cannot mean loss of legal humanity. A refugee does not cease to be a subject of dignity because their relationship with a State has broken. Disability, dependence or poverty cannot reduce belonging.",
    "Children should not lose protection because of their parents' decisions.\n\nStatelessness cannot mean loss of legal humanity.\n\nA refugee does not cease to be a subject of dignity because their relationship with a State has broken.\n\nDisability, dependence or poverty cannot reduce belonging."
)

# LIV · EN had several compressed paragraph groups relative to ES.
path54 = 'manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md'
replace_once(
    path54,
    'A broken object preserves matter, already invested energy, design, human work, memory and sometimes beauty.',
    'A broken object preserves matter.\n\nIt preserves already invested energy.\n\nIt preserves design.\n\nIt preserves human work.\n\nIt preserves memory.\n\nSometimes it preserves beauty.'
)
replace_once(
    path54,
    'Obsolescence is not only technical. It can also be cultural.',
    'Obsolescence is not only technical.\n\nIt can also be cultural.'
)
replace_once(
    path54,
    'A permanent-replacement system needs to manufacture the desire to discard. Neodialectics proposes manufacturing **pride in preservation**.',
    'A permanent-replacement system needs to manufacture the desire to discard.\n\nNeodialectics proposes manufacturing **pride in preservation**.'
)
replace_once(
    path54,
    'This is not an absolute prohibition on manufacturing. It is a reversal of decision order.',
    'This is not an absolute prohibition on manufacturing.\n\nIt is a reversal of decision order.'
)
replace_once(
    path54,
    'GDP may register the sale of a new object. It may also register some repairs.',
    'GDP may register the sale of a new object.\n\nIt may also register some repairs.'
)

print('symmetry repair batch completed')
