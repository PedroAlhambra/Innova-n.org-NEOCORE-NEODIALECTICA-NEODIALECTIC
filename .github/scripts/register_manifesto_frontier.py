from pathlib import Path
import json
import re

ROOT = Path('.').resolve()
MDIR = ROOT / 'manifiestos'
REGISTRY = MDIR / 'CANONICAL_FILENAMES.json'
INDEX = MDIR / 'README.md'
SYNTH = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'

TITLE = re.compile(r'^#\s+([IVXLCDM]+)\s*·\s*(.+?)\s*$', re.M)
META = re.compile(r'^\*\*Manifiesto / Manifesto:\*\*\s*([IVXLCDM]+)\s*$', re.M)
ISSUE = re.compile(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)')
ROW = re.compile(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)(?:.*)$', re.M)

# One-shot migration recovery for a manifesto that was published together with
# its Open Synthesis issue but without the reciprocal backlink in the source.
# The workflow writes the backlink into the manifesto itself, so this fallback
# can be removed after the first healthy synchronization.
BOOTSTRAP_ISSUES = {
    'LXXXI': '160',
}


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v < prev:
            total -= v
        else:
            total += v; prev=v
    return total


def expected_canonical(roman, legacy_path):
    name=Path(legacy_path).name
    stem=name[:-3] if name.endswith('.md') else name
    stem=re.sub(r'^\d+_', '', stem)
    return f'manifiestos/canonicos/{roman}_{stem}.md'


def parse_source(p):
    text=p.read_text(encoding='utf-8', errors='replace')
    titles=TITLE.findall(text[:5000])
    if not titles:
        return None
    roman=titles[0][0]
    same=[t.strip() for r,t in titles if r==roman]
    meta=META.search(text[:6000])
    if not meta or meta.group(1)!=roman or len(same)<2:
        return None
    front=text.split('# ES ·',1)[0]
    issues=ISSUE.findall(front)
    if not issues:
        issues=ISSUE.findall(text)
    if not issues and roman in BOOTSTRAP_ISSUES:
        issue=BOOTSTRAP_ISSUES[roman]
        issue_url=f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue}'
        marker=f'**Síntesis Abierta / Open Synthesis:** [#{issue}]({issue_url})  '
        anchor='**Autoría / Authorship:**'
        lines=text.splitlines()
        insert_at=None
        for i,line in enumerate(lines):
            if line.startswith(anchor):
                insert_at=i+1
                break
        if insert_at is None:
            raise SystemExit(f'Cannot bootstrap synthesis backlink for {roman}: authorship anchor missing')
        lines.insert(insert_at, marker)
        text='\n'.join(lines)+'\n'
        p.write_text(text,encoding='utf-8')
        print(f'BOOTSTRAP_SYNTHESIS_BACKLINK {roman} issue=#{issue} source={p.relative_to(ROOT)}')
        issues=[issue]
    if not issues:
        return None
    return {'roman':roman,'es':same[0],'en':same[1],'issue':issues[0],'path':p,'text':text}


data=json.loads(REGISTRY.read_text(encoding='utf-8'))
entries=data.setdefault('entries',{})
registry_changed=False

# Canonical mirror naming is deterministic for every registered manifesto.
# Repair malformed historical/dynamic entries before deciding whether there is
# a new frontier node.
for roman,entry in entries.items():
    expected=expected_canonical(roman,entry['legacy'])
    if entry.get('canonical') != expected:
        print(f'CANONICAL_PATH_REPAIRED {roman}: {entry.get("canonical")} -> {expected}')
        entry['canonical']=expected
        registry_changed=True

registered_ord=set(entries)
candidates={}
for p in sorted(MDIR.glob('[0-9]*_ES_EN.md')):
    parsed=parse_source(p)
    if not parsed:
        continue
    roman=parsed['roman']
    if roman in registered_ord:
        continue
    if roman in candidates:
        raise SystemExit(f'Ambiguous unregistered manifesto ordinal {roman}: {candidates[roman]["path"]} and {p}')
    candidates[roman]=parsed

max_registered=max((roman_to_int(r) for r in registered_ord), default=0)
new_sorted=sorted(candidates.values(), key=lambda x:roman_to_int(x['roman']))
for c in new_sorted:
    if roman_to_int(c['roman']) <= max_registered:
        raise SystemExit(f'Unregistered non-frontier manifesto requires manual review: {c["roman"]} {c["path"]}')
    max_registered=roman_to_int(c['roman'])

for c in new_sorted:
    roman=c['roman']; p=c['path']; legacy=f'manifiestos/{p.name}'
    entries[roman]={
        'legacy': legacy,
        'canonical': expected_canonical(roman,legacy),
    }
    registry_changed=True

ordered=dict(sorted(entries.items(), key=lambda kv:roman_to_int(kv[0])))
data['entries']=ordered
if registry_changed:
    REGISTRY.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if not new_sorted:
    print(f'MANIFESTO_FRONTIER_REGISTER new=0 registry_repaired={1 if registry_changed else 0}')
    raise SystemExit(0)

# Rebuild only the canonical collection rows, preserving all surrounding prose.
idx=INDEX.read_text(encoding='utf-8')
existing={r:(label,href) for r,label,href in ROW.findall(idx)}
for c in new_sorted:
    label=c['es'] if c['es']==c['en'] else f'{c["es"]} / {c["en"]}'
    existing[c['roman']]=(label,c['path'].name)

rows=[]
for roman in sorted(existing,key=roman_to_int):
    label,href=existing[roman]
    extra=''
    m=re.search(r'^- \*\*'+re.escape(roman)+r'\*\* · \[[^\]]+\]\('+re.escape(href)+r'\)(.*)$',idx,re.M)
    if m:
        extra=m.group(1)
    else:
        c=next((x for x in new_sorted if x['roman']==roman),None)
        if c:
            extra=f' · [SAN #{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]})'
    rows.append(f'- **{roman}** · [{label}]({href}){extra}')

start='## Colección canónica / Canonical collection'
end='> Ningún manifiesto equivale por sí solo al marco completo. / No single manifesto equals the complete framework.'
if start not in idx or end not in idx:
    raise SystemExit('Cannot locate canonical collection block in manifiestos/README.md')
pre,rest=idx.split(start,1)
body,post=rest.split(end,1)
inf_match=re.search(r'^- \*\*∞\*\* · .*$',body,re.M)
inf_row=inf_match.group(0) if inf_match else '- **∞** · [Manifiesto de Neo0™ · Puerta Abierta del Fractal / Neo0™ Manifesto · Open Gate of the Fractal](INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md)'
idx=pre+start+'\n\n'+'\n'.join(rows+[inf_row])+'\n\n'+end+post
INDEX.write_text(idx,encoding='utf-8')

syn=SYNTH.read_text(encoding='utf-8')
for c in new_sorted:
    if re.search(r'^\|\s*'+re.escape(c['roman'])+r'\s*\|',syn,re.M):
        continue
    label=c['es'] if c['es']==c['en'] else f'{c["es"]} / {c["en"]}'
    row=f'| {c["roman"]} | [{label}](../../manifiestos/{c["path"].name}) | [#{c["issue"]}](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{c["issue"]}) |'
    infpat=r'^(\|\s*∞\s*\|.*)$'
    if not re.search(infpat,syn,re.M):
        raise SystemExit('Cannot locate ∞ row in complete synthesis index')
    syn=re.sub(infpat,row+'\n'+r'\1',syn,count=1,flags=re.M)
SYNTH.write_text(syn,encoding='utf-8')

print('MANIFESTO_FRONTIER_REGISTER new='+str(len(new_sorted))+' ordinals='+','.join(c['roman'] for c in new_sorted))
for c in new_sorted:
    print(f'REGISTERED {c["roman"]} source={c["path"].relative_to(ROOT)} issue=#{c["issue"]}')
