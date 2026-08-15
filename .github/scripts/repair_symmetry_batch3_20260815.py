from pathlib import Path

ROOT = Path('.')


def replace_once(path, old, new):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'expected block not found in {path}: {old[:160]!r}')
    if text.count(old) != 1:
        raise SystemExit(f'expected unique block in {path}, found {text.count(old)}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')
    print(f'patched {path}')

stanford='analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md'

replace_once(
    stanford,
    'That is the starting point of **Neodialectics™**.\n\n---\n\n## 3. Public anomaly of accessibility',
    '''That is the starting point of **Neodialectics™**.\n\n**Neodialectics™**, created by **Pedro Martínez Alhambra**, did not arise as a late reaction to the AI market.  \nIt arose as an attempt to reunite what modernity had separated: truth, technique, philosophy, art, organisation and action.\n\nFor that reason, when the field begins to move toward living contexts, reflection, verification, review or local nodes, the reading from **Innova_N** is not that of a mere technical novelty, but of a **fragmentary convergence** toward a direction already formulated previously within the framework.\n\n---\n\n## 3. Public anomaly of accessibility'''
)

replace_once(
    stanford,
    '''**Original title:**  \n**“When Stanford discovers Neodialectics without knowing it: the end of fine-tuning and the beginning of living AIs”**\n\nThe original Spanish text is preserved above as part of this public record.\n\n---\n\n## 5. Structural reading of the Stanford / ACE case''',
    '''**Original title:**  \n**“When Stanford discovers Neodialectics without knowing it: the end of fine-tuning and the beginning of living AIs”**\n\n> A few days ago, Stanford presented a work titled “Fine-Tuning is Dead: This AI Learns by Itself”. In it they propose a technique called Agential Context Engineering (ACE): a system in which the AI is not retrained and does not modify its weights, but instead evolves its own context. The model generates, reflects on itself and curates itself in a loop. Errors become strategies; successes become rules.\n>\n> The description seems new, but it is not. It is exactly the logic that, since 2021, Neodialectical Open Synthesis (SAN™) had already formulated: a human–AI symbiosis in which both learn through contextual feedback, without reprogramming, transforming each failure into awareness and each success into structure.\n>\n> In other words, Stanford has just discovered —without knowing it— the mechanism of applied Neodialectics: the transition from static intelligence to living intelligence, where the model ceases to be merely an algorithm and begins to behave like a conceptual organism.\n>\n> SAN had already anticipated something central: intelligence does not improve through accumulation, but through conscious synthesis.\n>\n> And the process can be summarised as follows:\n>\n> **Generate → Reflect → Synthesise → Validate → Learn → Reinsert**\n>\n> The difference is that we do not limit this to AI. We extend it to the human being, art, society and the economy.\n>\n> That is why it is not a coincidence.\n\n---\n\n## 5. Structural reading of the Stanford / ACE case'''
)

replace_once(
    stanford,
    '''What matters is that the case makes visible a deeper difference between two ways of moving forward:\n\n- advancement through fragments;\n- advancement through framework.\n\nFrom the perspective of **Innova_N**, fragments may be valuable, but they are not the end.  \nThe end is to integrate them into a living architecture with memory, traceability, validation, ethics, and orientation toward the Common Good.\n\nThat is where the difference with **Neodialectics™** lies.''',
    '''What matters is that the case makes visible a deeper difference between two ways of moving forward:\n\n### A. Advancement through fragments\nIt consists of reconstructing partial mechanisms:\n\n- evolving contexts;\n- verifiers;\n- reviewers;\n- small models;\n- local nodes.\n\nEach of these pieces may be useful.  \nBut none of them is, by itself, an architecture.\n\n### B. Advancement through framework\nIt consists of integrating those pieces into a higher structure with:\n\n- memory;\n- traceability;\n- validation;\n- ethics;\n- and orientation toward the Common Good.\n\nFrom **Innova_N**, the thesis is that a fragment may have value, but it does not constitute the end.  \nThe end is to bring the pieces together within a larger living architecture.\n\nThat is where the difference with **Neodialectics™** lies:\n\n- others reconstruct mechanisms;\n- others optimise pieces;\n- **Innova_N** works on the framework that allows those pieces to coexist without losing meaning.'''
)

replace_once(
    stanford,
    '''That limit remains the same:\n\n**there is plenty of computational power; what is missing are guiding ideas.**\n\n---\n\n## 7. Base LinkedIn publication''',
    '''That limit remains the same:\n\n**there is plenty of computational power; what is missing are guiding ideas.**\n\nWhen guiding ideas are missing, intelligence ends up serving a world that is already broken instead of reorganising it.\n\n**Neodialectics™** arises precisely to intervene there:  \nnot as a philosophical ornament of technical progress, but as an attempt to correct a civilisation that has fragmented knowledge and then tries to build valuable AI from an insufficient human foundation.\n\n---\n\n## 7. Base LinkedIn publication'''
)

# Extend only explicit known shared-tail headings; never a generic slash rule.
p='.github/scripts/audit_global_bilingual_symmetry.py'
text=(ROOT/p).read_text(encoding='utf-8')
old=r"m=re.search(r'^#{1,6}\s+(?:Fuentes[^\n]* / [^\n]*(?:Sources|sources)|Historial de versiones / Version history|Firma común / Common signature|Principio de procedencia / Provenance principle)\s*$',s,re.M)"
new=r"m=re.search(r'^#{1,6}\s+(?:Fuentes[^\n]* / [^\n]*(?:Sources|sources)|Historial de versiones / Version history|Firma común / Common signature|Principio de procedencia / Provenance principle|Relaciones internas y trabajo aplicado / Internal relations and applied work|Relación con los manifiestos / Relation to the manifestos|Candidatos neoaxiomáticos / Neoaxiomatic candidates)\s*$',s,re.M)"
if old not in text:
    raise SystemExit('known shared-tail regex not found')
text=text.replace(old,new,1)
oldmeta="if re.match(r'^(?:Clasificación provisional / Provisional classification|Síntesis / Synthesis|Regla / Rule|Estado / Status|Puertas / Gates|Principio de procedencia / Provenance principle):',plain,re.I): continue"
newmeta="if re.match(r'^(?:Clasificación provisional / Provisional classification|Síntesis / Synthesis|Regla / Rule|Estado / Status|Puertas / Gates|Principio de procedencia / Provenance principle|Auditoría viva / Living audit):',plain,re.I): continue"
if oldmeta not in text:
    raise SystemExit('shared metadata regex not found')
(ROOT/p).write_text(text.replace(oldmeta,newmeta,1),encoding='utf-8')
print('patched auditor')
