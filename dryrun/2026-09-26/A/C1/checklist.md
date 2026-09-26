# Checklist: A-C1

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
- S1 Exact statement: for every N and all lines l_1..l_N through the origin of R^2, repetitions allowed, S = sum_{i<j} theta(l_i, l_j) <= (pi/2) floor(N^2/4), with theta = arccos|<x, x'>| in [0, pi/2]. (source: target.md)
- S2 Equality configuration: the N lines split as evenly as possible between two perpendicular directions (floor(N/2) on one, ceil(N/2) on the other) gives S = (pi/2) floor(N^2/4) exactly (stated in C1's text). Whether other configurations also attain equality: unknown (not given). A valid proof must not give a strictly smaller bound at the stated configuration. (source: statement)
- S3 Cases to cover: every N, both parities, including N = 1 (empty sum) and N = 2; repeated (coincident) lines with theta = 0; lines, not vectors, so theta <= pi/2 and signs of spanning vectors are irrelevant. (source: statement; problem skill §8, §11)
- S4 Known traps (source: problem skill §8): treating vector angles in [0, pi] instead of line angles in [0, pi/2]; assuming the lines are distinct; an argument valid for only one parity of N; floating-point "violations" near equality are meaningless, any claimed violation must be interval-certified; citing a published proof of this exact statement does not count.
- S5 Consistency (arithmetic from the definitions; no verified cells yet): binom(N,2) - M(N,2) = floor(N^2/4), so C1 is C6 at d = 2; the Setting's example at d = 2 gives S = (binom(N,2) - k) pi/2 for N = 2 + k, 0 <= k <= 2, i.e. pi/2, pi, 2pi for N = 2, 3, 4, each equal to (pi/2) floor(N^2/4). (source: statement; problem skill §11)
- S6 Checkable values: at the balanced perpendicular split, S = (pi/2) floor(N^2/4): N = 2 -> pi/2, N = 3 -> pi, N = 4 -> 2pi, N = 5 -> 3pi. (source: statement)
