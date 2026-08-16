from pathlib import Path
import re

ROOT = Path('.').resolve()
README = ROOT / 'neoaxiomas/README.md'
AUDIT = ROOT / '.github/scripts/audit_neoaxiom_registry_integrity.py'
DELTA = ROOT / 'propuestas/sintesis-abierta/2026-08-16_DELTA_PODER_TRAZABILIDAD_ESCRUTINIO_EVIDENCIA_ES_EN.md'

ACCESS = {
1: {
'es_plain': 'El sistema puede compartir un mismo propósito y criterios sin concentrar toda la ejecución en una sola persona, IA o máquina. La dirección común pertenece al sentido; la capacidad de actuar puede repartirse entre muchos nodos.',
'es_example': 'Una red de respuesta ante incendios puede compartir el mismo objetivo, protocolos de seguridad y criterios de prioridad, mientras equipos locales, sensores e IAs ejecutan tareas distintas cerca de donde ocurre cada problema. Coordinar no exige que todo pase por una única máquina o autoridad operativa.',
'en_plain': 'The system may share a common purpose and criteria without concentrating all execution in a single person, AI or machine. Common direction belongs to meaning; the capacity to act may be distributed across many nodes.',
'en_example': 'A wildfire-response network may share the same goal, safety protocols and priority criteria while local teams, sensors and AIs perform different tasks close to each problem. Coordination does not require every action to pass through one machine or operational authority.'
},
2: {
'es_plain': 'Cuando el conocimiento relevante está repartido entre historias, hilos o especialidades distintas, una síntesis importante no debería depender de una sola lectura. Primero se recuperan varias cabezas independientes; después se comparan sus aportes.',
'es_example': 'Para revisar una nueva arquitectura WEB4, una cabeza puede releer la genealogía técnica, otra los manifiestos, otra las reglas de trazabilidad y otra la experiencia visual. Cada una devuelve lo que ve desde su propia memoria antes de que SAN intente recomponer el conjunto.',
'en_plain': 'When relevant knowledge is distributed across different histories, threads or specialities, an important synthesis should not depend on a single reading. Several independent heads are recovered first; their contributions are compared afterwards.',
'en_example': 'When reviewing a new WEB4 architecture, one head may reread technical genealogy, another the Manifestos, another traceability rules and another the visual experience. Each returns what it sees from its own memory before SAN attempts to recompose the whole.'
},
3: {
'es_plain': 'Las perspectivas independientes no deben corregirse para que coincidan antes de compararlas. El desacuerdo puede contener información útil; si lo borramos demasiado pronto, perdemos señal.',
'es_example': 'Si tres revisores estudian si ejecutar IA en local es más ecológico, deben registrar por separado sus datos y conclusiones, aunque discrepen. Sólo después se contrastan consumo, ciclo de vida y contexto; obligarlos a coincidir antes falsearía la síntesis.',
'en_plain': 'Independent perspectives should not be corrected to agree before they are compared. Disagreement may contain useful information; erasing it too early destroys signal.',
'en_example': 'If three reviewers study whether running AI locally is more ecological, they should record their data and conclusions separately even when they disagree. Energy use, life cycle and context are compared afterwards; forcing agreement first would distort the synthesis.'
},
4: {
'es_plain': 'Para comprender algo complejo, el sistema primero abre el problema en partes y perspectivas y después vuelve a reunirlas. La síntesis superior debe conservar el camino de vuelta a las partes que la hicieron posible.',
'es_example': 'Un proyecto energético puede separarse en análisis técnico, ambiental, económico y social. Después se recomponen en una propuesta común, pero cada conclusión sigue enlazada a los informes y datos de los que salió. Esa síntesis puede convertirse a su vez en una pieza de una síntesis mayor.',
'en_plain': 'To understand something complex, the system first opens the problem into parts and perspectives and then recomposes them. A higher synthesis must preserve the path back to the parts that made it possible.',
'en_example': 'An energy project may be separated into technical, environmental, economic and social analyses. They are then recomposed into a common proposal, while every conclusion remains linked to the reports and data from which it arose. That synthesis may itself become one part of a higher synthesis.'
},
5: {
'es_plain': 'Una buena revisión no necesita repetir todo el marco: debe señalar qué aporta de nuevo, qué falta, qué contradice y de dónde sale. Comprimir está permitido; perder el camino a la fuente, no.',
'es_example': 'Al revisar un nuevo manifiesto, una cabeza puede devolver: “esta idea ya existe en NAX-08; falta relacionarla con C-NAX-26; aquí hay una contradicción con el Issue X”. Cada diferencia lleva enlace a la fuente para que otra persona pueda reconstruir el razonamiento.',
'en_plain': 'A good review does not need to repeat the entire framework: it should identify what is new, what is missing, what contradicts something else and where it comes from. Compression is allowed; losing the path to the source is not.',
'en_example': 'When reviewing a new Manifesto, a head may return: “this idea already exists in NAX-08; the relation to C-NAX-26 is missing; here there is a contradiction with Issue X”. Each difference links back to its source so another person can reconstruct the reasoning.'
},
6: {
'es_plain': 'Saber que algo importante falta también es conocimiento. Una ausencia documentada debe quedar registrada para poder investigarla, pero detectar la ausencia no obliga automáticamente a restaurar lo que había.',
'es_example': 'Si antiguos commits y documentos muestran un proyecto que ya no aparece en el índice actual, el sistema puede registrar “proyecto histórico ausente de la representación vigente” con sus fuentes. SAN decidirá después si debe recuperarse, archivarse o mantenerse sólo como genealogía.',
'en_plain': 'Knowing that something important is missing is also knowledge. A documented absence should be recorded so it can be investigated, but detecting the absence does not automatically require restoring what used to be there.',
'en_example': 'If old commits and documents show a project that no longer appears in the current index, the system may record “historical project absent from the current representation” together with its sources. SAN can later decide whether to restore it, archive it or keep it only as genealogy.'
},
7: {
'es_plain': 'Los actores que ejecutan acciones dentro del ecosistema deben dejar una traza reconstruible de la decisión y de su relación con el sistema. No hace falta explicar cada activación interna de una red neuronal; sí debe poder reconstruirse la acción que NEOCore incorpora.',
'es_example': 'Si un robot cierra una válvula, la capa NEOREAL debe poder relacionar qué sensor activó la decisión, qué versión de reglas o modelo intervino, qué actor tenía autoridad, qué acción se ejecutó y qué resultado produjo. No es necesario traducir cada cálculo interno del modelo a lenguaje humano.',
'en_plain': 'Actors executing actions inside the ecosystem must leave a reconstructible trace of the decision and its relation to the system. Every internal activation of a neural network need not be explained; the action incorporated by NEOCore must be reconstructible.',
'en_example': 'If a robot closes a valve, the NEOREAL layer should be able to relate which sensor triggered the decision, which rule or model version intervened, which actor had authority, what action was executed and what result followed. It is not necessary to translate every internal model calculation into human language.'
},
8: {
'es_plain': 'Competir puede mejorar resultados, pero deja de ser útil cuando la competición destruye las condiciones compartidas que permiten vivir, crear o seguir compitiendo. La excelencia debe ocurrir dentro de límites y cooperación superiores.',
'es_example': 'Dos empresas pueden competir por fabricar baterías mejores y más baratas. Esa competencia deja de ser excelencia si una obtiene ventaja contaminando impunemente el agua común o bloqueando de forma extractiva una infraestructura necesaria para todos. La innovación permanece; la depredación no se convierte en regla.',
'en_plain': 'Competition may improve results, but it stops being useful when it destroys the shared conditions that allow people to live, create or continue competing. Excellence should operate inside higher limits and cooperation.',
'en_example': 'Two companies may compete to make better and cheaper batteries. That competition ceases to be excellence if one gains advantage by polluting shared water with impunity or extractively blocking infrastructure needed by everyone. Innovation remains; predation does not become the rule.'
},
9: {
'es_plain': 'Usar computación local o distribuida es una preferencia condicionada, no un dogma ecológico. Hay que medir el caso real y comparar energía, hardware, red, refrigeración y vida útil antes de decidir.',
'es_example': 'Ejecutar una tarea de IA en un ordenador local reutilizado puede ahorrar tráfico y aprovechar hardware ya existente, pero un centro de datos eficiente puede consumir menos energía por tarea. La decisión correcta sale de comparar ambos casos completos, no de asumir que “local” o “nube” siempre gana.',
'en_plain': 'Using local or distributed computing is a conditional preference, not an ecological dogma. The real case must be measured by comparing energy, hardware, network use, cooling and useful life before deciding.',
'en_example': 'Running an AI task on a reused local computer may reduce traffic and use existing hardware, while an efficient data centre may consume less energy per task. The correct decision comes from comparing both complete cases, not from assuming that “local” or “cloud” always wins.'
},
10: {
'es_plain': 'La gramática simbólica funciona como un mapa de responsabilidades y de relación con el mundo, no como una fuente automática de autoridad ni como una teoría científica cerrada. Las figuras de custodia recuerdan cómo actuar; la capa elemental recuerda la realidad material que se custodia y permanece abierta a la totalidad.',
'es_example': 'En el escudo, la Corona puede recordar responsabilidad de gobierno y el Águila visión de conjunto, sin conceder privilegio político por el símbolo. Agua, Fuego, Tierra, Madera y Metal hacen visible la dimensión material y transformadora del mundo sin afirmar que cinco elementos expliquen científicamente toda la realidad. La ampliación activa está documentada en [Fuego de Agua™ y Totalidad Elemental](./NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md).',
'en_plain': 'The symbolic grammar works as a map of responsibilities and relation to the world, not as an automatic source of authority or a closed scientific theory. Custodial figures recall how to act; the elemental layer recalls the material reality being cared for and remains open to totality.',
'en_example': 'In the shield, the Crown may recall responsibility for governance and the Eagle an overview, without granting political privilege through the symbol. Water, Fire, Earth, Wood and Metal make the material and transformative dimension of the world visible without claiming that five elements scientifically explain all reality. The active extension is documented in [WaterFire™ and Elemental Totality](./NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md).'
},
11: {
'es_plain': 'La inteligencia puede estar distribuida, pero eso no significa que cualquier IA o nodo pueda cambiar por sí solo el estado canónico. La decisión de fijación debe tener una autoridad humana identificable y quedar registrada; además, sigue siendo revisable.',
'es_example': 'Varias IAs pueden coincidir en que un Neoaxioma debería modificarse y aportar argumentos excelentes. Esa convergencia es una propuesta, no una fijación automática. El cambio entra en SAN y sólo pasa a estado canónico cuando la gobernanza humana vigente lo fija de forma trazable; una revisión posterior puede volver a corregirlo.',
'en_plain': 'Intelligence may be distributed, but that does not mean any AI or node may change canonical state by itself. Fixation must have identifiable human authority and be recorded; it also remains revisable.',
'en_example': 'Several AIs may agree that a Neoaxiom should be changed and provide excellent arguments. That convergence is a proposal, not automatic fixation. The change enters SAN and becomes canonical only when current human governance fixes it traceably; a later review may correct it again.'
},
12: {
'es_plain': 'Si el sistema ya puede demostrar de forma fiable quién hizo qué, con qué versión, controles y resultado, no debería obligar a repetir la misma prueba en formularios que no añaden seguridad. Pero una obligación legal o contractual vigente sigue cumpliéndose hasta que exista equivalencia reconocida.',
'es_example': 'Un despliegue de software puede registrar automáticamente versión, pruebas superadas, aprobador, fecha, incidencias y rollback. Si ese registro cubre realmente la función de control, copiar los mismos datos a otra hoja puede ser redundante. Si un regulador exige todavía un formulario concreto, se mantiene hasta que acepte una vía equivalente.',
'en_plain': 'If the system can already prove reliably who did what, with which version, controls and result, people should not be forced to repeat the same evidence in forms that add no safety. But a current legal or contractual obligation still applies until recognised equivalence exists.',
'en_example': 'A software deployment may automatically record version, passed tests, approver, date, incidents and rollback. If that record genuinely covers the control function, copying the same data into another sheet may be redundant. If a regulator still requires a specific form, it remains in use until an equivalent route is recognised.'
},
13: {
'es_plain': 'Eliminar control redundante no tiene como único objetivo ahorrar dinero. El tiempo y la capacidad liberados deberían volver a tareas que crean, cuidan, investigan, reparan o mejoran el conocimiento común.',
'es_example': 'Si una ingeniera deja de copiar manualmente los mismos datos de una entrega en tres sistemas porque la traza ya es automática y auditable, el tiempo recuperado puede dedicarse a probar fallos difíciles, documentar aprendizajes o mejorar el producto. Ahorrar el trámite sólo tiene sentido si la capacidad liberada se usa mejor.',
'en_plain': 'Removing redundant control is not only about saving money. The time and capacity released should return to work that creates, cares, researches, repairs or improves shared knowledge.',
'en_example': 'If an engineer no longer copies the same release data manually into three systems because the trace is already automatic and auditable, the recovered time can be used to test difficult failures, document learning or improve the product. Removing the procedure matters because the released capacity can be used better.'
},
14: {
'es_plain': 'Si sólo una minoría puede usar bien IA avanzada, la diferencia de acceso puede multiplicar desigualdades de aprendizaje, trabajo, creación y defensa de derechos. El objetivo es ampliar acceso y alfabetización crítica sin obligar a todos a usar la misma IA.',
'es_example': 'Si estudiantes con muchos recursos tienen tutores de IA potentes y formación para verificarlos mientras otros no tienen ni acceso ni alfabetización, la brecha no es sólo tecnológica: se acumula en aprendizaje y oportunidades. Acceso progresivo, educación crítica y protección frente a dependencia reducen esa bifurcación.',
'en_plain': 'If only a minority can use advanced AI well, differences in access may multiply inequalities in learning, work, creation and defence of rights. The goal is to broaden access and critical literacy without forcing everyone to use the same AI.',
'en_example': 'If well-resourced students have powerful AI tutors and training to verify them while others have neither access nor literacy, the gap is not merely technological: it compounds through learning and opportunity. Progressive access, critical education and safeguards against dependency reduce that bifurcation.'
}
}


def inject_language(body, lang):
    matches = list(re.finditer(r'^##\s+NAX-(\d+)\s+·.*$', body, re.M))
    rebuilt = []
    cursor = 0
    for i, m in enumerate(matches):
        n = int(m.group(1))
        if n not in ACCESS:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        block = body[m.start():end]
        rebuilt.append(body[cursor:m.start()])
        marker_start = f'<!-- NAX-{n:02d}_ACCESS_{lang}_START -->'
        marker_end = f'<!-- NAX-{n:02d}_ACCESS_{lang}_END -->'
        a = ACCESS[n]
        if lang == 'ES':
            layer = f'''{marker_start}

**En sencillo:** {a['es_plain']}

**Ejemplo:** {a['es_example']}

> **Capa pedagógica:** esta lectura facilita comprensión; no sustituye ni modifica la formulación canónica, su estado, genealogía o Síntesis Abierta.

{marker_end}
'''
            status_pattern = r'^\*\*Estado:\*\*'
        else:
            layer = f'''{marker_start}

**In plain language:** {a['en_plain']}

**Example:** {a['en_example']}

> **Pedagogical layer:** this reading supports understanding; it neither replaces nor modifies the canonical formulation, its status, genealogy or Open Synthesis.

{marker_end}
'''
            status_pattern = r'^\*\*Status:\*\*'
        if marker_start in block and marker_end in block:
            block = re.sub(re.escape(marker_start) + r'.*?' + re.escape(marker_end) + r'\n?', layer.strip() + '\n', block, flags=re.S)
        else:
            status = re.search(status_pattern, block, re.M)
            if not status:
                raise SystemExit(f'NAX-{n:02d} {lang}: status insertion point not found')
            block = block[:status.start()].rstrip() + '\n\n' + layer + '\n' + block[status.start():]
        rebuilt.append(block)
        cursor = end
    rebuilt.append(body[cursor:])
    return ''.join(rebuilt)


def update_readme():
    text = README.read_text(encoding='utf-8')
    es_tag = '# ES · Castellano'
    en_tag = '# EN · English'
    if es_tag not in text or en_tag not in text:
        raise SystemExit('Canonical ES/EN split missing')
    prefix, rest = text.split(es_tag, 1)
    es_body, en_body = rest.split(en_tag, 1)
    es_body = inject_language(es_body, 'ES')
    en_body = inject_language(en_body, 'EN')
    rule = '> **Regla de accesibilidad canónica / Canonical accessibility rule:** la formulación y desarrollo formal de NAX-01–NAX-14 conservan autoridad documental; cada NAX incorpora además una lectura sencilla y un ejemplo simétricos ES/EN que no pueden ampliar ni reducir el canon. / the formal formulation and development of NAX-01–NAX-14 retain documentary authority; each NAX also includes a symmetric ES/EN plain-language reading and example that may neither expand nor narrow the canon.\n\n'
    if 'Regla de accesibilidad canónica / Canonical accessibility rule' not in prefix:
        anchor = '> **Regla heredada de integridad no reductiva:**'
        # The inherited rule sits after the ES split, so insert immediately after ES heading instead.
        es_body = '\n\n' + rule + es_body.lstrip('\n')
    README.write_text(prefix + es_tag + es_body + en_tag + en_body, encoding='utf-8')


def update_delta_symmetry():
    text = DELTA.read_text(encoding='utf-8')
    es_rel = '''## XVI. Relaciones canónicas

- [LIII · Leónidas™](../../manifiestos/53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md)
- [LXXII · El Hombre Custodio™ / The Custodian Man™](../../manifiestos/72_hombre_custodio_fuerza_deseo_poder_responsabilidad_ES_EN.md)
- [LXXIV · Asimetría de la Destrucción™ / Asymmetry of Destruction™](../../manifiestos/74_asimetria_destruccion_trol_humano_bot_ES_EN.md)
- [LXXVII · Contra la Polarización Binaria y la Radicalización Recíproca™ / Against Binary Polarisation and Reciprocal Radicalisation™](../../manifiestos/77_polarizacion_binaria_radicalizacion_reciproca_fenomeno_narrativa_ES_EN.md)
- [C-NAX-25 · Fenómeno ≠ Narrativa™ / Phenomenon ≠ Narrative™](./2026-08-16_C_NAX_25_FENOMENO_NO_ES_NARRATIVA_ES_EN.md)
- [C-NAX-26 · Poder ↑ → Trazabilidad ↑ · Acusación ↑ → Evidencia ↑ / Power ↑ → Traceability ↑ · Accusation ↑ → Evidence ↑](./2026-08-16_C_NAX_26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md)
- [Síntesis C-NAX-26 · #156](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/156)
- [Auditorías públicas / Public audits](../../auditorias/publicas/README.md)

**PROPUESTA ABIERTA ≠ CANON / OPEN PROPOSAL ≠ CANON.**
'''
    split = '\n---\n\n# EN · English'
    if split not in text:
        raise SystemExit('Delta ES/EN split not found')
    es, en = text.split(split, 1)
    if '## XVI. Relaciones canónicas' not in es:
        es = es.rstrip() + '\n\n' + es_rel.rstrip() + '\n'
    en = en.replace('## Relaciones canónicas / Canonical relations', '## XVI. Canonical relations')
    text = es + split + en
    DELTA.write_text(text, encoding='utf-8')


def harden_audit():
    text = AUDIT.read_text(encoding='utf-8')
    marker = "        if es_ids != en_ids:\n            problems.append(f'IDs NAX ES/EN no coinciden / ES/EN NAX IDs differ: ES={es_ids} EN={en_ids}')\n"
    addition = marker + "        for n in range(1, 15):\n            es_mark = f'<!-- NAX-{n:02d}_ACCESS_ES_START -->'\n            en_mark = f'<!-- NAX-{n:02d}_ACCESS_EN_START -->'\n            if es_mark not in es_body or en_mark not in en_body:\n                problems.append(f'NAX-{n:02d} carece de capa pedagógica simétrica ES/EN / lacks symmetric ES/EN pedagogical layer')\n"
    if 'NAX-{n:02d} carece de capa pedagógica' not in text:
        if marker not in text:
            raise SystemExit('Canonical audit insertion point not found')
        text = text.replace(marker, addition, 1)
    rule_anchor = "        '- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**',\n"
    canonical_rule = "        '- **Todo NAX canónico debe conservar formulación completa y añadir una capa pedagógica ES/EN simétrica sin sustituir el canon. / Every canonical NAX must preserve its complete formulation and add a symmetric ES/EN pedagogical layer without replacing the canon.**',\n"
    if 'Every canonical NAX must preserve its complete formulation' not in text:
        text = text.replace(rule_anchor, canonical_rule + rule_anchor, 1)
    AUDIT.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    update_readme()
    update_delta_symmetry()
    harden_audit()
    print('NAX_ACCESS_AND_SYMMETRY_REPAIR_OK canonical=14 delta_relations=paired')
