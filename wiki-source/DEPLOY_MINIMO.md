# Despliegue mínimo de la Wiki
# Minimal Wiki deployment

## Objetivo

Reducir el mantenimiento manual de la Wiki a cuatro páginas estables y evitar que vuelva a convertirse en una copia paralela del repositorio.

Reduce manual Wiki maintenance to four stable pages and prevent it from becoming a parallel copy of the repository again.

---

# ES · Procedimiento

## Cambios imprescindibles

Realizar únicamente estas cuatro sustituciones en la Wiki pública:

| Página Wiki | Fuente que debe copiarse |
|---|---|
| `Home` | [`wiki-source/Home.md`](./Home.md) |
| `Manifiestos` | [`wiki-source/Manifiestos.md`](./Manifiestos.md) |
| `Analisis_Neodialecticos_Publicos` | [`wiki-source/Analisis_Neodialecticos_Publicos.md`](./Analisis_Neodialecticos_Publicos.md) |
| `_Sidebar` | [`wiki-source/_Sidebar.md`](./_Sidebar.md) |

## Páginas antiguas

No es necesario borrar inmediatamente todas las páginas temáticas antiguas.

1. Retirarlas de `_Sidebar` para que dejen de formar parte de la navegación principal.
2. Mantenerlas temporalmente como archivo histórico cuando contengan información útil.
3. No actualizarlas salvo que sean imprescindibles.
4. Trasladar al repositorio cualquier contenido canónico que sólo exista en una página antigua.
5. Cuando una página quede totalmente absorbida por el repositorio, puede eliminarse o conservarse con una nota de archivo.

Nota recomendada para páginas históricas:

```markdown
> **Página histórica no canónica.**
> El contenido actualizado y versionado se conserva en el repositorio principal.
> Consulte los enlaces de la página Home para acceder a la fuente vigente.
```

## Ritmo de mantenimiento

Actualizar la Wiki únicamente cuando cambie:

* la ruta de entrada;
* la guía de lectura;
* el mecanismo de participación;
* o la navegación principal.

No actualizarla por cada nuevo manifiesto, auditoría, análisis, edición o commit.

## Verificación posterior

Después de las cuatro sustituciones:

1. abrir `Home`;
2. probar los tres enlaces internos principales;
3. comprobar la Sidebar en una página distinta;
4. abrir los índices canónicos del repositorio;
5. confirmar que ninguna página principal exige duplicar listados completos.

---

# EN · Procedure

## Required changes

Perform only these four replacements in the public Wiki:

| Wiki page | Source to copy |
|---|---|
| `Home` | [`wiki-source/Home.md`](./Home.md) |
| `Manifiestos` | [`wiki-source/Manifiestos.md`](./Manifiestos.md) |
| `Analisis_Neodialecticos_Publicos` | [`wiki-source/Analisis_Neodialecticos_Publicos.md`](./Analisis_Neodialecticos_Publicos.md) |
| `_Sidebar` | [`wiki-source/_Sidebar.md`](./_Sidebar.md) |

## Older pages

There is no need to delete every older thematic page immediately.

1. Remove them from `_Sidebar` so they are no longer part of primary navigation.
2. Keep them temporarily as historical archives when they contain useful information.
3. Do not update them unless necessary.
4. Move to the repository any canonical content that exists only on an older page.
5. When a page has been fully absorbed by the repository, it may be deleted or retained with an archive notice.

Recommended notice for historical pages:

```markdown
> **Historical non-canonical page.**
> Updated and versioned content is preserved in the main repository.
> Use the links on the Home page to access the current source.
```

## Maintenance cadence

Update the Wiki only when the following changes:

* the entry route;
* the reading guide;
* the participation mechanism;
* or primary navigation.

Do not update it for every new manifesto, audit, analysis, edition or commit.

## Post-deployment verification

After the four replacements:

1. open `Home`;
2. test the three main internal links;
3. check the Sidebar from another page;
4. open the canonical repository indexes;
5. confirm that no primary page requires complete lists to be duplicated.

---

**Regla final / Final rule:**  
**Repositorio = contenido canónico y commits. Wiki = guía de uso estable.**  
**Repository = canonical content and commits. Wiki = stable usage guide.**