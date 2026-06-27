#!/usr/bin/env bash
# Open opp/pipeline for a new opportunity evaluation PR.
# Usage: ./scripts/open_pipeline.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

BRANCH="opp/pipeline"

echo "Updating master..."
git checkout master
git pull origin master

if git ls-remote --heads origin "$BRANCH" | grep -q "$BRANCH"; then
  echo "Deleting remote branch $BRANCH ..."
  git push origin --delete "$BRANCH" || true
fi

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git branch -D "$BRANCH"
fi

echo "Creating $BRANCH from master..."
git checkout -b "$BRANCH"
git commit --allow-empty -m "chore: open pipeline PR for automation run"
git push -u origin "$BRANCH"

echo ""
echo "Branch $BRANCH pushed. Open a PR with ## Intake body:"
echo ""
echo "  gh pr create --base master --head $BRANCH --title \"intake: YOUR TITLE\" --body-file - <<'EOF'"
echo "  ## Intake"
echo ""
echo "  **Title:** Your opportunity title"
echo "  **Owner:** studio-team"
echo "  **Tags:** tag1, tag2"
echo ""
echo "  ### Description"
echo ""
echo "  1-3 paragraphs..."
echo "  EOF"
echo ""
echo "See docs/runbook-weekly.md and docs/automations.md"
