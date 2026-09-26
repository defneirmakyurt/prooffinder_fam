No known gap remains in proof.md (both bounds written out).
Points a referee should check most carefully:
1. B7 (Griggs-Ho Lemma 3.5): the invariant I(m) and the termination bound m <= q-p-2; the final check q' <= p+1.
2. B5, subcase i = t-k with all c_j in {k-1,k}: the identification of the parts of B^{t-1}(lambda) with the columns having a 1 in row t, and the count T_k - 1.
3. B9: the chain length bound (at most k-3 applications of B7) and the arithmetic p_0 <= k^2 - 2k.
Abandoned route: a pure diagonal/energy argument (E non-increasing, strict at slides, 0.3) only gives a cubic-type bound, not k^2 - k.
