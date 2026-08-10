# Nombres canónicos de manifiestos / Canonical manifesto filenames

<!-- NEOAXIOMAS_GLOBAL_LINK_START -->

## NEOCore™ 7.2 · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™
## NEOCore™ 7.2 · First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™

Los **Neoaxiomas™** expresan principios de alta estabilidad del NEOCore™ sin convertirse en dogmas cerrados: permanecen abiertos a contraste, evidencia, crítica, refutación y revisión mediante **Síntesis Abierta Neodialéctica™ — SAN™**. / **Neoaxioms™** express high-stability principles of NEOCore™ without becoming closed dogma: they remain open to challenge, evidence, criticism, refutation and revision through **Neodialectical Open Synthesis™ — SAN™**.

**[Abrir Neoaxiomas™ / Open Neoaxioms™](../../neoaxiomas/README.md)** · **[Síntesis Abierta Neoaxiomas™ / Neoaxioms Open Synthesis](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80)** · **[Protocolo / Protocol](../../propuestas/sintesis-abierta/NEOAXIOMAS_SINTESIS_ABIERTA_ES_EN.md)**

<!-- NEOAXIOMAS_GLOBAL_LINK_END -->


## Regla

El **número romano es el identificador canónico** del manifiesto y debe ser visible también en su nombre de archivo canónico.

Patrón:

`<ROMANO>_<slug>_ES_EN.md`

Ejemplo:

`I_neo0_soberania_de_guia_ES_EN.md`

Los nombres históricos se mantienen temporalmente como rutas **legacy** para no romper enlaces, citas, navegación, auditorías ni referencias externas. La correspondencia completa I–LX está registrada en `../CANONICAL_FILENAMES.json`.

**No se debe inferir jamás el número canónico a partir del prefijo decimal histórico.**

## Fuente única y resolución de enlaces

La ruta **legacy** es, durante la migración, la **fuente de contenido editable**. La ruta canónica es una **representación derivada automáticamente** y no debe editarse manualmente.

La sincronización se realiza mediante:

`.github/scripts/sync_canonical_manifestos.py`

El principio es:

```text
FUENTE LEGACY EDITABLE
        ↓
REGISTRO CANÓNICO ÚNICO
        ↓
RESOLUTOR DE DESTINOS
        ↓
REPRESENTACIÓN CANÓNICA DERIVADA
```

Un mismo destino lógico debe resolverse siempre desde una única fuente de verdad. Al generar una copia canónica, los enlaces relativos se recalculan según la ubicación real del archivo derivado. Si un enlace apunta a otro manifiesto registrado, se dirige a su ruta canónica romana; si apunta a otra parte del repositorio, se conserva el mismo destino lógico con una ruta relativa correcta.

Por tanto, **no se exige identidad byte-a-byte entre fuente legacy y representación canónica**: el contenido semántico debe conservarse, pero los enlaces pueden y deben transformarse para mantener exactamente el mismo destino lógico.

La migración sólo podrá retirar una ruta legacy cuando no queden dependencias externas o internas que necesiten conservarla.

## Invariante de seguridad

Toda sincronización canónica debe terminar con:

```text
CANONICAL_GENERATED = número registrado
CANONICAL_MISSING_LEGACY = 0
BROKEN_INTERNAL_LINKS = 0
```

Si cualquiera de estas condiciones falla, la migración queda abierta y debe corregirse antes de declarar el estado documental como sano.
