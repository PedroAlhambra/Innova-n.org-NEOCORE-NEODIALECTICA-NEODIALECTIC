from pathlib import Path
import re
ROOT=Path('.').resolve()

def replace_en_section(path, heading, body):
    p=ROOT/path; text=p.read_text(encoding='utf-8'); en=text.index('# EN · English')
    marker='## '+heading; start=text.index(marker,en); rest=text[start+len(marker):]
    m=re.search(r'^##\s+',rest,re.M); end=start+len(marker)+m.start() if m else text.index('<!-- NEO_RELATIONS_START -->',start)
    text=text[:start]+marker+'\n\n'+body.strip()+'\n\n'+text[end:]
    p.write_text(text,encoding='utf-8')

P='manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md'
replace_en_section(P,'I. We are not only in theory',r'''
The repository already contains public applications of the framework to concrete objects.

These include:

* documentary auditing of links, READMEs, manifestos and sources in the repository itself;
* public tracking of publishing, metadata and edition-association incidents involving IDEA in Amazon KDP and Author Central;
* the record of a verifiable correction derived from that process and of improvement proposals sent to KDP;
* the public DistroKid–Spotify case concerning traceability of identifiers and royalties, responses received, insufficient reconciliation and later escalations;
* public analyses concerning the attention economy, Contribution Economy™, AI governance, professional networks, identity, territory and other systems;
* and permanent review of the manifestos themselves through commits, navigation, genealogy and Open Synthesis.

Access points:

* [Public audit index](../auditorias/publicas/README.md)
* [Public analysis index](../analisis/publicos/README.md)
* [Documentary integrity audit](../auditorias/publicas/2026-08-06_auditoria_integridad_enlaces_readmes_wiki_ES_EN.md)
* [KDP · Author Central · IDEA public audit](../analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md)
* [Spotify–DistroKid update](../analisis/publicos/2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md)
* [Second DistroKid escalation](../analisis/publicos/2026-08-06_segundo_escalado_distrokid_sin_respuesta_ES_EN.md)
* [Circular closure and new Spotify–DistroKid escalation](../analisis/publicos/2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md)

This does not mean that “the whole world” or “every system” has already been audited. It means the architecture has moved from formulation to **verifiable public cases**, with a vocation to extend this capacity gradually, traceably and correctably.
''')
replace_en_section(P,'II. What audit means within the framework',r'''
Unless explicitly stated otherwise, the word **audit** is used here in a functional and documentary sense.

It does not automatically claim the legal meaning of a financial audit, regulatory certification, administrative inspection or expert examination requiring specific accreditation.

A public neodialectical audit seeks to:

1. define the object precisely;
2. preserve the source and its date;
3. reconstruct genealogy and context;
4. distinguish facts, statements, inferences, hypotheses and pending matters;
5. locate contradictions and asymmetries;
6. identify who bears costs and who captures returns;
7. formulate testable questions;
8. propose a delta or correction;
9. transmit it to the node capable of acting where one exists;
10. record the response or absence of response;
11. verify the result;
12. publicly correct the audit itself when superior evidence appears.

```text
AUDIT
≠ CONDEMN IN ADVANCE

AUDIT
= MAKE VISIBLE
+ TRACE
+ CONTRAST
+ PROPOSE
+ VERIFY
+ CORRECT
```
''')
replace_en_section(P,'III. Audit begins with ourselves',r'''
The framework loses legitimacy if it demands external traceability while declaring itself immune from it.

Its own documents must therefore be auditable:

* visible authorship;
* dates;
* versions;
* commits;
* deltas;
* genealogical relations;
* verifiable links;
* contradictions preserved where historically relevant;
* explicit corrections;
* and public spaces for challenge and contribution.

Manifestos are not tablets delivered outside history. They are **living objects under joint audit**.

Each new version should be able to answer:

```text
WHAT CHANGED?
WHY DID IT CHANGE?
WHO CONTRIBUTED?
WHAT SOURCE JUSTIFIES IT?
WHAT WAS PRESERVED?
WHAT EFFECT DOES IT HAVE ON THE WHOLE?
```
''')
replace_en_section(P,'V. Open Synthesis as the engine of joint audit',r'''
Open Synthesis distributes review among people with expert knowledge, pertinent experience, sufficient study or ideas capable of producing a material delta.

Its function is not to manufacture unanimity. It is to preserve and relate:

* endorsements;
* objections;
* evidence;
* counterexamples;
* experiences;
* alternative proposals;
* minority positions;
* changes of criterion;
* and later results.

```text
INDIVIDUAL AUDIT
+ HUMAN CONTRAST
+ AI CONTRAST
+ SOURCES
+ VERSIONED MEMORY
= JOINT AUDIT
```

AI expands reading, memory, comparison and contradiction detection. Direction and responsibility do not disappear inside the machine.
''')
replace_en_section(P,'VI. Perpetual does not mean static',r'''
A perpetual audit must change when its object changes.

```text
OPEN
→ UNDER CONTRAST
→ CORRECTION PROPOSED
→ CORRECTION APPLIED
→ VERIFIED
→ REOPENED IF NEW EVIDENCE APPEARS
```

Operationally closing a case does not destroy its memory.

It preserves it for learning and recurrence detection.

A system that forgets every incident forces society to pay the same cost repeatedly.
''')
replace_en_section(P,'VIII. From error to contribution',r'''
The principal purpose of audit is not to find culprits. It is to **find capacity for improvement**.

```text
DETECTED ERROR
→ TRACE
→ CAUSE
→ CORRECTION
→ LEARNING
→ BETTER DESIGN
```

When a company, institution, person or system corrects a problem, that correction must also enter memory.

The framework must recognise improvement with the same traceability with which it documents failure.

Without that symmetry, audit becomes permanent reputational punishment and loses its regenerative function.
''')
replace_en_section(P,'IX. Auditing the auditors',r'''
An auditor may be wrong, exaggerate, select evidence in a biased way or misinterpret a response.

Every neodialectical audit must therefore be auditable.

It must distinguish:

* documented fact;
* a party's statement;
* inference;
* hypothesis;
* interpretation;
* contradiction;
* pending evidence;
* and later correction.

Intentions must not be attributed without sufficient evidence. Unnecessary personal data must not be published. Non-response must not be presented as a confession of guilt.

```text
AUDITOR WITHOUT AUDIT
= NEW BLIND SPOT

AUDIT OF THE AUDIT
= SELF-CORRECTION MECHANISM
```
''')
replace_en_section(P,'XI. WEB4™ as traceability layer',r'''
WEB4™ · SistemaTrazable™ provides the public layer where relationships among sources, works, manifestos, analyses, audits, cases and corrections can remain navigable.

Publishing separate documents is not enough. It must be possible to reconstruct:

* where a claim came from;
* which document developed it;
* which criticism it received;
* which version changed;
* which case tested it;
* and what result followed.

Traceability turns dispersed memory into learning infrastructure.
''')
replace_en_section(P,'XII. Joint audit and systemic replacement',r'''
Manifesto XXXIII proposes systemic reset through replacement.

Perpetual audit provides the mechanism for knowing **what should be preserved, repaired or replaced**.

```text
AUDIT
→ UNDERSTAND FUNCTION
→ MEASURE HARM AND VALUE
→ DESIGN REPLACEMENT
→ TEST
→ VERIFY
→ MIGRATE
```

Without audit, replacement risks destroying useful functions.

Without replacement capacity, audit risks describing harm forever.

Both functions must remain connected.
''')
replace_en_section(P,'XIII. Criterion of success',r'''
The framework does not demonstrate utility by accumulating vocabulary, documents or followers.

It must demonstrate utility through verifiable effects:

* detected and corrected errors;
* preserved memory;
* reduced resolution times;
* improved processes;
* better recognition of creators and affected parties;
* clarified contradictions;
* better-informed decisions;
* avoided harm;
* new capabilities created;
* and learning reusable by third parties.

```text
THEORY WITHOUT EFFECT
= HYPOTHESIS NOT YET OPERATIONALISED

FRAMEWORK + VERIFIABLE RESULT
= UTILITY DEMONSTRATED IN THAT CASE
```

One successful case does not universally prove the whole framework. It proves that a particular function produced a particular result. General validity must be built case by case and remain open to refutation and improvement.
''')
replace_en_section(P,'XV. Open Synthesis',r'''
Contributions are invited on:

* neodialectical audit criteria;
* legal and terminological limits of the word audit;
* distinction among facts, statements, inferences and hypotheses;
* later verification mechanisms;
* auditing the auditors themselves;
* framework-utility metrics;
* relation between audit and the Contribution Economy™;
* public accumulation of learning derived from incidents;
* data protection and minimisation of unnecessary exposure;
* human–AI participation in joint audits;
* relation among manifestos, commits, Issues and perpetual review;
* criteria for closing and reopening cases;
* and the relation among audit, correction and systemic replacement.

Every contribution requires source, context, genealogy, separation between fact and interpretation, traceability, classification, delta and version.

* [Open the Synthesis of this manifesto · Issue #29](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/29)
* [Current operational contribution protocol](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Open Synthesis index](../propuestas/sintesis-abierta/README.md)
* [Public audits](../auditorias/publicas/README.md)
* [Public analyses](../analisis/publicos/README.md)
''')

# XXXVI: exact paragraph count in section XII; keep the same material content.
P='manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md'
p=ROOT/P; text=p.read_text(encoding='utf-8'); en=text.index('# EN · English')
start=text.index('## XII. Open Synthesis',en); rest=text[start+len('## XII. Open Synthesis'):]
m=re.search(r'^##\s+',rest,re.M); end=start+len('## XII. Open Synthesis')+m.start() if m else text.index('<!-- NEO_RELATIONS_START -->',start)
body=r'''
This manifesto has its own Open Synthesis, differentiated from the previous genealogical annex.

Contributions are invited on the limits among custodianship, property and symbolic appropriation; the difference between archetypal recovery and political restoration; the universal meaning of the Age of Man; historical risks associated with Crown, Eagle and Lion; the Spanish heraldic constellation and its non-causal relations with NAX-10; the Flag of Spain in Synthesis™ and the Flag of Humanity in Synthesis™; criteria for symbolic inclusion without biologising identities or turning diversity into hierarchy; mechanisms preventing authoritarian, imperial, nationalist, racial or commercial capture; Innova_N as a living tool rather than an external representation of a hammer; transformation of memory into an engine of ideas vectorised by joint synthesis; the relation among framework, planet, human life and fractal organism; responsibility of the creative agent integrated into the whole; and criteria for institutional use by the Innova_N Foundation.

Every contribution requires prior reading, genealogy, separation between historical form and archetypal function, traceability, classification, delta and version.

- [Open Synthesis of Manifesto XXXVI · Issue #42](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/42)
- [Previous genealogical annex](../propuestas/sintesis-abierta/ANEXO_CORONA_AGUILA_CUSTODIA_LEGADO_EDAD_DEL_HOMBRE_ES_EN.md)
- [Current operational contribution protocol](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
- [Open Synthesis index](../propuestas/sintesis-abierta/README.md)

**Navigation:** [← XXXV](./35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md) · [Index](./README.md) · [XXXVII · Neofraternity™ →](./37_neofraternidad_ES_EN.md)
'''
text=text[:start]+'## XII. Open Synthesis\n\n'+body.strip()+'\n\n'+text[end:]
p.write_text(text,encoding='utf-8')

print('STRICT_SYMMETRY_34_36=OK')
