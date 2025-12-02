context_kernel/context_kernel_v0.1.md  # Context Kernel v0.1

Defines the minimal shape of information passed through the system.

## Input Shape

```json
{
  "event_id": "uuid",
  "timestamp": "...",
  "source": "user or system",
  "payload": {
    "text": "...",
    "entities": [...],
    "signals": {...}
  },
  "memory_window": {}
}
```

## Output Shape

```json
{
  "decision": "...",
  "confidence": 0.00 to 1.00,
  "explanation": "...",
  "memory_write_intent": {},
  "telemetry": {}
}
```

The kernel contains no logic.  
It is the contract between all agents.
