# Space choices: B-C6

## 16:52, map B-C6-001

| Card | Tag | Branch | Fidelity | Check | Tight | Cost | Payoff | Decision | Reason |
|---|---|---|---|---|---|---|---|---|---|
| S1 | LU-split | ALGEBRAIC | EQUIVALENT | PASSED | N/A | MEDIUM | HIGH | WAVE | EQUIVALENT, check reproduced (lu_split n<=36, 3.4 s); concrete reduction d_B=max(fill,fit) for the open upper bound, derived independently by blind B-C6-003 (Step 8); a 2B blind solver would get only the generic lens and lose it, so it goes to a FRESH prover as ANGLE |
| S2 | rotating-diagonals | NUMBER-THEORY | EQUIVALENT | PASSED | N/A | MEDIUM | MEDIUM | HOLD | EQUIVALENT, restates the live diagonal-rotation lineages of all three blind provers; 2B not run now (lower bound at the gate, budget) |
| S3 | part-count-sequence | DISCRETE | EQUIVALENT | PASSED | N/A | HIGH | MEDIUM | HOLD | restates the live EXPLOIT lineage B-C6-008 (gated Cell 3 c-sequence method); map notes r enters only via the window sum |
| S4 | exhaustive-computation | COMPUTATIONAL | RESTRICTION | PASSED | N/A | LOW | MEDIUM | DROP | dominated by three independent blind exhaustive checks (n<=60, 62, 66) and this map's n<=80 table (compare_GH reproduced: 78 agree) |
| S5 | witness-families | DISCRETE | RESTRICTION | PASSED | YES | LOW-MEDIUM | HIGH | DROP | dominated: the same three witness families are proved by all three blind provers and at the gate (B-C6-004, referees 006/007) |
| S6 | carolina-compositions | DISCRETE | RELAXATION | PASSED | NO | LOW | LOW | DEADEND | TIGHT NO: Carolina D_C(T_k)=k^2-1 > k^2-k, relaxation cannot carry the bound |
| S7 | necklace-orbits | ALGEBRAIC | EQUIVALENT | PASSED | N/A | MEDIUM | MEDIUM | HOLD | EQUIVALENT (necklace orbit count reproduced n<=45), plausible for the fill side but not affordable now |

Kept branches: none (the matrix falls back to the latest 2A triage)

Handed to workers (2B / VERIFIER: the branch and its generic lens only, since card text never reaches blind agents; WAVE: the card's ANGLE, in a FRESH brief):
- S1 WAVE [LU-split]: Rewrite d_B as max of two one-sided hitting times in Young's lattice (fill delta_{k-1}; fit inside delta_k), each monotone in lambda and in n within a rank, with Cell-2 endpoint values. Try first the U-side: prove that removing one cell from any lambda |- m <= T_k shortens U by at least k+1 unless U is already <= m-k+1 (compare with GH Thm 4.4 route for r=k-1). Sources allowed: GH Thm 4.1 (Akin-Davis).

