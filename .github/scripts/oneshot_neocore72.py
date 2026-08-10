from pathlib import Path
import re
import subprocess
import sys

# Final closure for NEOCore™ 7.2 after the main 7.2 integration has passed.

# 1. Complete Open Synthesis index.
p=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md')
s=p.read_text(encoding='utf-8')
s=s.replace(
    '65 manifiestos finitos I–LXV + Manifiesto ∞ · 14 Neoaxiomas™',
    '68 manifiestos finitos I–LXVIII + Manifiesto ∞ · 14 Neoaxiomas™'
).replace(
    '65 finite manifestos I–LXV + Manifesto ∞ · 14 Neoaxioms™',
    '68 finite manifestos I–LXVIII + Manifesto ∞ · 14 Neoaxioms™'
)
if '| LXVI | [NeoSinergia™]' not in s:
    infinity='| ∞ | [Neo0™ · Puerta Abierta del Fractal](../../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md) | [#106](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/106) |'
    rows='''| LXVI | [NeoSinergia™](../../manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md) | [#110](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/110) |
| LXVII | [NeoTitanes™ · Reconstrucción Sistémica y Motor del Bien Común](../../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md) | [#112](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/112) |
| LXVIII | [Los Conflictos que No Son Nuestros™ · Soberanía Intelectual de la Especie](../../manifiestos/68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md) | [#114](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/114) |'''
    if infinity not in s:
        raise SystemExit('∞ row missing in complete synthesis index')
    s=s.replace(infinity,rows+'\n'+infinity,1)
p.write_text(s,encoding='utf-8')

# 2. Remove historical duplicate entry route, preserving managed canonical block.
p=Path('propuestas/sintesis-abierta/README.md')
s=p.read_text(encoding='utf-8')
end='<!-- NEO_ENTRY_REGISTER_ROUTE_END -->'
if s.count('### 1. Registrar entrada / Register entry') > 1:
    pat=re.compile(
        re.escape(end)+r'\n\n### 1\. Registrar entrada / Register entry.*?(?=\n### 2\. Contrastar un manifiesto o Neoaxioma / Challenge a manifesto or Neoaxiom)',
        re.S,
    )
    s,n=pat.subn(end+'\n',s,count=1)
    if n != 1:
        raise SystemExit('Could not remove duplicate entry-register section')
p.write_text(s,encoding='utf-8')

# 3. Regenerate actual bilingual parity report after 7.2.
subprocess.run([sys.executable,'.github/scripts/audit_es_en_parity.py'],check=True)
parity=Path('auditorias/publicas/2026-08-09_auditoria_paridad_ES_EN_manifiestos_articulos.md').read_text(encoding='utf-8')
flagged=parity.split('## Casos marcados',1)[1].split('## ',1)[0] if '## Casos marcados' in parity else ''
bad=[line for line in flagged.splitlines() if re.match(r'^\| `manifiestos/.*\.md` \|',line)]
missing=[]
if '## Marcadores incompletos' in parity:
    block=parity.split('## Marcadores incompletos',1)[1].split('## ',1)[0]
    missing=[line for line in block.splitlines() if '`manifiestos/' in line]
if bad or missing:
    print('\n'.join(bad+missing))
    raise SystemExit('MANIFESTO_PARITY=FAIL')

# 4. Final postcheck.
idx=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md').read_text(encoding='utf-8')
syn=Path('propuestas/sintesis-abierta/README.md').read_text(encoding='utf-8')
base=Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_soberania_sintesis_web4_ES_EN.md').read_text(encoding='utf-8')
pos=[idx.find('| LXVI |'),idx.find('| LXVII |'),idx.find('| LXVIII |'),idx.find('| ∞ |')]
checks={
    'base_postcheck_OK':'**Estado / Status:** **OK**' in base,
    'complete_index_68':'68 manifiestos finitos I–LXVIII' in idx,
    'complete_index_recent_nodes':all(x >= 0 for x in pos) and pos == sorted(pos),
    'open_synthesis_single_entry_route':syn.count('### 1. Registrar entrada / Register entry') == 1,
    'parity_report_current':'**Fecha:** 2026-08-10' in parity,
    'parity_no_flagged_manifest':not bad,
    'parity_no_missing_manifest':not missing,
}
status='OK' if all(checks.values()) else 'REQUIERE CORRECCIÓN'
out=[
    '# Cierre de integración · NEOCore™ 7.2 · índices y paridad ES/EN / Final integration check','',
    '**Fecha / Date:** 2026-08-10  ',f'**Estado / Status:** **{status}**','',
    '## Verificaciones / Checks',''
]
out += [f'- [{"x" if ok else " "}] `{k}`' for k,ok in checks.items()]
out += [
    '', '## Resultado', '',
    '- **68 manifiestos finitos · I–LXVIII + ∞** reflejados en el índice completo de Síntesis Abierta.',
    '- **NAX-01–NAX-14** permanecen canónicos; los candidatos 7.2 siguen explícitamente como candidatos, sin promoción automática.',
    '- **NEOCore™ 7.2** conserva la capa 7.1 y añade Soberanía de Síntesis™, incluida la diferenciación futura Innova_N Fundación / Corporación.',
    '- **WEB4™** continúa etiquetada como DEMO/prototipo público; NeoCronos™ permanece experimental, multidimensional y revisable.',
    '- Auditoría ES/EN regenerada después del delta 7.2.',
    ''
]
Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_final_indices_paridad_ES_EN.md').write_text('\n'.join(out),encoding='utf-8')
if status != 'OK':
    raise SystemExit('FINAL_POSTCHECK=FAIL')
print('FINAL_POSTCHECK=OK')
