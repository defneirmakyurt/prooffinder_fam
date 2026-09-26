```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves (i) for all k>=1; (ii)(a) iff-characterisation C(k,r) for all k>=1, 1<=r<=k; (ii)(b) N(k,r)=(1/k)sum_{d|gcd(k,r)}phi(d)binom(k/d,r/d); no extra hypotheses.
  G2 PASS — every step written out; no "clearly/similarly/obviously/by symmetry/WLOG"; only trivially-filled one-liners (6.1 inclusion, 6.5 gcd scaling).
  G3 PASS — k=1 treated explicitly (Thm 9(a),(d)); r=k and r'=0 handled in Thm 11; r=1 generic; 1-parts handled via mu's zero entries.
  G4 PASS — E non-increasing (Lemma 3a), strict when sorting is needed (Lemma 2); constancy on cycles gives sort-free steps; strictness only used where proved.
  G5 PASS — lambda(eps), rho-equivariance proved for every k>=1, eps in W(k,r) (Thm 9).
  G6 PASS — no circularity; (i) is derived from (ii)(a) plus pigeonhole; no citation of the target.
  G7 PASS — no step depends on computation; included code is exact, stdlib, 4.5 s.
  G8 PASS — only elementary facts used (Bezout, unique sorted arrangement); Burnside proved in 6.3. (Two stale internal refs "Step 10.1/10.3" in the preamble, cosmetic.)
  G9 PASS — header and Section 9 state exactly what is established; KNOWN GAPS: none.
  S1 PASS — both directions of (ii)(a) (Cor 10 and Thm 11 =>), count binom(k,r), cycle count proved via bijection with necklaces + Burnside; (i) both parts.
  S2 PASS — delta_k unique cyclic at T_k (Thm 13); claimed set and count re-derived and confirmed exhaustively n<=50.
  S3 PASS — general lemmas have no restriction on #parts or part size; k=1, n=2,3, r=1, r=k all covered; exhaustive check covers them.
  S4 PASS — s counts 1-parts (Lemma 1, mu includes zeros); sorting handled (Lemma 2/3); fixed points cyclic (p>=1); cycles counted, not cyclic partitions; energy only used for sort-freeness on cycles, cycles identified by Prop 7.
  S5 PASS — r=k: C(k,k)={delta_k}, N(k,k)=1 (6.7); k=1: (1) fixed.
  S6 PASS — statement's example chain reproduced; exhaustive n=1..50 comparison of cyclic set and cycle count all match.
EQUALITY CASES: n=T_k, k=1..9: cyclic set = {delta_k}, one fixed point, every partition reaches delta_k by iteration. r<k for all n<=50: cyclic set = C(k,r), cycle lengths = rotation-orbit sizes.
CROSS-CELL: N/A (C1 first cell); internal r=k reduction consistent.
CEX SEARCH: out/cex/indep_check.py (n=1..50), out/cex/steps_check.py; no counterexample.
OTHER ISSUES: cosmetic only (see below).
RAN: subject check_c1.py copy, n=1..45, COMPLETED, real 4.50 s | indep_check.py n=1..50 (literal-definition check n<=28), COMPLETED, real 26.09 s | steps_check.py, COMPLETED, real 0.79 s
```

# Referee report, task B-C1-006 (GATE on subject B-C1-001)

## 1. Statement match

Target (i): for every k >= 1, every lambda |- T_k has i >= 0 with B^i(lambda) = delta_k, and delta_k is the only cyclic partition of T_k.
Proof: Theorem 13 proves both parts for every k >= 1. Match.

Target (ii)(a): for every k >= 1 and 1 <= r <= k, an explicit description of ALL cyclic partitions of T_{k-1}+r, as a function of k and r, with an iff proof.
Proof: C(k,r) = {(k-1+e_0, ..., 1+e_{k-2}, e_{k-1}) with a final 0 deleted : e in {0,1}^k, sum e = r}. Theorem 11 proves both directions. Match.

Target (ii)(b): the exact number of distinct cycles, as a formula in k and r.
Proof: N(k,r) = (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d) (Theorem 12). This is an explicit formula. Match.

The quantifiers, the ranges (k >= 1, 1 <= r <= k, both ends included), and the definitions (s counts parts before subtraction, 1-parts included; cyclic means B^i = id for some i >= 1) are all preserved. The reading of "distinct cycles" as the cycles of the functional graph of B on P(n) is stated explicitly, and it is the natural reading.

## 2. Checklist

The table is in the block above. All items are PASS.

## 3. Per-step reasons (why each step holds)

- **0.1–0.3.** These are conventions. Y(lambda) has sum_a lambda_a = n points. Y is injective because lambda_a is the number of points in row a.
- **0.4 (Young property).** b < lambda_a forces a < s. Then lambda_{a'} >= lambda_a > b >= b' by monotonicity. Holds.
- **0.5–0.6.** Diagonals D_d have d+1 points each and partition the quadrant. T_d = sum_{j<d}(j+1). T is strictly increasing, so the rank is unique. Holds.
- **1.1.** A zero entry contributes a·0 + C(0,2) = 0. So trailing zeros do not change E. Holds.
- **Lemma 1.** Identity used: C(x-1,2) = C(x,2) - (x-1), valid for every integer x. The entry at index a+1 contributes a·lambda_a + C(lambda_a,2) - a. Summing, sum_{a<s} a = C(s,2), and this cancels the C(s,2) contributed by mu_0 = s. I verified this algebra by hand and exhaustively for all partitions with n <= 50.
- **Lemma 2.** Swapping an adjacent ascent y_a < y_{a+1} changes F by y_a - y_{a+1} < 0 (I recomputed this). Bubble sort terminates because F strictly decreases on a finite set, and the sorted arrangement is unique. C(x,2) is invariant under rearrangement. So E(x*) <= E(x), strictly if x is unsorted. Also tested on 20000 random sequences.
- **Lemma 3.** The multiset of mu is the parts of B(lambda) plus zeros, so mu* = (B(lambda), 0, ..., 0) and E(mu*) = E(B(lambda)).
  - (a) Lemma 2 plus Lemma 1.
  - (mu_1, ..., mu_s) is always decreasing, so mu is sorted iff s >= lambda_0 - 1.
  - (b) is the contrapositive of the strict part of Lemma 2.
  - (c) If mu is sorted, then mu = mu*, so its zeros are trailing.
  - Holds, and was checked exhaustively for n <= 50, including strict decrease whenever s < lambda_0 - 1.
- **2.1.** tau is a bijection, and its explicit inverse is checked in both directions. Holds.
- **Lemma 4.** With nu_0 = s, nu_{a+1} = lambda_a - 1 (zero-padded) and nu_c = 0 for c > s, Y(nu) splits into row 0 plus the shifted rows. tau sends column 0 of Y(lambda) to row 0 and the rest by (a+1, b-1). Holds, and was checked exhaustively (Y(B lambda) = tau(Y lambda) whenever s >= lambda_0 - 1, n <= 50).
- **Lemma 5.** Direct computation on p_d(a), then induction on t. Holds.
- **Lemma 6.**
  - (a) Periodicity.
  - (b) E is non-increasing along a periodic sequence, so it is constant. Then Lemma 3(b) applies at every t.
  - (c) Lemma 4 plus induction.
  - Holds. This is the only place the energy is used, so no "strict decrease off cycles" is needed (S4 trap avoided).
- **Prop 7.** The steps:
  - (1) Injectivity of tau^t gives the hole at tau^t(q). Lemma 5 gives the positions.
  - (2) g | (Q-P) >= 1, so {0, ..., Q-P} contains every residue mod g. Bezout gives j with jP ≡ c* - y - t_0 (mod Q). Then t = t_0 + jP puts the hole at p_d(0) = (0,d) and the cell at p_{d'}(c*) with 0 <= c* <= Q-P.
  - (3) (0,d) <= (c*, d'-c*) componentwise, since d' - c* >= d. The Young property then gives a contradiction.
  - Holds. The construction of t was re-run exactly for all 0 <= d < d' <= 40 and all x, y (358750 tuples).
- **Cor 8.** e exists by counting. Prop 7 applied to the hole on D_e removes every cell above e. r' <= e because D_e has a hole. n = T_e + r' by the disjoint union. Holds, and the shape was checked on every cyclic partition with n <= 50.
- **Thm 9.**
  - (a) Entries L_a >= 1 for a <= k-2. Differences 1 + e_a - e_{a+1} >= 0. The sum is T_{k-1} + r. k = 1 is explicit.
  - (b) Row a is {a+b <= k-2}, plus p_{k-1}(a) iff e_a = 1. There are no rows >= k.
  - (c) Follows from (b).
  - (d) lambda_0 - 1 <= k-1 <= s, so Lemma 3(c) applies. Entrywise comparison with L(rho e) covers both cases e_{k-1} = 0 and e_{k-1} = 1. Only the last entry of L(rho e) can be 0.
  - Holds. (d) was checked for every e, k <= 10.
- **Cor 10.** rho^k = id, so B^k = id on C(k,r), with k >= 1. Holds.
- **Thm 11.**
  - (<=) Thm 9(a) plus Cor 10.
  - (=>) Case r' >= 1: T_e < n < T_{e+1}, so by uniqueness of rank e+1 = k and r' = r. Then Y(lambda) = Y(lambda(e)) and Y is injective.
  - (=>) Case r' = 0: n = T_e with e >= 1, so k = e and r = k, and Y(lambda) = Y(lambda(1,...,1)).
  - The count follows from Thm 9(c).
  - Holds.
- **5.2.** Restates the set. It is explicit in k and r.
- **6.1.** O(mu) = O(lambda) for mu in O(lambda): lambda = B^{p-t'}(mu), and O(mu) ⊆ O(lambda) trivially (B^u mu = B^{u+t} lambda; this one-liner is left implicit). So cycles partition the cyclic set. Holds.
- **6.2.** Lambda is a bijection W -> C with B∘Lambda = Lambda∘rho. So Lambda maps rho-orbits bijectively onto cycles. Holds.
- **6.3 (Burnside).** Standard double count plus orbit–stabiliser, written out. Holds.
- **6.4.** Bezout reduces rho^j to rho^g with g = gcd(j,k). Invariance under rho^g means constant on residue classes mod g, and conversely. The count is binom(g, rg/k) if (k/g) | r, else 0. Holds, and was brute-forced for all j, 1 <= r <= k <= 14.
- **6.5.** j = g j' with gcd(j', k/g) = 1, which uses gcd(gj', gm) = g·gcd(j', m) (elementary, left implicit). The j' = 0 ↔ j' = m swap gives phi(k/g). Holds, and was checked for k <= 200.
- **Thm 12.** Group the Burnside sum by g = gcd(j,k) and substitute d = k/g. Holds. The formula matches brute-force necklace counts for 1 <= r <= k <= 16, and the actual B-cycle counts and lengths for n <= 50.
- **6.7.** sum_{d|k} phi(d) = k gives N(k,k) = 1. For r in {1, k-1}, gcd = 1 gives N = 1. Holds.
- **Thm 13.** r = k gives W(k,k) = {(1,...,1)}, so C(k,k) = {delta_k}. Pigeonhole on M+1 iterates gives a cyclic iterate, and that iterate must be delta_k. Holds.
- **Sections 8–9.** The edge cases listed are correctly handled by the earlier steps.

No unjustified, circular or false step found.

## 4. Numerical sanity, equality cases, cross-cell

- **Subject code.** An identical copy was run (cmp-verified) as out/cex/subject_check_c1_copy.py: ALL OK up to n = 45, real 4.50 s. It uses exact integers and stdlib only. It is not load-bearing.
- **Equality / named cases.** For n = T_k, k = 1..9: the cyclic set is {delta_k}, it is a fixed point, and every partition reaches delta_k under direct iteration. The statement's example chain (2,1,1,1,1) -> (5,1) -> (4,2) -> (3,2,1) -> (3,2,1) was reproduced.
- **Cross-cell (S5).** r = k reduces to (i): N(k,k) = 1 and C(k,k) = {delta_k}. k = 1: (1) -> (1). There are no lower gated cells.

## 5. Counterexample search (out/cex/)

- **out/cex/indep_check.py** (log: out/cex/indep_log.txt). It is written independently of the subject's code, uses a different partition generator, and its count is validated against the pentagonal recurrence. B is implemented literally from the pile description. For every n = 1..50:
  - cyclic set via Kahn peeling of the functional graph;
  - for n <= 28, also the literal definition "exists 1 <= i <= |P(n)| with B^i lambda = lambda";
  - comparison with C(k,r), with binom(k,r), with N(k,r), with brute-force necklace orbits, and with the multiset of cycle lengths versus the multiset of rotation-orbit sizes;
  - checks of Lemma 1, Lemma 3(a)(b)(c), Lemma 4, Lemma 6(b), the Cor 8 shape, Thm 9(d), and (i) by direct iteration;
  - a random test of Lemma 2.
  - Result: no failure. COMPLETED, real 26.09 s.
- **out/cex/steps_check.py** (log: out/cex/steps_log.txt). It checks the Prop 7 time construction (all d < d' <= 40), the fixed-point counts of 6.4 (k <= 14) and the gcd-class counts of 6.5 (k <= 200). No failure. COMPLETED, real 0.79 s.

The finite checks are corroboration only. The proof does not rely on them, and it covers all k by argument.

## 6. Other issues (cosmetic, non-blocking)

1. The preamble cites "Step 10.1" and "Step 10.3". These steps do not exist; they should be Step 6.1 and Step 6.3.
2. The code path is given as `out/code/check_c1.py`, but the supplied path is `code/check_c1.py`.
3. The hand-in requires LaTeX. The subject is Markdown with LaTeX math, so it needs mechanical conversion to a .tex file before hand-in.
4. Two one-line facts are left implicit but are elementary:
   - O(mu) ⊆ O(lambda) in 6.1;
   - gcd(gj', gm) = g·gcd(j', m) in 6.5.
