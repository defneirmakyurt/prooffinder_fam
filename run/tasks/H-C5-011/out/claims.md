# Claims: H-C5-011 (EXPLOIT / REPAIR of H-C5-007, rung R9)

| claim | status | where proved (file, step) |
|---|---|---|
| Lemma A (every labelling f of Q_d has >= 2^d + (d-1)abs(S_f) uphill paths; V \ S_f induces a forest) | ASSUMED (brief ASSUMPTIONS line; gated VALID) | inbox/gated-lemmaA.md; restated proof.md Step 1 |
| Parity swap sigma(x) = x + e_1 maps induced forests to induced forests, O \ sigma F = sigma(E \ F) | PROVED | proof.md Step 2 |
| Lemma 1: distance-2 pairs of M = F n E have a common neighbour in Z = O \ F | PROVED | proof.md Step 3 |
| Lemma 3: even-weight length-9 code with minimum distance >= 4 has <= 21 words | PROVED (hand) + CHECKED arithmetic (code/check_code_bound.py) | proof.md Step 4 |
| (2): abs(F) <= 277 + tau(G_2[M]) - z for every induced forest | PROVED | proof.md Step 5 |
| (4): tau(G_2[M]) <= sum over clusters C of Z of tau(G_2[M_C]) | PROVED | proof.md Steps 8-9 |
| (5): M_C is C-valid for every cluster C, hence tau(G_2[M_C]) <= tau*(C) | PROVED | proof.md Step 10 |
| tau* invariant under x -> pi(x) + v (v even) | PROVED | proof.md Step 11 |
| tau*(C) <= abs(C) for every set C of <= 5 odd vertices connected in the distance-2 graph | CHECKED (exhaustive up to symmetry; 1+1+2+8+31 classes; reduction written) | proof.md Step 12; code/cluster_tau.py |
| Same for clusters of size 6 | NOT ESTABLISHED (run TIMED OUT) | stuck.md |
| R9 (indeed tau(G_2[M]) <= z) for every induced forest with z = abs(O \ F) <= 5 | PROVED (from Steps 5, 9, 10, 12) | proof.md Step 13 |
| Every induced forest F with abs(O \ F) <= 5 or abs(E \ F) <= 5 has abs(F) <= 277 | PROVED | proof.md Step 13 |
| Every labelling f of Q_9 with abs(S_f n E) <= 5 or abs(S_f n O) <= 5 has >= 2392 uphill paths | PROVED (given Lemma A) | proof.md Step 14 |
| R9 for 6 <= z <= 116 | GAP | proof.md Step 15; stuck.md |
| F_9 <= 279 | GAP (would follow from R9) | proof.md Steps 6-7 |
| U(Q_9) >= 2369 (the cell) | GAP | proof.md Step 6 |
| Heuristic: simulated annealing finds induced forests of Q_9 of size 276, none larger (3 runs) | exploratory, not a claim | code/sa_forest.c |
