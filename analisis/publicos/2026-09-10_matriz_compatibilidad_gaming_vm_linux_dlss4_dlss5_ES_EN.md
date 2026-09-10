# Matriz pública de compatibilidad gaming virtualizado · Linux + VM + RTX + DLSS 4/4.5/5
## Virtualized Linux RTX Gaming Compatibility Matrix · Rocinante Reference Stack

**Fecha / Date:** 2026-09-10  
**Estado / Status:** PUBLIC-BETA · matriz viva / living matrix  
**Ámbito / Scope:** Linux · KVM/QEMU · PCIe GPU passthrough · NVIDIA GeForce RTX · Steam/Proton · DLSS 4/4.5/5  
**Plataforma de referencia / Reference platform:** Rocinante™ como banco de pruebas, no como requisito de marca.

---

## ES · Criterio

Esto **no es un ranking de “juegos para Rocinante”** ni una exhibición de hardware. Es una matriz técnica y reproducible para sistemas de tipo **Rocinante-like**:

```text
host Linux / hipervisor
→ KVM/QEMU
→ VM Linux de escritorio
→ GPU NVIDIA RTX dedicada mediante PCIe passthrough
→ Steam
→ Proton / DXVK-NVAPI / VKD3D-Proton
→ juego Windows
→ DLSS cuando el juego y la pila lo permiten
```

Rocinante™ funciona como **plataforma de referencia y validación**. El objetivo público es que la información sirva también a otras configuraciones Linux virtualizadas equivalentes.

### Estados

- **R0 · VERIFICADO_ROCINANTE**: probado materialmente en la VM de referencia con evidencia reproducible.
- **R1 · CANDIDATO_FUERTE**: soporte DLSS 4/4.5 relevante y sin bloqueo conocido específico contra KVM/VM; candidato prioritario para prueba local.
- **R2 · CONDICIONAL**: compatible o prometedor bajo Proton, pero requiere validación local adicional por versión reciente, anticheat, servicio online o ruta DLSS concreta.
- **BLOQUEADO**: existe un bloqueo conocido contra VM o contra Proton/Linux que invalida el caso actual.

**Regla de trazabilidad:** no se eleva un juego a R0 por documentación, fama o inferencia. R0 exige ejecución real y registro de versión de juego, Proton, driver, kernel, resolución y funciones DLSS observadas.

---

## DLSS 5

A fecha de esta matriz, **NBA 2K27** es la primera integración oficial publicada de **DLSS 5 / 3D-Guided Neural Rendering**. NVIDIA exige GeForce RTX Serie 50 y su nueva rama de driver compatible. SteamDB registra el juego como compatible con SteamOS/Proton, pero eso **no demuestra por sí solo** que DLSS 5 esté validado dentro de una VM KVM con GPU passthrough.

| Juego | Tecnología | Estado Rocinante-like | Motivo |
|---|---|---|---|
| NBA 2K27 | DLSS 5 Neural Rendering + SR + FG/MFG + Reflex | **R2 · CONDICIONAL** | Proton/SteamOS es viable; falta validación específica KVM + RTX passthrough + DLSS 5 en Rocinante. No se presenta como R0. |

---

## DLSS 4 / 4.5 · candidatos fuertes para VM Linux RTX

La siguiente tabla prioriza títulos que combinan soporte DLSS moderno con ausencia de un bloqueo conocido explícito contra KVM/VM. **R1 no significa “probado ya en Rocinante”**; significa que la arquitectura no presenta actualmente un bloqueo conocido que justifique excluirlo antes de probar.

| Juego | DLSS/RTX de interés | Estado |
|---|---|---|
| Cyberpunk 2077 | DLSS 4, Multi Frame Generation, Ray Reconstruction, Path Tracing | **R1** |
| DOOM: The Dark Ages | DLSS 4/4.5, Frame Generation/MFG, ray/path tracing según versión | **R1** |
| Indiana Jones and the Great Circle | DLSS 4, MFG, Ray Reconstruction, Path Tracing | **R1** |
| Black Myth: Wukong | DLSS 4, MFG, Full Ray Tracing | **R1** |
| Hogwarts Legacy | DLSS 4-class features, Frame Generation, RT | **R1** |
| Resident Evil Requiem | DLSS 4/4.5-class features, RT/PT según build | **R1** |
| PRAGMATA | DLSS 4/4.5-class features, RT/PT según build | **R1** |
| 007 First Light | DLSS 4.5-class features, Dynamic MFG, RT/PT según actualización | **R1** |
| Crimson Desert | DLSS 4-class features, MFG/RT según build | **R1** |
| Phantom Blade Zero | DLSS 4, Multi Frame Generation, ray tracing | **R2 · reciente** |
| Marvel's Spider-Man 2 | DLSS 4-class features, MFG, RT | **R1** |
| God of War Ragnarök | DLSS 4-class features, MFG | **R1** |
| S.T.A.L.K.E.R. 2: Heart of Chornobyl | DLSS 4-class features, MFG | **R1** |
| Stellar Blade | DLSS 4-class features, MFG | **R1** |
| Lost Soul Aside | DLSS 4-class features, MFG, RT | **R1** |
| Dying Light: The Beast | DLSS 4-class features, MFG, RT | **R1** |
| Cronos: The New Dawn | DLSS 4-class features, RT | **R1** |
| The Outer Worlds 2 | DLSS 4-class features, MFG/RT | **R1** |
| WUCHANG: Fallen Feathers | DLSS 4-class features, MFG | **R1** |
| NINJA GAIDEN 2 Black | DLSS 4-class features, MFG | **R1** |
| Rise of the Ronin | DLSS 4-class features, MFG | **R1** |
| FINAL FANTASY XVI | DLSS 4-class features, MFG | **R1** |
| SILENT HILL 2 | DLSS 4-class features, MFG | **R1** |
| Star Wars Jedi: Survivor | DLSS 4-class features, Frame Generation/MFG path | **R1** |
| Remnant II | DLSS 4-class features, MFG | **R1** |
| Dragon Age: The Veilguard | DLSS 4-class features, MFG | **R1** |
| Avowed | DLSS 4-class features, MFG | **R1** |
| Eternal Strands | DLSS 4-class features, MFG | **R1** |
| Flintlock: The Siege of Dawn | DLSS 4-class features, MFG | **R1** |
| Still Wakes the Deep | DLSS 4-class features, MFG | **R1** |
| Layers of Fear (2023) | DLSS 4-class features, MFG | **R1** |
| A Quiet Place: The Road Ahead | DLSS 4-class features, MFG | **R1** |
| Immortals of Aveum | DLSS 4-class features, MFG | **R1** |
| Ghostrunner 2 | DLSS 4-class features, MFG | **R1** |
| The Thaumaturge | DLSS 4-class features, MFG | **R1** |
| Jusant | DLSS 4-class features, MFG | **R1** |
| Deliver Us Mars | DLSS 4-class features, MFG, RT | **R1** |
| Lords of the Fallen | DLSS 4-class features, MFG | **R1** |
| ICARUS | DLSS 4-class features, MFG, RT | **R1** |
| EVERSPACE 2 | DLSS 4/4.5-class Super Resolution path | **R1** |
| Satisfactory | DLSS 4-class features, MFG | **R1** |
| Deep Rock Galactic | DLSS 4-class path; NGX update may need Proton-specific overrides | **R1** |
| RoadCraft | DLSS 4-class features, MFG | **R1** |
| inZOI | DLSS 4-class features, MFG | **R1** |
| MindsEye | DLSS 4-class features, MFG | **R1** |
| Frostpunk 2 | DLSS 4-class features, MFG | **R1** |
| HITMAN World of Assassination | DLSS 4-class path | **R1** |
| Witchfire | DLSS 4-class path | **R1** |

---

## Exclusiones actuales por VM / Proton

Estos títulos **no deben mezclarse con la lista positiva** aunque aparezcan en catálogos generales de DLSS:

| Juego | Estado | Motivo |
|---|---|---|
| Marvel Rivals | **BLOQUEADO_VM** | El desarrollador incluye expresamente VMware, **KVM** y VirtualBox entre las máquinas virtuales prohibidas mientras se ejecuta el juego. |
| Mecha BREAK | **BLOQUEADO_VM** | El anticheat ACE muestra bloqueo explícito de máquinas virtuales en la versión publicada. |
| Fate Trigger | **BLOQUEADO_PROTON** | El launcher/anticheat ha requerido funciones de kernel no implementadas en Wine/Proton y aborta el arranque en informes públicos. |
| SCUM | **BLOQUEADO_PROTON** | El desarrollador ha indicado en 2026 que no habilita soporte Linux/Proton en el estado actual. |

Los títulos online con anticheat que no tengan una posición estable respecto a KVM deben permanecer en **R2** o fuera de la matriz positiva hasta disponer de evidencia suficiente.

---

## Stray y juegos sin DLSS 4/5

**Stray no entra en la tabla DLSS 4/5.** En una RTX moderna bajo Linux/Proton puede estudiarse por otra ruta: DX12/RT cuando proceda y **NVIDIA Smooth Motion**. Esta categoría debe mostrarse separada en WEB4 para no confundir Frame Generation externo con una integración DLSS del motor.

---

## Qué demuestra realmente la plataforma

El interés técnico de una configuración Rocinante-like no es “tener una RTX 5090”. La prueba relevante es otra:

```text
GPU física dedicada
+ passthrough PCIe
+ Linux virtualizado
+ Steam/Proton
+ NVAPI expuesto por DXVK-NVAPI
+ DLSS del juego
+ evidencia de ejecución
= gaming RTX reproducible dentro de VM
```

NVIDIA documenta que los juegos Windows ejecutados mediante **Steam Play / Proton** pueden utilizar DLSS cuando Proton expone NVAPI; las instalaciones estándar modernas incluyen DXVK-NVAPI. También documenta actualización de librerías NGX mediante `PROTON_ENABLE_NGX_UPDATER=1`, overrides para SR/RR/FG y el indicador DLSS para comprobar materialmente qué se está utilizando.

Por tanto, la futura sección WEB4 debe ser un **observatorio técnico vivo**, no una lista promocional cerrada.

---

## Campos propuestos para WEB4

Cada ficha de juego debería mostrar:

```text
juego
estado_R0_R1_R2_BLOCKED
fecha_ultima_revision
Steam_AppID
Proton_version
NVIDIA_driver
kernel
GPU
hipervisor
passthrough
DLSS_SR
DLSS_FG
DLSS_MFG
DLSS_RR
DLSS_5_neural_rendering
ray_tracing
path_tracing
anti_cheat
vm_policy
resolucion_probada
fps_base
fps_DLSS
incidencias
fuentes
```

Cuando se pruebe un juego materialmente en Rocinante, la entrada puede ascender a **R0** y registrar la evidencia de la sesión. Así la clasificación crece por pruebas, no por marketing.

---

## Fuentes principales / Primary sources

- NVIDIA · DLSS 5 / NBA 2K27: https://www.nvidia.com/es-la/geforce/news/dlss-5-3d-guided-neural-rendering/
- NVIDIA · listado general RTX/DLSS: https://www.nvidia.com/en-us/geforce/news/nvidia-rtx-games-engines-apps/
- NVIDIA · más de 250 juegos/apps DLSS 4: https://www.nvidia.com/es-la/geforce/news/dlss-4-rtx-path-tracing-game-announcements-ces-2026/
- NVIDIA · guía Linux · DLSS / Smooth Motion / Reflex / Proton: https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/gaming.html
- Valve Proton · regresión DLSS Frame Generation en RTX 5090, con juegos afectados y evidencia de funcionamiento previo: https://github.com/ValveSoftware/Proton/issues/8692
- Valve Proton · DOOM: The Dark Ages: https://github.com/ValveSoftware/Proton/issues/8690
- SteamDB · NBA 2K27 / SteamOS-Proton compatibility: https://steamdb.info/app/4356430/config/
- Marvel Rivals · lista oficial de software/hardware prohibido, incluyendo KVM: https://www.marvelrivals.com/guide/20250226/41348_1214569.html
- Valve Proton · Fate Trigger: https://github.com/ValveSoftware/Proton/issues/8988
- Valve Proton · Mecha BREAK: https://github.com/ValveSoftware/Proton/issues/8475

---

# EN · Summary

This is **not a “best games for Rocinante” ranking**. It is a reproducible compatibility matrix for Linux gaming systems using KVM/QEMU, dedicated RTX PCIe passthrough and Steam/Proton. Rocinante™ is the reference and validation platform.

`R0` means materially tested on Rocinante. `R1` means a strong architectural candidate with no known VM-specific blocker. `R2` means conditional/pending local verification. `BLOCKED` means that current VM or Proton restrictions invalidate the title for this stack.

DLSS 5 is kept separate from DLSS 4/4.5: NBA 2K27 is the first official DLSS 5 title, but it remains **R2** until the exact KVM + passthrough + Proton + DLSS 5 path is validated locally.

The WEB4 projection should consume this as a **living technical observatory**, with per-game evidence and versioned state rather than a static marketing list.
