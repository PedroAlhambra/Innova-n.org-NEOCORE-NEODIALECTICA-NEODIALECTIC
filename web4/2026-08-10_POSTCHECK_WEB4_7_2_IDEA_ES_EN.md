# Postcheck WEB4™ · NEOCore™ 7.2 + IDEA

**Fecha / Date:** 2026-08-10  
**Estado / Status:** **OK EN REPOSITORIO / OK IN REPOSITORY**

## Alcance / Scope

Actualización de la portada WEB4™ y de la página IDEA tomando como referencia la base HTML anterior y el estado canónico actual del repositorio.

## WEB4™

- [x] `web4/index.html` creado como portada NEOCore™ 7.2.
- [x] Banner superior de **Neoaxiomas™**.
- [x] Banner superior de **Manifiestos**.
- [x] Inventarios obtenidos dinámicamente desde GitHub.
- [x] Fallback RAW → API pública de GitHub.
- [x] Rotación automática.
- [x] Navegación anterior/siguiente.
- [x] Pausa manual.
- [x] La rotación se detiene mientras el usuario lee un banner desplegado.
- [x] Lectura dentro del propio banner mediante panel desplazable.
- [x] El manifiesto seleccionado obtiene su contenido desde su archivo GitHub al abrirse.
- [x] Neoaxiomas ES/EN deduplicados por identificador.
- [x] NAX-01–NAX-14 y candidatos C-NAX-15–C-NAX-18 admitidos por el parser.
- [x] NEOCore™ 7.2, I–LXVIII + ∞, SAN™, Soberanía de Síntesis™, Fundación/Corporación futuras, Leónidas–Cancerbero™, NeoCronos™ e IDEA representados en portada.

## IDEA

- [x] `web4/idea/index.html` creado.
- [x] Pedro Martínez Alhambra se presenta en **tercera persona** en el cuerpo editorial.
- [x] La página explica la historia, no sólo los temas.
- [x] Incluye Satélites Casa de Luz Horizonte, Robert y SensFusión.
- [x] Conserva cronología 1997–2002 → Premio UPC 2002 → primera publicación 2026.
- [x] Distingue obra de origen y relación posterior con el marco.
- [x] Enlaza Amazon, ediciones, nodo documental, Press Kit, manifiesto XXXIII y guía Starkdr–Gritax.
- [x] Portada cargada desde el activo público del repositorio.

## Validación local previa al commit / Local validation before commit

- HTML parseado estructuralmente.
- JavaScript comprobado con `node --check` sin errores sintácticos.
- Búsqueda textual visible en IDEA: sin primera persona (`yo`, `mi`, `mis`, `me`, `escribí`, `creé`, `presenté`).
- Versiones descargables generadas junto al trabajo para despliegue manual si el hosting no sincroniza desde GitHub.

## Límite de verificación

Este postcheck confirma el **estado del repositorio**. No afirma despliegue efectivo en `innova-n.org`: la publicación en el hosting debe verificarse por la ruta de despliegue correspondiente.
