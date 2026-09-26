# Space choices: B-C3

## 16:20, map B-C3-001

| Card | Tag | Branch | Fidelity | Check | Tight | Cost | Payoff | Decision | Reason |
|---|---|---|---|---|---|---|---|---|---|
| S1 | diag-array | DISCRETE | EQUIVALENT | PASSED | N/A | MEDIUM | HIGH | WAVE | EQUIVALENT, check reproduced (4507 partitions n<=22); restates the live diagonal lineage whose lower-half proof B-C3-002 is already gated VALID; language for (c) if a later wave needs it |
| S2 | seqB-diagram | DISCRETE | EQUIVALENT | PASSED | N/A | MEDIUM | HIGH | WAVE | EQUIVALENT, check reproduced; restates the live c-sequence lineage (gated C2 proof B1-B9, repair B-C3-011) and is what 1L B-C3-007 and analyst B-C3-012 are reconstructing; FRESH wave only if all three fail |
| S3 | containment-order | DISCRETE | RELAXATION | PASSED | NO | LOW | LOW | DEADEND | TIGHT NO, reproduced: comparison with /beta/=T_k gives max_lam min_beta d(beta)=k^2-k at n=T_k-1 (20,30,42 vs 14,23,34 for k=5,6,7); cannot carry (a) |
| S4 | CRT-timing | NUMBER-THEORY | RELAXATION | PASSED | NO | MEDIUM | MEDIUM | DEADEND | TIGHT NO, reproduced: summing CRT waiting times over drops is far from tight (k=5 n=14: 9 drops, max gap 14, product bound 126 vs D=14); tight only on the single-drop extremizer |
| S5 | reverse-tree | COMPUTATIONAL | EQUIVALENT | PASSED | N/A | LOW | HIGH | WAVE | COMPUTATIONAL (search-only), check reproduced (reverse rule 0 mismatches; E_k=B^{-L}(mu_k) k=7..9); the next (c) wave if B-C3-010/013 return without a closed-form description |
| S6 | carolina-analogue | DISCRETE | ANALOGY | NOT | N/A | MEDIUM | LOW | DROP | ANALOGY, CHECK NOT RUN, low payoff; humans asked for fewer agents |

Kept branches: none (the matrix falls back to the latest 2A triage)

Handed to workers (2B / VERIFIER: the branch and its generic lens only, since card text never reaches blind agents; WAVE: the card's ANGLE, in a FRESH brief):
- S1 WAVE [diag-array]: Encode lambda |- T_k-1 as the Etienne/Griggs-Ho (0,1)-array; B is diagonal rotation plus a left-shift that lowers the energy. First write the orbit of lambda_k=(k-1,k-2,k-2,...,1,1) explicitly (one drop, at step k^2-2k-2), then study which arrays sit at depth k^2-2k-1 via the merge point mu_k.
- S2 WAVE [seqB-diagram]: Work with seq_B and diagram_B exactly as Griggs-Ho Sections 3-4 (preprint linked). Reprove Thm 4.4(1) self-contained (the cell needs a written proof; cite nothing as the proof), then run the equality case: d_B=k^2-2k-1 forces which (p,q,x) pattern chain, hence which c_1..c_D.
- S5 WAVE [reverse-tree]: Treat E_k as the set of legal reversed-move words of length k^2-4k-2 starting at mu_k=(k,k-1,k-1,k-3,...,3,1). Enumerate for k<=11, find the word language / array conditions, then hand the conjectured description to S1/S2 for proof.

