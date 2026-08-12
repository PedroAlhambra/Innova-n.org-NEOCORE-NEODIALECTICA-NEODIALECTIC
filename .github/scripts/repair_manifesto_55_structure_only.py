from pathlib import Path
p=Path('manifiestos/55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md')
text=p.read_text(encoding='utf-8')
repls=[
("Neodialectics must ask who manufactures, who releases, who controls, what capacities the units have, how long they persist, how they degrade, how they are detected, how they are removed, which organisms they affect and what traceability preserves their full life cycle.","""Neodialectics must ask:

- who manufactures;
- who releases;
- who controls;
- what capacities the units have;
- how long they persist;
- how they degrade;
- how they are detected;
- how they are removed;
- which organisms they affect;
- what traceability preserves their full life cycle."""),
("The framework therefore distinguishes intentional attack, negligence, externality, accident, emergent interaction, biological process and technological process.","""The framework therefore distinguishes:

- intentional attack;
- negligence;
- externality;
- accident;
- emergent interaction;
- biological process;
- technological process."""),
("Not afterwards. Before.","""Not afterwards.

Before."""),
("A micromachine may transport a drug, support diagnosis, remove pollutants, repair tissue, detect toxins, inspect infrastructure—or, in future systems, be badly designed, hacked, persistent, contaminating or weaponised.","""A micromachine may:

- transport a drug;
- support diagnosis;
- remove pollutants;
- repair tissue;
- detect toxins;
- inspect infrastructure;
- or, in future systems, be badly designed, hacked, persistent, contaminating or weaponised."""),
("It can describe observable feedback: immune response, biological selection, antimicrobial resistance, population collapse, trophic changes, behavioural changes, social regulation, technological bans, economic reactions and loss of trust.","""It can describe observable feedback:

- immune response;
- biological selection;
- antimicrobial resistance;
- population collapse;
- trophic changes;
- behavioural changes;
- social regulation;
- technological bans;
- economic reactions;
- loss of trust."""),
("A system under pressure changes. Pressure may return to the agent that produced it.","""A system under pressure changes.

Pressure may return to the agent that produced it."""),
("The most dangerous plague would not necessarily be a machine that “wants to kill”. It could be a machine whose local objective keeps operating after the context that gave that objective meaning has disappeared.","""The most dangerous plague would not necessarily be a machine that “wants to kill”.

It could be a machine whose local objective keeps operating after the context that gave that objective meaning has disappeared."""),
("Not every coincidence is causality. Not every particle is a machine. Not every disease is an attack. Not every new technology is deployed merely because it exists in a laboratory.","""Not every coincidence is causality.

Not every particle is a machine.

Not every disease is an attack.

Not every new technology is deployed merely because it exists in a laboratory.""")]
for a,b in repls:
    if text.count(a)!=1: raise SystemExit(f'target count {text.count(a)}: {a[:90]}')
    text=text.replace(a,b,1)
p.write_text(text,encoding='utf-8')
print('MANIFESTO_55_STRUCTURE=OK')
