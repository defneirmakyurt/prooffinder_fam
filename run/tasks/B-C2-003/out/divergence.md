# Divergence: literature vs blind solvers (B-C2)

Blind Phase-1 results: NOT AVAILABLE. The brief lists no inbox/earlier/ folder and none exists in this task's inbox, so no comparison with blind solvers is possible yet. A later comparison should check:
- the value: literature and this attempt give F(k) = k^2 - k for every k >= 1 with no small-k exceptions (k=1: 0, k=2: 2);
- the witness: literature (Griggs-Ho Thm 3.1) and this file use (k-1, k-1, k-2, ..., 2, 1, 1); for k >= 4 many other maximisers exist (3 for k=4, 16 for k=5, 65 for k=6, 293 for k=7, 1267 for k=8, by out/tmp/dbt.py), so a blind solver may legitimately use a different witness;
- the upper-bound method: Griggs-Ho's number-of-parts sequence (seq_B / diagram_B, sandwich patterns, backward chain of patterns of decreasing length) versus any diagonal/energy argument a blind solver may use.

Origin of ideas here:
- From literature (Griggs-Ho 1998, opened): diagonal-rotation description of B (their Steps 1-2, Sec. 2), witness family (Thm 3.1), c-sequence architecture and Lemmas 3.2-3.6 (Sec. 3).
- New in this write-up (not found in the opened source in written form): the explicit two-residue orbit computation for the witness (proof.md A.2-A.3: hole on diagonal k at column 1+(t mod k), extra cell on diagonal k+1 at column 1+((t+k) mod (k+1)), first coincidence at t = k^2-k-1 by CRT; Griggs-Ho state the orbit with "it is easy to see"); the non-cyclicity argument A.4 that avoids the uniqueness of cyclic partitions; the explicit counting in B9 (Griggs-Ho state "at most k^2-2k-1 terms before the c_p term" without the arithmetic); the flip form of the row comparison (B2) and the explicit induction I(m) replacing "continue this process" in Lemma 3.5 (B7); the part-sum formulation of the contradiction in Lemma 3.3(2) (B5). These are re-derivations of Griggs-Ho's lemmas, not new results.
- From the blind run: none (not available).
