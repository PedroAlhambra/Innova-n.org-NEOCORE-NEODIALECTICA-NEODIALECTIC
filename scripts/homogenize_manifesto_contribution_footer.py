from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFESTOS_DIR = ROOT / "manifiestos"

ES_BLOCK = """<!-- SAN-CONTRIBUTION-ES-START -->
### Cómo aportar a esta Síntesis Abierta

Antes de aportar, lee el manifiesto completo y el protocolo operativo. Presenta una contribución trazable con contexto, fuente o experiencia, genealogía, tipo de aporte y delta propuesto. Las aportaciones se abren mediante la plantilla pública de GitHub.

* [Cómo aportar a la Síntesis Abierta Neodialéctica™](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Abrir una aportación con la plantilla pública](../.github/ISSUE_TEMPLATE/sintesis_abierta_aporte.md)
<!-- SAN-CONTRIBUTION-ES-END -->
"""

EN_BLOCK = """<!-- SAN-CONTRIBUTION-EN-START -->
### How to contribute to this Open Synthesis

Before contributing, read the full manifesto and the operational protocol. Submit a traceable contribution with context, source or experience, genealogy, contribution type and proposed delta. Contributions are opened through the public GitHub template.

* [How to contribute to Neodialectical Open Synthesis™](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)
* [Open a contribution with the public template](../.github/ISSUE_TEMPLATE/sintesis_abierta_aporte.md)
<!-- SAN-CONTRIBUTION-EN-END -->
"""

OLD_LINES = {
    "* [Protocolo operativo actual para aportar](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)\n",
    "* [Current operational contribution protocol](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)\n",
}


def remove_existing_blocks(text: str) -> str:
    text = re.sub(
        r"\n?<!-- SAN-CONTRIBUTION-ES-START -->.*?<!-- SAN-CONTRIBUTION-ES-END -->\n?",
        "\n",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"\n?<!-- SAN-CONTRIBUTION-EN-START -->.*?<!-- SAN-CONTRIBUTION-EN-END -->\n?",
        "\n",
        text,
        flags=re.S,
    )
    for line in OLD_LINES:
        text = text.replace(line, "")
    return text


def insert_before_heading(text: str, heading: str, block: str) -> str:
    marker = f"\n{heading}\n"
    pos = text.find(marker)
    if pos == -1:
        raise ValueError(f"Missing heading: {heading}")
    return text[:pos].rstrip() + "\n\n" + block.rstrip() + "\n\n" + text[pos + 1 :]


def process(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = remove_existing_blocks(original)
    text = insert_before_heading(text, "## Navegación", ES_BLOCK)
    text = insert_before_heading(text, "## Navigation", EN_BLOCK)
    text = text.rstrip() + "\n"
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    changed: list[str] = []
    failures: list[str] = []
    for path in sorted(MANIFESTOS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        content = path.read_text(encoding="utf-8")
        if "**Manifiesto / Manifesto:**" not in content:
            continue
        try:
            if process(path):
                changed.append(str(path.relative_to(ROOT)))
        except ValueError as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")

    if failures:
        raise SystemExit("\n".join(failures))

    print(f"Updated {len(changed)} manifesto files")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
