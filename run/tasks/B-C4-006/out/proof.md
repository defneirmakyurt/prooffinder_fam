**Proved:** For every k >= 5, with n = T_{k-1}+1: (LOWER) the partition λ^(k) = (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1) of n satisfies d_B(λ^(k)) = (k-1)(k-3), hence D_B(T_{k-1}+1) >= (k-1)(k-3); (UPPER, partial) every partition λ of n with E(λ) <= E_min + 1 (energy defined in Step 2) satisfies d_B(λ) <= (k-1)(k-3). The upper bound for ALL partitions of n is NOT proved here ([GAP], Step 14).

Conjectured value: D_B(T_{k-1}+1) = F(k) := (k-1)(k-3) = (k-2)^2 - 1 for all k >= 5. Exhaustive computation (out/code/check.py) confirms it for k = 5..11 only. That is evidence, not proof.

Reading of the brief: none needed. Definitions are as in inbox/statement.md. d_B is the time to ENTER the set of cyclic partitions. The new pile has size s = number of piles before the move, and it is sorted into place.

Assumptions used (gated, from the brief): **B-C1**, applied with r = 1 (so eps has exactly one 1). Its hypotheses: n = T_{k-1} + r with 1 <= r <= k, k >= 1; here r = 1 and k >= 5, so they hold. In that case the cyclic partitions of n are exactly λ(e_j), j = 1..k. Here λ(e_j) is the staircase (k-1, k-2, ..., 1) with 1 added to entry j, and for j = k it is (k-1, ..., 1, 1). **B-C2** is not used.

---

## Setup

**Step 0 (Cyclic set is forward invariant).** If ν is cyclic, say B^i(ν) = ν with i >= 1, then B^i(B(ν)) = B(B^i(ν)) = B(ν), so B(ν) is cyclic. So if B^t(λ) is cyclic, B^{t'}(λ) is cyclic for all t' >= t. Consequently, for an integer m >= 1, d_B(λ) = m iff B^{m-1}(λ) is not cyclic and B^m(λ) is cyclic.

**Step 1 (Diagram criterion, R1).** The diagram of a partition λ = (λ_1, ..., λ_s) is diag(λ) = {(i,j) : 1 <= i <= s, 1 <= j <= λ_i}. Claim: a finite set S of cells (i,j) in Z_{>0}^2 equals diag(λ) for some partition λ iff it satisfies
(C) whenever (i,j) ∈ S: if j >= 2 then (i,j-1) ∈ S, and if i >= 2 then (i-1,j) ∈ S.
*Proof.* (⇒) Let (i,j) ∈ diag(λ), so j <= λ_i. If j >= 2 then j-1 <= λ_i, so (i,j-1) ∈ diag(λ). If i >= 2 then λ_{i-1} >= λ_i >= j, so (i-1,j) ∈ diag(λ).
(⇐) Let r_i = #{j : (i,j) ∈ S}. By the first half of (C), row i of S is {1, ..., r_i}. If r_i >= 1 and i >= 2, then (i, r_i) ∈ S, so (i-1, r_i) ∈ S by (C), and therefore r_{i-1} >= r_i. So (r_1, r_2, ...) is weakly decreasing, and its positive entries r_1 >= ... >= r_s > 0 occupy rows 1..s. Hence S = diag(r_1, ..., r_s). ∎

**Step 2 (Diagonals, energy).** For a cell (i,j) put h(i,j) = i+j-1. Let D_d = {(i, d+1-i) : 1 <= i <= d} (so |D_d| = d). The **position** of (i, d+1-i) in D_d is i-1 ∈ {0, ..., d-1}. If a cell (i,j) ∈ D_d has i >= 2 or j >= 2, then the neighbours (i-1,j) and (i,j-1) named in (C) lie in D_{d-1}. For λ ⊢ n let o_d(λ) = |diag(λ) ∩ D_d| (so 0 <= o_d <= d) and E(λ) = Σ_{(i,j) ∈ diag λ} h(i,j) = Σ_d d·o_d(λ). For a finitely supported sequence r = (r_1, r_2, ...) of non-negative integers, define the cell set S(r) = {(i,j) : 1 <= j <= r_i} and E(r) = Σ_{(i,j) ∈ S(r)} h(i,j) = Σ_i ( i·r_i + r_i(r_i-1)/2 ).

**Step 3 (Rigid rotation, R2).** Let λ = (λ_1, ..., λ_s) and define the sequence R(λ) = (s, λ_1 - 1, λ_2 - 1, ..., λ_s - 1, 0, 0, ...). By the definition of B, B(λ) is the weakly decreasing rearrangement of the positive entries of R(λ). Define ρ on cells by ρ(i,j) = (i+1, j-1) if j >= 2 and ρ(i,1) = (1,i).
(a) ρ maps diag(λ) bijectively onto S(R(λ)). The first column {(i,1) : i <= s} goes bijectively onto row 1 {(1,i) : i <= s}. For each i, the cells (i,j) with 2 <= j <= λ_i go bijectively onto {(i+1, j') : 1 <= j' <= λ_i - 1}, which is row i+1 of S(R(λ)). These pieces partition diag(λ) and S(R(λ)) respectively. ρ is injective on each piece, and the images are disjoint because they lie in different rows.
(b) h(ρ(c)) = h(c) for every cell c: h(i+1, j-1) = i+j-1 and h(1,i) = i = h(i,1). Hence E(R(λ)) = E(λ).
(c) On D_d, ρ sends position p to position p+1 mod d. For p <= d-2 the cell (p+1, d-p) has column d-p >= 2 and goes to (p+2, d-p-1), at position p+1. For p = d-1 the cell (d,1) goes to (1,d), at position 0.
In particular, if D_d ⊆ diag(λ) then D_d ⊆ ρ(diag λ).

**Step 4 (Rigid step or energy drop, R3).** Let a_i = λ_i - 1.
(a) If λ_1 <= s+1: R(λ) = (s, a_1, a_2, ...) is weakly decreasing, since s >= a_1 >= a_2 >= ... . So B(λ) is the sequence of positive entries of R(λ), diag B(λ) = S(R(λ)) = ρ(diag λ), and E(B(λ)) = E(λ) by Step 3(b).
(b) If λ_1 >= s+2: (2, s+1) ∈ S(R(λ)) because row 2 has length a_1 >= s+1, but (1, s+1) ∉ S(R(λ)) because row 1 has length s. So S(R(λ)) fails (C) and is not a diagram (Step 1). Let q = #{i : a_i > s} >= 1. The sequence r' = (a_1, ..., a_q, s, a_{q+1}, ..., a_s, 0, ...) is weakly decreasing (a_q > s >= a_{q+1}), so its positive entries form B(λ). Now r' and R(λ) have the same multiset of entries. So Σ r_i(r_i-1)/2 is the same for both, and
Σ_i i·r'_i - Σ_i i·R(λ)_i = [Σ_{i<=q} i·a_i + (q+1)s] - [s + Σ_{i<=q} (i+1)a_i] = -Σ_{i<=q} (a_i - s) <= -1.
Hence E(B(λ)) = E(r') <= E(R(λ)) - 1 = E(λ) - 1.
(c) Summary: ρ(diag λ) is a diagram iff λ_1 <= s+1, and in that case diag B(λ) = ρ(diag λ). Otherwise E(B(λ)) <= E(λ) - 1.

## Energy levels for n = T_{k-1}+1 (k >= 5)

**Step 5 (Energy decomposition, R4).** Let E_min = Σ_{d=1}^{k-1} d^2 + k and ε(λ) = E(λ) - E_min. Put h_d = d - o_d >= 0 for d <= k-1, and X = Σ_{d>=k} o_d. Since Σ_d o_d = n = Σ_{d<=k-1} d + 1, we get Σ_{d<=k-1} h_d = X - 1. In particular X >= 1. Then
Σ_{d<=k-1} d·h_d = (k-1)(X-1) - Σ_{d<=k-1} (k-1-d) h_d,
and so
ε(λ) = Σ_{d>=k} d·o_d - k - Σ_{d<=k-1} d·h_d = [ Σ_{d>=k} (d-k+1) o_d - 1 ] + Σ_{d<=k-1} (k-1-d) h_d.
The first bracket is >= X - 1 >= 0, since d-k+1 >= 1 for d >= k. The second sum is >= 0. So ε >= 0.

**Step 6 (Level 0 is the cycle, R5).** ε(λ) = 0 iff both parts of Step 5 vanish. The first vanishes iff o_k = 1 and o_d = 0 for all d > k. Then X = 1, so every h_d = 0, which makes the second sum vanish too. So ε = 0 iff diag(λ) = D_1 ∪ ... ∪ D_{k-1} ∪ {(j, k+1-j)} for some j ∈ {1, ..., k}. Such a set has rows k-i+[i=j] for i <= k-1 and row k equal to [j=k], i.e. it is λ(e_j). Conversely diag λ(e_j) is such a set. By B-C1 (r = 1): **ε(λ) = 0 iff λ is cyclic.**

**Step 7 (Level 1 occupancy, R6a).** Claim: ε(λ) = 1 iff D_1, ..., D_{k-2} ⊆ diag(λ), o_{k-1} = k-2, o_k = 2 and o_d = 0 for d > k.
*Proof.* If the second part of Step 5 were 1, the first part would be 0. By Step 6 that forces X = 1 and all h_d = 0, so the second part would be 0, a contradiction. Hence the second part is 0 and the first part is 1. A second part of 0 means h_d = 0 for all d <= k-2. A first part of 1 means Σ_{d>=k} (d-k+1) o_d = 2. So either (i) o_k = 2 and o_d = 0 for d > k (X = 2, and then h_{k-1} = 1), or (ii) o_k = 0, o_{k+1} = 1 and o_d = 0 for d > k+1 (X = 1, no holes). In case (ii) the cell c = (i,j) ∈ D_{k+1} has i + j = k+2 >= 3, so i >= 2 or j >= 2. By Step 2 the neighbour required by (C) lies in D_k, which is empty, so (C) fails, contradicting Step 1. Hence (i) holds. Conversely, in configuration (i) the first part of Step 5 is 1·2 - 1 = 1 and the second part is (k-1-(k-1))·1 = 0, so ε = 1. ∎

**Step 8 (Level-1 coordinates, R6b).** A level-1 cell set is determined by a triple (Q; P, P') with 0 <= Q <= k-2 and 0 <= P < P' <= k-1. Here Q is the position of the missing cell of D_{k-1}, and P, P' are the positions of the two cells of D_k. Claim: this cell set is a diagram iff **P, P' ∉ {Q, Q+1}** (the "constraint").
*Proof.* Check (C) cell by cell. Take a cell of D_d with d <= k-1 and i >= 2 (resp. j >= 2). Its required neighbour lies in D_{d-1}, which is full because d-1 <= k-2. The cell of D_k at position P is (P+1, k-P). Its upper neighbour (P, k-P) is required iff P >= 1, and it is the cell of D_{k-1} at position P-1. Its left neighbour (P+1, k-P-1) is required iff P <= k-2, and it is the cell of D_{k-1} at position P. The only missing cell of D_{k-1} is at position Q ∈ {0..k-2}. So (C) holds at this cell iff Q ≠ P-1 and Q ≠ P. (When P = 0, Q = P-1 is impossible. When P = k-1, Q = P is impossible, since Q <= k-2.) Equivalently, P ∉ {Q, Q+1}. ∎
Combined with Step 7, the partitions λ ⊢ n with ε(λ) = 1 are in bijection with the triples satisfying the constraint. None of them is cyclic (Step 6).

**Step 9 (Rotation of a triple).** Let λ be at level 1 with triple (Q; P, P'). By Step 3(c), ρ(diag λ) contains D_1, ..., D_{k-2}. It misses exactly the cell of D_{k-1} at position Q+1 mod (k-1), and it meets D_k exactly at positions P+1 mod k and P'+1 mod k. No other cells occur, because ρ preserves h and is a bijection onto its image. So ρ(diag λ) is the cell set with triple (Q+1 mod (k-1); P+1 mod k, P'+1 mod k), which is a diagram iff this triple satisfies the constraint (Step 8).

**Step 10 (d_B on level 1, R7).** Let λ be at level 1 with triple c_0 = (Q; P, P'). Put c_t = (Q+t mod (k-1); P+t mod k, P'+t mod k), and let T = min{t >= 1 : c_t violates the constraint}. Step 12 shows T is finite. Claim: **d_B(λ) = T**.
*Proof.* By induction on t, for 0 <= t <= T-1, B^t(λ) is the level-1 partition with triple c_t. For t = 0 this holds by definition. Suppose it holds for some t <= T-2. By Step 9, ρ(diag B^t λ) has triple c_{t+1}, which satisfies the constraint because t+1 < T, so it is a diagram. By Step 4(c) diag B^{t+1}(λ) = ρ(diag B^t λ), which proves the case t+1. Now take t = T-1. ρ(diag B^{T-1} λ) has triple c_T, which violates the constraint, so it is not a diagram. By Step 4(c), E(B^T λ) <= E(B^{T-1} λ) - 1 = E_min. By Step 5 then ε(B^T λ) = 0, so B^T(λ) is cyclic by Step 6. Each B^t(λ) with t <= T-1 is at level 1 and hence not cyclic. By Step 0, d_B(λ) = T. ∎

**Step 11 (Lap lemma, R8).** Let t_0 = (k-1-Q) mod (k-1) ∈ {0, ..., k-2}, so that Q + t_0 ≡ 0 (mod k-1). For an integer t >= 0 write t - t_0 = a(k-1) + r with 0 <= r <= k-2. Here a >= -1, and a = -1 iff t < t_0. Put π_a = (P + t_0 - a) mod k and π'_a = (P' + t_0 - a) mod k, both in {0, ..., k-1}. Claim: **c_t violates the constraint iff π_a ∈ {0,1} or π'_a ∈ {0,1}.** In particular, whether c_t violates the constraint depends only on a.
*Proof.* The first coordinate of c_t is (Q+t) mod (k-1) = (t - t_0) mod (k-1) = r. Since a(k-1) ≡ -a (mod k), the second coordinate is (P+t) mod k = (P + t_0 - a + r) mod k = (π_a + r) mod k, and the third is (π'_a + r) mod k in the same way. The coordinate (π_a + r) mod k belongs to {r, r+1} iff π_a ∈ {0,1}. Indeed, if π_a + r <= k-1, the coordinate equals π_a + r, and π_a + r ∈ {r, r+1} iff π_a ∈ {0,1}. If π_a + r >= k, the coordinate equals π_a + r - k, which lies in {r, r+1} only if π_a ∈ {k, k+1}, impossible. In this case also π_a >= k - r >= 2, so π_a ∉ {0,1}, and both sides are false. The same argument applies to π'_a. ∎

**Step 12 (Level-1 bound, R9).** Let m = min(π_0, π'_0). Note π_0 ≠ π'_0 since P ≠ P'. For 0 <= a <= π_0 we have π_a = π_0 - a, because π_0 - a ∈ {0..k-1}. So π_a ∈ {0,1} iff a >= π_0 - 1 (for 0 <= a <= π_0), and likewise for π'. Hence, when m >= 1, the laps a = 0, ..., m-2 satisfy the constraint and lap a = m-1 violates it.
- *Case t_0 = 0* (Q = 0). Here c_0 lies in lap a = 0 and satisfies the constraint, so π_0, π'_0 ∈ {2, ..., k-1} and are distinct. Therefore 2 <= m <= k-2. The first violating time is the first time of lap m-1, namely T = (m-1)(k-1) >= k-1 >= 1. So **T <= (k-3)(k-1)**, with equality iff m = k-2, i.e. {π_0, π'_0} = {k-2, k-1}. As π_0 = P here, this means {P, P'} = {k-2, k-1}.
- *Case t_0 >= 1* (Q >= 1). The times 0, ..., t_0-1 form the tail of lap a = -1, whose violation status is that of c_0 (Step 11), i.e. no violation. So π_{-1}, π'_{-1} ∉ {0,1}, where π_{-1} = (π_0 + 1) mod k. π_{-1} ≠ 0 gives π_0 ≠ k-1, and π_{-1} ≠ 1 gives π_0 ≠ 0. The same holds for π'. So π_0, π'_0 are distinct elements of {1, ..., k-2}, and 1 <= m <= k-3. Laps -1, 0, ..., m-2 satisfy the constraint and lap m-1 violates it, so T = t_0 + (m-1)(k-1) <= (k-2) + (k-4)(k-1) = (k-1)(k-3) - 1.
Together with Steps 6 and 10: **every λ ⊢ T_{k-1}+1 with ε(λ) <= 1 has d_B(λ) <= (k-1)(k-3). Among those with ε(λ) = 1, equality holds exactly for the triple (0; k-2, k-1).**

## LOWER bound (R10)

**Step 13.** Let k >= 5 and λ^(k) = (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1). Explicitly: part 1 is k-2, part i is k-i for 2 <= i <= k-2, part k-1 is 2, and part k is 1. For k = 5 this is (3,3,2,2,1). It is weakly decreasing (k-2 >= k-2 >= ... >= 2 >= 2 >= 1), because k-2 >= 2. Compare with the staircase (k-1, ..., 1) of T_{k-1}. Row 1 lacks the cell (1, k-1), which is in D_{k-1} at position 0. Row k-1 gains (k-1, 2), in D_k at position k-2. Row k gains (k, 1), in D_k at position k-1. Rows 2..k-2 agree. So |λ^(k)| = T_{k-1} - 1 + 2 = n, and diag λ^(k) is the level-1 set with triple (0; k-2, k-1). This triple satisfies the constraint because k-2 >= 3 > 1 = Q+1. By Steps 10 and 12 (case t_0 = 0, m = k-2):
**d_B(λ^(k)) = (k-3)(k-1)**, hence D_B(T_{k-1}+1) >= (k-1)(k-3) for every k >= 5.
*Explicit end of the orbit, as a check of Steps 10-12.* Let F = (k-1)(k-3). Then F - 1 = (k-4)(k-1) + (k-2), so a = k-4 and r = k-2. Step 11 gives the triple c_{F-1} = (k-2; (k-2-(k-4)+k-2) mod k, (k-1-(k-4)+k-2) mod k) = (k-2; 0, 1). So B^{F-1}(λ^(k)) has cells D_1 ∪ ... ∪ D_{k-2}, plus D_{k-1} minus (k-1, 1), plus (1, k) and (2, k-1). That is, B^{F-1}(λ^(k)) = (k, k-1, k-3, k-4, ..., 3, 2), with k-2 parts. Applying B: the parts minus 1 are k-1, k-2, k-4, ..., 2, 1, and the new part is s = k-2. So B^F(λ^(k)) = (k-1, k-2, k-2, k-4, ..., 1) = λ(e_3), which is cyclic by B-C1. B^{F-1}(λ^(k)) lacks the cell (k-1,1) ∈ D_{k-1}, so it is not of the form λ(e_j) and is not cyclic. This agrees with Step 0.

## UPPER bound for all partitions (R11): [GAP]

**Step 14 [GAP].** The target needs d_B(λ) <= (k-1)(k-3) for every λ ⊢ T_{k-1}+1. Steps 6 and 12 prove this only for ε(λ) <= 1. For ε(λ) >= 2 no proof is given. Step 4 does show that every non-rigid step lowers ε by at least 1, and that between such steps the configuration rotates rigidly, each diagonal D_d with period d. But the exhaustive data (k = 5..11) show that for k >= 7 every level ε = 1, ..., 13 contains partitions with d_B exactly (k-1)(k-3). So a bound of the form (time above level 1) + (maximum time on level 1) cannot work. A proof would have to control the *phase* (the triple of Step 8, or its analogue) at which an orbit from a higher level first reaches level 1 or level 0. See stuck.md.

**What is established.** (1) D_B(T_{k-1}+1) >= (k-1)(k-3) for all k >= 5 (Step 13). (2) d_B(λ) <= (k-1)(k-3) for all λ with ε(λ) <= 1 and all k >= 5 (Step 12). The maximum of d_B over level 1 is exactly (k-1)(k-3), attained only by λ^(k). (3) D_B(T_{k-1}+1) = (k-1)(k-3) for k = 5, ..., 11 by exhaustive exact computation (out/code/check.py). **Not established:** the upper bound for ε >= 2 and k >= 12 (and, without computation, for k <= 11).
