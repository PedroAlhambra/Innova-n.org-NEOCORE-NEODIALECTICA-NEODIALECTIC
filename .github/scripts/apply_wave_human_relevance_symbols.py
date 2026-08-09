from pathlib import Path
import re, sys

ROOT=Path('.').resolve()
REPO='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'

NEO=ROOT/'neoaxiomas/README.md'
M36=ROOT/'manifiestos/36_corona_aguila_custodia_edad_del_hombre_ES_EN.md'
MIDX=ROOT/'manifiestos/README.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
ROOTREADME=ROOT/'README.md'
WIKI=ROOT/'wiki-source/Manifiestos.md'
POST=ROOT/'.github/scripts/postcheck_neocore_71_integridad_relacional.py'
M59=ROOT/'manifiestos/59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md'
M60=ROOT/'manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md'

for p in [NEO,M36,MIDX,SYN,REL,ROOTREADME,WIKI,POST,M59,M60]:
    if not p.exists(): raise SystemExit(f'missing {p.relative_to(ROOT)}')

# ---------------------------------------------------------------------------
# 1. NAX-10: additive symbolic expansion. Do not change other Neoaxioms.
# ---------------------------------------------------------------------------
t=NEO.read_text(encoding='utf-8')
es_pat=re.compile(r'## NAX-10 · Gramática Arquetípica de Custodia™\n.*?(?=\n---\n\n## NAX-11 ·)',re.S)
en_pat=re.compile(r'## NAX-10 · Archetypal Grammar of Custodianship™\n.*?(?=\n## NAX-11 ·)',re.S)
es_new='''## NAX-10 · Gramática Arquetípica de Custodia™ — Águila, Corona, Tierra, Torre, Piedra y León

La arquitectura simbólica relaciona **seis figuras nucleares** y mantiene abierta una constelación histórica adicional cuando un símbolo conserve una función útil sin imponer su forma política originaria:

- **Águila™** → visión de conjunto, altura cognitiva y perspectiva;
- **Corona™** → responsabilidad de gobierno y custodia, no privilegio automático;
- **Tierra™ / Mundo™** → límite material, biosfera, comunidad y realidad compartida;
- **Torre™ / Castillo™** → estructura, vigilancia, continuidad, refugio y defensa;
- **Piedra™** → fundamento, memoria, resistencia, construcción y pulido;
- **León™** → coraje, dignidad, fuerza protectora y capacidad de sostener una posición sin convertir la fuerza en depredación.

Su lectura conjunta queda ampliada:

> **Ver alto · asumir responsabilidad · permanecer anclado a la Tierra · proteger la estructura · construir sobre piedra · sostener con valor aquello que debe ser custodiado.**

### Constelación histórica abierta

La gramática no pretende borrar símbolos porque hayan pertenecido a órdenes anteriores. Puede recuperar su función, conservar su genealogía y someterlos a SAN™.

En el **escudo oficial de España**, regulado por la Ley 33/1981, aparecen el castillo de Castilla, el león de León, los cuatro palos de Aragón, las cadenas de Navarra, la granada, las Columnas de Hércules, coronas y las lises del escusón dinástico. El águila no forma parte del escudo vigente, aunque el Águila de San Juan sí estuvo presente en modelos históricos anteriores al de 1981. Esta coincidencia parcial se registra como relación histórica y simbólica, **no como prueba de que la gramática neodialéctica derive del escudo español**.

- **Columnas / Umbral™** → límite, tránsito, apertura y responsabilidad ante lo que existe más allá del marco conocido;
- **Cadenas / Vínculo™** → interdependencia, compromiso y también memoria de aquello de lo que una sociedad necesita liberarse;
- **Granada / Fruto plural™** → pluralidad contenida, fecundidad y unidad compuesta;
- **Franjas / Continuidad territorial™** → memoria de capas históricas que permanecen distinguibles dentro de una composición mayor;
- **Lis / Genealogía dinástica™** → memoria de filiación histórica sin convertir filiación en privilegio automático;
- **Orbe y cruz históricos** → memoria de cosmologías y tradiciones religiosas europeas, sometidas al mismo principio de no monopolio simbólico.

No todos estos símbolos deben convertirse automáticamente en emblemas centrales. Su estatus permanece abierto a Síntesis Abierta.

### Principio de Bandera de Síntesis™

Una futura bandera neodialéctica de España o una **Bandera de la Humanidad en Síntesis™** no debe nacer destruyendo banderas anteriores. Puede estudiarse como composición de capas actuales, históricas y culturales: española constitucional, tradiciones históricas rojigualdas y rojiblancas cuando proceda, europea, neodialéctica, herencias judías/hebreas, árabes e islámicas, cristianas, laicas, regionales, migrantes, diversidad sexual y de género y otras memorias que la propia SAN™ detecte como ausentes.

La inclusión de una memoria **no equivale a adhesión a todos sus dogmas**, ni permite clasificar a grupos humanos como biológicamente puros, impuros o degradados. La función de la bandera de síntesis sería representar convivencia, memoria y posibilidad de recomposición sin expulsión.

Cualquier diseño de este tipo es por ahora **propuesta simbólica abierta**, no bandera oficial del Estado ni sustitución unilateral de símbolos constitucionales vigentes.

Este Neoaxioma no convierte los símbolos en autoridad por sí mismos. Los utiliza como **gramática arquetípica de responsabilidades, memoria y reconciliación histórica**.

**Estado:** ACTIVADO COMO AXIOMA SIMBÓLICO · AMPLIADO CON LEÓN Y CONSTELACIÓN ABIERTA · ABIERTO A SÍNTESIS.
**Síntesis Abierta específica:** [#93](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/93) · [Matriz general / General matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80)
'''
en_new='''## NAX-10 · Archetypal Grammar of Custodianship™ — Eagle, Crown, Earth, Tower, Stone and Lion

The symbolic architecture relates **six core figures** while keeping an additional historical constellation open whenever a symbol retains a useful function without imposing its original political form:

- **Eagle™** → overview, cognitive height and perspective;
- **Crown™** → responsibility for governance and custodianship, not automatic privilege;
- **Earth™ / World™** → material limit, biosphere, community and shared reality;
- **Tower™ / Castle™** → structure, vigilance, continuity, refuge and defence;
- **Stone™** → foundation, memory, resistance, construction and refinement;
- **Lion™** → courage, dignity, protective strength and the capacity to hold a position without turning strength into predation.

Their expanded joint reading is:

> **See high · assume responsibility · remain grounded in Earth · protect the structure · build on stone · sustain with courage what must be kept.**

### Open historical constellation

The grammar does not seek to erase symbols because they belonged to previous orders. It may recover function, preserve genealogy and submit them to SAN™.

Spain's **official coat of arms**, regulated by Law 33/1981, contains the castle of Castile, the lion of León, the four pales of Aragon, the chains of Navarre, the pomegranate, the Pillars of Hercules, crowns and the fleurs-de-lis of the dynastic inescutcheon. The eagle is not part of the current coat of arms, although the Eagle of Saint John appeared in historical models preceding the 1981 design. This partial overlap is recorded as a historical and symbolic relation, **not as proof that the neodialectical grammar derives from the Spanish coat of arms**.

- **Pillars / Threshold™** → limit, transit, opening and responsibility towards what lies beyond the known frame;
- **Chains / Bond™** → interdependence, commitment and also memory of that from which a society may need liberation;
- **Pomegranate / Plural fruit™** → contained plurality, fertility and composite unity;
- **Stripes / Territorial continuity™** → memory of historical layers remaining distinguishable inside a larger composition;
- **Fleur-de-lis / Dynastic genealogy™** → memory of historical lineage without turning lineage into automatic privilege;
- **Historical orb and cross** → memory of European cosmologies and religious traditions, subject to the same principle of symbolic non-monopoly.

Not all of these symbols automatically become central emblems. Their status remains open to Open Synthesis.

### Synthesis Flag Principle™

A future neodialectical flag of Spain or a **Humanity-in-Synthesis Flag™** should not arise by destroying previous flags. It may be studied as a composition of current, historical and cultural layers: constitutional Spanish, historical red-yellow-red and red-white traditions where relevant, European, neodialectical, Jewish/Hebrew, Arab and Islamic, Christian, secular, regional, migrant, sexual and gender diversity, and other memories SAN™ identifies as absent.

Including a memory **does not imply adherence to all its dogmas**, nor does it permit classifying human groups as biologically pure, impure or degraded. The function of a synthesis flag would be to represent coexistence, memory and the possibility of recomposition without expulsion.

Any such design is currently an **open symbolic proposal**, not an official State flag nor a unilateral replacement of constitutional symbols in force.

This Neoaxiom does not turn symbols into authority by themselves. It uses them as an **archetypal grammar of responsibility, memory and historical reconciliation**.

**Status:** ACTIVATED AS SYMBOLIC AXIOM · EXPANDED WITH LION AND OPEN CONSTELLATION · OPEN SYNTHESIS.
**Dedicated Open Synthesis:** [#93](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/93) · [General matrix #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80)
'''
if not es_pat.search(t) or not en_pat.search(t): raise SystemExit('NAX-10 sections not found')
t=es_pat.sub(es_new.rstrip(),t,count=1)
t=en_pat.sub(en_new.rstrip(),t,count=1)
NEO.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 2. XXXVI: lion + flag synthesis, additive via bis sections.
# ---------------------------------------------------------------------------
t=M36.read_text(encoding='utf-8')
t=t.replace('**Versión / Version:** 1.0','**Versión / Version:** 1.1',1)
if '## III bis. El León' not in t:
    anchor='## IV. Innova_N como herramienta neodialéctica'
    block='''## III bis. El León

El **León™** se incorpora a la gramática de custodia como fuerza protectora contenida.

No representa superioridad de sangre, pueblo o linaje. Representa:

- coraje ante el peligro;
- dignidad sin sometimiento;
- capacidad de defender al vulnerable;
- permanencia ante la presión;
- fuerza limitada por finalidad;
- y decisión de proteger sin convertir protección en dominio.

```text
FUERZA SIN LÍMITE
= DEPREDACIÓN

LEÓN NEODIALÉCTICO
= CORAJE + DIGNIDAD + PROTECCIÓN + LÍMITE
```

Su presencia conecta esta gramática con una memoria heráldica española real, pero su función neodialéctica es universalizable y queda sometida a la misma prohibición de supremacía que Corona y Águila.

'''
    if anchor not in t: raise SystemExit('M36 ES IV anchor missing')
    t=t.replace(anchor,block+anchor,1)
if '## VII bis. La bandera hecha de memoria' not in t:
    anchor='## VIII. Custodia por la Fundación Innova_N'
    block='''## VII bis. La bandera hecha de memoria

Una bandera puede funcionar como frontera identitaria o como superficie de memoria compartida.

La propuesta neodialéctica no consiste en arrancar los símbolos anteriores para dejar un lienzo vacío. Consiste en preguntar qué memorias siguen vivas, cuáles fueron excluidas, cuáles necesitan ser reinterpretadas y cómo pueden convivir sin que una sola reclame monopolio sobre el conjunto.

El escudo español vigente comparte parte de la constelación que está apareciendo en NEOCore™: **Corona, León, Castillo/Torre y Mundo/Orbe** aparecen de forma directa o asociada; las Columnas, cadenas, granada, franjas y lises aportan otras capas históricas. El Águila pertenece a etapas históricas del escudo español, no al modelo oficial vigente desde 1981. La Piedra es un arquetipo neodialéctico, no una pieza del escudo estatal.

Esta relación es sugerente, pero debe mantenerse trazable: **semejanza simbólica no demuestra genealogía causal**.

### Bandera de España en Síntesis™ · propuesta abierta

Se abre una línea de SAN™ para estudiar una bandera capaz de conservar, sin confundirlas, capas que hoy aparecen fragmentadas:

- la bandera constitucional vigente y su continuidad histórica;
- enseñas históricas españolas y regionales que aporten memoria relevante;
- la Corona como responsabilidad;
- la gramática neodialéctica;
- la pertenencia europea;
- la herencia judía/hebraica de la península y de su diáspora;
- la herencia árabe e islámica de Al-Ándalus y del Mediterráneo;
- la memoria cristiana y laica;
- pueblos, regiones, migraciones y minorías;
- y la diversidad sexual y de género, precisamente porque una bandera que aspire a representar a todos no puede exigir que una parte de la población desaparezca simbólicamente para entrar en ella.

La Síntesis **no adopta la idea de que la diversidad sexual constituya degradación biológica**. Puede estudiar cómo distintos dogmas la han juzgado históricamente y cómo esas exclusiones fragmentaron sociedades, pero no convierte ese juicio moral en una afirmación genética.

La bandera resultante, si alguna vez converge, no debería parecer un collage de logotipos. La función de SAN™ sería encontrar **equivalencias arquetípicas** capaces de condensar memorias distintas en una composición legible.

### Bandera de la Humanidad en Síntesis™

El mismo procedimiento puede escalarse. La humanidad no necesita una bandera que declare vencedora una civilización. Necesita, si decide construirla, una bandera capaz de recordar que su historia está hecha de fragmentos que todavía deben aprender a reconocerse mutuamente.

```text
MEMORIA FRAGMENTADA
+ RECONOCIMIENTO
+ TRADUCCIÓN SIMBÓLICA
+ NO EXCLUSIÓN
+ SAN
→ BANDERA COMO SÍNTESIS ABIERTA
```

No se proclama aquí un diseño final. Se abre un proceso.

'''
    if anchor not in t: raise SystemExit('M36 ES VIII anchor missing')
    t=t.replace(anchor,block+anchor,1)
if '## III bis. The Lion' not in t:
    anchor='## IV. Innova_N as the neodialectical tool'
    block='''## III bis. The Lion

The **Lion™** enters the grammar of custodianship as contained protective strength.

It does not represent superiority of blood, people or lineage. It represents courage before danger, dignity without submission, defence of the vulnerable, endurance under pressure, strength limited by purpose and the decision to protect without turning protection into domination.

```text
STRENGTH WITHOUT LIMIT
= PREDATION

NEODIALECTICAL LION
= COURAGE + DIGNITY + PROTECTION + LIMIT
```

Its presence connects this grammar with real Spanish heraldic memory, but its neodialectical function is universalizable and remains subject to the same prohibition of supremacy as Crown and Eagle.

'''
    if anchor not in t: raise SystemExit('M36 EN IV anchor missing')
    t=t.replace(anchor,block+anchor,1)
if '## VII bis. The flag made of memory' not in t:
    anchor='## VIII. Custodianship by the Innova_N Foundation'
    block='''## VII bis. The flag made of memory

A flag may function as an identity border or as a surface of shared memory.

The neodialectical proposal does not tear away previous symbols to leave an empty canvas. It asks which memories remain alive, which were excluded, which need reinterpretation and how they can coexist without one claiming monopoly over the whole.

Spain's current coat of arms shares part of the constellation emerging in NEOCore™: **Crown, Lion, Castle/Tower and World/Orb** appear directly or by association; the Pillars, chains, pomegranate, stripes and fleurs-de-lis add further historical layers. The Eagle belongs to historical stages of the Spanish arms, not to the official model in force since 1981. Stone is a neodialectical archetype, not an element of the State coat of arms.

The relation is suggestive, but must remain traceable: **symbolic similarity does not prove causal genealogy**.

### Spain-in-Synthesis Flag™ · open proposal

SAN™ is opened to study a flag capable of preserving, without confusing them, layers that are now fragmented: the current constitutional flag and its historical continuity; relevant historical and regional ensigns; Crown as responsibility; neodialectical grammar; European belonging; Jewish/Hebrew heritage of the peninsula and diaspora; Arab and Islamic heritage of Al-Andalus and the Mediterranean; Christian and secular memory; peoples, regions, migrations and minorities; and sexual and gender diversity, precisely because a flag aspiring to represent everyone cannot require part of the population to disappear symbolically in order to belong.

The Synthesis **does not adopt the claim that sexual diversity constitutes biological degradation**. It may study how different dogmas judged it historically and how exclusion fragmented societies, but it does not turn a moral judgement into a genetic statement.

If a design ever converges, it should not become a collage of logos. SAN™ should search for **archetypal equivalences** capable of condensing different memories into a legible composition.

### Humanity-in-Synthesis Flag™

The same procedure may scale. Humanity does not need a flag proclaiming one civilisation victorious. If it chooses to build one, it needs a flag capable of remembering that its history is made of fragments that still need to recognise one another.

```text
FRAGMENTED MEMORY
+ RECOGNITION
+ SYMBOLIC TRANSLATION
+ NON-EXCLUSION
+ SAN
→ FLAG AS OPEN SYNTHESIS
```

No final design is proclaimed here. A process is opened.

'''
    if anchor not in t: raise SystemExit('M36 EN VIII anchor missing')
    t=t.replace(anchor,block+anchor,1)
# Add new relations without deleting existing ones.
t=t.replace('- and **XXXVI** fixes the constitutional function of the Crown, Eagle and Innova_N tool within that architecture.', '- **XLIX · Meeting Point between Cultures™** provides the principle of cultural interoperability and plural unity;\n- **LX · Necessary Human Relevance™** requires that symbolic integration preserve actual human participation rather than merely represent populations;\n- and **XXXVI** fixes the constitutional function of the Crown, Eagle, Lion and Innova_N tool within that architecture.',1)
t=t.replace('- y **XXXVI** fija la función constitucional de la Corona, el Águila y la herramienta Innova_N dentro de esa arquitectura.', '- **XLIX · Punto de Encuentro entre Culturas™** aporta el principio de interoperabilidad cultural y unidad plural;\n- **LX · Relevancia Humana Necesaria™** exige que la integración simbólica preserve participación humana real y no sólo representación abstracta;\n- y **XXXVI** fija la función constitucional de la Corona, el Águila, el León y la herramienta Innova_N dentro de esa arquitectura.',1)
# Expand synthesis topics.
t=t.replace('- los riesgos históricos asociados a Corona y Águila;', '- los riesgos históricos asociados a Corona, Águila y León;\n- la constelación heráldica española y sus relaciones no causales con NAX-10;\n- la Bandera de España en Síntesis™ y la Bandera de la Humanidad en Síntesis™;\n- criterios de inclusión simbólica sin biologizar identidades o convertir diversidad en jerarquía;',1)
t=t.replace('- historical risks associated with Crown and Eagle;', '- historical risks associated with Crown, Eagle and Lion;\n- the Spanish heraldic constellation and its non-causal relations with NAX-10;\n- the Spain-in-Synthesis Flag™ and Humanity-in-Synthesis Flag™;\n- criteria for symbolic inclusion without biologising identities or turning diversity into hierarchy;',1)
M36.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 3. Canonical manifesto index: add LX and update direct latest surfaces.
# ---------------------------------------------------------------------------
t=MIDX.read_text(encoding='utf-8')
entry='- **LX** · [Relevancia Humana Necesaria™ · Inteligencia Distribuida, Aporte y Anti-Captura Social / Necessary Human Relevance™ · Distributed Intelligence, Contribution and Anti-Capture](60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md)'
if entry not in t:
    anchor='- **LIX** · [Custodia Cognitiva Distribuida™ · IA, Reparación y Responsabilidad Humana / Distributed Cognitive Custodianship™ · AI, Repair and Human Responsibility](59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN.md)'
    if anchor not in t: raise SystemExit('MIDX LIX entry missing')
    t=t.replace(anchor,anchor+'\n'+entry,1)
t=re.sub(r'> \*\*LIX · Custodia Cognitiva Distribuida™ · IA, Reparación y Responsabilidad Humana\*\*  \n> \*\*LIX · Distributed Cognitive Custodianship™ · AI, Repair and Human Responsibility\*\*\n>\n> \*\*\[Leer LIX / Read LIX\]\(59_custodia_cognitiva_distribuida_ia_reparacion_ES_EN\.md\) · \[Síntesis Abierta LIX · #79 / Open Synthesis LIX · #79\]\([^\n]+\)\*\*',
'''> **LX · Relevancia Humana Necesaria™ · Inteligencia Distribuida, Aporte y Anti-Captura Social**  
> **LX · Necessary Human Relevance™ · Distributed Intelligence, Contribution and Anti-Capture**
>
> **[Leer LX / Read LX](60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) · [Síntesis Abierta LX · #99 / Open Synthesis LX · #99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99)**''',t,count=1)
t=t.replace('**59 manifiestos bilingües · I–LIX · 24 oleadas / 59 bilingual manifestos · I–LIX · 24 waves**','**60 manifiestos bilingües · I–LX · 24 oleadas / 60 bilingual manifestos · I–LX · 24 waves**')
t=re.sub(r'\*\*Última síntesis / Latest synthesis:\*\* \[LIX[^\n]+', '**Última síntesis / Latest synthesis:** [LX · Relevancia Humana Necesaria™](60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) · [Issue #99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99)  ', t,count=1)
MIDX.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 4. Open Synthesis index: append LX in ES and EN canonical tables.
# ---------------------------------------------------------------------------
t=SYN.read_text(encoding='utf-8')
es_row='| LX | [Relevancia Humana Necesaria™](../../manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) | [#99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99) |'
en_row='| LX | [Necessary Human Relevance™](../../manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) | [#99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99) |'
pos_en=t.find('# EN · English')
if pos_en<0: raise SystemExit('SYN EN marker missing')
es=t[:pos_en]; en=t[pos_en:]
if es_row not in es:
    hits=list(re.finditer(r'^\| LIX \|.*$',es,re.M))
    if not hits: raise SystemExit('SYN ES LIX row missing')
    m=hits[-1]; es=es[:m.end()]+'\n'+es_row+es[m.end():]
if en_row not in en:
    hits=list(re.finditer(r'^\| LIX \|.*$',en,re.M))
    if not hits: raise SystemExit('SYN EN LIX row missing')
    m=hits[-1]; en=en[:m.end()]+'\n'+en_row+en[m.end():]
SYN.write_text(es+en,encoding='utf-8')

# ---------------------------------------------------------------------------
# 5. Relation map: explicit LX node and NAX relations.
# ---------------------------------------------------------------------------
t=REL.read_text(encoding='utf-8')
t=t.replace('**Cobertura / Coverage:** I–LIX · 59 manifiestos / 59 manifestos','**Cobertura / Coverage:** I–LX · 60 manifiestos / 60 manifestos')
if '### LX · Relevancia Humana Necesaria™' not in t:
    block='''### LX · Relevancia Humana Necesaria™ · inteligencia distribuida y anti-captura social
- [Manifiesto / Manifesto](./60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) · [Síntesis #99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99)
- Relaciones principales: V · Simbiosis Humano–IA; VII · Economía del Aporte; VIII · Ingeniería Social Abierta; XIV · Alienación; XXI · Reconocimiento; XXIII · Tiempo Cognitivo; XXXI · Neuromarketing; XLII–XLIII · soberanía e inteligencia expandida; XLVIII · Síntesis; L · Inteligencia Compartida; LVIII · Inteligencia Civilizatoria; LIX · Custodia Cognitiva; NAX-08, NAX-13 y NAX-14.
- Función aplicada: separar popularidad de aporte, detectar amplificación social sin presumir fraude, distribuir capacidad de trabajo con IA y evitar una aristocracia reputacional.

'''
    anchor='## Neoaxiomas™ ↔ Manifiestos ↔ trabajo aplicado'
    if anchor not in t: raise SystemExit('REL Neoaxiom anchor missing')
    t=t.replace(anchor,block+anchor,1)
# Enrich NAX lines additively.
t=t.replace('- **NAX-01 / NAX-08 / NAX-14** ↔ V · Simbiosis Humano–IA; VII · Economía del Aporte; L · Inteligencia Compartida; LVIII · Inteligencia Civilizatoria; LIX · Custodia Cognitiva.', '- **NAX-01 / NAX-08 / NAX-14** ↔ V · Simbiosis Humano–IA; VII · Economía del Aporte; L · Inteligencia Compartida; LVIII · Inteligencia Civilizatoria; LIX · Custodia Cognitiva; **LX · Relevancia Humana Necesaria**.')
t=t.replace('- **NAX-10** ↔ XXV · Pulido de la Piedra; XXXVI · Corona, Águila y Custodia.', '- **NAX-10** ↔ XXV · Pulido de la Piedra; XXXVI · Corona, Águila, León y Custodia; XLIX · interoperabilidad cultural y bandera como síntesis simbólica.')
t=t.replace('- **NAX-13** ↔ VII · Economía del Aporte; XXI · Reconocimiento; XXIII · Soberanía del Tiempo Cognitivo.', '- **NAX-13** ↔ VII · Economía del Aporte; XXI · Reconocimiento; XXIII · Soberanía del Tiempo Cognitivo; **LX · Relevancia Humana Necesaria**.')
t=t.replace('- **NAX-14** ↔ V · Simbiosis; XIV · Alienación; XXXVIII · Protección de Infancia; XLII–XLIII · soberanía e inteligencia expandida; LVIII–LIX.', '- **NAX-14** ↔ V · Simbiosis; XIV · Alienación; XXXVIII · Protección de Infancia; XLII–XLIII · soberanía e inteligencia expandida; LVIII–LIX; **LX · Relevancia Humana Necesaria**.')
REL.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 6. Root latest feature not marker-managed.
# ---------------------------------------------------------------------------
t=ROOTREADME.read_text(encoding='utf-8')
pat=re.compile(r'### LIX · Custodia Cognitiva Distribuida™\n### LIX · Distributed Cognitive Custodianship™\n\n.*?\n\n\*\*\[Leer LIX / Read LIX\].*?\*\*',re.S)
new='''### LX · Relevancia Humana Necesaria™
### LX · Necessary Human Relevance™

Inteligencia distribuida con potencia humana suficiente, separación entre visibilidad y aporte, cooperación frente a competición de estatus y simbiosis con IA sin nueva aristocracia cognitiva. / Distributed intelligence with sufficient human capacity, separation of visibility from contribution, cooperation over status competition and AI symbiosis without a new cognitive aristocracy.

**[Leer LX / Read LX](./manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md)** · **[Síntesis Abierta #99 / Open Synthesis #99](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/99)**'''
if pat.search(t): t=pat.sub(new,t,count=1)
ROOTREADME.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 7. Wiki reading guide: remove stale I-L pointer and extend recent waves.
# ---------------------------------------------------------------------------
t=WIKI.read_text(encoding='utf-8')
t=t.replace('Índice canónico de manifiestos I–L]','Índice canónico de manifiestos I–LX]')
t=t.replace('Canonical manifesto index I–L]','Canonical manifesto index I–LX]')
if '* **XLIX–LII:**' not in t:
    es_anchor='* **XLVIII:** La Síntesis Todo lo Ve™, observación distribuida, Placa de Petri Universal™, escalas de potencias de diez y Máquina Fractal del Tiempo™ como modelo filosófico de memoria evolutiva del organismo conjunto.'
    es_add='''\n* **XLIX–LII:** interoperabilidad cultural, inteligencia compartida, poder cívico y ciudadanía humana funcional.\n* **LIII–LVI:** Leónidas™, reparación, riesgos de escala invisible y NO-CONTROL™.\n* **LVII–LIX:** refugio, inteligencia civilizatoria y custodia cognitiva distribuida.\n* **LX:** Relevancia Humana Necesaria™, potencia distribuida, aporte y anti-captura social.'''
    if es_anchor in t:t=t.replace(es_anchor,es_anchor+es_add,1)
if '* **XLIX–LII:** cultural interoperability' not in t:
    en_anchor='* **XLVIII:** The Synthesis Sees Everything™, distributed observation, Universal Petri Dish™, powers-of-ten scales and Fractal Time Machine™ as a philosophical model of evolutionary memory of the joint organism.'
    en_add='''\n* **XLIX–LII:** cultural interoperability, shared intelligence, civic power and functional human citizenship.\n* **LIII–LVI:** Leónidas™, repair, invisible-scale risks and NO-CONTROL™.\n* **LVII–LIX:** refuge, civilisational intelligence and distributed cognitive custodianship.\n* **LX:** Necessary Human Relevance™, distributed capacity, contribution and social anti-capture.'''
    if en_anchor in t:t=t.replace(en_anchor,en_anchor+en_add,1)
# Add direct recent link.
if '60_relevancia_humana_necesaria' not in t:
    es_link='* [LX · Relevancia Humana Necesaria™](../manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md)'
    t=t.replace('* [XLVIII · La Síntesis Todo lo Ve™](../manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)', '* [XLVIII · La Síntesis Todo lo Ve™](../manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)\n'+es_link,1)
    # English section gets same bilingual target.
    en_link='* [LX · Necessary Human Relevance™](../manifiestos/60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md)'
    idx=t.find('# EN · English')
    if idx>=0:
        pre,post=t[:idx],t[idx:]
        post=post.replace('* [XLVIII · The Synthesis Sees Everything™](../manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)', '* [XLVIII · The Synthesis Sees Everything™](../manifiestos/48_sintesis_todo_lo_ve_placa_petri_universal_maquina_fractal_tiempo_ES_EN.md)\n'+en_link,1)
        t=pre+post
WIKI.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 8. Update LIX explicit older navigation if present; managed block sync will finish it.
# ---------------------------------------------------------------------------
t=M59.read_text(encoding='utf-8')
t=t.replace('← [LVIII · Civilisational Intelligence™](58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md) · [Index](README.md) · Fin provisional de la serie / Provisional end of series', '← [LVIII · Civilisational Intelligence™](58_inteligencia_civilizatoria_democracia_cognitiva_ES_EN.md) · [Index](README.md) · [LX · Necessary Human Relevance™](60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN.md) →')
M59.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# 9. Current postcheck expectation: 60 / LX instead of old snapshot 59 / LIX.
# ---------------------------------------------------------------------------
t=POST.read_text(encoding='utf-8')
t=t.replace("ok('Corpus canónico I–LIX = 59 manifiestos',len(mans)==59 and mans[0][0]=='I' and mans[-1][0]=='LIX'", "ok('Corpus canónico I–LX = 60 manifiestos',len(mans)==60 and mans[0][0]=='I' and mans[-1][0]=='LX'")
t=t.replace("f'**Manifiestos canónicos:** {len(mans)}  ',f'**Neoaxiomas:** 14", "f'**Manifiestos canónicos:** {len(mans)}  ',f'**Neoaxiomas:** 14")
POST.write_text(t,encoding='utf-8')

# ---------------------------------------------------------------------------
# Validation before downstream synchronisers/audits.
# ---------------------------------------------------------------------------
checks=[]
checks.append(('NAX lion ES', 'León™' in NEO.read_text(encoding='utf-8')))
checks.append(('NAX lion EN', 'Lion™' in NEO.read_text(encoding='utf-8')))
checks.append(('NAX flag synthesis', 'Bandera de la Humanidad en Síntesis™' in NEO.read_text(encoding='utf-8')))
checks.append(('M36 flag section', '## VII bis. La bandera hecha de memoria' in M36.read_text(encoding='utf-8')))
checks.append(('M60 indexed', '60_relevancia_humana_necesaria' in MIDX.read_text(encoding='utf-8')))
checks.append(('M60 synth ES/EN', SYN.read_text(encoding='utf-8').count('60_relevancia_humana_necesaria')>=2))
checks.append(('REL 60 coverage', '**Cobertura / Coverage:** I–LX · 60 manifiestos / 60 manifestos' in REL.read_text(encoding='utf-8')))
checks.append(('Wiki LX', 'I–LX' in WIKI.read_text(encoding='utf-8') and 'Relevancia Humana Necesaria' in WIKI.read_text(encoding='utf-8')))
failed=[x for x,v in checks if not v]
if failed:
    print('FAIL',failed);sys.exit(1)
print('PATCH OK',len(checks),'checks')
