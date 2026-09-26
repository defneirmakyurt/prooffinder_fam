# Checklist: A-C5-D2

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
- S1 Exact statement and the quantities to be bounded (from target.md): for every 4 lines
     ℓ_1,...,ℓ_4 through the origin of R^2 (repetitions allowed), S=Σ_{i<j}θ(ℓ_i,ℓ_j) ≤ 2π,
     θ=arccos|⟨x,x'⟩|∈[0,π/2]. This is A-C5's target specialised to d=2, N=4 only — NOT the
     full A-C5 statement (which also requires d≥3; that is explicitly out of scope for this
     lemma-cell and must NOT cause a FAIL here).
- S2 Equality / extremal configuration: the 2 coordinate axes, each used twice (g=(0,π/2,0,π/2)
     in the submitted proof's gap parametrisation); also 4 evenly-spaced lines
     (g=(π/4,π/4,π/4,π/4)). Both must give S=2π exactly.
- S3 Cases the proof must cover: every configuration of 4 lines in R^2, including all
     degenerate/repeated (coincident) lines (θ=0 pairs are legal, not excluded).
- S4 Known traps: θ uses |⟨x,y⟩| (lines, not vector angles in [0,π]); repetitions are legal and
     occur in the extremal configuration; C(4,2)-2=4 so the bound is 4·π/2=2π (recompute, don't
     pattern-match).
- S5 Consistency with other cells: none gated in this run to check against.
- S6 Small explicit instance: N=4, d=2 IS the instance (the whole lemma); the bound 2π must be
     reproduced exactly, with equality demonstrated at the two configurations in S2.
