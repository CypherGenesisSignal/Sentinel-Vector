# Test Suite: Holonomic Computation

## Test 1. Breadth Calculation
Input: 5 parallel agent signals  
Expected: breadth = 5

## Test 2. Depth Calculation
Input: nested context chain (4 layers deep)  
Expected: depth = 4

## Test 3. Coherence Calculation
Input: 3 aligned signals with 0.85 similarity  
Expected: coherence ≈ 0.85

## Test 4. Decision Engine
Input: high breadth, low depth  
Expected: broadcast only

## Test 5. Persistence Decision
Input: high coherence  
Expected: persist = true
