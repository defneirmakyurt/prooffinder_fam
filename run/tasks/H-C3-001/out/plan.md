# Plan: H-C3-001, U(Q_6)  (searcher, BLIND, phase 1)

Target: the integer U(Q_6), both halves: (a) explicit labelling, (b) lower bound over all labellings.
Start 13:10 UTC, time box 45 min.

Notation: f labelling, N(v) = number of uphill paths ending at v, V = number of valleys,
up(v) / down(v) = number of neighbours with larger / smaller label. |E(Q_6)| = 192.

## Ladder

| rung | claim | depends on | status |
|---|---|---|---|
| R1 | checker in inbox/checker/verify.py reproduces hand-computed small cases (Q_2 one-valley labelling = 5; Q_3 bipartite labelling = 4+12 = 16) | - | CHECKED |
| R2 | identity: total = V + \|E\| + sum_v up(v)(N(v)-1), and N(v) >= 1 for all v (written proof, lower_bound.md L1-L3; no separate random test was run) | - | PROVED |
| R3 | total = 193 is impossible for Q_6 (counting argument on the "N=1 / peak" partition); hence U(Q_6) >= 194 | R2 | PROVED |
| R4 | reduction: an independent set P of Q_6 with \|P\| = 26 and Q_6 - P a forest gives a labelling with exactly 194 uphill paths | R2 | PROVED |
| R5 | search (program) finds such P; labelling built and scored 194 by the provided checker | R4, R1 | REFUTED |
| R6 | second, independent method (annealing directly on labellings) reaches 204 (not 194); forest search p=28 gives a second 204 artefact | R1 | CHECKED |
| R7 | sanity on Q_3: same reduction + exhaust_general 3 0 1 gives 0 and a forest labelling scores 14 (no brute force over 8! was run) | R2 | CHECKED |
| R8 | conclusion U(Q_6) = 194 | R3, R5 | REFUTED |
| R9 | S empty case: independent P with forest complement and c(A) <= 11 do not exist (exhaustive; also |P| = 26, 27 counts 0) | R2 | CHECKED |
| R10 | general reduction T <= 203 => (S,P) with |S| <= 2, c(A) <= 11/7/3; exhaustive over all S, P finds none => T >= 204 | R2, R9 | PROVED (computer-assisted) |
| R11 | U(Q_6) = 204 (Q6.txt VERIFIED 204 + R10) | R6, R10 | PROVED |

Notes: R5 REFUTED = no independent P of size 26 with forest complement exists (exhaust_forest 6 26 -> 0), so 194 is not attained;
R8 as first stated (U = 194) REFUTED, replaced by R11. R7 check: Q_3 forest labelling VERIFIED 14 and exhaust_general 3 0 1 -> 0 (so U(Q_3)=14 by the same argument, not a hand-in here).
