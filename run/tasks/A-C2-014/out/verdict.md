VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
(Subject: A-C2-011 proof.md / claims.md. Referee task A-C2-014, MODE VERIFY.)

## 1. Checklist

- G1 PASS — Proves exactly: every m >= 2, unit x_i in R^(m-1), <x_i,x_j>=0 for |i-j|>=2, consecutive chain sum <= (m-2)pi/2 with theta = arccos|.|. No extra hypotheses.
- G2 PASS — Every step written out (arccos+arcsin identity, AM-GM, subtraction formula, coefficient collection, downward induction). "Standard linear algebra" in Step 6 is the fact that m vectors in an (m-1)-dim space are dependent, which is elementary.
- G3 PASS — m = 2 (R^1, B_1 = pi/2 forced), k = 1 in Step 4, alpha_i = pi/2 (repeated/antipodal), c_i = 0 (orthogonal), a_j or b_j = 0 in Step 2 all handled.
- G4 PASS — No invariants/decrease; the monotonicity B_0 <= ... <= B_{m-1} is used and holds since alpha_i >= 0; strictness cos(B_{k-1}) > 0 comes from B_{k-1} < pi/2.
- G5 N/A — No construction is needed (equality example is illustrative only).
- G6 PASS — No circularity; no citation of the target.
- G7 PASS — No computation used; the mentioned float script is declared non-load-bearing.
- G8 PASS — Only standard facts used (Cauchy–Schwarz, arcsin/arccos identity, sin subtraction, dimension count).
- G9 PASS — States "SOLVED, full target for every m >= 2", and what is/isn't used.
- S1 PASS — Exact statement matches; theta in [0, pi/2] via |c_i|; only consecutive pairs summed.
- S2 PASS — Equality tuple (e1,e1,e2,...,e_{m-1}): alpha_1 = pi/2, rest 0, B_{m-1} = pi/2 exactly; the only inequality chained at the end is B_{m-1} >= pi/2 (an equivalence of the target), so tight. Step 4 lemmas are only used in the case B < pi/2 (contrapositive), so no loss.
- S3 PASS — m = 2, 3, general m; equal/antiparallel (|c|=1), orthogonal (c=0); signs irrelevant (only |c_j| used, step 4a bounds 2c_j t_j t_{j+1} >= -2|c_j||t_j t_{j+1}|).
- S4 PASS — (a) uses arccos|c| in [0,pi/2]; (b) consecutive pairs only; (c) dimension R^(m-1) used essentially in Step 6 (in R^m, e_1..e_m give B = 0 < pi/2, consistent with Step 5 since they're independent); (d) no distinctness assumed; (e) no float; (f) no citation.
- S5 PASS — At m = 3 the proof gives B_2 >= pi/2, i.e. theta_1+theta_2 <= pi/2, same as A-C1 at N=3 with theta(x1,x3)=pi/2. In fact for m=3 equality always holds (x1 ⟂ x3 in R^2), consistent.
- S6 PASS — m=2: bound 0 matches; m=3: pi/2; S2 tuple values (m-2)pi/2 checked numerically m=2..11; random admissible instances never exceed.

## 2. Per-step re-derivation (reasons each step holds)

- Notation: |c_i| <= 1 by Cauchy–Schwarz so arcsin|c_i| is defined in [0,pi/2]; B_j nondecreasing since alpha_i >= 0.
- Step 1: For y in [0,1], s = arcsin y in [0,pi/2], cos(pi/2 - s) = sin s = y and pi/2 - s in [0,pi/2] = range of arccos, so arccos y = pi/2 - s. Summing gives chain = (m-1)pi/2 - B_{m-1}; target <=> B_{m-1} >= pi/2. Correct equivalence.
- Step 2: If a=0 or b=0, c=0 and RHS >= 0. Else (sqrt a |t| - sqrt b |s|)^2 >= 0 gives at^2+bs^2 >= 2 sqrt(ab)|ts| >= 2|c||ts|. Correct.
- Step 3: sin(v-u) = sin v cos u - cos v sin u <= sin v cos u since cos v, sin u >= 0 on [0,pi/2]; v-u in [0,pi/2] gives sin(v-u) >= 0; squaring nonnegatives preserves order. Correct.
- Step 4: (4a) expansion uses unit norms and orthogonality for |i-j|>=2; lower bound by -|.| valid. (4b) for j <= k-1, B_{j-1} <= B_j <= B_{k-1} <= pi/2, so Step 3 hypotheses hold with u=B_{j-1}, v=B_j, v-u = alpha_j, giving a_j b_j >= sin^2 alpha_j = c_j^2; Step 2 applies. (4c) coefficient of t_i^2: i=1 gets cos^2 B_0 = 1; 2<=i<=k-1 gets cos^2 B_{i-1} (from j=i) + sin^2 B_{i-1} (from j=i-1) = 1; i=k gets sin^2 B_{k-1}. Verified index bookkeeping incl. k=2. (4d) subtraction gives cos^2(B_{k-1}) t_k^2. k=1 trivially. Correct.
- Step 5: Downward induction; at stage k the relation reduces to sum_{i<=k} t_i x_i = 0; B_{k-1} <= B_{m-1} < pi/2 so Step 4 applies and cos(B_{k-1}) > 0 forces t_k = 0. Correct.
- Step 6: m vectors in R^(m-1) are dependent; contrapositive of Step 5 gives B_{m-1} >= pi/2; Step 1 converts to target. Correct.

No unjustified, circular or false step found. Only cosmetic remark: the proof mentions a script out/tmp/sanity.py that is not included in the inbox; nothing rests on it.

## 3. Numerical sanity / 4. Equality cases / 6. Counterexample search

Script: out/cex/search.py, log out/cex/log.txt, runtime out/cex/time.txt (real 15.5 s).
- Model: admissible configurations <=> tridiagonal Gram G = I + offdiag(c), PSD, rank <= m-1. Drew rational c_1..c_{m-2}^2 with leading block PD, set c_{m-1}^2 = D_{m-1}/D_{m-2} exactly (Fraction) so det G = 0 exactly (asserted); kept only if <= 1. m = 2..12, 33000 draws, 20114 admissible. Chain sum vs bound evaluated in mpmath 60 digits: 0 violations beyond 1e-40; min slack -2.2e-59 at m = 3 (roundoff at the identically-tight m=3 case). This is sanity only (float, high precision), not load-bearing.
- S2 equality tuple (c_1 = 1, others 0) m = 2..11: chain = (m-2)pi/2 to 1e-50; B_{m-1} = pi/2 exactly by hand.
- Step 3 inequality: 200000 random (u,v), 0 failures.
- Step 4 lemma: for random signed c with B_{k-1} <= pi/2 (incl. some |c|=1), compared the exact minimum of Q over t_k = 1 (Schur complement 1 - b^T A^{-1} b) to cos^2(B_{k-1}): 6738 instances, k = 1..9, 0 failures.

## 5. Cross-cell
Consistent with A-C1 at N = 3 (m = 3 case), see S5.
