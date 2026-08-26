from pathlib import Path
import os
import re
import sys

root = Path('.').resolve()
mdir = root / 'manifiestos'
index = mdir / 'README.md'
protocol = root / 'propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md'
synth_index = root / 'propuestas/sintesis-abierta/README.md'
audits = root / 'auditorias/publicas/README.md'
leonidas = root / 'propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md'
entry_register = root / 'propuestas/sintesis-abierta/REGISTRO_ENTRADA_TRAZABLE_DERIVACION_ES_EN.md'
follow = root / 'proyeccion/SEGUIR_MARCO_SINTESIS_ES_EN.md'
neoaxioms = root / 'neoaxiomas/README.md'
neoaxioms_protocol = root / 'propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md'
neoaxioms_issue = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80'
CURRENT_VERSION = '7.3 CANON ABIERTO'
CURRENT_VERSION_EN = '7.3 OPEN CANON'
OBSOLETE_73 = '7.3-' + 'CANDIDATE'

for p in (index, protocol, synth_index, audits, leonidas, entry_register, follow, neoaxioms, neoaxioms_protocol):
    if not p.exists():
        raise SystemExit(f'Missing canonical target: {p.relative_to(root)}')

idx = index.read_text(encoding='utf-8')
entries = []
seen = set()
for roman, title, href in re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[([^\]]+)\]\(([^)]+\.md)\)', idx, re.M):
    p = (mdir / href).resolve()
    if p in seen or not p.exists():
        continue
    seen.add(p)
    entries.append((roman, title.strip(), p))

if not entries:
    raise SystemExit('No canonical manifestos found in manifiestos/README.md')

roman, title, latest = entries[-1]
count = len(entries)
latest_text = latest.read_text(encoding='utf-8')
issue_match = re.search(r'https://github\.com/PedroAlhambra/Innova-n\.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/(\d+)', latest_text)
if issue_match:
    issue_num = issue_match.group(1)
else:
    issue_num = {'LVII':'77', 'LVIII':'78', 'LIX':'79', 'LXVI':'110', 'LXVII':'112', 'LXVIII':'114', 'LXIX':'119', 'LXX':'120', 'LXXI':'121', 'LXXII':'122'}.get(roman)
if not issue_num:
    raise SystemExit(f'Cannot resolve Open Synthesis issue for latest manifesto {roman}')
issue_url = f'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/{issue_num}'

START='<!-- NEO_LATEST_MANIFESTO_START -->'
END='<!-- NEO_LATEST_MANIFESTO_END -->'
NAX_START='<!-- NEOAXIOMAS_GLOBAL_LINK_START -->'
NAX_END='<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'

def rel(f,target):
    return os.path.relpath(target,start=f.parent).replace(os.sep,'/')

def block(f):
    return f'''{START}

> ## 🔴 ÚLTIMO MANIFIESTO ABIERTO A SÍNTESIS / LATEST MANIFESTO OPEN FOR SYNTHESIS
>
> **{roman} · {title}**
>
> **[Leer {roman} / Read {roman}]({rel(f,latest)}) · [Síntesis Abierta {roman} · #{issue_num} / Open Synthesis {roman} · #{issue_num}]({issue_url})**  
> [Seguir marco / Follow framework]({rel(f,follow)}) · [Registrar entrada / Register entry]({rel(f,entry_register)}) · [Cómo aportar / How to contribute]({rel(f,protocol)}) · [Leónidas™]({rel(f,leonidas)}) · [Auditorías públicas / Public audits]({rel(f,audits)}) · [{count} manifiestos / manifestos · I–{roman}]({rel(f,index)})

{END}'''

def neoaxioms_block(f):
    if f.resolve() == neoaxioms.resolve():
        links = f'''**[Síntesis Abierta Neoaxiomas™ / Neoaxioms Open Synthesis]({neoaxioms_issue})** · **[Protocolo / Protocol]({rel(f,neoaxioms_protocol)})**'''
    else:
        links = f'''**[Abrir Neoaxiomas™ / Open Neoaxioms™]({rel(f,neoaxioms)})** · **[Síntesis Abierta Neoaxiomas™ / Neoaxioms Open Synthesis]({neoaxioms_issue})** · **[Protocolo / Protocol]({rel(f,neoaxioms_protocol)})**'''
    return f'''{NAX_START}

## NEOCore™ {CURRENT_VERSION} · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™
## NEOCore™ {CURRENT_VERSION_EN} · First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™

Los **Neoaxiomas™** expresan principios de alta estabilidad del NEOCore™ sin convertirse en dogmas cerrados: permanecen abiertos a contraste, evidencia, crítica, refutación y revisión mediante **Síntesis Abierta Neodialéctica™ — SAN™**. / **Neoaxioms™** express high-stability principles of NEOCore™ without becoming closed dogma: they remain open to challenge, evidence, criticism, refutation and revision through **Neodialectical Open Synthesis™ — SAN™**.

{links}

{NAX_END}'''

def replace_version(text):
    text = re.sub(r'NEOCore™\s+(?:v?7\.[01]|7\.x)', f'NEOCore™ {CURRENT_VERSION}', text)
    text = re.sub(r'NEOCore\s+(?:v?7\.[01]|7\.x)', f'NEOCore {CURRENT_VERSION}', text)
    text = text.replace(OBSOLETE_73, CURRENT_VERSION)
    text = text.replace(
        'NEOCore™ 7.3 CANON ABIERTO · candidata abierta, no canónica / open candidate, non-canonical',
        'NEOCore™ 7.3 CANON ABIERTO · canónico y reabrible / open canon, canonical and reopenable',
    )
    text = text.replace(
        '`PRE-7.3` identifica aquí la baseline documental estabilizada de WEB4™; no niega ni sustituye la frontera pública `7.3 CANON ABIERTO`. `7.3 CANON ABIERTO` permanece en Síntesis/evolución y **no equivale a 7.3 canónica ni a una implementación WEB4 final**. / `PRE-7.3` identifies the stabilised WEB4™ documentary baseline here; it does not deny or replace the public `7.3 CANON ABIERTO` frontier. `7.3 CANON ABIERTO` remains under Synthesis/evolution and **does not equal canonical 7.3 or a final WEB4 implementation**.',
        '`PRE-7.3` identifica una baseline documental histórica de WEB4™. La base operativa vigente del marco es `NEOCore™ 7.3 CANON ABIERTO`, canónica y reabrible; esto no equivale a que la implementación WEB4 privada esté aprobada o desplegada. / `PRE-7.3` identifies a historical WEB4™ documentary baseline. The current operating framework base is `NEOCore™ 7.3 OPEN CANON`, canonical and reopenable; this does not mean the private WEB4 implementation is approved or deployed.',
    )
    text = text.replace('no canónica / open candidate, non-canonical', 'canónica y reabrible / canonical and reopenable')
    return text

def insert_neoaxioms(text, f):
    nb = neoaxioms_block(f)
    if NAX_START in text and NAX_END in text:
        return re.sub(re.escape(NAX_START)+r'.*?'+re.escape(NAX_END), nb, text, count=1, flags=re.S)
    if START in text and END in text:
        m = re.search(re.escape(START)+r'.*?'+re.escape(END), text, re.S)
        if m:
            return text[:m.end()] + '\n\n' + nb + text[m.end():]
    selector = re.search(r'^\[ES[^\n]*\]\([^\n]+\)\s*·\s*\[EN[^\n]*\]\([^\n]+\)\s*$', text, re.M)
    if selector:
        return text[:selector.end()] + '\n\n' + nb + text[selector.end():]
    lines = text.splitlines(True)
    insert = 1 if lines and lines[0].lstrip().startswith('#') else 0
    lines.insert(insert, '\n' + nb + '\n\n')
    return ''.join(lines)

readmes = sorted({p for p in root.rglob('README*.md') if '.git' not in p.parts})
changed=[]
for f in readmes:
    text=f.read_text(encoding='utf-8'); old=text
    text = replace_version(text)
    if START in text and END in text:
        text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block(f),text,count=1,flags=re.S)
    text = insert_neoaxioms(text, f)
    if text!=old:
        f.write_text(text,encoding='utf-8'); changed.append(f)

fail=[]
old_version_re = re.compile(r'NEOCore(?:™)?\s+(?:v?7\.[01]|7\.x)')
for f in readmes:
    text=f.read_text(encoding='utf-8')
    if OBSOLETE_73 in text:
        fail.append(f'{f.relative_to(root)} obsolete 7.3 state remains')
    if old_version_re.search(text):
        fail.append(f'{f.relative_to(root)} stale NEOCore version remains')
    if text.count(NAX_START) != 1 or text.count(NAX_END) != 1:
        fail.append(f'{f.relative_to(root)} Neoaxioms block count')
    if f'NEOCore™ {CURRENT_VERSION}' not in text:
        fail.append(f'{f.relative_to(root)} current version missing')

print(f'CANONICAL_MANIFESTOS={count}')
print(f'LATEST={roman} {latest.name} ISSUE=#{issue_num}')
print(f'NEOCORE_VERSION={CURRENT_VERSION}')
print('README_TARGETS=',len(readmes))
print('FILES_CHANGED=',len(changed))
for p in changed:
    print('CHANGED', p.relative_to(root).as_posix())
if fail:
    print('POSTCHECK FAIL'); print('\n'.join(fail)); sys.exit(1)
print(f'POSTCHECK OK: all living README surfaces use NEOCore {CURRENT_VERSION}; count={count}')