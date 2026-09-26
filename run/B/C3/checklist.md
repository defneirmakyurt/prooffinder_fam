# Checklist: B-C3

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
- S1 Exact statement: (a) d_B(lambda) <= k^2-2k-1 for every k >= 4, every n with T_{k-1} < n < T_k, every lambda |- n; (b) F(k) = D_B(T_k - 1) with its k-range stated, upper bound over all partitions + explicit witness, each for every k in range; (c) the complete set of maximisers at n = T_k - 1, with both inclusion directions proved (source: target.md). (b)'s two halves are gated separately.
- S2 Extremal configurations: unknown to the head for (a), (b), (c). Referee must enumerate exhaustively (exact) all partitions for every non-triangular n with rank 4..9 at least (n <= 44) and check (a); compute D_B(T_k - 1) and the full maximiser set for k <= 9 and compare with the claimed F(k) and set.
- S3 Cases: (a) EVERY non-triangular n in (T_{k-1}, T_k), i.e. every r = n - T_{k-1} in 1..k-1, for every k >= 4 (not just n = T_k - 1); every partition, incl. (n), (1^n), partitions with many 1-parts, and cyclic starts. (b)/(c): the claimed k-range, including its smallest k; (c) completeness (no other maximiser) proved for every k in range, not by table.
- S4 Traps (problem skill §8): d_B is the cycle-ENTRY time, not the first-repeat time; s counts parts before subtraction (1-parts included); new part s inserted in sorted position; d_B(cyclic) = 0; C3(b) states no k-range — the proof must state its range; computations for finitely many k prove nothing for all k; the witness orbit must be tracked symbolically in k.
- S5 Consistency: gated C1 (B-C1, VALID): for n = T_{k-1} + r (1 <= r <= k), lambda is cyclic iff lambda = (k-1+e_1, ..., 1+e_{k-1}, e_k) (final 0 dropped) with e in {0,1}^k, sum e = r; so for n = T_k - 1 (r = k-1) the cyclic partitions are delta_k with exactly one cell of the k-th diagonal removed (k of them). Any cyclicity test in the proof must agree with this. T_k - 1 = T_{k-1} + (k-1): C3(b) at k = 3 is n = 5 = T_2 + 2, so it must agree with C5 at k = 3 (C5 not gated: N/A now). For k >= 4, F(k) must satisfy F(k) <= k^2-2k-1 by (a).
- S6 Checkable values (from the statement): B((2,1,1,1,1)) = (5,1) -> (4,2) -> (3,2,1) -> (3,2,1), d_B((2,1,1,1,1)) = 3 (n = 6 triangular: not in scope of (a)). Referee's exhaustive table (S2) is the numerical check.
- S7 Consistency (added 16:25): gated C2 (B-C2, VALID): D_B(T_k) = k^2 - k for every k. Gated C3 lower half (B-C3-002, VALID): d_B((k-1,k-2,k-2,k-3,...,2,1,1)) = k^2-2k-1 for every k >= 3.
- S8 (hypothesis, from B-C3-001): (a) must hold for every k >= 4 and FAIL at k = 3 (n = 5: D_B = 3 > 2); a proof of (a) that never uses k >= 4 is suspect. A k = 4 computer step must be exhaustive over n in {7, 8, 9} with code.
- S9 (hypothesis, from B-C3-001): within each block the bound of (a) is attained only at n = T_k - 1 (checked k = 4..7); the argument must be tight on orbits with ONE drop and with SEVERAL drops (every maximiser makes its last drop at step D-1, checked k = 4..9).
- S10 (hypothesis, from B-C3-001): containment comparison with T_k / T_{k-1} alone gives only k^2 - k at n = T_k - 1 (objects (3,3,3,3,1,1), (4,4,4,2,2,1,1,1,1)); a proof resting only on it cannot reach k^2-2k-1.
- S11 (hypothesis, from B-C3-001): small k for (b): D_B(2) = 0 (k = 2), D_B(5) = 3 (k = 3); formula k^2-2k-1 from k = 4 (k = 3 gives 2 != 3).
- S12 (hypothesis, from B-C3-001): (c) set sizes |E_k| = 1, 6, 34, 175, 831, 3911, 18163 for k = 4..10 (a finite list in k is impossible; the description must be structural); any description must agree with E_k = B^{-(k^2-4k-2)}(mu_k), mu_k = (k,k-1,k-1,k-3,...,3,1), for k = 6..9.
- S13 (hypothesis, from B-C3-001): no cited result (e.g. Griggs-Ho 1998 Thm 4.4) may stand in as the proof of (a); it must be re-proved in full.
