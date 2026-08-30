from pathlib import Path
import re
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
SYNC_PATH = ROOT / ".github/scripts/sync_neoaxiom_manifest_relations.py"
spec = importlib.util.spec_from_file_location("neo_rel_sync", SYNC_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

README = ROOT / "neoaxiomas/README.md"
START = mod.START
END = mod.END

problems = []
readme = README.read_text(encoding="utf-8", errors="replace")

for ident, filename in mod.DOC_NAMES.items():
    doc = ROOT / "neoaxiomas" / filename
    if not doc.exists():
        problems.append(f"{ident}: missing own document / falta documento propio")
        continue
    text = doc.read_text(encoding="utf-8", errors="replace")
    if START not in text or END not in text:
        problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: {ident} lacks managed relation block")
    if "## Relaciones con manifiestos / Relations with Manifestos" not in text:
        problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: {ident} lacks bilingual relation heading")
    for roman, _, _, manifest in mod.REL[ident]:
        rel = f"../manifiestos/{manifest}"
        if rel not in text:
            problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: {ident} missing {roman} in own document")
        if rel not in readme:
            problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: README missing {ident} -> {roman}")
        if not (ROOT / "manifiestos" / manifest).exists():
            problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: missing target {manifest}")

    row = next((line for line in readme.splitlines() if line.startswith(f"| [**{ident} ·")), None)
    if row is None:
        problems.append(f"NEOAXIOM_READABILITY_FAILURE: README row missing for {ident}")
    elif len([c for c in row.strip().strip('|').split('|')]) < 4:
        problems.append(f"NEOAXIOM_MANIFEST_RELATION_FAILURE: README has no manifesto relation column for {ident}")

if problems:
    print("NEOAXIOM_MANIFEST_RELATIONS FAIL")
    for p in problems:
        print("FAIL:", p)
    raise SystemExit(1)

print("NEOAXIOM_MANIFEST_RELATIONS PASS NAX-01..NAX-14 README+OWN_DOCUMENTS")
