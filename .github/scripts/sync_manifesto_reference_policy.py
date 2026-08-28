from pathlib import Path
import re

README = Path('manifiestos/README.md')
START = '<!-- NEO_CROSS_REFERENCE_POLICY_START -->'
END = '<!-- NEO_CROSS_REFERENCE_POLICY_END -->'

BLOCK = f'''{START}

## Norma de referencias cruzadas / Cross-reference policy

Para mantener los manifiestos legibles sin perder la red documental, se adopta esta norma común: / To keep manifestos readable without losing the documentary graph, the following common rule applies:

1. **Toda superficie que presente una relación como navegación debe ser clicable.** `Relaciones principales / Main relations`, índices relacionales, referencias de Síntesis Abierta, Issues, deltas y fuentes explícitamente ofrecidas para continuar el recorrido deben usar hipervínculos reales, no referencias de texto plano. / **Every surface that presents a relation as navigation must be clickable.** `Main relations`, relational indexes, Open Synthesis references, Issues, deltas and sources explicitly offered as continuation routes must use real hyperlinks, not plain-text references.
2. **Todo manifiesto debe terminar además con un bloque `Referencias cruzadas canónicas / Canonical cross-references`** que reúna como índice navegable adicional las relaciones internas directas detectadas y permita retorno a fuente. / **Every manifesto must additionally end with a `Canonical cross-references` block** collecting detected direct internal relations as an additional navigable index and preserving return to source.
3. Las menciones meramente discursivas dentro de un párrafo pueden permanecer como prosa cuando no actúen como elemento de navegación. **Una relación declarada, un Issue o una llamada a continuar el recorrido nunca debe depender sólo de texto plano.** / Purely discursive mentions inside prose may remain plain when they are not acting as navigation. **A declared relation, Issue or continuation route must never depend on plain text alone.**
4. Si un manifiesto declara una relación directa con otro manifiesto, Neoaxioma™, Síntesis Abierta o fuente estructural y no existe al menos una ruta clicable hacia ella en la superficie donde se declara, se considera **RELATIONAL_NAVIGATION_FAILURE**. / If a manifesto declares a direct relation to another manifesto, Neoaxiom™, Open Synthesis or structural source and there is no clickable route to it on the surface where it is declared, this is a **RELATIONAL_NAVIGATION_FAILURE**.
5. Un vínculo cruzado declara **relación documental o conceptual**, no identidad, subordinación, aceptación automática ni prueba de una tesis. / A cross-link declares a **documentary or conceptual relation**, not identity, subordination, automatic endorsement or proof of a claim.
6. Los generadores y workflows deben impedir regresiones: una sincronización no puede convertir enlaces existentes en texto plano y la auditoría de navegabilidad debe ejecutarse antes de cualquier PASS documental. / Generators and workflows must prevent regressions: synchronization must never downgrade existing links to plain text, and navigability auditing must run before any documentary PASS.

La sincronización se automatiza mediante `.github/scripts/sync_manifesto_crossrefs.py` y se valida mediante `.github/scripts/audit_manifesto_clickable_relations.py`; la fuente íntegra de cada manifiesto nunca debe ser sustituida por el índice o por el bloque de navegación. / Synchronisation is automated through `.github/scripts/sync_manifesto_crossrefs.py` and validated through `.github/scripts/audit_manifesto_clickable_relations.py`; the full manifesto source must never be replaced by its index or navigation block.

{END}
'''

text = README.read_text(encoding='utf-8')
text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\s*', '', text, flags=re.S)
anchor = '## Dos puertas principales / Two main doors'
if anchor in text:
    text = text.replace(anchor, BLOCK + '\n' + anchor, 1)
else:
    text = text.rstrip() + '\n\n' + BLOCK
README.write_text(text, encoding='utf-8')
print('REFERENCE_POLICY=OK')
