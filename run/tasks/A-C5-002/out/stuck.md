# Where the argument fails for general d≥3

Two distinct approaches were carried out to completion (i.e., pushed until each produced a
concrete, checkable obstruction), neither closes the target for d≥3.

**Approach A (aggregate second moment + Jensen convexity of arcsin).**
The Gram-matrix rank constraint gives a lower bound on Σ_{i<j} G_ij² (Step 3 of proof.md), which
via |G_ij| ≥ G_ij² and Jensen's inequality (arcsin is convex on [0,1]) gives a lower bound on
Σ arcsin|G_ij|. At d=2 (the one case where we also know the true answer) this bound evaluates to
≈2.039, short of the required π by ≈1.10 rad (exact computation in
out/code/approach_A_check.py). The reason, stated precisely (proof.md Step 8): Jensen's bound
from one aggregate moment is tightest for "spread out" (equal) configurations of |G_ij|, but the
true extremal configuration (2 pairs coincident, rest orthogonal) is maximally *concentrated* —
exactly the opposite extreme — so a single-moment Jensen bound structurally cannot certify the
needed inequality, independent of how the moment bound itself is sharpened.

**Approach B (Veronese/projector embedding into a sphere in Sym_0(R^d)).**
This is the natural generalization of the trick that solves d=2 (doubling map to S^1, itself the
d=2 special case of this embedding, proof.md Step 11). It would work if ang_P(x,x') ≥ 2θ(x,x')
held pointwise for all d, because then a hyperplane-separation bound on Σang_P (valid in any
dimension, by the same argument as Steps 18-20) would upper-bound Σθ_ij. This inequality is
**exactly true only at d=2** and **strictly reverses for every d≥3**: at θ=π/2, d=3, ang_P =
2π/3 < π = 2θ exactly (proof.md Step 12); near θ=0, ang_P ≈ θ√(2d/(d-1)) < 2θ for every d≥3
(Step 13, exact rational check). So the embedding gives a bound in the wrong direction.

**What would be needed to close the gap.** Either (a) a genuinely rank/PSD-aware inequality
stronger than one aggregate moment (e.g. using more of the spectrum of G, or a semidefinite
duality / Lagrangian certificate tailored to the concentrated extremizer), or (b) a different
embedding or comparison function whose combinatorial (hyperplane-type) bound is dimension-
independent tight, matching ang_P = 2θ not just at d=2 but with a valid ≥ inequality for all d.
Neither was found within the time box; no third approach was attempted.

**Everything else in proof.md (Steps 1-3, 9-11, and all of Part IV, Steps 16-22) stands on its
own and is not affected by this gap** — it is either a proved general-d lemma or the complete,
unconditional d=2 proof.
