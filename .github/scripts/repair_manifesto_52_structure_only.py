from pathlib import Path
p=Path('manifiestos/52_ciudadania_humana_neodialectica_sangre_suelo_pertenencia_civica_funcional_ES_EN.md')
text=p.read_text(encoding='utf-8')
repls=[
("Future political belonging may progressively rely on real and traceable relations with a community, including effective residence, family and affective bonds, community participation, legal responsibility, taxation where applicable, care, work, study, cooperation, rootedness, stable willingness to belong and acceptance of reciprocal responsibilities.","""Future political belonging may progressively rely on real and traceable relations with a community.

Among them:

- effective residence;
- family and affective bonds;
- community participation;
- legal responsibility;
- taxation where applicable;
- care;
- work;
- study;
- cooperation;
- rootedness;
- stable willingness to belong;
- and acceptance of reciprocal responsibilities."""),
("Communities still need to administer housing, healthcare, education, infrastructure, security, mobility, environment, taxation, institutional capacity, demographic planning and common resources.","""Communities still need to administer:

- housing;
- healthcare;
- education;
- infrastructure;
- security;
- mobility;
- environment;
- taxation;
- institutional capacity;
- demographic planning;
- and common resources.

Therefore:"""),
("It may inform origin, family history, applicable legal frameworks, institutional bonds, residence, active political rights, concrete obligations and routes of protection.","""It may inform:

- origin;
- family history;
- applicable legal frameworks;
- institutional bonds;
- residence;
- active political rights;
- concrete obligations;
- and routes of protection."""),
("Each level may preserve different competences, responsibilities and forms of participation. Belonging to one scale should not require denying the others.","""Each level may preserve different competences, responsibilities and forms of participation.

Belonging to one scale should not require denying the others."""),
("A person may maintain traceable relations with territorial, cultural, professional, scientific, educational, family, cooperative and civilisational nodes.","""A person may maintain traceable relations with different nodes:

- territorial;
- cultural;
- professional;
- scientific;
- educational;
- family;
- cooperative;
- and civilisational."""),
("The question ceases to be only “what country are you from?” and incorporates:","""The question ceases to be exclusively:

> “what country are you from?”

and also incorporates:"""),
("A culture may transmit language, symbols, history, customs, memory, forms of care, art and knowledge without turning someone born elsewhere into a second-class human being.","""A culture may transmit:

- language;
- symbols;
- history;
- customs;
- memory;
- forms of care;
- art;
- knowledge;

without turning someone born elsewhere into a second-class human being."""),
("Contribution has many forms: creating, caring, learning, teaching, maintaining, correcting, protecting, paying taxes, raising children, researching, producing, mediating, participating—or simply passing through a stage of life in which the common organism sustains the person.","""Contribution has many forms:

- creating;
- caring;
- learning;
- teaching;
- maintaining;
- correcting;
- protecting;
- paying taxes;
- raising children;
- researching;
- producing;
- mediating;
- participating;
- or simply passing through a stage of life in which the common organism sustains the person."""),
("Belonging also means being able to ask, contribute, contradict, propose, access public memory, understand decisions, verify answers and participate in the evolution of common rules.","""Belonging also means being able to:

- ask;
- contribute;
- contradict;
- propose;
- access public memory;
- understand decisions;
- verify answers;
- and participate in the evolution of common rules."""),
("Blood and soil may preserve information. They must not become hierarchy.","""Blood and soil may preserve information.

They must not become hierarchy.""")]
for a,b in repls:
    if text.count(a)!=1: raise SystemExit(f'target count {text.count(a)}: {a[:80]}')
    text=text.replace(a,b,1)
p.write_text(text,encoding='utf-8')
print('MANIFESTO_52_STRUCTURE=OK')
