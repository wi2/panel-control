#!/usr/bin/env bash
# Bootstrap a product repository from a BUILD_MICRO opportunity.
# Usage: ./scripts/bootstrap_product_repo.sh OPP-ID slug TARGET_DIR
# Example: ./scripts/bootstrap_product_repo.sh OPP-20260626-coachbrief coachbrief ~/Projects/coachbrief

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$ROOT/templates/product-repo"

usage() {
  echo "Usage: $0 OPP-ID slug TARGET_DIR" >&2
  echo "  OPP-ID     e.g. OPP-20260626-coachbrief" >&2
  echo "  slug       directory/repo name" >&2
  echo "  TARGET_DIR absolute or relative path for new product repo" >&2
  exit 1
}

[[ $# -eq 3 ]] || usage

OPP_ID="$1"
SLUG="$2"
TARGET="$(cd "$(dirname "$3")" 2>/dev/null && pwd)/$(basename "$3")"
OPP_FILE="$ROOT/opportunities/${OPP_ID}.md"

if [[ ! -f "$OPP_FILE" ]]; then
  echo "error: opportunity not found: $OPP_FILE" >&2
  exit 1
fi

if [[ -e "$TARGET" ]] && [[ -n "$(ls -A "$TARGET" 2>/dev/null)" ]]; then
  echo "error: target directory exists and is not empty: $TARGET" >&2
  exit 1
fi

# Parse frontmatter (minimal)
get_fm() {
  local key="$1"
  local val
  val="$(sed -n '/^---$/,/^---$/p' "$OPP_FILE" | grep "^${key}:" | head -1 | cut -d: -f2- | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  val="${val#\"}" ; val="${val%\"}"
  echo "$val"
}

DECISION="$(get_fm decision)"
if [[ "$DECISION" != "BUILD_MICRO" ]]; then
  echo "warning: decision is '$DECISION', expected BUILD_MICRO — continuing anyway" >&2
fi

TITLE="$(get_fm title)"
MSFI="$(get_fm msfi_lite)"
WEDGE="$(get_fm title)"
PANEL_URL="https://github.com/wi2/panel-control/blob/master/opportunities/${OPP_ID}.md"

echo "Bootstrapping product repo at $TARGET ..."
mkdir -p "$TARGET"
cp -R "$TEMPLATE/." "$TARGET/"

# Copy OPP snapshot
cp "$OPP_FILE" "$TARGET/docs/SOURCE-OPP.md"

README="$TARGET/README.md"
if [[ -f "$README" ]]; then
  python3 - "$README" "$OPP_ID" "$SLUG" "$TITLE" "$MSFI" "$PANEL_URL" <<'PY'
import sys
from pathlib import Path

readme, opp_id, slug, title, msfi, panel_url = sys.argv[1:7]
text = Path(readme).read_text(encoding="utf-8")
text = text.replace("{{PRODUCT_NAME}}", title or slug)
text = text.replace("{{OPP_ID}}", opp_id)
text = text.replace("{{MSFI_LITE}}", msfi or "unknown")
text = text.replace("{{PANEL_CONTROL_OPP_URL}}", panel_url)
text = text.replace("{{WEDGE_SUMMARY}}", title or f"Bootstrap from {opp_id}")
Path(readme).write_text(text, encoding="utf-8")
PY
fi

# Update package.json name
if [[ -f "$TARGET/package.json" ]]; then
  python3 - "$TARGET/package.json" "$SLUG" <<'PY'
import json, sys
path, slug = sys.argv[1], sys.argv[2]
data = json.loads(open(path, encoding="utf-8").read())
data["name"] = slug
open(path, "w", encoding="utf-8").write(json.dumps(data, indent=2) + "\n")
PY
fi

echo ""
echo "Done. Product repo ready at: $TARGET"
echo ""
echo "Next steps:"
echo "  cd $TARGET"
echo "  git init && git add -A && git commit -m \"chore: bootstrap from ${OPP_ID}\""
echo "  gh repo create wi2/${SLUG} --private --source=. --remote=origin"
echo "  git push -u origin main"
echo ""
echo "Then read AGENTS.md and run product agents (Vision → MVP → … → Code)."
echo "See playbooks/build-handoff.md in panel-control."
