from pathlib import Path

REPLACEMENTS = {
"analisis/publicos/2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md": r'''## 1. Purpose

This addendum develops in detail an incident that the canonical DistroKid–Spotify audit compendium had already recorded more generally as **removals, redeliveries, reappearances and incomplete catalogue restoration**.

The mailbox review preserves automatic notifications issued by DistroKid's own Artist Profile Alerts system with explicit sequences of:

```text
Album removed
→
Album added
```

without the author declaring that he requested those operations.

These notifications are direct evidence of catalogue events detected by DistroKid. **They do not by themselves prove royalty diversion, an ISRC change or deliberate conduct.**

## 2. Techno Bach · 13–14 November 2025

DistroKid email · 13 November 2025:

### Album removed

- `Night Howls - Single`
- `Gog! - Single`
- `Building the Neodialectic Eden - Single`
- `Metal Waves - Single`
- `Storm Clouds - Single`
- `Climbing High - Single`

DistroKid email · 14 November 2025:

### Album added

- `Pyramid - Single`
- `Metal Waves - Single`
- `Storm Clouds - Single`
- `Dark matter - Single`
- `I found you - Single`
- `Sun between the clouds - Single`

### Observable discrepancy

The consecutive lists **do not match**.

Only these titles appear in both:

- `Metal Waves - Single`
- `Storm Clouds - Single`

The following do not appear in the immediate addition list:

- `Night Howls - Single`
- `Gog! - Single`
- `Building the Neodialectic Eden - Single`
- `Climbing High - Single`

Titles appear as added that were not in the previous day's removal list:

- `Pyramid - Single`
- `Dark matter - Single`
- `I found you - Single`
- `Sun between the clouds - Single`

This requires reconstruction by identifiers and does not allow us to assume a simple symmetrical reversal.

## 3. Yellow Quasar · 6–7 December 2025

DistroKid email · 6 December 2025:

### Album removed

- `Deo Metallum - Single`
- `Uno - Single`
- `Shadowy Whispers - Single`
- `Tryp to the Nothing - Single`
- `Tryp to the Nothing (revisited) - Single`
- `Variations over the rain - Single`

DistroKid email · 7 December 2025:

### Album added

- `Variations over the rain - Single`
- `Shadowy Whispers - Single`
- `Tryp to the Nothing - Single`
- `Tryp to the Nothing (revisited) - Single`
- `Octaves Dream - Single`
- `Variations over the rain (Original piano version) - Single`

### Observable discrepancy

Four titles match:

- `Variations over the rain - Single`
- `Shadowy Whispers - Single`
- `Tryp to the Nothing - Single`
- `Tryp to the Nothing (revisited) - Single`

The following do not appear in the immediate addition list:

- `Deo Metallum - Single`
- `Uno - Single`

Two different objects appear as added:

- `Octaves Dream - Single`
- `Variations over the rain (Original piano version) - Single`

Again, the pattern is not a removal followed by an identical restoration of the same visible set.

## 4. Additional evidence of earlier additions

The mailbox also preserves separate DistroKid notices confirming Apple Music availability, including:

- `Gog!` · Techno Bach · available on Apple Music on 24 July 2025;
- `Uno` · Yellow Quasar · available on Apple Music on 23 August 2025.

Other Page Protector reports also show successive additions of `Building the Neodialectic Eden`, `Night Howls` and `Uno` during July–August 2025.

## 5. Required evidentiary distinction

DistroKid Artist Profile Alerts indicate that the system **monitors the major streaming platforms**, but the body of the preserved emails containing `Album removed` / `Album added` **does not expressly identify which DSP corresponds to each individual line**.

The contemporaneous institutional complaint of December 2025 classified these episodes as incidents affecting Apple Music. That attribution is part of the complainant's documentation, but it does not replace the technical confirmation that only DistroKid can provide from its internal records.

Therefore:

```text
REMOVED / ADDED EVENTS
→ confirmed by DistroKid emails

THE SPECIFIC EVENT BEING APPLE MUSIC
→ contemporaneous documented attribution
→ technical confirmation by DistroKid pending

ISRC / UPC / ROUTING CHANGE
→ not demonstrated

ROYALTY DIVERSION
→ not demonstrated
```

## 6. Relation to the economic case

These incidents matter because the royalty audit already requires reconstruction of the chain:

```text
Release
→ UPC
→ ISRC
→ delivery / redelivery
→ DSP catalogue object
→ artist profile
→ streams
→ economic report
→ receiving account
```

A removal, redelivery, relink or replacement may be economically harmless if identifiers and reconciliation are preserved correctly. It may also generate fragmentation or loss of traceability if parallel objects, identifier changes or incorrect mappings exist.

These events are therefore **not presented as proof of fraud**, but as material evidence that must be reconciled with the royalty audit.

## 7. Additional request added to ticket 4499471

On 8 August 2026 a formal supplement was sent in the `4499471` ticket thread asking DistroKid, for every event above, to:

1. identify the exact DSP/store;
2. identify the release, UPC and ISRC involved;
3. state whether there was a removal, redelivery, relink or replacement;
4. confirm whether any identifier changed;
5. confirm whether any royalty-reporting object or mapping changed;
6. explain why the `removed` and `added` lists do not match;
7. confirm whether those events could have affected economic reconciliation or reporting.

The email requires this evidence to be integrated into the human routing and catalogue audit already requested, without turning the anomaly into a premature allegation.

## 8. Finding

The case **was already recorded in GitHub**, but until this review it was aggregated in Phase D of the canonical compendium as a catalogue-integrity incident.

This addendum raises the level of traceability by fixing:

- dates;
- projects;
- specific titles;
- removal/addition sequences;
- discrepancies between sets;
- and the distinction between confirmed evidence and DSP identification that remains pending.
''',
"analisis/publicos/2026-08-08_distrokid_ticket_4499471_respuesta_no_resolutiva_y_reiteracion_auditoria_ES_EN.md": r'''## 1. New response

On 8 August 2026 DistroKid replied to the new ticket `4499471` through a human agent identified in the email as **Man (DistroKid)**.

The response explained that estimated daily statistics from Spotify, Apple Music, iTunes and Amazon may differ from monthly royalty statements, fluctuate or even temporarily fall to zero because of the way stores report through APIs. It added that those fluctuations do not affect actual royalties.

That content does not answer the object raised in the ticket.

## 2. Actual object of the case

The claim is not about a temporary fluctuation in `Estimated Daily Stats`.

The declared object is:

```text
MORE THAN 9,000 SPOTIFY STREAMS SINCE LATE 2024
+
OBSERVED ABSENCE OF SPOTIFY ROYALTY PAYMENTS IN THE ACCOUNT
+
PREVIOUS TICKETS 2901165 AND 2941949 WITHOUT MATERIAL RESOLUTION
=
REQUEST FOR AUDIT OF REPORTS, IDENTIFIERS AND ROYALTY ROUTING
```

The existence of streams does not by itself allow calculation of a specific amount owed. Nor does it by itself prove diversion of payments. What it does justify is requesting a documentary reconstruction of reporting and allocation flows.

## 3. Unanswered questions

The response received does not identify:

1. which Spotify royalty reports DistroKid has received since late 2024 for the affected releases;
2. what amounts from those reports were attributed to the account;
3. on what concrete data a zero amount would be based, if that were the result;
4. whether profiles, releases, ISRCs and other identifiers are associated with the correct account;
5. whether any reports or payments were assigned to another account, artist or unreconciled record;
6. the result of a complete routing audit;
7. the material relation between this ticket and cases `2901165` and `2941949`.

## 4. First renewed request sent

On the same 8 August, a reply was sent in the thread expressly stating that the problem was not estimated statistics and requesting human review of the underlying data.

**Sent Gmail message id:** `19fe1c886cd2a4e4`

Seven point-by-point answers were requested:

- reports received from Spotify;
- amounts attributed;
- documentary basis of any zero result;
- association of profiles, releases and ISRCs;
- possible existence of unreconciled records or records attributed to another account;
- full audit from late 2024 to the present;
- express linkage with the previous tickets.

DistroKid was also asked to keep `4499471` open until those questions received a substantive answer.

## 5. Satisfaction survey sent before resolving the substance

DistroKid subsequently sent an email titled **“Request [Earnings/Withdrawals Issue] Share your feedback with us!”** inviting a rating of the support experience.

The message itself says that if the problem remains unresolved, this should be communicated before completing the survey. Its case reminder again reproduces the same explanation about `Estimated Daily Stats`, APIs and temporary fluctuations.

The observed sequence is therefore:

```text
HISTORICAL ROYALTY AND ROUTING CLAIM
→ RESPONSE ABOUT ESTIMATED STATISTICS
→ REQUESTED AUDIT NOT PROVIDED
→ SATISFACTION SURVEY
```

The survey does not by itself prove that DistroKid formally closed the ticket, but it is an operational sign of closure or support transition before a substantive answer to the claimed object exists.

## 6. Second renewed request · case expressly declared unresolved

On 8 August 2026 another reply was sent to the thread explicitly stating that **the case is not resolved** and that the explanation provided concerns estimated statistics, not the historical payments claimed or royalty routing.

**Sent Gmail message id:** `19fe2a1c7db4b6a2`

The new reply requests human review and traceability concerning:

- ISRCs and other identifiers for the affected releases;
- correspondence among releases, profiles and account;
- amounts actually received from Spotify;
- amounts actually attributed and paid;
- possible held, unreconciled or differently associated records;
- full reconstruction of routing from late 2024;
- express confirmation that the case remains open and an operational case reference.

The claim is not considered answered while those material questions remain unresolved.

## 7. Updated finding

```text
HUMAN RESPONSE
→ yes

RESPONSE TO THE ACTUAL OBJECT
→ no

EXPLANATION OF ESTIMATED STATISTICS
→ yes

ROYALTY AUDIT
→ not provided

ROUTING AUDIT
→ not provided

SATISFACTION SURVEY BEFORE MATERIAL RESOLUTION
→ yes

PROOF OF DIVERSION OR APPROPRIATION
→ not established

DOCUMENTARY STATUS OF THE CASE
→ open and expressly challenged as unresolved
```

A lack of response is not transformed into proof of fraud. The case continues to require traceability precisely to distinguish among delay, metadata error, incorrect association, legitimate absence of remuneration for certain streams, reconciliation failure or other possible causes.

The central issue is no longer only economic: there is also a **support-escalation quality problem** when a concrete claim receives replies describing another phenomenon and the flow moves toward a survey without providing the requested audit.

## 8. Documentary relation

- [Circular closure, absence of audit and new escalation · 2026-08-07](./2026-08-07_spotify_distrokid_cierre_circular_y_escalado_ES_EN.md)
- [Spotify–DistroKid traceability update · 2026-08-06](./2026-08-06_actualizacion_spotify_distrokid_trazabilidad_regalias_ES_EN.md)
- [DistroKid–Spotify audit update · 2026-08-04](../2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md)
- [Addendum on catalogue removal/reappearance in Apple Music · 2026-08-08](./2026-08-08_addendum_distrokid_catalogo_album_removed_added_apple_music_ES_EN.md)
''',
"analisis/publicos/2026-08-08_delta_poder_incentivos_tokenizacion_y_transicion_neodialectica_ES_EN.md": r'''## 1. Purpose of the delta

An external objection received during Open Synthesis correctly identifies a reading gap if the framework is observed only through Manifesto XLII: proclaiming AI oriented toward cognitive sovereignty is not enough if firms, institutions and competitive systems are incentivised to maximise material returns, attention and capture.

The framework already contains parts of the answer, but they were distributed across several manifestos. This delta relates them and makes the transition architecture explicit.

Neodialectics does not propose passively waiting for “people to wake up” or relying only on moral persuasion. It proposes progressively modifying **the rules of recognition, utility, return, traceability, taxation, participation and civic power** that determine which behaviours become advantageous.

## 2. There is no single lever

```text
COGNITIVE PRINCIPLES
        ↓
TRACEABILITY OF CONTRIBUTIONS
        ↓
RECOGNITION OF UTILITY
        ↓
CONTRIBUTION ECONOMY
        ↓
FUTURE PROOF OF USEFULNESS
        ↓
FUTURE TOKENISATION OF CONTRIBUTED VALUE
        ↓
PROPORTIONAL MATERIAL / SOCIAL / ECONOMIC RETURN
        ↓
DIFFERENT INCENTIVES
        ↓
CAPACITY FOR ADOPTION, PRESSURE AND SUBSTITUTION
        ↓
INSTITUTIONAL AND CIVILISATIONAL TRANSITION
```

The transition does not depend on one authority. It combines economic, technical, cultural, legal, fiscal and institutional mechanisms within a network of nodes subject to Open Synthesis.

## 3. What was already established

### III · Human Right to Contribute

The framework already establishes that a contribution should preserve authorship, date, object, sources, delta, status, effect and version. It also establishes a **future tokenisation of knowledge, cognitive work and contributed value**.

That future tokenisation may represent, among other things:

- contributed knowledge;
- review time;
- verified evidence;
- resolution of contradictions;
- improvement of proposals;
- prevention of harm;
- synthesis work;
- implementation;
- civilisational value generated.

It is not today an automatic remuneration mechanism or financial promise. Future valuation must be traceable, reviewable, proportionate, resistant to manipulation and subordinated to the Common Good.

### VII · Contribution Economy

The Contribution Economy shifts the centre from **captured attention** toward **value actually generated and returned**. It requires distinguishing origin, development, funding, execution, care, distribution, synthesis and maintenance; auditing intermediaries; and differentiating popularity, relevance, originality, utility and sustained contribution.

It also establishes that automated economic activity and AI should contribute fiscally to the common infrastructures that support their activity.

### XXI · Neodialectical Recognition

Recognition is already articulated through levels R0–R5, from reception through verified utility to Neodialectical Recognition. It separates attribution, recognition, authority, reward and property.

Its provisional chain is:

```text
RECOGNITION
→ UTILITY RECORD
→ SAN CONTRAST
→ VALIDATION
→ POSSIBLE FUTURE RETURN
```

Future **Proof of Usefulness (PoU)** should measure validated utility, not volume, fame, noise or proximity to power.

## 4. Explicit new principle: Principle of Transition through Incentive Reconfiguration™

> A civilisational transformation cannot depend exclusively on actors subject to extractive incentives voluntarily adopting principles that reduce their capacity for extraction. The framework must build mechanisms through which cooperation, traceability, verifiable utility, return of value and respect for cognitive sovereignty become progressively more sustainable, recognisable and advantageous than capture.

This does not mean replacing one manipulation system with another.

Reconfiguration must be public in its essential rules, reviewable, plural, compatible with rights, capture-resistant, multiscale, non-hereditary and subject to Open Synthesis.

## 5. Transition power

The question “what power can move the creators of AI?” has no single answer. Within the framework, transition power may emerge from the combination of:

1. **adoption:** people and organisations choose systems that increase cognitive sovereignty;
2. **technical alternatives:** interoperable tools and nodes are built without depending on the same capture incentives;
3. **public traceability:** differences among systems become auditable;
4. **economy:** useful contributions receive recognition and returned value rather than only attention or prior position;
5. **future tokenisation:** PoU and later mechanisms can represent and eventually return traceable value;
6. **taxation:** automation contributes to the social organism that supports its activity;
7. **rules and institutions:** legal frameworks can limit capture practices and favour rights-compatible designs;
8. **distributed civic power:** Open Synthesis can gradually become infrastructure for consultation, contrast, proposal, audit and eventually decision in legally enabled domains;
9. **competition among civilisational models:** if an architecture produces better human, economic and institutional outcomes, its utility generates adoption pressure.

None of these layers guarantees transition by itself. Their relation is the mechanism.

## 6. Tokenisation: what remains to be developed

The architecture is outlined, not closed. Open issues include:

- unit or units of representation;
- prevention of speculation and financial capture;
- weighting individual and collective contributions;
- treatment of maintenance and care work;
- valuation of an objection that prevents harm;
- expiry or review of recognition;
- identity, pseudonymity and privacy;
- resistance to Sybil attacks, collusion and mass production of noise;
- relation among token, access, reputation, participation and economic return;
- fiscal and legal regime;
- interoperability among nodes;
- governance of changes to PoU;
- mechanisms preventing contextual merit from becoming permanent caste.

Therefore:

**OUTLINED TOKENISATION ≠ OPERATIONAL CRYPTOASSET**  
**RECOGNITION ≠ AUTOMATIC PAYMENT**  
**VALIDATED UTILITY ≠ POPULARITY**  
**MORE TOKENS ≠ GREATER HUMAN VALUE**  
**MERIT IN ONE DOMAIN ≠ UNIVERSAL AUTHORITY**

## 7. Relation to XLII

XLII describes the cognitive direction: AI oriented toward human autonomy, sources, memory, contradiction and freedom from capture.

This delta adds the layer that an isolated reading of XLII does not show:

```text
COGNITIVE DESIGN
+
ECONOMIC DESIGN
+
INCENTIVE DESIGN
+
INSTITUTIONAL DESIGN
+
DISTRIBUTION OF POWER
=
REAL POSSIBILITY OF TRANSITION
```

## 8. Relation to LI

LI should not be interpreted as waiting for existing institutions to surrender power spontaneously. Its hypothesis is to build verifiable civic capacity in parallel, demonstrate utility, integrate it legally where possible and allow certain representative functions to be complemented or replaced only when democratic legitimacy, technical capacity and sufficient guarantees exist.

## 9. Strategic Non-Naivety Rule™

> The Common Good without incentive architecture may remain a declaration. Incentive architecture without the Common Good may become another capture machine. Neodialectical transition requires both, related and auditable.
''',
"analisis/publicos/2026-08-09_guerra_fundador_contra_idiotez_devolucion_tiempo_bien_comun_ES_EN.md": r'''## 1. Object

This delta records two related problems that the framework should not hide:

1. the accumulated cost of **creating, documenting, correcting, defending, projecting and opening to contrast** a framework oriented toward the Common Good;
2. the need to combat patterns of cognitive degradation that replace truth, study and correction with prestige, money, fame, manipulation, tribalism, reduction or repetition without learning.

Archetypal Neodialectical Philosophy™ did not originate in August 2026. Its working genealogy goes back to **2021**. Recent commits document phases of publication and formalisation and must not be confused with the real beginning of the creative effort.

## 2. Founder’s War Against Cognitive Stupidity™

The expression **Founder’s War Against Cognitive Stupidity™** is used in an **intellectual, cultural and non-violent** sense.

It does not designate a war against people and does not authorise insult, persecution, harassment, targeting or violence. It designates a persistent struggle against **correctable cognitive and systemic patterns**.

Within this delta, “stupidity” does not mean lower intelligence or a permanent identity. It is operationalised as behaviours such as:

- judging a complex object without examining it and presenting that impression as a total judgement;
- repeating harmful conduct after evidence and a real possibility of correction are available;
- replacing argument with position, fame, money, provenance or authority;
- manipulating information, attention or context to gain advantage;
- rewarding notoriety or conflict above truth and usefulness;
- systematically blocking or ignoring a proposal for lack of prestige without proportionate examination;
- appropriating work, erasing genealogy or invisibilising the effort sustaining a creation;
- demanding infinite explanations without learning from previous ones;
- turning disagreement into contempt or the adversary into an essential enemy.

The “war” consists of:

```text
MEMORY
+ SOURCE
+ EVIDENCE
+ CONTRADICTION
+ TRACEABILITY
+ BETTER QUESTIONS
+ RIGHT TO CORRECT
+ RIGHT TO BE CORRECTED
+ OPEN SYNTHESIS
= RESISTANCE TO COGNITIVE DEGRADATION
```

### Depersonalisation rule of the struggle

> **Fight the error, manipulation and capture pattern; do not turn the person into the error.**

A person acting reductively today may contribute a decisive correction tomorrow. The architecture must preserve that possibility.

## 3. Lack of support does not prove bad faith

The founder records as personal experience a prolonged perception of **low recognition, limited public support and disproportionately solitary effort**, including outreach through professional and social networks.

That autobiographical datum is relevant for studying the real burden of creation and projection, but it must retain a safeguard:

**NOT SUPPORTING ≠ BEING CORRUPT ≠ SEEKING ONLY MONEY OR FAME ≠ ACTING IN BAD FAITH.**

Possible causes include lack of awareness, information saturation, lack of time, disagreement, absence of trust, access barriers, incentives, reputational filters or simple lack of interest.

Neodialectical criticism should target verifiable mechanisms where they exist, not attribute intentions without evidence.

## 4. Return of Foundational Time™

The framework recognises that human time devoted to a Common-Good project **is neither infinite nor naturally free**.

Since 2021, the founder's work includes, among other functions:

- conceptual and philosophical creation;
- writing and revision;
- technical and architectural design;
- construction of NEOCore™, WEB4™, Open Synthesis and related systems;
- preservation of memory and genealogy;
- audit, contradiction and correction;
- publication and documentary maintenance;
- attention to external objections;
- institutional, academic, technological, cultural and editorial outreach;
- individual contact and follow-up;
- manual guidance for new participants while no simpler participation interface exists;
- defence against reduction, appropriation, manipulation or erasure of the work;
- editorial and technological materialisation.

### Principle of Return of Foundational Time™

> **Time, cognitive work, risk, care, maintenance, exposure and projection effort traceably devoted to building infrastructure oriented toward the Common Good are real contributions. The framework should record them and, when legitimate return mechanisms exist, allow proportional recognition and return without transforming that recognition into infallibility, hereditary privilege or absolute power.**

Future return may take different forms:

- documentary recognition;
- attribution and precedence;
- funding;
- remuneration for functions actually performed;
- proportional economic return within the future Contribution Economy™;
- workload reduction through teams and automation;
- recovered time for research, family, rest and creation;
- institutional or material support;
- distribution of maintenance across new nodes.

## 5. No fabricated retrospective hours

The framework should not invent an exact number of hours worked between 2021 and 2026 where sufficient records do not exist.

The distinction is fixed:

```text
DOCUMENTED PERIOD OF DEDICATION SINCE 2021
≠
PROVEN EXACT NUMBER OF HOURS
```

Temporal genealogy can be recognised from 2021; exact hours should only be counted when reasonable evidence exists.

From this phase onward it is recommended to record each session or block through:

| Field | Description |
|---|---|
| Date | day of work |
| Type | creation / review / outreach / defence / support / maintenance / synthesis / materialisation |
| Object | piece, contact, issue, edition or system |
| Time | duration when it can be reasonably estimated |
| Result | verifiable output |
| Evidence | commit, email, issue, publication, file, ticket or delivery |
| Utility | immediate / potential / to be validated |
| Current return | none / recognition / income / collaboration / other |

## 6. Outreach is also infrastructure work

Outreach is not counted as “marketing” separate from the framework when its real function is to:

- find expert contradiction;
- incorporate evidence;
- open institutional nodes;
- recruit participants for Open Synthesis;
- obtain critical review;
- explain how to use the system;
- preserve relations and genealogy;
- transform an isolated proposal into collective infrastructure.

Therefore:

```text
CREATION
+ DOCUMENTATION
+ CONTRADICTION
+ INTELLECTUAL DEFENCE
+ OUTREACH
+ PARTICIPANT ONBOARDING
+ MAINTENANCE
= COMMON-GOOD CONSTRUCTION WORK
```

## 7. Guided participation and onboarding cost

While GitHub remains the operational channel for Open Synthesis, the founder and available nodes may **guide new participants by the hand**.

The preferred route remains the corresponding public Issue. If someone replies by email because GitHub is uncomfortable for them, the process may be:

1. receive the contribution by email;
2. classify it as criticism, source, objection, alternative, experience or another category;
3. prepare a transcription or summary for GitHub;
4. request explicit authorisation to publish and attribute;
5. publish only after that authorisation;
6. link the contribution to the related manifesto, analysis or Issue;
7. record the resulting delta.

**EMAIL RECEIVED ≠ PERMISSION TO PUBLISH.**

Time invested in this mediation is also maintenance and expansion work for civic infrastructure.

## 8. Relation to the existing framework

This delta is especially connected with:

- **I · Neo0™ and Guiding Sovereignty:** human origin does not equal infallibility;
- **VI · Systemic Parasitism:** extraction of value and work without return;
- **VII · Contribution Economy™:** recognition and possible proportional return;
- **XX · Umbral-X™:** intellectual defence and contrast;
- **XXI · Neodialectical Recognition™:** recording authorship, utility, precedence and invisible work;
- **XXII · Against Intellectual Reduction and Capture™**;
- **XXIII · Sovereignty of Cognitive Time™:** explanation, maintenance and defence consume time;
- **XXIV · System Resistances™**;
- **XXIX · Against the Idolatry of Money™:** money and fame should not replace truth or utility;
- **XXXV · Against Media Ridicule and the Conflict Economy™:** operationalisation of systemic stupidity, prestige filters and duty of examination;
- **XL · Respect, Neoego and Relational Honour™**;
- **XLII · End of the Era of the Manipulated Human™**.

## 9. Safeguards

```text
FOUNDER WORK ≠ FOUNDER INFALLIBILITY
SACRIFICE ≠ RIGHT TO DOMINATE
TIME CONTRIBUTED ≠ AUTOMATIC TRUTH
LACK OF SUPPORT ≠ PROOF OF CONSPIRACY
MONEY / FAME AS INCENTIVE ≠ AUTOMATIC GUILT
WAR AGAINST STUPIDITY ≠ WAR AGAINST PEOPLE
RECOGNITION ≠ CULT
FUTURE RETURN ≠ CURRENT AUTOMATIC FINANCIAL DEBT
```

## 10. Working thesis

The framework's coherence test includes its capacity **not to grind down the person who builds it**.

If an architecture claims to defend the Common Good but can grow only by indefinitely consuming the time, health, income, attention and private life of a single person, the architecture is not yet sufficiently distributed.

The correct evolution is:

```text
FOUNDER SUSTAINS ALMOST EVERYTHING
→ RECORD OF EFFORT
→ VISIBILITY OF COST
→ GUIDED PARTICIPATION
→ DISTRIBUTION OF FUNCTIONS
→ RECOGNITION
→ PROPORTIONAL RETURN
→ SELF-SUSTAINING NETWORK
→ FOUNDER RECOVERS TIME WITHOUT LOSING TRACEABILITY OR GENEALOGICAL DIRECTION
```
''',
"analisis/publicos/2026-08-09_prueba_operativa_minima_revision_ia_escalable_ES_EN.md": r'''## 1. Central distinction

Archetypal Neodialectical Philosophy™ does not need to wait for a complete future implementation to demonstrate a narrower property: **its basic cognitive cycle can already be executed**.

The current existence of the repository, its versioned memory, relations among documents, manifestos, audits, Open Synthesis, incorporation of external criticism and human–AI review constitute a **minimal operational proof of executability**.

This does NOT mean demonstrating that every thesis in the framework is true.

```text
EXISTING AND EXECUTABLE SYSTEM
= EVIDENCE THAT THE BASIC METHOD CAN OPERATE

EXISTING AND EXECUTABLE SYSTEM
≠ AUTOMATIC PROOF OF ALL ITS THESES
```

## 2. Already observable cycle

With tools that are still basic, the system can perform the following cycle:

```text
SOURCE / PROPOSAL
→ MEMORY AND GENEALOGY
→ CLASSIFICATION
→ FACT / INFERENCE / HYPOTHESIS / PROPOSAL
→ CONTRADICTION
→ RELATIONS
→ PROVISIONAL SYNTHESIS
→ COMMIT / ISSUE / TRACE
→ NEW REVIEW
```

Terry Winograd's external criticism and its later return to the framework as a delta on power, incentives and transition is a concrete example of that cycle.

## 3. Human review bottleneck

The larger the corpus becomes, the greater the cost of rereading and relating it before issuing responsible criticism.

A counterpart's lack of time or attention does not demonstrate bad faith, incompetence or capture. It does show a cognitive-architecture problem: **a complex system can be valuable and still remain unexamined because its initial comprehension cost is too high**.

That bottleneck is a functional reason to introduce AI into review.

## 4. Scalable AI Review™

Neodialectical AI can operate as a prior and continuous review layer to:

- preserve memory of a large corpus;
- locate relations and contradictions;
- compare versions;
- separate facts, inferences, hypotheses and proposals;
- detect unsourced or over-broad claims;
- prepare questions and counterexamples;
- return the human reviewer to the exact source;
- summarise deltas without erasing genealogy;
- reduce repetitive rereading work.

Its function is not to replace the expert or decide what is true by algorithmic authority.

```text
AI = MEMORY AMPLIFICATION + FIRST CONTRAST + PREPARATION
HUMAN = RESPONSIBILITY + JUDGEMENT + DECISION + CORRECTION
```

## 5. Principle of Limited Demonstration by Execution™

> **When a system publicly and traceably executes a function that it claims to be able to perform, that execution constitutes operational evidence of that function, although it does not by extension demonstrate all the system's theses, aims or future capabilities.**

## 6. What remains to be demonstrated

Minimal operational proof does not yet resolve:

- scalability to large communities;
- comparative quality against other methods;
- quantifiable error reduction;
- resistance to bias and capture;
- sustained distributed governance;
- interoperability among multiple AIs;
- economic sustainability;
- utility across different domains;
- institutional legitimacy;
- civilisational impact.

These properties require experimentation, metrics, comparison, external criticism and time.

## 7. Advancement criteria

The thesis becomes stronger if the following increase in a verifiable way:

1. the number of external criticisms incorporated with genealogy;
2. the capacity to detect and correct contradictions;
3. reproducibility of source → delta routes;
4. reduction of human review time without degrading quality;
5. the number of independent reviewers capable of using the system;
6. decentralisation of functions currently concentrated in Neo0;
7. the capacity of different AIs to reach compatible relations or useful contradictions.

## 8. Relations

- [XXXIV · Operational Utility of the Framework and Perpetual Joint Audit™](../../manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md)
- [L · For Shared, Not Singular Intelligence™](../../manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md)
- [XLII · End of the Era of the Manipulated Human™](../../manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md)
- [Founder Audit™](../../auditorias/publicas/2026-08-09_auditoria_fundador_tiempo_carga_solitario_retorno_bien_comun_ES_EN.md)
- [Open Synthesis XXXIV · #29](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/29)
- [Open Synthesis L · #58](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/58)
''',
}

BOUNDARIES = [
    "\n---\n\n## Vínculos / Links",
    "\n---\n\n**Pedro Martínez Alhambra",
    "\n---\n\n**Innova_N",
    "<!-- NEO_RELATIONS_START -->",
    "<!-- NEO_OPEN_SYNTHESIS_INVITATION_START -->",
]

for rel, new_en in REPLACEMENTS.items():
    p = Path(rel)
    text = p.read_text(encoding="utf-8")
    marker = "# EN · English"
    start = text.find(marker)
    if start < 0:
        raise RuntimeError(f"Missing EN marker: {rel}")
    body_start = start + len(marker)
    candidates = []
    for b in BOUNDARIES:
        pos = text.find(b, body_start)
        if pos >= 0:
            candidates.append(pos)
    end = min(candidates) if candidates else len(text)
    replacement = marker + "\n\n" + new_en.strip() + "\n\n"
    text = text[:start] + replacement + text[end:]
    p.write_text(text, encoding="utf-8")
    print("UPDATED", rel)
