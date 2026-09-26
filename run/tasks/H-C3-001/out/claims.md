# Claims H-C3-001
| claim | status | where shown |
|---|---|---|
| provided checker reproduces hand cases (Q_2 one valley = 5, Q_3 bipartite = 16) | CHECKED | out/tmp/q2_onevalley.txt, q3_bipartite.txt; runlog |
| T = V + 192 + X, X = sum up(v)(N(v)-1), each term 0 or >= 4 | PROVED | lower_bound.md L1-L4 |
| peaks independent; N=1 vertices induce a forest with exactly V components | PROVED | lower_bound.md L5, L6 |
| T <= 203 implies (S,P) with |S|<=2, P indep., forest complement, c(A) <= 11/7/3 | PROVED | lower_bound.md Reduction |
| no such (S,P) exists: exhaustive over ALL S of size 0,1,2 and ALL P (no symmetry reduction, no size window) | CHECKED | exhaust_general.c, runlog rows (nodes 39783 / 2889353 / 103326594) |
| every labelling of Q_6 has >= 204 uphill paths (exhaustive over the reduced class given soundness of prunings (i)-(iii)) | PROVED (computer-assisted) | lower_bound.md |
| out/Q6.txt (= best.txt) has 204 uphill paths | CHECKED | provided checker: VERIFIED 204 |
| out/Q6_alt1.txt (forest-search method), out/Q6_alt2.txt (anneal seed 2) have 204 | CHECKED | provided checker: VERIFIED 204 |
| U(Q_6) = 204 | PROVED (computer-assisted) | lower_bound.md + Q6.txt |
Library dependence: verify.py = library entry H-uphill-checker, used only as scorer (lemma assumed: it counts uphill paths per the statement's definitions, via recursion L1).
