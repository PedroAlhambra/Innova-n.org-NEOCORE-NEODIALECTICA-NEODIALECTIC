from pathlib import Path
import json

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
print('REGISTERED=' + ','.join(required))
