# Submission — Problem A, Cell C5: "d+2 Lines in R^d" (8 pts)

## Verdict: PARTIAL — solved for d=2, open for d≥3

| | |
|---|---|
| **Cell status** | PARTIAL |
| **What's solved** | d=2 (N=4 lines in R²): S ≤ 2π, exact, all configurations — **gated VALID, board status PROVED** |
| **What's open** | d≥3 (general d): not established |
| **Confidence, d=2** | Maximal available in this run. Two structurally different proofs, agreeing exactly. **Gate: VALID** — both independent clean-room referees (A-C5-D2-002, A-C5-D2-003) returned **ACCEPT**, complete 15/15 checklists, zero FAILs, statement match confirmed word-for-word by the head. Combined independent numerical search across all verification rounds: ~350,000+ trials (exact-arithmetic grids + mpmath 50-digit random/perturbation search), zero violations found. See `run/A/C5-D2/gate/gate_report.md`. |
| **Confidence, d≥3** | Genuinely open, not "probably true but untried." One entire proof strategy is **proved incapable** of ever closing it, not merely unsuccessful. |

---

## 1. Exact statement being judged

> For every integer d≥2, any N=d+2 lines ℓ_1,...,ℓ_N through the origin of R^d (repetitions
> allowed) satisfy
>
> &nbsp;&nbsp;&nbsp;&nbsp;S := Σ_{i<j} θ(ℓ_i,ℓ_j) ≤ (C(d+2,2) − 2)·π/2
>
> where θ(ℓ,ℓ') = arccos|⟨x,x'⟩| ∈ [0,π/2] for unit vectors x,x' spanning ℓ,ℓ'.

Conjectured equality: the d coordinate axes, two of them repeated.

---

## 2. What is actually established, and how sure we are of it

### 2a. The reduction (used by every attempt below — this part is elementary and load-bearing everywhere)

arccos(x)+arcsin(x)=π/2 on [-1,1] (standard calculus identity) turns the target into an exactly
equivalent statement about T := Σ_{i<j}arcsin|⟨x_i,x_j⟩|:

&nbsp;&nbsp;&nbsp;&nbsp;**S ≤ (C(N,2)−2)·π/2 ⟺ T ≥ π.**

This step is pure algebra. Nobody disputes it; every prover and referee re-derived it independently.

### 2b. d=2, N=4: PROVED — S ≤ 2π

**The argument** (full text: `run/tasks/A-C5-D2-001/out/proof.md`): represent each line by an
angle mod π on a circle of circumference π; sort 4 lines into 4 cyclic gaps g_1..g_4 ≥ 0 summing
to π; S becomes an explicit function of the gaps; a two-case split (at most one gap can exceed
π/2, since two such would sum past π) bounds that function by 2π in both cases.

**Why we trust it — the actual verification chain, not just an assertion:**

1. **Two independent blind provers** (A-C5-001, A-C5-002), working with no knowledge of each
   other, no literature, no hints — each derived a complete d=2 proof. They used **different
   methods** (A-C5-001: direct cyclic-gap case analysis. A-C5-002: a doubling map to the circle
   plus a random-separating-line probability argument). Independent agreement between different
   methods is much stronger evidence than one proof checked twice.
2. **Two clean-room referees read the full A-C5-001 submission** (A-C5-004, A-C5-005) — neither
   was told who wrote it or how confident the author was. Both ran the full 7-step protocol
   (checklist, line-by-line re-derivation, numerical sanity, equality-case test, own
   counterexample search). Both independently flagged the d=2 argument itself (their "Steps 1-2,
   5") as **fully correct, no unjustified steps, no hidden symmetry claims** — their formal
   verdict on the *whole* submission was MAJOR only because that submission (correctly) also
   admits it doesn't cover d≥3; that is not a flaw in the d=2 argument, it's an honest scope gap
   elsewhere in the same document.
3. **Because (2)'s MAJOR verdict was about scope, not the d=2 math**, we carved the d=2 claim
   into its own correctly-scoped lemma (cell `A-C5-D2`, statement: exactly "S≤2π for 4 lines in
   R²," nothing about d≥3) and sent it to **two fresh referees who had never seen the original
   submission or each other's work**:
   - **A-C5-D2-003: ACCEPT.** All 15 checklist items PASS or N/A, zero FAIL. Own independent
     numerical audit: 20000 random configurations (including forced degenerate/repeated lines),
     20000×2 local-perturbation trials, a 12341-point deterministic grid, and a direct
     θ-sum-vs-gap-formula cross-check with **zero mismatches**.
   - **A-C5-D2-002: ACCEPT.** All 15 checklist items PASS or N/A, zero FAIL. Own independent
     numerical audit at 50-digit precision: 200,000 random trials (including forced 3+1/2+2/
     all-coincident degenerate patterns), a 5,832-point deterministic grid, and 40,000
     perturbation samples around both equality points. Zero violations.
   - **Gate decision: VALID.** Two independent ACCEPTs on the same proof version, complete
     checklists, statement checked word-for-word by the head against the exact cell text.
     `run/A/C5-D2/gate/gate_report.md`. **The d=2 lemma is now board-certified PROVED** — not a
     provisional or "probably fine" label, but this run's actual verification gate having run to
     completion and passed.

**Equality cases**, both exact: two doubled orthogonal axes (g=(0,π/2,0,π/2)), and four
evenly-spaced lines (g=(π/4,π/4,π/4,π/4)) — both give S=2π on the nose, cross-checked by three
independent pieces of code (exact-`Fraction` grids in two different task folders, plus an
mpmath 50-digit referee script), not floating point.

### 2c. d≥3: NOT solved — and here is exactly why, not just "we ran out of time"

Three independent attempts, each a different mathematical idea, each hitting a **specific,
named, checkable obstruction** rather than vaguely "not finding it":

| Attempt | Idea | Where it lands | Why it stops |
|---|---|---|---|
| **A. Second-moment / Cauchy–Schwarz** | Bound Σa_ij² from the Gram matrix's rank≤d, convert via a pointwise inequality arcsin(x)≥Bx² | T ≥ B·(d+2)/d | **Proved impossible to repair**: the best possible B is capped at ≈1.380 < π for *any* choice, so as d→∞ this whole family caps out below π. Root cause identified: this method is tuned to a "spread out" configuration, but the true extremizer is sparse (mass on exactly 2 entries), which second moments can't see. |
| **B. Veronese/projector embedding** | Map lines to a sphere in Sym₀(R^d); at d=2 this exactly doubles angles, which is why 2b's second proof works | Exact identity relating the embedded angle to θ | **Provably reverses for d≥3**: checked exactly at θ=π/2, d=3, the needed inequality goes the wrong way (2π/3 < π). The technique that solves d=2 cannot be transplanted. |
| **C. Kernel recurrence (new)** | Use corank(G)≥2 directly: an exact linear recurrence among the two kernel vectors | T≥1 for all d (proved); a weighted refinement exactly tight at the true extremal (proved) | **Doesn't convert to the unweighted bound.** This is the most promising lead (it's the only one exact at the true minimizer), but going from the weighted to the unweighted statement needs an ingredient (likely a Schur-complement or variational argument using the *full* PSD structure of G, not just its kernel) that was not developed. |

None of these is "we didn't think of it" — each is a concrete, checkable mathematical statement
of *why* it stops, which is itself part of what's being handed in (it tells the next attempt what
not to repeat).

**One-attempt literature check** (not exhaustive; primary sources were blocked by this
environment's network policy and could not be fetched to confirm): the general conjecture is
reported as open for d≥2 in three post-2015 papers found by title/abstract search; Fejes Tóth's
own 1959 result is reported to cover d=3, N≤6 (which would include this cell's d=3 instance as a
byproduct), but the actual argument could not be retrieved or checked here. Treated as
"unconfirmed," not used as a substitute for a proof.

---

## 3. What this submission is asking you to believe, precisely

- **Do** treat "S≤2π for d=2, N=4" as PROVED, board-certified: independently re-derived twice by
  different methods, and gated VALID by two independent referees who tried to break it and could
  not, across roughly 350,000 numerical trials combined (two prior full-submission reads plus the
  two gating referees).
- **Do not** treat the general d≥2 statement as proved. It isn't. The gap is real, specific, and
  documented above, not a placeholder for "probably fine."
- **Do** treat Theorem A (T≥1, all d) and its tight-at-equality weighted refinement as correct
  and potentially useful to a future attempt — they are proved, just not strong enough.
- **Do** treat the second-moment impossibility result (§2c, row A) as itself a real (if modest)
  contribution: it forecloses a whole family of arguments for anyone attempting this cell next.

## 4. Artefact index

- Full d=2 proof: `run/tasks/A-C5-D2-001/out/proof.md` (extracted, self-contained) /
  `run/tasks/A-C5-001/out/proof.md` (original, with the d≥3 attempt attached) /
  `run/tasks/A-C5-002/out/proof.md` (second, independent derivation)
- Referee verdicts: `run/tasks/A-C5-004/out/verdict.md`, `A-C5-005/out/verdict.md` (full-cell,
  MAJOR on scope only), `A-C5-D2-003/out/verdict.md` (lemma-scoped, ACCEPT)
- d≥3 partial results and obstructions, full detail: `run/A/C5/final_report.md`
- Board / ledger: `run/board.md`, `run/A/C5/gate/`, `run/A/C5-D2/gate/`
