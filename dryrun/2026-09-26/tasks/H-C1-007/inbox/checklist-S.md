# Checklist H-C1

## Part S (specific; referees and the gate only, NEVER shown to blind agents)
- S1 Exact statement: for each d in {3, 4}, a value V_d with (a) a labelling of Q_d whose uphill-path count, re-scored by the accepted checker, is exactly V_d, and (b) evidence that every labelling of Q_d has at least V_d uphill paths. Both values are needed. (source: target.md)
- S2 Extremal values: unknown; the statement gives no value for U(Q_3) or U(Q_4). (source: problem skill §11)
- S3 Cases to cover: a lone valley counts as an uphill path; paths are counted as sequences, so different routes to the same endpoint count separately; labels are a bijection onto 1..2^d; both d = 3 and d = 4; an exact value needs both halves, the lower half over ALL labellings. (source: statement; problem skill §8, §11)
- S4 Known traps (source: problem skill §8): paths must start at a valley; labels strictly increase; the hand-in lists vertices in increasing label order (line i = vertex with label i), strings of exactly d characters with leading zeros; "exhaustive" needs a defined search space and a written soundness argument for every symmetry reduction, otherwise the value is at most BEST-FOUND; a time-limited or unfinished search is not a lower bound; scores are never copied from a report.
- S5 Consistency: every value handed in equals the accepted checker's count on the submitted labelling; any lower-bound argument stated for general d agrees with every verified small value. No lower cells exist. (source: problem skill §11)
- S6 Checkable instances: the accepted checker's hand-computed Q_1 and Q_2 test cases (from the Phase 0 checker-builders, once cross-tested). (source: problem skill §11)
