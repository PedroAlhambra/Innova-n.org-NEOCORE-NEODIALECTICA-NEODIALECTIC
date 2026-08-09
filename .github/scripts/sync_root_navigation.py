from pathlib import Path


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
