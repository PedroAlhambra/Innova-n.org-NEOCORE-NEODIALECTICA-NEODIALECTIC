# WEB4™ · Connectoma completo de Drosophila / Complete Drosophila Connectome

**Fecha / Date:** 2026-09-10  
**Estado / Status:** RECURSO CIENTÍFICO EXTERNO / EXTERNAL SCIENTIFIC RESOURCE · EXPERIMENTOS COMPUTACIONALES RELACIONADOS / RELATED COMPUTATIONAL EXPERIMENTS  
**Área / Area:** neurociencia · connectómica · simulación · sistemas complejos / neuroscience · connectomics · simulation · complex systems

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Qué es MaleCNS

MaleCNS publica un connectoma a resolución sináptica del sistema nervioso central completo de un macho adulto de *Drosophila melanogaster*: cerebro y cordón nervioso ventral. La publicación apareció en *Cell* el 3 de septiembre de 2026 y el dataset `male-cns:v1.0` puede explorarse y descargarse desde Janelia/neuPrint.

Fuentes canónicas:

- MaleCNS · Janelia: https://male-cns.janelia.org/
- Explorador: https://male-cns.janelia.org/explore/
- Descarga / acceso programático: https://male-cns.janelia.org/download/
- Artículo: https://doi.org/10.1016/j.cell.2026.08.015
- Google Research: https://www.research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/
- Acceso/análisis R: https://github.com/natverse/malecns

## 2. Experimentos computacionales relacionados

### Fly Brain Minecraft

Repositorio: https://github.com/blendi-remade/fly-brain-minecraft

Es un mod Fabric para Minecraft 1.21.1 que incorpora un derivado de `male-cns:v1.0` y ejecuta sus neuronas como unidades *leaky integrate-and-fire*. El mundo del juego se traduce a estímulos sobre poblaciones sensoriales del connectoma y determinadas poblaciones descendentes/motoras se traducen en comportamiento del mob.

La frase «meter el cerebro de una mosca en Minecraft» es divulgativamente útil pero incompleta. El proyecto conserva conectividad biológica publicada y simula una red neuronal de punto, pero no reproduce toda la biofísica del animal. Su documentación distingue qué comportamientos emergen de la red y cuáles dependen de codificación sensorial, ganancias, reflejos o máquinas de estados construidas.

### DOOMFLY

Repositorio: https://github.com/nftechie/doomfly

Conecta MaleCNS con ViZDoom e investiga una regla experimental de plasticidad dopaminérgica. Su documentación conserva resultados negativos: el candidato descrito no superó determinados gates de aprendizaje/supervivencia. Ese resultado negativo es científicamente relevante porque limita la interpretación del experimento.

### Fly64

Repositorio: https://github.com/ornata/fly

Conecta un modelo MaleCNS con Super Mario 64. El propio autor advierte que es una demostración experimental realizada por diversión y que no debe asumirse como software revisado para uso científico serio.

Estos proyectos son independientes de los productores de MaleCNS y no constituyen validación oficial del dataset ni equivalencia funcional con una mosca viva.

## 3. Trazabilidad de cifras

La publicación describe **166.691 neuronas completamente revisadas y anotadas**. El dataset neuPrint `male-cns:v1.0` contiene además **176.422 nodos `:Neuron`** según la procedencia documentada por Fly Brain Minecraft. Ese derivado conserva esos nodos y, por rendimiento, mantiene **6.287.749 conexiones con peso ≥5 sinapsis**, que representan aproximadamente **90,3 millones de sinapsis** de las ~125 millones del dataset.

Las cifras no deben intercambiarse sin indicar qué nivel del dataset se está contando.

## 4. Licencias y derechos

- Dataset MaleCNS: CC BY 4.0 según Janelia.
- Código de Fly Brain Minecraft: MIT según su repositorio.
- Código de DOOMFLY: MIT según su repositorio.
- Fly64: licencia no fijada aquí hasta verificación específica.
- Screenshots, logos, papers y marcas se consideran capas de derechos separadas; por defecto WEB4 usa `LINK_ONLY` salvo licencia o permiso adicional verificado.

Esta página enlaza y describe recursos externos; no reivindica autoría ni afiliación con Janelia, Google Research, Cambridge/MRC LMB, los autores de los experimentos o Mojang/Microsoft.

## 5. Encaje experimental con NEOCore™

El interés para NEOCore™ no es presentar el connectoma como una «IA consciente». Es disponer de una red biológica grande, dirigida, ponderada y trazable, conectada desde entradas sensoriales hasta salidas motoras, para experimentar con relación, perturbación, trazabilidad y comparación multiescala.

Líneas candidatas:

1. importar MaleCNS como grafo externo de referencia sin modificar sus pesos originales;
2. comparar métricas topológicas NEOCore con circuitos biológicos descritos;
3. introducir estímulos reproducibles y registrar propagación, bifurcaciones y estados;
4. conectar un adaptador NEOCore sólo como capa explícita, separada del dataset y del modelo neuronal;
5. mantener hipótesis rivales, incertidumbre y falsación;
6. estudiar plasticidad sólo como capa experimental versionada y comparable contra un control sin plasticidad;
7. utilizar resultados negativos externos como controles, no sólo demos exitosas.

## 6. Frontera epistemológica

`CONNECTOMA ≠ CEREBRO BIOFÍSICO COMPLETO ≠ CONCIENCIA ≠ INTELIGENCIA GENERAL`.

WEB4™ debe mostrar siempre qué procede del dataset, qué del modelo neuronal, qué del adaptador sensorial/motor y qué del análisis o experimento NEOCore™.

---

# EN · English

## 1. What MaleCNS is

MaleCNS publishes a synapse-resolution connectome of the complete central nervous system of an adult male *Drosophila melanogaster*: brain and ventral nerve cord. The publication appeared in *Cell* on September 3, 2026, and the `male-cns:v1.0` dataset can be explored and downloaded through Janelia/neuPrint.

Canonical sources:

- MaleCNS · Janelia: https://male-cns.janelia.org/
- Explorer: https://male-cns.janelia.org/explore/
- Download / programmatic access: https://male-cns.janelia.org/download/
- Paper: https://doi.org/10.1016/j.cell.2026.08.015
- Google Research: https://www.research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/
- R access/analysis: https://github.com/natverse/malecns

## 2. Related computational experiments

### Fly Brain Minecraft

Repository: https://github.com/blendi-remade/fly-brain-minecraft

It is a Fabric mod for Minecraft 1.21.1 that embeds a derivative of `male-cns:v1.0` and runs its neurons as *leaky integrate-and-fire* units. The game world is translated into stimuli on sensory populations in the connectome, while selected descending/motor populations are translated into mob behaviour.

The phrase “putting a fly brain inside Minecraft” is useful for outreach but incomplete. The project preserves published biological connectivity and simulates a point-neuron network, but it does not reproduce the animal's full biophysics. Its documentation distinguishes behaviours emerging from the network from those depending on constructed sensory encoding, gains, reflexes or state machines.

### DOOMFLY

Repository: https://github.com/nftechie/doomfly

It connects MaleCNS to ViZDoom and investigates an experimental dopamine-dependent plasticity rule. Its documentation preserves negative results: the described candidate did not pass specific learning/survival gates. That negative result is scientifically relevant because it limits interpretation of the experiment.

### Fly64

Repository: https://github.com/ornata/fly

It connects a MaleCNS model to Super Mario 64. The author explicitly warns that it is an experimental demonstration made for fun and should not be assumed to be reviewed software for serious scientific use.

These projects are independent from the MaleCNS producers and do not constitute official validation of the dataset or functional equivalence with a living fly.

## 3. Traceability of counts

The paper describes **166,691 fully proofread and annotated neurons**. The `male-cns:v1.0` neuPrint dataset also contains **176,422 `:Neuron` nodes** according to the provenance documented by Fly Brain Minecraft. That derivative preserves those nodes and, for performance, keeps **6,287,749 connections with weight ≥5 synapses**, representing approximately **90.3 million synapses** out of the dataset's ~125 million.

These numbers must not be exchanged without stating which dataset level is being counted.

## 4. Licences and rights

- MaleCNS dataset: CC BY 4.0 according to Janelia.
- Fly Brain Minecraft code: MIT according to its repository.
- DOOMFLY code: MIT according to its repository.
- Fly64: licence is not fixed here until specifically verified.
- Screenshots, logos, papers and trademarks are treated as separate rights layers; WEB4 defaults to `LINK_ONLY` unless an additional licence or permission is verified.

This page links to and describes external resources; it does not claim authorship or affiliation with Janelia, Google Research, Cambridge/MRC LMB, the experiment authors or Mojang/Microsoft.

## 5. Experimental fit with NEOCore™

The interest for NEOCore™ is not to present the connectome as a “conscious AI”. It is to work with a large, directed, weighted and traceable biological network connected from sensory inputs to motor outputs, allowing experiments in relationships, perturbation, traceability and multiscale comparison.

Candidate lines:

1. import MaleCNS as an external reference graph without modifying its original weights;
2. compare NEOCore topological metrics with described biological circuits;
3. introduce reproducible stimuli and record propagation, bifurcations and states;
4. connect a NEOCore adapter only as an explicit layer, kept separate from the dataset and neural model;
5. maintain rival hypotheses, uncertainty and falsification;
6. study plasticity only as a versioned experimental layer comparable against a no-plasticity control;
7. use external negative results as controls, not only successful demos.

## 6. Epistemic boundary

`CONNECTOME ≠ COMPLETE BIOPHYSICAL BRAIN ≠ CONSCIOUSNESS ≠ GENERAL INTELLIGENCE`.

WEB4™ must always show what comes from the dataset, what comes from the neural model, what comes from the sensory/motor adapter and what comes from NEOCore™ analysis or experimentation.
