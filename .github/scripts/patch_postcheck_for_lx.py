from pathlib import Path

p=Path('.github/scripts/postcheck_neocore_71_integridad_relacional.py')
t=p.read_text(encoding='utf-8')
repls={
"ok('Corpus canónico I–LIX = 59 manifiestos',len(mans)==59 and mans[0][0]=='I' and mans[-1][0]=='LIX'":"ok('Corpus canónico I–LX = 60 manifiestos',len(mans)==60 and mans[0][0]=='I' and mans[-1][0]=='LX'",
"ok('Mapa relacional declara I–LIX / 59','**Cobertura / Coverage:** I–LIX · 59 manifiestos / 59 manifestos' in relt,'')":"ok('Mapa relacional declara I–LX / 60','**Cobertura / Coverage:** I–LX · 60 manifiestos / 60 manifestos' in relt,'')",
}
for a,b in repls.items():
    t=t.replace(a,b)
p.write_text(t,encoding='utf-8')
if "I–LX = 60" not in t or "I–LX / 60" not in t:
    raise SystemExit('postcheck LX patch failed')
print('POSTCHECK PATCH OK: corpus I–LX / 60')
