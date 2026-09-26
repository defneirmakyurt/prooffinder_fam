# Triage: A-C3-004 (cell 3, d+1 lines in R^d). REGIME: BLIND, PHASE 2A

RAN: none. I computed nothing. The hand checks below are marked as hand checks.

## Reading of the brief

- TARGET (used exactly as given): for every integer d >= 1 and all lines l_1, ..., l_{d+1} through the origin of R^d (repetitions allowed), S = sum_{i<j} theta(l_i, l_j) <= (C(d+1,2) - 1) * pi/2, where theta = arccos|<x, x'>| lies in [0, pi/2].
- Obstacles: there are none (the inbox has no obstacles/ folder), so every rating comes from the statement alone.
- The brief marks this as a T1 cell. It asks for EXACTLY two solver branches (the two best) and no verifier-only branches. I rated every branch honestly and then applied that cap.
- The brief mentions "section 11" for selected_branches.txt. I used the format from my core instructions: tab-separated lines of branch and tag.

## Structural facts from the statement (not a solution)

- Equivalent form: C(d+1,2)*pi/2 - S = Phi := sum_{i<j} arcsin|<x_i, x_j>|. The target is exactly Phi >= pi/2.
- The d+1 unit vectors in R^d are linearly dependent. So their Gram matrix G (PSD, unit diagonal, size d+1) has rank <= d and a nonzero kernel vector. This is the only hypothesis that forces non-orthogonality.
- Changing x_i to -x_i leaves every line and every theta unchanged. This sign symmetry is free.
- Edge case d = 1: both lines coincide, S = 0 = bound.
- Hand check (not a computation): equality is not isolated. At d = 2, lines at directions 0, alpha, pi/2 give angles alpha, pi/2 - alpha, pi/2, so S = pi for every alpha in [0, pi/2]. Three lines 60 degrees apart also give S = pi. Any proof must be tight on a positive-dimensional equality set.
- arcsin is convex on [0,1] with arcsin(0) = 0 and arcsin(1) = pi/2. So arcsin t <= (pi/2) t, and arcsin(a) + arcsin(b) <= arcsin(a+b) when a + b <= 1. A linear lower bound on the |g_ij| therefore does not give Phi >= pi/2. This is a hazard for any route, not a route.

## Branch ratings

### ALGEBRAIC: HIGH
- **REASON:** The whole hypothesis is algebraic: d+1 vectors in a d-dimensional space. It lives in the Gram matrix G = (<x_i, x_j>), which is PSD with unit diagonal and rank at most d. So det G = 0, the least eigenvalue is 0, and there is a kernel vector c with sum_i c_i x_i = 0. The branch's tools (kernel relations, eigenvalue and norm inequalities for G - I, rank arguments, reduction to a minimal dependent subfamily, sign-flip symmetry to normalise the signs of c or of the g_ij) act directly on the object that forces the off-diagonal entries of G to be large. That is exactly the quantity inside arcsin in Phi.
- **ENTRY POINT:** Fix a nonzero c in ker G, i.e. sum_i c_i x_i = 0. Use x_i -> -x_i to make every c_i >= 0, and record the row identities sum_j c_j g_ij = 0 for each i.
- **RISK:** The branch naturally produces linear or quadratic lower bounds on the |g_ij| (row sums >= 1, Frobenius or spectral bounds on G - I). Because arcsin is convex, these give Phi >= (something) < pi/2 rather than pi/2. Early warning sign: the argument needs arcsin t >= (pi/2) t, or arcsin a + arcsin b >= arcsin(a+b), both false. A second warning sign is a bound that is strict on the d = 2 equality family above.

### ANALYSIS: HIGH
- **REASON:** The quantity to bound is a sum of a specific nonlinear function (arcsin of |g_ij|, or equivalently arccos) over the pairs. That function has convexity/concavity structure, and the absolute value makes it non-smooth at g_ij = 0 and g_ij = +/-1. The problem is to minimise Phi over the compact set of (d+1)-tuples of unit vectors in R^d. The branch's tools act on exactly that: existence of a minimiser, first-order (Lagrange) conditions on the sphere product, behaviour at degenerate configurations (coincident or orthogonal pairs), smoothing and replacement moves that do not increase Phi, and tangent-line or angle-level estimates. The angle theta is itself a metric on lines, and the branch can work with angles directly instead of inner products. That is one way around the convexity hazard that affects ALGEBRAIC.
- **ENTRY POINT:** Rewrite the target as Phi = sum_{i<j} arcsin|<x_i, x_j>| >= pi/2. Take a minimiser of Phi over (S^{d-1})^{d+1}, which exists by compactness, and list which pairs have |g_ij| in {0, 1}, where Phi is not differentiable.
- **RISK:** The equality set has positive dimension (the d = 2 family above, plus copies in higher d obtained by adding orthogonal axes). So second-order conditions at a minimiser meet flat directions, and the first-order analysis splits into many non-smooth cases. Early warning signs: a degenerate Hessian, a case tree over which g_ij vanish that grows with d, or a local argument that shows only local minimality with no reduction that works for every d.

### DISCRETE: LOW
- **REASON:** There is real combinatorial structure. The pairs form K_{d+1}. The pairs with g_ij != 0 form a "non-orthogonality graph". Restricting to a minimal linearly dependent subfamily (a circuit of size m spanning R^{m-1}) loses nothing, because every arcsin term is >= 0. The non-orthogonality graph of a circuit must be connected, which gives induction on d or m a foothold. (The statement's cell 2 is the path-graph case of this viewpoint. I note this but did not use it for the rating.) Still, discrete tools reach only reductions. After reducing to a connected circuit, the remaining inequality is continuous: arcsin of inner products under a linear dependence. Double counting, pigeonhole or Turán-type arguments do not act on that quantity by themselves. The solver would have to import the ALGEBRAIC or ANALYSIS estimate for the core step.
- **ENTRY POINT:** Replace the family by a minimal linearly dependent subfamily of size m <= d+1, spanning R^{m-1}. Show that the target reduces to that subfamily and that its non-orthogonality graph is connected.
- **RISK:** Induction on d via projection or deletion does not control angles, because projecting changes the theta's non-monotonically. Early warning sign: the inductive step needs a monotonicity of theta under projection, or a reduction from a connected graph to a spanning tree, that is not actually justified.

### TOPOLOGICAL: LOW
- **REASON:** The configuration space (RP^{d-1})^{d+1} is compact and S is continuous, so a maximiser exists. The equality set is connected at least in part (the d = 2 family), which makes a deformation-to-a-canonical-maximiser idea conceivable. But the target is a single inequality with no degree, fixed-point or connectivity content. Compactness is just a first step that ANALYSIS already takes.
- **ENTRY POINT:** Use compactness to fix a maximiser of S and try to deform it continuously within the maximiser set to the "coordinate axes with one axis repeated" configuration.
- **RISK:** The deformation argument turns into the first- and second-order analysis of ANALYSIS without adding anything. Early warning sign: every step of the deformation needs a local inequality proved by calculus.

### NUMBER-THEORY: NONE
- **REASON:** No integrality, divisibility or rounding enters. N = d+1 makes the floor/ceiling split of the general conjecture trivial (one axis repeated). The constant C(d+1,2) - 1 is a fixed pair count. The quantities being bounded are real angles.
- **ENTRY POINT:** none nameable.
- **RISK:** n/a.

## Selection

- Solvers: ALGEBRAIC (HIGH) and ANALYSIS (HIGH). These are the two best, and there are exactly two, as the T1 instruction requires.
- Verifier-only: none, as the T1 instruction requires.

## Eliminations, in re-admission order

1. DISCRETE (LOW). Dropped because its tools yield only a reduction to a connected circuit, and the core continuous inequality would still need ALGEBRAIC or ANALYSIS methods. It has the best entry point among the dropped branches (circuit reduction plus connectivity of the non-orthogonality graph), so it is re-admitted first. It was the closest call. The T1 cap of two solvers would have excluded it even at MEDIUM.
2. TOPOLOGICAL (LOW). Dropped because compactness is already the first step of ANALYSIS, and there is no degree or connectivity content in a single inequality. Its entry point (deforming a maximiser along the equality set) is weaker.
3. NUMBER-THEORY (NONE). Dropped because there is no integrality structure and no entry point.

## Known gaps

- I recognise the conjecture named in the statement and know that published work exists on small-N cases. I did not use it for any rating and cite nothing.
- There were no obstacles, so the ratings rest on the statement alone.
