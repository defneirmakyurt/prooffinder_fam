# Code for B-C4-006

`check.py` is stdlib-only Python 3 with exact integer arithmetic. Run it as

    /usr/bin/time -p python3 check.py 11 60 25

Arguments: KMAX_EXHAUSTIVE KMAX_FAMILY KMAX_LEVEL1 (defaults 11 60 25). Measured: real 16.74 s (laptop).

It checks three things:
1. **Exhaustive** D_B(T_{k-1}+1) for 5 <= k <= 11, over all partitions. Cyclicity is tested via E = E_min (proof.md Step 6).
   Output: D_B = (k-1)(k-3) for each k. EVIDENCE ONLY: it proves nothing for k >= 12, and the written proof does not rest on it.
2. **Lower-bound family**, 5 <= k <= 60. lambda^(k) is non-cyclic (B-C1 form test) for F-1 steps.
   B^{F-1} = (k,k-1,k-3,...,2) and B^F = lambda(e_3). This is a sanity check of proof.md Step 13, which proves it for all k.
3. **Level-1 closed form**, 5 <= k <= 25. It enumerates all triples (Q; P<P'), checks that the diagram test agrees with the
   constraint P,P' not in {Q,Q+1} (Step 8) and that E = E_min+1. It checks that the true d_B equals
   T = t_0 + (min(pi_0,pi'_0) - 1)(k-1) (Steps 11-12) and that max T = (k-1)(k-3). For k <= 9 it also brute-force
   cross-checks the number of level-1 partitions. This is a sanity check of Steps 8-12, which are proved for all k.

No step of proof.md rests on this computation.
