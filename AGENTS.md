# AGENTS.md — seans-reporepo

## About
Personal GitHub repo catalog: 59 owned + 213 starred repos with tag-based combinatorial analysis.
Feeds into repo-transmute for code migration planning.

## Key Files
- `README.md` — Auto-generated index. DO NOT EDIT DIRECTLY. Run `scripts/generate-catalog.py`.
- `scripts/generate-catalog.py` — Main generator. Python 3, uses `gh` CLI for API calls.
- `COMBINATORIAL.md` — Cross-repo overlap analysis. Auto-generated.
- `candidates/` — High-priority migration targets for repo-transmute.
- `owned/*.md`, `starred/*.md` — Individual repo metadata with YAML frontmatter.

## Working with This Repo
- To update stats: run `scripts/refresh.sh` (pulls → generates → commits → pushes)
- To add tags: edit `TOPIC_TAG_MAP` in `generate-catalog.py`
- To mark migration candidates: create `.md` in `candidates/` and update `candidates/README.md`
- Query repos: `python3 scripts/query.py --tags agent,llm`

## Integration Points
- **repo-transmute** (`ChonSong/repo-transmute`) consumes candidates/ as migration input
- **hermes-web-computer** (`ChonSong/hermes-web-computer`) is the target unified stack
- Catalog refresh cron: `0 9 * * 1` (Monday 9am AEST)
