---
repo: 'ChonSong/circuit-breaker-framework'
url: 'https://github.com/ChonSong/circuit-breaker-framework'
description: 'A general-purpose circuit breaker framework that allows automated workflows to declare assumptions explicitly, monitors whether they hold, and halts gracefully with a full audit trail.'
type: library
status: active
language: Python
size_kb: 15
stars: 0
last_pushed: '2026-04-08'
license: unknown
tags:
  - agent
  - ai
  - aie
  - framework
  - ide
  - image-gen
  - monitoring
  - orchestration
  - python
  - rag
  - reliability
topics: []
refreshed_at: '2026-07-02 13:30 UTC'
---

# circuit-breaker-framework

> A general-purpose circuit breaker framework that allows automated workflows to declare assumptions explicitly, monitors whether they hold, and halts gracefully with a full audit trail.

**URL:** [ChonSong/circuit-breaker-framework](https://github.com/ChonSong/circuit-breaker-framework)

## Metadata

- **Type:** library
- **Status:** active
- **Language:** Python
- **Size:** 15 KB
- **Stars:** 0
- **Last Pushed:** 2026-04-08
- **License:** unknown
- **Tags:** agent, ai, aie, framework, ide, image-gen, monitoring, orchestration, python, rag, reliability

## README Excerpt

# Circuit Breaker Framework

Systems built on assumptions that eventually fail — without anyone noticing until the failure is expensive — are more common than systems that know when to stop.

Built a general-purpose circuit breaker framework that allows automated workflows to declare their assumptions explicitly, monitors whether those hold in practice, and halts gracefully — with a full audit trail — when they don't. Configured it around a document classification pipeline: when low-confidence classifications exceeded a threshold, the system paused and surfaced a human-review task.

## Features

- **Explicit assumption declarations** — workflows declare what they expect to be true
- **Runtime monitoring** — continuously check declared assumptions against real data
- **Graceful halting** — pause workflows with clear diagnostic information
- **Full audit trail** — every assumption check logged with context
- **Human-in-the-loop** — surface review tasks when thresholds exceeded

## Quick Start

```bash
pip install -e .
python -m circuit_breaker run --workflow examples/doc_classifier.yaml
```

## Example

```python
from circuit_breaker import CircuitBreaker

cb = CircuitBreaker()
cb.declare("low_confidence_rate", max_rate=0.15)
cb.monitor("low_confidence_rate", {"rate": 0.08})  # ok
cb.monitor("low_confidence_rate", {"rate": 0.22})  # trips circuit
```

## AIE Orchestrator Integration

The framework ships with an `OrchestratorNode` that wraps `CircuitBreaker` with AIE-grade observability and four semantic halt conditions.

### Architecture

```
Workflow
  └─ OrchestratorNode
       ├─ CircuitBreaker       (assumption-based CB, CLOSED/OPEN/HALF_OPEN)
       ├─ ProvenanceGraph      (DAG of all task executions)
       ├─ DriftScore           (STABLE → SEVERE, 0.0–1.0)
       └─ HitLDiagnostic       (human-readable halt package)
```

### Four Halt Conditions

| Condition | Threshold | Effect |
|---|---|---|
| Semantic drift | drift_score >= 0.9 | HALT + HitL diagnostic |
| ...
