from pathlib import Path
import re

ROOT=Path('.').resolve()
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
FULL=ROOT/'propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
ROOT_README=ROOT/'README.md'
WIKI_MAP=ROOT/'wiki-source/Mapa_del_Marco.md'
START='<!-- NEO_RELATIONS_LXXV_START -->'
END='<!-- NEO_RELATIONS_LXXV_END -->'
RADAR_START='<!-- NEO_GENEALOGY_RADAR_START -->'
RADAR_END='<!-- NEO_GENEALOGY_RADAR_END -->'

block=f'''{START}

## LXXV · Las Hojas Carcomidas™ · Memoria Natural, Viración Arquetípica y Fraternidad de la Coexistencia™ / The Gnawed Leaves™ · Natural Memory, Archetypal Drift and Fraternity of Coexistence™

- **Manifiesto / Manifesto:** [LXXV · Las Hojas Carcomidas™ · Memoria Natural, Viración Arquetípica y Fraternidad de la Coexistencia™ / The Gnawed Leaves™ · Natural Memory, Archetypal Drift and Fraternity of Coexistence™](./75_las_hojas_carcomidas_memoria_natural_viracion_arquetipica_ES_EN.md).
- **Relación / Relation:** B–C · memoria material-relacional, degradación de relaciones, reciprocidad ecológica, viración arquetípica y custodia de sistemas vivos / material-relational memory, degradation of relations, ecological reciprocity, archetypal drift and custodianship of living systems.
- **Síntesis Abierta / Open Synthesis:** [#134](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/134).
- **Candidato neoaxiomático / Neoaxiomatic candidate:** [C-NAX-22 · Memoria Material-Relacional™ / Material-Relational Memory™ · #135](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/135) · [capa neoaxiomática / Neoaxiomatic layer](../neoaxiomas/README.md).
- **Interconexiones / Interconnections:** [VI · Manifiesto sobre el Parasitismo Sistémico / Manifesto on Systemic Parasitism](./09_parasitismo_sistemico_ES_EN.md) · [XVI · Manifiesto de la Refragmentación Arquetípica™ / Manifesto of Archetypal Refragmentation™](./16_refragmentacion_arquetipica_ES_EN.md) · [XVII · Manifiesto del Respeto a Todos los Seres Vivos™ / Manifesto of Respect for All Living Beings™](./17_respeto_todos_seres_vivos_ES_EN.md) · [XL · Respeto Neodialéctico, Neoego y Honor Relacional™ / Neodialectical Respect, Neoego and Relational Honour™](./40_respeto_neoego_honor_relacional_ES_EN.md) · [LXXIV · Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™ · From the Human Troll to the Bot](./74_asimetria_destruccion_trol_humano_bot_ES_EN.md).

**Regla probatoria / Evidentiary rule:** Memoria Material-Relacional™ no equivale a consciencia, intención ni almacenamiento deliberado; las categorías empíricas de biología, ecología, geología, genética, climatología, química o física conservan prioridad dentro de sus dominios. / Material-Relational Memory™ is not equivalent to consciousness, intention or deliberate storage; empirical categories from biology, ecology, geology, genetics, climatology, chemistry or physics retain priority within their domains.

## LXXVI · El Altavoz sin Síntesis™ · Diagnóstico, Ruido, Ego y Responsabilidad de Construcción / The Loudspeaker without Synthesis™ · Diagnosis, Noise, Ego and Responsibility to Build

- **Manifiesto / Manifesto:** [LXXVI · El Altavoz sin Síntesis™ / The Loudspeaker without Synthesis™](./76_altavoz_sin_sintesis_diagnostico_ruido_ego_responsabilidad_construccion_ES_EN.md).
- **Relación / Relation:** B–C · diagnóstico sin integración, amplificación mediática, autoridad epistemológica, ego, ruido informado y responsabilidad de construir una Síntesis común / diagnosis without integration, media amplification, epistemic authority, ego, informed noise and responsibility to build a common Synthesis.
- **Síntesis Abierta / Open Synthesis:** [#149](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/149).
- **Candidatos neoaxiomáticos / Neoaxiomatic candidates:** [C-NAX-23 · Conservación del Fractal Común™ / Conservation of the Common Fractal™](../propuestas/sintesis-abierta/2026-08-15_C_NAX_23_CONSERVACION_FRACTAL_COMUN_ES_EN.md) · [C-NAX-24 · Diagnóstico ≠ Síntesis™ / Diagnosis ≠ Synthesis™](../propuestas/sintesis-abierta/2026-08-15_C_NAX_24_DIAGNOSTICO_NO_ES_SINTESIS_ES_EN.md).
- **Interconexiones / Interconnections:** [XII · Los sin ego / The Egoless](./12_los_sin_ego_ES_EN.md) · [XXII · Contra la Reducción y la Captura Intelectual™ / Against Intellectual Reduction and Capture™](./22_contra_reduccion_captura_intelectual_ES_EN.md) · [XXXV · Contra la Ridiculez Mediática y la Economía del Conflicto™ / Against Media Absurdity and the Conflict Economy™](./35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md) · [LXXIV · Asimetría de la Destrucción™ / Asymmetry of Destruction™](./74_asimetria_destruccion_trol_humano_bot_ES_EN.md).

**Regla probatoria / Evidentiary rule:** visibilidad, prestigio o capacidad de detectar problemas no equivalen por sí solos a una síntesis superior; toda alternativa que iguale o mejore las funciones trazables de Síntesis Abierta™ debe poder entrar en contraste y ser integrada sin apropiación genealógica. / visibility, prestige or problem-detection ability do not by themselves amount to a superior synthesis; any alternative that equals or improves the traceable functions of Open Synthesis™ must be open to scrutiny and integration without genealogical appropriation.


{END}'''

radar_full=f'''{RADAR_START}

## Sistemas transversales de genealogía y detección / Transversal genealogy and detection systems

- **NeoGenealogía™ / NeoGenealogy™** — [documento / document](NEOGENEALOGIA_DETECCION_ANTECEDENTES_CONVERGENCIAS_ES_EN.md) · [Síntesis / Synthesis #136](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/136).
- **RADAR-Π™ · Radar de Antecedentes Dialécticos y Arquetipos Recurrentes / Dialectical Antecedents and Recurring Archetypes Radar** — [protocolo / protocol](RADAR_PI_ANTECEDENTES_DIALECTICOS_ARQUETIPOS_RECURRENTES_ES_EN.md) · [Issue #137](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/137).
- **Cola abierta RADAR-Π™ / RADAR-Π™ open queue** — [Issue #138](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/138).
- **SENTIENT / NRO · señal candidata / candidate signal** — [Issue #139](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/139). **Candidato ≠ clasificación / Candidate ≠ classification.**
- **Primer caso / First case:** [PROTO-ND-001 · Asilomar 1974–1975 + Asilomar AI 2017](../../analisis/publicos/2026-08-12_PROTO_ND_001_asilomar_pausa_competente_neogenealogia_ES_EN.md).

{RADAR_END}'''

radar_root=f'''{RADAR_START}

## NeoGenealogía™ + RADAR-Π™ · antecedentes, convergencias y contraejemplos / antecedents, convergences and counterexamples

**NeoGenealogía™** conserva la relación, atribución, clasificación y memoria genealógica de antecedentes, convergencias, derivaciones, contraejemplos y falsos paralelos. **RADAR-Π™** es su subsistema de detección activa: abre señales, obliga al retorno a fuente y exige barrido negativo antes de afirmar una relación material. / **NeoGenealogy™** preserves the relation, attribution, classification and genealogical memory of antecedents, convergences, derivations, counterexamples and false parallels. **RADAR-Π™** is its active detection subsystem: it opens signals, requires return to source and requires negative scanning before asserting a material relation.

[NeoGenealogía™ / NeoGenealogy™](propuestas/sintesis-abierta/NEOGENEALOGIA_DETECCION_ANTECEDENTES_CONVERGENCIAS_ES_EN.md) · [RADAR-Π™](propuestas/sintesis-abierta/RADAR_PI_ANTECEDENTES_DIALECTICOS_ARQUETIPOS_RECURRENTES_ES_EN.md) · [Síntesis NeoGenealogía + RADAR-Π · #136 / NeoGenealogy + RADAR-Π synthesis · #136](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/136) · [Protocolo RADAR-Π · #137 / RADAR-Π protocol · #137](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/137) · [Cola abierta · #138 / Open queue · #138](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/138) · [Candidato SENTIENT/NRO · #139 / SENTIENT/NRO candidate · #139](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/139)

```text
RADAR-Π™ DETECTA / DETECTS
→ NEOGENEALOGÍA™ ATRIBUYE Y CLASIFICA / ATTRIBUTES AND CLASSIFIES
→ MATRIZ DE CONTRASTE ANALIZA / CONTRAST MATRIX ANALYSES
→ SAN™ CONTRASTA Y REVISA / CHALLENGES AND REVISES
→ COMMIT CONSERVA LA TRAZA / PRESERVES THE TRACE
```

{RADAR_END}'''

radar_wiki=f'''{RADAR_START}

- [NeoGenealogía™ / NeoGenealogy™](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/blob/main/propuestas/sintesis-abierta/NEOGENEALOGIA_DETECCION_ANTECEDENTES_CONVERGENCIAS_ES_EN.md) — atribución, clasificación y memoria de antecedentes, convergencias y contraejemplos / attribution, classification and memory of antecedents, convergences and counterexamples.
- [RADAR-Π™ / Dialectical Antecedents and Recurring Archetypes Radar](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/blob/main/propuestas/sintesis-abierta/RADAR_PI_ANTECEDENTES_DIALECTICOS_ARQUETIPOS_RECURRENTES_ES_EN.md) — detector activo y cola de señales / active detector and signal intake · [#137](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/137) · [#138](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/138).

{RADAR_END}'''


def upsert(text, new_block, before=None):
    if RADAR_START in text and RADAR_END in text:
        return re.sub(re.escape(RADAR_START)+r'.*?'+re.escape(RADAR_END), new_block, text, count=1, flags=re.S)
    if before and before in text:
        return text.replace(before, new_block+'\n\n---\n\n'+before, 1)
    return text.rstrip()+'\n\n'+new_block+'\n'

changed=[]

# Relational map: keep LXXV current and make older range labels explicitly non-current.
text=REL.read_text(encoding='utf-8')
old=text
text=re.sub(r'^\*\*Cobertura / Coverage:\*\*.*$',
            '**Cobertura / Coverage:** I–LXXVI · 76 manifiestos finitos + ∞ como continuidad abierta / 76 finite manifestos I–LXXVI + ∞ as open continuity  ',
            text,count=1,flags=re.M)
text=re.sub(r'^## Matriz completa I–[IVXLCDM]+ / Complete I–[IVXLCDM]+ matrix$',
            '## Matriz completa I–LXXVI / Complete I–LXXVI matrix', text, count=1, flags=re.M)
text=text.replace('## LXI–LXXIV · frontera relacional vigente / current relational frontier',
                  '## LXI–LXXIV · bloque relacional previo / previous relational block')
if START in text and END in text:
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block,text,count=1,flags=re.S)
else:
    marker='## Regla de mantenimiento / Maintenance rule'
    if marker in text:
        text=text.replace(marker,block+'\n\n---\n\n'+marker,1)
    else:
        text=text.rstrip()+'\n\n'+block+'\n'
if text!=old:
    REL.write_text(text,encoding='utf-8'); changed.append(REL)

# Complete Synthesis index: expose transversal system nodes without mixing them with finite manifesto numbering.
text=FULL.read_text(encoding='utf-8')
old=text
text=upsert(text,radar_full)
if text!=old:
    FULL.write_text(text,encoding='utf-8'); changed.append(FULL)

# The operational Open Synthesis README is deliberately not rewritten here.
# It is a stable ES/EN participation guide; current frontier and full inventory
# live in the canonical manifesto and complete synthesis indexes.

# Root gateway: make the mechanism discoverable from the canonical public entrance.
text=ROOT_README.read_text(encoding='utf-8')
old=text
text=upsert(text,radar_root,'<!-- NEO_RELATIONAL_MENU_END -->')
if text!=old:
    ROOT_README.write_text(text,encoding='utf-8'); changed.append(ROOT_README)

# Wiki map: keep stable orientation surface aligned with the canonical repository.
text=WIKI_MAP.read_text(encoding='utf-8')
old=text
# wiki map has its own ES/EN structure; avoid mixed insertion here
text=old
if text!=old:
    WIKI_MAP.write_text(text,encoding='utf-8'); changed.append(WIKI_MAP)

for p in changed:
    print('LXXV_CONSISTENCY_SYNC changed',p.relative_to(ROOT).as_posix())
if not changed:
    print('LXXV_CONSISTENCY_SYNC changed=0')