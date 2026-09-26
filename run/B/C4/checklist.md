# Checklist: B-C4

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
- S1 Exact statement: F(k) = D_B(T_{k-1}+1) for every k >= 5; UPPER over every partition of T_{k-1}+1; LOWER by an explicit lambda^(k) with d_B = F(k), for every k >= 5 (target.md). Halves gated separately.
- S2 Extremal configurations: unknown to the head. Referee must compute D_B(T_{k-1}+1) and all maximisers exhaustively (exact) for k = 5..10 at least (n = 11, 16, 22, 29, 37, 46) and compare with F(k) and lambda^(k).
- S3 Cases: every k >= 5 (smallest k = 5, n = 11); every partition, incl. (n), (1^n), many 1-parts, cyclic starts; witness proved symbolically for every k >= 5.
- S4 Traps (problem skill §8): cycle-ENTRY time, not first-repeat time; s counts parts before subtraction; new part s sorted in; d_B(cyclic) = 0; for n = T_{k-1}+1 there are k cyclic partitions forming ONE cycle of length k (gated C1), so "reaching a cycle" means reaching any of them, not a fixed point; finitely many k prove nothing.
- S5 Consistency: gated C1 (VALID): for n = T_{k-1}+1 the cyclic partitions are delta_{k-1} plus exactly one cell of the k-th diagonal, i.e. (k-1+e_1, ..., 1+e_{k-1}, e_k) with exactly one e_j = 1 (k of them, one cycle of length k). C3(a) (not yet gated): n = T_{k-1}+1 is non-triangular of rank k, so F(k) <= k^2-2k-1 is required for k >= 5. C2 (lower half pending): D_B(T_k) >= k^2-k — no direct constraint.
- S6 Checkable values: none given by the statement for this family; use the S2 exhaustive table.
