# Final report: A-C5 — "d+2 Lines in R^d" (8 pts)

## Statement (exact target)

For every integer d≥2, any N=d+2 lines ℓ_1,...,ℓ_N through the origin of R^d (repetitions
allowed) satisfy

    S := Σ_{i<j} θ(ℓ_i,ℓ_j) ≤ (C(d+2,2) − 2)·π/2

where θ(ℓ,ℓ') = arccos|⟨x,x'⟩| ∈ [0,π/2] for unit vectors x,x' spanning ℓ,ℓ'. Equality is
conjectured at the d coordinate axes with two of them repeated.
(Source: `run/A/C5/target.md`, `.claude/skills/problem-angles-lines/SKILL.md` §1, §4.)

## Status: **PARTIAL**

- **d=2 (N=4 lines in R^2): PROVED**, by two independent elementary arguments.
- **d≥3: OPEN.** Not established here. Three independent attempts each hit a different, explicitly
  identified obstruction (below), and a rigorous impossibility result was proved for one entire
  family of arguments (§3 below). Web search (one attempt) found the general conjecture stated as
  open in the literature for d≥2, but could not fetch primary sources to check this exact
  sub-case, because arxiv.org, link.springer.com, ams.org, semanticscholar.org, researchgate.net
  and the Szeged repository were all blocked by this environment's network egress. This is
  reported as "not found in the sources reachable here", not as "not in the literature."

## What is established

### 1. The reduction (used by all three attempts)

With G_ij = ⟨x_i,x_j⟩ the Gram matrix of unit representatives (G symmetric PSD, G_ii=1,
rank(G)≤d), and T := Σ_{i<j} arcsin|G_ij|, the identity arccos(x)+arcsin(x)=π/2 gives
S = C(N,2)·π/2 − T, so the target is **exactly equivalent to T ≥ π.**
(`run/tasks/A-C5-001/out/proof.md` step R1; `run/tasks/A-C5-002/out/proof.md` step R1;
independently rediscovered in `run/tasks/A-C5-003/` (the fast general-purpose attempt), §1.)

### 2. d=2, N=4: complete proof (two independent derivations)

- **Derivation 1** (`run/tasks/A-C5-001/out/proof.md`, step R4): represent each of the 4 lines by
  an angle mod π; the 4 angles split the circle of circumference π into 4 gaps g_1..g_4≥0 summing
  to π. S becomes an explicit function of the gaps, F(g) = (sum of circular distances of the 4
  gap-pairs and 2 "adjacent-pair" combinations). A two-case split (at most one gap can exceed π/2)
  shows F ≤ 2π always, matching the target (C(4,2)−2)π/2 = 2π exactly, with equality at the
  balanced/orthogonal configurations. Exact-rational exhaustive grid cross-check:
  `run/tasks/A-C5-001/out/code/check_d2.py` (39711 points, 0.85s, COMPLETED; not load-bearing).
- **Derivation 2** (`run/tasks/A-C5-002/out/proof.md`, steps R5-R8): the doubling map
  ℓ(angle α) ↦ y=(cos2α,sin2α)∈S^1 satisfies the exact identity ang(y,y')=2θ(ℓ,ℓ') for every α
  (all cases checked); a random-line-separation identity (probability a random line separates two
  points at circular distance β is β/π, proved from scratch) plus the elementary integer bound
  a(N−a) ≤ ⌊N/2⌋⌈N/2⌉ combine to give Σang(y_i,y_j) ≤ 4π exactly, i.e. S ≤ 2π. Exact-arithmetic
  cross-checks: `run/tasks/A-C5-002/out/code/approach_d2_check.py`.

Two structurally different proofs agreeing exactly on the d=2 case is strong (though not gate-
level — see Limitations) evidence this half of the ladder is solid.

### 3. d≥3: three attempts, three named obstructions, plus one impossibility proof

- **Attempt A — second-moment / Cauchy–Schwarz + pointwise minorant** (all three tasks tried a
  version of this). Σ_{i<j}G_ij² ≥ N(N−d)/(2d) = (d+2)/d (Cauchy–Schwarz on the ≤d nonzero
  eigenvalues of the rank-≤d PSD Gram matrix), combined with any pointwise bound arcsin(x)≥Bx² on
  [0,1]. **Rigorous impossibility result** (`run/tasks/A-C5-003` §3, Lemma 2): the best possible
  constant is B* = min_{x∈(0,1]} arcsin(x)/x² ≈ 1.380 < π. So T ≥ B·(d+2)/d → B ≤ 1.380 as d→∞,
  for *any* choice of B in this family — this whole approach is structurally capped below π for
  large d, not merely under-optimized. Root cause identified: the moment bound is tuned to a
  "spread-out" configuration, but the true extremizer is sparse (mass concentrated on exactly 2
  off-diagonal entries at exactly ±1), which second moments alone cannot see.

- **Attempt B — Veronese/projector embedding.** x ↦ P_x = xx^T − (1/d)I embeds lines into a
  sphere in Sym_0(R^d) with exact identity cos(ang_P(x,x')) = (d·cos²θ−1)/(d−1). At d=2 this
  gives ang_P=2θ exactly, which is exactly Derivation 2's doubling map, and is what makes the d=2
  proof work. For d≥3 the needed inequality ang_P ≥ 2θ **reverses**: checked exactly at θ=π/2,
  d=3: ang_P = 2π/3 < π = 2θ. So the angle-doubling technique that closes d=2 cannot be
  transplanted to higher d as-is. (`run/tasks/A-C5-002/out/proof.md` R4; confirmed independently
  in `A-C5-003` §3 context.)

- **Attempt C — kernel-recurrence (new, from the fast general-purpose attempt,
  `run/tasks/A-C5-003`).** Uses corank(G) ≥ N−d = 2 directly (Lemma 1) rather than trace
  identities: with u,v an orthonormal basis of ker(G), z=u+iv, r_i=|z_i|, Σr_i²=2, and the exact
  recurrence z_i = −Σ_{j≠i}G_ij z_j (from Gu=Gv=0). This proves, unconditionally for every d≥2:
    **Theorem A: T ≥ 1.**
    **Theorem A′ (sharper, weighted): Σ_{i<j} r_ir_j sin(arcsin|G_ij|)... = Σ_{i<j} r_ir_j|G_ij| ≥ 1**,
    and this weighted version is an **exact equality at the conjectured extremal** (unlike every
    other bound above, which has slack there). Neither Theorem A nor A′ reaches T≥π; converting
    the tight weighted inequality into the unweighted one is exactly the open step. Several
    natural next moves (Cauchy–Schwarz between the two sums; uniform r_ir_j≤1; a second
    edge-disjoint copy of the same argument) were tried and shown not to close the gap in the
    time available.

## Exact remaining gap

A rigorous argument, for every d≥3, closing the distance between the proved partial bound
(T ≥ 1, or the tight-at-equality T-weighted version ≥ 1) and the required T ≥ π. The report's own
assessment: the likely missing ingredient is a use of the *full* PSD structure of G (e.g. a Schur
complement or a variational/KKT argument at critical configurations), not just its kernel — this
was not developed to completion.

## Numerical sanity (not proof, illustrative only)

Stochastic local search over unit vectors in R^d for (d,N)=(3,5) and (4,6) (A-C4's two concrete
instances, which are exactly A-C5 at d=3,4) found best T ≈ 3.14165 and 3.14176 respectively,
approaching π ≈ 3.14159 from above with no counterexample found — consistent with, but not a
verification of, the conjecture. (`A-C5-003` §5; heuristic only, no exhaustiveness guarantee.)

## Limitations of this report

This is a head-authored summary, not a gate-cleared result: **no referee has verified either d=2
proof, no cross-checker has re-run the code, and no gate report exists.** Under this run's own
verification rules, nothing here may be labelled PROVED on the board without two independent
clean-room referees (VERIFY/GATE mode) accepting it and a gate report. This run was explicitly
run cost-capped and time-capped at the user's request (blind provers only, one fast
general-purpose attempt, no Phase 2S/2A/2B/2C, no Phase 2 verification referees, no auditor) —
so what follows is the strongest honest claim consistent with skipping that verification, not a
claim that verification has happened:

- d=2 (N=4): two independent, mutually-consistent, complete elementary proofs exist and are
  believed correct, but are **unverified by independent referees**.
- d≥3: **open**, with two new proved-but-insufficient partial results (Theorem A, A′) and a
  rigorous impossibility result ruling out an entire proof strategy.

## Cell status: PARTIAL (established: d=2; remaining gap: d≥3, general)
