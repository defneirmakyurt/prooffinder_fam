# Claims: H-C2-002

| claim | status | where proved |
|---|---|---|
| For every labelling f of any d-regular graph G on n vertices: P(f) >= n + (d-1)\|D_f\|, D_f = {v : down(v) >= 2} | PROVED | proof.md Steps 1-6 |
| D_f is a decycling set for every labelling f of every graph | PROVED | proof.md Step 5 |
| U(G) >= n + (d-1) nabla(G) for every d-regular G | PROVED | proof.md Step 6 |
| Edge identity (d-1)\|D\| = \|E\| - n + c + e(D) for a decycling set D of a d-regular graph | PROVED | proof.md Step 7 |
| U(Q_5) >= 84 (by hand) | PROVED | proof.md Steps 6-7 |
| nabla(Q_5) >= 14 (no 13-vertex decycling set) | COMPUTER-VERIFIED (code public: y; out/code/decycle.py; reduction written in Step 8; cross-checked without the edge cut and by an independent C brute force out/code/brute13.c) | proof.md Step 8 |
| U(Q_5) >= 88 | PROVED, computer-assisted (Steps 6 + 8) | proof.md Step 9 |
| out/Q5.txt has exactly 88 uphill paths | PROVED by hand count + COMPUTER-VERIFIED (verify.py: VERIFIED 88) | proof.md Step 10 |
| **U(Q_5) = 88** | PROVED (computer-assisted lower bound) | proof.md Conclusion |
| If a d-regular G has an independent minimum decycling set then U(G) = n + (d-1) nabla(G) | PROVED | proof.md By-product (A) |
| Labellings of Q_6, Q_7, Q_8 with 204, 464, 1040 uphill paths | COMPUTER-VERIFIED (verify.py) | out/Q6.txt, Q7.txt, Q8.txt; by-product (B) |
| U(Q_6) = 204 (neighbour cell, not this cell) | PROVED, computer-assisted (decycle.py 6 27 -> NONE, 8.2 s) | proof.md By-product (C) |
| U(Q_7) = 464, U(Q_8) = 1040 | CONJECTURED (would follow from nabla(Q_7) >= 56, nabla(Q_8) >= 112, which a search summary asserts but I could not open; my d = 7 search TIMED OUT) | proof.md By-product (D) |
| Organisers' U(Q_9) <= 2400 equals the construction of By-product (B) with \|S\| = A(9,4) = 20 | UNSURE (arithmetic identity 2560 - 8*20 = 2400 checked; A(9,4) = 20 from memory, not opened; Q9 not built) | proof.md By-product (B) |
| Simulated annealing (random restarts) never went below 88 / 204 / 464 / 1040 for d = 5/6/7/8 | COMPUTER-VERIFIED heuristic observation, proves nothing | runlog.md |
