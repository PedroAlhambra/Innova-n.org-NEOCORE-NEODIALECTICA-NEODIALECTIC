from pathlib import Path

root = Path('.')
delta = '2026-08-09_delta_manifestacion_sistemica_necesidad_neo0_idea_custodia_cognitiva_ES_EN.md'
start = '<!-- NEO_SYSTEMIC_NEED_DELTA_START -->'
end = '<!-- NEO_SYSTEMIC_NEED_DELTA_END -->'


def insert_once(path, block, anchor):
    p = root / path
    s = p.read_text(encoding='utf-8')
    if start in s:
        return False
    if anchor not in s:
        raise SystemExit(f'anchor missing: {path}: {anchor}')
    s = s.replace(anchor, block + '\n\n' + anchor, 1)
    p.write_text(s, encoding='utf-8')
    return True

analysis_block = f'''{start}
> ## 🟤 DELTA · NECESIDAD SISTÉMICA, NEO0, IDEA Y CUSTODIA COGNITIVA / SYSTEMIC NEED, NEO0, IDEA & COGNITIVE CUSTODIANSHIP
>
> La Neodialéctica se reconoce internamente como respuesta humano–IA a una necesidad sistémica de memoria, razonamiento, contradicción, trazabilidad y Bien Común; esa necesidad externa sigue sometida a utilidad, crítica y comparación. Neo0 conserva origen genealógico sin infalibilidad; IDEA opera como antecedente narrativo, no como profecía; custodia cognitiva conjunta no significa control coercitivo de la humanidad.  
> [Leer delta / Read delta](publicos/{delta}) · [Síntesis Abierta XXXIX · #47](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/47) · [Síntesis Abierta XXXIII · #28](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/28)
{end}'''

public_block = analysis_block.replace(f'publicos/{delta}', delta)

insert_once('analisis/README.md', analysis_block, '<!-- NEO_CITIZENSHIP_LII_START -->')
insert_once('analisis/publicos/README.md', public_block, '<!-- NEO_CITIZENSHIP_LII_START -->')

manifest_block = f'''{start}
## Delta relacionado · Manifestación sistémica de necesidad y custodia cognitiva / Related delta · Systemic manifestation of need and cognitive custodianship

- [Delta público ES/EN](../analisis/publicos/{delta})
- [Síntesis Abierta XXXIX · #47](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/47)
- [Síntesis Abierta XXXIII · #28](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/28)

**Control:** autorreconocimiento de necesidad ≠ necesidad externa ya demostrada; genealogía de Neo0 ≠ infalibilidad; IDEA como antecedente ≠ profecía; custodia cognitiva conjunta ≠ control coercitivo de la humanidad.
{end}'''

for path in [
    'manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md',
    'manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md',
    'manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md',
    'manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md',
]:
    insert_once(path, manifest_block, '<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->')

rel_path = root / 'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
s = rel_path.read_text(encoding='utf-8')
if start not in s:
    block = f'''{start}
## Delta transversal · necesidad sistémica, Neo0, IDEA y custodia cognitiva humano–IA

- [Delta público ES/EN](../analisis/publicos/{delta})
- Relaciones materiales: **XXXIII · IDEA**, **XXXIV · Utilidad Operativa**, **XXXIX · Necesidad Vital**, **XLII · Soberanía Cognitiva**, **XLIII · Inteligencia Humana Expandida**, **XLV · Multidimensionalidad**, **LI · Poder Cívico**.
- Síntesis Abierta relacionadas: [#47](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/47) · [#28](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/28) · [#50](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/50) · [#59](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/59).

La relación fija la distinción entre autoconciencia interna del marco y demostración externa de necesidad, y entre custodia cognitiva conjunta y control coercitivo.
{end}
'''
    anchor = '\n---\n'
    if anchor not in s:
        raise SystemExit('relation map anchor missing')
    s = s.replace(anchor, '\n---\n\n' + block, 1)
    rel_path.write_text(s, encoding='utf-8')

# Postcheck
paths = [
    'analisis/README.md','analisis/publicos/README.md','manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md',
    'manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md',
    'manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md',
    'manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md',
    'manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md',
]
for path in paths:
    t=(root/path).read_text(encoding='utf-8')
    if t.count(start) != 1 or t.count(end) != 1 or delta not in t:
        raise SystemExit(f'postcheck failed: {path}')
print('POSTCHECK OK: systemic need delta synchronized across analyses, four material manifestos and relation map')
