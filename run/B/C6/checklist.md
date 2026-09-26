# Checklist: B-C6

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
- S1 Exact statement (target.md): the full cell asks F(n) = D_B(n) for EVERY n >= 1 with both halves. Partial results are judged on exactly the family they claim: each must state its n-range (which k, which r = n - T_{k-1}) and prove BOTH an upper bound over every partition of every n in the family and an explicit witness for every n in the family. A one-sided result must be labelled one-sided.
- S2 Extremal configurations: from gated cells only: D_B(T_k) = k^2-k (Cell 2); d_B((k-1,k-2,k-2,k-3,...,2,1,1)) = k^2-2k-1 at n = T_k - 1, k >= 3 (Cell 3 lower). Everything else unknown to the head; the referee must compute D_B(n) exhaustively (exact) for every n <= 40 at least and compare with the claimed formula on its whole family range inside that window.
- S3 Cases: every k and every r in the family claimed, including the smallest k where the family starts (small-k exceptions stated separately and exactly); n = 1, 2, 3 and triangular n if the claim covers them; r = 1 and r = k - 1 edges; every partition incl. (n), (1^n), cyclic starts (d_B = 0), many 1-parts.
- S4 Traps (problem skill section 8): d_B is the cycle-ENTRY time, not first-repeat time; s counts parts before subtraction (1-parts included); the new part s goes into sorted position; a formula checked for finitely many n is CONJECTURED; a computation counts only if exhaustive over a finite set the argument reduced the problem to; citing a published result for the claimed statement is not a proof.
- S5 Consistency: must agree with gated Cell 1 (cyclic partitions of T_{k-1}+r are (k-1+e_1,...,1+e_{k-1},e_k), e in {0,1}^k, sum e = r), Cell 2 (D_B(T_k) = k^2-k), Cell 3 lower (D_B(T_k-1) >= k^2-2k-1, k >= 3). Pending (not gated, N/A until gated): Cell 3(a) D_B(n) <= k^2-2k-1 for non-triangular n of rank k >= 4; Cells 4, 5 (families r = 1, r = 2).
- S6 Checkable values: official example d_B((2,1,1,1,1)) = 3, so D_B(6) >= 3; D_B(6) = D_B(T_3) = 6 by Cell 2. (hypothesis, from B-C3-001) D_B(2) = 0, D_B(5) = 3.
