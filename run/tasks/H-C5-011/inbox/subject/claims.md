# Claims: H-C5-007 (EXPLOIT of H-C5-002, LOWER route)

| claim | status | where proved (file, step) |
|---|---|---|
| Lemma A (every labelling of Q_d has >= 2^d + (d-1)abs(S_f) paths, S_f = {down >= 2}, V \ S_f induces a forest) | ASSUMED (brief ASSUMPTIONS line) | inbox/lemmaA-claims.md sec. A; restated proof.md Step 1 |
| Reduction: F_9 <= 279 implies U(Q_9) >= 2376 | PROVED | proof.md Step 2 |
| Parity swap sigma(x) = x + e_1 maps induced forests to induced forests and swaps E \ F, O \ F | PROVED | proof.md Step 3 |
| Lemma 1: distance-2 pairs in M = F n E have a common neighbour in Z = O \ F | PROVED | proof.md Step 4 |
| Lemma 2: H_o is acyclic; z >= 1 + (t_o-1)(t_o-2)/2 for o in Z | PROVED | proof.md Step 5 |
| Lemma 3: even-weight length-9 code with min distance >= 4 has <= 21 words | PROVED (hand proof) + CHECKED (arithmetic: code/check_code_bound.py, ALL OK) | proof.md Step 6 |
| abs(F) <= 277 + tau(G_2[F n E]) - abs(O \ F) for every induced forest F of Q_9 | PROVED | proof.md Step 7, (2) |
| tau(G_2[M]) <= sum_{o in Z} (t_o - 1)^+ | PROVED | proof.md Step 7, (3) |
| Every induced forest F of Q_9 with abs(E \ F) <= 3 or abs(O \ F) <= 3 has abs(F) <= 279 | PROVED | proof.md Steps 8-9 |
| Every labelling f of Q_9 with abs(S_f n E) <= 3 or abs(S_f n O) <= 3 has >= 2376 uphill paths | PROVED (given Lemma A) | proof.md Step 10 |
| R9: tau(G_2[F n E]) <= abs(O \ F) + 2 for every induced forest with abs(O \ F) <= abs(E \ F) | GAP (proved only for abs(O \ F) <= 3) | proof.md Step 11 |
| F_9 <= 279 (nabla(Q_9) >= 233) | GAP (follows from R9) | proof.md Steps 7, 11 |
| U(Q_9) >= 2369 (the cell) | GAP (follows from F_9 <= 279) | proof.md Steps 2, 11 |
| U(Q_9) >= 2312 (strongest unconditional bound here; from subject H-C5-002) | PROVED (edge counting + Lemma A) | proof.md "What is established" |
