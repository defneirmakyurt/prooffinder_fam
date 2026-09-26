# Stuck point

Rung R9 (general exact upper bound): d_B(lambda) <= (k-1)(k-3) for EVERY partition lambda of T_{k-1}+1, k >= 5.

What is proved:
- Theorem N (proof.md Step 8): the bound holds for near states D(p,Q) (diagonals <= k-2 full,
  one hole on diagonal k-1, two cells on diagonal k).
- Corollary U1 (Step 7): d_B(lambda) <= min over removable cells c of d_B(lambda \ c) <= (k-1)(k-2),
  via monotonicity (Lemma M) and B-C2 at k-1.

Where it fails:
- Combining the two gives only d_B(lambda) <= t_0 + (k-1)(k-3), t_0 = entry time into near states,
  or (k-1)(k-2) = F(k) + (k-1). The missing ingredient is a potential/clock argument showing the
  transient before entering near states (or reaching other states whose remaining time is
  explicitly bounded) is compensated, i.e. states reached after t_0 steps have remaining time
  <= (k-1)(k-3) - t_0.
- Using only the VALUE D_B(T_{k-1}) = (k-1)(k-2) (B-C2) is insufficient for the corner-removal
  route: at k = 6 there are 26 partitions of 16 all of whose one-cell removals nu have
  d_B(nu) > 15 (894 such at k = 8). One would need the STRUCTURE of the partitions of T_{k-1}
  with d_B > (k-1)(k-3) (for one-hole-one-particle states these are exactly those with the
  particle immediately behind the hole, proof-level fact derivable as in Step 8), plus a
  time-shifted version d_B(lambda) <= t + d_B(B^t(lambda) \ c).
- A useful observation not yet exploited: if nu subset lambda with |nu| = |lambda| - 1, then
  B^t(lambda) = B^t(nu) u {one cell} for all t (Lemma M and cardinality); with two different
  removals nu1, nu2, B^t(lambda) = B^t(nu1) u B^t(nu2) whenever these differ, and lambda is
  cyclic as soon as both are one-hole states with different holes.
