from pathlib import Path
from urllib.parse import unquote
import re

root = Path('.').resolve()
report = root / 'auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN.md'
manifest_index = root / 'manifiestos/README.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
latest = root / 'manifiestos/56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md'

markdown_files = sorted(p for p in root.rglob('*.md') if '.git' not in p.parts)
readmes = sorted(p for p in markdown_files if p.name.startswith('README'))
leeme = root / 'LEEME.md'
if leeme.exists() and leeme not in readmes:
    readmes.append(leeme)

link_re = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
internal_checked = 0
external_seen = 0
anchor_only = 0
broken = []

for f in markdown_files:
    text = f.read_text(encoding='utf-8', errors='replace')
    for raw in link_re.findall(text):
        target = raw.strip()
        if not target:
            continue
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1].strip()
        # Remove optional Markdown title only when clearly quoted after whitespace.
        target = re.sub(r'\s+["\'][^"\']*["\']\s*$', '', target)
        low = target.lower()
        if low.startswith(('http://','https://','mailto:','tel:','data:')):
            external_seen += 1
            continue
        if target.startswith('#'):
            anchor_only += 1
            continue
        clean = unquote(target.split('#',1)[0].split('?',1)[0]).strip()
        if not clean:
            anchor_only += 1
            continue
        internal_checked += 1
        p = (root / clean.lstrip('/')).resolve() if clean.startswith('/') else (f.parent / clean).resolve()
        try:
            p.relative_to(root)
        except ValueError:
            broken.append((f.relative_to(root).as_posix(), target, 'fuera del repositorio / outside repository'))
            continue
        if not p.exists():
            broken.append((f.relative_to(root).as_posix(), target, 'destino inexistente / missing target'))

idx = manifest_index.read_text(encoding='utf-8')
net = re.search(r'<!-- NEO_ALL_MANIFESTOS_START -->(.*?)<!-- NEO_ALL_MANIFESTOS_END -->', idx, re.S)
canonical = []
if net:
    seen=set()
    for roman, href in re.findall(r'- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', net.group(1)):
        p=(manifest_index.parent/href).resolve()
        if p not in seen:
            seen.add(p); canonical.append((roman,p))

critical=[]
if len(canonical)!=56 or not canonical or canonical[-1][0] != 'LVI':
    critical.append(f'Colección canónica inesperada: {len(canonical)} manifiestos; último={canonical[-1][0] if canonical else "ninguno"}.')
if not latest.exists():
    critical.append('Falta el manifiesto LVI.')
ss=synth_index.read_text(encoding='utf-8')
if '## Índice canónico · I–LVI' not in ss:
    critical.append('El índice de Síntesis Abierta no declara I–LVI.')
if latest.name not in ss or 'issues/76' not in ss:
    critical.append('La Síntesis Abierta no enlaza correctamente LVI / Issue #76.')

latest_markers=0
latest_bad=[]
for f in readmes:
    text=f.read_text(encoding='utf-8',errors='replace')
    if '<!-- NEO_LATEST_MANIFESTO_START -->' in text:
        latest_markers += 1
        m=re.search(r'<!-- NEO_LATEST_MANIFESTO_START -->(.*?)<!-- NEO_LATEST_MANIFESTO_END -->',text,re.S)
        if not m or 'LVI' not in m.group(1) or 'issues/76' not in m.group(1):
            latest_bad.append(f.relative_to(root).as_posix())
if latest_bad:
    critical.append('README con bloque latest desincronizado: '+', '.join(latest_bad))

status = 'OK' if not broken and not critical else 'REQUIERE CORRECCIÓN / NEEDS CORRECTION'
lines = [
    '# Postcheck LVI · NO-CONTROL™ · README, índices y enlaces / README, indices and links',
    '',
    '**Fecha / Date:** 2026-08-09  ',
    f'**Estado / Status:** **{status}**',
    '',
    '## ES · Resultado',
    '',
    f'- Archivos Markdown revisados: **{len(markdown_files)}**.',
    f'- README/LEEME revisados: **{len(readmes)}**.',
    f'- Enlaces internos de ruta comprobados: **{internal_checked}**.',
    f'- Enlaces externos inventariados sin comprobar disponibilidad remota: **{external_seen}**.',
    f'- Enlaces sólo a ancla detectados: **{anchor_only}**.',
    f'- Bloques de último manifiesto encontrados en README/LEEME: **{latest_markers}**.',
    f'- Manifiestos canónicos detectados: **{len(canonical)} · I–{canonical[-1][0] if canonical else "?"}**.',
    f'- Enlaces internos rotos detectados: **{len(broken)}**.',
    f'- Fallos canónicos críticos: **{len(critical)}**.',
    '',
    '### Comprobaciones canónicas',
    '',
    '- LVI debe ser el último manifiesto canónico.',
    '- La colección debe declarar 56 manifiestos I–LVI.',
    '- Síntesis Abierta debe enlazar LVI y el Issue #76.',
    '- Los README con bloque `NEO_LATEST_MANIFESTO` deben apuntar a LVI / #76.',
    '',
]
if critical:
    lines += ['### Fallos canónicos', ''] + [f'- {x}' for x in critical] + ['']
if broken:
    lines += ['### Enlaces internos rotos', '', '| Origen | Destino | Motivo |', '|---|---|---|']
    for src,target,why in broken:
        lines.append(f'| `{src}` | `{target}` | {why} |')
    lines.append('')
else:
    lines += ['### Enlaces internos rotos', '', '- Ninguno detectado por el validador de rutas del repositorio.', '']

lines += [
    '## EN · Result',
    '',
    f'- Markdown files reviewed: **{len(markdown_files)}**.',
    f'- README/LEEME files reviewed: **{len(readmes)}**.',
    f'- Internal path links checked: **{internal_checked}**.',
    f'- Broken internal links found: **{len(broken)}**.',
    f'- Canonical critical failures: **{len(critical)}**.',
    '',
    'External URL availability and rendered GitHub anchor semantics are not asserted by this local-path validator.',
    '',
    '**Innova_N · NEOCore™ · Neodialectica Framework™ / Network**',
]
report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'POSTCHECK_STATUS={status}')
print(f'MARKDOWN_FILES={len(markdown_files)} README_LEEME={len(readmes)} INTERNAL_LINKS={internal_checked} BROKEN={len(broken)} CRITICAL={len(critical)}')
