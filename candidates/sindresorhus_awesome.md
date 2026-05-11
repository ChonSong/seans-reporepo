# sindresorhus/awesome → Curated Resource Index

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/sindresorhus/awesome |
| **Stars** | 336,000+ |
| **License** | MIT |
| **Language** | Markdown |
| **Relevance Score** | 4/10 |

## Relevance Rationale

This is the canonical "awesome" list index — not code, but a curated directory of
awesome lists. For hermes-web-computer's Research Tile, this provides a structured
knowledge base that the agent can reference when suggesting tools, libraries, or resources.

This is purely a data import — no code migration needed.

## What to Extract

### 1. Markdown Parsing
- **Target:** Go `backend/data/awesome_index.go` — parse and index awesome lists
- **Use case:** Build a searchable index of awesome list categories and entries
- **Transpile:** None — just parse the markdown structure

### 2. Category Browser
- **Target:** Svelte 5 `frontend/src/components/ResearchTile/AwesomeBrowser.svelte`
- **Use case:** Browse awesome lists by category in Research Tile
- **Transpile:** None — build from scratch using parsed data

### What to SKIP

- The entire repo is markdown — there's nothing to transpile
- Just import the data structure and build a simple browser

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| Data import | 0.25 | Parse markdown, build JSON index |
| Svelte browser component | 0.25 | Simple tree view |
| **Total** | **0.5 days** | |

## Risks

- Low value relative to effort — may not be worth the tile space
- Better as a background index that the agent queries, not a visible tile
