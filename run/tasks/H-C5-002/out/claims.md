# Claims: H-C5-002

| claim | status | where proved |
|---|---|---|
| For every labelling f of Q_d: P(f) = 2^d + (d-1)\|S_f\| + sum_{u in S_f}(N(u)-2)up(u), S_f = {N >= 2}, all summands >= 0 | PROVED (new write-up here; not found in the sources searched) | proof.md Part A, Steps 1-7; sanity test code/check_identity.py (0 mismatches on 180 labellings + Q3..Q9) |
| V(Q_d) \ S_f induces a forest with exactly (#valleys) components; upper neighbours of S_f-vertices lie in S_f | PROVED | proof.md Steps 4-5 |
| U(Q_d) >= 2^d + (d-1) nabla(Q_d) | PROVED | proof.md Step 8 |
| U(Q_9) >= 2312 | PROVED (self-contained; weaker than the organisers' 2368) | proof.md Steps 8-9 |
| For every even-weight code M of length d with min distance >= 4: U(Q_d) <= 2^d + (d-1)(2^{d-1} - \|M\|) | PROVED | proof.md Step 10 |
| U(Q_9) <= 2400, labelling out/Q9.txt | COMPUTER-VERIFIED (code public: y, out/code/parity_code_construction.py; inbox/checker/verify.py -> VERIFIED 2400) | proof.md Step 10; out/tmp/parity_runs.log |
| Labellings out/Q3..Q8.txt with 14, 34, 88, 204, 464, 1040 uphill paths | COMPUTER-VERIFIED (verify.py) | out/tmp/parity_runs.log |
| U(Q_d) = 14, 34, 88, 204, 464, 1040 for d = 3..8 | CONDITIONAL on the cited values nabla(Q_d) = 3,6,14,28,56,112 (Beineke-Vandell 1996 via Bau survey; primary source not opened) | proof.md Step 11 |
| A labelling of Q_9 with <= 2399 uphill paths exists only if nabla(Q_9) <= 235 | PROVED | proof.md Step 8 |
| nabla(Q_9) >= 233 would imply U(Q_9) >= 2376 (solving the LOWER route of H-C5) | PROVED (implication only) | proof.md Step 8 |
| 225 <= nabla(Q_9) <= 237 | PROVED per Bau survey Thm 2.3 citing Bau et al. 2000 (argument not in survey); lower bound 225 re-proved here; upper bound superseded by nabla(Q_9) <= 236 from out/Q9.txt's forest | sources.md; proof.md Steps 9-10 |
| nabla(Q_9) <= 236 | PROVED (explicit forest: O_9 u M, M the 20-word code printed in out/tmp/parity_runs.log) | proof.md Step 10(a) |
| nabla(Q_9) = 236 (hence U(Q_9) = 2400) | CONJECTURED here; heuristic evidence only: 7 simulated-annealing runs for max induced forests of Q_9 (3 x 2e7, 3 x 1e8 moves: \|S\| = 236 each; 1 x 3e8 low-temperature: 238); none below 236 | RAN lines; out/code/mif_sa.c; out/code/check_forest.py |
| Minimum-size decycling sets of Q_9 need not be independent: the SA found decycling sets of size 236 with 234 vertices of one parity, 2 of the other, e(S) = 13, 83 forest components | COMPUTER-VERIFIED (code public: y; out/tmp/mif_Q9_s*.txt checked by code/check_forest.py) | RAN lines |
| The organisers' 2368 comes from nabla(Q_9) >= 232 | UNSURE (only the arithmetic 2368 = 2^9 + 8*232 is checked) | sources.md |
