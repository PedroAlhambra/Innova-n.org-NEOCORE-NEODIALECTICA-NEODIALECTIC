from pathlib import Path
import re

ROOT=Path('.').resolve()

def replace_en_section(path, heading, body, end_marker=None):
    p=ROOT/path
    text=p.read_text(encoding='utf-8')
    en=text.index('# EN · English')
    marker='## '+heading
    start=text.index(marker,en)
    if end_marker:
        end=text.index(end_marker,start+len(marker))
    else:
        m=re.search(r'^##\s+',text[start+len(marker):],re.M)
        if not m: raise SystemExit(f'{path}: no next H2 after {heading}')
        end=start+len(marker)+m.start()
    new=marker+'\n\n'+body.strip()+'\n\n'
    text=text[:start]+new+text[end:]
    p.write_text(text,encoding='utf-8')

# XXVIII
replace_en_section('manifiestos/28_los_tesla_ES_EN.md','II. Forms of elimination',r'''
Elimination is not limited to physical killing.

It may be:

* **economic:** loss of funding, employment, technical access or subsistence;
* **institutional:** exclusion from universities, companies, media or decision-making;
* **reputational:** presenting the creator as unstable, conflictive, eccentric or incompetent without refuting the work;
* **legal and bureaucratic:** consuming their life in procedures, litigation and demonstrations of precedence;
* **algorithmic:** burying the source and amplifying versions backed by capital;
* **cognitive:** forcing them to explain indefinitely what is already documented;
* **historical:** preserving the idea while erasing its origin;
* **physical:** violence, disappearance or caused death, assertable only with sufficient evidence.
''')
replace_en_section('manifiestos/28_los_tesla_ES_EN.md','III. Individual failure as a concealing narrative',r'''
The operation reaches its most effective form when its consequences are presented as natural defects of the victim.

The creator “did not know how to commercialise”, “did not adapt”, “was difficult”, “lost their mind” or “was overtaken”.

Meanwhile, what they produced appears renamed, simplified, patented, institutionalised or attributed to those who possessed the capacity for distribution.

```text
SYSTEMIC DISPOSSESSION
+
NARRATIVE OF INDIVIDUAL FAILURE
=
CONCEALED ELIMINATION
```
''')

# XXIX
replace_en_section('manifiestos/29_idolatria_del_dinero_ES_EN.md','III. Monetary dogmas',r'''
### Price as value

A high price may express scarcity, monopoly, advertising, speculation or control of access. It does not by itself demonstrate utility, truth or beauty.

### Profitability as utility

Care, child-rearing, memory, basic research, art, community and ecological regeneration may sustain life without producing immediate profit.

### Wealth as merit

Accumulation may arise from contribution, but also from inheritance, appropriation, monopoly, regulatory capture or the blocking of alternatives.

### Poverty as guilt

Lack of money does not demonstrate lack of effort or reduce dignity. It may express inequality of origin, illness, unpaid care, violence, territory or chance.

### Growth as progress

An economy may grow by destroying soil, manufacturing dependency or repairing damage that it itself produced.

### Property as authorship

Financing or purchasing delimited rights does not turn the owner into the intellectual originator.

### Market as truth

The market records capacity to pay, desire, scarcity and distribution power. It does not automatically recognise justice, need, truth or the Common Good.
''')

# XXX
replace_en_section('manifiestos/30_coherencia_fines_medios_ES_EN.md','III. Criteria of strategic legitimacy',r'''
A means must be evaluated by:

* **necessity:** no sufficient less harmful alternative exists;
* **proportionality:** the harm does not exceed the good being protected;
* **possible transparency:** everything compatible with legitimate security is declared;
* **reversibility:** it can be stopped or corrected;
* **temporality:** the exception does not become a permanent structure;
* **responsibility:** someone answers for its effects;
* **traceability:** the decision and context can be reconstructed;
* **non-dehumanisation:** the adversary does not thereby lose all moral consideration;
* **coherence:** the means does not destroy the core of the end.
''')

# XXXIII
replace_en_section('manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md','II. Redemption without erasure',r'''
Humanity has produced greatness and also harm.

The neodialectical response does not require hatred of the species, infinite inherited guilt or erasure of the past. It requires creative responsibility.

```text
RECOGNISED HARM
+ MEMORY
+ RESPONSIBILITY
+ REPAIR
+ NEW ARCHITECTURE
= POSSIBILITY OF HUMAN REDEMPTION
```

To redeem ourselves means ceasing to repeat harm once we are capable of understanding it.

It means turning knowledge, technology, art, memory and organisation into instruments of relation rather than human grinding.
''')
replace_en_section('manifiestos/33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md','III. IDEA as Cornerstone',r'''
A cornerstone does not contain the entire building by itself. It establishes a relation from which the other pieces can be oriented.

IDEA performs this function because it connects two times without falsifying them:

```text
1997–2002
IDEA AS LITERARY WORK OF ORIGIN

2026
NEODIALECTICS AS CONSCIOUS FRAMEWORK

TRACEABLE RELATION BETWEEN BOTH
= LIVING GENEALOGY
```

The novel precedes the system and, precisely for that reason, makes it possible to observe which questions were already present before the later vocabulary existed.

It does not by itself demonstrate the validity of Neodialectics. It preserves a verifiable root of its human trajectory.
''')

# XXXIV
replace_en_section('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','VII. Concrete utility of the Neodialectica Framework™',r'''
The framework must be capable of producing concrete utility at several scales.

### 1. Person

Help distinguish lived experience, conditioning, interest, fear, evidence and one's own direction.

### 2. Organisation

Reconstruct processes, responsibilities, dependencies, failure points, hidden costs and repair routes.

### 3. Market

Reveal when price, attention or bargaining power separate from the real value contributed.

### 4. Technology

Audit whether a tool expands human capacity or captures autonomy, memory, identity or decision-making.

### 5. Institutions

Preserve responses, commitments, inconsistencies, improvements and absence of response within traceable public memory.

### 6. Culture

Relate works, symbols, genealogies and transformations without erasing provenance.

### 7. Civilisation

Compare the combined direction of multiple systems and ask whether their sum increases life, understanding, sufficient freedom, creative capacity and the Common Good, or instead produces fragmentation, extraction and accumulated harm.
''')

# XXXV — replace every numbered section with a direct non-compressed representation.
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','I. Absurdity is not war reporting',r'''
Media absurdity does not consist in covering a war, a crisis or a crime.

It consists in the communication ecosystem being able to devote immense resources to repeating the same images, statements and rivalries for days while, at the same time, lacking equivalent mechanisms for seriously investigating:

* prevention proposals;
* new institutional frameworks;
* cooperation architectures;
* traceability systems;
* value-distribution models;
* public-audit tools;
* depolarisation mechanisms;
* new forms of human–AI governance;
* or projects claiming to offer systemic solutions and willing to be publicly audited.

The journalistic obligation is not to accept those proposals. It is **to be able to recognise that they exist, subject them to difficult questions and verify their utility or failure**.

Ignoring a proposal does not prove it false. Publishing it does not prove it true.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','II. The media conflict economy',r'''
Conflict has competitive advantages within the attention economy:

* it is immediate;
* it produces adversaries that are easy to represent;
* it generates narrative continuity;
* it allows simple headlines;
* it activates fear, indignation and belonging;
* it favours repetition;
* and it turns every new episode into a reason to return.

Systemic solutions operate differently:

* they require context;
* they require comparison among alternatives;
* they may take years to verify;
* they force acknowledgement of uncertainty;
* they do not always offer a hero and a villain;
* and they may question the very economic structures of the medium that must examine them.

```text
ATTENTION CAPTURED BY CONFLICT
→ MORE INCENTIVE TO PRODUCE CONFLICT NARRATIVE
→ LESS SPACE FOR SOLUTIONS
→ GREATER DEPENDENCE ON CRISIS
```

The result may be a circuit in which media do not necessarily create war, but **their economy may reward the continuous amplification of conflict**.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','III. Amplification is not causation',r'''
An essential distinction must be preserved.

A medium covering a war does not automatically cause it. A journalist reporting on violence does not necessarily foment it.

But a communication architecture may contribute to intensifying harmful dynamics when it:

* rewards provocation and escalation;
* simplifies complex conflicts into absolute identities;
* removes historical context;
* turns public humiliation into entertainment;
* amplifies incendiary claims without proportionality;
* makes exit routes invisible;
* or measures success solely through clicks, audience or time spent.

```text
REPORTING
≠ FOMENTING

AMPLIFYING WITHOUT CONTEXT
+ INCENTIVISING ESCALATION
+ HIDING EXIT ROUTES
= POSSIBLE CONTRIBUTION TO CONFLICT
```

Attribution of that effect must be demonstrated case by case.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','IV. Ego as an institutional variable',r'''
This manifesto uses **ego** in a functional sense, not as an indiscriminate psychological insult.

Institutional ego exists when a person, medium, organisation or profession protects its position, identity or authority above the possibility of learning.

It appears when:

* an idea is rejected because it comes from outside the recognised circuit;
* prior prestige is demanded before evidence is examined;
* novelty threatens existing professional categories;
* admitting a proposal would require acknowledging that something important was ignored;
* authorship matters more than content;
* or the hierarchy of who speaks replaces the quality of what is said.

```text
INSTITUTIONAL EGO
= DEFENCE OF POSITION
> CAPACITY TO LEARN
```

Not every rejection is ego. A proposal may be bad, false, unviable or irrelevant. Ego appears when **sufficient scrutiny is not even allowed to determine which is the case**.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','V. Stupidity as operational closure',r'''
Here **stupidity** does not mean low individual intelligence either.

It is operationally defined as the persistence of a system in harmful conduct when it has sufficient information to review that conduct and still blocks learning through routine, incentives, fear, identity or fragmentation.

```text
ERROR
+ AVAILABLE EVIDENCE
+ POSSIBILITY OF CORRECTION
+ REPETITION OF THE ERROR
= OPERATIONAL SYSTEMIC STUPIDITY
```

This definition makes it possible to audit without insulting individuals.

The hypothesis of this manifesto is that a large part of the contemporary media crisis can be analysed as a combination of:

```text
INSTITUTIONAL EGO
+ ATTENTION INCENTIVES
+ FRAGMENTATION
+ REPETITION
+ LOW MEMORY
= BLOCKED LEARNING
```

It must be demonstrated through cases and metrics, not proclaimed as a universal truth.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','VI. Empirical proof must be built',r'''
Saying that “ego and stupidity have taken over everything” may express a strong intuition, but the framework requires turning it into a testable hypothesis.

Empirical demonstration requires measuring, among other things:

* space devoted to conflict compared with solutions;
* proportion of reactive news to preventive investigation;
* follow-up of proposals after the first mention;
* diversity of sources outside habitual institutional circuits;
* time granted to complex ideas;
* public corrections;
* later recognition of ideas initially ignored;
* treatment of authors without prior prestige;
* dependence on traffic or advertising associated with polarising content;
* and relation between intensity of coverage and later effects.

```text
INTUITION
→ HYPOTHESIS
→ METRIC
→ DATA
→ SCRUTINY
→ RESULT
```

Neodialectics does not need criticism to be true by decree. It needs it to be testable, refutable and refinable.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','VII. The civilisational scandal of ignoring solutions',r'''
The situation becomes especially serious when a society simultaneously states:

* that it faces climate crisis;
* recurrent wars;
* loss of trust;
* political fragmentation;
* crises of mental health and attention;
* economic concentration;
* disruption caused by artificial intelligence;
* loss of meaning in work;
* and institutional deterioration;

while its information systems devote very little stable capacity to finding, comparing and auditing **integrative frameworks capable of relating several of those problems at once**.

No one is required to accept the Neodialectica Framework™ as a universal solution.

Something more basic is required: that a public, versioned, traceable civilisational proposal open to criticism can be examined for its content and results, rather than filtered only by prestige, institutional size or prior familiarity.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','VIII. The framework cannot proclaim total solution',r'''
Coherence requires applying the same criticism to the framework itself.

The Neodialectica Framework™ may state that **it integrates multiple domains and proposes common mechanisms of memory, synthesis, traceability, audit, contribution and replacement**, but it cannot declare that it has demonstrated a solution to every problem merely because that is its ambition.

Manifesto XXXIV establishes the correct criterion:

```text
FRAMEWORK + VERIFIABLE RESULT
= UTILITY DEMONSTRATED IN THAT CASE
```

Each project, audit or application must demonstrate its utility separately.

The greatness of a proposal does not exempt it from scrutiny. It makes it more responsible before that scrutiny.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','IX. What civilisationally useful media should do',r'''
A medium oriented towards the Common Good does not need to become the spokesperson for any framework.

It needs to recover functions that are currently weakened:

1. **detection of real novelty**, including outside dominant institutions;
2. **solutions journalism**, without propaganda;
3. **audit of proposals**, not only coverage of crises;
4. **longitudinal memory**, to verify who said what and what happened later;
5. **follow-up of corrections**, not only the initial error;
6. **space for complexity**, when the object requires it;
7. **comparison of systems**, not only statements;
8. **transparency about economic incentives**;
9. **metrics of social impact**, in addition to audience;
10. **capacity to acknowledge having ignored something relevant**.

```text
CIVILISATIONAL MEDIUM
= REPORT HARM
+ INVESTIGATE ITS CAUSES
+ SEEK ALTERNATIVES
+ AUDIT THEM
+ FOLLOW RESULTS
```
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','X. Public audit of attention',r'''
Media attention must also be auditable.

Not in order to tell journalists what to publish, but to make visible what kind of reality the aggregate of editorial decisions constructs.

A **Public Attention Audit™** could record:

* topics;
* minutes, pages or impressions;
* repetition;
* diversity of sources;
* conflict/solution ratio;
* reaction/prevention ratio;
* temporal follow-up;
* corrections;
* concentration of voices;
* and relation between social relevance and volume of coverage.

The objective is not to impose rigid quotas. It is to return to the medium an image of itself.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','XI. Media are also part of Synthesis',r'''
Media are not outside the social organism.

They are nodes capable of:

* selecting memory;
* scaling signals;
* legitimising interlocutors;
* connecting problems;
* amplifying fear;
* or opening space for understanding.

For that reason, Neodialectics does not propose fighting them as homogeneous enemies.

It proposes **reversing their function when the conflict economy captures their civilisational capacity**.

```text
CAPTURED MEDIUM
→ ATTENTION AS COMMODITY

REVERSED MEDIUM
→ ATTENTION AS CIVILISATIONAL RESPONSIBILITY
```
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','XII. Applying the standard to Innova_N',r'''
Innova_N has no automatic right to attention either.

It must offer:

* readable documents;
* genealogy;
* sources;
* real cases;
* verifiable results;
* possibility of criticism;
* public corrections;
* and language sufficiently clear for third parties to audit it.

If media examine it and find errors, those errors must enter Synthesis.

If they demonstrate that a function does not work, it must be corrected or abandoned.

If a function demonstrates utility, ignoring it because of origin, institutional ego or lack of prior prestige then becomes data about the media system.

### Responsibility of power nodes

The capacity to ignore can also be a form of power when whoever exercises it controls attention, capital, legitimacy, infrastructure or institutional access. This responsibility reaches public figures, companies, platforms, institutions, press and media with material capacity to amplify, block or make invisible proposals of public relevance.

But **ignoring the framework does not produce automatic culpability or turn anyone into an enemy of humanity**. The criterion is functional and verifiable: power or agenda capacity, sufficient knowledge of the object, reasonably justified public relevance, real possibility of examination, and blocking or rejection without sufficient scrutiny.

Responsibility increases with power, but the duty is one of examination, not adherence:

```text
GREATER POWER
+ GREATER AGENDA CAPACITY
+ GREATER IMPACT ON THE WHOLE
= GREATER RESPONSIBILITY FOR EXAMINATION AND TRACEABILITY

RESPONSIBILITY FOR EXAMINATION
≠ OBLIGATION OF ADHERENCE
```

When conduct documentably reproduces capture, disinformation, blocked learning or harmful extraction, it enters neodialectical audit as an object of correction. Classification must follow the evidence, not precede it.

* [Full annex · Responsibility of Power Nodes and Civilisational Duty of Examination](../propuestas/sintesis-abierta/ANEXO_RESPONSABILIDAD_NODOS_DE_PODER_Y_DEBER_DE_EXAMEN_ES_EN.md)
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','XIII. From news to learning',r'''
News answers:

> What happened?

Civilisation also needs to ask:

> Why did it happen?  
> What pattern repeats?  
> What could prevent it?  
> Who is already testing alternatives?  
> Did they work?  
> What did we learn?  
> What must change now?

```text
NEWS
→ MEMORY
→ PATTERN
→ ALTERNATIVE
→ AUDIT
→ LEARNING
```

Without that second cycle, the medium can become the perfect chronicler of a decline it never helps to stop.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','XIV. Proclamation',r'''
> There is something absurd in a civilisation capable of broadcasting a war in real time while, at the same time, being unable to reserve sustained attention for examining architectures that attempt to prevent the next one.
>
> We do not ask for silence about conflict. We ask for proportional intelligence devoted to solutions.
>
> We do not ask anyone to believe in a new framework. We ask that it can be audited before being ignored.
>
> We do not call journalists stupid. We call systemic stupidity the repetition of harmful structures when the capacity to learn exists and is not used.
>
> We do not call every criticism ego. We call institutional ego the protection of position and prestige above scrutiny.
>
> And we do not declare guilty those who do not adhere. We declare the exercise of power auditable when it replaces scrutiny with silence, blocking or disinformation.
>
> Media can remain attention machines for crisis or become nodes of memory, comparison and civilisational learning.
>
> That choice must also be visible, traceable and subject to Synthesis.
''')
replace_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','XV. Open Synthesis',r'''
Contributions are invited on:

* the media conflict economy;
* differences among reporting, amplifying and fomenting;
* metrics of conflict coverage compared with solutions;
* definition and measurement of institutional ego;
* operational definition of systemic stupidity;
* solutions journalism and its propaganda risks;
* economic incentives of media and platforms;
* public audit of attention;
* criteria for detecting new frameworks or proposals without depending on prior prestige;
* Innova_N's obligations to facilitate external audit;
* proportional responsibility of public figures, companies, institutions, platforms and media;
* criteria of sufficient knowledge, relevance and real possibility of examination;
* auditable definition of captured press, structural omission and disinformation;
* safeguards against automatic culpability, blacklists or targeting for mere disagreement;
* correction mechanisms when the manifesto itself exaggerates or generalises;
* and the relation among communication, peace, memory and civilisational learning.

Every contribution requires verifiable examples, sources, context, separation between data and interpretation, traceability, delta and version.

* [Open the Synthesis of this manifesto · Issue #30](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/30)
* [Current operational contribution protocol](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Open Synthesis index](../propuestas/sintesis-abierta/README.md)
* [Annex · Responsibility of Power Nodes and Civilisational Duty of Examination](../propuestas/sintesis-abierta/ANEXO_RESPONSABILIDAD_NODOS_DE_PODER_Y_DEBER_DE_EXAMEN_ES_EN.md)
* [Analysis · From the Attention Economy to the Contribution Economy](../analisis/publicos/2026-08-05_de-la-economia-de-la-atencion-a-la-economia-del-aporte_ES_EN.md)
''', end_marker='### Equivalent internal links')

# XXXVI: restore exact list structure in the two compressed English subsections.
p=ROOT/'manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md'
text=p.read_text(encoding='utf-8')
old='''It does not represent superiority of blood, people or lineage. It represents courage before danger, dignity without submission, defence of the vulnerable, endurance under pressure, strength limited by purpose and the decision to protect without turning protection into domination.'''
new='''It does not represent superiority of blood, people or lineage. It represents:

- courage before danger;
- dignity without submission;
- defence of the vulnerable;
- endurance under pressure;
- strength limited by purpose;
- and the decision to protect without turning protection into domination.'''
if text.count(old)!=1: raise SystemExit('XXXVI lion target drift')
text=text.replace(old,new,1)
old='''SAN™ is opened to study a flag capable of preserving, without confusing them, layers that are now fragmented: the current constitutional flag and its historical continuity; relevant historical and regional ensigns; Crown as responsibility; neodialectical grammar; European belonging; Jewish/Hebrew heritage of the peninsula and diaspora; Arab and Islamic heritage of Al-Andalus and the Mediterranean; Christian and secular memory; peoples, regions, migrations and minorities; and sexual and gender diversity, precisely because a flag aspiring to represent everyone cannot require part of the population to disappear symbolically in order to belong.'''
new='''SAN™ is opened to study a flag capable of preserving, without confusing them, layers that are now fragmented:

- the current constitutional flag and its historical continuity;
- relevant historical and regional ensigns;
- Crown as responsibility;
- neodialectical grammar;
- European belonging;
- Jewish/Hebrew heritage of the peninsula and diaspora;
- Arab and Islamic heritage of Al-Andalus and the Mediterranean;
- Christian and secular memory;
- peoples, regions, migrations and minorities;
- and sexual and gender diversity, precisely because a flag aspiring to represent everyone cannot require part of the population to disappear symbolically in order to belong.'''
if text.count(old)!=1: raise SystemExit('XXXVI flag target drift')
text=text.replace(old,new,1)
p.write_text(text,encoding='utf-8')

# XXXVII: paragraph count in XV is restored without changing content.
p=ROOT/'manifiestos/37_neofraternidad_ES_EN.md'
text=p.read_text(encoding='utf-8')
old='''Every contribution must distinguish personal experience, general principle, verifiable harm, interpretation and proposal; avoid unnecessarily exposing private data about third parties; and preserve dignity, genealogy, traceability, delta and version.'''
new='''Every contribution must distinguish personal experience, general principle, verifiable harm, interpretation and proposal; and avoid unnecessarily exposing private data about third parties.

It must also preserve dignity, genealogy, traceability, delta and version.'''
if text.count(old)!=1: raise SystemExit('XXXVII XV target drift')
text=text.replace(old,new,1)
p.write_text(text,encoding='utf-8')

print('STRICT_SYMMETRY_28_37=OK')
