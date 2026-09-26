# Stuck point (A-C5-001)

The proof is complete and exact for d=2 (Step 5 of proof.md), and a true but strictly weaker
general bound (T >= (d+2)/d, all d>=2) is established in Step 4.

The exact target for d>=3 is NOT proved. The precise obstruction:

- The natural linear-algebra route (Gram matrix rank <= d, Cauchy-Schwarz on eigenvalues,
  Step 3) only bounds the *sum of squared cosines* sum a_ij^2 >= (d+2)/d. Converting this into a
  bound on T = sum arcsin|a_ij| requires a pointwise inequality between arcsin(x) and some
  function of x^2; the elementary inequality arcsin(x) >= x^2 (Step 4) is too lossy: it treats
  every pair symmetrically, whereas the true extremal configuration (two doubled orthogonal axes)
  concentrates all the "excess" on exactly 2 pairs (a_ij=1 there, 0 elsewhere) rather than
  spreading it evenly, and the function t -> arcsin(sqrt(t)) is neither globally convex nor
  concave (concave on [0,1/2], convex on [1/2,1]), so no single Jensen-type inequality in one
  direction converts a *sum* constraint into the required lower bound on T without an extra
  extremal/rearrangement lemma that itself needs proof (attempted informally in proof.md Step 6b,
  not completed rigorously, and even if completed the resulting bound is still short of pi for
  d>=3 -- see Step 6).
- The averaging idea from a hypothetical (d+1)-line ("corank 1") analogue of this same theorem
  (Step 6a) is algebraically insufficient by itself: even granting that lemma, double counting
  over the N deletions only recovers T >= (d+2)/d * (pi/2), which is < pi for every d>=3.
- No fully rigorous route achieving the exact constant pi (equivalently the "-2" in the target)
  for general d>=3 was found within the time box. This would need either (i) a genuinely sharper
  spectral/algebraic inequality that is tight exactly at the two-doubled-axes (and other) extremal
  configurations for every d, or (ii) an inductive/combinatorial argument (e.g. via the metric
  triangle inequality for theta on lines, which does hold since theta is the quotient of the
  spherical geodesic metric by the antipodal map, but was not successfully combined with the
  dimension/rank constraint into a proof within the time available).

Nothing beyond this was attempted; the two distinct approaches above (Step 6a, Step 6b) both hit
the same underlying obstruction (the linear/averaging relaxations are not tight for d>=3), matching
the brief's stopping condition.
