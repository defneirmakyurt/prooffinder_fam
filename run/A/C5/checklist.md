# Checklist: A-C5

## Part G (generic; shared with every agent, blind ones included)
- G1 The statement proved is exactly the cell's: no extra hypotheses, no weaker inequality, the full parameter range.
- G2 Every step justified. No unexplained "clearly", "similarly", "routine", "obviously", "by symmetry".
- G3 Base cases, edge and degenerate cases, exceptional parameter values handled.
- G4 Every claimed invariant is preserved; every claimed decrease is strict where strictness is needed.
- G5 Every construction works for every claimed parameter value, not only the tested ones.
- G6 No circularity, and no citation that is the statement itself.
- G7 Any computation is exact or interval-based, code included, under 10 minutes; a finite check proves
     nothing beyond its range; a computer-assisted step has a written reduction to exactly the set searched.
- G8 Cited results separated from new work, with precise references.
- G9 The proof says what is established and what is not.

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement and the quantities to be bounded (from target.md): for every d≥2 and every
     N=d+2 lines ℓ_1,...,ℓ_{d+2} in R^d (repetitions allowed), S = Σ_{i<j} θ(ℓ_i,ℓ_j) satisfies
     S ≤ (C(d+2,2)-2)·π/2, θ = arccos|⟨x,x'⟩| ∈ [0,π/2] for unit spanning vectors. All of d≥2 is
     required; a proof only for small d, or only for A-C4's two instances (d=3,4), is PARTIAL.
- S2 Equality / extremal configuration (problem skill §1, Setting's conjectured optimum, N=d+k with
     k=2 here): the d coordinate axes, each used once, with two of them repeated once more (i.e.
     multiplicities (2,2,1,1,...,1) summing to d+2). A proof must be tight exactly there and must
     not exclude it as "not achievable" (repetitions, i.e. θ=0 pairs, are explicitly legal — problem
     skill §8 pitfall). Source: problem-angles-lines SKILL.md §1, §4, §11.
- S3 Cases the proof must cover: every integer d≥2 (not just d=3,4); repetitions/coincident lines
     (θ=0) must be legal configurations, not excluded as degenerate; the lines need not be linearly
     independent (N=d+2 > d, so they cannot be). Source: SKILL.md §4, §8.
- S4 Known traps (problem skill §8, labelled as pitfalls, not facts):
     (a) "Lines, not vectors": θ uses |⟨x,y⟩|, so a proof that instead bounds vector angles in
         [0,π] proves a different statement.
     (b) Repetitions allowed: a proof implicitly assuming the N lines are pairwise distinct is
         invalid, since the conjectured optimum itself has repeats.
     (c) M(N,d) / k bookkeeping: for N=d+k, 0≤k≤d, M(N,d)=k; here k=2, so the bound's "-2" is exactly
         M(d+2,d) and must be recomputed by the prover, not assumed by pattern-matching to C3.
     (d) "d≥2" specifically for this cell (S is required to start at d=2, not d=1).
- S5 Consistency with other cells (no cell in this run's ledger has been gated — this is a
     single-cell run on A-C5 only, A-C1..A-C4 were not attempted here): none available as an
     ASSUMPTION. If a proof internally reproves and uses an A-C2- or A-C3-style lemma, that
     sub-argument must itself be checked as part of this proof (see G6 no circularity / G8 cite
     precisely) — it is not pre-verified and may not be waved through as "known".
- S6 Small explicit instances and numerical checks (from the statement/skill only, not from any
     gated computation): at d=2 (N=4 lines in the plane) the bound gives S≤(C(4,2)-2)π/2 = 4π/2 = 2π;
     the two coordinate axes each used twice give exactly S=2π (6 pairs, 2 coincide at θ=0, 4 are
     orthogonal at π/2: 4·π/2=2π) — this is also a special case of A-C1's bound at N=4 (⌊16/4⌋=4,
     matching). At d=3 (N=5) the bound is 4π (A-C4's first instance, verbatim in the skill); at d=4
     (N=6) the bound is 13π/2 (A-C4's second instance, verbatim). Any proof must reproduce these
     three numbers exactly when specialised.
