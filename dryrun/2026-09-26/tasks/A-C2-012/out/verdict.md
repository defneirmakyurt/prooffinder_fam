```
CROSS VERDICT: CONFIRMED
BRANCH: ALGEBRAIC
STATEMENT MATCH: yes
TRANSLATION: Gram G = I + tridiag(c_1..c_{m-1}), PSD with rank <= m-1, so det G = 0. Step 4 is the Schur complement of G at pivot (m,m) followed by the diagonal congruence rescaling row/column m-1 by 1/sqrt(1-c_{m-1}^2). This gives a unit-diagonal tridiagonal PSD matrix of size m-1 with rank(G)-1 <= m-2. Its squared off-diagonals are s_1..s_{m-3} and s_{m-2}/(1-s_{m-1}). Induction then runs on matrix size, and the base case is the 2x2 PSD rank-1 matrix, where |c|=1. Steps 5-6 show that one Schur step cannot lower sum arcsin|c_i|. Contrapositive: a tridiagonal matrix with off-diagonals sin a_i and sum a_i < pi/2 is positive definite.
RED FLAGS: none
CHECKLIST: see below
CEX SEARCH: out/cex/gram_search.py, log out/cex/log.txt. Tested 32252 exact-rational admissible Gram chains (m=3..12, squared off-diagonals exact, det=0 and PSD checked exactly). The Step 4 reduction was re-checked exactly on each one (reduced det = 0, PSD). The S2 equality tuples (m=2..8) were checked, and the Step-5 lemma was checked exactly on 1330 pairs. No violations; the minimum gaps are about -2e-15, which is float noise at exact-equality families.
RAN: sanity_lemma.py (subject, 1e6 float samples) COMPLETED 0.63 s; out/cex/gram_search.py (m=3..12, 4000 draws each; m=2..8 equality; 1330 lemma pairs) COMPLETED 2.38 s
```

## Translation (ALGEBRAIC lens)

An admissible chain is the same thing as a real symmetric m x m matrix G with unit diagonal, G_ij = 0 for |i-j| >= 2, G PSD and rank G <= m-1, which here is equivalent to det G = 0. Every such matrix is realised in R^(m-1) (Cholesky / spectral factorisation), and conversely. Its leading minors form the continuant D_k = D_{k-1} - c_{k-1}^2 D_{k-2}, which depends only on s_i = c_i^2. That is why signs don't matter (S3).

- **Step 1** turns theta = arccos|c| into pi/2 - arcsin|c|. The target becomes A = sum arcsin|c_i| >= pi/2. This is a purely scalar identity and is correct.
- **Step 4 = Schur complement.** Projecting x_1..x_{m-1} onto x_m^perp gives the Gram matrix G/G_mm with entries G_ij - G_im G_jm. Since G_im = 0 for i <= m-2, only the (m-1,m-1) entry changes, to 1 - c^2. The (m-2,m-1) entry stays c_{m-2} because G_{m-2,m} = 0; this is (4d). Rescaling by diag(1,..,1,1/sqrt(1-c^2)) restores unit diagonal. It gives the off-diagonal c_{m-2}/sqrt(1-c^2) = sin a_{m-2}/cos a_{m-1}, as the proof states. By the Guttman/Haynsworth rank additivity rank G = 1 + rank(G/G_mm), the reduced matrix has rank <= m-2. This is exactly the proof's statement "an (m-1)-chain in the (m-2)-dimensional W". The dimension hypothesis is used here, and it ends in the base case: a 2x2 PSD rank-1 unit-diagonal matrix forces |c| = 1. So trap S4(c) is avoided. In R^m the identity basis has det 1 and is excluded.
- **Steps 5-6** say the reduced arcsin-sum a_1+...+a_{m-3}+a' is <= A. So the Schur reduction does not lower the arcsin-sum, and the induction closes. Algebraically, the key inequality is sin a <= sin(a+b) cos b when a+b < pi/2, i.e. sin b cos(a+b) >= 0. The identity was re-derived by hand and is correct.

Contrapositive view, as a check that the translation is coherent: if sum a_i < pi/2, the unit-diagonal tridiagonal matrix with off-diagonals sin a_i is positive definite. It then has full rank m, so it cannot be realised in R^(m-1). This is consistent with the proof.

## Red flags
None. Every step translates, and the translation agrees with the proof's own formulas.

Cosmetic notes, none of which is a gap:
- The "continuity" remark in Step 1 is superfluous.
- The second clause of the Lemma in Step 5 is unused.
- The remark cites the code path as "out/code/"; it actually lives in subject/code.

## Per-step check
- **Step 1.** arccos t + arcsin t = pi/2 on [0,1]. The argument given is valid: pi/2 - s is in [0,pi/2] and cos(pi/2 - s) = t. The equivalence with (*) is exact. The isometry remark is valid: Gram–Schmidt gives an orthonormal basis of W.
- **Step 2.** In R^1, unit vectors are ±1, so |c_1| = 1 and A = pi/2. This covers m = 2 fully.
- **Step 3.** If |c_{m-1}| = 1, then a_{m-1} = pi/2, and since every a_i >= 0 we get A >= pi/2.
- **Step 4.** Checked:
  - dim W = m-2 >= 1.
  - u ⊥ x_m, and |u|^2 = 1 - c^2 > 0.
  - (4a): <x_j, x_m> = 0 for j <= m-2.
  - (4c): <x_i, y> = 0 for i <= m-3, because both <x_i,x_{m-1}> and <x_i,x_m> vanish.
  - (4d): <x_{m-2}, y> = c_{m-2}/cos a_{m-1}, because <x_{m-2},x_m> = 0.
  - The induction hypothesis applies to an (m-1)-chain with m-1 >= 2, through the isometry remark.
  - m = 3: the prefix sum is empty, W is 1-dimensional and a' = pi/2. Correct.
- **Step 5.** The expansion is re-derived and correct. sin b >= 0 and cos(a+b) > 0 hold on the stated ranges, and cos b > 0 justifies the division. arcsin is increasing, and arcsin(sin(a+b)) = a+b holds because a+b is in [0, pi/2).
- **Step 6.** The hypotheses of the Lemma are verified. Both cases are exhaustive, and every a_i >= 0 is used correctly.
- **Step 7.** Pure arithmetic: (m-1)pi/2 - A <= (m-2)pi/2.

## Checklist
- G1 PASS — The proved statement is exactly the cell's: m >= 2, R^(m-1), consecutive pairs, theta = arccos|.|, the same inequality direction.
- G2 PASS — Every step is written out, and there is no "clearly/similarly". The Step 5 identity is expanded in full.
- G3 PASS — m = 2 (Step 2), m = 3 (empty prefix sum), |c| = 1 (Step 3) and c = 0 (a_i = 0, handled uniformly) are all covered.
- G4 PASS — Invariant: the reduced tuple is a genuine (m-1)-chain in dimension m-2 (unit vectors, orthogonality, dimension). It was verified in text and re-checked exactly by Schur complement in cex Part B.
- G5 PASS — The construction of y is valid for every m >= 3 whenever |c_{m-1}| < 1. The other case is Step 3.
- G6 PASS — The induction hypothesis is used only at m-1. There is no citation of the target.
- G7 PASS — No load-bearing computation. The floating-point script is explicitly non-load-bearing.
- G8 PASS — Only standard facts are used (Cauchy–Schwarz, Gram–Schmidt, trigonometry). No external results are cited.
- G9 PASS — It says "SOLVED, full range, no computation used", and KNOWN GAPS is "none".
- S1 PASS — Statement matches word for word, including the chain sum over consecutive pairs only.
- S2 PASS — (e1,e1,e2,..,e_{m-1}) satisfies the hypotheses, and in the proof c_1 = 1, so Step 3 at every level gives A = pi/2 exactly. It is tight. Exact check for m = 2..8 in Part C. Every m = 3 chain is an equality case (s_1 + s_2 = 1 forces a_1 + a_2 = pi/2).
- S3 PASS — The m = 2 and m = 3 cases, R^(m-1), equal or antiparallel vectors (Step 3), orthogonal vectors (a_i = 0) and signs (through |c|) are all covered.
- S4 PASS — (a) theta is in [0,pi/2] through |c|. (b) Only consecutive pairs are summed. (c) The dimension is used in the base case, via the Schur rank drop. (d) No distinctness is assumed. (e) No float claims. (f) No citation.
- S5 PASS — At m = 3 the proof gives theta_1 + theta_2 <= pi/2 (with equality always), which agrees with A-C1 at N = 3.
- S6 PASS — m = 2 gives 0; m = 3 gives pi/2; the S2 tuples give (m-2)pi/2. The random exact-Gram instances never exceed the bound.

## Numerical checks and counterexample search
Runs (python3 stdlib, measured with bash `time`):
- **Subject `sanity_lemma.py`** (venv python). Minimum margin 3.08e-12 over 1e6 samples. 0.63 s, COMPLETED.
- **`out/cex/gram_search.py` Part A/B.** For m = 3..12, 4000 random draws each, using exact rational squared off-diagonals. The last entry is forced so that det = 0, and PSD is verified exactly through the leading minors. 32252 admissible chains were accepted. The minimum of A - pi/2 per m is -2.2e-15 (m=3), -8.9e-16 (m=4), -4.4e-16 (m=5), 0 (m=6), and >= 0.058 for m >= 7. The tiny negatives are float rounding at exact-equality configurations (m = 3 is identically equal, and zero off-diagonals split the chain). There are 0 violations below -1e-12. On every chain the proof's Step 4 reduction is verified exactly: the reduced squared entry is <= 1, the reduced determinant = 0, and the reduced matrix is PSD.
- **Part C.** The equality tuples give chain sum = (m-2)pi/2 for m = 2..8. The identity basis has det 1, so it is excluded.
- **Part D.** The Step-5 lemma is checked exactly on 1330 rational-tangent pairs.
- Part A/B/C/D together took 2.38 s, COMPLETED. Full log is in `out/cex/log.txt`.

Limitation: Part A's arcsin sums are floating point. This is used only as a search and is not load-bearing. The verdict rests on the written re-derivation above.
