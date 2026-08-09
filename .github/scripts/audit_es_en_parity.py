from pathlib import Path
import re

# Postcheck final tras normalización editorial ES/EN · 2026-08-09
ROOT = Path('.')
TARGETS = [ROOT / 'manifiestos', ROOT / 'analisis' / 'publicos']
REPORT = ROOT / 'auditorias' / 'publicas' / '2026-08-09_auditoria_paridad_ES_EN_manifiestos_articulos.md'

ES_MARKERS = [r'^# ES · Castellano\s*$', r'^# ES · Español\s*$', r'^## ES · Castellano\s*$']
EN_MARKERS = [r'^# EN · English\s*$', r'^## EN · English\s*$']
SHARED_TRAILING_MARKERS = [
    '<!-- NEO_RELATIONS_START -->',
    '<!-- NEO_RELATED_WORK_START -->',
    '<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->',
    '<!-- NEO_MANIFESTO_NAV_START -->',
    '<!-- MANIFESTOS_CURRENT_START -->',
    '<!-- NEO_LATEST_MANIFESTO_START -->',
]

def find_marker(text, patterns):
    hits=[]
    for pat in patterns:
        m=re.search(pat,text,re.M)
        if m: hits.append(m)
    return min(hits,key=lambda m:m.start()) if hits else None

def words(s):
    s=re.sub(r'```.*?```',' ',s,flags=re.S)
    s=re.sub(r'https?://\S+',' ',s)
    s=re.sub(r'[`*_>#|\[\](){}]',' ',s)
    return re.findall(r"\b[\wÀ-ÿ’'-]+\b",s,flags=re.UNICODE)

def headings(s):
    return [x.strip() for x in re.findall(r'^#{2,6}\s+(.+)$',s,re.M)]

def cut_shared_tail(s):
    positions=[s.find(marker) for marker in SHARED_TRAILING_MARKERS if s.find(marker)>=0]
    return s[:min(positions)] if positions else s

rows=[]
flagged=[]
missing=[]
for base in TARGETS:
    for p in sorted(base.glob('*.md')):
        if p.name.lower().startswith('readme'): continue
        text=p.read_text(encoding='utf-8')
        es=find_marker(text,ES_MARKERS); en=find_marker(text,EN_MARKERS)
        if not es and not en:
            continue
        rel=p.as_posix()
        if not es or not en or en.start() < es.start():
            missing.append((rel,bool(es),bool(en)))
            continue
        es_body=cut_shared_tail(text[es.end():en.start()])
        en_body=cut_shared_tail(text[en.end():])
        ew=len(words(es_body)); nw=len(words(en_body)); ratio=(nw/ew if ew else 0)
        eh=len(headings(es_body)); nh=len(headings(en_body))
        status='OK'
        reasons=[]
        if ratio < 0.78:
            status='REVISAR'; reasons.append(f'EN/ES palabras={ratio:.2f}')
        if eh >= 4 and nh < max(2, int(eh*0.70)):
            status='REVISAR'; reasons.append(f'encabezados ES={eh}, EN={nh}')
        if ratio > 1.55:
            status='REVISAR'; reasons.append(f'EN/ES palabras={ratio:.2f}')
        rows.append((rel,ew,nw,ratio,eh,nh,status,'; '.join(reasons)))
        if status!='OK': flagged.append(rows[-1])

lines=[]
lines.append('# Auditoría de paridad ES/EN · manifiestos y artículos públicos')
lines.append('')
lines.append('**Fecha:** 2026-08-09  ')
lines.append('**Ámbito:** `manifiestos/*.md` y `analisis/publicos/*.md` con secciones ES/EN.  ')
lines.append('**Objetivo:** detectar versiones inglesas ausentes, materialmente resumidas o estructuralmente incompletas.  ')
lines.append('')
lines.append('## Criterio')
lines.append('')
lines.append('- Se compara recuento aproximado de palabras entre las secciones ES y EN.')
lines.append('- Se compara el número de encabezados internos como señal de estructura perdida.')
lines.append('- Se excluyen de ambos lados bloques compartidos de relaciones, navegación, invitación a Síntesis Abierta y otros bloques automáticos bilingües.')
lines.append('- Se marca **REVISAR** si EN tiene menos del 78% de palabras de ES, más del 155%, o pierde de forma importante la estructura de encabezados.')
lines.append('- Es un detector: cada caso marcado requiere lectura humana antes de corregir.')
lines.append('')
lines.append(f'**Documentos bilingües examinados:** {len(rows)}  ')
lines.append(f'**Marcados para revisión:** {len(flagged)}  ')
lines.append(f'**Con marcador incompleto/ausente:** {len(missing)}')
lines.append('')
lines.append('## Casos marcados')
lines.append('')
lines.append('| Archivo | Palabras ES | Palabras EN | Ratio EN/ES | H ES | H EN | Motivo |')
lines.append('|---|---:|---:|---:|---:|---:|---|')
for rel,ew,nw,ratio,eh,nh,status,reason in flagged:
    lines.append(f'| `{rel}` | {ew} | {nw} | {ratio:.2f} | {eh} | {nh} | {reason} |')
if not flagged: lines.append('| — | — | — | — | — | — | Sin casos |')
lines.append('')
if missing:
    lines.append('## Marcadores incompletos')
    lines.append('')
    for rel,has_es,has_en in missing:
        lines.append(f'- `{rel}` · ES={has_es} · EN={has_en}')
    lines.append('')
lines.append('## Inventario completo')
lines.append('')
lines.append('| Archivo | ES | EN | Ratio | H ES | H EN | Estado |')
lines.append('|---|---:|---:|---:|---:|---:|---|')
for rel,ew,nw,ratio,eh,nh,status,reason in rows:
    lines.append(f'| `{rel}` | {ew} | {nw} | {ratio:.2f} | {eh} | {nh} | {status} |')
lines.append('')
lines.append('> La paridad editorial exigida no significa traducción palabra por palabra, pero sí conservación íntegra de tesis, secciones, matices, cautelas epistemológicas, ejemplos, fórmulas y conclusión.')
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'PARITY_AUDIT docs={len(rows)} flagged={len(flagged)} missing={len(missing)} report={REPORT}')
