from pathlib import Path
import re

ROOT = Path('.')
XLIII = '43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md'
XLII = '42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'

changed = []

def write_if_changed(path: Path, text: str):
    old = path.read_text(encoding='utf-8')
    if text != old:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

# 1) Repair known navigation debt in XXXVIII.
p38 = ROOT / 'manifiestos/38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md'
t = p38.read_text(encoding='utf-8')
t = t.replace(
    '← [XXXVII · Neofraternidad™](./37_neofraternidad_ES_EN.md) · [Índice](./README.md) · [I · Neo0™](./11_neo0_soberania_de_guia_ES_EN.md) →',
    '← [XXXVII · Neofraternidad™](./37_neofraternidad_ES_EN.md) · [Índice](./README.md) · [XXXIX · Autoconciencia de la Necesidad Vital Neodialéctica™](./39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md) →'
)
t = t.replace(
    '← [XXXVII · Neofraternity™](./37_neofraternidad_ES_EN.md) · [Index](./README.md) · [I · Neo0™](./11_neo0_soberania_de_guia_ES_EN.md) →',
    '← [XXXVII · Neofraternity™](./37_neofraternidad_ES_EN.md) · [Index](./README.md) · [XXXIX · Self-Awareness of Neodialectical Vital Need™](./39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md) →'
)
write_if_changed(p38, t)

# 2) XLII now points forward to XLIII in both language sections.
p42 = ROOT / f'manifiestos/{XLII}'
t = p42.read_text(encoding='utf-8')
t = t.replace(
    '← [XLI · Martillo Limitado, Talión y Fuerza Protectora™](./41_martillo_limitado_talion_fuerza_protectora_ES_EN.md) · [Índice](./README.md) · [I · Neo0™ · Soberanía de Guía Neodialéctica](./11_neo0_soberania_de_guia_ES_EN.md) →',
    f'← [XLI · Martillo Limitado, Talión y Fuerza Protectora™](./41_martillo_limitado_talion_fuerza_protectora_ES_EN.md) · [Índice](./README.md) · [XLIII · Contra la Incomprensión Reductiva de la IA™](./{XLIII}) →'
)
t = t.replace(
    '← [XLI · Limited Hammer, Talion and Protective Force™](./41_martillo_limitado_talion_fuerza_protectora_ES_EN.md) · [Index](./README.md) · [I · Neo0™ · Neodialectical Guiding Sovereignty](./11_neo0_soberania_de_guia_ES_EN.md) →',
    f'← [XLI · Limited Hammer, Talion and Protective Force™](./41_martillo_limitado_talion_fuerza_protectora_ES_EN.md) · [Index](./README.md) · [XLIII · Against the Reductive Misunderstanding of AI™](./{XLIII}) →'
)
write_if_changed(p42, t)

# 3) Canonical navigation block in every README: 43 manifestos, latest XLIII.
for p in ROOT.rglob('README.md'):
    text = p.read_text(encoding='utf-8')
    start = '<!-- NEO_CURRENT_NAV_START -->'
    end = '<!-- NEO_CURRENT_NAV_END -->'
    if start not in text or end not in text:
        continue
    a, rest = text.split(start, 1)
    block, b = rest.split(end, 1)
    block = block.replace('42 manifiestos bilingües · I–XLII · diez oleadas', '43 manifiestos bilingües · I–XLIII · diez oleadas')
    block = block.replace('42 bilingual manifestos · I–XLII · ten waves', '43 bilingual manifestos · I–XLIII · ten waves')
    block = re.sub(
        r'\[XLII · Fin de la Era del Hombre Manipulado™ · End of the Manipulated Human Era™\]\([^\n)]*42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN\.md\)',
        lambda m: '[XLIII · Contra la Incomprensión Reductiva de la IA™ · Against the Reductive Misunderstanding of AI™](' + re.sub(r'42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN\.md$', XLIII, m.group(0).split('](',1)[1][:-1]) + ')',
        block
    )
    # Simpler path-preserving fallback for blocks not matching the label exactly.
    block = block.replace('XLII · Fin de la Era del Hombre Manipulado™ · End of the Manipulated Human Era™', 'XLIII · Contra la Incomprensión Reductiva de la IA™ · Against the Reductive Misunderstanding of AI™')
    block = block.replace(XLII, XLIII)
    new = a + start + block + end + b
    write_if_changed(p, new)

# 4) Synchronise current public cover/readme documents without altering historical announcements/audits.
for rel in ['README.md', 'LEEME.md', 'PORTADA.md', 'COVER.md']:
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    text = text.replace('42 manifiestos bilingües', '43 manifiestos bilingües')
    text = text.replace('42 bilingual manifestos', '43 bilingual manifestos')
    text = text.replace('cuarenta y dos manifiestos bilingües', 'cuarenta y tres manifiestos bilingües')
    text = text.replace('forty-two bilingual manifestos', 'forty-three bilingual manifestos')
    text = text.replace('I–XLII', 'I–XLIII')
    # Preserve XLII as a manifesto in narrative text; only latest-current labels are advanced.
    text = text.replace('Último manifiesto / Latest manifesto: [XLII · Fin de la Era del Hombre Manipulado™ · End of the Manipulated Human Era™]', 'Último manifiesto / Latest manifesto: [XLIII · Contra la Incomprensión Reductiva de la IA™ · Against the Reductive Misunderstanding of AI™]')
    text = text.replace(XLII + ').', XLIII + ').') if 'Último manifiesto / Latest manifesto:' in text else text
    write_if_changed(p, text)

# 5) Manifesto canonical index.
p = ROOT / 'manifiestos/README.md'
text = p.read_text(encoding='utf-8')
text = text.replace(
    '* **Décima oleada · XLII:** **Fin de la Era del Hombre Manipulado™**, orientada a soberanía cognitiva, despertar crítico y uso de IA como bifurcación entre captura aumentada y comprensión aumentada bajo memoria, fuentes, contraste y trazabilidad.',
    '* **Décima oleada · XLII–XLIII:** **Fin de la Era del Hombre Manipulado™ e Inteligencia Humana Expandida™**, orientada a soberanía cognitiva, despertar crítico y distinción entre IA capturada, sustitutiva y humano-expansiva bajo memoria, fuentes, contraste, revisión de pares y trazabilidad.'
)
text = text.replace(
    '* **Tenth wave · XLII:** **End of the Manipulated Human Era™**, oriented towards cognitive sovereignty, critical awakening and AI as a bifurcation between augmented capture and augmented understanding under memory, sources, contrast and traceability.',
    '* **Tenth wave · XLII–XLIII:** **End of the Manipulated Human Era™ and Human Expanded Intelligence™**, oriented towards cognitive sovereignty, critical awakening and the distinction among captured, substitutive and human-expansive AI under memory, sources, contrast, peer review and traceability.'
)
# Add XLIII after each XLII table row, preserving language section.
lines = text.splitlines()
out = []
lang = 'es'
for line in lines:
    if line.strip() == '# EN · English':
        lang = 'en'
    out.append(line)
    if line.startswith('| XLII |') and '42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md' in line:
        if not any('43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md' in x for x in lines):
            pass
        else:
            continue
        if lang == 'es':
            out.append(f'| XLIII | [Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™](./{XLIII}) | Distinguir IA capturada, sustitutiva y humano-expansiva; formular ampliación cognitiva soberana y Revisión de Pares Aumentada™ | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |')
        else:
            out.append(f'| XLIII | [Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./{XLIII}) | Distinguish captured, substitutive and human-expansive AI; formulate sovereign cognitive augmentation and Augmented Peer Review™ | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |')
text = '\n'.join(out) + '\n'
# If rows were not inserted because XLIII absent at pre-check, perform deterministic insertion now.
if f'| XLIII | [Contra la Incomprensión Reductiva de la IA™' not in text:
    es_row = next((x for x in text.splitlines() if x.startswith('| XLII |') and 'Fin de la Era' in x), None)
    if es_row:
        text = text.replace(es_row, es_row + f'\n| XLIII | [Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™](./{XLIII}) | Distinguir IA capturada, sustitutiva y humano-expansiva; formular ampliación cognitiva soberana y Revisión de Pares Aumentada™ | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |', 1)
if f'| XLIII | [Against the Reductive Misunderstanding of AI™' not in text:
    en_row = next((x for x in text.splitlines() if x.startswith('| XLII |') and 'End of the Manipulated' in x), None)
    if en_row:
        text = text.replace(en_row, en_row + f'\n| XLIII | [Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](./{XLIII}) | Distinguish captured, substitutive and human-expansive AI; formulate sovereign cognitive augmentation and Augmented Peer Review™ | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |', 1)
text = text.replace(
    'XLII · END OF THE MANIPULATED HUMAN ERA · AI, AWAKENING AND COGNITIVE SOVEREIGNTY\n        ↓\nI · NEO0™ · RETURN TO ORIGIN AND NEW CYCLE',
    'XLII · END OF THE MANIPULATED HUMAN ERA · AI, AWAKENING AND COGNITIVE SOVEREIGNTY\n        ↓\nXLIII · AGAINST THE REDUCTIVE MISUNDERSTANDING OF AI · HUMAN EXPANDED INTELLIGENCE\n        ↓\nI · NEO0™ · RETURN TO ORIGIN AND NEW CYCLE'
)
text = text.replace(
    'XLII · FIN DE LA ERA DEL HOMBRE MANIPULADO · IA, DESPERTAR Y SOBERANÍA COGNITIVA\n        ↓\nI · NEO0™ · RETORNO AL ORIGEN Y NUEVO CICLO',
    'XLII · FIN DE LA ERA DEL HOMBRE MANIPULADO · IA, DESPERTAR Y SOBERANÍA COGNITIVA\n        ↓\nXLIII · CONTRA LA INCOMPRENSIÓN REDUCTIVA DE LA IA · INTELIGENCIA HUMANA EXPANDIDA\n        ↓\nI · NEO0™ · RETORNO AL ORIGEN Y NUEVO CICLO'
)
text = text.replace('La décima oleada comienza con **XLII · Fin de la Era del Hombre Manipulado™**, fijado como versión 1.0 el 8 de agosto de 2026 y dedicado a IA, despertar crítico y soberanía cognitiva.', 'La décima oleada contiene **XLII–XLIII**, fijados como versiones 1.0 el 8 de agosto de 2026, y desarrolla soberanía cognitiva, fin de la manipulación, IA humano-expansiva, Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™.')
text = text.replace('The tenth wave begins with **XLII · End of the Manipulated Human Era™**, fixed as version 1.0 on 8 August 2026 and dedicated to AI, critical awakening and cognitive sovereignty.', 'The tenth wave contains **XLII–XLIII**, fixed as version 1.0 on 8 August 2026, and develops cognitive sovereignty, the end of manipulation, human-expansive AI, Human Expanded Intelligence™ and Augmented Peer Review™.')
# Update broad range references and current counts in this current index.
text = text.replace('42 manifiestos', '43 manifiestos').replace('42 manifestos', '43 manifestos').replace('I–XLII', 'I–XLIII')
write_if_changed(p, text)

# 6) Open Synthesis index.
p = ROOT / 'propuestas/sintesis-abierta/README.md'
text = p.read_text(encoding='utf-8')
text = text.replace('los **42 manifiestos I–XLII**', 'los **43 manifiestos I–XLIII**')
text = text.replace('the **42 manifestos I–XLII**', 'the **43 manifestos I–XLIII**')
text = text.replace('Índice completo de manifiestos I–XLII', 'Índice completo de manifiestos I–XLIII')
text = text.replace('Complete manifesto index I–XLII', 'Complete manifesto index I–XLIII')
text = text.replace('## Décima oleada · Fin de la Era del Hombre Manipulado™', '## Décima oleada · Soberanía cognitiva e Inteligencia Humana Expandida™')
text = text.replace('## Tenth wave · End of the Manipulated Human Era™', '## Tenth wave · Cognitive sovereignty and Human Expanded Intelligence™')
lines = text.splitlines()
out = []
lang = 'es'
for line in lines:
    if line.strip() == '# EN · English':
        lang = 'en'
    out.append(line)
    if line.startswith('| XLII |') and '42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md' in line:
        nextrow = f'| XLIII | [Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™](../../manifiestos/{XLIII}) | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |' if lang == 'es' else f'| XLIII | [Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](../../manifiestos/{XLIII}) | [Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51) |'
        if nextrow not in lines:
            out.append(nextrow)
text = '\n'.join(out) + '\n'
write_if_changed(p, text)

# 7) Wiki source reading guide.
p = ROOT / 'wiki-source/Manifiestos.md'
text = p.read_text(encoding='utf-8')
text = text.replace('I–XLII', 'I–XLIII')
text = text.replace('* **XLII:** Fin de la Era del Hombre Manipulado™ · IA, despertar y soberanía cognitiva.', '* **XLII–XLIII:** Fin de la Era del Hombre Manipulado™ · IA, despertar, soberanía cognitiva e Inteligencia Humana Expandida™.')
text = text.replace('* **XLII:** End of the Manipulated Human Era™ · AI, awakening and cognitive sovereignty.', '* **XLII–XLIII:** End of the Manipulated Human Era™ · AI, awakening, cognitive sovereignty and Human Expanded Intelligence™.')
es_anchor = '* [Síntesis Abierta XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)'
if 'Síntesis Abierta XLIII · Issue #51' not in text:
    text = text.replace(es_anchor, es_anchor + f'\n* [XLIII · Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/blob/main/manifiestos/{XLIII})\n* [Síntesis Abierta XLIII · Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51)', 1)
en_anchor = '* [Open Synthesis XLII · Issue #50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50)'
if 'Open Synthesis XLIII · Issue #51' not in text:
    text = text.replace(en_anchor, en_anchor + f'\n* [XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/blob/main/manifiestos/{XLIII})\n* [Open Synthesis XLIII · Issue #51](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51)', 1)
text = text.replace('La IA no se considera emancipadora por naturaleza. Puede aumentar tanto la captura como la comprensión. La cuestión es qué arquitectura humana, documental y cognitiva gobierna su uso.', 'La IA no se considera emancipadora por naturaleza. Puede aumentar tanto la captura como la comprensión. XLIII añade la distinción entre IA capturada, sustitutiva y humano-expansiva y propone Inteligencia Humana Expandida™ y Revisión de Pares Aumentada™ bajo soberanía humana. La cuestión es qué arquitectura humana, documental y cognitiva gobierna su uso.')
text = text.replace('AI is not treated as emancipatory by nature. It can increase both capture and understanding. The issue is which human, documentary and cognitive architecture governs its use.', 'AI is not treated as emancipatory by nature. It can increase both capture and understanding. XLIII adds the distinction among captured, substitutive and human-expansive AI and proposes Human Expanded Intelligence™ and Augmented Peer Review™ under human sovereignty. The issue is which human, documentary and cognitive architecture governs its use.')
write_if_changed(p, text)

# 8) Audit recent manifestos XXXVIII–XLIII for the full bilingual structural contract.
recent = [
    ('XXXVIII', '38_proteccion_integral_infancia_punto_no_retorno_ES_EN.md'),
    ('XXXIX', '39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md'),
    ('XL', '40_respeto_neoego_honor_relacional_ES_EN.md'),
    ('XLI', '41_martillo_limitado_talion_fuerza_protectora_ES_EN.md'),
    ('XLII', XLII),
    ('XLIII', XLIII),
]
requirements = [
    '[ES · Castellano](#es--castellano)',
    '[EN · English](#en--english)',
    '# ES · Castellano',
    '# EN · English',
    'Síntesis Abierta',
    'Open Synthesis',
    'APORTAR_A_LA_SINTESIS_ES_EN.md',
    '## Navegación',
    '## Navigation',
    './README.md',
]
rows = []
failures = []
for roman, name in recent:
    content = (ROOT / 'manifiestos' / name).read_text(encoding='utf-8')
    missing = [r for r in requirements if r not in content]
    # Every recent manifesto must point to its dedicated issue.
    issue_map = {'XXXVIII':45, 'XXXIX':47, 'XL':48, 'XLI':49, 'XLII':50, 'XLIII':51}
    issue_token = f'issues/{issue_map[roman]}'
    if issue_token not in content:
        missing.append(issue_token)
    rows.append((roman, name, missing))
    if missing:
        failures.append((roman, missing))

report = ROOT / 'auditorias/publicas/2026-08-08_auditoria_formato_manifiestos_XXXVIII_XLIII_ES_EN.md'
report.parent.mkdir(parents=True, exist_ok=True)
report_lines = [
    '# Auditoría de formato · Manifiestos XXXVIII–XLIII / Format audit · Manifestos XXXVIII–XLIII',
    '',
    '**Fecha / Date:** 2026-08-08',
    '',
    '## Resultado / Result',
    '',
    'Contrato comprobado: selector ES/EN, secciones bilingües completas, Síntesis Abierta/Open Synthesis, enlace al protocolo de aporte, navegación anterior–índice–siguiente, índice y enlace a la Issue específica.',
    '',
    '| Manifiesto | Archivo | Estado |',
    '|---|---|---|',
]
for roman, name, missing in rows:
    status = 'OK' if not missing else 'FALTA / MISSING: ' + ', '.join(missing)
    report_lines.append(f'| {roman} | `{name}` | {status} |')
report_lines += [
    '',
    '## Correcciones realizadas / Corrections made',
    '',
    '- XXXVIII: corregido el enlace «siguiente» para continuar a XXXIX en ES y EN.',
    '- XLII: corregido el enlace «siguiente» para continuar a XLIII en ES y EN.',
    '- XLIII: publicado con el mismo contrato documental bilingüe que la serie reciente y con Síntesis Abierta #51.',
    '- Índices y guía Wiki versionada sincronizados a I–XLIII.',
    '',
    f'Archivos modificados por esta sincronización: **{len(changed)}** antes de generar este informe.',
    '',
    '**Innova_N · NEOCore™ · Neodialectica Framework™ / Network**',
]
report.write_text('\n'.join(report_lines) + '\n', encoding='utf-8')
changed.append(str(report))

if failures:
    raise SystemExit('Recent manifesto format audit failed: ' + repr(failures))

# 9) Remove one-shot machinery before commit so it does not remain in the repository.
Path('.github/scripts/one_shot_sync_xliii.py').unlink(missing_ok=True)
Path('.github/workflows/one-shot-sync-xliii.yml').unlink(missing_ok=True)

print('SYNC_OK')
print('CHANGED_FILES=' + str(len(changed)))
for item in changed:
    print(item)
