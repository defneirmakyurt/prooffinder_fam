# Plan: H-C5-010 (FRESH, angle sat-ilp-lower + exhaustive-symbreak)

Goal (LOWER route): prove every induced forest of Q_9 has <= 279 vertices (F_9 <= 279);
then Lemma A (gated) gives U(Q_9) >= 512 + 8*(512-279) = 2376 >= 2369.
Fallback deliverable: the smallest threshold m such that "no induced forest of Q_9 has m vertices"
is proved with a checked certificate, plus where the solver stalls.

Reduction used throughout: deleting a vertex from an induced forest leaves an induced forest,
so "no induced forest with exactly m vertices" implies F_9 <= m-1.

| rung | content | depends | status |
|---|---|---|---|
| R1 | checker sanity: verify.py on a labelling built from a found forest (Lemma B decode) | - | NOT STARTED |
| R2 | encoder + CEGAR pipeline: F_5 = 18 (UNSAT at 19 with DRAT check, SAT at 18) | - | NOT STARTED |
| R3 | pipeline validation without top-level subcube bound: F_6 <= 36 using only Q_3..Q_5 bounds | R2 | NOT STARTED |
| R4 | validity of every implied constraint (subcube bounds, 4-cycle, cycle clauses, cardinality encoding) written out | - | NOT STARTED |
| R5 | soundness of symmetry breaking under Aut(Q_9) written out | - | NOT STARTED |
| R6 | analytic identity 8s = 1792 + c + e(S) (s=|S|, c=#components of T): gives F_9 <= 287 without computation | - | NOT STARTED |
| R7 | Q_9 SAT: UNSAT certificates for m = 287, 286, ... (smallest m reached) | R2-R5 | NOT STARTED |
| R8 | Q_9 SAT: UNSAT at m = 280 (=> F_9 <= 279) with DRAT/LRAT checked in < 10 min | R7 | NOT STARTED |
| R9 | lower-side sanity: largest induced forest found in Q_9 (search), to locate the true F_9 window | - | NOT STARTED |
| R10 | chain to U(Q_9) >= 2369 via Lemma A (only if R8) | R8 | NOT STARTED |
