#!/bin/bash
# Standalone refresh script for cron (no_agent mode)
set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

# Pull latest from remote
git pull origin main 2>&1 || echo "git pull had issues"

# Regenerate README
python3 scripts/generate-catalog.py "$REPO_DIR" 2>&1

# Commit and push
git add -A
if git diff --cached --quiet; then
    echo "No changes to commit."
else
    git commit -m "Auto-refresh: $(date '+%Y-%m-%d %H:%M UTC')"
    git push
    echo "Catalog updated and pushed."
fi

# Summary
LAST_COMMIT=$(git log -1 --format="%ai" HEAD)
OWNED_COUNT=$(ls owned/*.md 2>/dev/null | wc -l)
STARRED_COUNT=$(ls starred/*.md 2>/dev/null | wc -l)
echo "---"
echo "Last commit: $LAST_COMMIT"
echo "Repos: $OWNED_COUNT owned + $STARRED_COUNT starred = $((OWNED_COUNT + STARRED_COUNT)) total"
