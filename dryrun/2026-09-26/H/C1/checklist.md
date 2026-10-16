# Checklist: H-C1

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
- S1 Exact statement: for each d in {3, 4}, a value V_d with (a) a labelling of Q_d whose uphill-path count, re-scored by the accepted checker, is exactly V_d, and (b) evidence that every labelling of Q_d has at least V_d uphill paths. Both values are needed. (source: target.md)
- S2 Extremal values: unknown; the statement gives no value for U(Q_3) or U(Q_4). (source: problem skill §11)
- S3 Cases to cover: a lone valley counts as an uphill path; paths are counted as sequences, so different routes to the same endpoint count separately; labels are a bijection onto 1..2^d; both d = 3 and d = 4; an exact value needs both halves, the lower half over ALL labellings. (source: statement; problem skill §8, §11)
- S4 Known traps (source: problem skill §8): paths must start at a valley; labels strictly increase; the hand-in lists vertices in increasing label order (line i = vertex with label i), strings of exactly d characters with leading zeros; "exhaustive" needs a defined search space and a written soundness argument for every symmetry reduction, otherwise the value is at most BEST-FOUND; a time-limited or unfinished search is not a lower bound; scores are never copied from a report.
- S5 Consistency: every value handed in equals the accepted checker's count on the submitted labelling; any lower-bound argument stated for general d agrees with every verified small value. No lower cells exist. (source: problem skill §11)
- S6 Checkable instances: the accepted checker's hand-computed Q_1 and Q_2 test cases (from the Phase 0 checker-builders, once cross-tested). (source: problem skill §11)
