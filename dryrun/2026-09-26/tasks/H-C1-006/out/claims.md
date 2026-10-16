# Claims: H-C1-006 (literature)

| claim | status | where proved |
|---|---|---|
| Recurrence `N(v) = [down(v)=0] + sum_{w~v, f(w)<f(v)} N(w)` for any finite simple graph and labelling | PROVED | out/proof.md Step 2 (explicit bijection, well-definedness + injectivity + surjectivity written out) |
| `N(v) >= 1` for every vertex, every labelling | PROVED | out/proof.md Step 3 |
| `sum_v up(v) = |E| = sum_v down(v)` | PROVED | out/proof.md Step 1 |
| Identity `P = #valleys + sum_v N(v)*up(v)` for any finite simple graph and labelling | PROVED | out/proof.md Step 4; also verified computationally on 2000 random labellings for each d=2..5 and on all 8! labellings of Q_3 (run 5) |
| `P >= |E| + #valleys >= |E| + 1` for every finite simple graph and labelling (so `U(G) >= |E|+1`) | PROVED here; also KNOWN (this is the lower-bound half of the official IMO 2022 P6 solution, stated there for the grid) | out/proof.md Step 5; source: Bajnok, arXiv:2509.19303, Problem 6 solution (opened) |
| If `P = |E| + 1` and G has no isolated vertex, then G has exactly one valley, `N(v) = 1` for every v with `up(v) >= 1`, and `|E| = (n - 1 - m) + sum_{v: up(v)=0} deg(v)` where `m = #{v : up(v)=0}` | PROVED | out/proof.md Step 6. The "exactly one valley" half is stated (for the grid) in Bajnok's write-up; the down-degree count is not in any source I found |
| No labelling of Q_3 has exactly 13 uphill paths; no labelling of Q_4 has exactly 33 | PROVED (divisibility: `2m = 5` resp. `3m = 17` has no integer solution) | out/proof.md Step 7 |
| **U(Q_3) >= 14** | PROVED (by hand, no computer) | out/proof.md Steps 5+7 |
| **U(Q_4) >= 34** | PROVED (by hand, no computer) | out/proof.md Steps 5+7 |
| `U(Q_3) <= 14`, attained by out/Q3.txt | COMPUTER-VERIFIED (code public: y, out/code/uphill.py; also hand-checkable, the N-values are written out) | out/proof.md Step 8, runlog run 1 |
| `U(Q_4) <= 34`, attained by out/Q4.txt | COMPUTER-VERIFIED (code public: y, out/code/uphill.py) | out/proof.md Step 8, runlog run 4 |
| **U(Q_3) = 14** | PROVED (lower bound by hand) + COMPUTER-VERIFIED (upper bound) | the four rows above |
| **U(Q_4) = 34** | PROVED (lower bound by hand) + COMPUTER-VERIFIED (upper bound) | the four rows above |
| min over ALL 8! labellings of Q_3 is 14, attained by 7104 of them | COMPUTER-VERIFIED (code public: y) | out/code/q3_exhaustive.py, runlog run 2. Independent confirmation of the d=3 lower bound |
| `U(Q_d) >= d*2^{d-1} + 2` for every d >= 3 | PROVED, but OUTSIDE the cell's range and not used | out/proof.md, closing Remark |
| Any value of U(Q_d) for d >= 5 | NOT CLAIMED | nothing here bears on d >= 5 |

Nothing above is a citation of the cell's own statement: no source I found states U(Q_3) or U(Q_4).
The only thing taken from the literature is the general inequality `P >= |E| + 1` and the idea of
looking at the equality case, and both are re-proved in full in out/proof.md.
