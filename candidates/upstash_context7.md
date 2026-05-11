# upstash/context7 → Research Tile Data Source

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/upstash/context7 |
| **Stars** | new |
| **License** | MIT (expected) |
| **Language** | TypeScript |
| **Relevance Score** | 5/10 |

## Relevance Rationale

Context7 provides code snippet retrieval and developer knowledge base functionality.
For hermes-web-computer's Research Tile, this could power a "look up API docs" feature
where the agent queries Context7 and displays results in a dedicated tile.

This is more of a data source/API integration than a UI migration — the Go backend
needs an HTTP client to query Context7's API.

## What to Extract

### 1. API Integration Pattern
- **Target:** Go `backend/api/context7.go` — HTTP client for Context7 API
- **Use case:** Hermes Agent tool that queries Context7 for code snippets/docs
- **Transpile:** TS fetch calls → Go `http.Client` requests

### 2. Result Display Component
- **Target:** Svelte 5 `frontend/src/components/ResearchTile/CodeSnippet.svelte`
- **Use case:** Display code snippets with syntax highlighting in Research Tile
- **Transpile:** TS→Svelte 5 component (simple display logic)

### What to SKIP

- Indexing/crawling infrastructure (Context7 handles this server-side)
- Database/storage (use Context7's API, don't replicate)

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| repo-transmute ingest | 0.25 | API inspection only |
| Go HTTP client | 0.5 | Straightforward |
| Svelte display component | 0.25 | Simple |
| **Total** | **1 day** | |

## Risks

- Context7 API may be rate-limited or require authentication
- May be overkill — simpler to just use web search for doc lookups
