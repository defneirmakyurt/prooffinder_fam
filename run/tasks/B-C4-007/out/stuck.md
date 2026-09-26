# Stuck point — B-C4-007

Rung R9 (UPPER bound for all partitions), proof.md Step 9.

Proved: d_B <= (k-1)(k-3) for every partition of n = T_{k-1}+1 of energy E_min or E_min+1
(Lemma 7 gives the exact value d_B(Q(h0;x,y)) = (k-h0) + (m-2)(k-1) on level E_min+1).

Missing: partitions of energy >= E_min+2. Let tau(lambda) = first time the orbit has energy <= E_min+1
and let Q(h0;x,y) = B^tau(lambda). Then d_B(lambda) = tau + (k-h0) + (m-2)(k-1). What is needed is a
"phase/arrival trade-off" lemma: tau + (k-h0) + (m-2)(k-1) <= (k-1)(k-3), i.e. an orbit that spends
tau steps above level E_min+1 must land on level E_min+1 with its hole-to-bead offset m (and hole row h0)
reduced accordingly. Equivalently one needs a potential on all partitions that (i) equals
(k-h0)+(m-2)(k-1) on level E_min+1, (ii) is <= (k-1)(k-3) everywhere, (iii) drops by >= 1 per step
until the cycle. I could not construct it in the time box. The natural candidates (energy excess, dominance
of diagonal counts c_d) do not see the rotation phase, while the long orbits (e.g. the extremal one) run at
constant energy with only the phase changing.

Note: the extremal orbits of maximal length are numerous (3, 12, 62, 288, ... partitions attain the maximum
for k = 5, 6, 7, 8, ...), so many high-energy partitions reach level E_min+1 exactly "in phase"; any proof must
control this exactly, not up to O(k).

Warning for whoever continues: Lemma 7 / Cor. 7' hold for k = 4 as well (bound 3 on the two lowest levels),
yet D_B(T_3+1) = D_B(7) = 4 (attained by (1,1,1,1,1,1,1), exhaustive run in out/tmp). So the missing trade-off
lemma is genuinely false for k = 4 and must use k >= 5; a high-energy start can beat the level-(E_min+1) maximum
when k is small.
