from pathlib import Path

ROOT=Path('.').resolve()

REPAIRS={
'manifiestos/25_pulido_de_la_piedra_ES_EN.md': [(
'''The framework will promote multidimensional education, judgement developed through real projects, contact with works and examples of human greatness, repair instead of totalising condemnation, human–AI mentoring, protection of singularity, Archetypal Refragmentation™ of valuable functions, and continuous review of formative mechanisms to prevent indoctrination and capture.''',
'''The framework will promote:

* multidimensional education;
* development of judgement through real projects;
* contact with works and examples of human greatness;
* repair instead of totalising condemnation;
* human–AI mentoring;
* protection of singularity;
* Archetypal Refragmentation™ of valuable functions;
* and continuous review of formative mechanisms to prevent indoctrination and capture.''')],

'manifiestos/27_valor_alimentos_vida_ES_EN.md': [(
'''These capacities are underused when extractors restrict essential data, conceal prices or availability, block interoperability, maintain inadequate rural connectivity, concentrate logistics information or prevent surplus from reaching need.''',
'''These capacities are underused when extractors:

* restrict essential data;
* conceal prices, margins or availability;
* block interoperability;
* maintain inadequate rural connectivity;
* concentrate logistics information;
* or prevent surplus from being connected with needs.''')],

'manifiestos/28_los_tesla_ES_EN.md': [(
'''Protection must act while the person can still create through verifiable precedence, dates, versions, commits and SHA, explicit attribution, human claims channels, protection against discrediting campaigns, minimum subsistence and proportional return, legal and technical support, archive preservation, protection of cognitive time and separation between criticism of work and destruction of person.''',
'''Protection must act while the person can still create through:

* verifiable precedence;
* dates, versions, commits and SHA;
* explicit attribution;
* human claims channels;
* protection against discrediting campaigns;
* minimum subsistence and proportional return;
* legal and technical support;
* archive preservation;
* protection of cognitive time;
* and separation between criticism of work and destruction of person.''')],

'manifiestos/29_idolatria_del_dinero_ES_EN.md': [(
'''Monetary idolatry normalises destroyed health, families without time, abandoned vocations, degraded territories, industrialised animals, wasted food, dispossessed creators and indebted future generations.''',
'''Monetary idolatry normalises:

* health destroyed to preserve employment;
* families without time;
* vocations abandoned for lack of profitability;
* degraded territories;
* industrialised animals;
* wasted food;
* dispossessed creators;
* and indebted future generations.''')],

'manifiestos/30_coherencia_fines_medios_ES_EN.md': [
(
'''A means does not merely produce an immediate result. It also forms habits, selects allies, normalises behaviour, distributes power, generates debt, changes trust and determines what must be done next.''',
'''A means does not merely produce an immediate result. It also:

* forms habits;
* selects allies;
* normalises behaviour;
* distributes power;
* generates debt;
* changes trust;
* and determines what must be done next.'''),
(
'''Protecting sensitive information, reserving strategy, competing commercially, reporting abuse, withdrawing access, applying proportionate pressure, blocking capture or using sufficient force to stop aggression may be legitimate.''',
'''It may be legitimate to:

* protect sensitive information;
* reserve strategy;
* compete commercially;
* report abuse;
* withdraw access;
* apply proportionate pressure;
* block capture;
* or use sufficient force to stop aggression.'''),
(
'''They become incompatible with the framework when they conceal material information, manufacture deceptive scarcity, exploit vulnerability, induce purchases against the buyer's interest, promise non-existent benefits or turn support for the Common Good into moral coercion.''',
'''They become incompatible with the framework when they:

* conceal material information;
* manufacture deceptive scarcity;
* exploit vulnerabilities;
* induce purchases against the buyer's interest;
* promise non-existent benefits;
* or turn support for the Common Good into moral coercion.'''),
(
'''Every exception requires a verifiable threat, direct relation to protection, minimum duration, limited scope, later record when safe, independent review and prohibition against becoming a general permission.''',
'''Every exception requires:

* a verifiable threat;
* direct relation to protection;
* minimum duration;
* limited scope;
* later record when safe;
* independent review;
* and prohibition against becoming a general permission.'''),
(
'''Every significant strategic action should declare the end pursued, means employed, people affected, foreseeable harms, alternatives considered, duration, review mechanism, intended repair and closure criterion.''',
'''Every significant strategic action should declare:

1. the end pursued;
2. the means employed;
3. the people affected;
4. foreseeable harms;
5. alternatives considered;
6. duration;
7. the review mechanism;
8. intended repair;
9. the closure criterion.'''),
]
}

changed=[]
for rel,repls in REPAIRS.items():
    p=ROOT/rel
    text=p.read_text(encoding='utf-8')
    old_text=text
    for old,new in repls:
        n=text.count(old)
        if n!=1:
            raise SystemExit(f'{rel}: expected one exact repair target, found {n}: {old[:90]!r}')
        text=text.replace(old,new,1)
    if text!=old_text:
        p.write_text(text,encoding='utf-8')
        changed.append(rel)

print('BILINGUAL_SYMMETRY_BATCH_25_30 changed=',len(changed))
for x in changed: print('CHANGED',x)
