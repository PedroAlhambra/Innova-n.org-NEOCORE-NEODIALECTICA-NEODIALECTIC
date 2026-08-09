from pathlib import Path

p = Path('README.md')
s = p.read_text(encoding='utf-8')
old = s

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

if s != old:
    p.write_text(s, encoding='utf-8')
    print('ROOT_NAVIGATION_UPDATED')
else:
    print('ROOT_NAVIGATION_ALREADY_OK')
