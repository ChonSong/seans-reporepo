# bytebot-ai/bytebot → Browser Tile

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/bytebot-ai/bytebot |
| **Stars** | 11,003 |
| **License** | Apache-2.0 ✅ |
| **Language** | TypeScript |
| **Last Pushed** | 2025-09-12 |
| **Relevance Score** | 9/10 |

## Relevance Rationale

bytebot is the closest open-source equivalent to what the Browser Tile needs:
- Screenshot capture pipeline (pixel-level browser rendering)
- DOM analysis (structural understanding of page content)
- Click/typing automation (input routing)
- Already works as an AI agent that can browse and interact

The Apache-2.0 license is permissive — no copyleft concerns.

## What to Extract

### 1. Browser Screenshot Capture
- **Source files:** `src/browser/capture.ts` (or equivalent)
- **Target:** Go `sandbox/screenshot.go` — headless Chrome → PNG → WebSocket stream
- **Transpile:** TS puppeteer/playwright calls → Go chromedp/rod calls
- **Complexity:** Medium — straightforward browser automation API mapping

### 2. DOM Analysis Pipeline
- **Source files:** `src/browser/dom-analysis.ts` (or equivalent)
- **Target:** Go `sandbox/dom.go` — parse DOM → JSON structure → JSON-RPC tool
- **Transpile:** TS DOM traversal → Go chromedp DOM extraction
- **Complexity:** Medium — DOM APIs differ but the logic is portable

### 3. Input Automation (Click/Type)
- **Source files:** `src/browser/input.ts` (or equivalent)
- **Target:** Go `sandbox/input.go` — coordinate-based mouse/keyboard events
- **Transpile:** TS → Go xdotool/xdg calls inside Docker sandbox
- **Complexity:** Low — simple event mapping

### What to SKIP

- Full agent orchestration (hermes-web-computer already has this)
- LLM integration (uses Hermes Agent instead)
- Desktop automation beyond browser (out of scope for Browser Tile)

## repo-transmute Plan

```bash
cd /opt/data/repo-transmute-v2
python3 -m src.cli v2 ingest https://github.com/bytebot-ai/bytebot --output data/bytebot

# Review blueprint
cat data/bytebot/blueprint.json | jq '.components[] | select(.name | contains("browser") or contains("capture"))'

# Migrate
python3 -m src.cli v2 migrate data/bytebot /opt/data/hermes-web-computer \
  --extract "browser-capture,dom-analysis,input-routing" \
  --target svelte5+go \
  --style tailwind
```

## Tile Spec Integration

The extracted code feeds into:
- `frontend/src/components/BrowserTile.svelte` — screenshot viewer + URL bar
- `backend/sandbox/browser.go` — headless Chrome manager
- `backend/ws/multiplexer.go` — new `browser.navigate`, `browser.screenshot`, `browser.click` JSON-RPC methods

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| repo-transmute ingest + blueprint | 0.5 | Automated |
| Migration (TS→Go + Svelte 5) | 2-3 | LLM-driven with vision verification |
| Integration into hermes-web-computer | 1 | Wire up JSON-RPC methods |
| Testing + refinement | 0.5-1 | Vision scoring, edge cases |
| **Total** | **4-5 days** | |

## Risks

- bytebot may use Playwright which has Go equivalents (rod/playwright-go) but API differs
- DOM analysis may be tightly coupled to bytebot's agent loop — needs decoupling
- Screenshots at 500ms refresh may be heavy — need optimization (diff-based updates)
