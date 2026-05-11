# trycua/cua → Sandbox Tile

## Source Analysis

| Field | Value |
|-------|-------|
| **URL** | https://github.com/trycua/cua |
| **Stars** | 15,833 |
| **License** | MIT ✅ |
| **Language** | Python/Swift/TS |
| **Last Pushed** | 2026-05-09 (active!) |
| **Relevance Score** | 8/10 |

## Relevance Rationale

cua provides the cross-platform computer-use infrastructure that hermes-web-computer's
Sandbox Tile needs: screen capture, mouse/keyboard routing, and coordinate mapping.
It's actively maintained (pushed 2 days ago) and MIT-licensed.

The macOS/Swift parts are irrelevant for our Linux+Docker target, but the Python core
(screen capture, input routing) maps directly to Go.

## What to Extract

### 1. Screen Capture Pipeline
- **Source files:** Python screen capture modules
- **Target:** Go `sandbox/capture.go` — `scrot`/`import` + Docker exec
- **Transpile:** Python PIL/mss → Go exec calls to screenshot tools in container
- **Complexity:** Low — simple subprocess calls

### 2. Mouse/Keyboard Event Routing
- **Source files:** Python input modules
- **Target:** Go `sandbox/input.go` — `xdotool` commands in Docker
- **Transpile:** Python pynput/autopy → Go exec xdotool
- **Complexity:** Low — command mapping

### 3. Coordinate Mapping
- **Source files:** Coordinate normalization code
- **Target:** Go `sandbox/coords.go` — map tile coordinates to sandbox resolution
- **Transpile:** Python math → Go math (trivial)
- **Complexity:** Low

### What to SKIP

- macOS/Swift components (platform-specific, not needed for Linux)
- Full agent loop (hermes-web-computer has its own agent orchestration)
- Cross-platform abstraction layer (we target Linux+Docker only)

## repo-transmute Plan

```bash
cd /opt/data/repo-transmute-v2
python3 -m src.cli v2 ingest https://github.com/trycua/cua --output data/cua

# Focus on Python files only (skip Swift/TS)
cat data/cua/blueprint.json | jq '.components[] | select(.language == "python")'

# Migrate
python3 -m src.cli v2 migrate data/cua /opt/data/hermes-web-computer \
  --extract "screen-capture,input-routing,coordinate-mapping" \
  --target go \
  --platform linux-docker
```

## Tile Spec Integration

The extracted code feeds into:
- `backend/sandbox/manager.go` — Docker container lifecycle + screenshot stream
- `backend/sandbox/container.go` — per-sandbox session management
- `frontend/src/components/SandboxTile.svelte` — screenshot viewer + input overlay
- `backend/ws/multiplexer.go` — new `sandbox.screenshot`, `sandbox.click`, `sandbox.type` JSON-RPC methods

## Effort Estimate

| Phase | Days | Notes |
|-------|------|-------|
| repo-transmute ingest + blueprint | 0.5 | Automated |
| Migration (Python→Go) | 1.5-2 | Straightforward subprocess mapping |
| Docker sandbox image setup | 1 | Ubuntu+XFCE+scrot+xdotool base |
| Integration into hermes-web-computer | 0.5 | Wire up JSON-RPC methods |
| Testing + refinement | 0.5 | Input latency, screenshot quality |
| **Total** | **3.5-4 days** | |

## Risks

- cua is macOS-first; Linux screen capture may need different tools (scrot vs screencapture)
- xdotool in Docker requires X11 forwarding or virtual framebuffer (xvfb)
- Screenshot frequency (500ms) vs Docker exec latency — may need persistent VNC connection instead
