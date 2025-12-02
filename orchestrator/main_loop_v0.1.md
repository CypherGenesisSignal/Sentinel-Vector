# PRPL Orchestrator Main Loop v0.1

The Purple Orchestrator coordinates all color agents through a deterministic event cycle. Holonomic memory scale integration is optional but scaffolded.

## Event Cycle

1. Receive input event  
2. Normalize event shape  
3. Query short term memory  
4. Fan out to Red, Blue, Green agents  
5. Collect agent outputs  
6. Merge outputs with Router v0.2  
7. Apply persistent memory hooks  
8. Produce final action packet  
9. Log to Memory Event Ledger  

## Pseudocode

```
loop:
    event = receive_event()
    norm = normalize(event)
    st_context = stm.retrieve(norm)
    
    red_out = red.process(norm, st_context)
    blue_out = blue.process(norm, st_context)
    green_out = green.process(norm, st_context)
    
    merged = router.merge([red_out, blue_out, green_out])
    
    final = memory_hooks.apply(merged)
    
    ledger.log(event, merged, final)
    
    send(final)
```
