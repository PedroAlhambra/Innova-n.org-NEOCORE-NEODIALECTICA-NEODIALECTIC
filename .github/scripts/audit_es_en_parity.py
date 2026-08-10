from pathlib import Path
import re

# Auditoría reforzada de paridad editorial ES/EN · 2026-08-10
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
    '<!-- NEO_CROSS_REFERENCES_START -->',
]
LANGUAGE_TRAILING_HEADINGS = [
    r'^## Navegación\s*$',
    r'^## Navigation\s*$',
    r'^### Vínculos internos equivalentes\s*$',
    r'^### Equivalent internal links\s*$',
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


def numbered_section_ids(s):
    ids=[]
    for h in re.findall(r'^##\s+(.+)$',s,re.M):
        m=re.match(r'^((?:\d+)|(?:[IVXLCDM]+))\.\s+',h.strip())
        if m:
            ids.append(m.group(1))
    return ids


def numbered_sections(s):
    matches=list(re.finditer(r'^##\s+((?:\d+)|(?:[IVXLCDM]+))\.\s+.+$',s,re.M))
    out={}
    for i,m in enumerate(matches):
        start=m.end()
        end=matches[i+1].start() if i+1 < len(matches) else len(s)
        out[m.group(1)] = s[start:end]
    return out


def list_items(s):
    return len(re.findall(r'^\s*(?:[-*+]\s+|\d+\.\s+)',s,re.M))


def code_blocks(s):
    return len(re.findall(r'```.*?```',s,flags=re.S))


def blockquotes(s):
    return len(re.findall(r'^>\s+\S',s,re.M))


def cut_shared_tail(s):
    positions=[s.find(marker) for marker in SHARED_TRAILING_MARKERS if s.find(marker)>=0]
    return s[:min(positions)] if positions else s


def cut_language_tail(s):
    """Exclude language-specific navigation/link tails from semantic parity.

    These blocks are navigation infrastructure, not translated manifesto body.
    Without this cut the last numbered section can absorb a different amount
    of ES/EN navigation and create false semantic-ratio failures.
    """
    positions=[]
    for pat in LANGUAGE_TRAILING_HEADINGS:
        m=re.search(pat,s,re.M)
        if m:
            positions.append(m.start())
    return s[:min(positions)] if positions else s


def section_diagnostics(es_body, en_body):
    """Return (material_failures, structural_warnings). Formatting alone is warning, not proof of abridgement."""
    material=[]
    warnings=[]
    es_sections=numbered_sections(es_body)
    en_sections=numbered_sections(en_body)
    for sid in [x for x in es_sections if x in en_sections]:
        a=es_sections[sid]; b=en_sections[sid]
        aw=len(words(a)); bw=len(words(b)); ratio=(bw/aw if aw else 1.0)

        if aw >= 90 and ratio < 0.65:
            material.append(f'sección {sid} EN/ES={ratio:.2f} ({bw}/{aw} palabras)')
        if bw >= 90 and aw > 0 and ratio > 1.80:
            material.append(f'sección {sid} EN/ES={ratio:.2f} ({bw}/{aw} palabras)')

        ai=list_items(a); bi=list_items(b)
        list_asym = max(ai,bi) >= 4 and min(ai,bi) < max(1, int(max(ai,bi)*0.50))
        if list_asym:
            msg=f'sección {sid} listas ES={ai}, EN={bi}'
            # Si además hay compresión notable, la asimetría es indicio material; si no, sólo formato.
            if aw >= 70 and (ratio < 0.75 or ratio > 1.55):
                material.append(msg)
            else:
                warnings.append(msg)

        ac=code_blocks(a); bc=code_blocks(b)
        if ac != bc and max(ac,bc) >= 1:
            material.append(f'sección {sid} fórmulas/bloques ES={ac}, EN={bc}')

        aq=blockquotes(a); bq=blockquotes(b)
        quote_asym = max(aq,bq) >= 3 and min(aq,bq) < max(1, int(max(aq,bq)*0.50))
        if quote_asym:
            msg=f'sección {sid} citas ES={aq}, EN={bq}'
            if aw >= 70 and (ratio < 0.75 or ratio > 1.55):
                material.append(msg)
            else:
                warnings.append(msg)
    return material, warnings


rows=[]
flagged=[]
warned=[]
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
        es_body=cut_language_tail(cut_shared_tail(text[es.end():en.start()]))
        en_body=cut_language_tail(cut_shared_tail(text[en.end():]))
        ew=len(words(es_body)); nw=len(words(en_body)); ratio=(nw/ew if ew else 0)
        eh=len(headings(es_body)); nh=len(headings(en_body))
        es_ids=numbered_section_ids(es_body); en_ids=numbered_section_ids(en_body)
        material=[]
        warnings=[]
        if ratio < 0.78:
            material.append(f'EN/ES global={ratio:.2f}')
        if ratio > 1.55:
            material.append(f'EN/ES global={ratio:.2f}')
        if eh >= 4 and nh < max(2, int(eh*0.70)):
            material.append(f'encabezados ES={eh}, EN={nh}')
        if rel.startswith('manifiestos/') and es_ids and es_ids != en_ids:
            material.append(f'secciones principales ES={es_ids}, EN={en_ids}')
        if rel.startswith('manifiestos/'):
            m,w=section_diagnostics(es_body,en_body)
            material.extend(m); warnings.extend(w)
        status='REVISAR' if material else ('ADVERTENCIA' if warnings else 'OK')
        reason='; '.join(material)
        warning='; '.join(warnings)
        row=(rel,ew,nw,ratio,eh,nh,status,reason,warning)
        rows.append(row)
        if material: flagged.append(row)
        elif warnings: warned.append(row)

lines=[]
lines.append('# Auditoría de paridad ES/EN · manifiestos y artículos públicos')
lines.append('')
lines.append('**Fecha:** 2026-08-10  ')
lines.append('**Ámbito:** `manifiestos/*.md` y `analisis/publicos/*.md` con secciones ES/EN.  ')
lines.append('**Objetivo:** detectar traducciones ausentes o materialmente recortadas sin confundir automáticamente diferencias legítimas de maquetación con pérdida semántica.  ')
lines.append('')
lines.append('## Criterio')
lines.append('')
lines.append('- Se compara volumen global, encabezados y secuencia de secciones principales H2 numeradas.')
lines.append('- Se compara sección por sección el volumen material y la conservación de fórmulas/bloques.')
lines.append('- Las diferencias de listas o citas se marcan como **ADVERTENCIA estructural** si el volumen de la sección sigue siendo razonablemente equivalente; pasan a **REVISAR** cuando coinciden con compresión material.')
lines.append('- Los bloques generados de navegación, referencias cruzadas y colas de navegación específicas de idioma no se contabilizan como traducción.')
lines.append('- `REVISAR` bloquea la publicación automática de manifiestos; `ADVERTENCIA` exige inspección editorial pero no demuestra por sí sola recorte.')
lines.append('')
lines.append(f'**Documentos bilingües examinados:** {len(rows)}  ')
lines.append(f'**Recortes/materialmente asimétricos para revisión:** {len(flagged)}  ')
lines.append(f'**Advertencias estructurales sin prueba suficiente de recorte:** {len(warned)}  ')
lines.append(f'**Con marcador incompleto/ausente:** {len(missing)}')
lines.append('')
lines.append('## Casos marcados')
lines.append('')
lines.append('| Archivo | Palabras ES | Palabras EN | Ratio EN/ES | H ES | H EN | Motivo |')
lines.append('|---|---:|---:|---:|---:|---:|---|')
for rel,ew,nw,ratio,eh,nh,status,reason,warning in flagged:
    lines.append(f'| `{rel}` | {ew} | {nw} | {ratio:.2f} | {eh} | {nh} | {reason} |')
if not flagged: lines.append('| — | — | — | — | — | — | Sin casos |')
lines.append('')
lines.append('## Advertencias estructurales')
lines.append('')
lines.append('| Archivo | Estado | Advertencia |')
lines.append('|---|---|---|')
for rel,ew,nw,ratio,eh,nh,status,reason,warning in warned:
    lines.append(f'| `{rel}` | ADVERTENCIA | {warning} |')
if not warned: lines.append('| — | — | Sin advertencias |')
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
for rel,ew,nw,ratio,eh,nh,status,reason,warning in rows:
    lines.append(f'| `{rel}` | {ew} | {nw} | {ratio:.2f} | {eh} | {nh} | {status} |')
lines.append('')
lines.append('> La paridad editorial exigida no significa traducción palabra por palabra ni idéntica maquetación, pero sí conservación íntegra de tesis, secciones, matices, cautelas epistemológicas, ejemplos, fórmulas, relaciones y conclusión.')
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'PARITY_AUDIT docs={len(rows)} flagged={len(flagged)} warnings={len(warned)} missing={len(missing)} report={REPORT}')