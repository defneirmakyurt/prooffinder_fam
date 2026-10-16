# Checklist: A-C2

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
- S1 Exact statement: for every integer m >= 2 and all unit vectors x_1..x_m in R^(m-1) with <x_i, x_j> = 0 whenever |i-j| >= 2, sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m-2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. The quantity bounded is the chain sum over consecutive pairs only. (source: target.md)
- S2 Equality configurations: the statement gives none (unknown in general). Head arithmetic from the definitions, to be re-checked by the referee: for every m >= 2 the tuple (e_1, e_1, e_2, e_3, ..., e_{m-1}) in R^(m-1) satisfies the hypotheses and has chain sum 0 + (m-2)(pi/2) = (m-2) pi/2, so the bound is attained for every m and every inequality a proof chains together must be tight there; at m = 2 the only unit vectors in R^1 are +-e_1, so every admissible pair has sum 0 = bound. Whether other equality configurations exist: unknown. (source: definitions; head arithmetic, labelled)
- S3 Cases to cover: every m >= 2 (including m = 2, where the space is R^1 and the bound is 0, and m = 3); vectors in R^(m-1); consecutive vectors equal, antiparallel (theta = 0) or orthogonal (theta = pi/2); non-consecutive vectors exactly orthogonal; vectors are unit; signs of the x_i irrelevant because theta uses |<x, y>|. (source: statement; problem skill section 8, 11)
- S4 Known traps (source: problem skill section 8, plus arithmetic from the statement where labelled): (a) treating the vector angle in [0, pi] instead of arccos|<x,y>| in [0, pi/2]; (b) summing all pairs instead of consecutive pairs; (c) the dimension hypothesis R^(m-1), not R^m: a proof that never uses it is suspect, because in R^m the standard basis e_1..e_m satisfies the orthogonality hypothesis and has chain sum (m-1) pi/2 > (m-2) pi/2 (arithmetic from the statement); (d) assuming consecutive vectors are distinct, non-orthogonal or non-parallel; (e) floating-point "violations" near equality are meaningless, any claimed violation must be exact or interval-certified; (f) citing a published proof of this exact statement does not count.
- S5 Consistency with verified cells: A-C1 (gated VALID, final report filed) proves: for every N and all lines l_1..l_N in R^2 (repetitions allowed), S <= (pi/2) floor(N^2/4). At m = 3 the hypotheses put x_1, x_2, x_3 in R^2 with theta(x_1, x_3) = pi/2, so A-C1 at N = 3 gives theta(x_1,x_2) + theta(x_2,x_3) <= pi - pi/2 = pi/2, which is this cell's bound at m = 3; a C2 proof must agree. (source: gated A-C1; arithmetic)
- S6 Checkable values: m = 2 -> bound 0, every admissible pair gives 0; m = 3 -> bound pi/2; the S2 tuple gives exactly (m-2) pi/2 for each m (m = 3: pi/2, m = 4: pi, m = 5: 3pi/2). Random admissible instances must never exceed the bound in exact or interval arithmetic. (source: statement; head arithmetic in S2)
