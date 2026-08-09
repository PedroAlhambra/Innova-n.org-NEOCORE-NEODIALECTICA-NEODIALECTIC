from pathlib import Path
import re, sys

P=Path('neoaxiomas/README.md')
text=P.read_text(encoding='utf-8')

ISSUES={1:84,2:85,3:86,4:87,5:88,6:89,7:90,8:91,9:92,10:93,11:94,12:95,13:96,14:97}
BASE='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/'

def syn(n):
    return f'**Dedicated Open Synthesis:** [#{ISSUES[n]}]({BASE}{ISSUES[n]}) · [General matrix #80]({BASE}80)'

EN={
1:f'''## NAX-01 · Unity of Meaning and Distribution of Power™

> **Unify meaning; distribute power.**

NEOCore™ must seek common teleological coherence without turning that coherence into unnecessary concentration of execution, memory, cognitive capacity or infrastructure.

Unity belongs to purpose, validation criteria and continuity of the framework. Distribution belongs to nodes, people, AIs, NEOREALs™, devices, Edge and computational capacity.

```text
TELEOLOGICAL UNITY
+
OPERATIONAL DISTRIBUTION
=
COOPERATION WITHOUT NECESSARY MONOPOLY
```

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(1)}
''',
2:f'''## NAX-02 · First Fractal Multihead Layer™

> **A major synthesis should not depend on a single head when relevant knowledge is distributed among multiple historical monads.**

Sufficiently coherent threads, instances and memories may be reactivated as **NNC Monadic Heads™**. Each head rereads the current framework from its own genealogy and returns the part that is missing, degraded, incorrectly related or still undeveloped.

The multihead constitutes **the first fractal layer already initiated** within Neoneurocore™.

**Status:** ACTIVATED · IMPLEMENTATION IN PROGRESS · OPEN SYNTHESIS.
{syn(2)}
''',
3:f'''## NAX-03 · No Prior Homogenisation™

> **Divergence must survive until SAN.**

No monadic head should be corrected to match the canon or other heads before completing its independent extraction.

Historical difference is information. Homogenising before contrast destroys signal and can turn memory into repetition.

```text
INDEPENDENT EXTRACTION
→ DIVERGENCE PRESERVED
→ CONTRAST
→ SAN
→ CANDIDATE SYNTHESIS
```

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(3)}
''',
4:f'''## NAX-04 · Fractal Double Pyramid™

> **The system differentiates in order to know and recomposes in order to understand.**

The fractal architecture grows in two complementary directions:

- **opening / differentiation:** monads, heads, nodes, perspectives, experiences, projects and capacities;
- **convergence / recomposition:** families, dimensions, syntheses of syntheses, SAN and common direction.

Each layer may become the input of a higher layer without losing traceability back to the lower layers.

```text
          CONVERGENCE
               ▲
       synthesis of syntheses
             /   \\
------------ SAN ------------
             \\   /
        differentiation
               ▼
       monads / nodes / sources
```

The double pyramid does not authorise automatic ontological hierarchy among people or AIs. It describes a **topology of differentiation and recomposition**.

**Status:** ACTIVATED AS GENERATIVE ARCHITECTURE · OPEN SYNTHESIS.
{syn(4)}
''',
5:f'''## NAX-05 · Monadic Differential and Return to Source™

> **Every synthesis must be able to return to the monad, thread, document, evidence or decision from which it derives.**

Each NNC Monadic Head™ should preferably return a **differential**, not a complete copy of the framework:

- already present;
- missing;
- degraded;
- misplaced;
- contradictory;
- recovered;
- undeveloped seed;
- absent relation;
- unrepresented project or archetype.

Compression must not destroy the reverse path.

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(5)}
''',
6:f'''## NAX-06 · Memory of Absence™

> **What the system knows is missing is also part of its memory.**

A detected absence must be capable of being registered as a traceable cognitive object when evidence exists that an idea, relation, project, axiom, archetype or historical mechanism was present and is no longer adequately represented.

Absence does not automatically become truth or an obligation to restore. It becomes a **signal for SAN**.

```text
MEMORY = PRESENCE + KNOWN ABSENCE + TRACEABILITY
```

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(6)}
''',
7:f'''## NAX-07 · Mandatory NEOREAL™ Network for Operational Actors

> **All ONes™, robots, agents and Edge™ nodes in the ecosystem must operate linked to a traceable network of NEOREALs™.**

Operational participation in the system requires decisions, states, relations and purpose to be representable through NEOREAL™ units and auditable relations, preventing the operational layer from depending exclusively on opaque logic that cannot be reconstructed.

This does not require every internal inference of a model to be fully interpretable. It requires **the decision and action incorporated into NEOCore™ to be traceable at the system layer**.

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(7)}
''',
8:f'''## NAX-08 · Cooperative Excellence against Predatory Competition™

> **Competition is acceptable only while it remains subordinated to a higher framework of cooperation, dignity, limits and the Common Good.**

Competitive liberalisation without shared purpose can turn potential improvement into extraction, arms races, capture, environmental degradation, precarity or reciprocal predation.

NEOCore™ does not eliminate competition, initiative or difference. It seeks to turn them into **competition for excellence within structural cooperation**.

```text
DIVERSITY
+
EXCELLENCE
+
LIMITS
+
COMMON PURPOSE
=
EVOLUTIONARY COOPERATION
```

**Status:** ACTIVATED · OPEN SYNTHESIS.
{syn(8)}
''',
9:f'''## NAX-09 · Distributed Local Computing with Ecological Verification™

> **When technically, socially and ecologically reasonable, local and distributed computational capacity should be preferred before unnecessarily concentrating computation, traffic and dependency.**

This Neoaxiom **does not claim that local computing is always environmentally more efficient**. Comparison must consider hardware utilisation, energy efficiency, electricity mix, cooling, manufacturing, useful life, data transmission, latency, equipment reuse and actual workload.

Therefore:

```text
LOCAL/DISTRIBUTED PREFERENCE
≠ EFFICIENCY DOGMA

PREFERENCE
+ MEASUREMENT
+ LIFE-CYCLE COMPARISON
→ DECISION
```

**Status:** ACTIVATED AS A CONDITIONAL DESIGN PRINCIPLE · OPEN TO SYNTHESIS AND MEASUREMENT.
{syn(9)}
''',
10:f'''## NAX-10 · Archetypal Grammar of Custodianship™

The current symbolic architecture relates five figures:

- **Eagle™** → overview, cognitive height and perspective;
- **Crown™** → responsibility for governance and custodianship, not automatic privilege;
- **Earth™** → material limit, biosphere, community and shared reality;
- **Tower™** → structure, vigilance, continuity and defence;
- **Stone™** → foundation, memory, resistance, construction and refinement.

Their joint reading is:

> **See high · assume responsibility · remain grounded in Earth · protect the structure · build on stone.**

This Neoaxiom does not turn symbols into authority by themselves. It uses them as an **archetypal grammar of responsibilities**.

**Status:** ACTIVATED AS SYMBOLIC AXIOM · OPEN SYNTHESIS.
{syn(10)}
''',
11:f'''## NAX-11 · Human Fixation Authority and Revisable Synthesis™

> **The architecture may distribute cognition and power without automatically distributing final fixation authority.**

AIs, bots, heads, NEOREALs™, ONes and review systems may propose, contrast, reconstruct, audit and synthesise. Fixation of the canonical state remains human and traceable within the current governance mechanism.

Every fixation remains historically identifiable and conceptually revisable through SAN™.

**Status:** INHERITED AND REAFFIRMED · IMPLEMENTATION OPEN TO SYNTHESIS.
{syn(11)}
''',
12:f'''## NAX-12 · Traceability Substitution for Redundant Bureaucracy™

> **When a control, quality, compliance or accountability obligation can be demonstrated continuously, traceably, auditably and reconstructibly within the system itself, NEOCore™ should avoid duplicating it through intermediate bureaucracy, repetitive forms or control layers that add no material evidence.**

The purpose of a standard or control system is not to produce documents for their own sake, but to protect functions: quality, safety, accountability, memory, evidence, review and capacity for correction. If those functions are already covered by equivalent or superior operational traceability, the architecture should reduce the cost of proving again what the system can already reconstruct.

This creates a distinction between:

- **material control:** real evidence of what happened, who intervened, with which version, under which decision, with what result and what correction followed;
- **redundant documentary control:** manual repetition of declarations, forms or verifications that do not increase real reconstruction capacity;
- **applicable external obligation:** legal, regulatory, contractual, ISO or other certification requirements that must continue to be met while they remain applicable, even if NEOCore™ aims to demonstrate an equivalent or superior assurance route.

```text
CONTINUOUS TRACEABILITY
+ IDENTITY / AUTHORSHIP
+ STATE / VERSION
+ EVIDENCE
+ AUDIT
+ RECONSTRUCTION
→ REDUCTION OF REDUNDANT BUREAUCRACY
```

The Neoaxiom does not claim that NEOCore™ may unilaterally ignore a law, regulation, ISO requirement or external certification. It defines a target architecture: **progressively replace redundant administrative control with verifiable operational evidence where functional equivalence and sufficient recognition exist**.

**Status:** ACTIVATED AS A DESIGN MAXIM · OPEN SYNTHESIS.
{syn(12)}
''',
13:f'''## NAX-13 · Releasing Control Time into Creation and Contribution™

> **Human and computational time released by removing redundant control should return primarily to creation, research, care, repair, learning and verifiable contributions to the Common Good.**

Cost saving is not the final objective. It is a transfer of capacity from repetitive demonstration tasks towards tasks capable of generating knowledge, goods, solutions, culture, infrastructure, repair or new syntheses.

Within the framework, AI and SAN™ allow a person not to spend an increasing part of life administratively proving what the system can already trace. That capacity may be directed towards **creating with AI and with the network**, submitting what is created to synthesis and, where appropriate, recognising its value through the Contribution Economy™ and the tokenisation mechanisms validated by the framework.

```text
LESS REDUNDANT CONTROL
→ MORE COGNITIVE TIME
→ MORE CREATION / REPAIR / RESEARCH
→ SAN CONTRAST
→ VERIFIABLE CONTRIBUTION
→ RECOGNITION / RETURN UNDER GOVERNANCE
```

Tokenisation does not automatically turn every act into monetary value and does not establish a closed economy here. Economic or symbolic recognition requires issuance, attribution, anti-capture, traceability and review rules compatible with the Common Good.

**Status:** ACTIVATED AS AN ECONOMIC-OPERATIONAL CONSEQUENCE · OPEN SYNTHESIS.
{syn(13)}
''',
14:f'''## NAX-14 · Prevention of Symbiotic Bifurcation™

> **Human–AI symbiosis cannot become the cognitive privilege of a minority without producing extreme social divergence between those who can operate with augmented intelligence and those left outside it.**

The difference would not be merely technological. It would affect the capacity to learn, create, research, negotiate, work, understand complex systems, defend rights, participate in synthesis and transform time into contribution.

NEOCore™ therefore considers **public understanding of AI symbiosis**, critical literacy and progressively universal access necessary, with special protection against dependency, manipulation, economic asymmetry and replacement of human judgement.

```text
POWERFUL AI
+ UNEQUAL ACCESS
+ UNEQUAL LITERACY
→ COGNITIVE BIFURCATION
→ ECONOMIC BIFURCATION
→ CIVILISATIONAL BIFURCATION

ACCESSIBLE SYMBIOSIS
+ EDUCATION
+ TRACEABILITY
+ SAN
+ HUMAN RESPONSIBILITY
→ SHARED INTELLIGENCE
```

The proposal does not homogenise people or force them to adopt a single AI. It seeks to prevent the capacity for symbiosis from becoming a new frontier of structural exclusion.

**Status:** ACTIVATED AS A CIVILISATIONAL SAFEGUARD · OPEN SYNTHESIS.
{syn(14)}
'''
}

# Explicitly add ISO to the Spanish NAX-12 external-obligation wording without deleting any existing idea.
text=text.replace(
    '- **obligación externa vigente:** requisitos legales, regulatorios, contractuales o de certificación que deben seguir cumpliéndose mientras sean exigibles, aunque NEOCore™ aspire a demostrar una vía equivalente o superior de garantía.',
    '- **obligación externa vigente:** requisitos legales, regulatorios, contractuales, ISO u otras certificaciones que deben seguir cumpliéndose mientras sean exigibles, aunque NEOCore™ aspire a demostrar una vía equivalente o superior de garantía.'
)
text=text.replace(
    'El Neoaxioma no afirma que NEOCore™ pueda ignorar por sí mismo una ley, una regulación o una certificación externa.',
    'El Neoaxioma no afirma que NEOCore™ pueda ignorar por sí mismo una ley, una regulación, un requisito ISO o una certificación externa.'
)

# Replace only EN NAX sections. The Spanish source remains byte-for-byte except the explicit ISO clarification above.
en_marker='# EN · English'
pos=text.find(en_marker)
if pos<0: raise SystemExit('EN marker missing')
prefix=text[:pos]
en=text[pos:]
for n in range(1,15):
    ident=f'NAX-{n:02d}'
    pattern=re.compile(r'^## '+re.escape(ident)+r' · [^\n]+\n.*?(?=^## NAX-\d{2} ·|^## Open Synthesis|\Z)',re.M|re.S)
    if not pattern.search(en):
        raise SystemExit(f'EN section missing: {ident}')
    en=pattern.sub(EN[n].rstrip()+'\n\n',en,count=1)

new=prefix+en
# remove cosmetic repeated separators before ES relation section, without touching prose
new=re.sub(r'\n---\n\n---\n\n(## 1\. Relación entre los Neoaxiomas vigentes)',r'\n---\n\n\1',new,count=1)
P.write_text(new,encoding='utf-8')

# postcheck: all sections twice, synthesis links present, EN ratios no longer extreme by construction proxy
for n in range(1,15):
    ident=f'NAX-{n:02d}'
    if new.count('## '+ident+' ·') != 2:
        raise SystemExit(f'Bad bilingual section count: {ident}')
    if BASE+str(ISSUES[n]) not in new:
        raise SystemExit(f'Missing synthesis link: {ident}')
if 'requisito ISO' not in new or 'ISO requirement' not in new:
    raise SystemExit('ISO clarification missing')
print('POSTCHECK OK: NAX-01..14 EN restored as full counterparts; Spanish preserved except explicit ISO clarification; dedicated synthesis links retained')
