#!/bin/bash
# Refresh the seans-reporepo catalog
set -e

REPO_DIR="/home/sean/.hermes/cache/seans-reporepo"
SCRIPT_DIR="/home/sean/.hermes/scripts"
RUN_QUERY=false
QUERY_ARGS=()

# Parse arguments
for arg in "$@"; do
    if [ "$arg" = "--query" ]; then
        RUN_QUERY=true
    elif [ "$arg" = "--no-auto-catalog" ]; then
        SKIP_AUTO_CATALOG=true
    else
        QUERY_ARGS+=("$arg")
    fi
done

cd "$REPO_DIR" || { echo "Repo not found at $REPO_DIR"; exit 1; }

# Pull latest
git pull origin main 2>/dev/null || true

# Run the catalog generation script
python3 "$SCRIPT_DIR/generate-catalog.py" "$REPO_DIR"

# Commit and push if changes
cd "$REPO_DIR"
git add -A
if git diff --cached --quiet; then
    echo "No changes to commit."
else
    git commit -m "Auto-refresh: $(date '+%Y-%m-%d %H:%M UTC')"
    git push
    echo "Catalog updated and pushed."
fi

# Optional: run query after refresh
if [ "$RUN_QUERY" = true ]; then
    echo ""
    echo "=== Running query after refresh ==="
    python3 "$(dirname "$0")/query.py" "${QUERY_ARGS[@]}"
fi

# ── Auto-catalog: import newly-starred repos not yet in catalog ──
if [ "$SKIP_AUTO_CATALOG" != true ]; then
    echo ""
    echo "=== Auto-cataloging newly starred repos ==="

    if ! command -v gh &> /dev/null; then
        echo "gh CLI not available. Skipping auto-catalog step."
        echo "Install GitHub CLI (https://cli.github.com/) to enable this feature."
    else
        # Verify gh is authenticated
        if ! gh auth status &> /dev/null; then
            echo "gh CLI is installed but not authenticated. Skipping auto-catalog step."
        else
            NEW_ENTRIES=0
            AUTO_CATALOG_SCRIPT="$REPO_DIR/scripts/auto-catalog.py"

            if [ ! -f "$AUTO_CATALOG_SCRIPT" ]; then
                echo "auto-catalog.py not found at $AUTO_CATALOG_SCRIPT. Skipping."
            else
                # Temp files for repo lists
                STARRED_LIST=$(mktemp)
                OWNED_LIST=$(mktemp)

                # ── Starred repos ──
                echo "Checking starred repos..."
                gh api /user/starred --paginate --jq '.[].full_name' 2>/dev/null | sort -u > "$STARRED_LIST" || true

                while IFS= read -r repo; do
                    [ -z "$repo" ] && continue
                    filename="${repo//\//_}.md"
                    if [ ! -f "$REPO_DIR/starred/$filename" ]; then
                        echo "  New starred: $repo"
                        python3 "$AUTO_CATALOG_SCRIPT" --url "https://github.com/$repo" --starred || true
                        NEW_ENTRIES=$((NEW_ENTRIES + 1))
                    fi
                done < "$STARRED_LIST"

                # ── Owned repos (ChonSong) ──
                echo "Checking owned repos..."
                gh api /users/ChonSong/repos --paginate --jq '.[].full_name' 2>/dev/null | sort -u > "$OWNED_LIST" || true

                while IFS= read -r repo; do
                    [ -z "$repo" ] && continue
                    filename="${repo//\//_}.md"
                    if [ ! -f "$REPO_DIR/owned/$filename" ]; then
                        echo "  New owned: $repo"
                        python3 "$AUTO_CATALOG_SCRIPT" --url "https://github.com/$repo" --owned || true
                        NEW_ENTRIES=$((NEW_ENTRIES + 1))
                    fi
                done < "$OWNED_LIST"

                # Clean up temp files
                rm -f "$STARRED_LIST" "$OWNED_LIST"

                # Commit and push any new entries
                if [ "$NEW_ENTRIES" -gt 0 ]; then
                    git add -A
                    git commit -m "Auto-catalog: $NEW_ENTRIES new repo(s) added via auto-catalog"
                    git push
                    echo "Auto-catalog: $NEW_ENTRIES new repo(s) added and pushed."
                else
                    echo "Auto-catalog: all repos already cataloged."
                fi
            fi
        fi
    fi
fi
