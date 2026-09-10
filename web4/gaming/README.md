# WEB4™ · Gaming virtualizado / Virtualized Gaming

**Estado / Status:** PUBLIC-SOURCE · READY-FOR-WEB4-ADAPTER · NO-LIVE-DEPLOY  
**Fecha / Date:** 2026-09-10

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Función

Esta carpeta define la fuente pública de una futura sección WEB4™ sobre compatibilidad de juegos en configuraciones Linux virtualizadas con GPU RTX dedicada mediante passthrough y Steam/Proton.

No se plantea como ranking de potencia ni como «juegos para Rocinante». **Rocinante™ es plataforma de referencia y validación**; el objeto público es reproducible por otras configuraciones Rocinante-like.

## 2. Fuentes

- [Matriz pública completa ES/EN](../../analisis/publicos/2026-09-10_matriz_compatibilidad_gaming_vm_linux_dlss4_dlss5_ES_EN.md)
- [Datos estructurados JSON](./compatibility.json)

## 3. Estados

- `R0 · VERIFIED_ROCINANTE`: prueba material registrada en la plataforma de referencia.
- `R1 · STRONG_CANDIDATE`: sin bloqueo VM conocido y con ruta DLSS/Proton técnicamente plausible.
- `R2 · CONDITIONAL`: requiere prueba local por versión, anticheat, online o ruta DLSS concreta.
- `BLOCKED`: bloqueo conocido por VM o Proton/Linux.

La interfaz debe poder filtrar por DLSS 5, DLSS 4/4.5, MFG, Ray Reconstruction, Ray Tracing, Path Tracing, estado Proton y política de VM.

## 4. Publicación y evidencia

```text
FUENTE PÚBLICA VERSIONADA
→ adaptador WEB4
→ tabla / fichas / filtros
→ evidencia por juego
→ revisión periódica
```

`R0` sólo se concede después de una ejecución real con registro de versión de juego, Proton, driver, kernel, GPU, resolución y funciones DLSS observadas. La documentación o inferencia no sustituyen la prueba local.

La implementación viva se desarrolla en el workspace privado y esta carpeta actúa como fuente de datos, contrato de superficie y genealogía pública, no como baseline de implementación.

## 5. Relación con interoperabilidad

Los bloqueos por virtualización o sistema operativo deben registrarse como hechos técnicos por título y versión. La matriz no presupone mala fe ni declara por sí sola una infracción legal. Puede alimentar una Síntesis Abierta™ sobre interoperabilidad, anticheat y proporcionalidad de restricciones.

---

# EN · English

## 1. Purpose

This folder defines the public source for a future WEB4™ section covering game compatibility on virtualized Linux configurations using a dedicated RTX GPU through passthrough and Steam/Proton.

It is not framed as a performance ranking or as “games for Rocinante”. **Rocinante™ is the reference and validation platform**; the public subject is reproducible by other Rocinante-like configurations.

## 2. Sources

- [Complete public ES/EN matrix](../../analisis/publicos/2026-09-10_matriz_compatibilidad_gaming_vm_linux_dlss4_dlss5_ES_EN.md)
- [Structured JSON data](./compatibility.json)

## 3. States

- `R0 · VERIFIED_ROCINANTE`: material test recorded on the reference platform.
- `R1 · STRONG_CANDIDATE`: no known VM blocker and a technically plausible DLSS/Proton path.
- `R2 · CONDITIONAL`: requires local testing because of version, anticheat, online mode or a specific DLSS path.
- `BLOCKED`: known VM or Proton/Linux blocker.

The interface should support filtering by DLSS 5, DLSS 4/4.5, MFG, Ray Reconstruction, Ray Tracing, Path Tracing, Proton state and VM policy.

## 4. Publication and evidence

```text
VERSIONED PUBLIC SOURCE
→ WEB4 adapter
→ table / cards / filters
→ per-game evidence
→ periodic review
```

`R0` is granted only after a real execution with recorded game version, Proton, driver, kernel, GPU, resolution and observed DLSS functions. Documentation or inference do not replace local testing.

The living implementation is developed in the private workspace, while this folder acts as a public data source, surface contract and genealogy, not as the implementation baseline.

## 5. Relationship with interoperability

Virtualization or operating-system blocks must be recorded as technical facts per title and version. The matrix does not presume bad faith or by itself declare a legal violation. It may provide evidence for an Open Synthesis™ on interoperability, anticheat and proportionality of restrictions.
