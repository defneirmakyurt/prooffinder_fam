# Where H-C5-011 stops

Strongest statement proved (given Lemma A): every induced forest F of Q_9 with |O \ F| <= 5 or |E \ F| <= 5 has
|F| <= 277 (in fact tau(G_2[F n E]) <= |O \ F| when |O \ F| <= 5, i.e. rung R9 for z <= 5, with slack 2); hence every
labelling whose S_f = {down >= 2} has <= 5 vertices of one parity has >= 2392 uphill paths. Unconditional bound
unchanged: U(Q_9) >= 2312. U(Q_9) >= 2369 is NOT proved.

Exact failing rung: R9 for 6 <= z <= 116 (proof.md Step 15).
Method that closes z <= 5: cluster decomposition (proof.md Steps 8-11): tau(G_2[M]) <= sum over clusters C of Z
(components of the distance-2 graph on Z) of tau*(C), where tau*(C) depends only on C; then an exhaustive,
symmetry-reduced computation (code/cluster_tau.py) shows tau*(C) <= |C| for all connected C with |C| <= 5
(1, 1, 2, 8, 31 classes). Exact (unpruned) values for |C| <= 4: tau*(C) - |C| in {-1, 0}; never positive.
Why it stops at 5: the stdlib branch-and-bound needs about 2 minutes for |C| <= 5; the |C| = 6 layer did not finish
within the 10-minute cap (run TIMED OUT, see RAN). More importantly, the method cannot reach z ~ 116: clusters can be
arbitrarily large (up to z), and a size-k cluster needs an enumeration of classes growing quickly with k.
What would be needed: a uniform proof of "tau*(C) <= |C| for every connected set C of odd vertices" (supported by
all data for |C| <= 5; tight for C = O minus a maximum code, where tau(G_2[E]) = z), i.e. every C-valid M' contains
at least |M'| - |C| vertices with pairwise disjoint C-neighbourhoods; or a global argument/computation for large z.
Note: tau(G_2[M]) <= z for ALL forests would give F_9 <= 277 via (2), which is stronger than the cell needs; R9 only
needs tau <= z + 2, but the small-cluster data show no cluster with positive excess, so the slack 2 is not what
limits the method.
Stopping reason: the rung failed once structurally (no uniform argument found) and the computational extension
beyond 5 timed out; the time box was the binding constraint.
