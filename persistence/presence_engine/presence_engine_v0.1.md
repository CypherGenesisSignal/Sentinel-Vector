# Presence Engine v0.1

## Purpose
Track which agent is active, dormant, or waiting.  
Provide sense of system presence and awareness of active threads.

## Fields
- active_agent
- last_agent
- dormant_map
- wake_signals
- presence_coherence

## Logic
1. read scheduler queue
2. update active_agent
3. compute presence_coherence based on:
   - agent alignment
   - output stability
   - memory sync integrity
4. broadcast presence snapshot to orchestrator

## Output
- presence_frame
- wake recommendations
- dormancy advisories
