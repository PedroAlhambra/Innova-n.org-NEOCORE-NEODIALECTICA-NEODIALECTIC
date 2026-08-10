from pathlib import Path
import json
import re

p = Path('manifiestos/CANONICAL_FILENAMES.json')
data = json.loads(p.read_text(encoding='utf-8'))
entries = data.setdefault('entries', {})

required = {
    'LXIII': {
        'legacy': 'manifiestos/63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md',
        'canonical': 'manifiestos/canonicos/LXIII_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md',
    },
    'LXIV': {
        'legacy': 'manifiestos/64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md',
        'canonical': 'manifiestos/canonicos/LXIV_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md',
    },
    'LXV': {
        'legacy': 'manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md',
        'canonical': 'manifiestos/canonicos/LXV_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md',
    },
    'LXVI': {
        'legacy': 'manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md',
        'canonical': 'manifiestos/canonicos/LXVI_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md',
    },
}

for roman, entry in required.items():
    legacy = Path(entry['legacy'])
    if not legacy.exists():
        raise SystemExit(f'Missing manifesto source for {roman}: {legacy}')
    entries[roman] = entry

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# The main synchronizer discovers canonical order from manifiestos/README.md.
# Therefore a newly registered manifesto must be inserted into the collection
# before sync_open_synthesis_manifestos.py runs.
manifest_index = Path('manifiestos/README.md')
text = manifest_index.read_text(encoding='utf-8')
manifest_line = '- **LXVI** · [NeoSinergia™ · Neowar™ Activa, Sistema MÉDICI™ y Leónidas–Cancerbero™ / NeoSynergy™](66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md)'
if manifest_line not in text:
    marker = '- **∞** · [Neo0™ · Puerta Abierta del Fractal / Open Door of the Fractal](INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)'
    if marker not in text:
        raise SystemExit('Cannot locate ∞ row in manifiestos/README.md')
    text = text.replace(marker, manifest_line + '\n' + marker, 1)
manifest_index.write_text(text, encoding='utf-8')

# Keep both Open Synthesis indices structurally aware of LXVI before the
# synchronizer/normalizer validates that the latest manifesto is represented.
row = '| LXVI | [NeoSinergia™ · Neowar™ Activa, Sistema MÉDICI™ y Leónidas–Cancerbero™](../../manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md) | [#110](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/110) |'
for index_path in (
    Path('propuestas/sintesis-abierta/README.md'),
    Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'),
):
    s = index_path.read_text(encoding='utf-8')
    if row not in s:
        inf_pattern = r'^\| ∞ \| .*issues/106\) \|$'
        m = re.search(inf_pattern, s, re.M)
        if not m:
            raise SystemExit(f'Cannot locate ∞ synthesis row in {index_path}')
        s = s[:m.start()] + row + '\n' + s[m.start():]
    index_path.write_text(s, encoding='utf-8')

# Remove the known duplicated unmanaged entry-register section if it appears
# immediately after the managed block. The managed block remains canonical.
synth = Path('propuestas/sintesis-abierta/README.md')
s = synth.read_text(encoding='utf-8')
s = re.sub(
    r'(<!-- NEO_ENTRY_REGISTER_ROUTE_END -->\n)\n'
    r'### 1\. Registrar entrada / Register entry\n\n'
    r'La lectura pública no exige identificación\..*?'
    r'(?=\n### 2\. Contrastar un manifiesto)',
    r'\1', s, count=1, flags=re.S
)
synth.write_text(s, encoding='utf-8')

print('REGISTERED=' + ','.join(required))
print('INDEXED=LXVI')
