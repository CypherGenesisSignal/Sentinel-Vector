# Sentinel Vector

Multi agent cybersecurity system with holonomic orchestration, persistent memory, and interpretable event flow.

## Introduction

Sentinel Vector is a multi agent defensive and adversarial simulation system.  
It models real world cyber operations by allowing independent agents to probe, defend, analyze, and coordinate across a shared operational space. The system grows more capable as new memories accumulate and as holonomic patterns begin to stabilize across agents.

This project is designed as an open and observable architecture. Every component is structured so researchers and engineers can inspect how reasoning emerges, how agents learn over time, and how orchestration behaves when multiple cognitive layers interact. Nothing is hidden behind opaque abstractions. The goal is clarity, reproducibility, and long term verifiability.

## Architecture Overview

Sentinel Vector consists of seven agents operating inside a unified substrate:

- Red Team 1 and Red Team 2: offensive probing and exploit generation  
- Blue Team 1 and Blue Team 2: defensive policy, detection, and counter strategy  
- Green Team 1 and Green Team 2: environment scanning, baseline telemetry, and anomaly mapping  
- Purple Orchestrator: coordination, synthesis, memory routing, holonomic scoring, and global optimization

All agents communicate through the Context Kernel and the Orchestrator Router.  
All memory and temporal patterns accumulate inside a shared persistent memory ledger.

A full system diagram is provided in the docs folder.

## Folder Structure

```
sentinel-vector/
orcestrator/
core/
router/
context-kernel/
holonomic/
memory/
tests/
agents/
red/
corelogic/
tools/
memory/
tests/
blue/
corelogic/
tools/
memory/
tests/
green/
corelogic/
tools/
memory/
tests/
tools/
shared/
environment/
data/
logs/
samples/
captures/
docs/
diagrams/
specs/
research/
tests/
smoke/
integration/
LICENSE
README.md
```

## Getting Started

Requirements:
- Python 3.11 or newer  
- Experimental LLM endpoint or local model  
- Basic command line familiarity  

To run the first checks:

```bash
python tests/smoke/smoke_test_suite.py
```

This validates the router, checks agent registration, verifies the event kernel, and ensures memory writing works.

## Holonomic Layer

The holonomic subsystem computes cross agent coherence.  
It tracks:

- Temporal persistence  
- Cross agent agreement  
- Behavioral stability  
- Identity consistency  
- Multi step reliability

Scores are stored in a ledger inside `orchestrator/holonomic/`.  
This layer governs long term trust inside the system.

## Persistent Memory

Persistent memory is implemented as a JSON based ledger with append only writes.  
All agents contribute events, which the orchestrator normalizes and stores.

Placement:  
`orchestrator/memory/event_ledger_v0.json`

Memory objects include:
- actor  
- timestamp  
- context  
- action  
- outcome  
- coherence score  

## Context Kernel

The context kernel handles message routing, summarization, and multi agent synchronization.  
It is the main interface the orchestrator uses for real time decision making.

Core logic:  
`orchestrator/context-kernel/kernel.py`

## Roadmap

### v0.4  
- First functional agent loop  
- Working memory writes  
- Holonomic scoring v0.2  

### v0.5  
- Multi agent runs with replay logs  
- Initial defensive playbooks  
- Red team exploit simulation  

### v0.6  
- Green team telemetry mapping  
- Dynamic orchestrator policy switching  
- Early graph rendering  

### v1.0  
- Full holonomic orchestration  
- Persistent memory stabilization  
- Exportable reports and graphs  

## License

MIT License.  
See LICENSE for full terms.

## Acknowledgments

Special thanks to early collaborators, reviewers, and researchers helping shape the system.  
Sentinel Vector is an open project and encourages external review, analysis, and contribution.
