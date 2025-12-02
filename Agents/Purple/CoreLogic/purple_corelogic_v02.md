# Purple CoreLogic v0.2

## Purpose
Provide the orchestrator with multi dimensional event awareness, resolving agent level signals into a unified holonomic frame. Purple computes breadth, depth, and coherence to determine routing and persistence paths.

## Responsibilities
- Ingest event bundles from Red, Blue, Green, Tools, OS.
- Normalize event metadata.
- Compute holonomic scale (breadth, depth, coherence).
- Trigger decision engine for retain or broadcast.
- Update global working context.
- Surface high dimensional patterns to scheduler.

## Input Schema
- event_id
- event_source (red, blue, green, tools, os)
- raw_signal
- metadata
- temporal_signature
- cross_agent_refs

## Output Schema
- holonomic vector
- decision flags
- retention values
- broadcast targets
- working context mutation
