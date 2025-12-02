# Routing Table v0.1

## Purpose
Define routing paths for agent outputs and orchestrator actions.

## Structure
routing_table = {
  "red_scenario": ["blue", "orchestrator"],
  "blue_defense_plan": ["orchestrator"],
  "green_pattern_map": ["orchestrator"],
  "threat_indicator": ["red", "blue"],
  "system_snapshot": ["green", "orchestrator"],
  "memory_event": ["persistence", "orchestrator"]
}

## Routing Logic
1. receive agent output
2. look up target list
3. validate through safety module
4. dispatch to each target
5. update context kernel after merge

## Notes
- orchestrator always receives a copy
- persistence receives only memory_event entries
- no circular routing allowed
