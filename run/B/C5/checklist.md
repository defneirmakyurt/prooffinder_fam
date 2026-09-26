# Checklist: B-C5

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
- S1 Exact statement: target.md (1)-(4) for every k >= 2: formula with stated k-range + remaining values; ONE uniform upper-bound argument; explicit extremal partitions in k; the Cell 3 extension analysis (its bound, strictly weaker, what replaces it).
- S2 Extremal configurations: unknown to the head. Referee computes D_B(T_{k-1}+2) and all maximisers exhaustively (exact) for k = 2..10 at least (n = 3, 5, 8, 12, 17, 23, 30, 38, 47) and compares with F(k), the stated range, the remaining values and lambda^(k).
- S3 Cases: every k >= 2, incl. k = 2 (n = 3 = T_2, triangular!), k = 3 (n = 5 = T_3 - 1), k = 4; every partition incl. (n), (1^n), cyclic starts; the upper bound must be ONE argument over the whole range, not per-k cases.
- S4 Traps (skill §8): k = 2 gives n = 3 = T_2, triangular, so it falls under C2, not C3(a); cycle-ENTRY time not first-repeat; s counts parts before subtraction; new part sorted in; d_B(cyclic) = 0; finitely many k prove nothing; the C3 analysis must name a concrete bound and prove strict weakness, not just assert it.
- S5 Consistency: gated C1 (VALID): for n = T_{k-1}+2 the cyclic partitions are delta_{k-1} plus exactly two cells of the k-th diagonal (binom(k,2) of them, floor(k/2) cycles). k = 2: must agree with C2 at k = 2 (lower half gated for C2: D_B(T_k) >= k^2-k, value 2 at k = 2 if C2's upper half is gated). k = 3: n = 5 = T_3 - 1 must agree with C3(b) at k = 3. k >= 4: F(k) <= k^2-2k-1 (C3(a), not yet gated).
- S6 Checkable values: none given by the statement for this family; use the S2 exhaustive table.
