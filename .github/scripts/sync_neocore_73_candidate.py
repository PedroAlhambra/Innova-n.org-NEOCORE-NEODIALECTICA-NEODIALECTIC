from pathlib import Path
import runpy

# Remove superseded numeric version labels before rebuilding the active 7.3-CANDIDATE surfaces.
runpy.run_path('.github/scripts/migrate_neocore_pre_73_refs.py', run_name='__main__')

START='<!-- NEOCORE_73_CANDIDATE_START -->'
END='<!-- NEOCORE_73_CANDIDATE_END -->'

ROOT_BLOCK=f'''{START}\n\n### NEOCore™ 7.3-CANDIDATE · Capa de Autosíntesis Recursiva™ / Recursive Self-Synthesis Layer™\n\nNEOCore™ desarrolla públicamente **7.3-CANDIDATE** como frontera evolutiva activa. La nueva capa recorre las preguntas abiertas del corpus, genera una respuesta interna provisional, construye su antítesis, clasifica el estado epistemológico y conserva la necesidad de contraste externo. **Autorresponder ≠ autovalidar.** / NEOCore™ publicly develops **7.3-CANDIDATE** as its active evolutionary frontier. The new layer traverses open questions in the corpus, generates a provisional internal answer, constructs its antithesis, classifies epistemic status and preserves the need for external scrutiny. **Self-answering ≠ self-validation.**\n\n**[Documento versionado / Versioned document](./propuestas/sintesis-abierta/NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)** · **[Matriz #161 / Matrix #161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161)** · **[Lote I–XII #162 / Batch I–XII #162](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/162)**\n\n{END}\n'''

SAN_BLOCK=f'''{START}\n\n## NEOCore™ 7.3-CANDIDATE · Capa de Autosíntesis Recursiva™\n## NEOCore™ 7.3-CANDIDATE · Recursive Self-Synthesis Layer™\n\nLa evolución 7.3-CANDIDATE añade una fase recursiva a SAN™: pregunta abierta → retorno al corpus → respuesta interna provisional → antítesis/red-team → estado epistemológico → evidencia/falsadores → síntesis versionada → contraste externo → delta/reapertura. Una pregunta puede estar respondida internamente y seguir abierta porque `OPEN` significa **revisable**, no necesariamente «sin respuesta». / The 7.3-CANDIDATE evolution adds a recursive phase to SAN™: open question → return to corpus → provisional internal answer → antithesis/red-team → epistemic status → evidence/falsifiers → versioned synthesis → external scrutiny → delta/reopening. A question may be internally answered and remain open because `OPEN` means **revisable**, not necessarily “unanswered”.\n\n> **AUTORRESPONDER ≠ AUTOVALIDAR / SELF-ANSWERING ≠ SELF-VALIDATION.**\n\n[Documento / Document](NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md) · [Matriz / Matrix #161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161) · [Primer lote I–XII / First batch I–XII #162](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/162) · [Registro documental / Documentary registry #163](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/163)\n\n{END}\n'''

INDEX_BLOCK=f'''{START}\n\n## 0 · NEOCore™ 7.3-CANDIDATE · Autosíntesis Recursiva™ / Recursive Self-Synthesis™\n\n- **Documento versionado / Versioned document:** [NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md](NEOCORE_7_3_AUTOSINTESIS_RECURSIVA_ES_EN.md)\n- **Matriz conceptual / Conceptual matrix:** [#161](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/161)\n- **Lote 01 · I–XII / Batch 01 · I–XII:** [#162](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/162)\n- **Registro documental / Documentary registry:** [#163](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/163)\n- **Estado / Status:** `7.3-CANDIDATE`; promoción a canon sólo tras superar el gate de cobertura, evidencia, simetría y auditoría. / promotion to canon only after passing the coverage, evidence, symmetry and audit gate.\n\n{END}\n'''

def replace_or_insert(text, block, anchor, after=True):
    if START in text and END in text:
        a=text.index(START)
        b=text.index(END,a)+len(END)
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
    lines[0]='# Innova_N — NEOCore™ 7.3-CANDIDATE · Neodialéctica™ / Neodialectics™ · Neodialectica Framework™'
    text='\n'.join(lines)+'\n'

    # Keep one current architecture heading; prior numeric labels are intentionally not exposed.
    import re
    text=re.sub(
        r'## NEOCore™ .*?· Primera Capa Fractal Multicabeza™ \+ Capa Neoaxiomática™ \+ Soberanía de Síntesis™\n## NEOCore™ .*?· First Fractal Multihead Layer™ \+ Neoaxiomatic Layer™ \+ Synthesis Sovereignty™',
        '## NEOCore™ 7.3-CANDIDATE · Arquitectura pública en evolución / Public architecture in evolution\n### Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™ / First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™',
        text,
        count=1,
    )

    text=text.replace(
        '#innova_n--neocore-pre-73--neodialéctica--neodialectics--neodialectica-framework',
        '#innova_n--neocore-73-candidate--neodialéctica--neodialectics--neodialectica-framework',
    )
    return text

root=Path('README.md')
text=root.read_text(encoding='utf-8')
text=sync_root_version_surface(text)
text=replace_or_insert(text,ROOT_BLOCK,'## 🔴 Actualidad / Latest',after=True)
root.write_text(text,encoding='utf-8')

san=Path('propuestas/sintesis-abierta/README.md')
text=san.read_text(encoding='utf-8')
text=replace_or_insert(text,SAN_BLOCK,'> **OPEN TO SYNTHESIS ≠ VALIDATED.**',after=True)
san.write_text(text,encoding='utf-8')

idx=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md')
text=idx.read_text(encoding='utf-8')
text=text.replace('**Fecha / Date:** 2026-08-18','**Fecha / Date:** 2026-08-19',1)
text=replace_or_insert(text,INDEX_BLOCK,'> **OPEN TO SYNTHESIS ≠ VALIDATED.**',after=True)
idx.write_text(text,encoding='utf-8')

print('NEOCORE_73_CANDIDATE_NAV=SYNCED')
