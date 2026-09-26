# Claims

| claim | status | where proved (file, step) |
|---|---|---|
| S = C(N,2)pi/2 - Phi; for N=d+2 target <=> Phi >= pi | PROVED | proof.md S0 (0.1-0.3) |
| Lemma 1: arcsin(R cos(t-t0)) concave where R cos(t-t0) >= 0 (0<R<=1) | PROVED | proof.md L1 |
| Lemma 2 / Cor 2': path-orthogonal sequence => y_2..y_m independent; path spans >= n-1, cycle spans >= n-2 | PROVED | proof.md L2 |
| Lemma 3: connected graph, max degree <= 2 => path or cycle | PROVED | proof.md L3 |
| Lemma 4: a maximiser exists in which every line is orthogonal to all others or its orthogonal lines span its complement | PROVED | proof.md L4 (4.1-4.6) |
| Lemma 5: n path-orthogonal unit vectors in an (n-1)-dim space: sum of edge phi >= pi/2 (from A-C2) | PROVED | proof.md L5 |
| Lemma 6: 3- and 4-cycles spanning dim n-2: sum of edge phi >= pi | PROVED | proof.md L6 |
| Lemma 7: 5-cycle in R^3 (non-adjacent orthogonal, edges non-orthogonal): sum of edge phi >= pi | PROVED | proof.md L7 (7.1-7.10) |
| Lemma 8: 6-cycle in R^4 (non-adjacent orthogonal, edges non-orthogonal): sum of edge phi > pi | PROVED | proof.md L8 (8.1-8.9) |
| (a) 5 lines in R^3: S <= 4 pi | PROVED | proof.md S9 (d=3; 9.2 uses A-C1, 9.3 uses Lemmas 2-7) |
| (b) 6 lines in R^4: S <= 13 pi/2 | PROVED | proof.md S9 (d=4; 9.2 uses part (a), 9.3 uses Lemmas 2-8) |
| Both bounds attained (e1,e1,e2,e2,e3 and e1,e1,e2,e2,e3,e4) | PROVED | proof.md 9.5 |

Note: out/code/ holds floating-point sanity checks (evidence only, not a status claim; no proof step depends on them). See out/code/README.md.
