from pathlib import Path
import json
import re

# Historical helper: it now only guarantees the registry entries it originally
# introduced and normalises duplicates. It must never append LXVI after newer
# manifestos, because the live collection already owns canonical ordering.
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

# Deduplicate manifesto collection rows by ordinal while preserving the first,
# correctly ordered occurrence. This repairs the former helper's habit of
# appending a second LXVI immediately before ∞ after newer manifestos existed.
manifest_index = Path('manifiestos/README.md')
lines = manifest_index.read_text(encoding='utf-8').splitlines()
seen_ord = set()
out = []
for line in lines:
    m = re.match(r'^- \*\*([IVXLCDM]+)\*\* · \[', line)
    if m:
        roman = m.group(1)
        if roman in seen_ord:
            continue
        seen_ord.add(roman)
    out.append(line)
manifest_index.write_text('\n'.join(out) + '\n', encoding='utf-8')

# Deduplicate manifesto rows in the two live Open-Synthesis tables too. Do not
# insert historical rows: current ordering comes from the canonical manifesto
# index and sync_open_synthesis_manifestos.py.
for index_path in (
    Path('propuestas/sintesis-abierta/README.md'),
    Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'),
):
    text = index_path.read_text(encoding='utf-8')
    seen = set()
    cleaned = []
    for line in text.splitlines():
        m = re.match(r'^\|\s*([IVXLCDM]+)\s*\|', line)
        if m:
            roman = m.group(1)
            if roman in seen:
                continue
            seen.add(roman)
        cleaned.append(line)
    index_path.write_text('\n'.join(cleaned) + '\n', encoding='utf-8')

print('REGISTERED=' + ','.join(required))
print('LEGACY_DUPLICATES_NORMALISED=YES')