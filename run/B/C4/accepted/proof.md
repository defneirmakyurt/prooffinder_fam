**Proved statement.** For every k >= 5, with n = T_{k-1}+1: the partition λ^(k) = (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1) of n satisfies d_B(λ^(k)) = (k-1)(k-3), hence D_B(T_{k-1}+1) >= (k-1)(k-3); moreover d_B(λ) <= (k-1)(k-3) for every partition λ of n whose energy E(λ) (Step 2) is at most E_min + 1 (Step 5). The upper bound D_B(T_{k-1}+1) <= (k-1)(k-3) for **all** partitions is **NOT proved** here ([GAP], Step 9).

Conjectured value: F(k) = (k-1)(k-3) = k^2 - 4k + 3. Exhaustive computation confirms D_B(T_{k-1}+1) = F(k) for 5 <= k <= 12 only (out/code/exhaustive_DB.py). That is evidence, not proof, for k >= 13.

Reading of the brief: none needed beyond the statement. d_B is the time to *enter* a cycle (d_B = 0 for cyclic partitions). The new pile has s cards, where s is the number of piles before removal, and it is sorted into the partition.

---

## 0. Conventions

0.1. The Young diagram of a partition λ = (λ_1 >= ... >= λ_s) is Y(λ) = {(i,j) : 1 <= i <= s, 1 <= j <= λ_i}. Here i is the row and j the column. A finite set S of cells in Z_{>0}^2 is *closed* if (i,j) ∈ S with i >= 2 implies (i-1,j) ∈ S, and (i,j) ∈ S with j >= 2 implies (i,j-1) ∈ S. The closed finite sets are exactly the Young diagrams, and the partition is read off as the sequence of row lengths. (This is standard: in a closed set, row i is an initial segment {1..r_i} of columns, and (i, r_{i+1}) ∈ S whenever r_{i+1} >= 1 forces r_i >= r_{i+1}. Conversely, left-justified rows of weakly decreasing lengths form a closed set.) λ ↦ Y(λ) is a bijection, and |Y(λ)| = n.

0.2. The *diagonal* of a cell (i,j) is i+j-1. Diagonal d consists of the d cells ⟨d,r⟩ := (r, d+1-r), r = 1..d. We call r the *row* of ⟨d,r⟩. The left neighbour (i,j-1) and the upper neighbour (i-1,j) of a cell on diagonal d lie on diagonal d-1. The right and lower neighbours lie on diagonal d+1. In diagonal coordinates the left neighbour of ⟨d,r⟩ is ⟨d-1,r⟩ (exists iff r <= d-1), and the upper neighbour is ⟨d-1,r-1⟩ (exists iff r >= 2).

0.3. Y(δ_{k-1}) = {(i,j): i+j <= k} is the set of all cells on diagonals 1, ..., k-1. It has T_{k-1} cells.

0.4. The rotation ρ is the map of Z_{>0}^2 given by ρ(i,j) = (i+1, j-1) if j >= 2, and ρ(i,1) = (1,i). In diagonal coordinates, ρ⟨d,r⟩ = ⟨d,r+1⟩ for r < d and ρ⟨d,d⟩ = ⟨d,1⟩. Check: (r, d+1-r) ↦ (r+1, d-r) when d+1-r >= 2, i.e. r < d; and ⟨d,d⟩ = (d,1) ↦ (1,d) = ⟨d,1⟩. Hence ρ maps each diagonal bijectively onto itself, as a cyclic shift of order d. So ρ is a bijection of Z_{>0}^2, it preserves i+j, and ρ(Y(δ_{k-1})) = Y(δ_{k-1}).

## 1. Rotation lemma (R1)

Let λ have s parts. Define the row list r(λ) = (r_1, ..., r_{s+1}) := (s, λ_1-1, λ_2-1, ..., λ_s-1). Then

  ρ(Y(λ)) = {(1,j) : 1 <= j <= s} ∪ {(i+1, j) : 1 <= i <= s, 1 <= j <= λ_i - 1},

which is the set of left-justified rows of lengths r_1, ..., r_{s+1}. B(λ) is the partition whose parts are the nonzero entries of r(λ), sorted.

*Proof.* The cells of Y(λ) in column 1 are (i,1) for 1 <= i <= s, and ρ sends them to (1,i), 1 <= i <= s. The remaining cells are (i,j) with 2 <= j <= λ_i, and ρ sends them to (i+1, j-1), where 1 <= j-1 <= λ_i - 1. The statement about B is the definition of the shift: the parts are λ_i - 1 when positive, together with s. ∎

## 2. Energy lemma (R2)

For a finite sequence of nonnegative integers a = (a_1, ..., a_m), put E(a) = Σ_i Σ_{j=1}^{a_i} (i+j) = Σ_i ( i·a_i + a_i(a_i+1)/2 ). For a partition, E(λ) := E((λ_1, ..., λ_s)) = Σ_{(i,j)∈Y(λ)} (i+j).

**Lemma 2.** (a) E(B(λ)) <= E(λ). (b) The following are equivalent: (i) E(B(λ)) = E(λ); (ii) λ_1 <= s + 1, where s is the number of parts; (iii) ρ(Y(λ)) is closed. (c) If these hold, then Y(B(λ)) = ρ(Y(λ)). If they fail, then E(B(λ)) <= E(λ) - 1.

*Proof.* By Step 1, E(r(λ)) = Σ_{c∈ρ(Y(λ))} (i+j) of c. This equals E(λ), because ρ is a bijection preserving i+j (0.4).

Let r↓ be the weakly decreasing rearrangement of r = r(λ). Zeros go last, so r↓ with its trailing zeros deleted is B(λ), and trailing zeros contribute nothing to E. Hence E(B(λ)) = E(r↓).

The sum Σ a_i(a_i+1)/2 does not change under rearrangement. For Σ i·a_i, suppose a is not weakly decreasing. Then some adjacent pair has a_i < a_{i+1}. Swapping the pair changes Σ i·a_i by (i·a_{i+1} + (i+1)·a_i) - (i·a_i + (i+1)·a_{i+1}) = a_i - a_{i+1} < 0. Each such swap lowers the number of inversions by exactly one, so repeated swaps end, after finitely many strict decreases, at the unique weakly decreasing rearrangement r↓. Hence E(r↓) < E(r) if r is not weakly decreasing, and r↓ = r otherwise. This proves (a) and (i)⇔(r weakly decreasing).

Since λ is weakly decreasing, r_2 >= r_3 >= ... >= r_{s+1}. So r is weakly decreasing iff r_1 >= r_2, i.e. s >= λ_1 - 1. This gives (i)⇔(ii).

By Step 1, ρ(Y(λ)) is the set of left-justified rows of lengths r_1, r_2, .... Such a set is closed iff the lengths are weakly decreasing (0.1), which gives (ii)⇔(iii). When r is weakly decreasing, B(λ) is r with its trailing zeros removed, so Y(B(λ)) = ρ(Y(λ)). Finally, E takes integer values, so failure of (i) gives E(B(λ)) <= E(λ) - 1. ∎

## 3. Cyclic partitions keep energy (R3)

**Lemma 3.** If μ is cyclic, then B(μ) is cyclic and E(B(μ)) = E(μ). Consequently, if E(B(ν)) < E(ν), then ν is not cyclic.

*Proof.* Suppose B^i(μ) = μ with i >= 1. Then B^i(B(μ)) = B(B^i(μ)) = B(μ), so B(μ) is cyclic. By Lemma 2(a), E(μ) = E(B^i μ) <= E(B^{i-1} μ) <= ... <= E(B μ) <= E(μ), so every inequality is an equality. ∎

**Corollary 3'.** If B^t(λ) is cyclic, then B^u(λ) is cyclic for all u >= t. Hence d_B(λ) = t exactly when B^t(λ) is cyclic and B^{t-1}(λ) is not (for t >= 1).

*Proof.* The first sentence is Lemma 3 applied u - t times. For the second: if B^u(λ) were cyclic for some u < t-1, then B^{t-1}(λ) would be cyclic by the first sentence. ∎

## 4. The cyclic partitions of n = T_{k-1}+1 (R4)

In this step k >= 2, so n = T_{k-1}+1 satisfies T_{k-1} < n < T_k (because T_k - T_{k-1} = k >= 2).

For j ∈ {1, ..., k}, let γ_j be the partition with Y(γ_j) = Y(δ_{k-1}) ∪ {⟨k,j⟩}. This set is closed. The cells of diagonals <= k-1 need only cells of lower diagonals (0.2). The left and upper neighbours of ⟨k,j⟩, when they exist, lie on diagonal k-1 and so belong to Y(δ_{k-1}). Explicitly, ⟨k,j⟩ = (j, k+1-j). So γ_j is δ_{k-1} = (k-1, ..., 1) with its j-th part raised by 1 when j <= k-1, and with a part 1 appended when j = k.

**Lemma 4.** (a) B(γ_j) = γ_{j+1} for j < k, and B(γ_k) = γ_1. Hence every γ_j is cyclic, of period k. (b) Every cyclic partition of n is one of γ_1, ..., γ_k.

*Proof.* (a) By 0.4, ρ(Y(γ_j)) = ρ(Y(δ_{k-1})) ∪ {ρ⟨k,j⟩} = Y(δ_{k-1}) ∪ {⟨k, j+1⟩} (read j+1 as 1 when j = k), and this is Y(γ_{j+1}). That set is closed, as shown above, so Lemma 2(c) gives Y(B(γ_j)) = Y(γ_{j+1}). Iterating, B^k(γ_j) = γ_j.

(b) Let μ be cyclic. By Lemma 3, all B^t(μ) are cyclic and E(B^{t+1}μ) = E(B^t μ). By Lemma 2(c) and induction on t, Y(B^t μ) = ρ^t(Y(μ)), and each such set is closed.

*Claim:* if diagonal d (d >= 1) of Y(μ) is not full, then diagonal d+1 of Y(μ) is empty. Suppose instead that ⟨d,a⟩ ∉ Y(μ) and ⟨d+1,c⟩ ∈ Y(μ). Since gcd(d, d+1) = 1, the Chinese remainder theorem gives t >= 0 with t ≡ 1-a (mod d) and t ≡ 1-c (mod d+1). By 0.4, ρ^t⟨d,a⟩ = ⟨d,1⟩ and ρ^t⟨d+1,c⟩ = ⟨d+1,1⟩. Because ρ^t is a bijection, ⟨d,1⟩ = (1,d) ∉ ρ^t(Y(μ)), while ⟨d+1,1⟩ = (1,d+1) ∈ ρ^t(Y(μ)). This contradicts closedness, since (1,d+1) requires its left neighbour (1,d). So the claim holds.

If diagonal d+1 is empty, then so is diagonal d+2. Each cell (i,j) on diagonal d+2 >= 2 has i >= 2 or j >= 2, so its upper or left neighbour exists, lies on diagonal d+1, and would have to belong to the closed set Y(μ). By induction, all diagonals beyond d are empty.

Let d be the smallest diagonal of Y(μ) that is not full. It exists because Y(μ) is finite. Then diagonals 1..d-1 are full, diagonal d has c cells with 0 <= c <= d-1, and all later diagonals are empty. So n = T_{d-1} + c with T_{d-1} <= n <= T_d - 1. The intervals [T_{d-1}, T_d - 1], d >= 1, are pairwise disjoint, and n lies in the one with d = k (since T_{k-1} < n < T_k). Hence d = k and c = n - T_{k-1} = 1, i.e. μ = γ_j for some j. ∎

## 5. Energy levels (R5)

Let c_d be the number of cells of Y(λ) on diagonal d, so 0 <= c_d <= d and Σ_d c_d = n. Every cell on diagonal d has i+j = d+1, so E(λ) = Σ_d (d+1) c_d. Put E_min := E(γ_1) = Σ_{d=1}^{k-1} d(d+1) + (k+1). For d <= k-1, write m_d := d - c_d >= 0, and let M := Σ_{d<=k-1} m_d. Counting cells gives Σ_{d>=k} c_d = n - T_{k-1} + M = 1 + M.

**Lemma 5.** E(λ) - E_min = M + Σ_{d>=k} (d-k)·c_d + Σ_{d<=k-1} (k-1-d)·m_d, a sum of nonnegative terms. Hence:
(a) E(λ) >= E_min, with equality iff λ ∈ {γ_1, ..., γ_k};
(b) E(λ) = E_min + 1 iff diagonals 1..k-2 are full, diagonal k-1 has exactly one missing cell, diagonal k has exactly two cells, and there are no cells beyond diagonal k.

*Proof.* We have E(λ) - E_min = Σ_{d>=k}(d+1)c_d - (k+1) - Σ_{d<=k-1}(d+1)m_d. Substitute Σ_{d>=k}(d+1)c_d = Σ_{d>=k}(d-k)c_d + (k+1)(1+M) and Σ_{d<=k-1}(d+1)m_d = kM - Σ_{d<=k-1}(k-1-d)m_d. This gives the displayed identity, and each term in it is >= 0.

(a) Equality forces M = 0 (all diagonals <= k-1 full) and c_d = 0 for d > k. Then c_k = 1 + M = 1, so Y(λ) = Y(δ_{k-1}) ∪ {one cell of diagonal k}, i.e. λ = γ_j. Conversely, E(γ_j) = E_min, since γ_j has the same diagonal counts as γ_1.

(b) Value 1 means exactly one of the three sums equals 1 and the others are 0.
- Case M = 1. The third sum is then 0, which forces the unique missing cell to be on diagonal k-1. The second sum is 0, so there are no cells beyond diagonal k. Then c_k = 1 + M = 2.
- Case M = 0 and Σ_{d>=k}(d-k)c_d = 1. This forces c_{k+1} = 1 and c_d = 0 for d >= k+2. Then c_k = (1+M) - c_{k+1} = 0. But a cell on diagonal k+1 has its left or upper neighbour on diagonal k (as in the proof of Lemma 4(b)), and that neighbour must be present. Contradiction, so this case is impossible.
- Case third sum = 1 with M = 0. Impossible, since M = 0 makes every m_d = 0.
Conversely, the configuration described in (b) has M = 1, and all other terms are 0. ∎

## 6. The family Q (R6)

For h ∈ {1, ..., k-1} and distinct x, y ∈ {1, ..., k}, put
  S(h;x,y) := (Y(δ_{k-1}) \ {⟨k-1,h⟩}) ∪ {⟨k,x⟩, ⟨k,y⟩}.
By Lemma 5(b), the partitions of energy E_min + 1 are exactly the partitions whose diagram is some closed S(h;x,y). When S(h;x,y) is closed, write Q(h;x,y) for its partition.

For z ∈ {1..k} write z⁺ = z+1 if z < k, and z⁺ = 1 if z = k. For h ∈ {1..k-1} write h⁺ = h+1 if h < k-1, and h⁺ = 1 if h = k-1. So z⁺ ≡ z+1 (mod k) and h⁺ ≡ h+1 (mod k-1).

**Lemma 6.** (a) S(h;x,y) is closed iff x, y ∉ {h, h+1}. (b) ρ(S(h;x,y)) = S(h⁺; x⁺, y⁺). (c) Define the offset o(z,h) ∈ {0, ..., k-1} by o(z,h) ≡ z - h (mod k). If h < k-1, then o(z⁺,h⁺) = o(z,h). If h = k-1 (a *wrap step*), then o(z⁺,h⁺) ≡ o(z,h) - 1 (mod k).

*Proof.* (a) First, Y(δ_{k-1}) \ {⟨k-1,h⟩} is closed. Removing a cell c from a closed set keeps it closed iff no remaining cell has c as its left or upper neighbour, i.e. iff the right and lower neighbours of c are absent. For c on diagonal k-1, those neighbours lie on diagonal k, which Y(δ_{k-1}) does not meet.

Next, add ⟨k,x⟩ and ⟨k,y⟩. The two added cells are on the same diagonal, so neither is a neighbour of the other (0.2). No cell on a diagonal <= k-1 requires a cell on diagonal k. So closedness holds iff, for each z ∈ {x,y}, the existing neighbours of ⟨k,z⟩ are present. Those neighbours are ⟨k-1,z⟩ (exists iff z <= k-1) and ⟨k-1,z-1⟩ (exists iff z >= 2). The only absent cell on diagonal k-1 is ⟨k-1,h⟩, so the condition is: not (z <= k-1 and h = z), and not (z >= 2 and h = z-1). Because 1 <= h <= k-1, h = z already forces z <= k-1, and h = z-1 already forces z >= 2. So the condition is z ∉ {h, h+1}.

(b) ρ is a bijection mapping each diagonal onto itself (0.4). So ρ(Y(δ_{k-1}) \ {⟨k-1,h⟩}) = Y(δ_{k-1}) \ {ρ⟨k-1,h⟩} = Y(δ_{k-1}) \ {⟨k-1,h⁺⟩}. Also ρ⟨k,z⟩ = ⟨k,z⁺⟩.

(c) If h < k-1, then z⁺ - h⁺ ≡ (z+1) - (h+1) = z - h (mod k). If h = k-1, then h⁺ = 1 = h - (k-2), so z⁺ - h⁺ ≡ z + 1 - h + k - 2 ≡ (z - h) - 1 (mod k). ∎

By (a), S(h;x,y) is closed iff o(x,h) ∉ {0,1} and o(y,h) ∉ {0,1}, i.e. iff both offsets lie in {2, ..., k-1}. The offsets o(x,h) and o(y,h) are distinct because x ≠ y are distinct residues mod k.

## 7. Exact depth on the level E_min + 1 (R7)

**Lemma 7.** Let k >= 4, and let Q = Q(h_0;x,y) be a partition of n of energy E_min + 1, with offsets o_x = o(x,h_0), o_y = o(y,h_0) ∈ {2,...,k-1}. Put m := min(o_x, o_y). Then
  d_B(Q) = (k - h_0) + (m-2)(k-1).
In particular d_B(Q) <= (k-1) + (k-4)(k-1) = (k-1)(k-3), with equality iff h_0 = 1 and {o_x, o_y} = {k-2, k-1}, i.e. iff Q = Q(1; k-1, k).

*Proof.* Put h_t := the element of {1..k-1} with h_t ≡ h_0 + t (mod k-1); x_t ≡ x + t and y_t ≡ y + t (mod k), in {1..k}. The step t → t+1 is a wrap step iff h_t = k-1. This happens for t = τ_1 < τ_2 < ..., where τ_j := (k-1-h_0) + (j-1)(k-1).

By Lemma 6(c), after the steps 0→1, ..., (t-1)→t the offsets are o_x - w(t) and o_y - w(t) (mod k), where w(t) is the number of wrap steps among them. Here w(t) = #{j : τ_j <= t-1}.

Let t_* := τ_{m-1} = (k-1-h_0) + (m-2)(k-1). Since m >= 2, m-1 >= 1, so t_* is a genuine wrap time. For 0 <= t <= t_* we have w(t) <= m-2. Since 2 <= m <= o_x, o_y <= k-1, the integers o_x - w(t) and o_y - w(t) lie in {2, ..., k-1}, so no reduction mod k is needed and neither is 0 or 1.

We prove by induction on t that B^t(Q) = Q(h_t; x_t, y_t) for 0 <= t <= t_*. The case t = 0 holds. Suppose it holds for some t < t_*. By Lemma 6(b), ρ(S(h_t;x_t,y_t)) = S(h_{t+1};x_{t+1},y_{t+1}). Its offsets are o_x - w(t+1) and o_y - w(t+1), with w(t+1) <= m-2 (because t+1 <= t_*), so both lie in {2,...,k-1}. By Lemma 6(a) the set is closed, so by Lemma 2(b)(c), Y(B^{t+1}Q) = S(h_{t+1};x_{t+1},y_{t+1}).

At t = t_*, the step t_* → t_*+1 is the (m-1)-th wrap step, so w(t_*+1) = m-1. One offset becomes m - (m-1) = 1. So ρ(Y(B^{t_*}Q)) = S(h_{t_*+1}; x_{t_*+1}, y_{t_*+1}) is not closed (Lemma 6(a)). By Lemma 2(b)(c), E(B^{t_*+1}Q) <= E(B^{t_*}Q) - 1 = E_min. By Lemma 5(a), equality holds and B^{t_*+1}Q = γ_j for some j, which is cyclic by Lemma 4(a). Moreover E(B^{t_*+1}Q) < E(B^{t_*}Q), so B^{t_*}Q is not cyclic (Lemma 3). By Corollary 3', d_B(Q) = t_* + 1 = (k-h_0) + (m-2)(k-1).

Maximisation: h_0 >= 1. The offsets are distinct elements of {2..k-1}, so m <= k-2, with equality iff {o_x,o_y} = {k-2,k-1}. So d_B(Q) <= (k-1) + (k-4)(k-1) = (k-1)(k-3), with equality iff h_0 = 1 and {o_x,o_y} = {k-2,k-1}. With h_0 = 1, o(z,1) = k-1 gives z = k, and o(z,1) = k-2 gives z = k-1. So Q = Q(1;k-1,k). (That S(1;k-1,k) is closed follows from Lemma 6(a): k-1, k ∉ {1,2} since k >= 4.) ∎

**Corollary 7'.** For every partition λ of n with E(λ) <= E_min + 1, d_B(λ) <= (k-1)(k-3) (k >= 4).
*Proof.* If E(λ) = E_min, then λ is cyclic (Lemmas 5(a) and 4(a)), so d_B = 0. If E(λ) = E_min + 1, apply Lemma 7. By Lemma 5(a) no other values occur. ∎

## 8. Lower bound: the explicit extremal partition and its orbit (R8)

Let k >= 5 and λ^(k) := Q(1; k-1, k), i.e. Y(λ^(k)) = (Y(δ_{k-1}) \ {⟨k-1,1⟩}) ∪ {⟨k,k-1⟩, ⟨k,k⟩}.

8.1 (Explicit parts.) ⟨k-1,1⟩ = (1,k-1), so row 1 has length k-2. ⟨k,k-1⟩ = (k-1,2), so row k-1 has length 2 instead of 1. ⟨k,k⟩ = (k,1) adds a row k of length 1. The other rows i (2 <= i <= k-2) keep length k-i. Hence
  λ^(k) = (k-2, k-2, k-3, ..., 3, 2, 2, 1),
with k parts: row 1 = k-2, rows i = k-i for 2 <= i <= k-2, row k-1 = 2, row k = 1. This is weakly decreasing (k-2 >= k-2 and 2 >= 2 >= 1), and its sum is T_{k-1} - 1 + 2 = n. For k = 5 it is (3,3,2,2,1).

8.2 (Orbit, symbolic in k.) Here h_0 = 1, and the offsets are o(k-1,1) = k-2 and o(k,1) = k-1, so m = k-2. By the induction in Lemma 7, for 0 <= t <= t_* := (k-2) + (k-4)(k-1) = k^2 - 4k + 2,
  B^t(λ^(k)) = Q(h_t; b_t, b_t⁺),  where h_t = 1 + (t mod (k-1)) and b_t ∈ {1..k}, b_t ≡ t - 1 (mod k).
(Indeed x_t ≡ k-1+t ≡ t-1 and y_t ≡ k+t ≡ t, so y_t = x_t⁺.)
At t = t_*: t_* ≡ -1 (mod k-1), so h_{t_*} = k-1; and t_* - 1 = k^2 - 4k + 1 ≡ 1 (mod k), so b_{t_*} = 1. Thus B^{t_*}(λ^(k)) = Q(k-1; 1, 2). Its diagram is Y(δ_{k-1}) minus (k-1,1), plus (1,k) and (2,k-1). So
  B^{t_*}(λ^(k)) = (k, k-1, k-3, k-4, ..., 2)   (k-2 parts: rows 1,2 have lengths k, k-1; row i has length k-i for 3 <= i <= k-2; row k-1 is empty).
Direct check of the last step: s = k-2 and λ_1 - 1 = k-1 > s, so sorting occurs. The parts minus 1 are k-1, k-2, k-4, ..., 1; adding the new part k-2 gives
  B^{t_*+1}(λ^(k)) = (k-1, k-2, k-2, k-4, k-5, ..., 1) = γ_3,
which is cyclic by Lemma 4(a) (k >= 5 ensures 3 <= k). Energy: E(Q(k-1;1,2)) = E_min + 1 > E_min = E(γ_3), so B^{t_*}(λ^(k)) is not cyclic (Lemma 3).

8.3 (Conclusion.) By Corollary 3', d_B(λ^(k)) = t_* + 1 = k^2 - 4k + 3 = (k-1)(k-3), for every k >= 5. Hence D_B(T_{k-1}+1) >= (k-1)(k-3) for every k >= 5. ∎

(The same orbit was checked against direct iteration of B for 5 <= k <= 60 by out/code/verify_lower_orbit.py. That check is a sanity test only. The proof above is symbolic in k.)

## 9. Upper bound for all partitions — [GAP]

**Not proved:** d_B(λ) <= (k-1)(k-3) for every partition λ of n = T_{k-1}+1 with E(λ) >= E_min + 2, for all k >= 5.

What is proved: Corollary 7' (all λ with E(λ) <= E_min + 1). Also the exhaustive computation for 5 <= k <= 12 (out/code/exhaustive_DB.py): D_B(T_{k-1}+1) = (k-1)(k-3), and the cyclic set is {γ_j}. That covers every partition for those k only.

Why the easy extension fails. Let τ(λ) be the first time the orbit reaches energy <= E_min + 1. Lemma 7 gives d_B(λ) = τ(λ) + d_B(B^{τ}λ) <= τ(λ) + (k-1)(k-3). This is too weak unless one shows that a late arrival (large τ) forces a good phase on arrival (small h_0-offset quantity (k-h_0)+(m-2)(k-1)). No such phase/arrival trade-off is proved here. See stuck.md.

## 10. Summary of what is established

- F(k) := (k-1)(k-3). LOWER BOUND D_B(T_{k-1}+1) >= F(k) for every k >= 5: **PROVED** (Step 8), with the explicit λ^(k) and its orbit.
- Cyclic partitions of T_{k-1}+1 are exactly γ_1..γ_k (one cycle of length k): **PROVED** (Step 4).
- d_B <= F(k) on the two lowest energy levels, and λ^(k) is the unique maximiser of d_B on level E_min+1: **PROVED** (Lemma 7, Cor. 7').
- UPPER BOUND for all partitions: **[GAP]**. CHECKED exhaustively only for 5 <= k <= 12.
- Hence D_B(T_{k-1}+1) = (k-1)(k-3) is established only for 5 <= k <= 12 (lower bound by proof, upper bound by exhaustive computation). For k >= 13 only ">=" is established.
