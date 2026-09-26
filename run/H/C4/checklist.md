# Checklist: H-C4

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
- S1 Exact statement: determine both integers U(Q_7) (128 vertices, 448 edges) and U(Q_8) (256 vertices, 1024 edges): for each, an explicit attaining labelling and a proof that every labelling has at least that many uphill paths. Hand-in: both values, Q7.txt and Q8.txt.
- S2 Extremal values: none given; the optima are unknown. Hypothesis (not gated; promoted lemma H-L1 under review): >= d*2^(d-1)+2, i.e. >= 450 for Q_7 and >= 1026 for Q_8. Known upstream fact (statement, C5): 2368 <= U(Q_9) <= 2400, well above 2306 = 9*2^8+2, so the pattern |E|+2 fails by d = 9 at the latest; at the first d where the best labelling stays above |E|+2, the lower bound needs a new argument and a value there is at most BEST-FOUND without one.
- S3 Cases: both values required; both halves for each; lone valleys; sequences; bijection onto 1..2^d; exhaustive claims need a defined search space and written soundness for every symmetry reduction and pruning bound; a time-limited search is not a lower bound.
- S4 Known traps (problem skill §8): a lone valley counts as an uphill path (k=1); uphill paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley (increasing paths from non-valleys do not count); labels strictly increase and are a bijection onto 1..2^d; hand-in lists vertices in increasing label order (line 1 = label 1), strings exactly d characters with leading zeros; never trust a reported count, re-score with the accepted checker. Dry run (source: dryrun/2026-09-26-findings.md items 23, 25): two blind searches can be one algorithm (byte-identical artefacts, near-identical node counts); agreement of runs is evidence, not proof.
- S5 Consistency: each value equals the checker's count on its file; any general-d lower bound must agree with Q_3 = 14 and not exceed 34 at d = 4; monotonic sanity: values below |E|+2 contradict H-L1.
- S6 Checkable instances: accepted checker on Q7.txt, Q8.txt (runtime well under a second).
