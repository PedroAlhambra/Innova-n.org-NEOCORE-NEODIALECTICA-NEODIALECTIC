from pathlib import Path
import re

ROOT = Path('.').resolve()
REPORT = ROOT / 'auditorias' / 'publicas' / '2026-08-12_auditoria_global_simetria_ES_EN.md'

# Historical material is preserved as evidence and never rewritten by a live-state audit.
# Canonical manifesto mirrors are validated independently against their source and are not
# double-counted here.
EXCLUDED_PARTS = {'.git', 'wiki-legacy-archive'}
EXCLUDED_PREFIXES = (
    '.github/scripts/',
    '.github/workflows/',
    'manifiestos/canonicos/',
)

ES_PATTERNS = [
    r'^#\s+ES\s+·\s+(?:Castellano|Español)\s*$',
    r'^##\s+ES\s+·\s+(?:Castellano|Español)\s*$',
]
EN_PATTERNS = [
    r'^#\s+EN\s+·\s+English\s*$',
    r'^##\s+EN\s+·\s+English\s*$',
]

SHARED_TAIL_MARKERS = [
    '<!-- NEO_RELATIONS_START -->',
    '<!-- NEO_RELATED_WORK_START -->',
    '<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->',
    '<!-- NEO_MANIFESTO_NAV_START -->',
    '<!-- MANIFESTOS_CURRENT_START -->',
    '<!-- NEO_LATEST_MANIFESTO_START -->',
    '<!-- NEO_CROSS_REFERENCES_START -->',
    '<!-- NEO_RELATIONAL_FOOTER_START -->',
]

LANG_TAIL_HEADINGS = [
    r'^##\s+Navegación\s*$', r'^##\s+Navigation\s*$',
    r'^###\s+Vínculos internos equivalentes\s*$', r'^###\s+Equivalent internal links\s*$',
]


def first_match(text, pats):
    hits=[]
    for pat in pats:
        m=re.search(pat,text,re.M)
        if m: hits.append(m)
    return min(hits,key=lambda x:x.start()) if hits else None


def strip_generated_tail(s):
    positions=[s.find(x) for x in SHARED_TAIL_MARKERS if s.find(x)>=0]
    for pat in LANG_TAIL_HEADINGS:
        m=re.search(pat,s,re.M)
        if m: positions.append(m.start())
    # A bilingual heading after the EN body normally begins a shared tail, e.g.
    # "## Trazabilidad / Traceability". It belongs to neither language half.
    m=re.search(r'^#{2,6}\s+[^\n]+\s+/\s+[^\n]+\s*$',s,re.M)
    if m: positions.append(m.start())
    return s[:min(positions)] if positions else s


def without_fenced_code(s):
    return re.sub(r'```.*?```','\n',s,flags=re.S)


def without_comments(s):
    return re.sub(r'<!--.*?-->','\n',s,flags=re.S)


def clean_for_words(s):
    s=without_fenced_code(s)
    s=without_comments(s)
    s=re.sub(r'https?://\S+',' ',s)
    s=re.sub(r'[`*_>#|\[\](){}]',' ',s)
    return s


def word_count(s):
    return len(re.findall(r"\b[\wÀ-ÿ’'-]+\b",clean_for_words(s),flags=re.UNICODE))


def headings(s):
    out=[]
    for m in re.finditer(r'^(#{2,6})\s+(.+?)\s*$',without_comments(s),re.M):
        level=len(m.group(1)); title=m.group(2).strip()
        ident=''
        mm=re.match(r'^((?:\d+)|(?:[IVXLCDM]+))\.\s+',title)
        if mm: ident=mm.group(1)
        out.append((level,ident,title))
    return out


def structural_heading_signature(s):
    return [(lvl,ident) for lvl,ident,_ in headings(s)]


def sections_by_heading(s):
    cleaned=without_comments(s)
    hs=list(re.finditer(r'^(#{2,6})\s+(.+?)\s*$',cleaned,re.M))
    out=[]
    for i,m in enumerate(hs):
        start=m.end(); end=hs[i+1].start() if i+1<len(hs) else len(cleaned)
        title=m.group(2).strip()
        ident=''
        mm=re.match(r'^((?:\d+)|(?:[IVXLCDM]+))\.\s+',title)
        if mm: ident=mm.group(1)
        out.append((len(m.group(1)),ident,title,cleaned[start:end]))
    return out


def count_lists(s):
    s=without_fenced_code(s)
    return len(re.findall(r'^\s*(?:[-*+]\s+|\d+\.\s+)',s,re.M))


def count_quotes(s):
    s=without_fenced_code(s)
    return len(re.findall(r'^>\s+\S',s,re.M))


def count_code(s):
    return len(re.findall(r'```.*?```',s,re.S))


def count_table_rows(s):
    s=without_fenced_code(s)
    n=0
    for line in s.splitlines():
        x=line.strip()
        if not (x.startswith('|') and x.endswith('|')): continue
        if re.fullmatch(r'\|?[\s:|-]+\|?',x): continue
        n += 1
    return n


def count_paragraphs(s):
    s=without_fenced_code(without_comments(s))
    # Remove list/table blocks: those are compared independently and should not inflate prose.
    s=re.sub(r'(?m)^\s*(?:[-*+]\s+|\d+\.\s+).*$','',s)
    s=re.sub(r'(?m)^\s*\|.*\|\s*$','',s)
    blocks=[]
    for part in re.split(r'\n\s*\n',s):
        p=part.strip()
        if not p or p.startswith('#'): continue
        blocks.append(p)
    return len(blocks)


def section_shape(body):
    return {
        'lists': count_lists(body),
        'quotes': count_quotes(body),
        'code': count_code(body),
        'tables': count_table_rows(body),
        'paragraphs': count_paragraphs(body),
    }


def explicit_split(text):
    es=first_match(text,ES_PATTERNS); en=first_match(text,EN_PATTERNS)
    if not es and not en: return None
    if not es or not en or en.start() < es.start(): return ('BROKEN',None,None)
    a=strip_generated_tail(text[es.end():en.start()])
    b=strip_generated_tail(text[en.end():])
    return ('OK',a,b)


def audit_split(rel,es,en):
    problems=[]
    ewc=word_count(es); nwc=word_count(en)
    ratio=(nwc/ewc if ewc else 1.0)
    # Translation is not word-for-word, but large volume divergence is a compression alarm.
    if ewc >= 80 and not (0.82 <= ratio <= 1.35):
        problems.append(f'volumen EN/ES={ratio:.2f} ({nwc}/{ewc})')
    es_sig=structural_heading_signature(es); en_sig=structural_heading_signature(en)
    if es_sig != en_sig:
        problems.append(f'esqueleto de encabezados distinto ES={es_sig} EN={en_sig}')
    a=sections_by_heading(es); b=sections_by_heading(en)
    if len(a)==len(b):
        for sa,sb in zip(a,b):
            ash=section_shape(sa[3]); bsh=section_shape(sb[3])
            ident=sa[1] or sa[2]
            # Strict symmetry: lists, quotes, formulas and tables must be mirrored exactly.
            for key in ('lists','quotes','code','tables'):
                if ash[key] != bsh[key]:
                    problems.append(f'{ident}: {key} ES={ash[key]} EN={bsh[key]}')
            # Paragraph segmentation may vary by one for language grammar; larger differences
            # are treated as compression until manually reviewed.
            if abs(ash['paragraphs']-bsh['paragraphs']) > 1:
                problems.append(f'{ident}: párrafos ES={ash["paragraphs"]} EN={bsh["paragraphs"]}')
    return problems,ewc,nwc,ratio


def bilingual_filename(p):
    return '_ES_EN' in p.name or p.name in {'README.md','LEEME.md','COVER.md','PORTADA.md'}


def paired_heading_issues(text):
    # Interleaved bilingual documents may express both languages on one heading or as
    # consecutive headings of equal level. Flag lone headings for editorial review.
    hs=[(len(m.group(1)),m.group(2).strip()) for m in re.finditer(r'^(#{1,6})\s+(.+?)\s*$',without_comments(text),re.M)]
    bad=[]; i=0
    while i < len(hs):
        lvl,title=hs[i]
        if ' / ' in title:
            i+=1; continue
        if i+1 < len(hs) and hs[i+1][0]==lvl:
            i+=2; continue
        if re.match(r'^(?:NAX-|C-NAX-|[IVXLCDM]+\s*·|\d+\.)',title):
            i+=1; continue
        bad.append(title)
        i+=1
    return bad


rows=[]; split_fail=[]; marker_fail=[]; paired_review=[]
active_md=[]
for p in sorted(ROOT.rglob('*.md')):
    rel=p.relative_to(ROOT).as_posix()
    if any(part in EXCLUDED_PARTS for part in p.parts): continue
    if rel.startswith(EXCLUDED_PREFIXES): continue
    active_md.append(p)
    text=p.read_text(encoding='utf-8',errors='replace')
    split=explicit_split(text)
    if split:
        state,es,en=split
        if state!='OK':
            marker_fail.append(rel); rows.append((rel,'MARCADORES','—'))
            continue
        problems,ewc,nwc,ratio=audit_split(rel,es,en)
        status='OK' if not problems else 'REVISAR'
        rows.append((rel,status,'; '.join(problems)))
        if problems: split_fail.append((rel,problems,ewc,nwc,ratio))
    elif bilingual_filename(p):
        bad=paired_heading_issues(text)
        if bad:
            paired_review.append((rel,bad[:20]))
            rows.append((rel,'REVISAR-PAREADO','encabezados potencialmente monolingües: '+ ' | '.join(bad[:20])))
        else:
            rows.append((rel,'PAREADO','sin marcador dividido; estructura pareada aceptada'))

# GitHub Issue templates are public response surfaces too. Check visible name/description/label.
yaml_review=[]
for p in sorted((ROOT/'.github'/'ISSUE_TEMPLATE').glob('*.y*ml')):
    text=p.read_text(encoding='utf-8',errors='replace')
    misses=[]
    for m in re.finditer(r'^\s*(name|description|label):\s*["\']?(.+?)["\']?\s*$',text,re.M):
        val=m.group(2).strip()
        if len(val)<3 or val.startswith('http'): continue
        if ' / ' not in val and not ('ES' in val and 'EN' in val):
            misses.append(f'{m.group(1)}={val[:90]}')
    if misses: yaml_review.append((p.relative_to(ROOT).as_posix(),misses[:20]))

lines=[
'# Auditoría global de simetría ES/EN / Global ES/EN symmetry audit','',
'**Fecha / Date:** 2026-08-12  ',
'**Regla / Rule:** **NO COMPRESIÓN / NO COMPRESSION.** Toda superficie editorial bilingüe debe conservar contenido y estructura: títulos, secciones, listas, citas, fórmulas, tablas, cautelas, ejemplos, navegación y llamadas a Síntesis. / Every bilingual editorial surface must preserve content and structure: titles, sections, lists, quotations, formulas, tables, safeguards, examples, navigation and Synthesis calls.','',
'> Los espejos `manifiestos/canonicos/` no se duplican en este recuento: su igualdad con la fuente se valida mediante la auditoría estructural canónica. / `manifiestos/canonicos/` mirrors are not double-counted here: equality with their source is validated by the canonical structural audit.','',
'## Resumen / Summary','',
f'- Markdown activo examinado / Active Markdown scanned: **{len(active_md)}**.',
f'- Documentos con secciones ES/EN divididas / Split ES/EN documents: **{sum(1 for _,s,_ in rows if s in ("OK","REVISAR","MARCADORES"))}**.',
f'- Fallos estructurales divididos / Split structural failures: **{len(split_fail)}**.',
f'- Fallos de marcadores / Marker failures: **{len(marker_fail)}**.',
f'- Superficies pareadas para revisión / Paired surfaces for review: **{len(paired_review)}**.',
f'- Plantillas de Issue con etiquetas visibles no simétricas / Issue templates with non-symmetric visible labels: **{len(yaml_review)}**.','',
'## Fallos divididos / Split failures','']
if split_fail:
    for rel,probs,ew,nw,ratio in split_fail:
        lines.append(f'- `{rel}` · ES={ew} · EN={nw} · ratio={ratio:.2f}')
        for x in probs: lines.append(f'  - {x}')
else:
    lines.append('- Ninguno / None.')
lines += ['', '## Marcadores / Markers','']
if marker_fail:
    lines += [f'- `{x}`' for x in marker_fail]
else: lines.append('- Ninguno / None.')
lines += ['', '## Superficies pareadas que requieren revisión / Paired surfaces requiring review','']
if paired_review:
    for rel,bad in paired_review:
        lines.append(f'- `{rel}`: ' + ' | '.join(bad))
else: lines.append('- Ninguna / None.')
lines += ['', '## Plantillas GitHub Issue / GitHub Issue templates','']
if yaml_review:
    for rel,misses in yaml_review:
        lines.append(f'- `{rel}`: ' + ' | '.join(misses))
else: lines.append('- OK.')
lines += ['', '## Inventario / Inventory','', '| Archivo | Estado | Detalle |','|---|---|---|']
for rel,status,detail in rows:
    lines.append(f'| `{rel}` | **{status}** | {detail.replace("|","/")} |')
lines += ['', '## Regla permanente / Permanent rule','',
'- **ES y EN son dos representaciones completas del mismo objeto editorial; ninguna es resumen de la otra. / ES and EN are two complete representations of the same editorial object; neither is a summary of the other.**',
'- Una diferencia estructural en listas, citas, fórmulas o tablas es fallo hasta ser revisada. / A structural difference in lists, quotations, formulas or tables is a failure until reviewed.',
'- Títulos, índices, Neoaxiomas™, Manifiestos, Síntesis Abierta, respuestas públicas, plantillas y navegación deben mantener simetría visible. / Titles, indices, Neoaxioms™, Manifestos, Open Synthesis, public responses, templates and navigation must maintain visible symmetry.',
'- Los archivos históricos inertes se conservan como evidencia y se auditan por separado para no reescribir el pasado. / Inert historical files are preserved as evidence and audited separately so the past is not rewritten.','']
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'GLOBAL_BILINGUAL_SYMMETRY split_fail={len(split_fail)} marker_fail={len(marker_fail)} paired_review={len(paired_review)} yaml_review={len(yaml_review)} report={REPORT}')
