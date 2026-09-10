# WEB4™ · Ciencia · Connectoma completo de Drosophila / Complete Drosophila connectome

**Fecha de incorporación / Added:** 2026-09-10  
**Estado:** RECURSO CIENTÍFICO EXTERNO · EXPERIMENTO COMPUTACIONAL RELACIONADO  
**Área:** neurociencia · connectómica · simulación · sistemas complejos

## Qué es

El proyecto MaleCNS publica un connectoma a resolución sináptica del sistema nervioso central completo de un macho adulto de *Drosophila melanogaster*: cerebro y cordón nervioso ventral. La publicación científica apareció en *Cell* el 3 de septiembre de 2026 y el dataset `male-cns:v1.0` puede explorarse y descargarse desde Janelia/neuPrint.

Fuentes canónicas:

- MaleCNS · Janelia: https://male-cns.janelia.org/
- Explorador: https://male-cns.janelia.org/explore/
- Descarga/programmatic access: https://male-cns.janelia.org/download/
- Artículo: https://doi.org/10.1016/j.cell.2026.08.015
- Google Research: https://www.research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/

## Experimento Minecraft

Repositorio externo: https://github.com/blendi-remade/fly-brain-minecraft

`Fly Brain Minecraft` es un mod Fabric para Minecraft 1.21.1 que incorpora un derivado del dataset `male-cns:v1.0` y ejecuta las neuronas como unidades *leaky integrate-and-fire*. El mundo del juego se traduce a estímulos sobre poblaciones sensoriales del connectoma y determinadas poblaciones descendentes/motoras se traducen a comportamiento del mob.

La frase «meter el cerebro de una mosca en Minecraft» es divulgativamente útil pero incompleta. El proyecto conserva la conectividad biológica publicada y simula una red neuronal de punto, pero no reproduce toda la biofísica del animal. Además, su propia documentación diferencia comportamientos que emergen de la red de otros que emplean codificación sensorial, ganancias, reflejos o máquinas de estados construidas por el desarrollador.

## Trazabilidad de cifras

La publicación describe 166.691 neuronas completamente revisadas y anotadas. El dataset neuPrint `male-cns:v1.0` contiene además 176.422 nodos `:Neuron`; el derivado del mod conserva esos 176.422 nodos y, por rendimiento, mantiene 6.287.749 conexiones con peso >=5 sinapsis, que representan aproximadamente 90,3 millones de sinapsis de las ~125 millones del dataset. Las cifras no deben intercambiarse sin indicar qué nivel del dataset se está contando.

## Licencias

- Dataset MaleCNS: CC BY 4.0 según Janelia.
- Código de `fly-brain-minecraft`: MIT según su repositorio.
- Esta página enlaza y describe recursos externos; no reivindica autoría ni afiliación con Janelia, Google Research, Cambridge/MRC LMB, el autor del mod o Mojang/Microsoft.

## Encaje experimental con NEOCore™

El interés para NEOCore™ no es tratar el connectoma como una «IA consciente» ni atribuirle propiedades que no estén demostradas. El valor experimental está en disponer de una red biológica grande, dirigida, ponderada, trazable y conectada de extremo sensorial a extremo motor para probar herramientas de relación, perturbación, trazabilidad y comparación multiescala.

Líneas de prueba candidatas:

1. importar el grafo MaleCNS como red externa de referencia sin modificar sus pesos originales;
2. comparar métricas topológicas NEOCore con circuitos biológicos ya descritos;
3. introducir estímulos reproducibles y registrar propagación, bifurcaciones y estados de salida;
4. conectar un adaptador NEOCore exclusivamente a canales sensoriales/motores, manteniendo separada la red biológica del marco interpretativo;
5. contrastar predicciones con circuitos conocidos y conservar hipótesis rivales, incertidumbre y criterios de falsación;
6. explorar aprendizaje/plasticidad sólo como capa experimental separada, porque el simulador Minecraft actual no reproduce de forma general la plasticidad sináptica biológica.

## Regla epistemológica

`CONNECTOMA ≠ CEREBRO BIOFÍSICO COMPLETO ≠ CONCIENCIA ≠ INTELIGENCIA GENERAL`.

Una simulación puede ser muy valiosa sin que su comportamiento demuestre equivalencia funcional completa con el animal. WEB4™ debe mostrar siempre qué procede del dataset, qué del modelo neuronal, qué del adaptador sensorial/motor y qué del análisis NEOCore™.