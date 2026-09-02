# Política de seguridad · Innova_N
# Security Policy · Innova_N

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## 1. Qué es un problema de seguridad

Esta política cubre vulnerabilidades técnicas o configuraciones que puedan permitir acceso no autorizado, ejecución de código, exposición de secretos o datos, escalado de privilegios, manipulación de integridad, abuso de automatizaciones o compromiso de infraestructura relacionada con este repositorio o con una proyección oficial de Innova_N.

Una objeción filosófica, factual, metodológica o de gobernanza **no es una vulnerabilidad de seguridad**: debe entrar por Síntesis Abierta™, Issues o Auditoría Pública según corresponda.

## 2. Versiones y superficies

- El estado público canónico del corpus se mantiene en la rama principal vigente del repositorio.
- WEB4™ pública y sus implementaciones de trabajo tienen ciclos de versión distintos del NEOCore™; una versión del marco no equivale a una versión de software.
- Si una vulnerabilidad sólo afecta a una rama, candidata, snapshot o artefacto histórico, indícalo con precisión.

## 3. Cómo reportar una vulnerabilidad

**No publiques detalles explotables en un Issue público.**

Ruta preferida:

1. abre la pestaña **Security** del repositorio;
2. si GitHub muestra la opción de **reportar una vulnerabilidad de forma privada**, utilízala;
3. incluye componente afectado, pasos mínimos de reproducción, impacto, condiciones necesarias, versión/ref/commit y cualquier mitigación conocida.

Si el reporte privado de vulnerabilidades no está habilitado o no aparece, evita publicar el exploit. Contacta con la persona mantenedora del repositorio mediante un canal privado disponible en GitHub. Si necesitas dejar constancia pública, abre únicamente un Issue mínimo que solicite un canal privado **sin incluir secretos, payloads, credenciales ni pasos de explotación**.

## 4. Qué información ayuda

- ruta, módulo o servicio afectado;
- commit/ref o URL pública afectada;
- precondiciones;
- pasos de reproducción seguros;
- impacto posible;
- si el problema ha sido explotado o sólo demostrado;
- evidencia técnica mínima;
- mitigación temporal, si existe;
- restricciones de divulgación responsable que debamos conocer.

No incluyas datos personales de terceros salvo que sean imprescindibles y exista base legítima para compartirlos.

## 5. Divulgación responsable

Se intentará:

1. confirmar recepción;
2. reproducir y clasificar;
3. limitar exposición;
4. corregir o mitigar;
5. verificar la reparación;
6. documentar públicamente lo necesario cuando hacerlo ya no incremente el riesgo.

Una vulnerabilidad puede conservar traza y genealogía sin publicar material que facilite explotación.

## 6. Fuera de alcance

Salvo que demuestren impacto técnico real, no se consideran vulnerabilidades:

- desacuerdo conceptual o político;
- falta de una función deseada;
- spam ordinario;
- enlaces externos caídos;
- errores tipográficos;
- afirmaciones no verificadas sobre terceros;
- ingeniería social dirigida a personas fuera de la infraestructura del proyecto;
- hallazgos obtenidos mediante daño, acceso no autorizado o degradación deliberada innecesaria.

## 7. Investigación de buena fe

Se agradece la investigación orientada a reducir riesgo y que minimice daño, acceso a datos, persistencia y afectación a terceros. No se autoriza por esta política ninguna actividad que sea ilegal, destructiva o que exceda permisos legítimos.

---

# EN · English

## 1. What counts as a security issue

This policy covers technical vulnerabilities or configurations that may enable unauthorised access, code execution, disclosure of secrets or data, privilege escalation, integrity manipulation, abuse of automation or compromise of infrastructure related to this repository or an official Innova_N projection.

A philosophical, factual, methodological or governance objection **is not a security vulnerability**; it belongs in Open Synthesis™, Issues or Public Audit as appropriate.

## 2. Versions and surfaces

- The canonical public corpus state is maintained on the repository's current main branch.
- Public WEB4™ and its working implementations have version cycles distinct from NEOCore™; a framework version is not a software version.
- If a vulnerability affects only a branch, candidate, snapshot or historical artefact, identify it precisely.

## 3. How to report a vulnerability

**Do not publish exploitable details in a public Issue.**

Preferred route:

1. open the repository's **Security** tab;
2. if GitHub offers **private vulnerability reporting**, use it;
3. include the affected component, minimal reproduction steps, impact, required conditions, version/ref/commit and any known mitigation.

If private vulnerability reporting is not enabled or not visible, do not publish the exploit. Contact the repository maintainer through an available private GitHub channel. If a public trace is necessary, open only a minimal Issue requesting a private channel **without secrets, payloads, credentials or exploitation steps**.

## 4. Useful report information

- affected path, module or service;
- affected commit/ref or public URL;
- preconditions;
- safe reproduction steps;
- possible impact;
- whether exploitation has occurred or is only demonstrated;
- minimal technical evidence;
- temporary mitigation, if known;
- responsible-disclosure constraints we should know about.

Do not include third-party personal data unless essential and legitimately shareable.

## 5. Responsible disclosure

The project will seek to:

1. acknowledge receipt;
2. reproduce and classify;
3. limit exposure;
4. fix or mitigate;
5. verify the repair;
6. document what is necessary publicly once doing so no longer increases risk.

A vulnerability may retain trace and genealogy without publishing material that facilitates exploitation.

## 6. Out of scope

Unless they demonstrate real technical impact, the following are not security vulnerabilities:

- conceptual or political disagreement;
- absence of a desired feature;
- ordinary spam;
- broken external links;
- typographical errors;
- unverified claims about third parties;
- social engineering aimed at people outside project infrastructure;
- findings obtained through unnecessary damage, unauthorised access or deliberate degradation.

## 7. Good-faith research

Research intended to reduce risk and minimise damage, data access, persistence and third-party impact is appreciated. This policy does not authorise unlawful, destructive activity or activity beyond legitimate permission.
