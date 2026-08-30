"""Validate the Neoaxiom candidate frontier without rewriting doctrine.

Candidate extraction is deliberately fail-closed: a new public C-NAX source
must be copied in full to its own neoaxiomas/C-NAX-*_ES_EN.md document and added
to the README index. This synchroniser never rebuilds a monolithic README and
never substitutes a source with a generated summary.
"""

from pathlib import Path
import subprocess
import sys


root = Path('.').resolve()
readme = (root / 'neoaxiomas/README.md').read_text(encoding='utf-8')
if 'README = ÍNDICE' not in readme or 'README = INDEX' not in readme:
    raise SystemExit('NEOAXIOM_MONOLITH_FAILURE: README index contract missing; refusing legacy synchronisation')

subprocess.run(
    [sys.executable, str(root / '.github/scripts/audit_neoaxiom_registry_integrity.py')],
    check=True,
)
print('NEOAXIOM_CANDIDATE_SYNC mode=non_reductive_document_gate changed=0')
