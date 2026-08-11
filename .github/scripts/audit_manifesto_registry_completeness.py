from pathlib import Path
import json
import re

ROOT=Path('.').resolve()
MDIR=ROOT/'manifiestos'
REG=MDIR/'CANONICAL_FILENAMES.json'
REPORT=ROOT/'auditorias/publicas/2026-08-12_auditoria_registro_canonico_manifiestos_ES_EN.md'
TITLE=re.compile(r'^#\s+([IVXLCDM]+)\s*·\s*(.+?)\s*$',re.M)
META=re.compile(r'^\*\*Manifiesto / Manifesto:\*\*\s*([IVXLCDM]+)\s*$',re.M)


def expected_canonical(roman,legacy_path):
    name=Path(legacy_path).name
    stem=name[:-3] if name.endswith('.md') else name
    stem=re.sub(r'^\d+_', '', stem)
    return f'manifiestos/canonicos/{roman}_{stem}.md'

entries=json.loads(REG.read_text(encoding='utf-8')).get('entries',{})
by_ord={r:(ROOT/v['legacy']).resolve() for r,v in entries.items()}
problems=[]
seen_sources={}

for p in sorted(MDIR.glob('[0-9]*_ES_EN.md')):
    text=p.read_text(encoding='utf-8',errors='replace')
    tm=TITLE.search(text[:5000]); mm=META.search(text[:6000])
    if not tm or not mm:
        continue
    roman=tm.group(1)
    if mm.group(1)!=roman:
        problems.append((p,roman,'ordinal H1 ≠ metadato / H1 ordinal ≠ metadata'))
        continue
    seen_sources.setdefault(roman,[]).append(p.resolve())
    if roman not in by_ord:
        problems.append((p,roman,'manifiesto con identidad válida no registrado / valid manifesto identity not registered'))

for roman,entry in entries.items():
    p=(ROOT/entry['legacy']).resolve()
    expected=expected_canonical(roman,entry['legacy'])
    canonical=(ROOT/entry.get('canonical','')).resolve()
    if entry.get('canonical') != expected:
        problems.append((ROOT/entry.get('canonical',''),roman,f'ruta canónica no determinista; esperada `{expected}` / non-deterministic canonical path; expected `{expected}`'))
    if not p.exists():
        problems.append((p,roman,'fuente registrada inexistente / registered source missing'))
        continue
    text=p.read_text(encoding='utf-8',errors='replace')
    tm=TITLE.search(text[:5000]); mm=META.search(text[:6000])
    if not tm or not mm or tm.group(1)!=roman or mm.group(1)!=roman:
        problems.append((p,roman,'identidad del registro no coincide con la fuente / registry identity does not match source'))
    if not canonical.exists():
        problems.append((canonical,roman,'espejo canónico inexistente / canonical mirror missing'))
    else:
        ct=canonical.read_text(encoding='utf-8',errors='replace')
        ctm=TITLE.search(ct[:5000]); cmm=META.search(ct[:6000])
        if not ctm or not cmm or ctm.group(1)!=roman or cmm.group(1)!=roman:
            problems.append((canonical,roman,'identidad del espejo canónico incorrecta / canonical mirror identity incorrect'))

lines=[
'# Auditoría de completitud del registro canónico de manifiestos / Canonical manifesto registry completeness audit','',
'**Fecha / Date:** 2026-08-12  ',
f'**Entradas canónicas / Canonical entries:** {len(entries)}  ',
f'**Problemas / Problems:** {len(problems)}','',
'## Regla / Rule','',
'Un archivo de manifiesto con ordinal romano y metadato `Manifiesto / Manifesto` válidos no puede quedar fuera de `CANONICAL_FILENAMES.json`. La ruta del espejo canónico se deriva de forma determinista de la fuente y debe terminar en `.md`; el espejo debe existir y conservar la misma identidad romana. Los duplicados históricos de un ordinal ya registrado pueden conservarse como rutas legacy, pero no crean un segundo nodo canónico. / A manifesto file with a valid Roman ordinal and `Manifesto` identity metadata may not remain outside `CANONICAL_FILENAMES.json`. The canonical mirror path is derived deterministically from the source and must end in `.md`; the mirror must exist and preserve the same Roman identity. Historical duplicate routes for an already registered ordinal may be preserved as legacy routes, but do not create a second canonical node.','',
'## Hallazgos / Findings','']
if problems:
    lines += ['| Nº | Archivo | Problema |','|---|---|---|']
    for p,r,msg in problems:
        try: rel=p.relative_to(ROOT).as_posix()
        except Exception: rel=str(p)
        lines.append(f'| {r} | `{rel}` | {msg} |')
else:
    lines.append('- Ninguno / None.')
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'MANIFESTO_REGISTRY_AUDIT canonical={len(entries)} problems={len(problems)}')
if problems:
    raise SystemExit('Unregistered, malformed or missing canonical manifesto detected')
