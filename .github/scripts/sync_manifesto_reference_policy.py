from pathlib import Path
import re

README = Path('manifiestos/README.md')
START = '<!-- NEO_CROSS_REFERENCE_POLICY_START -->'
END = '<!-- NEO_CROSS_REFERENCE_POLICY_END -->'

BLOCK = f'''{START}

## Norma de referencias cruzadas / Cross-reference policy

Para mantener los manifiestos legibles sin perder la red documental, se adopta esta norma común: / To keep manifestos readable without losing the documentary graph, the following common rule applies:

1. **Las menciones en el cuerpo pueden permanecer como texto** cuando convertir cada aparición en hipervínculo perjudique la lectura. / **Body mentions may remain as prose** when turning every occurrence into a hyperlink would harm readability.
2. **Todo manifiesto debe terminar con un bloque `Referencias cruzadas canónicas / Canonical cross-references`** que convierta en hipervínculos las relaciones internas directas detectadas y permita retorno a fuente. / **Every manifesto must end with a `Canonical cross-references` block** that hyperlinks detected direct internal relations and preserves return to source.
3. El hipervínculo inline es opcional; se recomienda en la primera mención cuando facilite orientación. **El bloque final es la capa normativa de navegación.** / Inline hyperlinks are optional and recommended on first mention when useful. **The final block is the normative navigation layer.**
4. Si un manifiesto menciona directamente otro manifiesto, Neoaxioma™ o fuente estructural y esa relación no aparece en el bloque final, se considera **defecto documental a corregir**, no ausencia deliberada de relación. / If a manifesto directly mentions another manifesto, Neoaxiom™ or structural source and that relation is absent from the final block, this is a **documentary defect to fix**, not an intentional absence of relation.
5. Un vínculo cruzado declara **relación documental o conceptual**, no identidad, subordinación, aceptación automática ni prueba de una tesis. / A cross-link declares a **documentary or conceptual relation**, not identity, subordination, automatic endorsement or proof of a claim.

La sincronización se automatiza mediante `.github/scripts/sync_manifesto_crossrefs.py`; la fuente íntegra de cada manifiesto nunca debe ser sustituida por el índice o por el bloque de navegación. / Synchronisation is automated by `.github/scripts/sync_manifesto_crossrefs.py`; the full manifesto source must never be replaced by its index or navigation block.

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
