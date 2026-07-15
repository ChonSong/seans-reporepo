---
repo: 'ChonSong/bim-to-print'
url: 'https://github.com/ChonSong/bim-to-print'
description: 'Automated BIM-to-print pipeline: Revit → Grasshopper → custom slicer → G-code for 3D concrete printing'
type: cli
status: active
language: Python
size_kb: 20051
stars: 0
last_pushed: '2026-06-19'
license: unknown
tags:
  - api
  - cli
  - orchestration
  - python
topics: []
refreshed_at: '2026-07-15 00:23 UTC'
---

# bim-to-print

> Automated BIM-to-print pipeline: Revit → Grasshopper → custom slicer → G-code for 3D concrete printing

**URL:** [ChonSong/bim-to-print](https://github.com/ChonSong/bim-to-print)

## Metadata

- **Type:** cli
- **Status:** active
- **Language:** Python
- **Size:** 20,051 KB
- **Stars:** 0
- **Last Pushed:** 2026-06-19
- **License:** unknown
- **Tags:** api, cli, orchestration, python

## README Excerpt

# bim-to-print

**BIM-to-G-code pipeline for 3D concrete printing.**

Reads building geometry from IFC files (or Grasshopper), slices it into print layers, generates toolpaths with configurable perimeters and infill, and outputs Marlin-compatible G-code.

---

## Quick start

```bash
# Install
pip install -e ".[dev]"

# Run demo wall (no IFC file needed)
bim2print demo --width 3000 --height 2400 -o wall.gcode

# From Grasshopper JSON export
bim2print gh examples/demo_wall.json output.gcode --layer-height 5

# From IFC file
bim2print ifc model.ifc output.gcode
```

## Pipeline

```
IFC / GH JSON
    ↓
IFC Reader (ifc_reader.py)   ← IfcOpenShell for IFC, manual JSON for GH
    ↓
Slicer (slicer.py)           ← horizontal layers at configured height
    ↓
Toolpath (toolpath.py)       ← contours + infill per layer
    ↓
G-code (gcode_writer.py)     ← Marlin/RepRap G-code
    ↓
.gcode file → printer
```

## Configuration

### Per-command options

| Option | Default | Description |
|--------|---------|-------------|
| `--layer-height` | 5.0 mm | Height of each printed layer |
| `--nozzle-diameter` | 6.0 mm | Nozzle opening |
| `--extrusion-width` | 8.0 mm | Extruded bead width |
| `--perimeter-count` | 2 | Number of contour passes |
| `--infill-pattern` | `lines` | `lines`, `grid`, or `none` |
| `--infill-density` | 0.3 (30%) | Fraction of area to infill |

### Print settings (programmatic API)

```python
from bim_to_print.gcode_writer import PrintSettings

settings = PrintSettings(
    travel_speed=6000,          # mm/min
    print_speed=1800,           # mm/min
    first_layer_speed=1200,     # mm/min
    extrusion_multiplier=1.0,   # flow rate tweak
    pre_gcode="M104 S200",      # run before print
    post_gcode="M84",           # run after print
)
```

## Commands

| Command | Purpose |
|---------|---------|
| `bim2print ifc <input> <output>` | Convert IFC file to G-code |
| `bim2print gh <input.json> <output>` | Convert GH JSON export to G-code |
| `bim2print demo [...
