# sveltejs/ai-tools → AI Component Library

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/sveltejs/ai-tools |
| **Stars** | new |
| **License** | MIT (expected) |
| **Language** | TypeScript/Svelte |
| **Relevance Score** | 6/10 |

## Relevance Rationale

Official Svelte AI tooling primitives. Low complexity because it's already Svelte —
may need Svelte 4→5 rune updates but the component patterns are directly applicable.
Useful for building consistent AI-facing UI in hermes-web-computer tiles.

## What to Extract

### 1. Streaming Response Display
- **Target:** Svelte 5 `frontend/src/components/AI/StreamingText.svelte`
- **Use case:** Display Hermes Agent responses with typewriter effect
- **Transpile:** Minimal — Svelte 4→5 rune syntax update

### 2. Tool Call Cards
- **Target:** Svelte 5 `frontend/src/components/AI/ToolCallCard.svelte`
- **Use case:** Show tool execution status (running/success/failed) in Dashboard tile
- **Transpile:** Minimal — prop and event syntax update

### 3. Chat Message List
- **Target:** Svelte 5 `frontend/src/components/AI/MessageList.svelte`
- **Use case:** Terminal tile's conversation history, Voice tile transcript display
- **Transpile:** Minimal — {#each} block stays the same

### What to SKIP

- Any build tooling (hermes-web-computer has its own Vite setup)
- Demo/example pages (extract components only)

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| repo-transmute ingest | 0.5 | Small repo, fast |
| Svelte 4→5 migration | 0.5-1 | Mostly syntax updates |
| Integration into hermes-web-computer | 0.5 | Drop-in components |
| **Total** | **1.5 days** | |

## Risks

- Repo may be minimal/early — might not have much to extract
- Svelte 5 runes may require rewriting reactive patterns
