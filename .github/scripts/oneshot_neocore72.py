from pathlib import Path
import re
import subprocess
import sys

# Final verification only. All conceptual and translation deltas are already
# committed; this run regenerates the audit from the actual current tree.
subprocess.run([sys.executable,'.github/scripts/audit_es_en_parity.py'],check=True)

parity=Path('auditorias/publicas/2026-08-09_auditoria_paridad_ES_EN_manifiestos_articulos.md').read_text(encoding='utf-8')
flagged=parity.split('## Casos marcados',1)[1].split('## ',1)[0] if '## Casos marcados' in parity else ''
bad=[line for line in flagged.splitlines() if re.match(r'^\| `manifiestos/.*\.md` \|',line)]
missing=[]
if '## Marcadores incompletos' in parity:
    block=parity.split('## Marcadores incompletos',1)[1].split('## ',1)[0]
    missing=[line for line in block.splitlines() if '`manifiestos/' in line]

idx=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md').read_text(encoding='utf-8')
syn=Path('propuestas/sintesis-abierta/README.md').read_text(encoding='utf-8')
base=Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_soberania_sintesis_web4_ES_EN.md').read_text(encoding='utf-8')
nax=Path('neoaxiomas/README.md').read_text(encoding='utf-8')
web4=Path('web4/manifiestos/index.html').read_text(encoding='utf-8')
inf=Path('manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md').read_text(encoding='utf-8')
pos=[idx.find('| LXVI |'),idx.find('| LXVII |'),idx.find('| LXVIII |'),idx.find('| ∞ |')]
checks={
    'base_postcheck_OK':'**Estado / Status:** **OK**' in base,
    'complete_index_68':'68 manifiestos finitos I–LXVIII' in idx,
    'complete_index_recent_nodes':all(x >= 0 for x in pos) and pos == sorted(pos),
    'open_synthesis_single_entry_route':syn.count('### 1. Registrar entrada / Register entry') == 1,
    'parity_report_current':'**Fecha:** 2026-08-10' in parity,
    'parity_no_flagged_manifest':not bad,
    'parity_no_missing_manifest':not missing,
    'neoaxiom_candidates_15_18':all(x in nax for x in ['C-NAX-15','C-NAX-16','C-NAX-17','C-NAX-18']),
    'web4_72_and_infinity':'NEOCore™ 7.2' in web4 and "['∞'" in web4 and "['LXVIII'" in web4,
    'foundation_corporation_synthesis':'Innova_N Fundación' in inf and 'Innova_N Corporación' in inf and 'No Coronación de la Parte™' in inf,
}
status='OK' if all(checks.values()) else 'REQUIERE CORRECCIÓN'
out=[
    '# Cierre de integración · NEOCore™ 7.2 · índices, paridad y WEB4™ / Final integration check','',
    '**Fecha / Date:** 2026-08-10  ',f'**Estado / Status:** **{status}**','',
    '## Verificaciones / Checks',''
]
out += [f'- [{"x" if ok else " "}] `{k}`' for k,ok in checks.items()]
out += [
    '', '## Resultado', '',
    '- **68 manifiestos finitos · I–LXVIII + ∞** reflejados en el índice completo de Síntesis Abierta.',
    '- **NAX-01–NAX-14** permanecen canónicos; **C-NAX-15–C-NAX-18** permanecen candidatos visibles, sin promoción automática.',
    '- **NEOCore™ 7.2** conserva 7.1 y añade Soberanía de Síntesis™, incluida la diferenciación futura Innova_N Fundación / Corporación.',
    '- **WEB4™** continúa como DEMO/prototipo público y su lector incluye I–LXVIII + ∞.',
    '- **NeoCronos™** permanece experimental, multidimensional y revisable.',
    '- Auditoría ES/EN regenerada desde el árbol real posterior a las reparaciones.',
    f'- Manifiestos con recorte material detectado: **{len(bad)}**.',
    f'- Manifiestos con marcador ES/EN incompleto: **{len(missing)}**.',
    ''
]
Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_final_indices_paridad_ES_EN.md').write_text('\n'.join(out),encoding='utf-8')
print('FINAL_CHECKS',checks)
if status != 'OK':
    if bad: print('\n'.join(bad))
    if missing: print('\n'.join(missing))
    raise SystemExit('FINAL_POSTCHECK=FAIL')
print('FINAL_POSTCHECK=OK')