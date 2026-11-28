#!/usr/bin/env bash
# Run a bounded sync transaction from fresh main; never force-push or rebase stale generated output.
set -euo pipefail
mode="${1:?latest or crossrefs required}"
case "$mode" in latest|crossrefs) ;; *) exit 64 ;; esac
root="$(git rev-parse --show-toplevel)"
scratch="$(mktemp -d)"
work="$scratch/work"
cleanup() {
  if [ -d "$work" ]; then git -C "$root" worktree remove --force "$work"; fi
  rmdir "$scratch"
}
trap cleanup EXIT
for attempt in 1 2 3; do
  git -C "$root" fetch --no-tags origin refs/heads/main
  base="$(git -C "$root" rev-parse FETCH_HEAD)"
  git -C "$root" worktree add --detach "$work" "$base"
  (
    cd "$work"
    git config user.name 'github-actions[bot]'
    git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
    if [ "$mode" = latest ]; then
      python .github/scripts/sync_latest_manifesto_feature.py
      python .github/scripts/audit_markdown_links_readmes.py
      allowed='(^|/)README\.md$|^auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN\.md$'
      msg='docs: synchronize latest manifesto README blocks'
    else
      python .github/scripts/sync_manifesto_crossrefs.py
      python .github/scripts/sync_manifesto_reference_policy.py
      python .github/scripts/sync_manifesto_index.py
      python .github/scripts/sync_canonical_manifestos.py
      python .github/scripts/audit_manifesto_registry_completeness.py
      python .github/scripts/audit_neocore_role_ontology.py
      python .github/scripts/audit_manifesto_clickable_relations.py
      python .github/scripts/audit_global_bilingual_symmetry.py
      python .github/scripts/audit_language_selectors.py
      allowed='^manifiestos/([^/]+\.md|canonicos/[^/]+\.md)$|^auditorias/publicas/[^/]+\.md$'
      msg='docs: sincronizar navegación e índice de manifiestos'
    fi
    unexpected="$( { git diff --name-only; git ls-files --others --exclude-standard; } | grep -Ev "$allowed" || true)"
    test -z "$unexpected" || { echo "UNEXPECTED_WRITE: $unexpected"; exit 1; }
    if [ "$mode" = latest ]; then
      git diff --check
      git add -A
    else
      git add manifiestos/*.md manifiestos/canonicos/*.md
    fi
    if ! git diff --cached --quiet; then
      git commit -m "$msg"
      python .github/scripts/audit_diff_integrity_markdown.py "$base"
    fi
  )
  proposed="$(git -C "$work" rev-parse HEAD)"
  # A no-op must also be current: if main advanced, regenerate rather than claiming success.
  if [ "$proposed" = "$base" ]; then
    git -C "$root" fetch --no-tags origin refs/heads/main
    if [ "$(git -C "$root" rev-parse FETCH_HEAD)" = "$base" ]; then
      echo "SYNC_TRANSACTION=PASS mode=$mode no_change base=$base"
      exit 0
    fi
  elif git -C "$work" push origin HEAD:refs/heads/main; then
    echo "SYNC_TRANSACTION=PASS mode=$mode base=$base commit=$proposed"
    exit 0
  else
    git -C "$root" fetch --no-tags origin refs/heads/main
    if [ "$(git -C "$root" rev-parse FETCH_HEAD)" = "$base" ]; then
      echo 'SYNC_TRANSACTION=FAIL push failed without remote advancement'
      exit 1
    fi
  fi
  echo "SYNC_TRANSACTION_RETRY mode=$mode attempt=$attempt base=$base"
  git -C "$root" worktree remove --force "$work"
done
echo 'SYNC_TRANSACTION=FAIL concurrent changes exhausted bounded retries'
exit 1
