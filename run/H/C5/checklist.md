# Checklist: H-C5

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
- S1 Exact statement: EITHER a labelling of Q_9 (512 vertices, 2304 edges) with at most 2399 uphill paths (Q9.txt, 512 lines, 9-character strings, line i = vertex with label i), OR a proof that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
- S2 Extremal values (statement): organisers' best bounds 2368 <= U(Q_9) <= 2400, lower bound unpublished. A labelling scoring below 2368 contradicts the organisers' (unpublished) lower bound: re-score with the accepted checker and tell the humans before believing it. A lower-bound proof reaching >= 2401 contradicts the organisers' 2400 construction and is wrong.
- S3 Cases: upper route: the count is the accepted checker's, on exactly the submitted file; the file passes validation (512 distinct 9-bit strings). Lower route: every labelling covered; computer-assisted steps need a written reduction to exactly the set searched, code under 10 minutes, exact arithmetic.
- S4 Known traps (problem skill §8): a lone valley counts as an uphill path (k=1); uphill paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley (increasing paths from non-valleys do not count); labels strictly increase and are a bijection onto 1..2^d; hand-in lists vertices in increasing label order (line 1 = label 1), strings exactly d characters with leading zeros; never trust a reported count, re-score with the accepted checker. Dry run (source: dryrun/2026-09-26-findings.md items 23, 25): two blind searches can be one algorithm (byte-identical artefacts, near-identical node counts); agreement of runs is evidence, not proof.
- S5 Consistency: any general-d argument must agree with Q_3 = 14 (exhaustive) and the checker-verified Q_4 labelling with 34; with H-L1 (if gated) the lower bound is at least 2306.
- S6 Checkable instances: accepted checker (library entry H-uphill-checker; Q_9 file scored in well under 1 s).
