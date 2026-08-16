from pathlib import Path
import re

ROOT = Path('.').resolve()
README = ROOT / 'neoaxiomas/README.md'
AUDIT = ROOT / '.github/scripts/audit_neoaxiom_registry_integrity.py'
START = '<!-- NEOAXIOM_CANDIDATES_72_START -->'
END = '<!-- NEOAXIOM_CANDIDATES_72_END -->'

ACCESS = {
15: {
'es_plain': 'Ninguna persona, institución o IA debe poder convertirse en la única puerta para decidir qué puede conocer, pensar o discutir la sociedad. Cuanto mayor sea su poder cognitivo, más importantes son las fuentes visibles, las alternativas, la crítica, la posibilidad de disentir y la capacidad de salir o corregir.',
'es_example': 'Si una IA pasa a orientar decisiones públicas importantes, no basta con que sea muy eficaz. Sus recomendaciones deben poder contrastarse, recurrirse y compararse con otras fuentes o criterios; que la use mucha gente no la convierte en soberana del juicio colectivo.',
'en_plain': 'No person, institution or AI should become the only gateway deciding what society may know, think or discuss. The greater its cognitive power, the more important visible sources, alternatives, criticism, the ability to dissent and the real possibility of exit or correction become.',
'en_example': 'If an AI begins to guide important public decisions, high performance is not enough. Its recommendations must remain open to scrutiny, appeal and comparison with other sources or criteria; widespread use does not make it sovereign over collective judgement.'
},
16: {
'es_plain': 'Una parte puede ser muy importante sin convertirse en el Todo. Autor, fundador, mayoría, empresa, institución o IA pueden cumplir funciones decisivas, pero ninguna de esas posiciones convierte por sí sola su criterio en verdad final.',
'es_example': 'Si quien creó una teoría propone una interpretación y después aparece evidencia mejor que la contradice, la autoría obliga a conservar la genealogía de la idea, no a blindarla frente a revisión. La fuente importa; no sustituye a la Síntesis.',
'en_plain': 'A part may be very important without becoming the Whole. An author, founder, majority, company, institution or AI may perform decisive functions, but none of those positions automatically turns its judgement into final truth.',
'en_example': 'If the creator of a theory proposes an interpretation and better evidence later contradicts it, authorship requires preserving the idea’s genealogy, not shielding it from revision. The source matters; it does not replace Synthesis.'
},
17: {
'es_plain': 'Antes de destruir, restaurar o sustituir una estructura hay que entender qué funciones útiles cumple realmente, incluso si hoy funciona mal. La reconstrucción conserva lo necesario, corrige lo dañino y evita repetir el pasado o borrarlo sin comprenderlo.',
'es_example': 'Un trámite administrativo puede ser lento y redundante, pero quizá también deja constancia de quién decidió, permite recurrir y protege frente a abusos. Digitalizarlo bien significa eliminar la repetición innecesaria conservando esas funciones de prueba, responsabilidad y recurso.',
'en_plain': 'Before destroying, restoring or replacing a structure, we must understand which useful functions it actually performs, even if it currently works badly. Reconstruction preserves what is needed, corrects what is harmful and avoids either copying or erasing the past without understanding it.',
'en_example': 'An administrative procedure may be slow and repetitive, yet it may also record who decided, allow appeals and protect against abuse. Good digital replacement removes unnecessary repetition while preserving evidence, accountability and appeal.'
},
18: {
'es_plain': 'El Bien Común no exige que todos hagan lo mismo. Exige que capacidades distintas puedan coordinarse ante una necesidad real sin perder autonomía, derechos ni límites. Cuando alguien ha aceptado una función y puede ayudar de forma proporcionada, puede existir una responsabilidad concreta de cooperación, no una obediencia ilimitada.',
'es_example': 'Ante un apagón local, técnicos, administración, vecinos y sistemas de IA pueden aportar capacidades distintas bajo funciones claras. Cooperar para restaurar un servicio común no autoriza a ninguno a apropiarse de las decisiones ajenas ni a ampliar indefinidamente su poder.',
'en_plain': 'The Common Good does not require everyone to do the same thing. It requires different capabilities to coordinate around a real need without losing autonomy, rights or limits. When someone has accepted a function and can help proportionally, a concrete responsibility to cooperate may arise, not unlimited obedience.',
'en_example': 'During a local blackout, technicians, public authorities, residents and AI systems may contribute different capabilities under clear roles. Cooperating to restore a shared service does not authorise any participant to appropriate others’ decisions or expand its power indefinitely.'
},
19: {
'es_plain': 'Tener deseo, afecto, autoridad, acceso o una relación con otra persona no crea un derecho sobre ella. La legitimidad de la relación depende de dignidad, consentimiento válido, posibilidad real de negarse o salir y mayor responsabilidad cuando existe más poder.',
'es_example': 'La dependencia laboral de una persona respecto de su responsable no convierte esa dependencia en consentimiento para una relación personal. Si existe una asimetría de poder, debe aumentar el cuidado para que un sí sea realmente libre y un no no produzca represalias.',
'en_plain': 'Desire, affection, authority, access or an existing relationship with another person does not create a right over that person. A legitimate relationship depends on dignity, valid consent, a real ability to refuse or leave, and greater responsibility where greater power exists.',
'en_example': 'An employee’s dependence on a manager does not turn that dependence into consent to a personal relationship. Where a power asymmetry exists, safeguards must increase so that yes is genuinely free and no does not lead to retaliation.'
},
20: {
'es_plain': 'Compartimos una dignidad humana común y, al mismo tiempo, tenemos diferencias reales que no deben borrarse. Reconocer una identidad o necesidad concreta no significa reducir a la persona entera a esa etiqueta ni convertir una diferencia en razón para degradar a otros.',
'es_example': 'Adaptar un espacio para una persona con discapacidad reconoce una diferencia real sin definir a esa persona únicamente por su discapacidad. Del mismo modo, esa adaptación no requiere negar la dignidad o las necesidades legítimas de quienes no comparten esa condición.',
'en_plain': 'We share common human dignity while also having real differences that should not be erased. Recognising a specific identity or need does not mean reducing the whole person to that label or turning a difference into a reason to degrade others.',
'en_example': 'Adapting a space for a person with a disability recognises a real difference without defining that person only by the disability. Likewise, the accommodation does not require denying the dignity or legitimate needs of people who do not share that condition.'
},
21: {
'es_plain': 'Ser capaz de ganar, dominar, extraer o destruir no demuestra comprender mejor el sistema. Una acción puede ser eficaz a corto plazo y, sin embargo, ser torpe sistémicamente si destruye las condiciones de las que depende el conjunto.',
'es_example': 'Una empresa puede aumentar beneficios agotando un acuífero del que dependen la comunidad y su propia producción futura. El beneficio inmediato demuestra capacidad de extracción; no demuestra sabiduría sistémica.',
'en_plain': 'Being able to win, dominate, extract or destroy does not demonstrate better understanding of the system. An action may be effective in the short term yet systemically foolish if it destroys the conditions on which the whole depends.',
'en_example': 'A company may increase profits by exhausting an aquifer on which both the community and its own future production depend. Immediate profit demonstrates extraction capacity; it does not demonstrate systemic wisdom.'
},
22: {
'es_plain': 'La historia deja huellas físicas y relacionales. Un objeto, organismo, lugar o sistema puede conservar señales de lo que le ocurrió aunque no tenga memoria consciente. Esas huellas permiten reconstruir parte de su historia y pueden perderse si destruimos el soporte.',
'es_example': 'Los anillos y cicatrices de un árbol pueden mostrar sequías, incendios o daños anteriores. El árbol no “recuerda” como una persona, pero su materia conserva información relacional que ayuda a reconstruir su historia.',
'en_plain': 'History leaves physical and relational traces. An object, organism, place or system may preserve signs of what happened to it without having conscious memory. Those traces help reconstruct part of its history and may be lost when the supporting material is destroyed.',
'en_example': 'Tree rings and scars may reveal previous droughts, fires or damage. The tree does not “remember” like a person, but its material state preserves relational information that helps reconstruct its history.'
},
23: {
'es_plain': 'Corregir una injusticia no debería consistir en invertirla y conceder al otro lado permiso permanente para degradar. Puede haber protecciones asimétricas legítimas, pero deben reparar el sistema común y limitar el daño, no crear una nueva impunidad.',
'es_example': 'Si una persona ha sufrido acoso, protegerla puede exigir separar al agresor, imponer límites y reparar el daño. Esa protección no convierte en legítima una humillación permanente del otro: la finalidad es restaurar seguridad, responsabilidad y convivencia, no cambiar quién tiene licencia para destruir.',
'en_plain': 'Correcting an injustice should not mean reversing it and granting the other side permanent permission to degrade. Legitimate asymmetric protections may be necessary, but they should repair the common system and limit harm rather than create a new impunity.',
'en_example': 'If a person has suffered harassment, protection may require separating the aggressor, imposing limits and repairing harm. That protection does not make permanent humiliation of the other person legitimate: the aim is to restore safety, accountability and coexistence, not to change who holds a licence to destroy.'
},
24: {
'es_plain': 'Detectar un problema es sólo el comienzo. Una síntesis necesita además contrastar causas, escuchar objeciones, conservar fuentes, comparar alternativas, admitir correcciones y construir una respuesta que pueda revisarse.',
'es_example': 'Que una persona muy conocida diga “la vivienda es inaccesible” puede señalar un problema real. Pero tener millones de oyentes no decide por sí mismo por qué ocurre ni qué solución es mejor: hacen falta datos, causas competidoras, efectos secundarios y propuestas contrastables.',
'en_plain': 'Detecting a problem is only the beginning. A synthesis also needs to test causes, hear objections, preserve sources, compare alternatives, admit corrections and build a response that can be revised.',
'en_example': 'A very well-known person saying “housing is unaffordable” may identify a real problem. But having millions of listeners does not by itself establish why it is happening or which solution is best: data, competing causes, side effects and testable proposals are still required.'
},
25: {
'es_plain': 'Primero hay que separar lo que está ocurriendo de la historia que usamos para explicarlo. Podemos comprobar que algo sucede y seguir discutiendo por qué sucede; también podemos demostrar que una explicación es falsa sin hacer desaparecer el hecho que todavía necesita explicación.',
'es_example': 'Si los alquileres de una ciudad han subido un 30 %, esa subida es el fenómeno medible. Una narrativa puede atribuirla principalmente al turismo, otra a la falta de vivienda y otra a factores financieros. Refutar que el turismo sea la causa principal no hace desaparecer la subida; reconocer la subida tampoco demuestra cuál de esas causas es correcta.',
'en_plain': 'We must first separate what is happening from the story used to explain it. We may establish that something is occurring while still disputing why; we may also show that one explanation is false without making the underlying fact disappear.',
'en_example': 'If rents in a city have risen by 30%, that increase is the measurable phenomenon. One narrative may attribute it mainly to tourism, another to housing shortage and another to financial factors. Refuting tourism as the main cause does not make the rent increase disappear; recognising the increase does not prove which explanation is correct.'
},
26: {
'es_plain': 'Cuanto más poder tiene alguien para afectar a los demás, más trazable debería ser el uso de ese poder. Y cuanto más grave es una acusación, más evidencia hace falta antes de tratarla como un hecho. Las dos reglas protegen a la vez al espacio común y a quien es investigado.',
'es_example': 'Si una empresa controla una infraestructura crítica, las decisiones que afectan al servicio común deben ser especialmente auditables. Si después se la acusa de manipular deliberadamente el sistema, esa acusación necesita evidencia mucho más fuerte que la necesaria para abrir una pregunta o una investigación. Poder no es culpa; investigar no es condenar.',
'en_plain': 'The more power someone has to affect others, the more traceable the exercise of that power should be. And the more serious an accusation is, the more evidence is required before treating it as fact. Both rules protect the common space and the person or organisation being investigated at the same time.',
'en_example': 'If a company controls critical infrastructure, decisions affecting the shared service should be especially auditable. If it is then accused of deliberately manipulating the system, that accusation requires much stronger evidence than is needed to open a question or investigation. Power is not guilt; investigating is not condemning.'
}
}


def access_block(n):
    a = ACCESS[n]
    return f'''<!-- C-NAX-{n}_ACCESS_START -->

**ES · en sencillo:** {a['es_plain']}

**ES · ejemplo:** {a['es_example']}

**EN · in plain language:** {a['en_plain']}

**EN · example:** {a['en_example']}

> **Capa pedagógica / Pedagogical layer:** esta explicación y el ejemplo facilitan la lectura; no sustituyen la formulación candidata, su procedencia ni su Síntesis Abierta. / this explanation and example support readability; they do not replace the candidate formulation, its provenance or its Open Synthesis.

<!-- C-NAX-{n}_ACCESS_END -->
'''


def candidate_blocks(text):
    region = text.split(START, 1)[1].split(END, 1)[0]
    matches = list(re.finditer(r'^###\s+C-NAX-(\d+)\s+·.*$', region, re.M))
    out = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(region)
        out.append((int(m.group(1)), m.start(), end, region[m.start():end]))
    return region, out


def update_readme():
    text = README.read_text(encoding='utf-8')
    if START not in text or END not in text:
        raise SystemExit('Candidate registry markers missing')
    region, blocks = candidate_blocks(text)
    rebuilt = []
    cursor = 0
    for n, start, end, block in blocks:
        rebuilt.append(region[cursor:start])
        marker_start = f'<!-- C-NAX-{n}_ACCESS_START -->'
        marker_end = f'<!-- C-NAX-{n}_ACCESS_END -->'
        if marker_start in block and marker_end in block:
            block = re.sub(re.escape(marker_start) + r'.*?' + re.escape(marker_end) + r'\n?', access_block(n).strip() + '\n', block, flags=re.S)
        else:
            meta = re.search(r'^\*\*(?:Procedencia / Provenance|Síntesis / Synthesis|Síntesis específica / Dedicated synthesis):', block, re.M)
            if not meta:
                raise SystemExit(f'C-NAX-{n}: metadata insertion point not found')
            block = block[:meta.start()].rstrip() + '\n\n' + access_block(n) + '\n' + block[meta.start():]
        rebuilt.append(block)
        cursor = end
    rebuilt.append(region[cursor:])
    new_region = ''.join(rebuilt)
    text = text.split(START, 1)[0] + START + new_region + END + text.split(END, 1)[1]

    global_marker = '<!-- NEOAXIOM_PLAIN_LANGUAGE_RULE -->'
    if global_marker not in text:
        anchor = '> **[Regla completa / Full rule](../propuestas/sintesis-abierta/REGLA_MADURACION_NEOAXIOMAS_365_DIAS_ES_EN.md)**'
        note = f'''\n> {global_marker}\n> **Regla de claridad / Clarity rule:** la formulación formal conserva autoridad documental, pero cada C-NAX debe incorporar una lectura sencilla y un ejemplo ES/EN simétricos. La capa pedagógica no puede introducir una obligación, excepción o causalidad que no exista en la formulación y sus fuentes. / the formal formulation retains documentary authority, but every C-NAX must include a symmetric ES/EN plain-language reading and example. The pedagogical layer may not introduce an obligation, exception or causality absent from the formulation and its sources.\n'''
        if anchor not in text:
            raise SystemExit('Clarity-rule anchor not found')
        text = text.replace(anchor, anchor + note, 1)
    README.write_text(text, encoding='utf-8')


def update_dedicated(n, path):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    marker_start = f'<!-- C-NAX-{n}_ACCESS_START -->'
    marker_end = f'<!-- C-NAX-{n}_ACCESS_END -->'
    a = ACCESS[n]
    section = f'''{marker_start}

## Lectura sencilla y ejemplo / Plain-language reading and example

### ES · En sencillo

{a['es_plain']}

### ES · Ejemplo

{a['es_example']}

### EN · In plain language

{a['en_plain']}

### EN · Example

{a['en_example']}

> **Regla / Rule:** esta capa pedagógica no sustituye ni modifica la formulación candidata; sirve para hacerla comprensible y debe permanecer semánticamente subordinada a la formulación, procedencia y Síntesis Abierta. / this pedagogical layer neither replaces nor modifies the candidate formulation; it exists to make it understandable and remains semantically subordinate to the formulation, provenance and Open Synthesis.

{marker_end}
'''
    if marker_start in text and marker_end in text:
        text = re.sub(re.escape(marker_start) + r'.*?' + re.escape(marker_end), section.strip(), text, flags=re.S)
    else:
        anchor = '\n## Relaciones / Relations\n'
        if anchor not in text:
            raise SystemExit(f'{path}: relations anchor not found')
        text = text.replace(anchor, '\n' + section + anchor, 1)
    p.write_text(text, encoding='utf-8')


def harden_audit():
    text = AUDIT.read_text(encoding='utf-8')
    needle = "        if 'CANDIDATO ≠ CANON / CANDIDATE ≠ CANON' not in b:\n            problems.append(f'C-NAX-{n} carece de salvaguarda candidato≠canon / lacks candidate≠canon safeguard')\n"
    addition = needle + "        required_access = [r'\\*\\*ES · en sencillo:\\*\\*', r'\\*\\*ES · ejemplo:\\*\\*', r'\\*\\*EN · in plain language:\\*\\*', r'\\*\\*EN · example:\\*\\*']\n        if any(not re.search(pattern, b) for pattern in required_access):\n            problems.append(f'C-NAX-{n} carece de lectura sencilla y ejemplo simétricos ES/EN / lacks symmetric ES/EN plain-language reading and example')\n"
    if 'required_access = [' not in text:
        if needle not in text:
            raise SystemExit('Audit insertion point not found')
        text = text.replace(needle, addition, 1)
    scope_old = "**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, documentos dedicados, índice vivo y portal público de Síntesis Neoaxiomática. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, dedicated documents, the live index and the public Neoaxiom Synthesis portal."
    scope_new = "**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, capa de claridad ES/EN, documentos dedicados, índice vivo y portal público de Síntesis Neoaxiomática. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, ES/EN clarity layer, dedicated documents, the live index and the public Neoaxiom Synthesis portal."
    text = text.replace(scope_old, scope_new)
    rule_anchor = "        '- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**',\n"
    rule_add = rule_anchor + "        '- **Todo C-NAX debe incluir lectura sencilla y ejemplo simétricos ES/EN, subordinados a la formulación formal. / Every C-NAX must include symmetric ES/EN plain-language reading and an example, subordinate to the formal formulation.**',\n"
    if 'Every C-NAX must include symmetric ES/EN plain-language' not in text:
        if rule_anchor not in text:
            raise SystemExit('Audit rule anchor not found')
        text = text.replace(rule_anchor, rule_add, 1)
    AUDIT.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    update_readme()
    for n, path in {
        23: 'propuestas/sintesis-abierta/2026-08-15_C_NAX_23_CONSERVACION_FRACTAL_COMUN_ES_EN.md',
        24: 'propuestas/sintesis-abierta/2026-08-15_C_NAX_24_DIAGNOSTICO_NO_ES_SINTESIS_ES_EN.md',
        25: 'propuestas/sintesis-abierta/2026-08-16_C_NAX_25_FENOMENO_NO_ES_NARRATIVA_ES_EN.md',
        26: 'propuestas/sintesis-abierta/2026-08-16_C_NAX_26_PODER_TRAZABILIDAD_ACUSACION_EVIDENCIA_ES_EN.md',
    }.items():
        update_dedicated(n, path)
    harden_audit()
    print('NEOAXIOM_ACCESSIBILITY_REPAIR_OK candidates=12 dedicated=4')
