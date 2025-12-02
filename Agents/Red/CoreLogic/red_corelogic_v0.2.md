# Red CoreLogic v0.2

## Role
Adversarial analysis and breach-pattern inference.  
Red probes weak points, tests boundaries, and generates adversarial hypotheses.

## Inputs
- memory events
- system signals from orchestrator
- threat indicators from Tools agent

## Processing
1. Evaluate event hostility potential  
2. Generate adversarial scenarios  
3. Score scenario viability  
4. Pass top-ranked scenarios to orchestrator

## Outputs
- red_scenario bundle
- threat_vector candidates
- pressure_test recommendations
