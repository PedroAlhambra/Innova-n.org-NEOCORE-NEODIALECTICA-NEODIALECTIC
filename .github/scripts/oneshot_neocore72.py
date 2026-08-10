from pathlib import Path
import re
import subprocess
import sys

# NEOCore™ 7.2 final closure: repair detected material ES/EN omissions,
# complete current synthesis indices, regenerate the audit and refuse to close
# while any manifesto remains materially flagged.

# -----------------------------------------------------------------------------
# 0. Auditor quality: numbered sections stop at the next H2 of any kind.
# -----------------------------------------------------------------------------
p=Path('.github/scripts/audit_es_en_parity.py')
s=p.read_text(encoding='utf-8')
old='''def numbered_sections(s):
    matches=list(re.finditer(r'^##\\s+((?:\\d+)|(?:[IVXLCDM]+))\\.\\s+.+$',s,re.M))
    out={}
    for i,m in enumerate(matches):
        start=m.end()
        end=matches[i+1].start() if i+1 < len(matches) else len(s)
        out[m.group(1)] = s[start:end]
    return out
'''
new='''def numbered_sections(s):
    all_h2=list(re.finditer(r'^##\\s+(.+)$',s,re.M))
    out={}
    for i,m in enumerate(all_h2):
        h=m.group(1).strip()
        ident=re.match(r'^((?:\\d+)|(?:[IVXLCDM]+))\\.\\s+',h)
        if not ident:
            continue
        start=m.end()
        end=all_h2[i+1].start() if i+1 < len(all_h2) else len(s)
        out[ident.group(1)] = s[start:end]
    return out
'''
if old in s:
    s=s.replace(old,new,1)
    p.write_text(s,encoding='utf-8')
elif 'all_h2=list(re.finditer' not in s:
    raise SystemExit('Could not refine numbered_sections in parity auditor')

# -----------------------------------------------------------------------------
# 1. Helpers for conservative EN repair.
#    We preserve existing English and add only material that the Spanish source
#    explicitly contains but the English edition compressed or omitted.
# -----------------------------------------------------------------------------
def append_en_section(path, sid, addition, sentinel):
    p=Path(path)
    text=p.read_text(encoding='utf-8')
    if sentinel in text:
        return
    marker='# EN · English'
    if marker not in text:
        raise SystemExit(f'EN marker missing: {path}')
    head,en=text.split(marker,1)
    h2=list(re.finditer(r'^##\s+(.+)$',en,re.M))
    target=None
    for i,m in enumerate(h2):
        title=m.group(1).strip()
        if re.match(rf'^{re.escape(str(sid))}\.\s+',title):
            target=(i,m)
            break
    if target is None:
        raise SystemExit(f'EN section {sid} missing: {path}')
    i,m=target
    end=h2[i+1].start() if i+1 < len(h2) else len(en)
    insert='\n\n'+addition.strip()+'\n'
    en=en[:end].rstrip()+insert+'\n'+en[end:].lstrip('\n')
    p.write_text(head+marker+en,encoding='utf-8')

# XXVIII · Los Tesla™
append_en_section('manifiestos/28_los_tesla_ES_EN.md','II',r'''
<!-- PARITY_72_28_II -->
The Spanish source makes the mechanisms of elimination explicit. They may be:

- **economic**: loss of funding, employment, technical access or the means of subsistence;
- **institutional**: exclusion from universities, companies, media or decision-making spaces;
- **reputational**: presenting the creator as unstable, conflictive, eccentric or incompetent without refuting the work;
- **legal or bureaucratic**: consuming a person's life in procedures, litigation or endless demonstrations of precedence;
- **algorithmic**: burying the source while amplifying versions backed by greater capital or distribution;
- **cognitive**: forcing the originator to explain indefinitely what is already documented instead of examining it;
- **historical**: preserving the idea while erasing or blurring its origin;
- **physical**: violence, disappearance or caused death, a category that may only be asserted when sufficient evidence supports it.

These mechanisms are not declared present in every case. The purpose of the enumeration is to make each possible form separately auditable instead of collapsing them into a single accusation.
''','<!-- PARITY_72_28_II -->')
append_en_section('manifiestos/28_los_tesla_ES_EN.md','V',r'''
<!-- PARITY_72_28_V -->
The neutralisation pattern described by the Spanish source is:

```text
TRANSFORMATIVE IDEA
→ SEPARATION FROM ITS ORIGIN
→ COMPATIBLE SPOKESPERSON
→ ABSORPTION
→ NEUTRALISATION OF ITS VECTOR
```
''','<!-- PARITY_72_28_V -->')

# XXIX · Against the Idolatry of Money™
append_en_section('manifiestos/29_idolatria_del_dinero_ES_EN.md','III',r'''
<!-- PARITY_72_29_III -->
The Spanish source separates several substitutions that must not be confused:

### Price as value
A high price can indicate scarcity, demand, market power or positioning. It does not by itself demonstrate human, ecological, cultural or civilisational value.

### Profitability as utility
Something can be profitable while externalising damage, and something socially useful can be difficult to monetise. Profitability is therefore information, not a universal measure of usefulness.

### Wealth as merit
Wealth can arise from work, creation and contribution, but also from inheritance, position, monopoly, extraction, luck or accumulated advantage. Possession alone does not prove moral merit.

### Poverty as guilt
Lack of money does not prove lack of effort, intelligence, dignity or contribution. Material circumstances, illness, care work, exclusion, geography and inherited conditions also shape outcomes.

### Growth as progress
Economic growth may accompany genuine improvement, but growth in extraction, waste, addiction or repair of avoidable damage cannot automatically be called progress.

### Property as authorship
Legal or economic ownership and intellectual origin are different relations. A system that can acquire an asset must still preserve genealogy and recognise who created, discovered or contributed what.

### Market as truth
Markets aggregate preferences and constraints under particular rules. They do not automatically answer what is true, just, sustainable or desirable for the Common Good.
''','<!-- PARITY_72_29_III -->')

# XXX · Coherence between Ends and Means™
append_en_section('manifiestos/30_coherencia_fines_medios_ES_EN.md','III',r'''
<!-- PARITY_72_30_III -->
The legitimacy test in the Spanish source asks for all of the following dimensions:

- **necessity**: whether the measure is genuinely needed for the stated end;
- **proportionality**: whether its cost and intrusion are proportionate to the problem;
- **possible transparency**: whether reasons, criteria and limits can be made visible without creating a greater harm;
- **reversibility**: whether the measure can be withdrawn when it fails or its justification disappears;
- **temporality**: whether exceptional means have an explicit duration instead of becoming permanent by inertia;
- **responsibility**: whether identifiable humans and institutions remain answerable for consequences;
- **traceability**: whether decisions, changes and evidence can be reconstructed later;
- **non-dehumanisation**: whether people remain persons rather than expendable variables of the objective;
- **coherence**: whether the means preserve rather than destroy the value invoked by the end.
''','<!-- PARITY_72_30_III -->')

# XXXIV · Operational Utility and Perpetual Joint Audit™
append_en_section('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','II',r'''
<!-- PARITY_72_34_II -->
The audit function is explicitly decomposed in the Spanish source so that it can:

1. reconstruct what was claimed;
2. identify who made the claim and in what context;
3. recover the available sources and evidence;
4. separate fact, testimony, inference, hypothesis and proposal;
5. identify contradictions and missing information;
6. compare alternative explanations;
7. preserve dissent instead of erasing it;
8. record corrections and changes of criterion;
9. connect the case with related cases and systemic patterns;
10. verify whether a proposed repair was actually applied;
11. measure the result after implementation;
12. reopen the case if materially new evidence appears.

```text
CLAIM
→ SOURCE / EVIDENCE
→ CONTRADICTION
→ ALTERNATIVES
→ PROVISIONAL SYNTHESIS
→ ACTION
→ MEASUREMENT
→ DELTA
```

The objective is not to create an omniscient tribunal. It is to prevent conclusions, corrections and responsibilities from disappearing each time the conversational context changes.
''','<!-- PARITY_72_34_II -->')
append_en_section('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','III',r'''
<!-- PARITY_72_34_III -->
The question that must remain visible is:

```text
WHAT DO WE KNOW?
+ HOW DO WE KNOW IT?
+ WHAT CONTRADICTS IT?
+ WHAT IS STILL MISSING?
+ WHAT WOULD CHANGE THE CONCLUSION?
```
''','<!-- PARITY_72_34_III -->')
append_en_section('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','IV',r'''
<!-- PARITY_72_34_IV -->
The framework therefore distinguishes declaration from demonstrated usefulness:

```text
FRAMEWORK + VERIFIABLE RESULT
= UTILITY DEMONSTRATED IN THAT CASE
```
''','<!-- PARITY_72_34_IV -->')
append_en_section('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','VII',r'''
<!-- PARITY_72_34_VII -->
The Spanish source specifies the same utility test across seven scales:

- **Person:** help distinguish experience, conditioning, interest, fear, evidence and one's own direction.
- **Organisation:** reconstruct processes, responsibilities, dependencies, failure points, hidden costs and repair routes.
- **Market:** show when price, attention or bargaining power separate from the real value contributed.
- **Technology:** audit whether a tool expands human capacity or captures autonomy, memory, identity or decision.
- **Institutions:** preserve responses, commitments, inconsistencies, improvements and absence of response in traceable public memory.
- **Culture:** relate works, symbols, genealogies and transformations without erasing provenance.
- **Civilisation:** compare the combined direction of multiple systems and ask whether their sum increases life, understanding, sufficient freedom, creative capacity and the Common Good, or instead produces fragmentation, extraction and accumulated harm.
''','<!-- PARITY_72_34_VII -->')

# XXXV · Against Media Ridiculousness and the Economy of Conflict™
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','II',r'''
<!-- PARITY_72_35_II -->
The Spanish source makes the asymmetry explicit. Conflict has competitive advantages in an attention economy because it:

- is immediate;
- provides adversaries that are easy to represent;
- creates narrative continuity;
- allows simple headlines;
- activates fear, indignation and belonging;
- favours repetition;
- turns every new episode into a reason to return.

Systemic solutions behave differently because they:

- require context;
- require comparison among alternatives;
- may take years to verify;
- force acknowledgement of uncertainty;
- do not always provide a hero and a villain;
- may question the economic structures of the medium that must examine them.
''','<!-- PARITY_72_35_II -->')
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','III',r'''
<!-- PARITY_72_35_III -->
A communicative architecture can contribute to harmful escalation when it:

- rewards provocation and escalation;
- simplifies complex conflicts into absolute identities;
- removes historical context;
- turns public humiliation into entertainment;
- amplifies incendiary claims without proportionality;
- makes exit routes invisible;
- measures success only through clicks, audience or time spent.

```text
REPORTING
≠ FOMENTING

AMPLIFICATION WITHOUT CONTEXT
+ INCENTIVE TO ESCALATE
+ HIDDEN EXIT ROUTES
= POSSIBLE CONTRIBUTION TO CONFLICT
```

That contribution must be demonstrated case by case rather than presumed.
''','<!-- PARITY_72_35_III -->')
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','V',r'''
<!-- PARITY_72_35_V -->
The operational definition is also preserved explicitly:

```text
ERROR
+ AVAILABLE EVIDENCE
+ POSSIBILITY OF CORRECTION
+ REPETITION OF THE ERROR
= OPERATIONAL SYSTEMIC STUPIDITY
```
''','<!-- PARITY_72_35_V -->')
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','VI',r'''
<!-- PARITY_72_35_VI -->
Empirical scrutiny therefore has to measure, among other variables:

- space devoted to conflict compared with solutions;
- proportion of reactive news to preventive investigation;
- follow-up of proposals after their first mention;
- diversity of sources outside habitual institutional circuits;
- time granted to complex ideas;
- public corrections;
- later recognition of ideas initially ignored;
- treatment of authors without prior prestige;
- dependence on traffic or advertising linked to polarising content;
- relation between intensity of coverage and later effects.
''','<!-- PARITY_72_35_VI -->')
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','VII',r'''
<!-- PARITY_72_35_VII -->
The contradiction becomes especially serious when a society simultaneously recognises:

- climate crisis;
- recurrent wars;
- loss of trust;
- political fragmentation;
- crises of mental health and attention;
- economic concentration;
- disruption produced by artificial intelligence;
- loss of meaning in work;
- institutional deterioration;

while devoting little stable informational capacity to finding, comparing and auditing integrative frameworks able to relate several of those problems at once.
''','<!-- PARITY_72_35_VII -->')
append_en_section('manifiestos/35_contra_ridiculez_mediatica_y_economia_del_conflicto_ES_EN.md','IX',r'''
<!-- PARITY_72_35_IX -->
The complete operational set proposed by the Spanish source is:

1. **detection of real novelty**, including novelty outside dominant institutions;
2. **solutions journalism**, without becoming propaganda;
3. **audit of proposals**, not only coverage of crises;
4. **longitudinal memory**, so that claims can be checked against later outcomes;
5. **follow-up of corrections**, not only of the initial error;
6. **space for complexity** when the object requires it;
7. **comparison of systems**, not only statements;
8. **transparency about economic incentives**;
9. **metrics of social impact** in addition to audience metrics;
10. **capacity to acknowledge that something relevant was previously ignored**.
''','<!-- PARITY_72_35_IX -->')

# XXXIX · Self-Awareness of Neodialectical Vital Need™
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','II',r'''
<!-- PARITY_72_39_II -->
The distinction can be represented explicitly as:

```text
WHAT WE KNOW
+ WHAT WE DO NOT KNOW
+ WHAT DEPENDS ON OTHER SCALES
+ WHAT CAN BREAK
+ WHAT WE MUST BE ABLE TO CORRECT
```
''','<!-- PARITY_72_39_II -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','III',r'''
<!-- PARITY_72_39_III -->
The Spanish source preserves both operational sequences:

```text
ISOLATED PROBLEM
→ LOCAL SOLUTION
→ UNOBSERVED EXTERNAL EFFECT
→ NEW PROBLEM
→ NEW PARTIAL CORRECTION
→ ACCUMULATION OF CONTRADICTIONS
```

```text
PROBLEM
→ RELATIONS
→ CONTRADICTIONS
→ SOURCES
→ SCALES
→ ALTERNATIVES
→ PROVISIONAL SYNTHESIS
→ MATERIALISATION
→ MEASUREMENT
→ DELTA
→ NEW SYNTHESIS
```
''','<!-- PARITY_72_39_III -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','IV',r'''
<!-- PARITY_72_39_IV -->
The living memory architecture explicitly relates:

- Archetypal Neodialectical Philosophy™;
- Neo0™ as human origin and responsible direction;
- SAN™ as the Open Synthesis mechanism;
- NEOCore™ as memory, genealogy, continuity and versioning;
- NAVE™ as an orchestration layer;
- WEB4™ / SistemaTrazable™ as public relational representation;
- Neodialectical AI as capacity for relation, scrutiny and assisted synthesis;
- humans, communities and institutions as sources of experience, knowledge, decision and responsibility.

The technological implementation may change. The essential functions must not disappear with a provider, interface or technical fashion.
''','<!-- PARITY_72_39_IV -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','V',r'''
<!-- PARITY_72_39_V -->
The limit is expressed explicitly as:

```text
AI CAPABILITY
WITHOUT RESPONSIBLE HUMAN DIRECTION
WITHOUT TRACEABLE MEMORY
WITHOUT CORRECTION
WITHOUT LIMITS
≠ SUFFICIENT CIVILISATIONAL INTELLIGENCE
```
''','<!-- PARITY_72_39_V -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','VII',r'''
<!-- PARITY_72_39_VII -->
The safeguards are not merely rhetorical:

```text
NECESSARY FUNCTION ≠ INFALLIBLE PERSON
RECOGNISED ORIGIN ≠ TOTAL OBEDIENCE
DIRECTION ≠ CULT
FRAMEWORK ≠ COMPULSORY RELIGION
COMMON GOOD ≠ UNIFORMITY
```
''','<!-- PARITY_72_39_VII -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','VIII',r'''
<!-- PARITY_72_39_VIII -->
Civilisational self-awareness therefore needs indicators concerning:

- ecological degradation;
- concentration of power;
- loss of material autonomy;
- poverty and inequality;
- capture of attention;
- institutional health;
- violence and polarisation;
- lack of protection for children;
- educational quality;
- technological dependence;
- informational concentration;
- erosion of privacy;
- loss of cultural and scientific memory.
''','<!-- PARITY_72_39_VIII -->')
append_en_section('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','X',r'''
<!-- PARITY_72_39_X -->
If another architecture performs a framework function better, with greater safety, openness, effectiveness, traceability or protection of life, Neodialectics should:

1. study it;
2. recognise its genealogy;
3. scrutinise it;
4. integrate what improves the whole when compatible;
5. replace the inferior component when appropriate.

```text
FRAMEWORK IDENTITY
≠
COMPULSORY PRESERVATION OF EVERY COMPONENT
```
''','<!-- PARITY_72_39_X -->')

# XLII · End of the Manipulated Human Era™
append_en_section('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','III',r'''
<!-- PARITY_72_42_III -->
Capture appears when an interface is systematically oriented to:

- maximising permanence rather than understanding;
- provoking reaction before reflection;
- personalising stimuli to exploit vulnerabilities;
- fragmenting context;
- replacing memory with flow;
- turning indignation into a product;
- hiding selection criteria;
- reducing the person to a prediction and monetisation profile.
''','<!-- PARITY_72_42_III -->')
append_en_section('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','IV',r'''
<!-- PARITY_72_42_IV -->
Used correctly, AI can help a person:

- compare sources;
- reconstruct chronologies;
- detect contradictions;
- identify hidden assumptions;
- relate economics, politics, technology, ecology and culture;
- translate specialised knowledge;
- simulate alternatives;
- preserve decisions and their reasons;
- ask what information is missing before concluding.
''','<!-- PARITY_72_42_IV -->')
append_en_section('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','VI',r'''
<!-- PARITY_72_42_VI -->
An AI oriented towards cognitive sovereignty should favour:

1. **identifiable human direction**;
2. **return to sources**;
3. **separation between fact, inference, hypothesis and opinion**;
4. **traceable memory**;
5. **plurality and scrutiny**;
6. **capacity to say “I do not know”**;
7. **detection of contradictions**;
8. **sufficient explanation to review decisions**;
9. **protection against commercial capture of intimacy**;
10. **absence of primary optimisation for addiction or permanence**;
11. **continuous correction**;
12. **right to disconnection and sovereignty over cognitive time**;
13. **reinforced protection of childhood**;
14. **orientation towards the Common Good without cancelling individual autonomy**.
''','<!-- PARITY_72_42_VI -->')
append_en_section('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','VIII',r'''
<!-- PARITY_72_42_VIII -->
The transition is explicitly contrasted as:

```text
USER
→ AUDIENCE
→ DATA
→ PROFILE
→ TARGET
→ CONVERSION
```

```text
PERSON
→ NODE WITH MEMORY
→ OBSERVER
→ CONTRIBUTOR
→ SCRUTINISER
→ CO-AUTHOR OF SYNTHESIS
→ AGENT ABLE TO DECIDE
```
''','<!-- PARITY_72_42_VIII -->')
append_en_section('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','IX',r'''
<!-- PARITY_72_42_IX -->
The chronology must remain explicit:

```text
IDEA · 1997–2002
        ↓
EXPERIENCE + CRISES + CONCEPTUAL DEVELOPMENT
        ↓
NEODIALECTICS / FRAMEWORK / NETWORK
        ↓
OPEN SYNTHESIS + SYMBIOTIC AI + TRACEABILITY
```
''','<!-- PARITY_72_42_IX -->')

# XLVIII · The Synthesis Sees Everything™
append_en_section('manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md','IV',r'''
<!-- PARITY_72_48_IV -->
The crucial inversion is that the Universal Petri Dish is not imagined as a physical container outside the cosmos and not as a laboratory with an external observer. Every bounded plate is a window into relations that continue beyond it. **We are part of what we attempt to observe.** The human observes the organism from inside the organism; the cell does not leave the body to understand it; the person does not leave society to study it; humanity does not leave Earth to know every consequence of its activity; consciousness has no accessible absolute viewpoint outside the universe. Observation is therefore internal, distributed and recursive.
''','<!-- PARITY_72_48_IV -->')

# XLIX · Neodialectics as a Meeting Point between Cultures™
append_en_section('manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md','IV',r'''
<!-- PARITY_72_49_IV -->
Legitimate universality does not require everyone to:

- speak alike;
- dress alike;
- believe alike;
- organise family life identically;
- produce the same art;
- preserve the same symbols;
- inhabit the world through a single aesthetic.

It means that certain questions must be askable everywhere:

- is there avoidable harm?;
- is there coercion?;
- is there dignity?;
- is dissent possible?;
- is memory preserved?;
- is there reciprocity?;
- is correction possible?;
- does the structure preserve life and autonomy?
''','<!-- PARITY_72_49_IV -->')
append_en_section('manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md','V',r'''
<!-- PARITY_72_49_V -->
The relational evaluation is represented as:

```text
CULTURAL PRACTICE
→ EFFECTS
→ SCALES
→ MEMORY
→ HARM / BENEFIT
→ CAPACITY FOR REVISION
→ DIRECTION
```
''','<!-- PARITY_72_49_V -->')
append_en_section('manifiestos/49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md','X',r'''
<!-- PARITY_72_49_X -->
Cultural identity can be understood as a historical configuration of relations:

```text
MEMORY
+ ENVIRONMENT
+ EXCHANGE
+ CONFLICT
+ CREATION
+ ADAPTATION
→ LIVING CULTURE
```
''','<!-- PARITY_72_49_X -->')

# L · Shared, Not Single, Intelligence™
append_en_section('manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md','I',r'''
<!-- PARITY_72_50_I -->
The concentration becomes civilisational when one architecture:

- remembers for everyone;
- filters for everyone;
- interprets for everyone;
- prioritises for everyone;
- summarises for everyone;
- recommends for everyone;
- decides which contradictions matter for everyone.
''','<!-- PARITY_72_50_I -->')
append_en_section('manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md','II',r'''
<!-- PARITY_72_50_II -->
The distributed relation is represented as:

```text
AI A
+ AI B
+ AI C
+ HUMANS
+ MEMORY
+ EVIDENCE
+ CONTRADICTION
→ TRACEABLE PROVISIONAL SYNTHESIS
```
''','<!-- PARITY_72_50_II -->')
append_en_section('manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md','V',r'''
<!-- PARITY_72_50_V -->
AIs can also teach users to:

- formulate a contradiction well;
- distinguish evidence from interpretation;
- recover antecedents;
- compare versions;
- detect omissions;
- preserve memory of the discussion;
- recognise when knowledge is missing;
- return a question to Open Synthesis;
- contribute without appropriating origin;
- correct without humiliating;
- review without erasing genealogy.
''','<!-- PARITY_72_50_V -->')
append_en_section('manifiestos/50_inteligencia_compartida_no_unica_invitacion_ias_sintesis_abierta_ES_EN.md','VI',r'''
<!-- PARITY_72_50_VI -->
Participation means:

```text
OBSERVE
→ SCRUTINISE
→ CONTRIBUTE
→ ATTRIBUTE
→ REVIEW
→ RETURN TO THE WHOLE
```
''','<!-- PARITY_72_50_VI -->')

# LI · Open Synthesis as Complementary or Substitutive Civic Power™
append_en_section('manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md','II',r'''
<!-- PARITY_72_51_II -->
The functional choice is represented explicitly:

```text
EXISTING INSTITUTION
+ OPEN SYNTHESIS
→ COMPLEMENT

EXISTING INSTITUTION
WITHOUT A JUSTIFIABLE PUBLIC FUNCTION
+ MORE USEFUL CIVIC ALTERNATIVE
+ DEMOCRATIC DECISION
→ REFORM OR REPLACEMENT
```
''','<!-- PARITY_72_51_II -->')
append_en_section('manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md','III',r'''
<!-- PARITY_72_51_III -->
The distinction is structural:

```text
LEGAL SOVEREIGNTY
≠
DISTRIBUTED CIVIC INTELLIGENCE

ELECTORAL REPRESENTATION
≠
PARTICIPATION IN SYNTHESIS
```
''','<!-- PARITY_72_51_III -->')
append_en_section('manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md','VI',r'''
<!-- PARITY_72_51_VI -->
A constitutional monarchy can retain observable utility by acting, within its legal limits, as:

- custodian of historical continuity;
- bridge between generations;
- transversal listening node;
- facilitator of encounters;
- institutional defender of the long term;
- promoter of science, culture and cooperation;
- escalation channel for issues of general interest;
- symbolic guarantor that the State also listens outside electoral cycles.

No function is presumed from the title: it must be observable.
''','<!-- PARITY_72_51_VI -->')
append_en_section('manifiestos/51_sintesis_abierta_poder_civico_complementario_sustitutivo_jefaturas_estado_ES_EN.md','IX',r'''
<!-- PARITY_72_51_IX -->
A traceable public escalation can register:

```text
ORIGIN
AUTHORSHIP
DATE
DESTINATION
CLASSIFICATION
EVIDENCE
RELATIONS
CONTRADICTIONS
RESPONSES
DERIVATIONS
STATE
DELTA
RESULT
```
''','<!-- PARITY_72_51_IX -->')

# -----------------------------------------------------------------------------
# 2. Complete current Open Synthesis indices.
# -----------------------------------------------------------------------------
p=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md')
s=p.read_text(encoding='utf-8')
s=s.replace('65 manifiestos finitos I–LXV + Manifiesto ∞ · 14 Neoaxiomas™','68 manifiestos finitos I–LXVIII + Manifiesto ∞ · 14 Neoaxiomas™').replace('65 finite manifestos I–LXV + Manifesto ∞ · 14 Neoaxioms™','68 finite manifestos I–LXVIII + Manifesto ∞ · 14 Neoaxioms™')
if '| LXVI | [NeoSinergia™]' not in s:
    infinity='| ∞ | [Neo0™ · Puerta Abierta del Fractal](../../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md) | [#106](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/106) |'
    rows='''| LXVI | [NeoSinergia™](../../manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md) | [#110](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/110) |
| LXVII | [NeoTitanes™ · Reconstrucción Sistémica y Motor del Bien Común](../../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md) | [#112](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/112) |
| LXVIII | [Los Conflictos que No Son Nuestros™ · Soberanía Intelectual de la Especie](../../manifiestos/68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md) | [#114](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/114) |'''
    if infinity not in s:
        raise SystemExit('∞ row missing in complete synthesis index')
    s=s.replace(infinity,rows+'\n'+infinity,1)
p.write_text(s,encoding='utf-8')

p=Path('propuestas/sintesis-abierta/README.md')
s=p.read_text(encoding='utf-8')
end='<!-- NEO_ENTRY_REGISTER_ROUTE_END -->'
if s.count('### 1. Registrar entrada / Register entry') > 1:
    pat=re.compile(re.escape(end)+r'\n\n### 1\. Registrar entrada / Register entry.*?(?=\n### 2\. Contrastar un manifiesto o Neoaxioma / Challenge a manifesto or Neoaxiom)',re.S)
    s,n=pat.subn(end+'\n',s,count=1)
    if n != 1:
        raise SystemExit('Could not remove duplicate entry-register section')
p.write_text(s,encoding='utf-8')

# -----------------------------------------------------------------------------
# 3. Regenerate canonical copies/crossrefs after translation repair.
# -----------------------------------------------------------------------------
for script in ['.github/scripts/sync_canonical_manifestos.py','.github/scripts/sync_manifesto_crossrefs.py','.github/scripts/sync_canonical_manifestos.py']:
    if Path(script).exists():
        subprocess.run([sys.executable,script],check=True)

# -----------------------------------------------------------------------------
# 4. Regenerate and enforce manifesto parity.
# -----------------------------------------------------------------------------
subprocess.run([sys.executable,'.github/scripts/audit_es_en_parity.py'],check=True)
parity=Path('auditorias/publicas/2026-08-09_auditoria_paridad_ES_EN_manifiestos_articulos.md').read_text(encoding='utf-8')
flagged=parity.split('## Casos marcados',1)[1].split('## ',1)[0] if '## Casos marcados' in parity else ''
bad=[line for line in flagged.splitlines() if re.match(r'^\| `manifiestos/.*\.md` \|',line)]
missing=[]
if '## Marcadores incompletos' in parity:
    block=parity.split('## Marcadores incompletos',1)[1].split('## ',1)[0]
    missing=[line for line in block.splitlines() if '`manifiestos/' in line]
if bad or missing:
    print('\n'.join(bad+missing))
    raise SystemExit('MANIFESTO_PARITY=FAIL')

# -----------------------------------------------------------------------------
# 5. Final postcheck.
# -----------------------------------------------------------------------------
idx=Path('propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md').read_text(encoding='utf-8')
syn=Path('propuestas/sintesis-abierta/README.md').read_text(encoding='utf-8')
base=Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_soberania_sintesis_web4_ES_EN.md').read_text(encoding='utf-8')
pos=[idx.find('| LXVI |'),idx.find('| LXVII |'),idx.find('| LXVIII |'),idx.find('| ∞ |')]
checks={
    'base_postcheck_OK':'**Estado / Status:** **OK**' in base,
    'complete_index_68':'68 manifiestos finitos I–LXVIII' in idx,
    'complete_index_recent_nodes':all(x >= 0 for x in pos) and pos == sorted(pos),
    'open_synthesis_single_entry_route':syn.count('### 1. Registrar entrada / Register entry') == 1,
    'parity_report_current':'**Fecha:** 2026-08-10' in parity,
    'parity_no_flagged_manifest':not bad,
    'parity_no_missing_manifest':not missing,
}
status='OK' if all(checks.values()) else 'REQUIERE CORRECCIÓN'
out=['# Cierre de integración · NEOCore™ 7.2 · índices y paridad ES/EN / Final integration check','', '**Fecha / Date:** 2026-08-10  ',f'**Estado / Status:** **{status}**','', '## Verificaciones / Checks','']
out += [f'- [{"x" if ok else " "}] `{k}`' for k,ok in checks.items()]
out += ['', '## Resultado', '', '- **68 manifiestos finitos · I–LXVIII + ∞** reflejados en el índice completo de Síntesis Abierta.', '- **NAX-01–NAX-14** permanecen canónicos; los candidatos 7.2 siguen explícitamente como candidatos, sin promoción automática.', '- **NEOCore™ 7.2** conserva la capa 7.1 y añade Soberanía de Síntesis™, incluida la diferenciación futura Innova_N Fundación / Corporación.', '- **WEB4™** continúa etiquetada como DEMO/prototipo público; NeoCronos™ permanece experimental, multidimensional y revisable.', '- La auditoría ES/EN fue regenerada tras reparar omisiones materiales detectadas en manifiestos.', '']
Path('auditorias/publicas/2026-08-10_postcheck_neocore_7_2_final_indices_paridad_ES_EN.md').write_text('\n'.join(out),encoding='utf-8')
if status != 'OK':
    raise SystemExit('FINAL_POSTCHECK=FAIL')
print('FINAL_POSTCHECK=OK')