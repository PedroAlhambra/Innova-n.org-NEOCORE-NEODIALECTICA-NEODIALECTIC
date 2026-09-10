# Matriz pública de compatibilidad gaming virtualizado / Virtualized Gaming Compatibility Matrix

**Fecha / Date:** 2026-09-10  
**Estado / Status:** PUBLIC-BETA · matriz viva / living matrix  
**Ámbito / Scope:** Linux · KVM/QEMU · PCIe GPU passthrough · NVIDIA GeForce RTX · Steam/Proton · DLSS 4/4.5/5  
**Plataforma de referencia / Reference platform:** Rocinante™ como banco de pruebas / as a validation testbed, not a brand requirement.

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Criterio

Esto **no es un ranking de “juegos para Rocinante”** ni una exhibición de hardware. Es una matriz técnica para sistemas Rocinante-like:

```text
host Linux / hipervisor
→ KVM/QEMU
→ VM Linux de escritorio
→ GPU NVIDIA RTX dedicada por PCIe passthrough
→ Steam
→ Proton / DXVK-NVAPI / VKD3D-Proton
→ juego Windows
→ DLSS cuando juego y pila lo permiten
```

Rocinante™ funciona como plataforma de referencia. La información debe ser reutilizable por configuraciones Linux virtualizadas equivalentes.

### Estados

- **R0 · VERIFIED_ROCINANTE:** probado materialmente en la VM de referencia con evidencia reproducible.
- **R1 · STRONG_CANDIDATE:** soporte DLSS relevante y sin bloqueo conocido específico contra KVM/VM; candidato prioritario para prueba local.
- **R2 · CONDITIONAL:** prometedor o parcialmente compatible, pero exige prueba local por anticheat, modo online/offline, versión o ruta DLSS.
- **BLOCKED:** existe bloqueo conocido por VM o por Proton/Linux que invalida el caso actual.

**Regla:** documentación, marketing o inferencia no elevan un título a R0.

## 2. DLSS 5

**NBA 2K27** es la primera integración oficial publicada de DLSS 5 / 3D-Guided Neural Rendering. Sin embargo, en PC utiliza Easy Anti-Cheat y existe un antecedente anti-VM en NBA 2K26. Steam expone además una ruta de lanzamiento offline sin EAC. Por tanto no debe clasificarse como compatible con Rocinante hasta probar por separado ejecución offline, ejecución online y activación material de DLSS 5 dentro de KVM + passthrough.

| Juego | Tecnología | Estado | Motivo |
|---|---|---|---|
| NBA 2K27 | DLSS 5 Neural Rendering + SR + FG/MFG + Reflex | **R2 · CONDITIONAL · HIGH_VM_RISK** | DLSS 5 está publicado, pero la compatibilidad KVM no está demostrada. EAC y el antecedente NBA 2K26 obligan a separar offline/online antes de cualquier R0. |

## 3. DLSS 4 / 4.5 · candidatos fuertes

`R1` significa **candidato arquitectónico**, no “probado ya en Rocinante”.

| Juego | DLSS/RTX de interés | Estado |
|---|---|---|
| Cyberpunk 2077 | DLSS 4/4.5, MFG, Ray Reconstruction, Path Tracing | **R1** |
| DOOM: The Dark Ages | DLSS 4/4.5, MFG, RR, RT/PT | **R1** |
| Indiana Jones and the Great Circle | DLSS 4/4.5, MFG, RR, Path Tracing | **R1** |
| Black Myth: Wukong | DLSS 4, MFG, Full Ray Tracing | **R1** |
| Hogwarts Legacy | DLSS 4-class, Frame Generation, RT | **R1** |
| Resident Evil Requiem | DLSS 4/4.5-class, MFG, RT/PT | **R1** |
| PRAGMATA | DLSS 4/4.5-class, MFG, RT/PT | **R1** |
| 007 First Light | DLSS 4.5-class, Dynamic MFG, RT/PT | **R1** |
| Crimson Desert | DLSS 4-class, MFG, RT | **R1** |
| Phantom Blade Zero | DLSS 4, MFG, RT | **R2 · reciente / recent** |
| Marvel's Spider-Man 2 | DLSS 4-class, MFG, RT | **R1** |
| God of War Ragnarök | DLSS 4-class, MFG | **R1** |
| S.T.A.L.K.E.R. 2: Heart of Chornobyl | DLSS 4-class, MFG | **R1** |
| Stellar Blade | DLSS 4-class, MFG | **R1** |
| Lost Soul Aside | DLSS 4-class, MFG, RT | **R1** |
| Dying Light: The Beast | DLSS 4-class, MFG, RT | **R1** |
| Cronos: The New Dawn | DLSS 4-class, RT | **R1** |
| The Outer Worlds 2 | DLSS 4/4.5-class, MFG, RT | **R1** |
| WUCHANG: Fallen Feathers | DLSS 4-class, MFG | **R1** |
| NINJA GAIDEN 2 Black | DLSS 4-class, MFG | **R1** |
| Rise of the Ronin | DLSS 4-class, MFG | **R1** |
| FINAL FANTASY XVI | DLSS 4-class, MFG | **R1** |
| SILENT HILL 2 | DLSS 4-class, MFG | **R1** |
| Star Wars Jedi: Survivor | DLSS 4-class, FG/MFG path | **R1** |
| Remnant II | DLSS 4-class, MFG | **R1** |
| Dragon Age: The Veilguard | DLSS 4/4.5-class, MFG | **R1** |
| Avowed | DLSS 4-class, MFG | **R1** |
| Eternal Strands | DLSS 4-class, MFG | **R1** |
| Flintlock: The Siege of Dawn | DLSS 4-class, MFG | **R1** |
| Still Wakes the Deep | DLSS 4-class, MFG | **R1** |
| Layers of Fear (2023) | DLSS 4-class, MFG | **R1** |
| A Quiet Place: The Road Ahead | DLSS 4-class, MFG | **R1** |
| Immortals of Aveum | DLSS 4-class, MFG | **R1** |
| Ghostrunner 2 | DLSS 4-class, MFG | **R1** |
| The Thaumaturge | DLSS 4-class, MFG | **R1** |
| Jusant | DLSS 4-class, MFG | **R1** |
| Deliver Us Mars | DLSS 4-class, MFG, RT | **R1** |
| Lords of the Fallen | DLSS 4-class, MFG | **R1** |
| ICARUS | DLSS 4-class, MFG, RT | **R1** |
| EVERSPACE 2 | DLSS 4/4.5-class Super Resolution path | **R1** |
| Satisfactory | DLSS 4-class, MFG | **R1** |
| Deep Rock Galactic | DLSS 4/4.5-class path | **R1** |
| RoadCraft | DLSS 4-class, MFG | **R1** |
| inZOI | DLSS 4-class, MFG | **R1** |
| MindsEye | DLSS 4-class, MFG | **R1** |
| Frostpunk 2 | DLSS 4-class, MFG | **R1** |
| HITMAN World of Assassination | DLSS 4-class path | **R1** |
| Witchfire | DLSS 4-class path | **R1** |

## 4. Exclusiones actuales por VM / Proton

| Juego | Estado | Motivo |
|---|---|---|
| Marvel Rivals | **BLOCKED_VM** | Política publicada incluye VMware, KVM y VirtualBox entre entornos prohibidos mientras se ejecuta el juego. |
| Mecha BREAK | **BLOCKED_VM** | ACE ha mostrado bloqueo explícito de máquinas virtuales. |
| Fate Trigger | **BLOCKED_PROTON** | Launcher/anticheat ha requerido funciones de kernel no implementadas en Wine/Proton en informes públicos. |
| SCUM | **BLOCKED_PROTON** | No existe soporte Linux/Proton utilizable en el estado documentado de esta matriz. |

Títulos online con anticheat y política inestable respecto a KVM permanecen en R2 o fuera de la lista positiva hasta disponer de evidencia suficiente.

## 5. Juegos sin DLSS 4/5

**Stray no forma parte de la tabla DLSS 4/5.** Puede estudiarse mediante DX12/RT cuando proceda y NVIDIA Smooth Motion, pero esa ruta debe mostrarse separada para no confundir generación externa de frames con integración DLSS nativa.

## 6. Qué demuestra realmente la plataforma

```text
GPU física dedicada
+ passthrough PCIe
+ Linux virtualizado
+ Steam/Proton
+ NVAPI mediante DXVK-NVAPI
+ DLSS soportado por el juego
+ evidencia de ejecución
= gaming RTX reproducible dentro de VM
```

La futura sección WEB4 debe funcionar como **observatorio técnico vivo**, no como lista promocional. Cada prueba R0 registrará juego, fecha, AppID, Proton, driver NVIDIA, kernel, GPU, hipervisor, passthrough, SR/FG/MFG/RR/DLSS5, RT/PT, anticheat, política VM, resolución, FPS, incidencias y fuentes.

---

# EN · English

## 1. Criterion

This is **not a “games for Rocinante” ranking** or a hardware showcase. It is a technical matrix for Rocinante-like systems:

```text
Linux host / hypervisor
→ KVM/QEMU
→ desktop Linux VM
→ dedicated NVIDIA RTX GPU through PCIe passthrough
→ Steam
→ Proton / DXVK-NVAPI / VKD3D-Proton
→ Windows game
→ DLSS when supported by game and stack
```

Rocinante™ acts as the reference platform. The information should remain useful to equivalent virtualized Linux configurations.

### States

- **R0 · VERIFIED_ROCINANTE:** materially tested in the reference VM with reproducible evidence.
- **R1 · STRONG_CANDIDATE:** relevant DLSS support and no known KVM/VM-specific blocker; priority candidate for local testing.
- **R2 · CONDITIONAL:** promising or partially compatible but requires local validation because of anticheat, online/offline mode, version or DLSS path.
- **BLOCKED:** a known VM or Proton/Linux restriction currently invalidates the case.

**Rule:** documentation, marketing or inference cannot promote a title to R0.

## 2. DLSS 5

**NBA 2K27** is the first published official integration of DLSS 5 / 3D-Guided Neural Rendering. However, the PC version uses Easy Anti-Cheat and NBA 2K26 provides an anti-VM precedent. Steam also exposes an offline launch path without EAC. Therefore it must not be classified as Rocinante-compatible until offline execution, online execution and material DLSS 5 activation inside KVM + passthrough are tested separately.

| Game | Technology | State | Reason |
|---|---|---|---|
| NBA 2K27 | DLSS 5 Neural Rendering + SR + FG/MFG + Reflex | **R2 · CONDITIONAL · HIGH_VM_RISK** | DLSS 5 is published, but KVM compatibility is not demonstrated. EAC and the NBA 2K26 precedent require offline/online separation before any R0. |

## 3. DLSS 4 / 4.5 · strong candidates

`R1` means **architectural candidate**, not “already tested on Rocinante”.

| Game | DLSS/RTX feature of interest | State |
|---|---|---|
| Cyberpunk 2077 | DLSS 4/4.5, MFG, Ray Reconstruction, Path Tracing | **R1** |
| DOOM: The Dark Ages | DLSS 4/4.5, MFG, RR, RT/PT | **R1** |
| Indiana Jones and the Great Circle | DLSS 4/4.5, MFG, RR, Path Tracing | **R1** |
| Black Myth: Wukong | DLSS 4, MFG, Full Ray Tracing | **R1** |
| Hogwarts Legacy | DLSS 4-class, Frame Generation, RT | **R1** |
| Resident Evil Requiem | DLSS 4/4.5-class, MFG, RT/PT | **R1** |
| PRAGMATA | DLSS 4/4.5-class, MFG, RT/PT | **R1** |
| 007 First Light | DLSS 4.5-class, Dynamic MFG, RT/PT | **R1** |
| Crimson Desert | DLSS 4-class, MFG, RT | **R1** |
| Phantom Blade Zero | DLSS 4, MFG, RT | **R2 · recent** |
| Marvel's Spider-Man 2 | DLSS 4-class, MFG, RT | **R1** |
| God of War Ragnarök | DLSS 4-class, MFG | **R1** |
| S.T.A.L.K.E.R. 2: Heart of Chornobyl | DLSS 4-class, MFG | **R1** |
| Stellar Blade | DLSS 4-class, MFG | **R1** |
| Lost Soul Aside | DLSS 4-class, MFG, RT | **R1** |
| Dying Light: The Beast | DLSS 4-class, MFG, RT | **R1** |
| Cronos: The New Dawn | DLSS 4-class, RT | **R1** |
| The Outer Worlds 2 | DLSS 4/4.5-class, MFG, RT | **R1** |
| WUCHANG: Fallen Feathers | DLSS 4-class, MFG | **R1** |
| NINJA GAIDEN 2 Black | DLSS 4-class, MFG | **R1** |
| Rise of the Ronin | DLSS 4-class, MFG | **R1** |
| FINAL FANTASY XVI | DLSS 4-class, MFG | **R1** |
| SILENT HILL 2 | DLSS 4-class, MFG | **R1** |
| Star Wars Jedi: Survivor | DLSS 4-class, FG/MFG path | **R1** |
| Remnant II | DLSS 4-class, MFG | **R1** |
| Dragon Age: The Veilguard | DLSS 4/4.5-class, MFG | **R1** |
| Avowed | DLSS 4-class, MFG | **R1** |
| Eternal Strands | DLSS 4-class, MFG | **R1** |
| Flintlock: The Siege of Dawn | DLSS 4-class, MFG | **R1** |
| Still Wakes the Deep | DLSS 4-class, MFG | **R1** |
| Layers of Fear (2023) | DLSS 4-class, MFG | **R1** |
| A Quiet Place: The Road Ahead | DLSS 4-class, MFG | **R1** |
| Immortals of Aveum | DLSS 4-class, MFG | **R1** |
| Ghostrunner 2 | DLSS 4-class, MFG | **R1** |
| The Thaumaturge | DLSS 4-class, MFG | **R1** |
| Jusant | DLSS 4-class, MFG | **R1** |
| Deliver Us Mars | DLSS 4-class, MFG, RT | **R1** |
| Lords of the Fallen | DLSS 4-class, MFG | **R1** |
| ICARUS | DLSS 4-class, MFG, RT | **R1** |
| EVERSPACE 2 | DLSS 4/4.5-class Super Resolution path | **R1** |
| Satisfactory | DLSS 4-class, MFG | **R1** |
| Deep Rock Galactic | DLSS 4/4.5-class path | **R1** |
| RoadCraft | DLSS 4-class, MFG | **R1** |
| inZOI | DLSS 4-class, MFG | **R1** |
| MindsEye | DLSS 4-class, MFG | **R1** |
| Frostpunk 2 | DLSS 4-class, MFG | **R1** |
| HITMAN World of Assassination | DLSS 4-class path | **R1** |
| Witchfire | DLSS 4-class path | **R1** |

## 4. Current VM / Proton exclusions

| Game | State | Reason |
|---|---|---|
| Marvel Rivals | **BLOCKED_VM** | Published policy includes VMware, KVM and VirtualBox among prohibited environments while the game runs. |
| Mecha BREAK | **BLOCKED_VM** | ACE has shown explicit virtual-machine blocking. |
| Fate Trigger | **BLOCKED_PROTON** | Launcher/anticheat has required kernel functions not implemented in Wine/Proton in public reports. |
| SCUM | **BLOCKED_PROTON** | No usable Linux/Proton support exists in the state documented by this matrix. |

Online titles with anticheat and an unstable KVM policy remain R2 or outside the positive list until sufficient evidence exists.

## 5. Games without DLSS 4/5

**Stray is not part of the DLSS 4/5 table.** It may be studied through DX12/RT where appropriate and NVIDIA Smooth Motion, but that path must remain separate to avoid confusing external frame generation with native DLSS integration.

## 6. What the platform actually demonstrates

```text
physical dedicated GPU
+ PCIe passthrough
+ virtualized Linux
+ Steam/Proton
+ NVAPI through DXVK-NVAPI
+ game-supported DLSS
+ execution evidence
= reproducible RTX gaming inside a VM
```

The future WEB4 section should act as a **living technical observatory**, not a promotional list. Every R0 test will record game, date, AppID, Proton, NVIDIA driver, kernel, GPU, hypervisor, passthrough, SR/FG/MFG/RR/DLSS5, RT/PT, anticheat, VM policy, resolution, FPS, incidents and sources.

---

## Fuentes principales / Primary sources

- NVIDIA · DLSS 5 / NBA 2K27: https://www.nvidia.com/es-la/geforce/news/dlss-5-3d-guided-neural-rendering/
- NVIDIA · RTX/DLSS games: https://www.nvidia.com/en-us/geforce/news/nvidia-rtx-games-engines-apps/
- NVIDIA · Linux gaming / DLSS / Proton: https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/gaming.html
- Valve Proton · RTX 5090 / Frame Generation regression evidence: https://github.com/ValveSoftware/Proton/issues/8692
- Valve Proton · DOOM: The Dark Ages: https://github.com/ValveSoftware/Proton/issues/8690
- SteamDB · NBA 2K27 configuration: https://steamdb.info/app/4356430/config/
- Marvel Rivals · prohibited software/hardware policy: https://www.marvelrivals.com/guide/20250226/41348_1214569.html
- Valve Proton · Fate Trigger: https://github.com/ValveSoftware/Proton/issues/8988
- Valve Proton · Mecha BREAK: https://github.com/ValveSoftware/Proton/issues/8475
