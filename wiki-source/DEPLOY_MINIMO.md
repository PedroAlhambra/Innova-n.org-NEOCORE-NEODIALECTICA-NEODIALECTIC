# Despliegue mínimo de la Wiki
# Minimal Wiki deployment

## Principio

La fuente editable y trazable está en `wiki-source/`. La Wiki pública debe recibir estas páginas sin introducir estados paralelos ni números de versión fuera de la cabecera del sidebar.

The editable, traceable source lives in `wiki-source/`. The public Wiki should receive these pages without introducing parallel states or version numbers outside the sidebar header.

## Archivos a proyectar / Files to project

- `Home.md`
- `Mapa_del_Marco.md`
- `Filosofia_y_NEOCore.md`
- `Manifiestos.md`
- `Neoaxiomas.md`
- `Sintesis_Abierta.md`
- `Participar.md`
- `Analisis_Neodialecticos_Publicos.md`
- `Obras_y_Cultura.md`
- `WEB4_y_Proyeccion.md`
- `Procedencia_Trazabilidad_y_Legal.md`
- `_Sidebar.md`

## Regla de nombres

Los nombres de archivo deben conservarse al proyectarlos para que los enlaces internos de la Wiki sean estables.

File names should be preserved when projecting them so that internal Wiki links remain stable.

## Postcheck mínimo / Minimum postcheck

1. Abrir Home / Open Home.
2. Confirmar que el sidebar carga / Confirm sidebar loads.
3. Recorrer todos los enlaces internos de las páginas nuevas / Follow all internal links on the new pages.
4. Confirmar que la versión vigente aparece sólo arriba en `_Sidebar.md` / Confirm the current version appears only at the top of `_Sidebar.md`.
5. Confirmar que los inventarios vivos remiten a índices canónicos del repositorio / Confirm living inventories point to canonical repository indexes.
6. Confirmar que ES y EN mantienen estructura equivalente / Confirm ES and EN keep equivalent structure.

## Límite operativo

GitHub no ofrece una API REST de contenidos equivalente para editar la Wiki como si fuera el árbol normal del repositorio. Por eso `wiki-source/` es la fuente trazable; la proyección al repositorio Git de la Wiki requiere una operación Git con credenciales que permitan escribir en la Wiki.

GitHub does not provide an equivalent repository-contents REST API for editing the Wiki as part of the normal repository tree. Therefore `wiki-source/` is the traceable source; projection to the Wiki Git repository requires a Git operation with credentials that allow Wiki writes.
