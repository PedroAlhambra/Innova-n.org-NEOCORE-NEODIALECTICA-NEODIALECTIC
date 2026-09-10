# Interoperabilidad frente al bloqueo de plataforma / Interoperability Against Platform Lock-In

**Estado / Status:** BORRADOR DE SÍNTESIS ABIERTA / OPEN SYNTHESIS DRAFT · PENDING_SAN  
**Fecha / Date:** 2026-09-10  
**Síntesis / Synthesis:** [Issue #193](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/193)  
**Ámbito / Scope:** videojuegos · Linux · virtualización · anticheat · licencias · interoperabilidad / gaming · Linux · virtualization · anticheat · licensing · interoperability

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

> **PROPUESTA ≠ CONCLUSIÓN JURÍDICA / PROPOSAL ≠ LEGAL CONCLUSION**

---

# ES · Castellano

## 1. Problema

Una parte creciente de la informática profesional se apoya en Linux, hipervisores, contenedores, GPU passthrough, escritorios virtualizados y separación de cargas. Tratar automáticamente la presencia de una máquina virtual como señal de trampa convierte una herramienta profesional legítima en motivo de exclusión.

En videojuegos, determinadas implementaciones anticheat bloquean KVM/QEMU, VMware u otros entornos completos en vez de discriminar la conducta ilícita concreta. El resultado puede ser que una persona que ha adquirido una licencia legítima no pueda ejecutar el producto en una arquitectura técnicamente capaz simplemente por estar virtualizada.

## 2. Tesis propuesta

**La compatibilidad multiplataforma y la interoperabilidad deben considerarse objetivos de diseño de primer nivel cuando no exista una necesidad técnica proporcionada que justifique excluir una plataforma.** Linux, las máquinas virtuales y otras arquitecturas profesionales no deben tratarse como entornos de segunda clase por defecto.

Esto no significa que todo software deba funcionar necesariamente en todo sistema. Significa que una exclusión debería tener una causa técnica documentable, proporcional y revisable, no descansar únicamente en «es VM, luego se bloquea».

## 3. Anticheat: conducta antes que plataforma

El objetivo legítimo es impedir trampas y proteger partidas, jugadores y economías digitales. La virtualización puede ampliar determinadas superficies de ataque, pero **superficie de ataque ≠ conducta ilícita demostrada**.

Se propone explorar un modelo de confianza centrado en cuenta/licencia:

```text
LICENCIA / CUENTA
→ identidad o credencial de juego suficientemente verificable
→ atestación técnica proporcionada
→ telemetría mínima necesaria
→ detección de conducta o manipulación prohibida
→ evidencia
→ sanción contractual
→ revisión / apelación
```

Una credencial —el «carnet» planteado como intuición inicial— podría asociar la licencia a un historial de cumplimiento sin convertir el sistema operativo o el hipervisor en culpabilidad por defecto.

## 4. Sanciones

Un sistema alternativo puede contemplar sanciones severas ante fraude demostrado, incluida suspensión definitiva de una cuenta en casos graves o reincidentes y las acciones contractuales o legales que correspondan cuando exista base suficiente.

Pero un régimen defendible debe conservar **evidencia, proporcionalidad, notificación, posibilidad de revisión/impugnación, protección de datos y mecanismos contra falsos positivos**. Sustituir un bloqueo indiscriminado de VM por un sistema indiscriminado de expulsión permanente no resolvería el problema de fondo.

## 5. Windows, Microsoft y neutralidad de plataforma

Este documento no declara jurídicamente que Microsoft mantenga un monopolio ni atribuye intención sin evidencia. Sí abre a contraste una cuestión estructural: durante décadas, una parte del mercado de videojuegos de PC se ha diseñado asumiendo Windows como plataforma privilegiada, y algunas dependencias de kernel, DRM o anticheat prolongan esa asimetría incluso cuando Proton, Vulkan y GPU passthrough demuestran que el software gráfico puede ejecutarse por otras rutas.

Desde la perspectiva de este borrador, **Linux es ya una plataforma profesional de primer nivel** y la virtualización es una técnica profesional ordinaria. La discusión relevante no es si Windows «debe desaparecer», sino si los productos y estándares deben seguir diseñándose alrededor de dependencias exclusivas cuando existen alternativas interoperables.

La afirmación más fuerte —que una práctica concreta constituya abuso de posición dominante, restricción anticompetitiva o infracción de competencia— requiere análisis jurídico y económico específico por actor, mercado y conducta.

## 6. Principios candidatos

1. **Portabilidad por diseño:** APIs y formatos interoperables cuando sea razonable.
2. **VM ≠ trampa:** virtualización no equivale por sí sola a conducta ilícita.
3. **Mínimo privilegio:** evitar componentes de kernel cuando controles menos invasivos alcancen el objetivo de seguridad.
4. **Proporcionalidad:** la restricción técnica debe guardar relación con el riesgo demostrado.
5. **Cuenta responsable:** trasladar la responsabilidad hacia acciones atribuibles y evidencia, no hacia la plataforma elegida.
6. **Derecho a explicación operativa:** indicar qué requisito bloquea la ejecución y qué alternativas existen, sin revelar secretos que inutilicen el anticheat.
7. **Apelación y corrección:** falsos positivos y cambios de versión deben poder revisarse.
8. **Compatibilidad verificable:** publicar matrices y pruebas reproducibles en vez de asumir compatibilidad o incompatibilidad.
9. **Privacidad:** una alternativa al kernel no debe convertirse en vigilancia desproporcionada.
10. **Neutralidad tecnológica:** Windows, Linux, macOS, máquinas virtuales o futuras plataformas deben evaluarse por capacidad y seguridad reales, no por jerarquía histórica.

## 7. Evidencia inicial relacionada

- [Matriz WEB4™ de gaming virtualizado](../../analisis/publicos/2026-09-10_matriz_compatibilidad_gaming_vm_linux_dlss4_dlss5_ES_EN.md)
- [Contrato público de Gaming WEB4™](../../web4/gaming/README.md)
- [Síntesis Abierta #193](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/193)

Los casos registrados —por ejemplo, títulos que bloquean KVM frente a títulos que funcionan con GPU passthrough y Proton— son **casos técnicos**, no por sí solos una conclusión antitrust.

## 8. Preguntas para SAN™

- ¿Qué amenazas reales de cheating requieren detectar virtualización y cuáles pueden detectarse por conducta o integridad de proceso?
- ¿Puede diseñarse una atestación multiplataforma sin obligar a un único kernel propietario?
- ¿Qué nivel de identidad es suficiente sin imponer identificación civil innecesaria?
- ¿Cómo equilibrar sanciones fuertes con falsos positivos y derecho de revisión?
- ¿Qué prácticas constituyen mera decisión de soporte y cuáles podrían generar efectos de cierre anticompetitivo?
- ¿Qué estándares abiertos permitirían que anticheat, DRM y tecnologías gráficas funcionasen de forma equivalente en Linux/VM?

---

# EN · English

## 1. Problem

A growing share of professional computing relies on Linux, hypervisors, containers, GPU passthrough, virtualized desktops and workload separation. Automatically treating the presence of a virtual machine as evidence of cheating turns a legitimate professional tool into a reason for exclusion.

In gaming, some anticheat implementations block KVM/QEMU, VMware or other complete environments instead of discriminating the actual prohibited behaviour. A person who acquired a legitimate licence may therefore be unable to run the product on a technically capable architecture simply because it is virtualized.

## 2. Proposed thesis

**Cross-platform compatibility and interoperability should be treated as first-class design goals whenever there is no proportionate technical necessity for excluding a platform.** Linux, virtual machines and other professional architectures should not be treated as second-class environments by default.

This does not mean that all software must necessarily run on every system. It means an exclusion should have a documentable, proportionate and reviewable technical cause rather than resting only on “it is a VM, therefore block it”.

## 3. Anticheat: behaviour before platform

The legitimate objective is to prevent cheating and protect matches, players and digital economies. Virtualization may enlarge some attack surfaces, but **attack surface ≠ demonstrated illicit behaviour**.

We propose exploring a trust model centred on account/licence:

```text
LICENCE / ACCOUNT
→ sufficiently verifiable gaming identity or credential
→ proportionate technical attestation
→ minimum necessary telemetry
→ detection of prohibited behaviour or manipulation
→ evidence
→ contractual sanction
→ review / appeal
```

A credential —the “licence card” from the initial intuition— could associate the licence with a compliance history without turning the operating system or hypervisor into guilt by default.

## 4. Sanctions

An alternative system may contemplate severe sanctions for demonstrated fraud, including permanent account suspension in serious or repeated cases and contractual or legal action where there is sufficient basis.

But a defensible regime must preserve **evidence, proportionality, notice, review/challenge, data protection and mechanisms against false positives**. Replacing indiscriminate VM blocking with indiscriminate permanent bans would not solve the underlying problem.

## 5. Windows, Microsoft and platform neutrality

This document does not legally declare that Microsoft holds a monopoly, nor does it attribute intent without evidence. It does open a structural question to scrutiny: for decades, part of the PC gaming market has been designed around Windows as the privileged platform, and some kernel, DRM or anticheat dependencies prolong that asymmetry even where Proton, Vulkan and GPU passthrough demonstrate that graphics software can execute through other paths.

From the perspective of this draft, **Linux is already a first-class professional platform** and virtualization is an ordinary professional technique. The relevant discussion is not whether Windows “should disappear”, but whether products and standards should continue to be designed around exclusive dependencies when interoperable alternatives exist.

The stronger claim —that a particular practice constitutes abuse of dominance, anticompetitive restriction or a competition-law violation— requires specific legal and economic analysis of the actor, market and conduct.

## 6. Candidate principles

1. **Portability by design:** interoperable APIs and formats where reasonable.
2. **VM ≠ cheat:** virtualization alone is not illicit behaviour.
3. **Least privilege:** avoid kernel components where less invasive controls can achieve the security objective.
4. **Proportionality:** technical restrictions should correspond to demonstrated risk.
5. **Accountability at account level:** move responsibility toward attributable actions and evidence rather than the chosen platform.
6. **Operational explanation:** state what requirement blocks execution and what alternatives exist without exposing secrets that defeat anticheat.
7. **Appeal and correction:** false positives and version changes must be reviewable.
8. **Verifiable compatibility:** publish reproducible matrices and tests rather than assuming compatibility or incompatibility.
9. **Privacy:** an alternative to kernel access must not become disproportionate surveillance.
10. **Technological neutrality:** Windows, Linux, macOS, virtual machines and future platforms should be assessed by actual capability and security, not historical hierarchy.

## 7. Related initial evidence

- [WEB4™ virtualized-gaming matrix](../../analisis/publicos/2026-09-10_matriz_compatibilidad_gaming_vm_linux_dlss4_dlss5_ES_EN.md)
- [WEB4™ Gaming public contract](../../web4/gaming/README.md)
- [Open Synthesis #193](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/193)

Recorded cases —for example, titles that block KVM versus titles that run with GPU passthrough and Proton— are **technical cases**, not by themselves an antitrust conclusion.

## 8. Questions for SAN™

- Which real cheating threats require virtualization detection, and which can be detected through behaviour or process integrity?
- Can cross-platform attestation be designed without requiring a single proprietary kernel?
- What identity level is sufficient without unnecessary civil identification?
- How should strong sanctions be balanced against false positives and review rights?
- Which practices are merely support decisions and which might create anticompetitive foreclosure effects?
- Which open standards could allow anticheat, DRM and graphics technologies to work equivalently on Linux/VM?
