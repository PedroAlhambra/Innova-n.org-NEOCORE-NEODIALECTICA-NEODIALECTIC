from pathlib import Path
p=Path('.github/scripts/repair_manifesto_48_strict_symmetry.py')
text=p.read_text(encoding='utf-8')
old="""    marker='## '+heading
    s=text.index(marker,en)
    rest=text[s+len(marker):]
    m=re.search(r'^##\\s+',rest,re.M)
    e=s+len(marker)+m.start() if m else text.index('<!-- NEO_RELATIONS_START -->',s)
    text=text[:s]+marker+'\\n\\n'+body.strip()+'\\n\\n'+text[e:]
"""
new="""    marker='## '+heading
    try:
        s=text.index(marker,en)
        marker_len=len(marker)
    except ValueError:
        ordinal=heading.split('.',1)[0]
        mm=re.search(r'^##\\s+'+re.escape(ordinal)+r'\\.\\s+.*$',text[en:],re.M)
        if not mm:
            raise SystemExit(f'Cannot resolve EN heading: {heading}')
        s=en+mm.start()
        marker_len=len(mm.group(0))
    rest=text[s+marker_len:]
    m=re.search(r'^##\\s+',rest,re.M)
    e=s+marker_len+m.start() if m else text.index('<!-- NEO_RELATIONS_START -->',s)
    text=text[:s]+marker+'\\n\\n'+body.strip()+'\\n\\n'+text[e:]
"""
if text.count(old)!=1: raise SystemExit('resolver target drift')
text=text.replace(old,new,1)
p.write_text(text,encoding='utf-8')
print('REPAIR_48_HEADING_RESOLVER=HARDENED')
