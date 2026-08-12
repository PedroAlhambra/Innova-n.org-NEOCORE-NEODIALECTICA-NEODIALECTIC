from pathlib import Path
p=Path('manifiestos/54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md')
text=p.read_text(encoding='utf-8')
repls=[
("This is not the archetype of misery. It is the archetype of the **material second chance**.","""This is not the archetype of misery.

It is the archetype of the **material second chance**."""),
("It looks at a part and asks: what still works? what can be repaired? what can be dismantled without destruction? which component can serve another object? which material can be recovered? which story deserves preservation? which residue can become art? which knowledge can be passed forward?","""It looks at a part and asks:

- what still works?;
- what can be repaired?;
- what can be dismantled without destruction?;
- which component can serve another object?;
- which material can be recovered?;
- which story deserves preservation?;
- which residue can become art?;
- which knowledge can be passed forward?"""),
("Repair should not remain confined to hobbies, precarity or economic emergency. It should become **basic social infrastructure**.","""Repair should not remain confined to hobbies, precarity or economic emergency.

It should become **basic social infrastructure**."""),
("Society needs electronics repairers, furniture restorers, mechanics, welders, carpenters, textile repairers and tailors, cobblers, appliance technicians, material recoverers, bicycle repairers, reuse artisans, remanufacturing specialists, metal/glass/complex-material recyclers, design-for-disassembly specialists, residue artists, tool libraries, community workshops, repair cooperatives, recovered-parts markets and specialists in safe classification of hazardous waste.","""Society needs more:

- electronics repairers;
- furniture restorers;
- mechanics;
- welders;
- carpenters;
- textile repairers and tailors;
- cobblers;
- appliance technicians;
- material recoverers;
- bicycle repairers;
- reuse artisans;
- remanufacturing specialists;
- metal, glass and complex-material recyclers;
- design-for-disassembly specialists;
- residue artists;
- tool libraries;
- community workshops;
- repair cooperatives;
- recovered-parts markets;
- specialists in safe classification of hazardous waste."""),
("Every product should try, where technically and materially reasonable, to optimise disassembly, access to parts, documentation, spare-part availability, modularity, component replacement, updates without artificial disablement, identifiable materials, end-of-life recovery, compatibility with common tools, and reduction of unnecessary irreversible adhesives or joints.","""Every product should try, where technically and materially reasonable, to optimise:

- disassembly;
- access to parts;
- documentation;
- spare-part availability;
- modularity;
- component replacement;
- updates without artificial disablement;
- identifiable materials;
- end-of-life recovery;
- compatibility with common tools;
- reduction of unnecessary irreversible adhesives or joints."""),
("Reducing waste and pollution is not merely “environmental management”. It is a form of coexistence.","""Reducing waste and pollution is not merely “environmental management”.

It is a form of coexistence."""),
("The [Contribution Economy™](./04_economia_del_aporte_ES_EN.md) should recognise the value of those who prevent extraction, extend an object's life, share a repair, document disassembly, recover a component, design a repairable product, clean a space, classify waste, turn discard into art, teach a craft, create an open tool or maintain common infrastructure.","""The [Contribution Economy™](./04_economia_del_aporte_ES_EN.md) should recognise the value of those who:

- prevent extraction;
- extend an object's life;
- share a repair;
- document disassembly;
- recover a component;
- design a repairable product;
- clean a space;
- classify waste;
- turn discard into art;
- teach a craft;
- create an open tool;
- maintain common infrastructure."""),
("The right to repair should therefore be accompanied by reasonable access to manuals, spare parts, diagnostic information, technical training, school and community workshops, shared tools, safety standards, transparent second-hand markets and protection against artificial repair barriers when they are not justified by real safety needs.","""The right to repair should therefore be accompanied by:

- reasonable access to manuals;
- spare parts;
- diagnostic information;
- technical training;
- school and community workshops;
- shared tools;
- safety standards;
- transparent second-hand markets;
- protection against artificial repair barriers when they are not justified by real safety needs."""),
("Children should learn that things have structure. That they can be opened, understood and maintained. That breaking does not always mean ending.","""Children should learn that things have structure.

That they can be opened.

That they can be understood.

That they can be maintained.

That breaking does not always mean ending."""),
("Not to turn everyone into mechanics. To prevent everyone from becoming powerless consumers.","""Not to turn everyone into mechanics.

To prevent everyone from becoming powerless consumers."""),
("Each neighbourhood could support nodes for repair, exchange, tool lending, part recovery, second-hand use, artistic reuse, training, composting where appropriate, material classification, component libraries and open documentation of solutions.","""Each neighbourhood could support nodes for:

- repair;
- exchange;
- tool lending;
- part recovery;
- second-hand use;
- artistic reuse;
- training;
- composting where appropriate;
- material classification;
- component libraries;
- open documentation of solutions."""),
("Waste then stops being a place. It becomes a **classification question**.","""Waste then stops being a place.

It becomes a **classification question**."""),
("On the contrary, if material recovery is a central function, it should receive labour protection, adequate equipment, training, infrastructure, professional recognition, decent wages, material traceability, health controls, producer responsibility and classification/decontamination technology.","""On the contrary.

If material recovery is a central function, it should receive:

- labour protection;
- adequate equipment;
- training;
- infrastructure;
- professional recognition;
- decent wages;
- material traceability;
- health controls;
- producer responsibility;
- classification and decontamination technology."""),
("Neodialectics proposes a broader account of contribution: avoided matter, added useful life, conserved embedded energy, avoided social cost, transmitted knowledge, gained autonomy, avoided waste, created beauty and preserved memory.","""Neodialectics proposes a broader account of contribution:

- avoided matter;
- added useful life;
- conserved embedded energy;
- avoided social cost;
- transmitted knowledge;
- gained autonomy;
- avoided waste;
- created beauty;
- preserved memory.""")]
for a,b in repls:
    if text.count(a)!=1: raise SystemExit(f'target count {text.count(a)}: {a[:90]}')
    text=text.replace(a,b,1)
p.write_text(text,encoding='utf-8')
print('MANIFESTO_54_STRUCTURE=OK')
