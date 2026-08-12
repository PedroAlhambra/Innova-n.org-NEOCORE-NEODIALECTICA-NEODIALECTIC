from pathlib import Path
import re

ROOT=Path('.').resolve()

def replace_en_section(path, heading, body):
    p=ROOT/path
    text=p.read_text(encoding='utf-8')
    en=text.index('# EN · English')
    marker='## '+heading
    start=text.index(marker,en)
    rest=text[start+len(marker):]
    m=re.search(r'^##\s+',rest,re.M)
    end=start+len(marker)+m.start() if m else text.index('<!-- NEO_RELATIONS_START -->',start)
    text=text[:start]+marker+'\n\n'+body.strip()+'\n\n'+text[end:]
    p.write_text(text,encoding='utf-8')

# XLV
P='manifiestos/45_multidimensionalidad_neodialectica_problema_mulo_soberania_distribuida_ES_EN.md'
replace_en_section(P,'Invocation',r'''
A vast share of political, economic, scientific, technological and moral error begins with the same operation:

> **reducing a multidimensional system to one variable and then confusing that variable with the whole of reality.**

Money.

Power.

Ideology.

Class.

Identity.

Intelligence quotient.

Productivity.

Popularity.

Votes.

Data.

One dimension may explain something.

None explains a person, a society or a civilisation by itself.

**Neodialectical Multidimensionality™** begins from this principle:

```text
LIVING REALITY
≠
ONE SCALE
≠
ONE METRIC
≠
ONE CAUSE
≠
ONE IDENTITY
```

Understanding requires relating dimensions without destroying their difference.
''')
replace_en_section(P,'I. The human is not a variable',r'''
A person is simultaneously:

- body;
- memory;
- emotion;
- intelligence;
- history;
- relationships;
- desire;
- fear;
- knowledge;
- error;
- creative capacity;
- responsibility;
- material context;
- cultural context;
- lived time;
- future project;
- and a node inside larger systems.

Reducing a person to consumer, worker, voter, profile, diagnosis, income, political identity or algorithmic score destroys essential information.

Neodialectics does not deny the usefulness of classification.

It denies that a partial classification can become a total definition.
''')
replace_en_section(P,'IV. Multidimensionality as an antidote to caudillismo',r'''
The problem of caudillismo is not solved by pretending exceptional persons, leaders, creators, experts or high-impact nodes do not exist.

It is solved by preventing excellence in one dimension from automatically becoming total domination.

A person may be extraordinary in one dimension and limited in many others.

A great scientist may be morally wrong.

A great entrepreneur may misunderstand society.

A great artist may manage an institution badly.

A great politician may ignore science.

A founder may understand origin better than anyone and still require contradiction regarding the consequences of their proposals.

Correct architecture does not abolish leadership.

**It frames it.**

```text
SINGULARITY
+
TRACEABILITY
+
CONTRADICTION
+
PLURALITY OF NODES
+
LIMITS
+
MEMORY
+
REVIEW
→ LEADERSHIP WITHOUT CAPTURE
```
''')
replace_en_section(P,'V. Distributed sovereignty',r'''
Shared sovereignty does not mean everyone has identical knowledge, function or responsibility.

It means no partial superiority makes anyone owner of another person's conscience.

Every node preserves an irreducible sphere of sovereignty.

And every common sphere requires coordination mechanisms.

```text
PERSONAL SOVEREIGNTY
+
RECIPROCAL RESPONSIBILITY
+
COMMON COORDINATION
+
TRACEABLE CONTRAST
→ DISTRIBUTED SOVEREIGNTY
```

We do not all know the same things.

We cannot all do the same things.

We do not contribute equally to every problem.

But nobody ceases to be a subject because they do not master one particular dimension.
''')
replace_en_section(P,'VI. Multidimensionality dissolves the false opposition between equality and excellence',r'''
A one-dimensional civilisation often falls into one of two traps:

1. denying differences in order to protect equality;
2. turning differences into absolute hierarchies in order to protect excellence.

Multidimensionality makes it possible to move beyond that opposition.

Two people may be unequal in one dimension while remaining equal in dignity.

One may contribute more technical knowledge.

Another may understand human harm better.

Another may possess historical memory.

Another may have greater execution capacity.

Another may contribute creativity.

Another may contribute direct experience.

Synthesis does not need to pretend all contributions are equal.

It needs to **place the value of each contribution correctly in relation to the concrete problem**.
''')
replace_en_section(P,'VIII. No AI contains the complete framework either',r'''
The same rule applies to artificial intelligence.

AI may relate enormous amounts of information and still be wrong.

It may recover context and produce a false synthesis.

It may multiply perspectives while inheriting bias from its data, architecture or instructions.

Neodialectical AI therefore receives no final sovereignty.

It must operate inside a relation:

```text
HUMAN
↔ AI
↔ SOURCES
↔ OTHER HUMANS
↔ OTHER AIS
↔ EXPERIENCE
↔ REALITY
```

Intelligence emerges from relation, not from the idolatry of one node.
''')
replace_en_section(P,'IX. Multidimensionality as a foundation of the Common Good',r'''
The Common Good cannot maximise one variable alone.

If it maximises only economic growth, it may destroy health, community or ecosystems.

If it maximises only security, it may destroy freedom.

If it maximises only individual liberty, it may ignore externalities and vulnerability.

If it maximises only equality, it may destroy functional diversity and initiative.

If it maximises only efficiency, it may sacrifice resilience.

The Common Good requires multivariable and multiscale composition.

There is no final formula that permanently abolishes tension.

There is a process of orientation and correction.

```text
DIMENSIONS
→ RELATIONS
→ TENSIONS
→ CONTRADICTION
→ PROVISIONAL SYNTHESIS
→ MEASUREMENT
→ DELTA
→ NEW SYNTHESIS
```
''')
replace_en_section(P,'X. Temporal multidimensionality',r'''
A decision does not only have multiple simultaneous dimensions.

It also has multiple times.

What is beneficial today may be destructive in twenty years.

What is costly today may prevent a future catastrophe.

A policy may benefit one generation and transfer the bill to another.

The framework therefore requires memory and horizon.

```text
PAST
+
PRESENT
+
POSSIBLE FUTURES
→ TEMPORAL RESPONSIBILITY
```
''')
replace_en_section(P,'XI. Fractal multidimensionality',r'''
The person is not an external observer of the system.

The person is a node within it.

Family.

Neighbourhood.

City.

State.

Species.

Ecosystem.

Planet.

Each scale modifies and is modified by others.

A solution valid at one scale may create harm at another.

Neodialectics therefore asks continuously:

> **what does this solve here, and what does it break there?**

That is the practical function of fractal reading.
''')
replace_en_section(P,'XII. Against capture by a single metric',r'''
Contemporary society is full of substitutes for reality:

- GDP for wellbeing;
- followers for relevance;
- money for value;
- clicks for legitimate attention;
- productivity for contribution;
- scores for learning;
- votes for understanding;
- data for truth;
- office for epistemic authority;
- algorithms for judgement.

Metrics are instruments.

When they replace the object they were meant to measure, they become capture mechanisms.

Multidimensionality returns metrics to their proper place.
''')
replace_en_section(P,'XVI. Open Synthesis',r'''
Contributions are invited on:

- multidimensional models of persons and societies;
- limits of single metrics;
- relation among singularity, leadership and capture;
- the Mule Problem as a metaphor for systems unable to integrate anomalies;
- complex-systems theory, cybernetics and resilience;
- psychology of ego and plurality of capacities;
- distributed governance;
- equality, dignity and excellence;
- multidisciplinarity and limits of expertise;
- AI as a contrast node rather than final sovereignty;
- temporality, scales and externalities;
- function and limits of ™ denominations within the corpus;
- criteria for Integrable Anomaly™;
- and evidence that contradicts, limits or improves the theses of this manifesto.

* [Open Synthesis XLV · Issue #53](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/53)
* [How to contribute to Open Synthesis](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Manifesto index](./README.md)
''')

# XLVI
P='manifiestos/46_cerrar_la_herida_comprension_evolutiva_memoria_reconciliacion_ES_EN.md'
replace_en_section(P,'I. The past was not born knowing what we know now',r'''
Humanity did not appear equipped with universal human rights, modern science, democratic institutions, psychology, global historical memory or technological capacity for self-observation.

For much of history it survived through structures that could be adaptive in some environments and devastating in others:

- tribalism;
- extreme group obedience;
- fear of strangers;
- rigid hierarchies;
- territorial domination;
- preventive violence;
- accumulation;
- patriarchies and coercive orders;
- exemplary punishment;
- purity mythologies;
- absolute loyalties;
- and enemy construction.

Explaining that some of these behaviours have evolutionary, ecological, material or historical roots **does not make them good or inevitable**.

It means understanding why they appeared.

Only mechanisms understood sufficiently can be transformed precisely.

```text
ORIGIN
≠
JUSTIFICATION

EXPLANATION
≠
ABSOLUTION

MEMORY
≠
HEREDITARY CONDEMNATION
```
''')
replace_en_section(P,'II. A wound remains open when understanding is replaced by identity',r'''
A historical wound can become permanent identity.

Pain then ceases to be only memory of what happened.

It begins to organise who we are, who deserves trust, who must pay, who may speak and who must carry inherited guilt.

That mechanism can reproduce itself across generations.

```text
HARM
→ MEMORY
→ WOUNDED IDENTITY
→ TRANSMISSION
→ NEW CONFLICT
→ NEW HARM
```

Closing the wound requires breaking the loop without erasing the original event.
''')
replace_en_section(P,'III. There is no automatic hereditary guilt',r'''
Nobody chooses their ancestors.

Nobody is born personally responsible for crimes committed before they existed.

A society can inherit advantages, harms, institutions, inequalities, silences, symbols and material consequences.

Those consequences may require recognition and repair.

But historical responsibility and personal guilt are not the same.

Neodialectics distinguishes:

```text
PERSONAL GUILT
→ requires one's own action or responsibility

INHERITED RESPONSIBILITY
→ requires understanding and managing received consequences
```

We do not need to manufacture new culprits in order to repair old victims.

We need to transform the conditions that keep harm alive.
''')
replace_en_section(P,'IV. Nor is there an obligation to forget',r'''
Closing a wound does not erase the scar.

A society without memory can repeat what it chose to forget.

Memory fulfils essential functions:

- recognise victims;
- preserve facts;
- prevent denial;
- understand causes;
- detect repeated patterns;
- preserve institutional responsibility;
- and transmit limits to later generations.

But memory ceases to repair when it is used to manufacture perpetual enemies.

Remembering should **reduce the probability of repetition**, not guarantee the continuity of hatred.
''')
replace_en_section(P,'V. Evolutionary understanding',r'''
Humans carry dispositions shaped through biological and cultural histories much older than current institutions.

Cooperation and competition.

Care and aggression.

Empathy and tribalism.

Curiosity and fear.

Altruism and status seeking.

Protection and domination.

There is no one-directional human essence.

There are capacities and tendencies expressed differently depending on culture, education, resources, threat, incentives and institutional architecture.

The Neodialectical question is therefore not:

> “which group is evil?”

but:

> **“which conditions activate destructive behaviour, and which architecture favours cooperative, creative and protective capacities?”**
''')
replace_en_section(P,'VI. Evolution continues culturally',r'''
Biology changes slowly.

Culture can transform in decades what seemed normal for centuries.

Slavery can cease to be regarded as legitimate.

Torture can cease to be accepted as spectacle.

The domination of women can cease to be understood as natural order.

Childhood can cease to be subjected to invasive state guardianship: its protection and upbringing belong primarily to responsible parents or guardians, while institutions should guarantee rights, safety and support without improperly replacing that bond.

War can cease to be glory.

Difference can cease to be threat.

Civilisational evolution consists precisely in **recognising inherited mechanisms and consciously deciding which should no longer govern us**.
''')
replace_en_section(P,'VII. We are not naturally better than our ancestors',r'''
It would be another error to look at the past from effortless superiority.

We possess information, institutions and possibilities they did not have.

And yet we continue to reproduce violence, humiliation, propaganda, exploitation, fanaticism and capture.

The right question is not only:

> “how could they do that?”

but also:

> **“what are we doing now that those who come later will find incomprehensible?”**

Memory works when it makes us less arrogant and more responsible.
''')
replace_en_section(P,'IX. Forgiveness cannot be imposed',r'''
Not every victim can forgive.

Not every wound can close in the same way.

Not every repair can restore what was lost.

Neodialectics does not turn forgiveness into a moral obligation of those who suffered.

Institutional reconciliation can exist without intimate forgiveness.

Coexistence can exist without forgetting.

A boundary can exist without revenge.

Justice can exist without requiring a victim to stop feeling pain.

Closing the wound means that **harm no longer has to govern the future**, not that it disappears from memory.
''')
replace_en_section(P,'X. The intergenerational wound',r'''
Conflicts can be transmitted even when those who started them have already died.

Through stories.

Silences.

Education.

Borders.

Inequalities.

Symbols.

Humiliations.

Fears.

Surnames.

Places.

The next generation receives an emotional map before it can judge that map.

Each generation therefore has a right and a responsibility:

> **to receive memory without receiving an obligation to hate.**
''')
replace_en_section(P,'XI. Closing is not erasing: it is integrating',r'''
A biological wound does not heal because we deny it exists.

It heals because the organism rebuilds relation among damaged parts.

The civilisational metaphor is similar.

```text
WOUND
→ RECOGNITION
→ UNDERSTANDING
→ CARE
→ REPAIR
→ INTEGRATION
→ SCAR
→ MEMORY WITHOUT DOMINATION
```

The scar preserves information.

But it no longer remains permanently open and consuming the organism.
''')
replace_en_section(P,'XIV. The function of the framework',r'''
Neodialectics should serve precisely what fragmented memory cannot do by itself:

- preserve incompatible historical accounts;
- distinguish fact from interpretation;
- recognise different harms;
- relate material, psychological, cultural and political causes;
- prevent capture of memory;
- preserve traceability of responsibility;
- allow contradiction;
- and build syntheses that reduce recurrence of conflict.

Multidimensionality is essential because no historical wound has only one cause.

Memory is essential because no reconciliation can be built on amnesia.

Synthesis is essential because no society can live indefinitely inside an accusation with no exit.
''')
replace_en_section(P,'XVII. Open Synthesis',r'''
Contributions are invited on:

- historical memory and reconciliation;
- individual, collective and intergenerational trauma;
- restorative and transitional justice;
- limits of analogies between biological and cultural evolution;
- tribalism, cooperation and cultural plasticity;
- personal responsibility versus inherited consequences;
- material and symbolic repair;
- forgiveness, boundaries and coexistence;
- prevention of identities organised solely around wounds;
- preservation of memory without mandatory transmission of enmity;
- educational mechanisms for understanding the origins of historical behaviour;
- and evidence that contradicts, limits or improves this manifesto.

* [Open Synthesis XLVI · Issue #54](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/54)
* [How to contribute to Open Synthesis](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Manifesto index](./README.md)
''')

# XLVII
P='manifiestos/47_odio_neo0_sino_goat_sombra_vinculo_doble_cara_ES_EN.md'
replace_en_section(P,'I. The Goat',r'''
In my own symbolic reading of the Chinese zodiac, I recognise myself in the **Earth Goat**.

I use it as an autobiographical archetype.

I do not need to turn it into a scientific law for it to have a narrative and reflective function.

The goat carries.

It seeks support.

It climbs difficult places.

It may look stubborn from outside while simply trying to find somewhere to stand.

**The Goat** also contains a useful contemporary ambiguity.

It can be read as *goat*, the animal.

And it can be read as the cultural acronym *Greatest Of All Time*.

This manifesto rejects turning that second reading into competitive coronation.

I do not need to be “the greatest of all time”.

I need to be able to be whole.

```text
THE GOAT
≠
CROWN OVER OTHERS

THE GOAT
=
PERSONAL SYMBOL
+
EARTH
+
BURDEN
+
ASCENT
+
VULNERABILITY
```
''')
replace_en_section(P,'III. Hatred is data, not a command',r'''
Neodialectics does not need to pretend hatred does not exist.

It exists.

It can be directed at a situation.

At a loss.

At an injustice.

At oneself.

At a trajectory.

At what we feel was imposed upon us.

The error is not recognising the emotion.

The error appears when we automatically convert it into permission to harm.

Therefore:

> **Hatred is data, not a command.**

```text
HATRED
→ SIGNAL
→ QUESTION
→ ORIGIN
→ UNRESOLVED NEED
→ BOUNDARY OR TRANSFORMATION
```

Not:

```text
HATRED
→ ENEMY
→ HARM
```
''')
replace_en_section(P,'IV. People see inventories; they do not always see absences',r'''
I have often felt that someone can look at a life from outside and think:

“he has everything”.

Ability.

Work.

Objects.

Ideas.

Projects.

Apparent freedom.

And from that inventory wonder why the person does not seem to enjoy enough.

But a life is not the sum of its visible possessions.

A house may be full and feel empty.

A schedule may be full and feel lonely.

A mind may be full of ideas while lacking the particular presence it desires.

What prevents enjoyment is not always what one does not possess.

Sometimes it is **who is not there to share what already exists**.
''')
replace_en_section(P,'V. Absence is not cancelled by abundance',r'''
There is a deeply reductive economic fantasy:

```text
MORE RESOURCES
→ MORE WELLBEING
```

Human reality is multidimensional.

Resources matter.

Material security matters.

Autonomy matters.

But so do:

- belonging;
- intimacy;
- friendship;
- reciprocity;
- recognition;
- presence;
- care;
- play;
- shared memory;
- shared time;
- being expected;
- and being able to give someone what one has.

Material abundance does not automatically cancel relational deprivation.
''')
replace_en_section(P,'VI. Envy can also arise from an incomplete image',r'''
A person who observes only visible dimensions may conclude another life is more complete than it really is.

Comparison follows.

And sometimes resentment.

But the comparison is between surfaces:

```text
MY COMPLETE INTERIOR
VS.
YOUR VISIBLE EXTERIOR
```

That comparison is structurally biased.

We do not know the emotional price someone pays for what we admire.

We do not know what they lost.

We do not know whom they miss.

We do not know what fear sustains their activity.

We do not know which part of their success also functions as refuge.

I therefore do not state as fact that “people hate me because they think I have everything”.

I state something more testable and generalisable:

> **when we judge a life from its visible dimensions, we may confuse partial privilege with total fulfilment.**
''')
replace_en_section(P,'VII. I project too',r'''
Multidimensionality must work in both directions.

It is not enough to ask others not to reduce me.

I cannot reduce them either.

If I perceive envy, judgement, distance or rejection, I may be wrong about its origin.

Perhaps there is envy.

Perhaps there is incomprehension.

Perhaps there is fatigue.

Perhaps there is fear.

Perhaps there is an old wound.

Perhaps they simply do not want the same bond I want.

A serious philosophy does not turn every personal pain into a total explanation of another person's mind.
''')
replace_en_section(P,'VIII. This happens to all of us, but not in the same way',r'''
Nobody lives only from inventory.

Even a person with security, knowledge, prestige, beauty, power or resources still needs dimensions that cannot be fully purchased.

Relationship.

Meaning.

Belonging.

Reciprocity.

Time.

Care.

But not everyone suffers equally.

Not everyone lacks the same things.

Not every absence carries the same weight.

The correct universal claim is not:

> “everyone feels exactly what I feel”.

It is:

> **“every human life contains invisible dimensions that external observation can miss.”**
''')
replace_en_section(P,'IX. The framework must look at shadow',r'''
Here appears one of the fundamental differences of the neodialectical architecture.

It is not enough to speak of Common Good, cooperation, mercy, fraternity and future.

A complete architecture must also be able to look at:

- hatred;
- anger;
- desire for revenge;
- ego;
- pride;
- fear;
- cowardice;
- envy;
- jealousy;
- desire for control;
- fantasies of escape;
- resentment;
- exhaustion;
- contradiction;
- and destructive capacity.

Not to celebrate them.

To prevent them from governing from places we refuse to observe.

> **What a system cannot name eventually acts outside its field of correction.**
''')
replace_en_section(P,'X. Two-Face Principle™',r'''
Every person contains potentials that may be oriented in different directions.

Care and domination.

Generosity and possession.

Courage and recklessness.

Dignified pride and narcissism.

Protection and control.

Love and fear of loss.

Creation and desire for recognition.

Neodialectics does not resolve the tension by declaring one face “true” and the other “false”.

It works with both.

> **Two-Face Principle™: no human model is sufficient if it integrates only the capacities it wishes to display and expels from representation the capacities it fears to recognise.**

```text
LIGHT
+
SHADOW
+
MEMORY
+
CONTRAST
+
BOUNDARIES
→ INTEGRATED HUMANITY
```
''')
replace_en_section(P,"XI. The founder's shadow must also be public",r'''
If a founder publishes only certainty, strength, vision and capacity, the result is incomplete.

The origin of the framework should also be traceable through contradiction.

I may feel pride in building something and resentment that it occupied my life.

I may love humanity as a horizon and become tired of particular humans.

I may defend mercy and feel anger.

I may seek connection and want isolation.

I may want recognition and distrust recognition.

I may build a future-oriented system and for an hour wish to have no responsibility for it at all.

That does not automatically invalidate the framework.

It makes it auditable.

The question is not whether the founder has shadow.

He does because he is human.

The question is:

> **can the architecture recognise it, limit it and prevent it from becoming authority?**
''')
replace_en_section(P,'XV. From fate to vector',r'''
This is the final transmutation.

Fate says:

> “this is what I was given.”

The vector asks:

> “where is this going and what can I still change?”

We do not control every condition.

We do not choose every loss.

We cannot force anyone to accompany us.

We cannot reverse time.

But we can understand more clearly which part of the direction remains ours to alter.

```text
FATE
→ AWARENESS
→ VECTOR
→ POSSIBLE CHOICE
```
''')
replace_en_section(P,'XVII. Open Synthesis',r'''
Contributions are invited on:

- fate, agency and perceived imposed trajectory;
- astrology and symbolic systems as personal meaning tools versus empirical claims;
- loneliness, absence and relational wellbeing;
- visible wealth and invisible suffering;
- social comparison, envy and projection;
- emotional ambivalence in leaders, creators and founders;
- integration of shadow without glorification of harm;
- hatred, frustration, grief and need for connection;
- sovereign interdependence;
- moral limits of intense emotions;
- the Two-Face Principle™;
- and evidence that contradicts, limits or improves this manifesto.

* [Open Synthesis XLVII · Issue #55](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/55)
* [How to contribute to Open Synthesis](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Manifesto index](./README.md)
''')

print('STRICT_SYMMETRY_45_47=OK')
