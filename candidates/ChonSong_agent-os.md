# ChonSong/agent-os → Dashboard Tile

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/ChonSong/agent-os |
| **Stars** | 0 (owned) |
| **License** | — |
| **Language** | React + Express + TypeScript |
| **Last Pushed** | 2026-05-10 (active!) |
| **Relevance Score** | 7/10 |

## Relevance Rationale

agent-os is your live dashboard — 22 frontend pages, 11 themes, Express backend, PostgreSQL.
It's the most immediately useful source because:
1. You already own it (no license concerns)
2. It has real content (agent status, sessions, metrics)
3. The Express API routes map directly to hermes-web-computer's Go backend
4. React→Svelte 5 is a well-understood migration path

The risk is scope: 22 pages is a lot. We should migrate only the top 3-4 pages for v1.0.

## What to Extract

### 1. Agent Status Page
- **Source:** `frontend/src/pages/Agents.tsx` (or equivalent)
- **Target:** Svelte 5 `frontend/src/components/DashboardTile/AgentStatus.svelte`
- **Transpile:** React hooks → Svelte runes (`useState` → `$state`, `useEffect` → `$derived`)
- **Complexity:** Medium — straightforward component mapping

### 2. Session List Page
- **Source:** `frontend/src/pages/Sessions.tsx` (or equivalent)
- **Target:** Svelte 5 `frontend/src/components/DashboardTile/SessionList.svelte`
- **Transpile:** React list rendering → Svelte `{#each}` blocks
- **Complexity:** Low — simple data display

### 3. System Metrics Page
- **Source:** `frontend/src/pages/System.tsx` (or equivalent)
- **Target:** Svelte 5 `frontend/src/components/DashboardTile/SystemMetrics.svelte`
- **Transpile:** React chart components → Svelte + Chart.js (or simpler sparklines)
- **Complexity:** Medium — chart libraries differ

### API Routes (Express→Go)
- **Source:** `backend/routes/*.js` (Express route handlers)
- **Target:** Go `backend/api/handlers.go` (HTTP handlers in hermes-web-computer)
- **Transpile:** Express middleware → Go `http.Handler` chain
- **Complexity:** Low — REST is REST, just language changes

### What to SKIP

- Themes system (11 themes → pick 1-2 for MVP)
- CasaOS integration (out of scope for hermes-web-computer)
- PostgreSQL queries (use Go's existing data sources or SQLite)
- Cloudflare tunnel config (hermes-web-computer has its own Caddy setup)

## repo-transmute Plan

```bash
cd /opt/data/repo-transmute-v2
python3 -m src.cli v2 ingest /opt/data/agent-os --output data/agent-os

# Review blueprint — focus on React components
cat data/agent-os/blueprint.json | jq '.components[] | select(.framework == "react")'

# Migrate pages
python3 -m src.cli v2 migrate data/agent-os /opt/data/hermes-web-computer \
  --extract "agent-status,session-list,system-metrics" \
  --target svelte5 \
  --style tailwind
```

## Tile Spec Integration

The extracted code feeds into:
- `frontend/src/components/DashboardTile.svelte` — container for dashboard sub-components
- `frontend/src/components/DashboardTile/AgentStatus.svelte`
- `frontend/src/components/DashboardTile/SessionList.svelte`
- `frontend/src/components/DashboardTile/SystemMetrics.svelte`
- `backend/api/handlers.go` — Go equivalents of Express routes

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| repo-transmute ingest + blueprint | 0.5 | Automated (local repo) |
| Migration (React→Svelte 5) — 3 pages | 1.5-2 | LLM-driven with vision verification |
| API route migration (Express→Go) | 0.5 | Straightforward mapping |
| Integration into hermes-web-computer | 0.5 | Wire up as tile content |
| Testing + refinement | 0.5 | Vision scoring, data binding |
| **Total** | **3-3.5 days** | |

## Risks

- React→Svelte 5 rune migration may need manual fixes for complex hooks
- agent-os uses PostgreSQL; hermes-web-computer may use SQLite — query rewriting needed
- 22 pages is tempting to migrate all at once — must resist scope creep
