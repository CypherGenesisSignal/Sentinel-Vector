# Safety Module v0.1

## Purpose
Ensure all agent actions remain inside approved boundaries.

## Responsibilities
- validate all agent outputs before routing
- filter unsafe or contradictory instructions
- enforce read-only surfaces unless approved
- apply coherence penalty for reckless or ambiguous outputs

## Processing Steps
1. inspect output for constraint violations
2. run static safety checks
3. compute safety_score
4. if below threshold, block output and notify orchestrator
5. forward sanitized output if approved

## Output
- approved_action
- blocked_action_report
- updated safety_state
