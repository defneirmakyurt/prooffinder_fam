# Submission: Problem A, Cell C5 — "d+2 Lines in R^d" (8 pts)

## Status: PARTIAL

**Solved:** d=2 (N=4 lines in R^2).
**Not solved:** d≥3 (general case remains open).

## Statement

For every integer d≥2, any N=d+2 lines ℓ_1,...,ℓ_N through the origin of R^d (repetitions
allowed) satisfy S := Σ_{i<j} θ(ℓ_i,ℓ_j) ≤ (C(d+2,2) − 2)·π/2, θ(ℓ,ℓ')=arccos|⟨x,x'⟩|∈[0,π/2].

## Proved: d = 2, N = 4 — S ≤ 2π

**Reduction.** With a_ij=⟨x_i,x_j⟩, the identity arccos(x)+arcsin(x)=π/2 gives
S = 6·(π/2) − T where T=Σ_{i<j}arcsin|a_ij|; the target S≤2π is exactly equivalent to T≥π.

**Proof of T≥π for N=4, d=2.** Represent each line by an angle mod π on a circle of
circumference π. Sort the 4 angles cyclically into 4 nonnegative gaps g_1,g_2,g_3,g_4 summing to
π. With h(x)=min(x,π−x), S = h(g_1)+h(g_2)+h(g_3)+h(g_4)+h(g_1+g_2)+h(g_2+g_3). At most one g_i
exceeds π/2 (else two would sum to more than π). Case A (all g_i≤π/2): the four h(g_i) sum to
exactly π, and each of the two "opposite" terms is ≤π/2, giving S≤2π. Case B (exactly one
g_k>π/2): the four h(g_i) sum to 2π−2g_k, and the two opposite terms sum to ≤π, giving
S≤3π−2g_k<2π. Either way S≤2π, with equality at two doubled orthogonal axes (g=(0,π/2,0,π/2))
and at four evenly-spaced lines (g=(π/4,π/4,π/4,π/4)). Both handle all degenerate/repeated
lines automatically (θ=0 pairs are legal, covered as g_i=0 in Case A).

Full detailed proof: `run/tasks/A-C5-D2-001/out/proof.md`. Independently re-derived by a second,
structurally different method (doubling map ℓ↦(cos2α,sin2α) + random-separating-line probability
argument): `run/tasks/A-C5-002/out/proof.md` steps R5–R8.

**Computation used:** `run/tasks/A-C5-D2-001/out/code/check_d2.py` — exact-`Fraction` exhaustive
grid over 4-part compositions of π (39711 points), COMPLETED in 0.85s, sanity-check only (not
load-bearing; the proof above is exact and unconditional).

**Verification in this run:** two independent clean-room referees (`run/tasks/A-C5-004`,
`run/tasks/A-C5-005`) each ran the full 7-step protocol against A-C5-001's complete submission
and confirmed this d=2 argument is correct, gap-free, with matching equality cases, and each ran
their own independent counterexample search (a separate exact-arithmetic grid and floating-point
random/perturbation trials) finding no violation. (Their formal verdict on that task was MAJOR
only because A-C5-001 also attempts, and does not close, the general d≥3 case — not because of
any fault in the d=2 argument itself.) A second pair of referees (`A-C5-D2-002`, `A-C5-D2-003`)
was dispatched against this exact, correctly-scoped d=2-only statement to produce a clean gate
verdict; that gate had not returned by the time this submission was written — see
`run/A/C5/gate/` for the outcome if it landed after this file was generated.

## Not solved: d ≥ 3

Not established. Two new partial results were proved (both fall short of what's needed):
- **T ≥ 1** for every d≥2 (a dimension-free bound via the corank-2 kernel of the Gram matrix).
- A weighted refinement, **exactly tight at the conjectured extremal**, that still doesn't convert
  to the required unweighted bound T≥π.

A separate rigorous result shows the natural "second-moment" proof strategy is **structurally
incapable** of reaching T≥π for any d≥3 (capped at a constant ≈1.380<π as d→∞), and a second
strategy (Veronese-embedding angle doubling, the technique that closes d=2) **provably reverses**
for d≥3. Full writeup and exact obstructions: `run/A/C5/final_report.md`.

## Hand-in per official format

"Say clearly which cells you consider solved and which are partial": **Cell A-C5 is PARTIAL.**
d=2 is solved (proof above); d≥3 is not, with the exact remaining gap stated in
`run/A/C5/final_report.md`.
