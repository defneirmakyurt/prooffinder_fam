Proved here: for every k >= 3 and every partition lambda of n = T_{k-1}+1, d_B(lambda) <= (k-1)(k-2) = F(k) + (k-1), where F(k) = (k-1)(k-3); this uses one cited published theorem (D_B(T_m) = m^2-m with unique fixed point delta_m; Step 4). The TARGET d_B(lambda) <= (k-1)(k-3) for all lambda and all k >= 5 is NOT proved here [GAP, Step 7]; it is exactly the r = 1 case of Griggs-Ho (1998) Conjecture 4.7, and no proof was found in the literature searched (sources.md).

Reading of the brief: TARGET is the upper half only. "ASSUMPTIONS: none beyond the statement" is read as: nothing from other cells of this problem may be assumed; published theorems about other statements may be cited with a precise reference, and are marked CITED. No blind-run proof is copied; comparison is in divergence.md.

---

## 1. Conventions

1.1. The diagram of lambda = (lambda_1 >= ... >= lambda_s > 0) is Y(lambda) = {(i,j) : 1 <= i <= s, 1 <= j <= lambda_i}. Put lambda_i = 0 for i > s. Write lambda <= mu (containment) if lambda_i <= mu_i for all i >= 1, i.e. Y(lambda) is a subset of Y(mu).

1.2. A finite set S of cells in Z_{>0}^2 is a diagram of a partition iff it is closed: (i,j) in S, i >= 2 implies (i-1,j) in S, and (i,j) in S, j >= 2 implies (i,j-1) in S. (If S is closed, row i of S is {1,...,r_i}, and if r_{i+1} >= 1 then (i+1, r_{i+1}) in S forces (i, r_{i+1}) in S, so r_i >= r_{i+1}; conversely left-justified rows of weakly decreasing length are closed.)

1.3. The diagonal of (i,j) is i+j-1. Y(delta_m) = {(i,j) : i+j-1 <= m}, since row i of delta_m = (m, m-1, ..., 1) has m-i+1 cells.

## 2. Monotonicity (Akin-Davis, as proved in Griggs-Ho 1998, Theorem 4.1) — re-derived in full

Lemma 2. If lambda <= mu then B(lambda) <= B(mu); hence B^t(lambda) <= B^t(mu) for all t >= 0.

2.1. Let s = s(lambda), s' = s(mu). Since lambda_i <= mu_i for all i, s <= s' (lambda_{s} >= 1 forces mu_s >= 1). Fix N >= s' and put a_0 = s, a_i = max(lambda_i - 1, 0), b_0 = s', b_i = max(mu_i - 1, 0) for 1 <= i <= N. Then a_i <= b_i for 0 <= i <= N. By the definition of B, B(lambda)_j is the j-th largest entry of (a_0, ..., a_N) (zero if there are fewer than j positive entries), and likewise B(mu)_j with b. (The zero entries of a correspond to discarded empty piles, and entries for i > s are 0.)

2.2. Fact: if a_i <= b_i for all i then for every j the j-th largest entry of a is <= the j-th largest entry of b. Proof: let I be a set of j indices carrying the j largest entries of a and let x be the smallest of them (the j-th largest entry of a). For i in I, b_i >= a_i >= x, so b has at least j entries >= x, so its j-th largest entry is >= x.

2.3. Hence B(lambda)_j <= B(mu)_j for every j, i.e. B(lambda) <= B(mu). Induction on t gives the second claim. QED

## 3. Partitions of T_{k-1}+1 containing delta_{k-1} are cyclic — proved in full

Lemma 3. Let k >= 2, n = T_{k-1}+1, and lambda a partition of n with delta_{k-1} <= lambda. Then lambda is cyclic.

3.1. |Y(lambda)| = |Y(delta_{k-1})| + 1, so Y(lambda) = Y(delta_{k-1}) together with one cell c = (i,j), i+j-1 >= k. If i >= 2, then (i-1,j) is in Y(lambda) and differs from c, so it lies in Y(delta_{k-1}): i+j-2 <= k-1. If i = 1 then j >= k >= 2, so (1,j-1) is in Y(delta_{k-1}): j-1 <= k-1, i.e. i+j-1 <= k. In both cases i+j-1 = k, so c = (j', k+1-j') for some j' in {1,...,k}.

3.2. For j in {1,...,k} let gamma_j be the partition with rows gamma_j(i) = (k-i) + [i = j] for 1 <= i <= k (row k is [j = k]; drop it if 0). By 3.1, lambda = gamma_{j'}.

3.3. B(gamma_j) = gamma_{j+1} for 1 <= j <= k-1, and B(gamma_k) = gamma_1.
 - Case j <= k-1. gamma_j has s = k-1 parts (row k-1 is 1 + [j = k-1] >= 1, row k is 0). The piles minus one are k-1-i+[i=j], 1 <= i <= k-1 (the entry for i = k-1 is [j = k-1], dropped if 0), and the new pile is k-1. The list (k-1, (k-1-i+[i=j])_{i=1}^{k-1}) is weakly decreasing: k-1 >= k-2+[1=j]; and for 1 <= i <= k-2, (k-1-i+[i=j]) - (k-2-i+[i+1=j]) = 1 + [i=j] - [i+1=j] >= 0. Re-indexing i' = i+1, its i'-th entry is k-i'+[i' = j+1] for 1 <= i' <= k (for i' = 1: k-1 = k-1+[1 = j+1] since j+1 >= 2). This is gamma_{j+1}.
 - Case j = k. gamma_k = (k-1, k-2, ..., 1, 1) has s = k parts. The piles minus one are k-2, ..., 1, 0, 0; dropping zeros and adding the new pile k gives (k, k-2, k-3, ..., 1), whose row 1 is k-1+1 and row i is k-i for 2 <= i <= k-1. This is gamma_1.

3.4. Hence B^k(gamma_j) = gamma_j with k >= 1, so every gamma_j, in particular lambda, is cyclic. QED

## 4. Cited theorem (not re-proved here)

Theorem 4 [CITED]. For every m >= 1 and every partition nu of T_m, B^{m^2-m}(nu) = delta_m.

Source: Griggs-Ho 1998, Theorem 3.7 (D_B(T_m) = m^2-m; attributed to Igusa 1985 and Etienne 1991) together with Corollary 2.2 (Brandt: delta_m is the unique cyclic partition of T_m). Griggs-Ho state exactly this consequence in the proof of their Theorem 4.2 ("Theorem 3.7 gives B^{(k^2-k)}(nu) = (k-1, k-2, ..., 2, 1)"). Derivation of the displayed form: by Thm 3.7, B^d(nu) is cyclic for d = d_B(nu) <= m^2-m; by Cor. 2.2 it equals delta_m; B(delta_m) = delta_m (piles minus one are m-1, ..., 1, 0 and the new pile is m); so B^{m^2-m}(nu) = delta_m. Status: PROVED in the source, argument contained there (opened, pp. 9-12); not re-derived here.

## 5. Upper bound (k-1)(k-2) — proved (modulo Theorem 4)

Proposition 5. Let k >= 3, n = T_{k-1}+1. (a) For every partition lambda of n and every cell c such that nu = Y(lambda) minus c is a diagram (a partition of T_{k-1}), d_B(lambda) <= d_B(nu). (b) d_B(lambda) <= (k-1)(k-2) for every partition lambda of n.

5.1. (b) from (a) and Theorem 4 with m = k-1: take c = (s, lambda_s), the last cell of the last row; removing it keeps the set closed (no cell of Y(lambda) lies to its right or below it). Then d_B(nu) <= (k-1)^2 - (k-1) = (k-1)(k-2).

5.2. Proof of (a). Let d = d_B(nu). B^d(nu) is cyclic, so equals delta_{k-1} (Theorem 4's derivation: it is a cyclic partition of T_{k-1}, and Cor. 2.2). Since nu <= lambda, Lemma 2 gives delta_{k-1} = B^d(nu) <= B^d(lambda). By Lemma 3, B^d(lambda) is cyclic. Hence d_B(lambda) <= d. QED

## 6. Comparison with the published non-triangular upper bounds

6.1. Griggs-Ho Theorem 4.2 gives D_B(n) <= k^2-k and Theorem 4.4(1) gives D_B(n) <= k^2-2k-1 for all non-triangular n of rank k >= 4. At r = 1: (k^2-2k-1) - (k-1)(k-2) = k-3 >= 1 for k >= 4. So for the family n = T_{k-1}+1 the best published general upper bound that I opened is weaker than Proposition 5(b), which in turn exceeds the target F(k) = (k-1)(k-3) by exactly k-1.

6.2. The Griggs-Ho machinery (part-count sequence seq_B(lambda) = <c_1, c_2, ...>, c_i = number of parts of B^{i-1}(lambda); Prop. 3.2: c_{i+1} <= c_i + 1, any k consecutive terms sum to <= k(k-1)+r, sandwich property; Lemmas 3.3-3.6, 4.3) bounds d_B by (position of a "sandwich" pattern x-1, x, ..., x, x+1) + k, with the position controlled by a descent through shorter patterns (Lemma 3.5, each step moving back by at most x). At r = 1 the final pattern has x = k or x = k-1 and length up to k, and the descent gives about (k-1)x before it, i.e. k^2 - O(k); to reach (k-1)(k-3) = k^2-4k+3 one would have to save about 2k-4 steps over Theorem 4.4, using r = 1 (sum of k consecutive c's <= k^2-k+1) much more sharply than Prop. 3.2(2) does. I did not find or construct such a refinement.

## 7. [GAP] The target upper bound

Not proved: d_B(lambda) <= (k-1)(k-3) for every partition lambda of T_{k-1}+1 and every k >= 5.

7.1. Status in the literature (sources.md): this is the r = 1 instance of Griggs-Ho Conjecture 4.7 (their Lower Bound Theorem 4.5 case (1) at r = 1 gives the value (k-3-1)k+1+2 = (k-1)(k-3) with the same witness as the blind runs). Griggs-Ho report it confirmed for n <= 36 (k <= 8 at r = 1), code not public. Hopkins (2012) lists the Griggs-Ho maximal lengths among open questions; Eriksson-Jonsson (2017) still call them conjectured. No later proof found (sources searched listed in sources.md). Etienne 1991 and Igusa 1985 were not opened.

7.2. Static monotonicity cannot close the gap (evidence, exact computation, out/code/corner_obstruction.py, not load-bearing): for k = 6, 7, 8, 9, 10 there are 26, 146, 894, 4927, 27660 partitions lambda of T_{k-1}+1 all of whose one-cell removals nu have d_B(nu) > (k-1)(k-3), and max over lambda of min over removals of d_B(nu) equals (k-1)(k-2) for each of these k. So Proposition 5(a) alone cannot improve Proposition 5(b) by even one step for 6 <= k <= 10. (At k = 5 the maximum of min_nu d_B(nu) is 8 = F(5).)

7.3. Finite evidence (exact, out/code/check_r1.py, not a proof for any k outside the range): for 5 <= k <= 12, max d_B over all partitions of T_{k-1}+1 equals (k-1)(k-3); the cyclic set is {gamma_1, ..., gamma_k}; lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1) attains the maximum; numbers of maximisers 3, 12, 62, 288, 1310, 5862, 26399, 119871. The same script reproduces Griggs-Ho Figure 1 (D_B(n), n <= 36). This proves D_B(T_{k-1}+1) = (k-1)(k-3) only for 5 <= k <= 12, given the lower-bound witness.

## 8. What is established

- PROVED (full): Lemma 2 (monotonicity), Lemma 3 (containment of delta_{k-1} implies cyclic; the cycle gamma_1 -> ... -> gamma_k -> gamma_1).
- PROVED modulo the CITED Theorem 4 (Griggs-Ho Thm 3.7 + Cor. 2.2): D_B(T_{k-1}+1) <= (k-1)(k-2) for all k >= 3, and d_B(lambda) <= min over removable cells c of d_B(lambda minus c).
- COMPUTER-VERIFIED (exact, code in out/code): target equality for 5 <= k <= 12 only.
- NOT established: the target upper bound for general k >= 5 (in particular for k >= 13).
