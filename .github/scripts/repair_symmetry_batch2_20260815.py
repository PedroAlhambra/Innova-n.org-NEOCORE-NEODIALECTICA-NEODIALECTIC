from pathlib import Path

ROOT = Path('.')


def replace_once(path, old, new):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'expected block not found in {path}: {old[:140]!r}')
    if text.count(old) != 1:
        raise SystemExit(f'expected unique block in {path}, found {text.count(old)}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')
    print(f'patched {path}')

# Ceuta · section 2: EN compressed two ES paragraphs into one.
replace_once(
    'analisis/publicos/2026-08-07_parte-iii-ceuta-marruecos-evolucion-conflicto-investigaciones_ES_EN.md',
    'This does not remove the role of smuggling networks. It changes it.',
    'This does not remove the role of smuggling networks.\n\nIt changes it.'
)

# Forgotten History · ES lacked the Open Synthesis heading + call present in EN.
replace_once(
    'analisis/publicos/2026-08-08_historia_olvidada_ceres_descompresion_arquetipica_generativa_ES_EN.md',
    '**PERO UNA RELACIÓN QUE PRODUCE PREDICCIONES Y SOBREVIVE A CONTRADICCIÓN = OBJETO LEGÍTIMO DE INVESTIGACIÓN**\n\n---\n\n# EN · English',
    '**PERO UNA RELACIÓN QUE PRODUCE PREDICCIONES Y SOBREVIVE A CONTRADICCIÓN = OBJETO LEGÍTIMO DE INVESTIGACIÓN**\n\n## Síntesis Abierta\n\nSe solicitan pruebas, objeciones, explicaciones alternativas, criterios de falsación y modelos superiores en [Issue #63](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/63).\n\n---\n\n# EN · English'
)

# XXXIV · section V: restore the two-paragraph EN structure corresponding to ES.
replace_once(
    'manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md',
    'Open Synthesis distributes review among people with expert knowledge, pertinent experience, sufficient study or ideas capable of producing a material delta.\n\nIts function is not to manufacture unanimity.',
    'Open Synthesis turns review into a distributed function.\n\nPeople with expert knowledge, pertinent experience, sufficient study or ideas capable of producing a material delta may participate.\n\nIts function is not to manufacture unanimity.'
)

# XXXVII · section XV: EN split one ES sentence into two paragraphs.
replace_once(
    'manifiestos/37_neofraternidad_ES_EN.md',
    'Every contribution must distinguish personal experience, general principle, verifiable harm, interpretation and proposal; and avoid unnecessarily exposing private data about third parties.\n\nIt must also preserve dignity, genealogy, traceability, delta and version.',
    'Every contribution must distinguish personal experience, general principle, verifiable harm, interpretation and proposal; avoid unnecessarily exposing private data about third parties; and preserve dignity, genealogy, traceability, delta and version.'
)

# XLVI · section VIII: EN compressed the three closing ES paragraphs into one.
replace_once(
    'manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md',
    'Without truth, closure is denial. Without responsibility, it can become impunity. Without a possibility of future, justice can become a permanent prison of the past.',
    'Without truth, closure is denial.\n\nWithout responsibility, it can become impunity.\n\nWithout a possibility of future, justice can become a permanent prison of the past.'
)

# Auditor: a bilingual provenance footer after the EN body is shared metadata, not EN-only prose.
replace_once(
    '.github/scripts/audit_global_bilingual_symmetry.py',
    "if re.match(r'^(?:Clasificación provisional / Provisional classification|Síntesis / Synthesis|Regla / Rule|Estado / Status|Puertas / Gates):',plain,re.I): continue",
    "if re.match(r'^(?:Clasificación provisional / Provisional classification|Síntesis / Synthesis|Regla / Rule|Estado / Status|Puertas / Gates|Principio de procedencia / Provenance principle):',plain,re.I): continue"
)

print('second symmetry repair batch completed')
