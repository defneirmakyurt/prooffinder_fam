# Checklist: B-C1

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
- S1 Exact statement: (i) for every k >= 1, every lambda |- T_k reaches delta_k under iteration of B, and delta_k is the ONLY cyclic partition of T_k; (ii) for every k >= 1 and every 1 <= r <= k, n = T_{k-1}+r: an explicit description of ALL cyclic partitions of n with an if-and-only-if proof, and the exact number of distinct B-cycles on partitions of n (formula in k, r), proved. Both directions of the characterisation are needed: every listed partition is cyclic, AND every cyclic partition is listed (source: target.md).
- S2 Extremal / named configurations: at n = T_k the unique cyclic partition is delta_k (named by the statement). For r < k the set of cyclic partitions and the cycle count are not given by the statement: unknown to the head; the referee must re-derive the claimed set and count and test them by exhaustive enumeration for small n.
- S3 Cases the proof must cover: every k >= 1 (including k = 1, n = 1 and k = 2, n = 2, 3); every r with 1 <= r <= k, including both ends r = 1 and r = k; partitions with many parts equal to 1 (the count s includes parts equal to 1, which vanish); partitions with more than k parts or with a part larger than k.
- S4 Known traps (source: problem skill §8): s is the number of parts BEFORE subtraction, 1-parts included; the new part s goes into its sorted position, not at the front; "cyclic" means B^i(lambda) = lambda for some i >= 1 (a fixed point is cyclic); counting cycles is not counting cyclic partitions — a cycle of length L contains L cyclic partitions, and the count of distinct cycles must be proved, not read off small cases; a finite check proves nothing for all k (G7). Any monotone potential/energy argument must be checked to decrease STRICTLY off the cycles, or to be eventually constant with a separate argument; "eventually periodic because finite" alone does not identify the cycles.
- S5 Consistency (arithmetic from the definitions): part (ii) at r = k is n = T_k, so it must reduce to part (i): exactly one cyclic partition (delta_k) and exactly one cycle (a fixed point). k = 1 gives n = 1, partition (1), B((1)) = (1). No gated lower cells exist (C1 is the first cell).
- S6 Checkable values (from the statement): B((2,1,1,1,1)) = (5,1), B((5,1)) = (4,2), B((4,2)) = (3,2,1), B((3,2,1)) = (3,2,1); so (3,2,1) = delta_3 is cyclic (a fixed point) and d_B((2,1,1,1,1)) = 3. Referee must run an exact exhaustive enumeration of all partitions of n for every n <= 30 (at least), compute the set of cyclic partitions and the number of cycles, and compare with the claimed description and formula for every (k, r) in that range.
