from pathlib import Path
import re

# Trigger 2026-08-11T12:45+02:00: final living-frontier sweep.
ROOT=Path('.')
repo='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'
readmes=sorted(set(ROOT.rglob('README.md'))|set(ROOT.rglob('README_*.md'))|{ROOT/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]

for p in readmes:
    s=p.read_text(encoding='utf-8')
    old=s
    # README/LEEME are living navigation surfaces; historical snapshots live in dated audit files.
    s=s.replace('I–LXXII','I–LXXIV')
    s=s.replace('72 manifiestos','74 manifiestos').replace('72 manifestos','74 manifestos')
    s=s.replace('72 finite manifestos','74 finite manifestos').replace('72 manifiestos finitos','74 manifiestos finitos')
    s=s.replace('C-NAX-15–C-NAX-18','C-NAX-15–C-NAX-21')
    s=s.replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21')
    s=s.replace('C-NAX-15–18','C-NAX-15–21').replace('C-NAX-15–19','C-NAX-15–21')
    if s!=old:
        p.write_text(s,encoding='utf-8')
        print('UPDATED',p)

# Repair manifesto index's legacy unmarked finite-latest block.
p=ROOT/'manifiestos/README.md'; s=p.read_text(encoding='utf-8')
block='''> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS
>
> **LXXIV · Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™ · From the Human Troll to the Bot**
>
> **[Leer LXXIV / Read LXXIV](74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [Síntesis Abierta LXXIV · #125 / Open Synthesis LXXIV · #125]('''+repo+'''/issues/125)**
'''
pat=re.compile(r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>.*?(?=\n> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',re.S)
if pat.search(s):
    s=pat.sub(block.rstrip()+'\n',s,count=1)
p.write_text(s,encoding='utf-8')

# WEB4 README explicit dynamic-banner wording.
p=ROOT/'web4/README.md'
if p.exists():
    s=p.read_text(encoding='utf-8')
    s=s.replace('C-NAX-15–C-NAX-18','C-NAX-15–C-NAX-21').replace('I–LXXII + ∞','I–LXXIV + ∞')
    if '## Delta LXXIII–LXXIV' not in s:
        s+='''\n\n## Delta LXXIII–LXXIV · Humanidad Común y Asimetría de la Destrucción / Common Humanity and Asymmetry of Destruction\n\n**ES.** WEB4™ incorpora la frontera viva **I–LXXIV + ∞**, con **Maduración Invertida™, Humanidad Común™, Faunismo™, Orquismo™, Trolismo™, Microagencia Digital Distribuida™ y Asimetría de la Destrucción™**. Los candidatos visibles llegan ahora a **C-NAX-21**. La fuente canónica sigue siendo GitHub y los banners deben leerla dinámicamente.\n\n**EN.** WEB4™ incorporates the living frontier **I–LXXIV + ∞**, with **Inverted Maturation™, Common Humanity™, Faunism™, Orcism™, Trollism™, Distributed Digital Micro-Agency™ and Asymmetry of Destruction™**. Visible candidates now extend through **C-NAX-21**. GitHub remains the canonical source and the banners must read it dynamically.\n'''
    p.write_text(s,encoding='utf-8')

# Permanent sync workflow must remain dynamic: remove temporary integrator dependency/hard-coded frontier gates.
p=ROOT/'.github/workflows/sync-open-synthesis-network.yml'
if p.exists():
    s=p.read_text(encoding='utf-8')
    s=s.replace("      - '.github/scripts/oneshot_integrate_LXXIII_LXXIV_cnax20_21_v2.py'\n",'')
    s=re.sub(r'      - name: Integrate current LXXIII-LXXIV and C-NAX-20-21 frontier\n        run: python \.github/scripts/oneshot_integrate_LXXIII_LXXIV_cnax20_21_v2\.py\n','',s)
    s=s.replace("          if 'Último manifiesto / Síntesis: **LXXIV / #125**' not in text and 'Latest manifesto / synthesis: **LXXIV / #125**' not in text:\n              raise SystemExit('Postcheck did not resolve LXXIV/#125 as current frontier')\n",'')
    s=s.replace('# Current live frontier: I–LXXIV + ∞ · C-NAX-15–C-NAX-21 candidates','# Current baseline: I–LXXIV + ∞ · C-NAX-15–C-NAX-21 candidates · latest manifesto derived dynamically')
    p.write_text(s,encoding='utf-8')

# Audit stale living README patterns after repair.
stale=[]
for p in readmes:
    s=p.read_text(encoding='utf-8')
    hits=[]
    for token in ('I–LXXII','72 manifiestos','72 manifestos','C-NAX-15–C-NAX-18','C-NAX-15–C-NAX-19'):
        if token in s: hits.append(token)
    if hits: stale.append((p.as_posix(),hits))

report=ROOT/'auditorias/publicas/2026-08-11_postcheck_README_frontera_LXXIV_ES_EN.md'
lines=['# Postcheck README · frontera viva LXXIV / README Postcheck · LXXIV Living Frontier','', '**Fecha / Date:** 2026-08-11  ',f'**README/LEEME revisados / README/LEEME reviewed:** {len(readmes)}  ',f'**Estado / Status:** **{"OK" if not stale else "REQUIERE CORRECCIÓN / NEEDS CORRECTION"}**','', '## ES · Resultado','', '- Frontera viva esperada: **74 manifiestos finitos · I–LXXIV + ∞**.','- Neoaxiomas: **NAX-01–NAX-14 canónicos + C-NAX-15–C-NAX-21 candidatos**.','- Último manifiesto finito: **LXXIV · #125**.','- WEB4™: lector y documentación referencian I–LXXIV + ∞ y candidatos hasta C-NAX-21.','']
if stale:
    lines.append('### Residuos detectados')
    for f,h in stale: lines.append(f'- `{f}`: {", ".join(h)}')
else: lines.append('- No se detectan residuos de frontera viva I–LXXII / 72 ni rangos C-NAX anteriores en README/LEEME.')
lines += ['','## EN · Result','', '- Expected living frontier: **74 finite manifestos · I–LXXIV + ∞**.','- Neoaxioms: **NAX-01–NAX-14 canonical + C-NAX-15–C-NAX-21 candidates**.','- Latest finite manifesto: **LXXIV · #125**.','- WEB4™: reader and documentation reference I–LXXIV + ∞ and candidates through C-NAX-21.','']
if stale:
    lines.append('### Detected residues')
    for f,h in stale: lines.append(f'- `{f}`: {", ".join(h)}')
else: lines.append('- No stale I–LXXII / 72 living-frontier residue or earlier C-NAX range remains in README/LEEME.')
report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
if stale:
    raise SystemExit('STALE README FRONTIER: '+repr(stale))
print('README_FRONTIER_POSTCHECK=OK')
