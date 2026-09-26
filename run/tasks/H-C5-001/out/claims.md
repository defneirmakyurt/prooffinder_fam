# Claims H-C5-001

| claim | status | where shown |
|---|---|---|
| Target: labelling of Q_9 with <= 2399 uphill paths | NOT ACHIEVED (SEARCH-FOUND-NOTHING) | runlog.md runs 5-19 |
| Q9.txt (= best.txt) is a labelling of Q_9 with 2400 uphill paths (matches, does not beat, the known bound) | CHECKED (provided checker: VERIFIED 2400) | runlog run 9; code/README.md |
| For every labelling of Q_d: F = {N=1} induces a forest with #trees = #valleys, and total = 2^d + (d-1)|S| + sum_{S-edges w<v}(N(w)-2) >= 2^d + (d-1)|S|, S = V\F a feedback vertex set | PROVED | reduction.md Steps 0-6 |
| Consequence d=9: a labelling with <= 2399 uphill paths requires a feedback vertex set of Q_9 of size <= 235 | PROVED | reduction.md (C) |
| An independent S with V\S a forest yields a labelling with exactly 2^d + (d-1)|S| uphill paths | PROVED; CHECKED on d=3,4,5,9 | reduction.md part (b); runlog runs 1, 9 |
| Min independent FVS of Q_d is 3, 6, 14, 28, 56, 112 for d = 3..8 | exploratory SAT only (no DRAT) -- NOT claimed | runlog runs 1-4 |
| No independent FVS of Q_9 with |S| <= 235 containing both parities | exploratory SAT UNSAT (no DRAT) -- NOT claimed | runlog run 13 |
| No G-invariant IFVS of size <= 235 for 12 listed groups G | exploratory SAT UNSAT (no DRAT) -- NOT claimed | runlog run 6 |

No library lemma is used in any proof. The checker (library entry H-uphill-checker, copied as
code/verify.py) is used only for scoring. No exhaustive search was completed for d = 9; nothing here is
a lower bound on U(Q_9).
