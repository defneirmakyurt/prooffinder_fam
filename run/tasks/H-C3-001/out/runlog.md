# Run log H-C3-001 (all wall times measured with date +%s.%N; 4-core shared machine)
Reading of the brief: none ambiguous; conventions exactly as in RULES.
| run | params | result | status | wall |
|---|---|---|---|---|
| forest_search.py (Python SA) | d6 p26 seed1 steps20000 | killed by timeout 600 s, nothing found | TIMED OUT | 600.0 s |
| forest_search (C) | d6 p26 seed1, 50 restarts x 2e5 steps (1e7 steps) | not found, best cost 3 | COMPLETED (SEARCH-FOUND-NOTHING) | 20.0 s |
| forest_search | d6 p26 seed2, 10x2e5 | best cost 3 every restart | COMPLETED (SEARCH-FOUND-NOTHING) | ~4 s |
| forest_search | d5 p13 seed1 20x1e5 ; d5 p14 seed1 | p13 best cost 1; p14 found (88) | COMPLETED | <5 s |
| forest_search | d6 p27 seed1 10x2e5; seed11 8x1e6 | best cost 2, not found | COMPLETED (SEARCH-FOUND-NOTHING) | 15.1 s (seed11) |
| forest_search | d3 p3, d4 p6 seed1 | found; checker 14, 34 | COMPLETED | <1 s |
| forest_search | d6 p28 seed5 | found in 8393 steps, 12 trees -> Q6_alt1.txt, checker 204 | COMPLETED | 0.06 s |
| anneal | d6 seed1, 4 restarts x 2e6 steps, T 3.0->0.2 | 204 in every restart -> Q6.txt | COMPLETED | 9.0 s |
| anneal | d6 seed2, seed3, 3 restarts x 3e6 steps, T 2.0->0.1 | 204 each (seed2 -> Q6_alt2.txt) | COMPLETED | ~13 s each (not separately timed) |
| exhaust_forest | d2..d4 controls; d5 p12,13,14; d6 p26,27,28 | 0,0,80 ; 0,0,240 solutions; nodes 1384/1628/1822; 28226/32295/36055 | COMPLETED, exhaustive | 0.005-0.02 s |
| exhaust_general | d6 mode0 cmax11 P-window [0,64] | 0 solutions, 39783 nodes | COMPLETED, exhaustive | 0.008 s |
| exhaust_general | d6 mode1 cmax7 [0,64] (64 sets S) | 0 solutions, 2889353 nodes | COMPLETED, exhaustive | 0.26 s |
| exhaust_general | d6 mode2 cmax3 [0,64] (2016 sets S) | 0 solutions, 103326594 nodes | COMPLETED, exhaustive | 4.1 s |
| exhaust_general controls | d6 mode0/1/2 cmax12; d3,d4 | 240 / 14400 / 597600; 8; 8 | COMPLETED | <5 s |
| run_all.sh | full rebuild + rerun | all as above, artefacts byte-identical | COMPLETED | 9.7 s |
Stopping condition: annealer 204 over 3 seeds / 10 restarts plus a second method (forest search) -> stopped upper search at 204; lower bound then met it.
