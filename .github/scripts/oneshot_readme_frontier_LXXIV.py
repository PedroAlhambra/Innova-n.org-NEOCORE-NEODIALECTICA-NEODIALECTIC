from pathlib import Path
import re

# Final 2026-08-11 integration sweep: living README frontier + ∞ ES/EN parity.
ROOT=Path('.')
repo='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'

# 0. Repair ∞: a previous generated bilingual delta was appended entirely inside
# the EN language body. Split it into its corresponding language bodies and add
# the LXXIII-LXXIV continuation symmetrically.
infp=ROOT/'manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
if infp.exists():
    s=infp.read_text(encoding='utf-8')
    mixed=re.search(r'\n<!-- INFINITO_LXIX_LXXII_START -->\n(.*?)\n<!-- INFINITO_LXIX_LXXII_END -->\n',s,re.S)
    if mixed:
        block=mixed.group(1)
        marker='## XII. Relational inviolability, Faun™ and custodianship of power'
        if marker not in block:
            raise SystemExit('Cannot split legacy ∞ bilingual block')
        espart,enrest=block.split(marker,1)
        espart=espart.strip()
        enpart=(marker+enrest).strip()
        s=s[:mixed.start()]+'\n'+s[mixed.end():]
        en_marker='\n---\n\n# EN · English\n'
        if en_marker not in s:
            raise SystemExit('Cannot locate EN boundary in ∞')
        es_insert='\n\n<!-- INFINITO_LXIX_LXXII_ES_START -->\n'+espart+'\n<!-- INFINITO_LXIX_LXXII_ES_END -->\n'
        s=s.replace(en_marker,es_insert+en_marker,1)
        cross='\n<!-- NEO_CROSS_REFERENCES_START -->'
        if cross not in s:
            raise SystemExit('Cannot locate crossrefs in ∞')
        en_insert='\n\n<!-- INFINITO_LXIX_LXXII_EN_START -->\n'+enpart+'\n<!-- INFINITO_LXIX_LXXII_EN_END -->\n'
        s=s.replace(cross,en_insert+cross,1)

    # Current finite frontier in the perpetuity examples.
    s=s.replace('Cuando exista LXXII, ∞ irá después de LXXII.','Cuando exista LXXIV, ∞ irá después de LXXIV.')
    s=s.replace('When LXVIII exists, ∞ goes after LXVIII.','When LXXIV exists, ∞ goes after LXXIV.')

    # Add the latest constellation once, separately inside each language body.
    if 'INFINITO_LXXIII_LXXIV_ES_START' not in s:
        es13='''\n\n<!-- INFINITO_LXXIII_LXXIV_ES_START -->
## XIII. Humanidad común, Maduración Invertida™ y Asimetría de la Destrucción™

∞ incorpora también la nueva frontera **LXXIII–LXXIV** sin convertirla en cierre. LXXIII formula **Maduración Invertida™** para estudiar cuándo una sociedad premia como madurez la adaptación a sus propias patologías y distingue Faunismo™, Orquismo™ y otras degradaciones funcionales de la identidad esencial de una persona. LXXIV formula la **Asimetría de la Destrucción™**, el arquetipo funcional Trol™ y su desplazamiento hacia bots y Microagencia Digital Distribuida™.

La relación se abre a dos candidatos adicionales:

- **C-NAX-20 · Humanidad Común sin Supresión de la Diferencia™**: la humanidad común no borra diferencias legítimas y ninguna identidad parcial debe coronarse como totalidad de la persona;
- **C-NAX-21 · Ignorancia Sistémica del Mal y No Superioridad de la Destrucción™**: destruir, someter, extraer o dañar no demuestra comprensión del sistema, y una función objetivo parcial puede ser localmente inteligente mientras degrada el conjunto.

```text
PERSONA ≠ CONDUCTA ≠ ARQUETIPO
DIVERSIDAD ≠ DEGRADACIÓN
IDENTIDAD ≠ TOTALIDAD
INTELIGENCIA LOCAL ≠ SABIDURÍA SISTÉMICA
DESTRUIR ≠ SUPERIORIDAD
```

Los dos permanecen **candidatos**, abiertos a refutación y SAN™; no modifican el rango canónico NAX-01–NAX-14.

[LXXIII · #124]('''+repo+'''/issues/124) · [LXXIV · #125]('''+repo+'''/issues/125) · [C-NAX-20 · #126]('''+repo+'''/issues/126) · [C-NAX-21 · #127]('''+repo+'''/issues/127)
<!-- INFINITO_LXXIII_LXXIV_ES_END -->'''
        en13='''\n\n<!-- INFINITO_LXXIII_LXXIV_EN_START -->
## XIII. Common humanity, Inverted Maturation™ and Asymmetry of Destruction™

∞ also incorporates the new **LXXIII–LXXIV** frontier without turning it into closure. LXXIII formulates **Inverted Maturation™** to examine when a society rewards adaptation to its own pathologies as maturity and distinguishes Faunism™, Orcism™ and other functional degradations from a person's essential identity. LXXIV formulates the **Asymmetry of Destruction™**, the functional Troll™ archetype and its displacement toward bots and Distributed Digital Micro-Agency™.

The relation opens two additional candidates:

- **C-NAX-20 · Common Humanity without Suppression of Difference™**: common humanity does not erase legitimate differences and no partial identity should be crowned as the totality of the person;
- **C-NAX-21 · Systemic Ignorance of Evil and Non-Superiority of Destruction™**: destroying, dominating, extracting or harming does not demonstrate understanding of the system, and a partial objective function may be locally intelligent while degrading the whole.

```text
PERSON ≠ CONDUCT ≠ ARCHETYPE
DIVERSITY ≠ DEGRADATION
IDENTITY ≠ TOTALITY
LOCAL INTELLIGENCE ≠ SYSTEMIC WISDOM
DESTROYING ≠ SUPERIORITY
```

Both remain **candidates**, open to refutation and SAN™; they do not modify the canonical rank of NAX-01–NAX-14.

[LXXIII · #124]('''+repo+'''/issues/124) · [LXXIV · #125]('''+repo+'''/issues/125) · [C-NAX-20 · #126]('''+repo+'''/issues/126) · [C-NAX-21 · #127]('''+repo+'''/issues/127)
<!-- INFINITO_LXXIII_LXXIV_EN_END -->'''
        # Put XIII after XII in each body, immediately before its language boundary/crossrefs.
        es_end='<!-- INFINITO_LXIX_LXXII_ES_END -->'
        en_end='<!-- INFINITO_LXIX_LXXII_EN_END -->'
        if es_end in s: s=s.replace(es_end,es_end+es13,1)
        if en_end in s: s=s.replace(en_end,en_end+en13,1)
    infp.write_text(s,encoding='utf-8')

# 1. Sweep every living README/LEEME surface.
readmes=sorted(set(ROOT.rglob('README.md'))|set(ROOT.rglob('README_*.md'))|{ROOT/'LEEME.md'})
readmes=[p for p in readmes if p.exists() and '.git' not in p.parts]
for p in readmes:
    s=p.read_text(encoding='utf-8'); old=s
    s=s.replace('I–LXXII','I–LXXIV')
    s=s.replace('72 manifiestos','74 manifiestos').replace('72 manifestos','74 manifestos')
    s=s.replace('72 finite manifestos','74 finite manifestos').replace('72 manifiestos finitos','74 manifiestos finitos')
    s=s.replace('C-NAX-15–C-NAX-18','C-NAX-15–C-NAX-21')
    s=s.replace('C-NAX-15–C-NAX-19','C-NAX-15–C-NAX-21')
    s=s.replace('C-NAX-15–18','C-NAX-15–21').replace('C-NAX-15–19','C-NAX-15–21')
    if s!=old:
        p.write_text(s,encoding='utf-8')
        print('UPDATED',p)

# 2. Repair manifesto index's legacy unmarked finite-latest block.
p=ROOT/'manifiestos/README.md'; s=p.read_text(encoding='utf-8')
block='''> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS
>
> **LXXIV · Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™ · From the Human Troll to the Bot**
>
> **[Leer LXXIV / Read LXXIV](74_asimetria_destruccion_trol_humano_bot_ES_EN.md) · [Síntesis Abierta LXXIV · #125 / Open Synthesis LXXIV · #125]('''+repo+'''/issues/125)**
'''
pat=re.compile(r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>.*?(?=\n> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',re.S)
if pat.search(s): s=pat.sub(block.rstrip()+'\n',s,count=1)
p.write_text(s,encoding='utf-8')

# 3. WEB4 README explicit dynamic-banner wording.
p=ROOT/'web4/README.md'
if p.exists():
    s=p.read_text(encoding='utf-8')
    s=s.replace('C-NAX-15–C-NAX-18','C-NAX-15–C-NAX-21').replace('I–LXXII + ∞','I–LXXIV + ∞')
    if '## Delta LXXIII–LXXIV' not in s:
        s+='''\n\n## Delta LXXIII–LXXIV · Humanidad Común y Asimetría de la Destrucción / Common Humanity and Asymmetry of Destruction\n\n**ES.** WEB4™ incorpora la frontera viva **I–LXXIV + ∞**, con **Maduración Invertida™, Humanidad Común™, Faunismo™, Orquismo™, Trolismo™, Microagencia Digital Distribuida™ y Asimetría de la Destrucción™**. Los candidatos visibles llegan ahora a **C-NAX-21**. La fuente canónica sigue siendo GitHub y los banners deben leerla dinámicamente.\n\n**EN.** WEB4™ incorporates the living frontier **I–LXXIV + ∞**, with **Inverted Maturation™, Common Humanity™, Faunism™, Orcism™, Trollism™, Distributed Digital Micro-Agency™ and Asymmetry of Destruction™**. Visible candidates now extend through **C-NAX-21**. GitHub remains the canonical source and the banners must read it dynamically.\n'''
    p.write_text(s,encoding='utf-8')

# 4. Permanent sync workflow must remain dynamic and independent of one-shot helpers.
p=ROOT/'.github/workflows/sync-open-synthesis-network.yml'
if p.exists():
    s=p.read_text(encoding='utf-8')
    s=s.replace("      - '.github/scripts/oneshot_integrate_LXXIII_LXXIV_cnax20_21_v2.py'\n",'')
    s=re.sub(r'      - name: Integrate current LXXIII-LXXIV and C-NAX-20-21 frontier\n        run: python \.github/scripts/oneshot_integrate_LXXIII_LXXIV_cnax20_21_v2\.py\n','',s)
    s=s.replace("          if 'Último manifiesto / Síntesis: **LXXIV / #125**' not in text and 'Latest manifesto / synthesis: **LXXIV / #125**' not in text:\n              raise SystemExit('Postcheck did not resolve LXXIV/#125 as current frontier')\n",'')
    s=s.replace('# Current live frontier: I–LXXIV + ∞ · C-NAX-15–C-NAX-21 candidates','# Current baseline: I–LXXIV + ∞ · C-NAX-15–C-NAX-21 candidates · latest manifesto derived dynamically')
    p.write_text(s,encoding='utf-8')

# 5. Audit stale README living-frontier patterns.
stale=[]
for p in readmes:
    s=p.read_text(encoding='utf-8'); hits=[]
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
print('README_FRONTIER_POSTCHECK=' + ('OK' if not stale else 'NEEDS_CORRECTION'))
