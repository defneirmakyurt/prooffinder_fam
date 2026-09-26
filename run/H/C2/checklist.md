# Checklist: H-C2

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
- S1 Exact statement: determine the integer U(Q_5) (Q_5: 32 vertices, 80 edges): both an explicit labelling attaining V and a proof that every labelling has >= V uphill paths. Hand-in: the value and Q5.txt (32 lines, vertex with label i on line i).
- S2 Extremal values: the statement gives no value; the optimum is unknown. Hypothesis (not gated; promoted lemma H-L1 is under review): every labelling of Q_d, d >= 3, has >= d*2^(d-1)+2 paths, which would be 82 here. Any claimed value below 82 contradicts H-L1 and must be re-scored and scrutinised; a value equal to 82 is optimal if H-L1 passes the gate.
- S3 Cases: both halves (labelling AND lower bound over ALL labellings); lone valleys count; paths counted as sequences; labels a bijection onto 1..32; a lower bound by search needs a defined search space and a written soundness argument for every symmetry reduction and every pruning bound; a time-limited or incomplete search is not a lower bound.
- S4 Known traps (problem skill §8): a lone valley counts as an uphill path (k=1); uphill paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley (increasing paths from non-valleys do not count); labels strictly increase and are a bijection onto 1..2^d; hand-in lists vertices in increasing label order (line 1 = label 1), strings exactly d characters with leading zeros; never trust a reported count, re-score with the accepted checker. Dry run (source: dryrun/2026-09-26-findings.md items 23, 25): two blind searches can be one algorithm (byte-identical artefacts, near-identical node counts); agreement of runs is evidence, not proof.
- S5 Consistency: the submitted value equals the accepted checker's count on the submitted Q5.txt; a lower-bound argument stated for general d must agree with Q_3 = 14 (exhaustive, dry run) and not exceed 34 at d = 4 (checker-verified labelling); if H-L1 is gated, the value is >= 82.
- S6 Checkable instances: accepted checker (library entry H-uphill-checker, cross-tested 208 cases d = 1..9) on the artefact; Q_3 brute force min 14.
