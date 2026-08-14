from pathlib import Path
import json
import re

ROOT = Path('.').resolve()
REGISTRY = ROOT / 'manifiestos' / 'CANONICAL_FILENAMES.json'
INDEX_TARGETS = [
    ROOT / 'manifiestos' / 'README.md',
    ROOT / 'manifiestos' / 'RELACIONES_TRABAJO_APLICADO_ES_EN.md',
    ROOT / 'manifiestos' / 'RELACIONES_LVII_LIX_ES_EN.md',
    ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md',
]
TITLE_LINE = re.compile(r'^#\s+([IVXLCDM]+|∞)\s*·\s*(.+?)\s*$')
ES_MARK = re.compile(r'^#\s+ES\s+·\s+(?:Castellano|Español)\s*$')
META_MAN = re.compile(r'^\*\*Manifiesto / Manifesto:\*\*\s*([IVXLCDM]+|∞)\s*$')


def parse_titles(text, roman):
    lines=text.splitlines()
    pre=[]
    for line in lines:
        if ES_MARK.match(line):
            break
        pre.append(line)
    hits=[]
    for i,line in enumerate(pre):
        m=TITLE_LINE.match(line)
        if m and m.group(1)==roman:
            hits.append((i,m.group(2).strip()))
    return lines,hits


def normalize_source(path, roman):
    text=path.read_text(encoding='utf-8')
    lines,hits=parse_titles(text,roman)
    changed=False

    # Historical early manifestos stored both language names in one H1.
    # Split only when there is no second ordinal H1 and an explicit separator exists.
    if len(hits)==1 and ' / ' in hits[0][1]:
        pos,title=hits[0]
        es,en=title.split(' / ',1)
        lines[pos:pos+1]=[f'# {roman} · {es.strip()}', f'# {roman} · {en.strip()}']
        changed=True
        text='\n'.join(lines)+'\n'
        lines,hits=parse_titles(text,roman)

    if len(hits)<2:
        raise SystemExit(f'Cannot establish bilingual H1 pair for {roman}: {path}')
    es_title=hits[0][1].strip(); en_title=hits[1][1].strip()

    # Every manifesto uses the same bilingual identity metadata.
    pre_end=next((i for i,l in enumerate(lines) if ES_MARK.match(l)), len(lines))
    has_meta=False
    for line in lines[:pre_end]:
        m=META_MAN.match(line)
        if m:
            if m.group(1)!=roman:
                raise SystemExit(f'Wrong manifesto ordinal metadata in {path}: {m.group(1)} != {roman}')
            has_meta=True
            break
    if not has_meta:
        title_positions=[i for i,l in enumerate(lines[:pre_end]) if (lambda m: bool(m and m.group(1)==roman))(TITLE_LINE.match(l))]
        insert_at=max(title_positions)+1
        while insert_at < len(lines) and lines[insert_at]=='' and insert_at+1 < len(lines) and lines[insert_at+1]=='':
            lines.pop(insert_at)
        lines[insert_at:insert_at]=['', f'**Manifiesto / Manifesto:** {roman}  ']
        changed=True

    new='\n'.join(lines)+'\n'
    if changed and new!=path.read_text(encoding='utf-8'):
        path.write_text(new,encoding='utf-8')
    return es_title,en_title,changed


def replace_link_label(text, filename, label):
    # Every link on canonical inventory/index surfaces whose target is a
    # manifesto source uses the same bilingual visible name. Operational
    # language-specific prose in other READMEs is intentionally not rewritten.
    rx=re.compile(r'\[([^\]]+)\]\(([^)\n]*'+re.escape(filename)+r'(?:#[^)]*)?)\)')
    return rx.sub(lambda m: f'[{label}]({m.group(2)})', text)


data=json.loads(REGISTRY.read_text(encoding='utf-8'))
entries=data.get('entries',{})
changed_sources=[]
titles={}
for roman,entry in entries.items():
    src=ROOT/entry['legacy']
    if not src.exists():
        raise SystemExit(f'Missing manifesto source {roman}: {src}')
    es,en,changed=normalize_source(src,roman)
    titles[roman]=(es,en,Path(entry['legacy']).name)
    if changed:
        changed_sources.append(entry['legacy'])

inf=ROOT/'manifiestos'/'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
if inf.exists():
    es,en,changed=normalize_source(inf,'∞')
    titles['∞']=(es,en,inf.name)
    if changed:
        changed_sources.append(inf.relative_to(ROOT).as_posix())

changed_indices=[]
for p in INDEX_TARGETS:
    if not p.exists():
        continue
    text=p.read_text(encoding='utf-8')
    old=text
    for roman,(es,en,filename) in titles.items():
        label=es if es==en else f'{es} / {en}'
        text=replace_link_label(text,filename,label)
    if text!=old:
        p.write_text(text,encoding='utf-8')
        changed_indices.append(p.relative_to(ROOT).as_posix())

print(f'BILINGUAL_NAME_NORMALIZE manifests={len(titles)} source_changed={len(changed_sources)} indices_changed={len(changed_indices)}')
for x in changed_sources:
    print('SOURCE',x)
for x in changed_indices:
    print('INDEX',x)