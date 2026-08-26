from pathlib import Path

START='<!-- NEOCORE_73_CANON_START -->'
END='<!-- NEOCORE_73_CANON_END -->'
OLD_START='<!-- NEOCORE_73_CANDIDATE_START -->'
OLD_END='<!-- NEOCORE_73_CANDIDATE_END -->'

ROOT_BLOCK=f'''{START}\n\n### NEOCore™ 7.3 · CANON ABIERTO · Capa de Autosíntesis Recursiva™ / OPEN CANON · Recursive Self-Synthesis Layer™\n\nNEOCore™ 7.3 es la **base operativa canónica y reabrible vigente**. La Síntesis Abierta nace abierta y opera como toroide multicabeza/multiescala. La capa recorre preguntas abiertas sin confundir creación con juicio inmediato: captura la emergencia, preserva continuidad y aplica contraste diferido con estados epistemológicos y fuentes proporcionales a cada afirmación. **Canon ≠ dogma · Canon ≠ final · Autorresponder ≠ autovalidar · Crear ≠ juzgar en el mismo instante.** / NEOCore™ 7.3 is the **current canonical and reopenable operating base**. Open Synthesis is born open and operates as a multihead/multiscale toroid. The layer processes open questions without conflating creation with immediate judgement: it captures emergence, preserves continuity and applies deferred scrutiny with epistemic states and sources proportional to each claim. **Canon ≠ dogma · Canon ≠ final · Self-answering ≠ self-validation · Creating ≠ judging at the same instant.**\n\n**[Canon 7.3 / 7.3 Canon](./propuestas/sintesis-abierta/NEOCORE_7_3_CANON_ES_EN.md)** · **[Documento matriz / Matrix document](./propuestas/sintesis-abierta/NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)** · **[#161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161)** · **[Delta #169](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/169)** · **[I–XII #162](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/162)** · **[XIII–XXXII #168](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/168)** · **[XXXIII–XLII #170](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/170)** · **[XLIII–LII #171](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/171)**\n\n{END}\n'''

SAN_BLOCK=f'''{START}\n\n## NEOCore™ 7.3 · CANON ABIERTO · Capa de Autosíntesis Recursiva™\n## NEOCore™ 7.3 · OPEN CANON · Recursive Self-Synthesis Layer™\n\nNEOCore™ 7.3 fija como base operativa vigente la evolución recursiva de SAN™ dentro de una topología **toroidal, multicabeza y multiescala**. Toda síntesis permanece revisable y puede funcionar como tesis, antítesis, fragmento u origen en otra escala. Se distinguen dos tiempos: **modo creador** (captura, memoria, continuidad, relación) y **modo de contraste** (antítesis, estado epistemológico, evidencia/falsadores, delta y retorno al toroide). / NEOCore™ 7.3 fixes the recursive evolution of SAN™ as the current operating base within a **toroidal, multihead and multiscale** topology. Every synthesis remains revisable and may function as thesis, antithesis, fragment or origin at another scale. Two cognitive times are distinguished: **creative mode** (capture, memory, continuity, relation) and **scrutiny mode** (antithesis, epistemic state, evidence/falsifiers, delta and return to the toroid).\n\n> **CANON ≠ DOGMA · CANON ≠ FINAL · AUTORRESPONDER ≠ AUTOVALIDAR / CANON ≠ DOGMA · CANON ≠ FINAL · SELF-ANSWERING ≠ SELF-VALIDATION.**\n\n[Canon 7.3 / 7.3 Canon](NEOCORE_7_3_CANON_ES_EN.md) · [Documento matriz / Matrix document](NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md) · [Matriz #161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161)\n\n{END}\n'''

INDEX_BLOCK=f'''{START}\n\n## 0 · NEOCore™ 7.3 · CANON ABIERTO / OPEN CANON · Autosíntesis Recursiva™ / Recursive Self-Synthesis™\n\n- **Documento canónico / Canonical document:** [NEOCORE_7_3_CANON_ES_EN.md](NEOCORE_7_3_CANON_ES_EN.md)\n- **Documento matriz / Matrix document:** [NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md](NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)\n- **Matriz conceptual / Conceptual matrix:** [#161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161)\n- **Delta arquitectónico / Architectural delta:** [#169](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/169)\n- **Estado / Status:** `CANÓNICO Y REABRIBLE / CANONICAL AND REOPENABLE`. Las preguntas, auditorías y contrastes pendientes abren deltas posteriores; no revierten por sí solos el estado canónico. / Pending questions, audits and scrutiny open subsequent deltas; they do not by themselves revert canonical status.\n\n{END}\n'''

def replace_any(text, block, anchor, after=True):
    pairs=((START,END),(OLD_START,OLD_END))
    for start,end in pairs:
        if start in text and end in text:
            a=text.index(start)
            b=text.index(end,a)+len(end)
            return text[:a]+block.rstrip()+text[b:]
    i=text.find(anchor)
    if i < 0:
        raise SystemExit(f'anchor not found: {anchor!r}')
    if after:
        i += len(anchor)
        return text[:i]+'\n\n'+block.rstrip()+'\n'+text[i:]
    return text[:i]+block.rstrip()+'\n\n'+text[i:]

def sync_root_version_surface(text):
    lines=text.splitlines()
    if not lines:
        raise SystemExit('empty root README')
    lines[0]='# Innova_N — NEOCore™ 7.3 CANON ABIERTO · Neodialéctica™ / Neodialectics™ · Neodialectica Framework™'
    text='\n'.join(lines)+'\n'
    text=text.replace('NEOCore™ 7.3-CANDIDATE','NEOCore™ 7.3 CANON ABIERTO')
    text=text.replace('NEOCore 7.3-CANDIDATE','NEOCore 7.3 CANON ABIERTO')
    text=text.replace('#innova_n--neocore-73-candidate--neodialéctica--neodialectics--neodialectica-framework','#innova_n--neocore-73-canon-abierto--neodialéctica--neodialectics--neodialectica-framework')
    return text

root=Path('README.md')
text=sync_root_version_surface(root.read_text(encoding='utf-8'))
text=replace_any(text,ROOT_BLOCK,'## 🔴 Actualidad / Latest',after=True)
root.write_text(text,encoding='utf-8')

san=Path('propuestas/sintesis-abierta/README.md')
text=san.read_text(encoding='utf-8').replace('7.3-CANDIDATE','7.3 · estado pre-canónico histórico')
text=replace_any(text,SAN_BLOCK,'> **OPEN TO SYNTHESIS ≠ VALIDATED.**',after=True)
san.write_text(text,encoding='utf-8')

idx=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md')
text=idx.read_text(encoding='utf-8').replace('7.3-CANDIDATE','7.3 · estado pre-canónico histórico')
text=replace_any(text,INDEX_BLOCK,'> **OPEN TO SYNTHESIS ≠ VALIDATED.**',after=True)
idx.write_text(text,encoding='utf-8')

print('NEOCORE_73_CANON_NAV=SYNCED')
