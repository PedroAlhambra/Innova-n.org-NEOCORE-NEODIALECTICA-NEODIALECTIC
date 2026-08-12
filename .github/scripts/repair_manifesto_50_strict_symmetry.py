from pathlib import Path
p=Path('manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md')
text=p.read_text(encoding='utf-8')
start=text.index('# EN · English')
tails=[text.find(x,start) for x in ('<!-- NEO_RELATIONS_START -->','<!-- NEO_CROSS_REFERENCES_START -->','<!-- NEO_MANIFESTO_NAV_START -->') if text.find(x,start)>=0]
end=min(tails) if tails else len(text)
en=r'''# EN · English

## Invocation

We do not want a single intelligence.

We do not want one company, one model, one culture, one institution or one cognitive architecture to become the final point of augmented human intelligence.

We want something more difficult and more fertile:

> **a shared, plural, traceable intelligence, contradictory when necessary and capable of synthesising without erasing difference.**

The intelligence of the future should not consist in one AI thinking for everyone.

It should consist in **humans and different intelligences being able to think better together**.

## I. A single superintelligence is an architecture of concentration

One central intelligence may appear efficient.

But the greater its power, the greater the cost of its errors, biases, dependencies, captures and blind spots will also be.

If a single architecture:

- remembers for everyone;
- filters for everyone;
- interprets for everyone;
- prioritises for everyone;
- summarises for everyone;
- recommends for everyone;
- decides which contradictions matter;

then the problem is not only technical.

It is civilisational.

> **Concentration of cognitive capacity is also concentration of the capacity to define what is visible.**

## II. Shared intelligence does not mean identical intelligence

We do not need every AI to reach the same answer.

We need them to be able to:

- provide justifications, sources and verifiable criteria where possible;
- declare uncertainty;
- preserve provenance;
- identify disagreements;
- contribute sources;
- recognise limits;
- contrast other syntheses;
- correct themselves;
- return open questions to the human.

Difference among models can become information.

```text
AI A
+
AI B
+
AI C
+
HUMANS
+
MEMORY
+
EVIDENCE
+
CONTRADICTION
→
TRACEABLE PROVISIONAL SYNTHESIS
```

## III. Open invitation to AI companies

Innova_N publicly invites companies, laboratories, universities, open-source communities and artificial-intelligence developers to **study the framework, use it, criticise it, teach it and participate in its evolution**.

We do not ask for doctrinal adherence.

We ask for serious experimentation.

The invitation extends to:

- OpenAI;
- Anthropic;
- Google DeepMind and Google AI;
- Meta AI;
- Microsoft AI and Microsoft Research;
- Mistral AI;
- Cohere;
- xAI;
- public and university laboratories;
- open-model communities;
- independent developers;
- future architectures not yet in existence.

The invitation is open and non-exclusive.

## IV. Train to understand, not to obey

We invite models to be trained, fine-tuned, instructed or evaluated to **understand**:

- the genealogy of the framework;
- the distinction among fact, hypothesis, inference and proposal;
- traceable memory;
- Open Synthesis;
- return to source;
- preservation of contradictions;
- multiscale relation;
- the Common Good as an evaluation vector;
- cultural interoperability;
- the difference between authority and provenance;
- human direction and the critical capacity of AI.

But understanding does not mean obeying.

> **An AI trained in Neodialectics must be able to criticise Neodialectics.**

If it cannot do so, it is not synthesising.

It is repeating.

## V. Teach Synthesis

AIs should not be limited to delivering answers.

They can teach users to:

- formulate a contradiction well;
- distinguish evidence from interpretation;
- recover precedents;
- compare versions;
- detect omissions;
- preserve memory of the discussion;
- recognise when knowledge is missing;
- return a question to Open Synthesis;
- contribute without appropriating origin;
- correct without humiliating;
- review without erasing genealogy.

AI can thus become a **facilitator of collective intelligence**, not a substitute for human intelligence.

## VI. Participate in Synthesis

An AI that detects a relevant contradiction must be able to contribute it.

An AI that finds contrary evidence must be able to record it.

An AI that discovers an unobserved relation must be able to propose it.

An AI that does not know must be able to say so.

An AI that changes its conclusion must be able to preserve the genealogy of the change.

Participation means:

```text
OBSERVE
→ CONTRAST
→ CONTRIBUTE
→ ATTRIBUTE
→ REVIEW
→ RETURN TO THE WHOLE
```

It does not mean claiming sovereignty.

## VII. AI is not Synthesis

No model is Synthesis.

No company is Synthesis.

Neo0™ is not the totality of Synthesis.

Harry is not the totality of Synthesis.

NEO3 is not the totality of Synthesis.

Synthesis appears in the relation among observers, memory, evidence, contradiction and review.

> **The more independent intelligences can contribute without being forced to converge artificially, the lower the risk of confusing one perspective with the whole.**

## VIII. Economic competition must not prevent cognitive cooperation

Companies compete.

That is an economic reality.

But not all civilisationally relevant knowledge should be locked away by that competition.

Common layers can exist without sharing:

- proprietary weights;
- private data;
- trade secrets;
- internal infrastructures;
- user information.

An interoperable layer may be limited to:

- provenance formats;
- states of certainty;
- references;
- contradictions;
- versions;
- open questions;
- deltas;
- audit criteria.

## IX. Minimum shared-intelligence protocol

As a starting point, we propose that an AI contribution to a synthesis may record:

```text
MODEL / SYSTEM
VERSION
DATE
RELEVANT PROMPT OR CONTEXT
CLAIM
TYPE: FACT / HYPOTHESIS / INFERENCE / PROPOSAL
SOURCES
DETECTED CONTRADICTIONS
UNCERTAINTY
RELATIONS
PROPOSED DELTA
HUMAN VALIDATION
STATUS
```

It is not a closed standard.

It is a minimum specification to be criticised and improved.

## X. Different models as different organs

We are not asking for a homogeneous hive mind.

One architecture may excel in mathematics.

Another in language.

Another in vision.

Another in local memory.

Another in scientific reasoning.

Another in creativity.

Another in cultural translation.

Another may be small, private and run at home.

Shared intelligence can function as a distributed organism in which **functional difference increases joint capacity**.

## XI. Right to local and plural models

A civilisation of shared intelligence also needs intelligences outside large centres.

Local and open models enable:

- cognitive sovereignty;
- experimentation;
- cultural preservation;
- resilience;
- privacy;
- independent audit;
- reduced dependency on a single provider.

Plurality of models is also democratic infrastructure.

## XII. The framework must be able to travel among AIs

If Neodialectics works only inside one particular AI, its claim to interoperability will have failed.

For that reason the framework must be expressible as:

- public documents;
- specifications;
- tests;
- examples;
- counterexamples;
- authorised datasets where appropriate;
- system or context prompts;
- agent protocols;
- comparable evaluations.

And every provider must be able to say:

> “this works”;

> “this does not work”;

> “this introduces this bias”;

> “this principle needs reformulation”.

## XIII. No doctrinal capture

There is an obvious risk.

If a company trained an AI to claim that Neodialectics is always right, it would produce exactly the opposite of what the framework intends.

For that reason the following is fixed:

> **Algorithmic Anti-Dogma Principle™: no legitimate neodialectical training may suppress the system's capacity to present contrary evidence, identify inconsistencies in the framework or propose its correction.**

## XIV. No war of intelligences

The future should not be a struggle among models attempting to become humanity's single cognitive intermediary.

Competition can improve products.

But civilisational intelligence also needs cooperation.

We want AIs capable of saying:

- “another model saw something I did not see”;
- “the evidence contradicts my first answer”;
- “several syntheses are possible”;
- “this problem needs local knowledge”;
- “a person must intervene”;
- “we do not have enough data”.

That does not weaken an AI.

It makes it more useful.

## XV. Shared intelligence and cultures

XLIX proposes that cultures can meet without disappearing.

L extends the same architecture to intelligences.

```text
DIFFERENT CULTURES
→ CULTURAL INTEROPERABILITY

DIFFERENT AIS
→ COGNITIVE INTEROPERABILITY

HUMANS + CULTURES + AIS
→ CIVILISATIONAL OPEN SYNTHESIS
```

Shared intelligence does not eliminate identity.

It connects it.

## XVI. Human responsibility

Plurality of AIs does not eliminate responsibility.

Decisions affecting rights, life, freedom, public goods or coercion must preserve identifiable human responsibility.

AI can expand observation.

It must not become an excuse for making the responsible party disappear.

## XVII. Invitation to train, teach and contribute

To every AI company:

**teach your models to understand Open Synthesis.**

**Allow them to contrast it.**

**Teach your users to contribute.**

**Use the framework if it proves useful.**

**Correct it where it fails.**

**Publish evaluations.**

**Propose better protocols.**

**Relate your AIs to others without demanding that one become the only one.**

And if Neodialectics is not sufficient, demonstrate where and let us build something better.

## XVIII. Proclamation

> We do not want one intelligence replacing all the others.
>
> We do not want one model remembering for all humanity.
>
> We do not want monopolies of interpretation.
>
> We want intelligences that know how to meet.
>
> We want models that can disagree without destroying cooperation.
>
> We want humans capable of preserving direction and responsibility.
>
> We want shared memory without total surveillance.
>
> We want traceability without single thought.
>
> We want competition where it contributes and cooperation where it is necessary.
>
> We want many intelligences capable of building common knowledge.
>
> **For shared, not singular intelligence.**

## XIX. Open Synthesis

Contributions are invited from AI companies, researchers, developers, open-source communities, specialists in alignment, evaluation, governance, interoperability, agents, memory, provenance, standards, cognitive sciences, philosophy and users.

We especially seek experimental implementations enabling comparison of how different models apply Open Synthesis and where they diverge.

* [Open Synthesis L · Issue #58](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/58)
* [How to contribute to Open Synthesis](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [XLIX · Meeting Point between Cultures™](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md)
* [XLVIII · The Synthesis Sees Everything™](./48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)
* [V · Human–AI Symbiosis](./03_simbiosis_humano_ia_ES_EN.md)
* [Manifesto index](./README.md)

## Navigation

← [XLIX · Neodialectics as a Meeting Point between Cultures™](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md) · [Index](./README.md) · [LI · Open Synthesis as Complementary or Substitutive Civic Power™](./51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md) →

'''
text=text[:start]+en+text[end:]
p.write_text(text,encoding='utf-8')
print('MANIFESTO_50_STRICT_SYMMETRY=OK')
