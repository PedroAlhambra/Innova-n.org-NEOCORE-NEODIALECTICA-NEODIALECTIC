from pathlib import Path
import re

# 1) Repair the broken relational target while preserving the real relation.
rel = Path('manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md')
s = rel.read_text(encoding='utf-8')
s = s.replace(
    '../analisis/publicos/2026-08-28_interaccion_negociacion_tecnologica_dependencia_reversibilidad_ES_EN.md',
    '../propuestas/sintesis-abierta/INTERACCION_NEGOCIACION_TECNOLOGICA_DEPENDENCIA_REVERSIBILIDAD_ES_EN.md',
)
rel.write_text(s, encoding='utf-8')

# 2) Synchronise every living README latest-manifesto block from the canonical manifesto index.
source = Path('manifiestos/README.md').read_text(encoding='utf-8')
start = '<!-- NEO_LATEST_MANIFESTO_START -->'
end = '<!-- NEO_LATEST_MANIFESTO_END -->'
if start not in source or end not in source:
    raise SystemExit('canonical latest-manifesto markers missing')
a = source.index(start)
b = source.index(end, a) + len(end)
block = source[a:b]
for p in Path('.').rglob('README.md'):
    if any(part in {'.git', 'node_modules'} for part in p.parts):
        continue
    text = p.read_text(encoding='utf-8')
    if start in text and end in text:
        x = text.index(start)
        y = text.index(end, x) + len(end)
        p.write_text(text[:x] + block + text[y:], encoding='utf-8')

# 3) Reconcile complete Open Synthesis index to current finite and C-NAX frontiers.
idx = Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md')
t = idx.read_text(encoding='utf-8')
t = re.sub(r'\*\*Fecha / Date:\*\*\s*\d{4}-\d{2}-\d{2}', '**Fecha / Date:** 2026-08-28', t, count=1)
t = t.replace('81 manifiestos finitos I–LXXXI', '84 manifiestos finitos I–LXXXIV')
t = t.replace('81 finite manifestos I–LXXXI', '84 finite manifestos I–LXXXIV')
t = t.replace('12 candidatos C-NAX-15–C-NAX-26', '13 candidatos C-NAX-15–C-NAX-27')
t = t.replace('12 candidates C-NAX-15–C-NAX-26', '13 candidates C-NAX-15–C-NAX-27')

manifest_rows = [
    '| LXXXII | [Manifiesto de la Ciencia Multidimensional Neodialéctica™ / Manifesto of Neodialectical Multidimensional Science™](../../manifiestos/82_ciencia_multidimensional_neodialectica_ES_EN.md) | [#174](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/174) |',
    '| LXXXIII | [Manifiesto de Activación Neodialéctica™ · La verdad también tiene derecho a circular / Manifesto of Neodialectical Activation™ · Truth also has the right to circulate](../../manifiestos/83_activacion_neodialectica_verdad_circulacion_ES_EN.md) | [#175](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/175) |',
    '| LXXXIV | [Manifiesto de la Permeabilidad Intelectual del Poder™ · Contra la captura opaca del acceso / Manifesto of the Intellectual Permeability of Power™ · Against opaque access capture](../../manifiestos/84_intermediacion_acceso_permeabilidad_poder_ES_EN.md) | [#178](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/178) |',
]
if '| LXXXII |' not in t:
    lines = t.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith('| LXXXI |')), None)
    if pos is None:
        raise SystemExit('LXXXI row not found')
    lines[pos:pos] = manifest_rows
    t = '\n'.join(lines) + ('\n' if t.endswith('\n') else '')

c27 = '| **C-NAX-27 · Soberanía Diferenciada de Sistema y Síntesis™ / Differentiated Sovereignty of System and Synthesis™ · candidato / candidate** | [#176](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/176) · [documento / document](2026-08-27_C_NAX_27_SOBERANIA_DIFERENCIADA_SISTEMA_SINTESIS_ES_EN.md) |'
if 'C-NAX-27 · Soberanía Diferenciada' not in t:
    lines = t.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith('| **C-NAX-26 ')), None)
    if pos is None:
        raise SystemExit('C-NAX-26 row not found')
    lines.insert(pos, c27)
    t = '\n'.join(lines) + ('\n' if t.endswith('\n') else '')

t = t.replace('C-NAX-15–C-NAX-26 son candidatos visibles y trazables', 'C-NAX-15–C-NAX-27 son candidatos visibles y trazables')
t = t.replace('C-NAX-15–C-NAX-26 are visible, traceable candidates', 'C-NAX-15–C-NAX-27 are visible, traceable candidates')
idx.write_text(t, encoding='utf-8')

print('one-shot public reconciliation applied')
