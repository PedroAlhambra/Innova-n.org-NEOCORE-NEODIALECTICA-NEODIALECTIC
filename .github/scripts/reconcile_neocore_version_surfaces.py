#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

GENERIC_REPLACEMENTS = {
    "## NEOCore™ 7.3 CANON ABIERTO · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™":
        "## NEOCore™ · CANON ABIERTO · Primera Capa Fractal Multicabeza™ + Capa Neoaxiomática™ + Soberanía de Síntesis™",
    "## NEOCore™ 7.3 OPEN CANON · First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™":
        "## NEOCore™ · OPEN CANON · First Fractal Multihead Layer™ + Neoaxiomatic Layer™ + Synthesis Sovereignty™",
}

TARGETS = [
    ROOT / "manifiestos" / "README.md",
    ROOT / "neoaxiomas" / "README.md",
    ROOT / "web4" / "README.md",
    ROOT / "wiki-source" / "README.md",
    ROOT / "propuestas" / "sintesis-abierta" / "README.md",
]

changed = []
for path in TARGETS:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in GENERIC_REPLACEMENTS.items():
        text = text.replace(old, new)

    if path.as_posix().endswith("web4/README.md"):
        text = text.replace(
            "**Frontera evolutiva pública activa / Active public evolutionary frontier:** NEOCore™ 7.3 CANON ABIERTO · canónico y reabrible / open canon, canonical and reopenable  ",
            "**Base del marco vigente / Current framework base:** [consultar versión vigente e histórico / read current version and history](../versiones/README.md)  ",
        )
        lines = []
        for line in text.splitlines():
            if line.startswith("> **Regla de versión / Version rule:**"):
                line = "> **Regla de versión / Version rule:** `PRE-7.3` identifica una baseline documental histórica de WEB4™. El estado vigente del núcleo se resuelve desde [`versiones/README.md`](../versiones/README.md); no se replica aquí. / `PRE-7.3` identifies a historical WEB4™ documentary baseline. Current core state is resolved from [`versiones/README.md`](../versiones/README.md) and is not duplicated here."
            lines.append(line)
        text = "\n".join(lines) + ("\n" if original.endswith("\n") else "")

    if path.as_posix().endswith("propuestas/sintesis-abierta/README.md"):
        # 7.3 is material provenance of this mechanism; keep the number but stop calling it CURRENT_VERSION.
        text = text.replace(
            "NEOCore™ 7.3 fija como base operativa vigente la evolución recursiva de SAN™",
            "NEOCore™ 7.3 fijó la evolución recursiva de SAN™ como capa de origen trazable",
        )
        text = text.replace(
            "NEOCore™ 7.3 fixes the recursive evolution of SAN™ as the current operating base",
            "NEOCore™ 7.3 fixed the recursive evolution of SAN™ as a traceable originating layer",
        )

    if text != original:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())

# LXXXII: remove a redundant dynamic-current label while preserving its 7.3-CANDIDATE genealogy.
p82 = ROOT / "manifiestos" / "82_ciencia_multidimensional_neodialectica_ES_EN.md"
if p82.exists():
    text = p82.read_text(encoding="utf-8")
    original = text
    text = text.replace(
        "**Estado / Status:** Público · Síntesis Abierta · NEOCore™ 7.3 CANON ABIERTO / Public · Open Synthesis · NEOCore™ 7.3 OPEN CANON  ",
        "**Estado / Status:** Público · Síntesis Abierta / Public · Open Synthesis  ",
    )
    if text != original:
        p82.write_text(text, encoding="utf-8")
        changed.append(p82.relative_to(ROOT).as_posix())

print("changed_files=")
for item in changed:
    print(f"- {item}")
