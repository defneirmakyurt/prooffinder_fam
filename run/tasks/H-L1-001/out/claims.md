# Claims: H-L1-001

| claim | status | where proved |
|---|---|---|
| For every finite simple graph G and labelling f: up(v)+down(v)=deg(v); v valley iff down(v)=0; P finite, P = sum_v N(v) | PROVED | proof.md Step 1 |
| sum_v up(v) = |E| = sum_v down(v) | PROVED | proof.md Step 2 |
| N(v) = [down(v)=0] + sum_{w~v, f(w)<f(v)} N(w) | PROVED | proof.md Step 3 |
| N(v) >= 1 for every v | PROVED | proof.md Step 4 |
| P = |Val| + sum_v N(v) up(v) | PROVED | proof.md Step 5 |
| P - (|E|+1) = (|Val|-1) + sum_v (N(v)-1) up(v) >= 0; hence U(G) >= |E(G)|+1 for every finite simple graph with >= 1 vertex | PROVED (the inequality is the known IMO 2022 P6 lower-bound argument, attributed in sources.md; proof written out in full here) | proof.md Step 6 |
| If G has no isolated vertex and P = |E|+1, then |Val| = 1, N(v)=1 whenever up(v)>=1, down(v)=1 for every v that is neither the valley nor a local maximum, and |E| = n-1-m+sum_{up(v)=0} deg(v) | PROVED | proof.md Step 7 |
| For every integer k >= 2, k does not divide 2^k - 1 | PROVED (classical; proved here from the division algorithm, Euclid's lemma and pigeonhole; no citation used) | proof.md Step 8 |
| Q_d is d-regular, 2^d vertices, d*2^(d-1) edges | PROVED | proof.md Step 9 |
| For d >= 3 no labelling of Q_d has exactly d*2^(d-1)+1 uphill paths | PROVED | proof.md Step 10 |
| **TARGET: for every d >= 3 and every labelling f of Q_d, P(f) >= d*2^(d-1)+2; i.e. U(Q_d) >= |E(Q_d)|+2** | **PROVED** | proof.md Step 11 |
| The bound is attained for d = 3, 4 (U(Q_3)=14, U(Q_4)=34) | attaining labellings COMPUTER-VERIFIED (code public: y, out/code/sanity.py check F); lower bound PROVED (Step 11) | sanity.py checks C, F; the labellings are from inbox/earlier-proof.md Step 8 |
| For d = 2 the argument gives nothing: Q_2 has labellings with P = |E|+1 = 5 | COMPUTER-VERIFIED (code public: y, exhaustive over 4! labellings) | sanity.py check D |
| Lemma 7's identity holds on every equality labelling of Q_1, Q_2, P4, K_{1,4}, C5, paw; K4 has none | COMPUTER-VERIFIED (exhaustive over all labellings of these graphs); sanity check only | sanity.py check D |
| k does not divide 2^k-1 for 2 <= k <= 10^5; (d-1) does not divide 2^(d-1)(d-2)+1 for 3 <= d <= 2000 | COMPUTER-VERIFIED (finite range; sanity check only, not used in the proof) | sanity.py checks A, B |
| Any source states a lower bound for, or a value of, U(Q_d) | not found in the sources searched (list in sources.md); no page could be opened this run | sources.md |
