from pathlib import Path
import os
import re
import urllib.parse

ROOT = Path('.').resolve()
EXCLUDED = {'.git', 'node_modules', 'vendor', '.venv', 'dist', 'build'}
START = '<!-- NEO_CURRENT_NAV_START -->'
END = '<!-- NEO_CURRENT_NAV_END -->'


def excluded(p: Path) -> bool:
    return any(part in EXCLUDED for part in p.parts)


def rel(from_file: Path, target: Path) -> str:
    value = os.path.relpath(target, start=from_file.parent)
    if not value.startswith('.'):
        value = './' + value
    return value.replace(os.sep, '/')


readmes = sorted(p for p in Path('.').rglob('README.md') if not excluded(p))
if not readmes:
    raise SystemExit('No README.md files found')

targets = {
    'manifestos': Path('manifiestos/README.md'),
    'xl42': Path('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'),
    'synthesis': Path('propuestas/sintesis-abierta/README.md'),
    'projection': Path('proyeccion/PROTOCOLO_PROYECCION_DISTRIBUIDA_NEODIALECTICA_ES_EN.md'),
    'wiki_manifestos': Path('wiki-source/Manifiestos.md'),
    'root': Path('README.md'),
}
for label, target in targets.items():
    if not target.exists():
        raise SystemExit(f'Missing canonical target {label}: {target}')


def nav_block(p: Path) -> str:
    return f'''{START}

---

## Estado canónico actual · Current canonical state

**Neodialectica Framework™ / Network · Innova_N · NEOCore™**

- Colección pública actual: **42 manifiestos bilingües · I–XLII · diez oleadas** / Current public collection: **42 bilingual manifestos · I–XLII · ten waves**.
- Último manifiesto / Latest manifesto: [XLII · Fin de la Era del Hombre Manipulado™ · End of the Manipulated Human Era™]({rel(p, targets['xl42'])}).
- Índice completo / Complete index: [Manifiestos / Manifestos]({rel(p, targets['manifestos'])}).
- Contraste público / Public contrast: [Síntesis Abierta / Open Synthesis]({rel(p, targets['synthesis'])}).
- Expansión y redundancia / Expansion and redundancy: [Protocolo de Proyección Distribuida Neodialéctica™]({rel(p, targets['projection'])}).
- Fuente Wiki versionada / Versioned Wiki source: [Manifiestos]({rel(p, targets['wiki_manifestos'])}).
- Nodo raíz / Root node: [README principal]({rel(p, targets['root'])}).

**Principio de procedencia / Provenance principle:** la fuente intelectual y genealógica es **Innova_N**, dentro de **NEOCore™ / Neodialectica Framework™ / Network**, bajo dirección humana de **Pedro Martínez Alhambra · Neo0™**. GitHub es la primera proyección WEB4™ pública, versionada y trazable; no es el origen intelectual del sistema. / The intellectual and genealogical source is **Innova_N**, within **NEOCore™ / Neodialectica Framework™ / Network**, under the human direction of **Pedro Martínez Alhambra · Neo0™**. GitHub is the first public, versioned and traceable WEB4™ projection; it is not the intellectual origin of the system.

{END}'''


changed = []
for p in readmes:
    text = p.read_text(encoding='utf-8')
    block = nav_block(p)
    if START in text and END in text:
        pattern = re.compile(re.escape(START) + r'.*?' + re.escape(END), re.S)
        new_text = pattern.sub(block, text, count=1)
    else:
        new_text = text.rstrip() + '\n\n' + block + '\n'
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        changed.append(str(p))

# Repository-local Markdown link validation for every README.
link_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
broken = []
checked = 0
for p in readmes:
    text = p.read_text(encoding='utf-8')
    for raw in link_re.findall(text):
        url = raw.strip().split()[0].strip('<>')
        if not url or url.startswith(('#', 'http://', 'https://', 'mailto:', 'tel:', 'data:')):
            continue
        url = urllib.parse.unquote(url)
        pathpart = url.split('#', 1)[0].split('?', 1)[0]
        if not pathpart:
            continue
        checked += 1
        target = (p.parent / pathpart).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            broken.append((str(p), raw, 'outside repository'))
            continue
        if not target.exists():
            broken.append((str(p), raw, str(target.relative_to(ROOT))))

manifesto_text = Path('manifiestos/README.md').read_text(encoding='utf-8')
required = [
    'XLII',
    '42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md',
    'issues/50',
    'PROTOCOLO_PROYECCION_DISTRIBUIDA_NEODIALECTICA_ES_EN.md',
    'I–XLII',
]
missing = [item for item in required if item not in manifesto_text]

report = Path('auditorias/publicas/2026-08-08_auditoria_readmes_enlaces_estado_XLII_ES_EN.md')
lines = [
    '# Auditoría de README, enlaces y estado XLII / README, links and XLII-state audit',
    '',
    '**Fecha / Date:** 2026-08-08',
    '',
    '## ES · Resultado',
    '',
    f'- README.md detectados y revisados: **{len(readmes)}**.',
    f'- Enlaces Markdown internos comprobados: **{checked}**.',
    f'- README actualizados con bloque canónico de navegación y procedencia: **{len(changed)}**.',
    f'- Enlaces internos rotos detectados tras la actualización: **{len(broken)}**.',
    f'- Requisitos faltantes en `manifiestos/README.md`: **{len(missing)}**.',
    '',
    '### README revisados',
    '',
]
lines.extend(f'- `{p}`' for p in readmes)
lines.extend(['', '### Enlaces internos rotos', ''])
if broken:
    lines.extend(f'- `{f}` → `{u}` → objetivo resuelto: `{t}`' for f, u, t in broken)
else:
    lines.append('- Ninguno detectado por el validador de rutas relativas.')
lines.extend(['', '### Estado del índice de manifiestos', ''])
if missing:
    lines.append('Faltan marcadores requeridos: ' + ', '.join(f'`{x}`' for x in missing))
else:
    lines.append('`manifiestos/README.md` contiene XLII, el fichero XLII, la Síntesis Abierta #50, el índice I–XLII y el Protocolo de Proyección Distribuida.')
lines.extend([
    '',
    '## EN · Result',
    '',
    f'- README.md files detected and reviewed: **{len(readmes)}**.',
    f'- Internal Markdown links checked: **{checked}**.',
    f'- README files synchronised with canonical navigation and provenance block: **{len(changed)}**.',
    f'- Broken internal links detected after synchronisation: **{len(broken)}**.',
    f'- Missing requirements in `manifiestos/README.md`: **{len(missing)}**.',
    '',
    'This audit validates repository-local relative paths. External URL availability and rendered anchor semantics require separate checks.',
    '',
    '**Innova_N · NEOCore™ · Neodialectica Framework™ / Network**',
])
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text('\n'.join(lines) + '\n', encoding='utf-8')

# Remove one-shot files before commit.
Path('.github/workflows/one-shot-audit-readmes-xl42.yml').unlink(missing_ok=True)
Path('.github/scripts/audit_readmes_xl42.py').unlink(missing_ok=True)

print(f'READMES={len(readmes)} CHECKED={checked} BROKEN={len(broken)} CHANGED={len(changed)} MISSING={len(missing)}')
