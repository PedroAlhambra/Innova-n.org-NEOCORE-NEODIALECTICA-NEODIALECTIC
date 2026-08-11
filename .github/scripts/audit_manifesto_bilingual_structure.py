from pathlib import Path
import json
import re

ROOT = Path('.').resolve()
REGISTRY = ROOT / 'manifiestos' / 'CANONICAL_FILENAMES.json'
MIDX = ROOT / 'manifiestos' / 'README.md'
SYNIDX = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
REPORT = ROOT / 'auditorias' / 'publicas' / '2026-08-12_auditoria_estructura_bilingue_manifiestos_ES_EN.md'

TITLE_RE = re.compile(r'^#\s+([IVXLCDM]+|∞)\s*·\s*(.+?)\s*$', re.M)
ES_MARK = re.compile(r'^#\s+ES\s+·\s+(?:Castellano|Español)\s*$', re.M)
EN_MARK = re.compile(r'^#\s+EN\s+·\s+English\s*$', re.M)
H2_RE = re.compile(r'^##\s+(.+)$', re.M)
MAIN_ID_RE = re.compile(r'^((?:\d+)|(?:[IVXLCDM]+))\.\s+')


def roman_to_int(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = prev = 0
    for ch in reversed(s):
        v = vals[ch]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total


def title_pair(text, expected):
    first_es = ES_MARK.search(text)
    preamble = text[:first_es.start()] if first_es else text[:4000]
    hs = TITLE_RE.findall(preamble)
    same = [(r,t.strip()) for r,t in hs if r == expected]
    if len(same) >= 2:
        return same[0][1], same[1][1], len(same)
    if len(same) == 1:
        return same[0][1], '', 1
    return '', '', 0


def numbered_ids(body):
    out=[]
    for h in H2_RE.findall(body):
        m=MAIN_ID_RE.match(h.strip())
        if m:
            out.append(m.group(1))
    return out


def section_bodies(text):
    es=ES_MARK.search(text); en=EN_MARK.search(text)
    if not es or not en or en.start() < es.start():
        return None, None
    return text[es.end():en.start()], text[en.end():]


def index_label(text, href, table=False):
    name = Path(href).name
    if table:
        m=re.search(r'^\|\s*[IVXLCDM]+\s*\|\s*\[([^\]]+)\]\([^\n)]*'+re.escape(name)+r'\)', text, re.M)
    else:
        m=re.search(r'^-\s+\*\*[IVXLCDM]+\*\*\s*·\s*\[([^\]]+)\]\([^\n)]*'+re.escape(name)+r'\)', text, re.M)
    return m.group(1).strip() if m else None


data=json.loads(REGISTRY.read_text(encoding='utf-8'))
entries=data.get('entries', {})
ordered=sorted(entries.items(), key=lambda x: roman_to_int(x[0]))
# ∞ remains outside the finite registry by design.
inf=ROOT/'manifiestos'/'INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'

idx=MIDX.read_text(encoding='utf-8')
syn=SYNIDX.read_text(encoding='utf-8')
rows=[]
fail=[]
warn=[]

for roman, entry in ordered:
    src=ROOT/entry['legacy']; canon=ROOT/entry['canonical']
    issues=[]; warnings=[]
    if not src.exists():
        issues.append('FALTA fuente legacy')
        rows.append((roman,entry['legacy'],'','','','; '.join(issues)))
        fail.append((roman,issues))
        continue
    text=src.read_text(encoding='utf-8',errors='replace')
    es_title,en_title,n_titles=title_pair(text,roman)
    if n_titles < 2 or not en_title:
        issues.append('falta H1 inglés simétrico')
    if es_title and en_title and es_title == en_title and re.search(r'\b(?:de|del|la|el|los|las|y|contra|para|como|sin|con|humano|humana|soberanía|síntesis|memoria|inteligencia|custodia|defensa)\b', es_title, re.I):
        warnings.append('H1 ES/EN idéntico pese a léxico traducible')
    # Canonical metadata and language gates.
    if not re.search(r'^\*\*Manifiesto / Manifesto:\*\*\s*'+re.escape(roman)+r'\s*$', text, re.M):
        issues.append('metadato Manifiesto/Manifesto ausente o ordinal distinto')
    if not re.search(r'^\*\*Versión / Version:\*\*', text, re.M):
        warnings.append('falta metadato Versión/Version')
    if not re.search(r'^\*\*Estado / Status:\*\*', text, re.M):
        warnings.append('falta metadato Estado/Status')
    if not ES_MARK.search(text) or not EN_MARK.search(text):
        issues.append('marcadores ES/EN incompletos')
    es_body,en_body=section_bodies(text)
    if es_body is not None:
        a=numbered_ids(es_body); b=numbered_ids(en_body)
        if a and b and a != b:
            issues.append(f'secciones principales asimétricas ES={a} EN={b}')
    # Cross-reference block is normative since the README policy states every manifesto ends with it.
    if '<!-- NEO_CROSS_REFERENCES_START -->' not in text or '<!-- NEO_CROSS_REFERENCES_END -->' not in text:
        issues.append('falta bloque de referencias cruzadas canónicas')
    # Canonical mirror existence and title parity.
    if not canon.exists():
        issues.append('falta espejo canónico')
    else:
        ct=canon.read_text(encoding='utf-8',errors='replace')
        ces,cen,_=title_pair(ct,roman)
        if (ces,cen)!=(es_title,en_title):
            issues.append('títulos del espejo canónico no coinciden con fuente')
    # Main manifesto index must display the bilingual pair when titles differ.
    lab=index_label(idx,entry['legacy'],table=False)
    expected = es_title if not en_title or es_title==en_title else f'{es_title} / {en_title}'
    if lab is None:
        issues.append('falta entrada en manifiestos/README.md')
    elif en_title and es_title!=en_title and lab != expected:
        issues.append(f'índice principal no simétrico: «{lab}»')
    # Complete Open Synthesis index must also show bilingual title.
    slab=index_label(syn,entry['legacy'],table=True)
    if slab is None:
        issues.append('falta entrada en índice completo de Síntesis')
    elif en_title and es_title!=en_title and slab != expected:
        issues.append(f'índice de Síntesis no simétrico: «{slab}»')

    status='REVISAR' if issues else ('ADVERTENCIA' if warnings else 'OK')
    rows.append((roman,entry['legacy'],es_title,en_title,status,'; '.join(issues+warnings)))
    if issues: fail.append((roman,issues))
    elif warnings: warn.append((roman,warnings))

# Infinite manifesto receives the same title/language/crossref checks, but no finite-index table requirement.
if inf.exists():
    text=inf.read_text(encoding='utf-8',errors='replace')
    es_title,en_title,n_titles=title_pair(text,'∞')
    issues=[]; warnings=[]
    if n_titles < 2 or not en_title: issues.append('falta H1 inglés simétrico')
    if not ES_MARK.search(text) or not EN_MARK.search(text): issues.append('marcadores ES/EN incompletos')
    if '<!-- NEO_CROSS_REFERENCES_START -->' not in text or '<!-- NEO_CROSS_REFERENCES_END -->' not in text: issues.append('falta bloque de referencias cruzadas canónicas')
    status='REVISAR' if issues else ('ADVERTENCIA' if warnings else 'OK')
    rows.append(('∞',inf.relative_to(ROOT).as_posix(),es_title,en_title,status,'; '.join(issues+warnings)))
    if issues: fail.append(('∞',issues))

lines=[
'# Auditoría estructural bilingüe de manifiestos / Bilingual manifesto structural audit','',
'**Fecha / Date:** 2026-08-12  ',
'**Objeto / Scope:** títulos ES/EN, metadatos mínimos, marcadores de idioma, simetría de secciones principales, índices, espejo canónico y bloque normativo de referencias cruzadas.','',
f'**Manifiestos revisados / Manifestos reviewed:** {len(rows)}  ',
f'**REVISAR / REVIEW:** {len(fail)}  ',
f'**ADVERTENCIAS / WARNINGS:** {len(warn)}','',
'## Resultado / Result','',
'| Nº | Fuente | Título ES | Title EN | Estado | Hallazgos |','|---:|---|---|---|---|---|']
for roman,path,es,en,status,detail in rows:
    lines.append(f'| {roman} | `{path}` | {es.replace("|","/")} | {en.replace("|","/")} | **{status}** | {detail.replace("|","/")} |')
lines += ['', '## Regla permanente / Permanent rule','',
'- El nombre canónico visible de un manifiesto debe conservar **título ES + título EN** cuando las formas lingüísticas difieran.',
'- La fuente legacy es histórica, pero el ordinal romano y el par de H1 son la identidad editorial canónica.',
'- `manifiestos/README.md`, el índice completo de Síntesis y las superficies de navegación deben derivar el nombre del par H1, no de una etiqueta manual parcial.',
'- El espejo `manifiestos/canonicos/` debe mantenerse sincronizado desde la fuente sin alterar contenido ni genealogía.',
'- Cada manifiesto debe conservar el bloque final `Referencias cruzadas canónicas / Canonical cross-references` y sus enlaces deben pasar la auditoría general de rutas.','']
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'MANIFESTO_STRUCTURE_AUDIT reviewed={len(rows)} review={len(fail)} warnings={len(warn)} report={REPORT}')
