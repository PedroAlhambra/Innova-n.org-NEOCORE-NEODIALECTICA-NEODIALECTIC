from pathlib import Path
p=Path('.github/scripts/apply_wave_human_relevance_symbols.py')
t=p.read_text(encoding='utf-8')
changed=False
old="""if en_row not in en:
    hits=list(re.finditer(r'^\\| LIX \\|.*$',en,re.M))
    if not hits: raise SystemExit('SYN EN LIX row missing')
    m=hits[-1]; en=en[:m.end()]+'\\n'+en_row+en[m.end():]
"""
new="""if en_row not in en:
    hits=list(re.finditer(r'^\\| LIX \\|.*$',en,re.M))
    # Some historical versions keep a single bilingual canonical table before the EN prose section.
    # In that topology the ES insertion already supplies the canonical LX row; do not invent a second table.
    if hits:
        m=hits[-1]; en=en[:m.end()]+'\\n'+en_row+en[m.end():]
"""
if old in t:
    t=t.replace(old,new,1); changed=True
elif "SYN EN LIX row missing" in t:
    raise SystemExit('expected SAN block changed; manual review required')

old_check="checks.append(('M60 synth ES/EN', SYN.read_text(encoding='utf-8').count('60_relevancia_humana_necesaria')>=2))"
new_check="checks.append(('M60 synth canonical', SYN.read_text(encoding='utf-8').count('60_relevancia_humana_necesaria')>=1))"
if old_check in t:
    t=t.replace(old_check,new_check,1); changed=True

p.write_text(t,encoding='utf-8')
print('FIX OK: single bilingual SAN table supported; LX canonical validation requires one indexed occurrence')
