# Router v0.2

Router v0.2 merges multi agent outputs into one coherent action.  
Conflict resolution is performed using a priority matrix.

## Priority Matrix

Red: high priority on risk  
Blue: high priority on stability  
Green: high priority on optional utility  
Purple: final arbitration layer

## Merge Rules

1. If Red flags a hard stop, override everything.  
2. If Blue detects system instability, defer to Blue.  
3. Green contributes options but never overrides.  
4. Purple resolves ties using the holonomic weighting vector.

## Pseudocode

```
def merge(outputs):
    if outputs.red.hazard:
        return outputs.red
    
    if outputs.blue.stability < threshold:
        return outputs.blue
    
    merged = combine(outputs.red, outputs.blue, outputs.green)
    final = apply_holonomic_weights(merged)
    return final
```
