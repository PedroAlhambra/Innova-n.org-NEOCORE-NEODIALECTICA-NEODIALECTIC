from pathlib import Path
from urllib.parse import unquote
import re

root = Path('.').resolve()
report = root / 'auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN.md'
manifest_index = root / 'manifiestos/README.md'
synth_entry = root / 'propuestas/sintesis-abierta/README.md'
synth_index = root / 'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

# Historical archives deliberately preserve old Wiki topology, including links
# to pages that no longer exist in the living Wiki. They must remain untouched
# and must not make the current documentary graph fail.
EXCLUDED_TOP_LEVEL = {'wiki-legacy-archive'}
LEGACY_ENTRY_FILES = {
    root / 'LEEME.md',
    root / 'PORTADA.md',
    root / 'COVER.md',
    root / 'PREFACIO.md',
    root / 'FOREWORD.md',
}
all_markdown = sorted(p for p in root.rglob('*.md') if '.git' not in p.parts)
archived_markdown = [p for p in all_markdown if p.relative_to(root).parts and p.relative_to(root).parts[0] in EXCLUDED_TOP_LEVEL]
legacy_entry_markdown = [p for p in all_markdown if p in LEGACY_ENTRY_FILES]
markdown_files = [p for p in all_markdown if p not in archived_markdown and p not in legacy_entry_markdown]
readmes = sorted(p for p in markdown_files if p.name.startswith('README'))

link_re = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
internal_checked = 0
external_seen = 0
anchor_only = 0
wiki_aliases = 0
broken = []

for f in markdown_files:
    text = f.read_text(encoding='utf-8', errors='replace')
    for raw in link_re.findall(text):
        target = raw.strip()
        if not target:
            continue
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1].strip()
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

        # A live document may explicitly link to a historical/legacy file; the
        # target remains valid while migration is in progress. Its internal
        # links are simply excluded from living-state enforcement.
        if p.exists():
            continue

        # GitHub Wiki source uses extensionless page aliases.
        wiki_candidate = p.with_suffix('.md') if f.parent.name == 'wiki-source' and not Path(clean).suffix else None
        if wiki_candidate and wiki_candidate.exists():
            wiki_aliases += 1
            continue
        broken.append((f.relative_to(root).as_posix(), target, 'destino inexistente / missing target'))

# Canonical collection is the explicit ordered list in manifiestos/README.md.
idx = manifest_index.read_text(encoding='utf-8')
canonical=[]; seen=set()
for roman, href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', idx, re.M):
    p=(manifest_index.parent/href).resolve()
    if p.exists() and p not in seen:
        seen.add(p); canonical.append((roman,p))

critical=[]
latest_roman=canonical[-1][0] if canonical else None
latest=canonical[-1][1] if canonical else None
count=len(canonical)
issue_num=None
if latest:
    lt=latest.read_text(encoding='utf-8',errors='replace')
    ims=re.findall(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)',lt)
    issue_num=ims[0] if ims else None

if not canonical:
    critical.append('No se pudo reconstruir la colección canónica desde el índice. / The canonical collection could not be reconstructed from the index.')
if latest and not latest.exists():
    critical.append(f'Falta el último manifiesto {latest_roman}. / Latest manifesto {latest_roman} is missing.')

# The complete synthesis index owns the dynamic inventory/frontier. The
# operational README owns participation routes and must not be forced to repeat
# the numerical corpus state.
ss=synth_index.read_text(encoding='utf-8')
se=synth_entry.read_text(encoding='utf-8')
if canonical:
    if f'I–{latest_roman}' not in ss:
        critical.append(f'El índice completo de Síntesis Abierta no declara I–{latest_roman}. / The complete Open Synthesis index does not declare I–{latest_roman}.')
    if latest.name not in ss:
        critical.append(f'El índice completo de Síntesis no enlaza el último manifiesto {latest_roman}. / The complete Synthesis index does not link the latest manifesto {latest_roman}.')
    if issue_num and f'issues/{issue_num}' not in ss:
        critical.append(f'El índice completo de Síntesis no enlaza el Issue #{issue_num} del último manifiesto {latest_roman}. / The complete Synthesis index does not link Issue #{issue_num} for the latest manifesto {latest_roman}.')
if 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md' not in se:
    critical.append('El README operativo de Síntesis no enlaza el índice completo. / The operational Synthesis README does not link the complete index.')
if 'REGISTRO_ENTRADA_TRAZABLE_DERIVACION_ES_EN.md' not in se:
    critical.append('El README operativo de Síntesis no enlaza el registro de entrada. / The operational Synthesis README does not link the entry register.')
if '# ES · Castellano' not in se or '# EN · English' not in se:
    critical.append('El README operativo de Síntesis no conserva división bilingüe ES/EN. / The operational Synthesis README does not preserve the ES/EN bilingual split.')

stale_current_nav=[]
for f in readmes:
    text=f.read_text(encoding='utf-8',errors='replace')
    if '<!-- NEO_CURRENT_NAV_START -->' in text or '<!-- NEO_CURRENT_NAV_END -->' in text:
        stale_current_nav.append(f.relative_to(root).as_posix())
if stale_current_nav:
    critical.append('README con bloque legacy NEO_CURRENT_NAV: '+', '.join(stale_current_nav)+' / README with legacy NEO_CURRENT_NAV block: '+', '.join(stale_current_nav))

latest_markers=0
latest_bad=[]
for f in readmes:
    text=f.read_text(encoding='utf-8',errors='replace')
    if '<!-- NEO_LATEST_MANIFESTO_START -->' in text:
        latest_markers += 1
        m=re.search(r'<!-- NEO_LATEST_MANIFESTO_START -->(.*?)<!-- NEO_LATEST_MANIFESTO_END -->',text,re.S)
        body=m.group(1) if m else ''
        if not m or (latest_roman and latest_roman not in body) or (issue_num and f'issues/{issue_num}' not in body):
            latest_bad.append(f.relative_to(root).as_posix())
if latest_bad:
    critical.append('README con bloque latest desincronizado / README with unsynchronised latest block: '+', '.join(latest_bad))

status = 'OK' if not broken and not critical else 'REQUIERE CORRECCIÓN / NEEDS CORRECTION'
latest_desc=f'{latest_roman} / #{issue_num}' if latest_roman and issue_num else (latest_roman or '?')
lines = [
    '# Postcheck dinámico · README, índices y enlaces / Dynamic README, indices and links postcheck',
    '',
    '**Fecha / Date:** 2026-08-12  ',
    f'**Estado / Status:** **{status}**',
    '',
    '> **Alcance / Scope:** el grafo vivo excluye `wiki-legacy-archive/` y las entradas raíz legacy `LEEME.md`, `PORTADA.md`, `COVER.md`, `PREFACIO.md` y `FOREWORD.md`. Esos nombres legacy no constituyen superficies canónicas vivas; tras su retirada de `main`, su contenido histórico permanece recuperable mediante Git. / the living graph excludes `wiki-legacy-archive/` and the root legacy entry files `LEEME.md`, `PORTADA.md`, `COVER.md`, `PREFACIO.md` and `FOREWORD.md`. Those legacy names are not living canonical surfaces; after retirement from `main`, their historical contents remain recoverable through Git.',
    '',
    '## ES · Resultado',
    '',
    f'- Archivos Markdown activos revisados: **{len(markdown_files)}**.',
    f'- Archivos Markdown históricos excluidos del estado vivo: **{len(archived_markdown)}**.',
    f'- Entradas legacy excluidas del estado vivo: **{len(legacy_entry_markdown)}**.',
    f'- README activos revisados: **{len(readmes)}**.',
    f'- Enlaces internos de ruta comprobados: **{internal_checked}**.',
    f'- Alias internos de GitHub Wiki reconocidos: **{wiki_aliases}**.',
    f'- Enlaces externos inventariados sin comprobar disponibilidad remota: **{external_seen}**.',
    f'- Enlaces sólo a ancla detectados: **{anchor_only}**.',
    f'- Bloques de último manifiesto encontrados en README: **{latest_markers}**.',
    f'- Bloques legacy NEO_CURRENT_NAV encontrados en README: **{len(stale_current_nav)}**.',
    f'- Manifiestos canónicos detectados: **{count} · I–{latest_roman or "?"}**.',
    f'- Último manifiesto / Síntesis: **{latest_desc}**.',
    f'- Enlaces internos rotos del grafo vivo: **{len(broken)}**.',
    f'- Fallos canónicos críticos: **{len(critical)}**.',
    '',
    '### Comprobaciones canónicas',
    '',
    '- La colección se reconstruye dinámicamente desde `manifiestos/README.md`; no se fija un número histórico en el auditor.',
    '- El índice completo de Síntesis Abierta debe enlazar el último manifiesto y su Issue específico.',
    '- El README operativo de Síntesis debe conservar las rutas de participación sin duplicar el inventario dinámico.',
    '- Los README con bloque `NEO_LATEST_MANIFESTO` deben apuntar al último manifiesto y su Síntesis.',
    '- Los README vivos no pueden conservar bloques `NEO_CURRENT_NAV`: la frontera numérica pertenece a los índices canónicos dinámicos.',
    '- El archivo Wiki histórico se conserva como evidencia y no se reescribe para simular vigencia.',
    '- La auditoría de rutas no sustituye la comprobación remota de URLs externas ni la validación semántica de anclas renderizadas.',
    '',
]
if critical:
    lines += ['### Fallos canónicos', ''] + [f'- {x}' for x in critical] + ['']
if broken:
    lines += ['### Enlaces internos rotos del grafo vivo', '', '| Origen | Destino | Motivo |', '|---|---|---|']
    for src,target,why in broken:
        lines.append(f'| `{src}` | `{target}` | {why} |')
    lines.append('')
else:
    lines += ['### Enlaces internos rotos del grafo vivo', '', '- Ninguno detectado por el validador de rutas del repositorio.', '']

lines += [
    '## EN · Result',
    '',
    f'- Active Markdown files reviewed: **{len(markdown_files)}**.',
    f'- Historical Markdown files excluded from living-state health: **{len(archived_markdown)}**.',
    f'- Legacy entry files excluded from living-state health: **{len(legacy_entry_markdown)}**.',
    f'- Active README files reviewed: **{len(readmes)}**.',
    f'- Internal path links checked: **{internal_checked}**.',
    f'- GitHub Wiki extensionless page aliases recognised: **{wiki_aliases}**.',
    f'- External links inventoried without checking remote availability: **{external_seen}**.',
    f'- Anchor-only links detected: **{anchor_only}**.',
    f'- Latest-manifesto blocks found in README files: **{latest_markers}**.',
    f'- Legacy NEO_CURRENT_NAV blocks found in README files: **{len(stale_current_nav)}**.',
    f'- Canonical manifestos detected: **{count} · I–{latest_roman or "?"}**.',
    f'- Latest manifesto / synthesis: **{latest_desc}**.',
    f'- Broken internal links in the living graph: **{len(broken)}**.',
    f'- Canonical critical failures: **{len(critical)}**.',
    '',
    '### Canonical checks',
    '',
    '- The collection is reconstructed dynamically from `manifiestos/README.md`; the auditor does not hardcode a historical number.',
    '- The complete Open Synthesis index must link the latest manifesto and its specific Issue.',
    '- The operational Synthesis README must preserve participation routes without duplicating the dynamic inventory.',
    '- README files with a `NEO_LATEST_MANIFESTO` block must point to the latest manifesto and its Synthesis.',
    '- Living README files may not retain `NEO_CURRENT_NAV` blocks: the numerical frontier belongs to dynamic canonical indexes.',
    '- The historical Wiki archive is preserved as evidence and is not rewritten to simulate current validity.',
    '- The route audit does not replace remote checking of external URLs or semantic validation of rendered anchors.',
    '',
]
if critical:
    lines += ['### Canonical failures', ''] + [f'- {x}' for x in critical] + ['']
if broken:
    lines += ['### Broken internal links in the living graph', '', '| Source | Target | Reason |', '|---|---|---|']
    for src,target,why in broken:
        lines.append(f'| `{src}` | `{target}` | {why} |')
    lines.append('')
else:
    lines += ['### Broken internal links in the living graph', '', '- None detected by the repository route validator.', '']

lines += [
    '**Innova_N · NEOCore™ · Neodialectica Framework™ / Network**',
]
report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'POSTCHECK_STATUS={status}')
print(f'MARKDOWN_ACTIVE={len(markdown_files)} ARCHIVED_EXCLUDED={len(archived_markdown)} LEGACY_ENTRY_EXCLUDED={len(legacy_entry_markdown)} README={len(readmes)} CANONICAL={count} LATEST={latest_roman} ISSUE={issue_num} INTERNAL_LINKS={internal_checked} WIKI_ALIASES={wiki_aliases} BROKEN={len(broken)} CRITICAL={len(critical)}')