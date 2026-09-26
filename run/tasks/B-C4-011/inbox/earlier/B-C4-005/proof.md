Proved: for every k >= 5, D_B(T_{k-1}+1) >= (k-1)(k-3), attained by lambda^(k) = (k-2,k-2,k-3,...,3,2,2,1); and D_B(T_{k-1}+1) <= (k-1)(k-2). The exact upper bound d_B(lambda) <= (k-1)(k-3) is proved only for "near states" (Step 8); for general lambda it is a [GAP]. Equality D_B(T_{k-1}+1) = (k-1)(k-3) is CHECKED by exhaustive exact computation only for 5 <= k <= 11.

Conjectured answer: F(k) = (k-1)(k-3) = k^2 - 4k + 3.

Reading of the brief: none ambiguous. d_B is the entry time into the set of cyclic partitions (d_B = 0 for cyclic ones). Assumptions used: B-C1 and B-C2 exactly as stated in the brief; their hypotheses are checked where used. No LaTeX file was produced (this markdown is the write-up).

---

## 0. Conventions

0.1. Fix k >= 4 and n = T_{k-1} + 1. The diagram of a partition lambda = (lambda_1,...,lambda_s) is the set of cells {(i,j) : 1 <= i <= s, 1 <= j <= lambda_i}. A finite set D of cells in {1,2,...}^2 is the diagram of a partition iff it is closed under (i,j) -> (i-1,j) (for i >= 2) and (i,j) -> (i,j-1) (for j >= 2). Then lambda_i = #{j : (i,j) in D}, the number of parts is s(lambda) = max{i : (i,1) in D}, and lambda_1 = max{j : (1,j) in D}. "lambda subset mu" means diagram containment, i.e. lambda_i <= mu_i for all i (with lambda_i = 0 for i > s(lambda)).

0.2. The diagonal of the cell c = (i,j) is d(c) = i+j-1 and its position is pos(c) = i. Diagonal d consists of the d cells (p, d-p+1), p = 1,...,d. The diagram of delta_m = (m, m-1, ..., 1) is {c : d(c) <= m} (row i of delta_m has m-i+1 cells, i.e. cells (i,j) with i+j-1 <= m).

0.3. For 1 <= p <= k-1 and Q subset {1,...,k} put
D(p,Q) = {c : d(c) <= k-2} u {c : d(c) = k-1, pos(c) != p} u {c : d(c) = k, pos(c) in Q}.
When |Q| = 2 this set has T_{k-2} + (k-2) + 2 = T_{k-1} + 1 = n cells. A partition of n whose diagram is D(p,Q) with |Q| = 2 is called a *near state* (p,Q).

0.4. The rotation of diagonal d is rho_d : {1,...,d} -> {1,...,d}, rho_d(p) = p+1 for p < d, rho_d(d) = 1. It is a bijection.

---

## 1. Lemma C (cyclic partitions of n)

Statement. For k >= 2, a partition lambda of n = T_{k-1}+1 is cyclic iff its diagram contains that of delta_{k-1}.

1.1. B-C1 applies with this k and r = 1 (hypothesis 1 <= r <= k holds). It says: lambda is cyclic iff lambda = lambda(eps) for some eps in {0,1}^k with eps_1 + ... + eps_k = 1, i.e. eps = e_i (the i-th unit vector), 1 <= i <= k. Row j of lambda(e_i) is (k-j) + [j = i] for 1 <= j <= k (row k is deleted when it is 0).

1.2. (=>) Row j of lambda(e_i) is >= k-j, which is row j of delta_{k-1} (j <= k-1). So lambda(e_i) contains delta_{k-1}.

1.3. (<=) Suppose the diagram of lambda contains delta_{k-1}. Since |lambda| = T_{k-1}+1 = |delta_{k-1}|+1, the diagram is delta_{k-1} u {c} for one cell c = (i,j) with d(c) >= k, i.e. i+j >= k+1.
 - If i >= 2: (i-1,j) is in the diagram (0.1) and differs from c, so it lies in delta_{k-1}: i-1+j-1 <= k-1, i.e. i+j <= k+1.
 - If i = 1: then j >= k >= 2, so (1,j-1) is in the diagram and differs from c, so it is in delta_{k-1}: j-1 <= k-1, i.e. i+j = 1+j <= k+1.
 In both cases i+j = k+1, so c = (i, k+1-i) with 1 <= i <= k. Row i of lambda is then (k-i)+1 and every other row j equals k-j; that is lambda = lambda(e_i), which is cyclic by 1.1. QED

---

## 2. Lemma R (the non-sorting step is a rotation of each diagonal)

Statement. Let lambda have s parts and suppose s >= lambda_1 - 1. Then B(lambda) = (s, lambda_1-1, ..., lambda_s-1) with trailing zeros deleted, and the map
phi(i,j) = (i+1, j-1) if j >= 2,   phi(i,1) = (1,i)
is a bijection from the diagram of lambda onto the diagram of B(lambda) with d(phi(c)) = d(c) and pos(phi(c)) = rho_{d(c)}(pos(c)).

2.1. By definition B(lambda) is the partition whose parts are the positive numbers among lambda_1-1, ..., lambda_s-1 together with s. The sequence (s, lambda_1-1, ..., lambda_s-1) is weakly decreasing: s >= lambda_1-1 by hypothesis and lambda_i - 1 >= lambda_{i+1} - 1. Its zero entries (if any) come last. Hence, deleting trailing zeros, it is exactly B(lambda): row 1 of B(lambda) is s and row i+1 is lambda_i - 1.

2.2. phi maps the column {(i,1) : 1 <= i <= s} bijectively onto {(1,i) : 1 <= i <= s}, which is row 1 of B(lambda) (length s). For each i, phi maps {(i,j) : 2 <= j <= lambda_i} bijectively onto {(i+1, j') : 1 <= j' <= lambda_i - 1}, which is row i+1 of B(lambda) (length lambda_i - 1). These pieces partition the two diagrams, so phi is a bijection.

2.3. d(i+1, j-1) = i+j-1 = d(i,j) and d(1,i) = i = d(i,1). For c = (i,j) with j >= 2 we have pos(c) = i < i+j-1 = d(c), and pos(phi(c)) = i+1 = rho_d(i). For c = (i,1) we have pos(c) = i = d(c) and pos(phi(c)) = 1 = rho_d(d). QED

2.4. Consequence. Under the hypothesis of Lemma R, for every d, the set of positions occupied on diagonal d in B(lambda) is the image under rho_d of the set occupied in lambda (phi maps diagonal-d cells of lambda bijectively onto diagonal-d cells of B(lambda)). Since rho_d is a bijection of {1,...,d}, the set of unoccupied positions on diagonal d is also mapped by rho_d.

---

## 3. Lemma S (near-state dynamics)

Statement. Let k >= 4 and let lambda be a partition whose diagram is D(p,Q) (0.3), 1 <= p <= k-1, Q subset {1,...,k}.
 (iii) If p = k-1 then k-1 not in Q and k not in Q.
 (i) s(lambda) <= lambda_1 - 2 holds iff p = k-1 and 1 in Q. Otherwise s(lambda) >= lambda_1 - 1.
 (ii) If s(lambda) >= lambda_1 - 1, then the diagram of B(lambda) is D(rho_{k-1}(p), rho_k(Q)).

3.1. Proof of (iii). The diagonal-k cells at positions k-1 and k are (k-1,2) and (k,1). By 0.1, (k-1,2) in D forces (k-1,1) in D, and (k,1) in D forces (k-1,1) in D. The cell (k-1,1) has diagonal k-1 and position k-1, so it is absent when p = k-1. Hence neither (k-1,2) nor (k,1) is present.

3.2. Proof of (i). Row 1 cells (1,j) have d = j and pos = 1. For j <= k-2 they are in D (k-2 >= 1); for j >= k+1 they are not. So lambda_1 in {k-2, k-1, k}, and lambda_1 = k iff (1,k) in D iff 1 in Q. Column 1 cells (i,1) have d = i and pos = i. For i <= k-2 they are in D; for i >= k+1 they are not. So s in {k-2, k-1, k}, and s = k-2 iff (k-1,1) not in D and (k,1) not in D. Now (k-1,1) not in D iff p = k-1, and then (k,1) is not in D by (iii). So s = k-2 iff p = k-1. Since s >= k-2 and lambda_1 <= k, the inequality s <= lambda_1 - 2 holds iff s = k-2 and lambda_1 = k, i.e. iff p = k-1 and 1 in Q.

3.3. Proof of (ii). By Lemma R and 2.4: diagonals d <= k-2 are full in lambda, so they are full in B(lambda); on diagonal k-1 the unique hole moves from p to rho_{k-1}(p); on diagonal k the occupied set moves from Q to rho_k(Q); diagonals d >= k+1 are empty in lambda, so they are empty in B(lambda). This is D(rho_{k-1}(p), rho_k(Q)). QED

---

## 4. Lemma F (the sorting step of a near state lands on a cycle)

Statement. Let k >= 4 and let lambda be a near state (k-1, Q), so |Q| = 2, and suppose 1 in Q. Then Q = {1, q} with 2 <= q <= k-2, and B(lambda) = lambda(e_{q+1}), which is cyclic.

4.1. By Lemma S(iii), Q subset {1,...,k-2}, so Q = {1,q} with 2 <= q <= k-2.

4.2. Rows of lambda. Row 1: cells (1,j), j <= k-2, are in D; (1,k-1) has pos 1 != k-1 = p, so it is in D; (1,k) is in D as 1 in Q. So lambda_1 = k. Row i with 2 <= i <= k-2: (i,j) with i+j-1 <= k-2 are in D; (i, k-i) has d = k-1 and pos i != k-1, so it is in D; (i, k-i+1) has d = k, pos i, and is in D iff i = q. So lambda_i = k-i+[i = q]. Row k-1: (k-1,1) has d = k-1, pos k-1 = p, so it is absent, and row k-1 is empty. Hence lambda = (k, (k-i+[i=q])_{i=2}^{k-2}) with s = k-2 parts (all positive, since k-i >= 2 for i <= k-2).

4.3. B(lambda) has parts: lambda_1 - 1 = k-1; lambda_i - 1 = k-i-1+[i=q] for 2 <= i <= k-2 (all >= 1); and the new part s = k-2. Listing them as (k-1, k-2, (k-i-1+[i=q])_{i=2}^{k-2}), this list is weakly decreasing: k-1 >= k-2; k-2 >= k-3+[2=q] because [2=q] <= 1; and for 2 <= i <= k-3, (k-i-1+[i=q]) - (k-i-2+[i+1=q]) = 1 + [i=q] - [i+1=q] >= 0. Re-indexing i' = i+1, B(lambda) = (k-1, k-2, (k-i'+[i' = q+1])_{i'=3}^{k-1}). With 3 <= q+1 <= k-1 this is row j = k-j+[j = q+1] for 1 <= j <= k-1 (and no row k), i.e. lambda(e_{q+1}). It is cyclic by 1.1. QED

---

## 5. Theorem L (LOWER bound): d_B(lambda^(k)) = (k-1)(k-3) for every k >= 5

5.1. Definition. lambda^(k)_1 = k-2; lambda^(k)_i = k-i for 2 <= i <= k-2; lambda^(k)_{k-1} = 2; lambda^(k)_k = 1. (k = 5: (3,3,2,2,1); k = 6: (4,4,3,2,2,1); k = 8: (6,6,5,4,3,2,2,1).) It is weakly decreasing because k-2 >= k-2 > ... > 2 >= 2 > 1 (row k-2 equals 2). Its sum is (k-2) + (T_{k-2} - 1) + 2 + 1 = T_{k-2} + k = T_{k-1} + 1 = n.

5.2. lambda^(k) is the near state (1, {k-1, k}). Row 1 = {(1,j): j <= k-2}: all cells of diagonals <= k-2 in row 1, and (1,k-1) (diagonal k-1, position 1) missing. Rows 2 <= i <= k-2 have k-i cells, i.e. exactly the cells (i,j) with d <= k-1, and no diagonal-k cell. Row k-1 = {(k-1,1), (k-1,2)}: (k-1,1) has d = k-1, pos k-1 != 1; (k-1,2) has d = k, pos k-1. Row k = {(k,1)}: d = k, pos k. Every cell of diagonal <= k-2 lies in rows 1..k-2 and has been listed; every cell of diagonal k-1 except position 1 has been listed. So the diagram is D(1, {k-1,k}).

5.3. Define, for t >= 0, p_t = 1 + (t mod (k-1)) and Q_t = {1 + ((t+k-2) mod k), 1 + ((t+k-1) mod k)}. Then (p_0, Q_0) = (1, {k-1, k}), p_{t+1} = rho_{k-1}(p_t) and Q_{t+1} = rho_k(Q_t) (since rho_d(1 + (x mod d)) = 1 + ((x+1) mod d)).

5.4. The "sorting condition" C(t): p_t = k-1 and 1 in Q_t. It holds iff t ≡ -1 (mod k-1) and (t+k-2 ≡ 0 or t+k-1 ≡ 0 (mod k)), i.e. iff t ≡ -1 (mod k-1) and t ≡ 2 or 1 (mod k). Since gcd(k-1,k) = 1, by the Chinese remainder theorem each of the two pairs of congruences has exactly one solution in [0, k(k-1)):
 - t ≡ -1 (mod k-1), t ≡ 2 (mod k): t_1 = (k-1)(k-3) - 1 = k^2-4k+2. Check: t_1 = (k-1)(k-3) - 1 ≡ -1 (mod k-1); t_1 = k(k-4) + 2 ≡ 2 (mod k); 0 <= t_1 < k(k-1) for k >= 4.
 - t ≡ -1 (mod k-1), t ≡ 1 (mod k): t_2 = k^2-3k+1. Check: t_2 = (k-1)(k-2) - 1 ≡ -1 (mod k-1); t_2 = k(k-3)+1 ≡ 1 (mod k); 0 <= t_2 < k(k-1).
 Since t_2 - t_1 = k-1 > 0, the least t >= 0 with C(t) is t* = t_1 = (k-1)(k-3) - 1.

5.5. Claim: for 0 <= t <= t*, B^t(lambda^(k)) is the near state (p_t, Q_t). Induction on t. t = 0 is 5.2. If it holds for t < t*, then C(t) fails (5.4), so by Lemma S(i) s >= lambda_1 - 1 for B^t(lambda^(k)), and by Lemma S(ii) and 5.3 B^{t+1}(lambda^(k)) has diagram D(p_{t+1}, Q_{t+1}).

5.6. For 0 <= t <= t*, B^t(lambda^(k)) is not cyclic: its diagram lacks the diagonal-(k-1) cell at position p_t, which belongs to delta_{k-1}; apply Lemma C.

5.7. At t*, C(t*) holds: p_{t*} = k-1 and Q_{t*} contains 1. So B^{t*}(lambda^(k)) is a near state (k-1, Q) with 1 in Q, and by Lemma F, B^{t*+1}(lambda^(k)) is cyclic. (Explicitly: t* + k - 2 = k^2 - 3k ≡ 0 (mod k), so Q_{t*} = {1,2}, and B^{t*+1}(lambda^(k)) = lambda(e_3) = (k-1, k-2, k-2, k-4, k-5, ..., 1).)

5.8. By 5.6 and 5.7, d_B(lambda^(k)) = t* + 1 = (k-1)(k-3). Hence D_B(T_{k-1}+1) >= (k-1)(k-3) for every k >= 5 (indeed for every k >= 4, but at k = 4 the true value is larger, see Step 9). QED

---

## 6. Lemma M (monotonicity of B under containment)

Statement. If lambda subset mu then B(lambda) subset B(mu). Hence B^t(lambda) subset B^t(mu) for all t >= 0.

6.1. Let N >= s(mu) and define a_0 = s(lambda), a_i = max(lambda_i - 1, 0) (1 <= i <= N), b_0 = s(mu), b_i = max(mu_i - 1, 0). From lambda_i <= mu_i for all i we get s(lambda) <= s(mu) and a_i <= b_i for all 0 <= i <= N. By definition, the parts of B(lambda) are the positive entries of (a_0,...,a_N) and B(lambda)_j is the j-th largest entry of this sequence (0 if j exceeds the number of positive entries); likewise for B(mu) with b.

6.2. Fact: if a_i <= b_i for all i, then for each j the j-th largest entry of a is <= the j-th largest entry of b. Proof: let I be a set of j indices carrying the j largest entries of a, and let x be the j-th largest entry of a. For i in I, b_i >= a_i >= x, so b has at least j entries >= x, hence its j-th largest entry is >= x.

6.3. Thus B(lambda)_j <= B(mu)_j for all j, i.e. B(lambda) subset B(mu). Induction on t gives the second sentence. QED

---

## 7. Corollary U1 (a weaker upper bound valid for all k)

Statement. Let k >= 3 and lambda |- n = T_{k-1}+1. For every cell c whose removal leaves a partition nu = lambda \ c of T_{k-1}, d_B(lambda) <= d_B(nu). Consequently d_B(lambda) <= (k-1)(k-2), i.e. D_B(T_{k-1}+1) <= (k-1)(k-2).

7.1. The cyclic partitions of T_{k-1}. Apply B-C1 with k' = k-1 >= 1 and r = k' (so n' = T_{k'-1} + k' = T_{k-1}; hypothesis 1 <= r <= k' holds). Then eps_1 + ... + eps_{k'} = k' forces eps = (1,...,1), so the only cyclic partition is lambda(1,...,1) = (k-1, k-2, ..., 1) = delta_{k-1}.

7.2. Let d = d_B(nu). Then B^d(nu) is cyclic, hence equals delta_{k-1} by 7.1. By Lemma M (nu subset lambda), delta_{k-1} = B^d(nu) subset B^d(lambda). By Lemma C, B^d(lambda) is cyclic, so d_B(lambda) <= d.

7.3. A cell c as required exists: take c = (s, lambda_s), the last cell of the last row. By B-C2 applied at k-1 >= 1 (T_{k-1} is triangular with index k-1), d_B(nu) <= D_B(T_{k-1}) = (k-1)^2 - (k-1) = (k-1)(k-2). QED

Remark. (k-1)(k-2) exceeds the conjectured F(k) = (k-1)(k-3) by k-1. The inequality d_B(lambda) <= min_c d_B(lambda \ c) is not enough by itself: at k = 6 there are 26 partitions of 16 all of whose one-cell removals nu have d_B(nu) > 15 (exploratory computation, out/tmp/reduce.py; not load-bearing).

---

## 8. Theorem N (exact upper bound for near states)

Statement. Let k >= 5 and let lambda be a near state (p, Q), |Q| = 2. Then d_B(lambda) <= (k-1)(k-3).

8.1. Let a = k-1-p, so 0 <= a <= k-2 and rho_{k-1}^a(p) = k-1, while rho_{k-1}^t(p) != k-1 for 0 <= t < a.

8.2. For 0 <= t <= a, B^t(lambda) is the near state (rho_{k-1}^t(p), rho_k^t(Q)): induction; for t < a the hole is not at k-1, so Lemma S(i) gives no sorting and Lemma S(ii) gives the next state.

8.3. At time a the state is (k-1, Q_a), Q_a = rho_k^a(Q). By Lemma S(iii), Q_a subset {1,...,k-2}. Let r = min Q_a; since Q_a has two distinct elements in {1,...,k-2}, 1 <= r <= k-3.

8.4. Claim: for 0 <= t <= a + (k-1)(r-1), B^t(lambda) is the near state (rho_{k-1}^t(p), rho_k^t(Q)), and sorting (condition p_t = k-1 and 1 in Q_t, Lemma S(i)) does not occur for t < a + (k-1)(r-1). Proof by induction on t, the inductive step being Lemma S(ii) whenever the sorting condition fails at t. The hole is at k-1 exactly at times t = a + (k-1)j (j >= 0), because rho_{k-1} has order k-1. At such a time, rho_k^t(Q) = rho_k^{(k-1)j}(Q_a), and rho_k^{k-1} = rho_k^{-1} (rho_k has order k), so rho_k^t(Q) = {x - j (mod k, in 1..k) : x in Q_a}. This contains 1 iff x - j ≡ 1 (mod k) for some x in Q_a, i.e. j ≡ x - 1 (mod k). For x in Q_a, x - 1 lies in {0,...,k-3}, so the least j >= 0 with j ≡ x-1 (mod k) is j = x - 1. Hence the least j at which the sorting condition holds is j = min_{x in Q_a}(x - 1) = r - 1, and it holds at t_s = a + (k-1)(r-1) and at no earlier time.

8.5. At t_s the state is a near state (k-1, Q') with 1 in Q', so by Lemma F, B^{t_s + 1}(lambda) is cyclic. Therefore
d_B(lambda) <= t_s + 1 = a + (k-1)(r-1) + 1 <= (k-2) + (k-1)(k-4) + 1 = (k-1)(k-3).
(In fact equality d_B(lambda) = t_s + 1 holds, since every near state lacks a cell of delta_{k-1} and so is not cyclic by Lemma C; and the bound is attained exactly when a = k-2 (i.e. p = 1) and Q_a = {k-3, k-2}, i.e. Q = rho_k^{-(k-2)}({k-3,k-2}) = rho_k^{2}({k-3,k-2}) = {k-1,k}; this is lambda^(k) of Theorem L.) QED

8.6. Consistency check: Theorem N gives an independent derivation of the lower-bound value, since lambda^(k) is the near state (1,{k-1,k}) with a = k-2, r = k-3, so d_B = (k-2) + (k-1)(k-4) + 1 = (k-1)(k-3).

---

## 9. What is and is not established; finite evidence

9.1. Established for every k >= 5:
 - LOWER: D_B(T_{k-1}+1) >= (k-1)(k-3), witnessed by lambda^(k) (Theorem L), orbit tracked symbolically in k.
 - UPPER (weak): D_B(T_{k-1}+1) <= (k-1)(k-2) (Corollary U1, using B-C1 and B-C2).
 - UPPER (exact, restricted class): d_B(lambda) <= (k-1)(k-3) for every near state (Theorem N).

9.2. NOT established: d_B(lambda) <= (k-1)(k-3) for all partitions lambda of T_{k-1}+1 and all k >= 5. [GAP] The missing step is a reduction showing that any partition either becomes cyclic, or enters the near-state class (or another class with an explicit exact bound) with its remaining time compensating the transient; Theorem N plus Corollary U1 only give d_B(lambda) <= min((k-1)(k-2), t_0 + (k-1)(k-3)) where t_0 is the entry time into near states. See out/stuck.md.

9.3. CHECKED (finite, exact integer computation, out/code/check.py): for each k = 5, 6, ..., 11, over ALL partitions of T_{k-1}+1, the maximum of d_B equals (k-1)(k-3) (values 8, 15, 24, 35, 48, 63, 80); the cyclic set found by direct cycle detection coincides with the B-C1 description; d_B(lambda^(k)) = (k-1)(k-3); every near state has d_B <= (k-1)(k-3). Also, direct simulation of the orbit of lambda^(k) gives d_B = (k-1)(k-3) for k = 5..80. These finite checks prove nothing for other k; they only corroborate the conjectured formula F(k) = (k-1)(k-3) and the symbolic orbit of Step 5.

9.4. Edge values outside the target range: k = 3 (n = 4) gives D_B = 2 and k = 4 (n = 7) gives D_B = 4 (maximiser (1^7)), whereas (k-1)(k-3) = 0 and 3. So the formula genuinely needs k >= 5; any complete upper-bound proof must use k >= 5 somewhere (Theorem N itself holds for k >= 4, so the failure at k = 4 comes from non-near states).
