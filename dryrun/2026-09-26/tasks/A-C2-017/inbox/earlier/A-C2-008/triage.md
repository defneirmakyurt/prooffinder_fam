# Triage: A-C2-008 (Cell 2, "An Orthogonality Lemma")

REGIME: BLIND. RAN: none (no code executed, nothing computed).

## Reading of the target

For every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i-j| >= 2,
prove sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m-2) pi/2, with theta(x,y) = arccos|<x,y>| in [0, pi/2].
Only consecutive pairs are summed. Write c_i = <x_i, x_{i+1}>. An equivalent form (pure rewriting, not a solution
step): sum_{i=1}^{m-1} (pi/2 - theta_i) >= pi/2, i.e. sum_i arcsin|c_i| >= pi/2. Edge case m = 2: two unit
vectors in R^1, so |c_1| = 1 and the claim is theta = 0 <= 0.

Key structural facts used for rating (read off the statement, not a solution):
- The Gram matrix G = (<x_i, x_j>) is m x m, tridiagonal with unit diagonal and off-diagonal entries c_i,
  positive semidefinite, and of rank <= m-1 because the vectors live in R^(m-1). So det G = 0 while G >= 0.
- The support pattern of G is a path graph; a zero c_i splits the chain into two mutually orthogonal sub-chains.
- The quantities to bound are sums of arccos/arcsin of the |c_i|, i.e. transcendental functions of the Gram entries.

## Obstacles

obstacles/A-C2-001/stuck.md and obstacles/A-C2-002/stuck.md both contain only "none". No earlier attempt recorded
a stall, so all ratings are from the statement alone.

## Branch ratings

### ALGEBRAIC — HIGH
REASON: The hypothesis is entirely a statement about the Gram matrix: a tridiagonal PSD matrix with unit diagonal
that must be singular (rank <= m-1 in an m x m matrix). Tridiagonal determinants obey a three-term (continuant)
recurrence D_k = D_{k-1} - c_{k-1}^2 D_{k-2} on the leading principal minors, and PSD forces all these minors to be
>= 0 while the full one vanishes. That converts the geometric hypothesis into a finite system of polynomial
conditions on c_1^2, ..., c_{m-1}^2, which is exactly the object on which the angle sum is evaluated. Signs of c_i
can be removed by flipping x_i (a symmetry that leaves the hypothesis and the theta's invariant), so one may assume
c_i >= 0.
ENTRY POINT: Write G as the tridiagonal matrix with entries c_i, set up the leading-minor recurrence D_k, and record
the constraints D_k >= 0 (k < m), D_m = 0 (after first reducing to the case where all c_i are nonzero, or handling
zeros separately).
RISK: The determinant conditions are polynomial in the c_i while the target is a sum of arccos's; the solver may
get a clean algebraic constraint but no way to push it through the transcendental functions. Warning sign: the
solver has the recurrence but keeps trying to compare polynomials of c_i directly with pi/2, or needs a
trigonometric parametrisation it cannot close without a further inequality.

### ANALYSIS — HIGH
REASON: The target is a sum of the functions arccos|c_i| (equivalently arcsin|c_i|) under a constraint, so the
decisive step is an inequality on transcendental functions: trigonometric substitution c_i = cos(theta_i) or
sin(phi_i), angle-addition/induction on the partial sums, concavity/convexity of arcsin, tangent-line bounds, or a
Lagrange/extremal argument on the compact constraint set. The angle between lines is also a metric on lines
(triangle inequality for theta), which gives an analytic handle on how angles accumulate along the chain.
Degenerate configurations (some c_i = 0, some |c_i| = 1) are exactly the equality-type cases and need the
"behaviour near degenerate configurations" tools of this branch.
ENTRY POINT: Rewrite the goal as sum_i arcsin|c_i| >= pi/2 and parametrise each c_i by an angle, then look for an
inductive quantity along the chain (e.g. an angle attached to the first k vectors) that must reach pi/2 by the time
the chain is forced to be linearly dependent.
RISK: A multiplier or convexity argument may prove the bound only at interior critical points and miss boundary
cases where some c_i = 0 or the chain splits; or the solver may produce a bound true only for small m. Warning
sign: case analysis grows with m, or the argument silently assumes all c_i nonzero.

### DISCRETE — MEDIUM
REASON: The orthogonality pattern is a path graph on {1, ..., m}, and the dimension bound m-1 is a counting
condition. If some c_i = 0, the chain splits into two sub-chains lying in orthogonal subspaces whose dimensions add
to at most m-1, so by pigeonhole one sub-chain of length k lives in dimension <= k-1 and the statement for smaller
m applies; this is a natural strong induction on m. What remains (all c_i nonzero) is not combinatorial, so this
branch supplies the scaffolding and reduction rather than the core inequality.
ENTRY POINT: Set up strong induction on m; handle the case "some c_i = 0" by the dimension-counting split into two
orthogonal sub-chains and verify the resulting sum bound, isolating the all-nonzero case.
RISK: The all-nonzero case is the heart of the problem and has no discrete handle; the solver may stall there.
Warning sign: the solver reduces to "all c_i nonzero" and then has no tool beyond restating it.

### TOPOLOGICAL — LOW
REASON: The configuration space (unit vectors with the prescribed orthogonalities in R^(m-1)) is compact and the
angle sum is continuous, so a maximiser exists; the angle function is a metric on projective space. Beyond
existence of an extremiser and perhaps a perturbation/connectedness argument, the branch's tools do not act on the
core quantitative inequality.
ENTRY POINT: Establish compactness of the constraint set and existence of a maximising chain, then study whether a
maximiser can be perturbed within the constraint set to increase the sum.
RISK: Reduces to a variational (analysis) problem without adding leverage. Warning sign: after existence, all
further work is calculus.

### NUMBER-THEORY — NONE
REASON: There are no counts to round, no divisibility, parity or integrality in the statement; the only integer is
m, and the bound (m-2) pi/2 is linear in m with no arithmetic content.
ENTRY POINT: none nameable.
RISK: n/a.

## Selection

Head budget rule (brief): exactly two branches, both solver, no verifier-only.

Selected (solver): ALGEBRAIC (HIGH), ANALYSIS (HIGH).

## Eliminations (re-admission order)

1. DISCRETE (MEDIUM) — dropped only by the two-branch budget cap; it supplies the induction/splitting scaffold but
   not the core all-nonzero inequality. Re-admit first.
2. TOPOLOGICAL (LOW) — gives existence of a maximiser only; no leverage on the quantitative bound.
3. NUMBER-THEORY (NONE) — no arithmetic structure in the cell.

No verifier-only tags (excluded by the brief's budget).

## Known gaps / notes

- I have a vague recognition that a lemma of this shape appears in the literature on this conjecture; per BLIND
  regime it played no role in the ratings, and I cite nothing.
- Ratings are from the statement alone; both obstacle files are empty ("none").
