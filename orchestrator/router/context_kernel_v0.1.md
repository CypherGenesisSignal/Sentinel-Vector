# Context Kernel v0.1

## Purpose
Provide a unified context window for all agents.  
The kernel supplies synchronized state slices so reasoning stays aligned.

## Kernel Fields
- global_time_index
- active_memory_context
- agent_status_map
- signal_bus snapshot
- last_commit_hash
- holonomic_scale_frame

## Update Cycle
1. Ingest latest agent outputs  
2. Recompute coherence window  
3. Merge memory deltas  
4. Produce shared frame  
5. Dispatch frame to all agents
