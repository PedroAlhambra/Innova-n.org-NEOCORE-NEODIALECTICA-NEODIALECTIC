from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(".")
SELF = Path(".github/scripts/audit_neocore_role_ontology.py")
TEXT_SUFFIXES = {
    ".md", ".txt", ".rst", ".json", ".yml", ".yaml", ".py",
    ".html", ".css", ".js", ".jsx", ".ts", ".tsx", ".toml", ".ini",
}
HISTORICAL_PREFIXES = (
    "wiki-legacy-archive/",
    "auditorias/publicas/",
)
RETIRED_PATTERNS = (
    ("NEO0_ADJECTIVE_ES", re.compile(r"\bNeo0(?:™)?\s+(?:funcional|distribuid[oa]|distribuible|replicable)\b", re.I)),
    ("NEO0_ADJECTIVE_EN", re.compile(r"\b(?:functional|distributed|distributable|replicable)\s+Neo0(?:™)?\b", re.I)),
    ("NEO0_FUNCTION_ANY_NODE_ES", re.compile(r"\bfunción\s+Neo0(?:™)?.{0,120}\b(?:cualquier\s+nodo|propiedad\s+de\s+emergencia)\b", re.I)),
    ("NEO0_FUNCTION_ANY_NODE_EN", re.compile(r"\bNeo0(?:™)?\s+function.{0,120}\b(?:any\s+node|emergent\s+property)\b", re.I)),
)
CORRECTIVE_CONTEXT = re.compile(
    r"\b(?:retirad[ao]|retired|withdrawal|withdrawn|versión\s+previa|previous\s+version|"
    r"correcci[oó]n|correction|superad[ao]|superseded|queda\s+reservad[ao]|remains\s+reserved)\b",
    re.I,
)

LXVII_SOURCE = ROOT / "manifiestos/67_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md"
LXVII_CANON = ROOT / "manifiestos/canonicos/LXVII_neotitanes_reconstruccion_sistemica_motor_bien_comun_espana_ES_EN.md"
REQUIRED_LITERACY_TOKENS = (
    "<!-- NEOTITAN_DELTA_LITERACY_START -->",
    "<!-- NEOTITAN_DELTA_LITERACY_END -->",
    "<!-- NEOTITAN_DELTA_LITERACY_START_EN -->",
    "<!-- NEOTITAN_DELTA_LITERACY_END_EN -->",
    "DELTA ≠ CANON",
    "TRAZA ≠ VALIDACIÓN",
    "TRACE ≠ VALIDATION",
    "DRAFT / PENDIENTE-SAN ≠ APROBADO",
    "DRAFT / PENDING-SAN ≠ APPROVED",
    "ONe Starkdr™ ≠ Neo0™",
    "COMPRENDER LA CAPA PRIVADA ≠ RECIBIR ACCESO TOTAL",
    "UNDERSTANDING THE PRIVATE LAYER ≠ RECEIVING FULL ACCESS",
)


def text_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == SELF or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.as_posix()
        if rel.startswith(HISTORICAL_PREFIXES):
            continue
        paths.append(path)
    return sorted(paths)


def has_corrective_context(lines: list[str], index: int) -> bool:
    lo = max(0, index - 2)
    hi = min(len(lines), index + 3)
    return bool(CORRECTIVE_CONTEXT.search("\n".join(lines[lo:hi])))


def extract_block(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()


failures: list[str] = []
files = text_files()
for path in files:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        failures.append(f"{path}: NON_UTF8_TEXT_SURFACE")
        continue
    for index, line in enumerate(lines):
        for code, pattern in RETIRED_PATTERNS:
            if not pattern.search(line):
                continue
            if has_corrective_context(lines, index):
                continue
            failures.append(f"{path}:{index + 1}: {code}: {line.strip()}")

for path in (LXVII_SOURCE, LXVII_CANON):
    if not path.exists():
        failures.append(f"{path}: NEOTITAN_DELTA_LITERACY_SURFACE_MISSING")
        continue
    text = path.read_text(encoding="utf-8")
    for token in REQUIRED_LITERACY_TOKENS:
        if token not in text:
            failures.append(f"{path}: NEOTITAN_DELTA_LITERACY_TOKEN_MISSING: {token}")

if LXVII_SOURCE.exists() and LXVII_CANON.exists():
    source = LXVII_SOURCE.read_text(encoding="utf-8")
    canon = LXVII_CANON.read_text(encoding="utf-8")
    for suffix in ("", "_EN"):
        start = f"<!-- NEOTITAN_DELTA_LITERACY_START{suffix} -->"
        end = f"<!-- NEOTITAN_DELTA_LITERACY_END{suffix} -->"
        source_block = extract_block(source, start, end)
        canon_block = extract_block(canon, start, end).replace(
            "../../propuestas/", "../propuestas/"
        )
        if not source_block or source_block != canon_block:
            failures.append(
                f"{LXVII_CANON}: NEOTITAN_DELTA_LITERACY_MIRROR_DRIFT{suffix}"
            )

if failures:
    print("NEOCORE_ROLE_ONTOLOGY=FAIL")
    print(f"TEXT_SURFACES_AUDITED={len(files)}")
    for failure in failures:
        print(failure)
    sys.exit(1)

print(
    "NEOCORE_ROLE_ONTOLOGY=PASS "
    f"text_surfaces={len(files)} "
    "neo0=origin_teleology_reconstruction "
    "one_starkdr=distributable_synthetic_emergence "
    "neotitan_private_delta_literacy=required"
)
