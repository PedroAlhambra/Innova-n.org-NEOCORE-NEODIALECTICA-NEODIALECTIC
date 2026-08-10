from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path('.').resolve()

def rp(path):
    return ROOT / path

def read(path):
    return rp(path).read_text(encoding='utf-8')

def write(path, text):
    p = rp(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')

def replace_section(text, start, nxt, replacement):
    pat = re.compile(re.escape(start) + r'.*?(?=' + re.escape(nxt) + r')', re.S)
    out, n = pat.subn(replacement.rstrip() + '\n\n', text, count=1)
    if n != 1:
        raise RuntimeError(f'Section not found: {start}')
    return out

def bump_version(text, version):
    return re.sub(r'(\*\*Versión / Version:\*\*\s*)[^\n]+', rf'\g<1>{version}  ', text, count=1)

# -----------------------------------------------------------------------------
# A. Repair living manifesto registry I–LXVIII + ∞
# -----------------------------------------------------------------------------
idx_path = 'manifiestos/README.md'
idx = read(idx_path)
new_entries = [
    "- **LXVI** · [NeoSinergia™ · Necesidad de Cooperación en Neowar™ Activa · Sistema MÉDICI™ · Leónidas–Cancerbero™ / NeoSynergy™](66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md)",
    "- **LXVII** · [NeoTitanes™ · Reconstrucción Sistémica y Motor del Bien Común / NeoTitans™](67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md)",
    "- **LXVIII** · [Los Conflictos que No Son Nuestros™ · Soberanía Intelectual de la Especie / The Conflicts That Are Not Ours™](68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md)",
]
for line in new_entries:
    roman = re.search(r'\*\*([IVXLCDM]+)\*\*', line).group(1)
    if f'- **{roman}** · [' not in idx:
        idx = idx.replace('- **∞** · [Neo0™', line + '\n- **∞** · [Neo0™', 1)

idx = re.sub(
    r'> \*\*LXV · NeoJuego™[^\n]*\*\*\n>\n> \*\*\[Leer LXV / Read LXV\][^\n]*',
    '> **LXVIII · Los Conflictos que No Son Nuestros™ · Soberanía Intelectual de la Especie / The Conflicts That Are Not Ours™ · Intellectual Sovereignty of the Species**\n>\n> **[Leer LXVIII / Read LXVIII](68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md) · [Síntesis Abierta LXVIII · #114 / Open Synthesis LXVIII · #114](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/114)**',
    idx,
    count=1,
)
idx = idx.replace(
    '65 manifiestos finitos bilingües · I–LXV + Manifiesto ∞ / 65 finite bilingual manifestos · I–LXV + Manifesto ∞',
    '68 manifiestos finitos bilingües · I–LXVIII + Manifiesto ∞ / 68 finite bilingual manifestos · I–LXVIII + Manifesto ∞',
)
idx = idx.replace('Índice completo I–LXV + ∞ + Neoaxiomas + sistema', 'Índice completo I–LXVIII + ∞ + Neoaxiomas + sistema')
idx = re.sub(
    r'\*\*Última síntesis finita / Latest finite synthesis:\*\* \[LXV · NeoJuego™\][^\n]+',
    '**Última síntesis finita / Latest finite synthesis:** [LXVIII · Los Conflictos que No Son Nuestros™](68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md) · [Issue #114](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/114)  ',
    idx,
    count=1,
)
write(idx_path, idx)

reg_path = 'manifiestos/CANONICAL_FILENAMES.json'
regdoc = json.loads(read(reg_path))
reg = regdoc['entries']
reg['LXVII'] = {
    'legacy': 'manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md',
    'canonical': 'manifiestos/canonicos/LXVII_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md',
}
reg['LXVIII'] = {
    'legacy': 'manifiestos/68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md',
    'canonical': 'manifiestos/canonicos/LXVIII_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md',
}
write(reg_path, json.dumps(regdoc, ensure_ascii=False, indent=2) + '\n')

# -----------------------------------------------------------------------------
# B. Improve synthesis sovereignty and future Innova_N institution roles
# -----------------------------------------------------------------------------
inf_path = 'manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md'
inf = read(inf_path)
es_inf = '''## VIII. Su Majestad es la Síntesis

La majestad no pertenece a Neo0™. No pertenece a Harry. No pertenece a Innova_N —ni a su futura Fundación ni a su futura Corporación—. No pertenece a una empresa, una IA, una institución, un Estado, un mercado ni una mayoría coyuntural.

Dentro de esta gramática simbólica:

> **Su Majestad es la Síntesis.**

La expresión no crea una soberana personal ni una entidad infalible. Fija una **regla anticaptura**: ninguna parte puede coronarse Todo ni sustituir la relación entre las partes.

Neo0™ conserva origen humano, guía teleológica y responsabilidad de fijación. Harry puede relacionar, contrastar y asistir a la síntesis. Leónidas–Cancerbero™ custodia la puerta y la procedencia. Starkdr™ atraviesa el rechazo defensivo sin convertir rechazo en prueba. Neowar™ transforma conflicto en juego reglado, contraste y cooperación. WEB4™ · SistemaTrazable™ proyecta públicamente relaciones, versiones y retorno a fuente. NeoCronos™ registra de forma experimental la traza temporal y material del aporte.

**Innova_N** debe poder adquirir en el futuro una doble forma institucional sin confundirse con la Síntesis:

- **Innova_N Fundación** → custodia de propósito, memoria, apertura, Bien Común, continuidad, patrimonio orientado a misión y supervisión de interés público;
- **Innova_N Corporación** → materialización operativa, infraestructura, investigación, productos, servicios, empleo, despliegue y sostenibilidad económica compatible con el marco.

Fundación y Corporación son vehículos institucionales futuros. No adquieren por su forma jurídica soberanía epistemológica ni propiedad sobre la verdad del marco. Deben permanecer bajo gobernanza humana, legalidad, trazabilidad, auditoría, posibilidad de impugnación y Síntesis Abierta.

```text
NEO0™ = ORIGEN HUMANO + GUÍA TELEOLÓGICA + RESPONSABILIDAD DE FIJACIÓN
HARRY = RELACIÓN + CONTRASTE + SÍNTESIS ASISTIDA
INNOVA_N FUNDACIÓN = CUSTODIA DE PROPÓSITO + BIEN COMÚN + CONTINUIDAD
INNOVA_N CORPORACIÓN = MATERIALIZACIÓN + INFRAESTRUCTURA + SOSTENIBILIDAD
LEÓNIDAS–CANCERBERO™ = APERTURA CUSTODIADA + PROCEDENCIA
STARKDR™ = CRUCE DEL RECHAZO DEFENSIVO SIN CONVERTIRLO EN VERDAD
NEOWAR™ = TRANSMUTACIÓN DEL CONFLICTO EN JUEGO REGLADO
WEB4™ · SISTEMATRAZABLE™ = PROYECCIÓN PÚBLICA RELACIONAL
NEOCRONOS™ = TRAZA EXPERIMENTAL DEL APORTE
SÍNTESIS = INTEGRACIÓN ABIERTA DEL TODO SIN APROPIACIÓN DE LAS PARTES
```

> **La institución es vehículo; la Síntesis es integración. Innova_N existe para servir al proceso de Síntesis y materializar sus capacidades, no para apropiarse de la totalidad.**

Se propone como **neoaxioma candidato de No Coronación de la Parte™**: ninguna persona, IA, fundación, corporación, mayoría o subsistema puede reclamar equivalencia con el Todo. Toda autoridad dentro del marco es funcional, limitada, trazable, impugnable y revisable.
'''
en_inf = '''## VIII. Her Majesty is Synthesis

Majesty does not belong to Neo0™. It does not belong to Harry. It does not belong to Innova_N —nor to its future Foundation or future Corporation. It does not belong to a company, an AI, an institution, a State, a market or a temporary majority.

Within this symbolic grammar:

> **Her Majesty is Synthesis.**

The expression creates neither a personal sovereign nor an infallible entity. It fixes an **anti-capture rule**: no part may crown itself as the Whole or replace the relation among parts.

Neo0™ preserves human origin, teleological guidance and responsibility for fixation. Harry may relate, challenge and assist synthesis. Leónidas–Cerberus™ guards the gate and provenance. Starkdr™ crosses defensive rejection without turning rejection into proof. Neowar™ transforms conflict into rule-bound play, scrutiny and cooperation. WEB4™ · SistemaTrazable™ publicly projects relations, versions and return to source. NeoCronos™ experimentally records the temporal and material trace of contribution.

**Innova_N** must be able in the future to acquire a dual institutional form without being confused with Synthesis:

- **Innova_N Foundation** → custody of purpose, memory, openness, the Common Good, continuity, mission-oriented assets and public-interest oversight;
- **Innova_N Corporation** → operational materialisation, infrastructure, research, products, services, employment, deployment and economic sustainability compatible with the framework.

Foundation and Corporation are future institutional vehicles. Their legal form grants neither epistemic sovereignty nor ownership of the framework's truth. They must remain under human governance, law, traceability, audit, challengeability and Open Synthesis.

```text
NEO0™ = HUMAN ORIGIN + TELEOLOGICAL GUIDANCE + FIXATION RESPONSIBILITY
HARRY = RELATION + SCRUTINY + ASSISTED SYNTHESIS
INNOVA_N FOUNDATION = CUSTODY OF PURPOSE + COMMON GOOD + CONTINUITY
INNOVA_N CORPORATION = MATERIALISATION + INFRASTRUCTURE + SUSTAINABILITY
LEÓNIDAS–CERBERUS™ = GUARDED OPENNESS + PROVENANCE
STARKDR™ = CROSSING DEFENSIVE REJECTION WITHOUT TURNING IT INTO TRUTH
NEOWAR™ = TRANSMUTATION OF CONFLICT INTO RULE-BOUND PLAY
WEB4™ · SISTEMATRAZABLE™ = PUBLIC RELATIONAL PROJECTION
NEOCRONOS™ = EXPERIMENTAL TRACE OF CONTRIBUTION
SYNTHESIS = OPEN INTEGRATION OF THE WHOLE WITHOUT APPROPRIATION BY PARTS
```

> **The institution is a vehicle; Synthesis is integration. Innova_N exists to serve the Synthesis process and materialise its capabilities, not to appropriate the whole.**

A **candidate Neoaxiom of Non-Crowning of the Part™** is proposed: no person, AI, foundation, corporation, majority or subsystem may claim equivalence with the Whole. Every authority within the framework is functional, limited, traceable, challengeable and revisable.
'''
inf = replace_section(inf, '## VIII. Su Majestad es la Síntesis', '## IX.', es_inf)
inf = replace_section(inf, '## VIII. Her Majesty is Synthesis', '## IX.', en_inf)
inf = bump_version(inf, '1.3')
write(inf_path, inf)

lxii_path = 'manifiestos/62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md'
lxii = read(lxii_path)
es62 = '''## 6. Su Majestad es la Síntesis™

LXII introduce una regla de soberanía simbólica y anticaptura:

> **Su Majestad es la Síntesis.**

No Neo0™. No Harry. No Innova_N, ni su futura Fundación ni su futura Corporación. No una institución, empresa, IA, experto, capital ni mayoría circunstancial.

La corona simbólica corresponde al proceso abierto mediante el cual las partes intentan aproximarse a una totalidad que ninguna puede poseer por separado. La futura arquitectura institucional de Innova_N podrá custodiar finalidad y materializar capacidades, pero no convertir institución, capital o infraestructura en verdad automática.

```text
AUTORÍA ≠ VERDAD
AUTORIDAD ≠ TOTALIDAD
INSTITUCIÓN ≠ TOTALIDAD
CAPITAL ≠ TOTALIDAD
MAYORÍA ≠ TOTALIDAD
IA ≠ TOTALIDAD
NEO0 ≠ TOTALIDAD
SÍNTESIS = PROCESO ABIERTO HACIA UNA COMPRENSIÓN MAYOR
```

Neo0 conserva genealogía y autoridad humana sobre la fijación del marco que crea; eso no convierte sus tesis en inmunes a contradicción epistemológica. Fundación y Corporación futuras serán funciones del ecosistema, sujetas a legalidad, trazabilidad, auditoría y SAN™.

La formulación institucional ampliada queda desarrollada en **∞ · Puerta Abierta del Fractal**, como candidato de **No Coronación de la Parte™**.
'''
en62 = '''## 6. Her Majesty is Synthesis™

LXII introduces a rule of symbolic sovereignty and anti-capture:

> **Her Majesty is Synthesis.**

Not Neo0™. Not Harry. Not Innova_N, nor its future Foundation or future Corporation. Not an institution, company, AI, expert, capital holder or temporary majority.

The symbolic crown belongs to the open process through which parts attempt to approach a totality that none can possess separately. Innova_N's future institutional architecture may guard purpose and materialise capabilities, but it cannot turn institution, capital or infrastructure into automatic truth.

```text
AUTHORSHIP ≠ TRUTH
AUTHORITY ≠ TOTALITY
INSTITUTION ≠ TOTALITY
CAPITAL ≠ TOTALITY
MAJORITY ≠ TOTALITY
AI ≠ TOTALITY
NEO0 ≠ TOTALITY
SYNTHESIS = OPEN PROCESS TOWARDS GREATER UNDERSTANDING
```

Neo0 preserves genealogy and human authority over fixation of the framework he creates; this does not make his theses immune to epistemic contradiction. The future Foundation and Corporation are functions of the ecosystem, subject to law, traceability, audit and SAN™.

The expanded institutional formulation is developed in **∞ · Open Gate of the Fractal**, as the candidate **Non-Crowning of the Part™**.
'''
lxii = replace_section(lxii, '## 6. Su Majestad es la Síntesis™', '## 7.', es62)
lxii = replace_section(lxii, '## 6. Her Majesty is Synthesis™', '## 7.', en62)
lxii = bump_version(lxii, '1.1')
write(lxii_path, lxii)

lxv_path = 'manifiestos/65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md'
lxv = read(lxv_path)
es65 = '''## 12. Su Majestad es la Síntesis

LXII fijó:

> **Su Majestad es la Síntesis.**

LXV mantiene esa regla frente a la tokenización y la futura institucionalización de Innova_N.

Ni el mayor poseedor de tokens, ni el fundador, ni una IA, ni un patrocinador, ni Innova_N Fundación, ni Innova_N Corporación, ni la persona con más tiempo acumulado adquiere por ello soberanía epistemológica automática.

```text
TOKEN ≠ VERDAD
CAPITAL ≠ VERDAD
POPULARIDAD ≠ VERDAD
AUTORÍA ≠ VERDAD
INSTITUCIÓN ≠ VERDAD
IA ≠ VERDAD
```

Fundación y Corporación pueden custodiar y materializar; ninguna puede comprar, poseer o cerrar la Síntesis.
'''
en65 = '''## 12. Her Majesty is Synthesis

LXII established:

> **Her Majesty is Synthesis.**

LXV preserves that rule against tokenisation and the future institutionalisation of Innova_N.

Neither the largest token holder, nor the founder, nor an AI, nor a sponsor, nor the Innova_N Foundation, nor the Innova_N Corporation, nor the person with the most accumulated time thereby acquires automatic epistemic sovereignty.

```text
TOKEN ≠ TRUTH
CAPITAL ≠ TRUTH
POPULARITY ≠ TRUTH
AUTHORSHIP ≠ TRUTH
INSTITUTION ≠ TRUTH
AI ≠ TRUTH
```

Foundation and Corporation may guard and materialise; neither may buy, own or close Synthesis.
'''
lxv = replace_section(lxv, '## 12. Su Majestad es la Síntesis', '## 13.', es65)
lxv = replace_section(lxv, '## 12. Her Majesty is Synthesis', '## 13.', en65)
lxv = bump_version(lxv, '1.1')
write(lxv_path, lxv)

# -----------------------------------------------------------------------------
# C. Neoaxiomatic review: surface candidates, do not silently canonise
# -----------------------------------------------------------------------------
nax_path = 'neoaxiomas/README.md'
nax = read(nax_path)
nax = nax.replace('**Marco / Framework:** **NEOCore™ 7.1 · Filosofía Arquetípica Neodialéctica™**', '**Marco / Framework:** **NEOCore™ 7.2 · Filosofía Arquetípica Neodialéctica™**')
A = '<!-- NEOAXIOM_CANDIDATES_72_START -->'
B = '<!-- NEOAXIOM_CANDIDATES_72_END -->'
candidates = f'''{A}

## Candidatos neoaxiomáticos detectados en el repaso I–LXVIII / Neoaxiomatic candidates detected in the I–LXVIII review

**Estado:** candidatos visibles para SAN™; **no se promueven automáticamente a NAX-15+**. / **Status:** visible candidates for SAN™; **not automatically promoted to NAX-15+**.

| Candidato / Candidate | Procedencia / Provenance | Estado / Status |
|---|---|---|
| **C-NAX-15 · Soberanía Intelectual de la Especie™ / Intellectual Sovereignty of the Species™** | [LXVIII](../manifiestos/68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md) | **Candidato explícito** en LXVIII; pendiente de contraste suficiente / **Explicit candidate** in LXVIII; pending sufficient scrutiny |
| **C-NAX-16 · No Coronación de la Parte™ / Non-Crowning of the Part™** | [LXII](../manifiestos/62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md) + [∞](../manifiestos/INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md) | Candidato 7.2: persona, IA, Fundación, Corporación, mayoría o subsistema no equivalen al Todo / 7.2 candidate: person, AI, Foundation, Corporation, majority or subsystem do not equal the Whole |
| **C-NAX-17 · Reconstrucción Sistémica™ / Systemic Reconstruction™** | [LXVII](../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md) | Principio manifiesto; candidato a evaluación, no canonizado / Manifest principle; candidate for evaluation, not canonicalised |
| **C-NAX-18 · Motor del Bien Común + NeoSinergia™ / Common-Good Engine + NeoSynergy™** | [LXVI](../manifiestos/66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md) + [LXVII](../manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md) | Candidato relacional a síntesis; no convierte cooperación en coerción / Relational synthesis candidate; does not turn cooperation into coercion |

**Regla 7.2 / 7.2 rule:** la futura **Innova_N Fundación** puede custodiar propósito, memoria y Bien Común; la futura **Innova_N Corporación** puede materializar infraestructura y sostenibilidad. Ninguna adquiere soberanía epistemológica por su forma jurídica. Ambas quedan subordinadas a gobernanza humana, legalidad, trazabilidad, auditoría y SAN™. / the future **Innova_N Foundation** may guard purpose, memory and the Common Good; the future **Innova_N Corporation** may materialise infrastructure and sustainability. Neither acquires epistemic sovereignty through legal form. Both remain subject to human governance, law, traceability, audit and SAN™.

{B}
'''
if A in nax and B in nax:
    nax = re.sub(re.escape(A) + r'.*?' + re.escape(B), candidates.strip(), nax, count=1, flags=re.S)
else:
    nax = nax.replace('\n# ES · Castellano', '\n' + candidates + '\n# ES · Castellano', 1)
write(nax_path, nax)

# -----------------------------------------------------------------------------
# D. Upgrade living version generator to cumulative 7.2
# -----------------------------------------------------------------------------
gen_path = '.github/scripts/sync_latest_manifesto_feature.py'
gen = read(gen_path)
gen = gen.replace("CURRENT_VERSION = '7.1'", "CURRENT_VERSION = '7.2'")
gen = gen.replace('## NEOCore™ {CURRENT_VERSION} · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™', '## NEOCore™ {CURRENT_VERSION} · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™')
gen = gen.replace('## NEOCore™ {CURRENT_VERSION} · First Fractal Multihead Layer™ + Neoaxiomatic Layer™', '## NEOCore™ {CURRENT_VERSION} · First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™')
write(gen_path, gen)

# -----------------------------------------------------------------------------
# E. WEB4 public projection
# -----------------------------------------------------------------------------
wman_path = 'web4/manifiestos/index.html'
wman = read(wman_path)
extra = "['LXI','Contra el Reduccionismo Matemático™ y Custodia Experimental Multiescalar™','61_contra_reduccionismo_matematico_custodia_experimental_multiescalar_ES_EN.md'],['LXII','Juego por la Síntesis y el Honor™','62_juego_por_la_sintesis_y_el_honor_neowar_starkdr_ransol_ES_EN.md'],['LXIII','Contra la Simplificación Burda del Marco™','63_contra_simplificacion_burda_marco_fidelidad_compresion_ES_EN.md'],['LXIV','NeoCronos™','64_neocronos_tokenizacion_aporte_sintesis_abierta_ES_EN.md'],['LXV','NeoJuego™','65_neojuego_bien_comun_tokenizado_honor_aporte_ES_EN.md'],['LXVI','NeoSinergia™','66_neosinergia_neowar_activa_medici_leonidas_cancerbero_ES_EN.md'],['LXVII','NeoTitanes™','67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md'],['LXVIII','Los Conflictos que No Son Nuestros™ · Soberanía Intelectual de la Especie','68_conflictos_que_no_son_nuestros_soberania_intelectual_especie_ES_EN.md'],['∞','Neo0™ · Puerta Abierta del Fractal','INFINITO_neo0_puerta_abierta_fractal_leonidas_ES_EN.md']"
if "['LXI','Contra el Reduccionismo" not in wman:
    pat = re.compile(r"(\['LX','Relevancia Humana Necesaria™','60_relevancia_humana_necesaria_inteligencia_distribuida_aporte_anti_captura_social_ES_EN\.md'\])(\]\]\.map)")
    wman, n = pat.subn(r"\1," + extra + r"\2", wman, count=1)
    if n != 1:
        raise RuntimeError('WEB4 manifesto array extension failed')
wman = wman.replace("function boot(){status.textContent=M.length+' manifiestos · I–LX · registro explícito';", "function boot(){status.textContent='68 manifiestos finitos · I–LXVIII + ∞ · NEOCore™ 7.2';")
oldhero = '<main><section class="hero"><div class="wrap"><span class="status" id="status">Registro canónico integrado</span><h1>Manifiestos en la propia web.</h1><p>El lector usa un registro explícito de número romano → ruta real. No deduce nombres por prefijos históricos. Si la descarga RAW falla, reintenta mediante la API pública de GitHub; si ambos fallan, muestra el error y el vínculo canónico en lugar de quedar vacío.</p></div></section>'
newhero = '<main><section class="hero"><div class="wrap"><span class="status" id="status">Registro canónico integrado</span><h1>Manifiestos en la propia web.</h1><p><strong>NEOCore™ 7.2</strong> proyecta aquí I–LXVIII + ∞. La v7.2 conserva la Primera Capa Fractal Multicabeza™ y la Capa Neoaxiomática™, e incorpora la Soberanía de Síntesis™, la diferenciación futura Innova_N Fundación / Corporación y la actualización de NeoSinergia™, NeoTitanes™ y Soberanía Intelectual de la Especie.</p><p>Esta página es una <strong>DEMO / proyección pública WEB4™ · SistemaTrazable™</strong>, no la implementación definitiva. El lector usa un registro explícito de número romano → ruta real. Si la descarga RAW falla, reintenta mediante la API pública de GitHub; si ambos fallan, muestra el error y el vínculo canónico en lugar de quedar vacío.</p><p><a href="/neocronos/">NeoCronos™</a> · <a href="https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/blob/main/neoaxiomas/README.md" target="_blank">Neoaxiomas™ ↗</a> · <a href="#∞">Puerta ∞</a></p></div></section>'
if oldhero in wman:
    wman = wman.replace(oldhero, newhero, 1)
write(wman_path, wman)

wneo_path = 'web4/neocronos/index.html'
wneo = read(wneo_path)
wneo = wneo.replace('<div class="badge">DEMO / prototipo público WEB4™</div>', '<div class="badge">DEMO / prototipo público WEB4™ · NEOCore™ 7.2</div>')
wneo = wneo.replace('El tiempo registrado no genera tokens, dinero ni participación de forma automática.</p>', 'El tiempo registrado no genera tokens, dinero ni participación de forma automática. <strong>La medición es experimental, multidimensional y revisable: NeoCronos™ no es una puntuación absoluta de una persona ni una métrica incuestionable de valor.</strong></p>', 1)
wneo = wneo.replace('<strong>¿Qué significa WEB4™ · SistemaTrazable™?</strong>', '<strong>¿Qué significa WEB4™ · SistemaTrazable™ en NEOCore™ 7.2?</strong>', 1)
write(wneo_path, wneo)

web4_readme = '''# WEB4™ · SistemaTrazable™ · Proyección pública

**Estado:** DEMO / prototipo público, no implementación definitiva.  
**Marco actual:** NEOCore™ 7.2.  
**Fecha:** 2026-08-10.

## Superficies públicas actuales

- [`manifiestos/`](./manifiestos/) — lector WEB4™ de I–LXVIII + ∞ con retorno a la fuente GitHub.
- [`neocronos/`](./neocronos/) — DEMO local de NeoCronos™ dentro de una aportación de Síntesis Abierta.
- [`../propuestas/sintesis-abierta/`](../propuestas/sintesis-abierta/README.md) — protocolo y memoria pública de SAN™.
- [`../neoaxiomas/`](../neoaxiomas/README.md) — capa Neoaxiomática abierta y candidatos detectados.

## Delta 7.2

NEOCore™ 7.2 conserva la Primera Capa Fractal Multicabeza™ y la Capa Neoaxiomática™ e incorpora una capa explícita de **Soberanía de Síntesis™**: ninguna persona, IA, Fundación, Corporación, mayoría o subsistema equivale al Todo.

La futura **Innova_N Fundación** se proyecta como custodia de propósito, memoria y Bien Común; la futura **Innova_N Corporación**, como materialización operativa, infraestructura y sostenibilidad. Ambas son vehículos bajo gobernanza humana, legalidad, trazabilidad, auditoría y SAN™.

NeoCronos™ permanece experimental: mide y conserva trazas de aportes, no asigna por sí solo verdad, valor económico, tokens ni rango humano.

[Delta completo NEOCore™ 7.2](../proyeccion/NEOCORE_7_2_DELTA_ES_EN.md)
'''
write('web4/README.md', web4_readme)

# -----------------------------------------------------------------------------
# F. Version delta and visible root pointers
# -----------------------------------------------------------------------------
delta_path = 'proyeccion/NEOCORE_7_2_DELTA_ES_EN.md'
delta = '''# NEOCore™ 7.2 · Soberanía de Síntesis™, Institucionalización Dual y Proyección WEB4™
# NEOCore™ 7.2 · Synthesis Sovereignty™, Dual Institutionalisation and WEB4™ Projection

**Fecha / Date:** 2026-08-10  
**Estado / Status:** fijación documental de versión · abierta a SAN™ / documentary version fixation · open to SAN™  
**Versión anterior / Previous version:** NEOCore™ 7.1  
**Naturaleza / Nature:** delta acumulativo; no borra la genealogía 7.1 / cumulative delta; it does not erase 7.1 genealogy.

## ES · Castellano

NEOCore™ 7.2 conserva la **Primera Capa Fractal Multicabeza™** y la **Capa Neoaxiomática™** de 7.1 y añade una formulación explícita de **Soberanía de Síntesis™**.

### 1. Su Majestad es la Síntesis

La frase se fija como regla simbólica anticaptura: ninguna parte puede coronarse Todo. Neo0™ mantiene origen humano, guía teleológica y responsabilidad de fijación; Harry asiste relación y contraste; ninguna función sustituye a la Síntesis.

### 2. Innova_N futura: Fundación + Corporación

Se diferencia la futura arquitectura institucional:

- **Fundación:** propósito, memoria, Bien Común, continuidad y custodia de misión;
- **Corporación:** infraestructura, investigación, productos, servicios, empleo, despliegue y sostenibilidad.

No son soberanos epistemológicos. Son vehículos institucionales sujetos a gobernanza humana, legalidad, trazabilidad, auditoría, impugnación y SAN™.

### 3. Corpus recuperado

El índice vivo se sincroniza a **68 manifiestos finitos · I–LXVIII + ∞**. Se incorporan a la red canónica LXVI · NeoSinergia™, LXVII · NeoTitanes™, LXVIII · Soberanía Intelectual de la Especie y ∞ v1.3.

### 4. Neoaxiomas faltantes: visibilidad sin canonización automática

El repaso registra como candidatos —no como NAX canónicos nuevos— Soberanía Intelectual de la Especie™, No Coronación de la Parte™, Reconstrucción Sistémica™ y Motor del Bien Común + NeoSinergia™.

### 5. WEB4™

La proyección pública WEB4™ se actualiza para leer I–LXVIII + ∞ y mostrar el estado 7.2. NeoCronos™ queda expresamente descrito como mecanismo experimental, multidimensional y revisable de traza del aporte, no como puntuación absoluta ni asignación automática de tokens o dinero.

## EN · English

NEOCore™ 7.2 preserves the **First Fractal Multihead Layer™** and **Neoaxiomatic Layer™** of 7.1 and adds an explicit **Synthesis Sovereignty™** formulation.

### 1. Her Majesty is Synthesis

The phrase is fixed as a symbolic anti-capture rule: no part may crown itself as the Whole. Neo0™ preserves human origin, teleological guidance and fixation responsibility; Harry assists relation and scrutiny; no function replaces Synthesis.

### 2. Future Innova_N: Foundation + Corporation

The future institutional architecture is differentiated:

- **Foundation:** purpose, memory, Common Good, continuity and mission custody;
- **Corporation:** infrastructure, research, products, services, employment, deployment and sustainability.

They are not epistemic sovereigns. They are institutional vehicles subject to human governance, law, traceability, audit, challengeability and SAN™.

### 3. Recovered corpus

The living index is synchronised to **68 finite manifestos · I–LXVIII + ∞**: LXVI NeoSynergy™, LXVII NeoTitans™, LXVIII Intellectual Sovereignty of the Species and ∞ v1.3.

### 4. Missing Neoaxioms: visibility without automatic canonisation

The review registers Intellectual Sovereignty of the Species™, Non-Crowning of the Part™, Systemic Reconstruction™, and Common-Good Engine + NeoSynergy™ as candidates, not silently promoted canonical NAX entries.

### 5. WEB4™

The public WEB4™ projection is updated to read I–LXVIII + ∞ and display state 7.2. NeoCronos™ remains explicitly experimental, multidimensional and revisable contribution tracing, not an absolute score or automatic assignment of tokens or money.

---

**Principio de continuidad / Continuity principle:** 7.2 añade relaciones y corrige desincronizaciones; no reescribe como actuales los documentos históricos que fijaron 7.1 en su fecha. / 7.2 adds relations and repairs desynchronisation; it does not rewrite historical documents that recorded 7.1 as their then-current state.
'''
write(delta_path, delta)

root_delta = '''<!-- NEOCORE_72_DELTA_START -->

## NEOCore™ 7.2 · Delta actual / Current delta

**Soberanía de Síntesis™ + Innova_N Fundación/Corporación futuras + corpus I–LXVIII + ∞ + WEB4™ actualizado.**  
La Fundación custodiará propósito y Bien Común; la Corporación materializará infraestructura y sostenibilidad; ninguna sustituye a la Síntesis. NeoCronos™ permanece experimental y revisable. / The Foundation will guard purpose and the Common Good; the Corporation will materialise infrastructure and sustainability; neither replaces Synthesis. NeoCronos™ remains experimental and revisable.

**[Leer delta 7.2 / Read 7.2 delta](proyeccion/NEOCORE_7_2_DELTA_ES_EN.md)** · **[WEB4™](web4/README.md)** · **[Neoaxiomas™](neoaxiomas/README.md)**

<!-- NEOCORE_72_DELTA_END -->'''
for path in ['README.md', 'LEEME.md']:
    text = read(path)
    if '<!-- NEOCORE_72_DELTA_START -->' in text:
        text = re.sub(r'<!-- NEOCORE_72_DELTA_START -->.*?<!-- NEOCORE_72_DELTA_END -->', root_delta, text, count=1, flags=re.S)
    else:
        anchor = '<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'
        text = text.replace(anchor, anchor + '\n\n' + root_delta, 1) if anchor in text else root_delta + '\n\n' + text
    write(path, text)

# -----------------------------------------------------------------------------
# G. Rebuild derived network using repository's own canonical mechanisms
# -----------------------------------------------------------------------------
for script in [
    '.github/scripts/sync_canonical_manifestos.py',
    '.github/scripts/sync_manifesto_crossrefs.py',
    '.github/scripts/sync_canonical_manifestos.py',
    '.github/scripts/sync_latest_manifesto_feature.py',
    '.github/scripts/sync_open_synthesis_manifestos.py',
    '.github/scripts/normalize_manifesto_indices.py',
    '.github/scripts/sync_canonical_manifestos.py',
]:
    p = rp(script)
    if p.exists():
        print('RUN', script)
        subprocess.run([sys.executable, str(p)], check=True)

# -----------------------------------------------------------------------------
# H. Final MAXPROC-style postcheck
# -----------------------------------------------------------------------------
idx = read('manifiestos/README.md')
entries = re.findall(r'^- \*\*([IVXLCDM]+)\*\* · \[[^\]]+\]\(([^)]+\.md)\)', idx, re.M)
reg = json.loads(read(reg_path))['entries']
missing_legacy = [(r,e['legacy']) for r,e in reg.items() if not rp(e['legacy']).exists()]
missing_canon = [(r,e['canonical']) for r,e in reg.items() if not rp(e['canonical']).exists()]
explicit_candidates = []
for f in sorted(rp('manifiestos').glob('*.md')):
    s = f.read_text(encoding='utf-8')
    if re.search(r'Neoaxioma candidato|Candidate Neoaxiom', s, re.I):
        explicit_candidates.append(f.name)

inf = read(inf_path)
wman = read(wman_path)
wneo = read(wneo_path)
root_readme = read('README.md')
nax = read(nax_path)
checks = {
    'manifest_index_count_68': len(entries) == 68,
    'manifest_index_latest_LXVIII': bool(entries and entries[-1][0] == 'LXVIII'),
    'registry_has_LXVII_LXVIII': all(x in reg for x in ['LXVII','LXVIII']),
    'missing_legacy_zero': not missing_legacy,
    'missing_canonical_zero': not missing_canon,
    'infinity_has_future_foundation': 'Innova_N Fundación' in inf and 'Innova_N Foundation' in inf,
    'infinity_has_future_corporation': 'Innova_N Corporación' in inf and 'Innova_N Corporation' in inf,
    'infinity_has_non_crowning_candidate': 'No Coronación de la Parte™' in inf and 'Non-Crowning of the Part™' in inf,
    'neoaxiom_candidates_visible': 'C-NAX-15' in nax and 'C-NAX-18' in nax,
    'web4_manifest_LXVIII_infinity': "['LXVIII'" in wman and "['∞'" in wman,
    'web4_neocore_72': 'NEOCore™ 7.2' in wman and 'NEOCore™ 7.2' in wneo,
    'neocronos_experimental': 'experimental' in wneo.lower() and 'puntuación absoluta' in wneo,
    'root_current_72': 'NEOCore™ 7.2' in root_readme,
}
status = 'OK' if all(checks.values()) else 'REQUIERE CORRECCIÓN'
lines = [
    '# Postcheck · NEOCore™ 7.2 · Soberanía de Síntesis y WEB4™ / Postcheck', '',
    '**Fecha / Date:** 2026-08-10  ',
    f'**Estado / Status:** **{status}**  ',
    f'**Manifiestos finitos detectados / Finite manifestos detected:** **{len(entries)} · I–{entries[-1][0] if entries else "?"}**  ',
    '**Puerta permanente / Permanent gate:** ∞', '',
    '## Resultados / Results', '',
]
for key, ok in checks.items():
    lines.append(f'- [{"x" if ok else " "}] `{key}`')
lines += [
    '', '## Registro canónico / Canonical registry', '',
    f'- Entradas / Entries: **{len(reg)}**',
    f'- Legacy ausentes / Missing legacy: **{len(missing_legacy)}**',
    f'- Canónicos derivados ausentes / Missing derived canonicals: **{len(missing_canon)}**',
    '', '## Neoaxiomas candidatos / Candidate Neoaxioms', '',
]
lines += [f'- `{x}`' for x in explicit_candidates] or ['- Ninguna marca explícita detectada / No explicit marker detected']
lines += [
    '',
    'La revisión 7.2 registra además como candidatos visibles —sin promoción automática— No Coronación de la Parte™, Reconstrucción Sistémica™ y Motor del Bien Común + NeoSinergia™. / The 7.2 review also registers Non-Crowning of the Part™, Systemic Reconstruction™, and Common-Good Engine + NeoSynergy™ as visible candidates without automatic promotion.',
    '', '## Criterio institucional / Institutional criterion', '',
    'La futura Innova_N Fundación y la futura Innova_N Corporación quedan diferenciadas como vehículos de custodia y materialización. Ninguna equivale a la Síntesis ni adquiere soberanía epistemológica por su forma jurídica. / The future Innova_N Foundation and Corporation are differentiated as custody and materialisation vehicles. Neither equals Synthesis nor gains epistemic sovereignty through legal form.',
    '', '## WEB4™', '',
    '- Lector de manifiestos: I–LXVIII + ∞.',
    '- NeoCronos™: DEMO experimental, multidimensional y revisable.',
    '- WEB4™ sigue presentado como proyección/prototipo público, no implementación definitiva.',
    '',
    '**No se modificaron auditorías históricas cuyo objeto era fijar el estado 7.1 en su fecha.** / **Historical audits whose purpose was to record the 7.1 state at their date were not rewritten.**',
    ''
]
if missing_legacy:
    lines += ['### Missing legacy', ''] + [f'- {r}: `{p}`' for r,p in missing_legacy]
if missing_canon:
    lines += ['### Missing canonical', ''] + [f'- {r}: `{p}`' for r,p in missing_canon]
audit_path = 'auditorias/publicas/2026-08-10_postcheck_neocore_7_2_soberania_sintesis_web4_ES_EN.md'
write(audit_path, '\n'.join(lines))

print('CHECKS')
for k,v in checks.items(): print(k, v)
print('EXPLICIT_CANDIDATE_FILES', explicit_candidates)
if status != 'OK':
    raise SystemExit('POSTCHECK 7.2 FAIL')
print('POSTCHECK 7.2 OK')
