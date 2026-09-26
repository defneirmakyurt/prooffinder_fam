```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves (i) and (ii)(a) iff and (ii)(b) for every k>=1, 1<=r<=k, with no extra hypotheses; (i) is Theorem 9 at r=k plus 1.2.
  G2 PASS — every step is argued; no bare "clearly/similarly/by symmetry"; the terse spots (2.1 compositions, 7.1 existence of K, 10.3 cosets) are one-line checks, re-derived below.
  G3 PASS — k=1 is handled explicitly (8.3), and d=1 in Lemma 6 (CRT mod 1 is trivial); r=k is the |S|=0 branch of 7.4 and r<k the |S|>=1 branch; 1-parts are counted in s (0.6).
  G4 PASS — E is non-increasing (4.1); on a cycle equality is forced (4.2), so the rotation law is exact. Strict decrease off cycles is not needed: reaching a cycle comes from pigeonhole (1.2).
  G5 PASS — lambda(eps) is a partition (8.1) and B(lambda(eps))=lambda(rho eps) (8.3) for every k>=1 and eps in W(k,r), by symbolic argument.
  G6 PASS — no circularity: the only-if direction (Sec. 6-7) uses only the energy/rotation facts; the if direction (Sec. 8) is a direct computation.
  G7 PASS — the included code is exact integers and stdlib only, declared not load-bearing, ran in 18.76 s; the proof uses no computation.
  G8 PASS — the external facts are standard and named (CRT, orbit-stabiliser, Burnside with its proof included, sum phi(d)=k with its proof sketched in 10.4); everything else is new work.
  G9 PASS — the "Established / not established" section states (i), (ii)(a), (ii)(b) for all k, r and excludes C2+.
  S1 PASS — both directions of the characterisation (7.5 only-if, 8.4 if) and the exact cycle count N(k,r) are proved.
  S2 PASS — delta_k is the unique cyclic partition at T_k; for r<k the set {lambda(eps)} and the count N(k,r) match my exhaustive enumeration for all n<=45.
  S3 PASS — all k>=1 including n=1,2,3; r=1 and r=k; many 1-parts (s counts them in 0.6/2.1); more than k parts or a part >k are excluded by 7.5 (cells on D_e, e>k, are absent).
  S4 PASS — s is taken before subtraction; the new part goes through sort; fixed points count as cyclic (p>=1); cycles are counted as orbits (Burnside), not as cyclic partitions; "eventually periodic" is not used to identify the cycles.
  S5 PASS — r=k gives binom(k,k)=1 cyclic partition (delta_k) and N(k,k)=1 cycle; k=1 gives (1), a fixed point.
  S6 PASS — the statement's example chain is reproduced; exhaustive enumeration n<=45 (>=30 required) agrees with the set and the formula for every (k,r).
EQUALITY CASES: n=T_k for k=1..9: the only cyclic partition is delta_k (a fixed point) and all partitions reach it. For r<k (n<=45) the cyclic set is exactly {lambda(eps)} and has binom(k,r) elements.
CROSS-CELL: consistent with S5 (r=k gives (i)); there are no lower gated cells.
CEX SEARCH: out/cex/check.py checks exhaustively n<=45 (540634 partitions) against the final claims and against Lemma 6 and the rotation law C(B^t lam)=R^t C(lam) on every cycle. It also checks the R-bijection, E(U)=E and the E-monotonicity/equality case for n<=30, Lemma 3 on all compositions n<=13, B(lambda(eps))=lambda(rho eps) for k<=14, and the formula against direct necklace counting for k<=16. No counterexample was found.
OTHER ISSUES: (presentation only) the hand-in asks for LaTeX, but proof.md is Markdown with LaTeX math, so it needs wrapping into a .tex file; "Established" cites out/code/check_c1.py but the file ships as code/check_c1.py.
RAN: subject code/check_c1.py, n=1..45, COMPLETED, real 18.76 s
RAN: out/cex/check.py 45 14 16 30 13 (A: n<=45; B: n<=30; C: compositions n<=13; D: k<=14; E: k<=16; F: examples), COMPLETED, real 4.68 s
```

# Referee report B-C1-004 (GATE, subject B-C1-002)

## 1. Checklist
This is the same as the block above. Statement match was checked word by word against target.md:
- (i) is stated for every k>=1 with i>=0. The target's "there is an i" is met with i=a>=0 from 1.2.
- (ii)(a) gives an explicit set as a function of (k,r) and proves iff.
- (ii)(b) gives the exact count as a formula in (k,r).
- Directions and strictness are correct: the count is exact and the set is an iff.

## 2. Per-step re-derivation (reason each step holds)

- **0.1** The reading of "cycle" is the forward orbit of a cyclic partition, and cycles are distinct as sets. This is the natural reading. Counting cyclic sequences instead gives the same number, since each cycle determines its cyclic order.
- **0.2** Definition of the cell set. |C(c)| = sum c_j by construction.
- **0.3** (1,h) in C(nu) means h <= nu_1, so every h' <= h also qualifies. This is immediate from the definition.
- **0.4** The D_d are disjoint, D_d has d cells, and every cell (j,h) lies in D_{j+h-1}. I verified this.
- **0.5** sum_{h=1}^{c_j}(j-1+h) = (j-1)c_j + c_j(c_j+1)/2. I verified this.
- **0.6** Because lambda is weakly decreasing, lambda_j >= 2 iff j <= t. So U(lambda) lists exactly the positive lambda_j - 1 together with s, and B = sort(U). This matches the official definition, and s counts the 1-parts.
- **0.7** Definition of R.
- **1.1** The parts are positive. Sorting makes the sequence decreasing. The sum is sum_{j<=t}(lambda_j - 1) + s = n, because the terms with j>t are 0.
- **1.2** P(n) is finite. Pigeonhole on |P(n)|+1 iterates gives a<b with B^a = B^b, so B^a(lambda) is cyclic with period b-a >= 1.
- **2.1** I checked both directions of the bijection:
  - Forward: a cell with h>=2 has lambda_j >= h >= 2, so j <= t, and it maps to (j+1, h-1) with h-1 <= c_{j+1}. A cell (j,1) has j <= s = c_1 and maps to (1,j).
  - Inverse: (1,h) maps to (h,1), which is valid because h <= s. A cell (j',h') with j'>=2 maps to (j'-1, h'+1), which is valid because h'+1 <= c_{j'}+1 = lambda_{j'-1}.
  - All four compositions give the identity; I checked each case.
  - Numerically confirmed for all partitions with n <= 30.
- **2.2** R preserves j+h-1 in both branches, so the bijection gives E(U) = E.
- **3.1** The sum of c_j(c_j+1)/2 is invariant under permutation, and both sequences have length m.
- **3.2** Swapping the order of summation gives sum_{j}(j-1)c_j = sum_{i=1}^{m-1}(n - P_i(c)). Correct.
- **3.3** Sort the i distinct indices sigma(1..i) as j_1 < ... < j_i. Then j_l >= l, so lambda_{j_l} <= lambda_l. Correct.
- **3.4** Subtract the two identities from 3.2 and apply 3.3.
- **3.5** Take c_i < c_{i+1}. The i distinct positions {1, ..., i-1, i+1} have sum > P_i(c), and by 3.3 that sum is <= P_i(lambda). So the i-th term (with i <= m-1, hence present in the sum) is strictly positive. Uniqueness of the sorted rearrangement gives the other direction. Numerically confirmed on all compositions with n <= 13.
- **4.1** Apply Lemma 3 to U(lambda), which consists of positive integers with sum n, then use 2.2. In the equality case sort(U) = U, so C(B lambda) = C(U) = R(C(lambda)) by 2.1. Numerically confirmed for n <= 30.
- **4.2** E is non-increasing around a closed orbit, so every step is an equality. Then B^i = B^{i mod p} extends this to all i. The equality case of 4.1 gives the one-step rotation law, and induction gives C(B^t lambda) = R^t C(lambda). Confirmed along every cycle for n <= 45.
- **5.1** For a<d the height d+1-a >= 2, so x_a maps to x_{a+1}. For a=d, R(d,1) = (1,d) = x_1. So R acts on D_d as a d-cycle.
- **5.2** R^t preserves every diagonal and is injective (R is globally injective: its two branches have images with first coordinate >=2 and =1 respectively). So membership in D_d transports exactly under R^t.
- **Lemma 6** CRT applies because gcd(d, d+1) = 1. For d=1 the congruence mod 1 is vacuous. It gives t with R^t x_a = (1,d) and R^t y_b = (1,d+1). By 5.2, (1,d) is not in C(B^t lambda) while (1,d+1) is in it, which contradicts 0.3. Confirmed on every cyclic partition for n <= 45.
- **7.1** Suppose every D_d were contained in C(lambda). The D_d are disjoint and nonempty (0.4), so C(lambda) would be infinite, which is impossible. So K exists. K >= 2 because (1,1) is in C.
- **7.2** Induction using Lemma 6. A nonempty diagonal that misses C is not contained in C, so the lemma applies at each step.
- **7.3** Follows from the partition of the cells into diagonals: n = T_{K-1} + |S| with 0 <= |S| <= K-1.
- **7.4** The rank is well defined because the intervals (T_{m-1}, T_m] tile N>=1. In the branch |S|>=1, n is in (T_{K-1}, T_K), so k=K and r=|S|. In the branch |S|=0, n = T_{K-1}, so k = K-1 and r = k. (*) holds in both branches.
- **7.5** In pile j <= k, the cells of height <= k-j lie on diagonals <= k-1 and are present. Height k+1-j is present iff eps_j = 1. Greater heights lie on diagonals >= k+1 and are absent. So lambda_j = k-j+eps_j, and piles j>k are empty. By (*), sum eps = r.
- **8.1** The first k-1 values are >= 1. Consecutive differences are 1 + eps_j - eps_{j+1} >= 0. The sum is T_{k-1} + r.
- **8.2** eps_j = lambda_j - (k-j) recovers eps from lambda.
- **8.3** s = k-1+eps_k (for k=1, s = 1 = eps_1), and the two multisets agree term by term. The k=1 case is checked separately. Confirmed for all eps with k <= 14.
- **8.4** rho^k = id, so B^k lambda(eps) = lambda(eps) with k >= 1.
- **Thm 9** Only-if is 7.5, if is 8.4, and the count binom(k,r) follows from injectivity (8.2).
- **10.1** Lambda is a bijection W(k,r) -> Cyc(n) that intertwines rho and B. Each cycle is the image of a rho-orbit, and orbits partition W(k,r), so the number of cycles equals the number of orbits.
- **10.2** The proof of Burnside's lemma is correct given orbit–stabiliser, which is a named standard theorem.
- **10.3** rho^j eps = eps iff eps is constant on the cosets of <j> = gZ/kZ, which has g cosets of size k/g. Such a word has r ones iff (k/g) divides r and exactly rg/k cosets carry a 1. So |Fix(rho^j)| = binom(g, rg/k).
- **10.4** There are phi(k/g) values of j with gcd(j,k) = g; this includes j=0 when g=k, since phi(1) = 1. Substituting d = k/g turns "d | k and d | r" into "d | gcd(k,r)". Checked against direct canonical-rotation counting for k <= 16. At r=k the formula gives 1 via sum phi(d) = k.
- **10.5** A remark that is not used.
- **11** The rank of T_k is k, so r=k. W(k,k) = {1^k} and lambda(1^k) = delta_k. With 1.2, every lambda reaches delta_k.

Unjustified, circular or false steps: none found.

## 3–6. Numerics, equality cases, cross-cell, counterexample search
The two runs are listed in the RAN lines of the block above. Logs:
- out/cex/subject_run_45.log and out/cex/subject_run_45.time (subject code)
- out/cex/check.log and out/cex/check.time (my checker)

Everything uses exact integer arithmetic; there is no floating point anywhere.

For n <= 45, the exhaustive cyclic sets and cycle counts agree with the claimed answer for every (k,r). Examples:
- k=6: counts (1,3,4,3,1,1)
- k=8, r=4: 10 cycles
- k=9, r=3: 10 cycles

No counterexample to any intermediate claim was found.

## 7. Verdict
ACCEPT. The only remarks are the two presentation points listed under OTHER ISSUES.
