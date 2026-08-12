from pathlib import Path
FILES=[
'.github/scripts/repair_manifesto_49_strict_symmetry.py',
'.github/scripts/repair_manifesto_50_strict_symmetry.py',
'.github/scripts/repair_manifesto_51_strict_symmetry.py',
'.github/scripts/repair_manifesto_53_strict_symmetry.py',
]
old="end=text.index('<!-- NEO_RELATIONS_START -->',start)"
new="""tails=[text.find(x,start) for x in ('<!-- NEO_RELATIONS_START -->','<!-- NEO_CROSS_REFERENCES_START -->','<!-- NEO_MANIFESTO_NAV_START -->') if text.find(x,start)>=0]
end=min(tails) if tails else len(text)"""
for name in FILES:
    p=Path(name); text=p.read_text(encoding='utf-8')
    if old not in text:
        print('SKIP',name); continue
    text=text.replace(old,new,1)
    p.write_text(text,encoding='utf-8')
    print('HARDENED',name)
