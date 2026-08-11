from pathlib import Path

ROOT = Path('.').resolve()
EXCLUDED_TOP_LEVEL = {'wiki-legacy-archive'}

# Historical document paths that were renamed while the logical node remained
# the same. This map exists to repair *references*, not to rewrite history.
ALIASES = {
    '58_inteligencia_civilizatoria_pacto_social_bien_comun_ES_EN.md':
        '58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md',
}

changed=[]
replacements=0
for p in sorted(ROOT.rglob('*.md')):
    rel=p.relative_to(ROOT)
    if '.git' in rel.parts or (rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL):
        continue
    text=p.read_text(encoding='utf-8',errors='replace')
    old=text
    for stale,current in ALIASES.items():
        n=text.count(stale)
        if n:
            text=text.replace(stale,current)
            replacements += n
    if text != old:
        p.write_text(text,encoding='utf-8')
        changed.append(rel.as_posix())

print(f'LINK_ALIAS_NORMALIZE aliases={len(ALIASES)} replacements={replacements} files_changed={len(changed)}')
for p in changed:
    print('LINK_ALIAS',p)
