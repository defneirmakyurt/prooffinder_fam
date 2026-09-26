# Stuck point: B-C2-002

Failing rung: R9, the upper bound d_B(lambda) <= k^2 - k for an ARBITRARY partition lambda of T_k (k >= 12;
k <= 11 is covered by exhaustive exact computation).

What is proved: once the orbit is in the two-track region R_k (tracks 1..k-1 full, nothing on tracks >= k+2),
the process is pure rotation of holes (track k, period k) and cells (track k+1, period k+1) plus annihilation of
the pair (hole at row 1, cell at row 2); the last pair annihilated was present at the time of entry, so
the remaining time is tau(h,i) <= k^2 - k, where (h,i) are the rows at ENTRY time (proof.md Steps 10-14).

Where it fails: for lambda outside R_k, the orbit enters R_k only at some time t_0 > 0 (observed up to
t_0 = T_{k-1} for k <= 8), so Step 14 yields only d_B <= t_0 + (k^2 - k). One needs that the pairs present at
entry (more precisely: the pair annihilated last) have collision time <= k^2 - k - t_0.

Attempt 1 (failed): prove the invariant t + max_{pairs at time t} tau(pair) <= k^2 - k. It is FALSE
(out/tmp/explore2.py finds violations for every 3 <= k <= 8: max of t + max tau reaches 7, 14, 23, 34, 47, 62
versus k^2-k = 6, 12, 20, 30, 42, 56). Late pairs with large nominal tau exist but are destroyed by other
annihilations first, so any correct argument must use the interaction between several pairs.

Attempt 2 (failed): two-phase additive bound (entry time into R_k) + (time inside R_k). Both terms are
individually sharp-ish (entry up to T_{k-1}, inside up to k^2-k), so the sum is not <= k^2-k.

What would be needed: a lemma controlling the absolute phases (residues mod k(k+1) of their collision times)
of holes arriving on track k and cells arriving on track k+1 via compaction after time 0, e.g. showing that the
last-annihilated pair has collision residue in [1, k^2-k] and is annihilated at its first occurrence; or a
potential function on all partitions of T_k, decreasing by >= 1 per step, bounded by k^2-k. Not found within the
time box.
