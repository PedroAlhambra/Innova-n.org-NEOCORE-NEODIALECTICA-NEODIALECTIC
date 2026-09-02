# Security Policy · Innova_N
# Política de seguridad · Innova_N

**Canonical GitHub location / Ubicación canónica para GitHub:** `.github/SECURITY.md`  
**Scope / Ámbito:** public repository, official WEB4™ projections and related project infrastructure / repositorio público, proyecciones oficiales WEB4™ e infraestructura relacionada del proyecto

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Supported Versions / Versiones admitidas

Innova_N separa las versiones del marco conceptual NEOCore™ de las versiones de software y de las candidatas WEB4™. Para seguridad técnica, la referencia soportada es la superficie pública vigente y el estado activo de la rama principal, salvo indicación expresa en sentido contrario.

| Superficie | Estado de soporte de seguridad |
|---|---|
| `main` del repositorio público canónico | ✅ Soportado |
| WEB4™ pública actualmente proyectada | ✅ Soportada |
| Candidata privada activa de WEB4™ | ✅ Se revisa dentro de su ciclo privado |
| Ramas/snapshots históricos | ⚠️ Sólo si el riesgo sigue afectando a una superficie vigente |
| Forks o copias de terceros | ❌ No mantenidos por Innova_N |

Si una vulnerabilidad sólo afecta a una rama, candidata, snapshot o artefacto histórico, indícalo con precisión.

## Reporting a Vulnerability / Notificar una vulnerabilidad

**No publiques detalles explotables, secretos, credenciales, payloads ni pasos de explotación en un Issue público, una Discussion o un Pull Request.**

Ruta preferida:

1. abre la pestaña **Security and quality** del repositorio;
2. entra en **Security policy** o, si GitHub ofrece la opción, en **Report a vulnerability / Informar de una vulnerabilidad**;
3. utiliza el canal privado de vulnerabilidades de GitHub cuando esté habilitado;
4. incluye componente afectado, commit/ref o URL, precondiciones, pasos mínimos de reproducción seguros, impacto, evidencia técnica mínima y mitigación conocida si existe.

Si GitHub no ofrece todavía un canal privado de vulnerabilidades en este repositorio, **no publiques el exploit**. Contacta con el mantenedor mediante un canal privado disponible. Si necesitas dejar una traza pública, limita el Issue a solicitar un canal privado sin exponer información explotable.

## Qué es un problema de seguridad

Esta política cubre vulnerabilidades técnicas o configuraciones que puedan permitir acceso no autorizado, ejecución de código, exposición de secretos o datos, escalado de privilegios, manipulación de integridad, abuso de automatizaciones o compromiso de infraestructura relacionada con este repositorio o con una proyección oficial de Innova_N.

Una objeción filosófica, factual, metodológica o de gobernanza **no es una vulnerabilidad de seguridad**: debe entrar por Síntesis Abierta™, Issues o Auditoría Pública según corresponda.

## Información útil para el reporte

Siempre que sea posible, aporta:

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

## Proceso de respuesta y divulgación responsable

El proyecto intentará:

1. confirmar recepción;
2. reproducir y clasificar;
3. limitar exposición;
4. corregir o mitigar;
5. verificar la reparación;
6. documentar públicamente lo necesario cuando hacerlo ya no incremente el riesgo.

Una vulnerabilidad puede conservar traza y genealogía sin publicar material que facilite explotación.

## Fuera de alcance

Salvo que demuestren impacto técnico real, no se consideran vulnerabilidades:

- desacuerdo conceptual o político;
- falta de una función deseada;
- spam ordinario;
- enlaces externos caídos;
- errores tipográficos;
- afirmaciones no verificadas sobre terceros;
- ingeniería social dirigida a personas fuera de la infraestructura del proyecto;
- hallazgos obtenidos mediante daño, acceso no autorizado o degradación deliberada innecesaria.

## Investigación de buena fe

Se agradece la investigación orientada a reducir riesgo y que minimice daño, acceso a datos, persistencia y afectación a terceros. Esta política no autoriza ninguna actividad ilegal, destructiva o que exceda permisos legítimos.

---

# EN · English

## Supported Versions

Innova_N separates conceptual NEOCore™ versions from software versions and WEB4™ candidates. For technical security, the supported reference is the current public surface and the active state of the default branch unless explicitly stated otherwise.

| Surface | Security support status |
|---|---|
| Canonical public repository `main` | ✅ Supported |
| Currently projected public WEB4™ | ✅ Supported |
| Active private WEB4™ candidate | ✅ Reviewed within its private lifecycle |
| Historical branches/snapshots | ⚠️ Only where the risk still affects a current surface |
| Third-party forks or copies | ❌ Not maintained by Innova_N |

If a vulnerability affects only a branch, candidate, snapshot or historical artefact, identify it precisely.

## Reporting a Vulnerability

**Do not publish exploitable details, secrets, credentials, payloads or exploitation steps in a public Issue, Discussion or Pull Request.**

Preferred route:

1. open the repository's **Security and quality** tab;
2. open **Security policy** or, when GitHub exposes it, **Report a vulnerability**;
3. use GitHub private vulnerability reporting when enabled;
4. include the affected component, commit/ref or URL, preconditions, safe minimal reproduction steps, impact, minimal technical evidence and any known mitigation.

If GitHub does not yet expose a private vulnerability-reporting channel for this repository, **do not publish the exploit**. Contact the maintainer through an available private channel. If a public trace is necessary, limit the Issue to requesting a private channel without exposing exploitable information.

## What counts as a security issue

This policy covers technical vulnerabilities or configurations that may enable unauthorised access, code execution, disclosure of secrets or data, privilege escalation, integrity manipulation, abuse of automation or compromise of infrastructure related to this repository or an official Innova_N projection.

A philosophical, factual, methodological or governance objection **is not a security vulnerability**; it belongs in Open Synthesis™, Issues or Public Audit as appropriate.

## Useful report information

Whenever possible, include:

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

## Response process and responsible disclosure

The project will seek to:

1. acknowledge receipt;
2. reproduce and classify;
3. limit exposure;
4. fix or mitigate;
5. verify the repair;
6. document what is necessary publicly once doing so no longer increases risk.

A vulnerability may retain trace and genealogy without publishing material that facilitates exploitation.

## Out of scope

Unless they demonstrate real technical impact, the following are not security vulnerabilities:

- conceptual or political disagreement;
- absence of a desired feature;
- ordinary spam;
- broken external links;
- typographical errors;
- unverified claims about third parties;
- social engineering aimed at people outside project infrastructure;
- findings obtained through unnecessary damage, unauthorised access or deliberate degradation.

## Good-faith research

Research intended to reduce risk and minimise damage, data access, persistence and third-party impact is appreciated. This policy does not authorise unlawful, destructive activity or activity beyond legitimate permission.