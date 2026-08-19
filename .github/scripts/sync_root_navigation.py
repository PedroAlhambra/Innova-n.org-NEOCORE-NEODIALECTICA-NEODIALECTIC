from pathlib import Path
import json
import re

ROOT = Path('.').resolve()


def roman_to_int(s):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v < prev:
            total -= v
        else:
            total += v; prev=v
    return total


def manifesto_latest_rows(limit=4):
    reg=json.loads((ROOT/'manifiestos/CANONICAL_FILENAMES.json').read_text(encoding='utf-8'))['entries']
    items=sorted(reg.items(),key=lambda kv:roman_to_int(kv[0]))[-limit:]
    es=[]; en=[]
    for roman,entry in items:
        rel=entry['legacy']
        p=ROOT/rel
        text=p.read_text(encoding='utf-8',errors='replace')
        titles=re.findall(r'^#\s+'+re.escape(roman)+r'\s*·\s*(.+?)\s*$',text,re.M)
        if len(titles)<2:
            raise SystemExit(f'Cannot derive bilingual latest-node titles for {roman}: {rel}')
        href='./'+rel
        es.append(f'- [{roman} · {titles[0].strip()}]({href})')
        en.append(f'- [{roman} · {titles[1].strip()}]({href})')
    return '\n'.join(es), '\n'.join(en)


def save_if_changed(path, transform):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    new = transform(s)
    if new != s:
        p.write_text(new, encoding='utf-8')
        print(f'UPDATED {path}')
    else:
        print(f'OK {path}')


def root_transform(s):
    es_works = '| **Obras** | [Ecosistema creativo](./obras/README.md) · [IDEA](./obras/idea/README.md) |'
    es_extra = es_works + '\n| **Proyección y difusión** | [Proyección distribuida](./proyeccion/README.md) |\n| **Creación abierta · UMBRAL-X** | [Apocalipsis de las IAs™ · Rama Starkdr Perdida](./obras/umbral-x/README.md) |'
    if es_works in s and '| **Proyección y difusión** |' not in s:
        s = s.replace(es_works, es_extra, 1)

    en_works = '| **Works** | [Creative ecosystem](./obras/README.md) · [IDEA](./obras/idea/README.md) |'
    en_extra = en_works + '\n| **Projection and outreach** | [Distributed projection](./proyeccion/README.md) |\n| **Open creation · UMBRAL-X** | [Apocalypse of the AIs™ · Lost Starkdr Branch](./obras/umbral-x/README.md) |'
    if en_works in s and '| **Projection and outreach** |' not in s:
        s = s.replace(en_works, en_extra, 1)

    es_nav = '- [Obras](./obras/README.md)\n- [IDEA](./obras/idea/README.md)'
    es_nav_new = es_nav + '\n- [Proyección y difusión](./proyeccion/README.md)\n- [UMBRAL-X · Apocalipsis de las IAs™](./obras/umbral-x/README.md)'
    if es_nav in s and '- [Proyección y difusión](./proyeccion/README.md)' not in s:
        s = s.replace(es_nav, es_nav_new, 1)

    en_nav = '- [Works](./obras/README.md)\n- [IDEA](./obras/idea/README.md)'
    en_nav_new = en_nav + '\n- [Projection and outreach](./proyeccion/README.md)\n- [UMBRAL-X · Apocalypse of the AIs™](./obras/umbral-x/README.md)'
    if en_nav in s and '- [Projection and outreach](./proyeccion/README.md)' not in s:
        s = s.replace(en_nav, en_nav_new, 1)

    # A historical fixation may preserve its historical frontier, but it must
    # never embed a second hard-coded claim about the *current* living frontier.
    s=re.sub(
        r'Este bloque conserva el estado fijado por el delta 7\.2\. El corpus vivo continuó evolucionando después de esa fijación y actualmente alcanza \*\*I–[IVXLCDM]+ \+ ∞\*\*; esa evolución no reescribe retrospectivamente el delta histórico\. / This block preserves the state fixed by the 7\.2 delta\. The living corpus continued evolving after that fixation and currently reaches \*\*I–[IVXLCDM]+ \+ ∞\*\*; that evolution does not retrospectively rewrite the historical delta\.',
        'Este bloque conserva el estado fijado por el delta PRE-7.3. El corpus vivo continuó evolucionando después de esa fijación; la frontera vigente se deriva del índice canónico y del bloque «Actualidad / Latest» de este README, sin reescribir retrospectivamente el delta histórico. / This block preserves the state fixed by the 7.2 delta. The living corpus continued evolving after that fixation; the current frontier is derived from the canonical index and the «Actualidad / Latest» block of this README, without retrospectively rewriting the historical delta.',
        s,
        count=1,
    )

    es_latest,en_latest=manifesto_latest_rows(4)
    s=re.sub(
        r'(Últimos nodos:\n\n).*?(\n\n## Análisis, auditorías y evidencia)',
        r'\1'+es_latest+r'\2',s,count=1,flags=re.S,
    )
    s=re.sub(
        r'(Latest nodes:\n\n).*?(\n\n## Analyses, audits and evidence)',
        r'\1'+en_latest+r'\2',s,count=1,flags=re.S,
    )
    return s


def insert_after_language_nav(s, marker, block):
    if marker in s:
        return s
    lines = s.splitlines()
    pos = 0
    for i, line in enumerate(lines[:20]):
        if '[ES' in line and '[EN' in line:
            pos = i + 1
            break
    lines[pos:pos] = ['', block, '']
    return '\n'.join(lines) + ('\n' if s.endswith('\n') else '')


def audits_transform(s):
    block = '''## Actualización 2026-08-09 · DistroKid / Spotify\n\n- [Ticket 4499471 · auditoría de royalty routing y catálogo](./2026-08-09_distrokid_ticket_4499471_royalty_routing_ES_EN.md)\n- [MAXPROC 001 · Leónidas-Cancerbero™](../../analisis/publicos/2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md)'''
    return insert_after_language_nav(s, '2026-08-09_distrokid_ticket_4499471_royalty_routing_ES_EN.md', block)


def analysis_transform(s):
    block = '''## Actualización 2026-08-09 · crítica externa / External criticism\n\n- [Václav Smil + Terry Winograd · deltas sobre integración, poder e incentivos](./2026-08-09_respuestas_externas_smil_winograd_deltas_ES_EN.md)\n- [MAXPROC 001 · Leónidas-Cancerbero™](./2026-08-08_umbral_x_maxproc_001_leonidas_cancerbero_streaming_trazabilidad_ES_EN.md)'''
    return insert_after_language_nav(s, '2026-08-09_respuestas_externas_smil_winograd_deltas_ES_EN.md', block)


def projection_transform(s):
    block = '''## Respuestas externas relevantes · 2026-08-09 / Relevant external responses\n\n- [Smil + Winograd · deltas incorporados a Síntesis Abierta](../analisis/publicos/2026-08-09_respuestas_externas_smil_winograd_deltas_ES_EN.md)\n- **Novum (Dinamarca):** presentación de IDEA enviada; actualización de estado canónico comunicada.\n- **Boekrecensiesblog (Países Bajos):** ejemplar físico acordado; envío directo por Amazon.\n- **deutsche-science-fiction.de:** EPUB acordado tras finalizar KDP Select.'''
    return insert_after_language_nav(s, 'Smil + Winograd · deltas incorporados', block)


save_if_changed('README.md', root_transform)
save_if_changed('auditorias/publicas/README.md', audits_transform)
save_if_changed('analisis/publicos/README.md', analysis_transform)
save_if_changed('proyeccion/README.md', projection_transform)
