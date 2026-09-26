```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves (i) and (ii)(a) iff + (ii)(b) formula for every k>=1, 1<=r<=k; no extra hypotheses
  G2 PASS — every step written out; only mild compressions (2.1 composition check, 3.5 "argument of 3.3"), both re-derived below and valid
  G3 PASS — k=1 (8.3 explicit; 7.1-7.4 give K=2, |S|=0), r=k via |S|=0 branch of 7.4, r=1, d=1 in Lemma 6 (mod 1 trivial), j=0 in 10.4 (gcd(0,k)=k)
  G4 PASS — E is non-increasing (4.1), and on a cycle equality is forced by periodicity (4.2); no strict decrease off cycles needed, since the cycles are identified by Lemma 6, not by E
  G5 PASS — lambda(eps) is a partition of n, and B(lambda(eps)) = lambda(rho eps), for every k, eps (8.1, 8.3)
  G6 PASS — no circularity; Theorem 9 uses 7.5 (only if) and 8.4 (if), which are independent; nothing cites the target
  G7 PASS — code not load-bearing; integer-only; rerun 19.34 s
  G8 PASS — only standard tools used (CRT, orbit-stabiliser, sum phi(d)=k), all named; Burnside proved inline
  G9 PASS — "Established / not established" section is present and accurate
  S1 PASS — both directions: 7.5 (cyclic => lambda(eps)), 8.4 (lambda(eps) cyclic); cycle count via Burnside
  S2 PASS — set = {lambda(eps)}, count C(k,r), #cycles = binary necklaces N(k,r); all match exhaustive enumeration for n<=50
  S3 PASS — all k>=1, both ends of r; s counts 1-parts (0.6); arbitrary partitions are covered by 1.2 + Theorem 9
  S4 PASS — s is taken before subtraction (0.6); the new part is sorted in (sort(U)); fixed point cyclic (i=1); cycles counted, not partitions; finite check not relied on
  S5 PASS — r=k gives the single cyclic partition delta_k and N(k,k)=1 (11, 10.4); k=1 gives (1) -> (1)
  S6 PASS — example values reproduced; exhaustive n<=50 matches set and count for every (k,r)
EQUALITY CASES: n=T_k for k=1..9: delta_k is the unique cyclic partition, a fixed point, reached from every partition (exhaustive). E-equality holds (U(lambda) already sorted) on every cyclic partition with n<=50.
CROSS-CELL: N/A (C1 is the first cell); internal r=k reduction consistent
CEX SEARCH: out/cex/search.py tested the full claim for n<=50 (exhaustive), claims 8.2/8.3/10.3/N=necklaces for k<=14, and Lemma 3 and 2.1/2.2/4.1 on 2x20000 random instances; no counterexample
OTHER ISSUES: the hand-in is Markdown with LaTeX math, not a .tex file; converting it is a packaging step and needs no mathematical change. Optional: attribute the classical result (Brandt 1982) as context.
RAN: out/cex/search.py 50 14 7 — n=1..50 exhaustive, k=1..14, 20000+20000 random — COMPLETED, real 7.07 s
RAN: out/cex/search.py 30 12 2 — n=1..30, k=1..12, seed 2 — COMPLETED, real 0.79 s
RAN: inbox/subject/code/check_c1.py 45 — n=1..45 — COMPLETED, "ALL OK up to 45", real 19.34 s
```

---

## 1. Checklist (full reasons)

Part G

- **G1 PASS.** Target (i): for every k >= 1, every lambda of T_k reaches delta_k (some i >= 0), and delta_k is the only cyclic partition. This is proved in section 11, which specialises Theorem 9 to r=k and uses 1.2. Target (ii)(a): an explicit set as functions of k, r, namely {lambda(eps) : eps in {0,1}^k, |eps| = r}, with an iff proof (Theorem 9). Target (ii)(b): N(k,r) = (1/k) sum_{d | gcd(k,r)} phi(d) C(k/d, r/d), proved (10.1–10.4). The parameter range is every k >= 1, 1 <= r <= k. The reading of "cycle" (0.1: forward orbit of a cyclic partition, distinct as sets) is the natural one.
- **G2 PASS.** I checked every "by induction" and every compressed step.
  - 2.1: "composing in both orders gives the identity". I wrote this out. R∘R⁻¹(1,h) = R(h,1) = (1,h). R∘R⁻¹(j',h') = R(j'-1,h'+1) = (j',h'), since h'+1 >= 2. The other order is symmetric.
  - 3.5: "argument of 3.3 applied to these i positions". It is valid because the 3.3 argument works for any i distinct positions.
  - Burnside's lemma is proved.
  - "sum_{d|k} phi(d) = k" gets a one-line proof via the gcd partition of 10.4.
- **G3 PASS.**
  - k=1: n=1, lambda=(1). Then C = D_1, K=2, |S|=0, so k=K-1=1 and r=1. Section 8.3 treats k=1 explicitly.
  - Lemma 6 with d=1: congruences mod 1 are trivial, and D_1 = {(1,1)}.
  - 10.4 with j=0: g=k, and phi(1)=1 counts it.
  - r=k: the |S|=0 branch of 7.4.
  - eps_k=0: the last part is dropped (8.1, 8.3).
- **G4 PASS.** Invariants:
  - 2.2: R preserves j+h-1, so E(U(lambda)) = E(lambda).
  - Lemma 3: sorting does not increase E, and strictly decreases it when U is unsorted (3.5 proves the strictness).
  - 4.2: on a cycle, E values are non-increasing and periodic, so they are constant. That forces U = sorted at every step, hence C(B^t lambda) = R^t C(lambda).
  - Strict decrease off cycles is never needed: the cycles are identified by the combinatorial Lemma 6, and the orbit reaching a cycle comes from pigeonhole.
- **G5 PASS.** 8.1 checks that lambda(eps) is positive and weakly decreasing (difference 1+eps_j-eps_{j+1} >= 0) with sum T_{k-1}+r, for all k, eps. 8.3 checks the B-action in general, including the eps_k = 1 case (lambda_k - 1 = 0 is dropped) and zeros in the middle of the tail (e.g. eps_{k-1}=0 gives lambda_{k-1}-1 = 0, which matches the dropped last entry of lambda(rho eps)).
- **G6 PASS.** The logical order is 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11, with no back-references to later results. Part (i) is derived from (ii); it is not assumed.
- **G7 PASS.** The code is declared non-load-bearing, and the proof never uses it. Its arithmetic is integer-only (`//`, `comb`, gcd). I reran it: "ALL OK up to 45", real 19.34 s (the claimed 18.58 s is consistent).
- **G8 PASS.** External facts used: the Chinese remainder theorem (Lemma 6), the orbit–stabiliser theorem (10.2) and uniqueness of the sorted rearrangement. All are standard textbook facts and named as such. Burnside and sum phi(d) = k are proved. The proof does not cite the classical result on Bulgarian solitaire cycles; it is self-contained, so no citation is needed.
- **G9 PASS.** The final section states what is established (all of (i), (ii)(a), (ii)(b)) and what is not addressed (C2+). It states that the brute force is not relied on.

Part S

- **S1 PASS.**
  - Only-if: 7.1–7.5. Lemma 6 plus the minimality of K give D_1..D_{k-1} ⊆ C(lambda) ⊆ D_1..D_k with r cells of D_k, so lambda = lambda(eps).
  - If: 8.4, since B^k lambda(eps) = lambda(rho^k eps) = lambda(eps).
  - Count: 10.1–10.4.
- **S2 PASS.** I re-derived the set and the count by hand (see section 2). Exhaustive enumeration (my own graph-based code) for every n = 1..50 matches all of these:
  - the cyclic set equals {lambda(eps)};
  - it also equals the independently built "staircase delta_{k-1} + r cells of D_k" set;
  - |set| = C(k,r);
  - #cycles = N(k,r) = brute-force necklace count.
- **S3 PASS.**
  - Every k >= 1 is covered through the general K argument. Both ends r=1 and r=k are covered (7.4 branches).
  - In 0.6, s counts all parts including 1s; U(lambda) = (s, lambda_1-1, ..., lambda_t-1) drops only the vanishing parts.
  - Partitions with more than k parts, or a part larger than k, are non-cyclic by Theorem 9 and reach a cycle by 1.2.
- **S4 PASS.**
  - s is the part count before subtraction (0.6).
  - The new part is inserted in sorted position: B = sort(U), and non-sortedness is exactly what 4.1 handles.
  - A fixed point counts as cyclic (p >= 1 allowed; delta_k with p=1).
  - Cycles are counted via Burnside, not read off; cyclic partitions and cycles are distinguished (C(k,r) vs N(k,r)).
  - The energy argument is used only on cycles, where constancy is proved; cycle identification is by Lemma 6, not by finiteness.
- **S5 PASS.** r=k: W(k,k) = {1^k}, lambda = delta_k, B(delta_k) = delta_k, and N(k,k) = (1/k) sum_{d|k} phi(d) = 1. k=1: (1) → (1). No lower cells exist.
- **S6 PASS.** B((2,1,1,1,1)) = (5,1), B((5,1)) = (4,2), B((4,2)) = (3,2,1), B((3,2,1)) = (3,2,1), all verified. The exhaustive comparison covers n <= 50 (required: <= 30).

## 2. Per-step reasons (line-by-line re-derivation)

- **0.2–0.5.** These are definitions.
  - The cell set determines a partition via column counts.
  - 0.3 follows directly from the definition of C.
  - The diagonals D_d partition N^2 via d = j+h-1 >= 1, with |D_d| = d.
  - The E formula: sum_{h=1}^{c_j} (j-1+h) = (j-1)c_j + c_j(c_j+1)/2.
- **0.6.** λ is weakly decreasing, so {j : λ_j >= 2} = {1..t}. U's entries are s >= 1 and λ_j - 1 >= 1 for j <= t, exactly the multiset in the definition of B. Hence B = sort(U).
- **0.7.** R maps N_{>=1}^2 into itself, since h-1 >= 1 when h >= 2.
- **1.1.** B(λ) has positive parts, is sorted by construction, and has sum sum_{j<=t}(λ_j-1) + s = n − s + s = n, because λ_j - 1 = 0 for j > t.
- **1.2.** |P(n)| is finite, and pigeonhole on |P(n)|+1 iterates gives B^a = B^b with a < b. Then B^a λ is cyclic with period b−a >= 1. Valid.
- **2.1.**
  - Forward map, case h >= 2: λ_j >= 2 gives j <= t; the image has first coordinate j+1 <= t+1 and height h-1 <= c_{j+1}.
  - Forward map, case h = 1: (1,j) with j <= s = c_1.
  - Inverse, (1,h) → (h,1): valid since h <= s, so λ_h >= 1.
  - Inverse, (j',h') → (j'-1,h'+1) for j' >= 2: valid since j'-1 <= t and h'+1 <= λ_{j'-1}.
  - Both compositions are the identity (checked case by case, see G2).
  - So R is a bijection C(λ) → C(U(λ)).
- **2.2.** (j+1)+(h-1)-1 = j+h-1, and 1+j-1 = j = j+1-1. So R preserves the diagonal index, and E(U λ) = E(λ) by the bijection.
- **3.1.** sort(c) has the same length m and the same multiset, so sum c_j(c_j+1)/2 cancels.
- **3.2.** Exchanging sums gives sum_{j}(j-1)c_j = sum_{i=1}^{m-1}(n − P_i). Correct index bookkeeping.
- **3.3.** The sorted positions j_1 < ... < j_i satisfy j_l >= l, so λ_{j_l} <= λ_l. Summing gives P_i(c) <= P_i(λ). Valid for any i distinct positions.
- **3.4.** Subtracting the two identities from 3.2 gives E(c) − E(λ) = sum_i (P_i(λ) − P_i(c)) >= 0.
- **3.5.** If c is sorted, c = λ by uniqueness of the sorted rearrangement. Otherwise take c_i < c_{i+1}. Swapping in position i+1 gives i distinct positions with sum > P_i(c), and that sum is <= P_i(λ) by 3.3. So the inequality is strict at index i, and E(c) > E(λ).
- **4.1.** Lemma 3 applies to c = U(λ): positive entries, sum n. Combined with 2.2, E(Bλ) <= E(λ), with equality iff U(λ) is sorted. In that case Bλ = U(λ) as sequences, so C(Bλ) = R(C λ).
- **4.2.**
  - The E values along the cycle are non-increasing and B^p λ = λ, so all are equal on i < p.
  - B^i = B^{i mod p} extends this to all i.
  - The equality case of 4.1 at each B^i λ gives C(B^{i+1}λ) = R C(B^i λ).
  - Induction then gives C(B^t λ) = R^t C(λ).
- **5.1.** For a < d, the height d+1-a >= 2, so R(x_a) = x_{a+1}; and R(x_d) = R(d,1) = (1,d) = x_1. So R restricted to D_d is the d-cycle, and R^t(x_a) = x_{a+t mod d}.
- **5.2.** R^t preserves diagonals, so R^t(X) ∩ D_d = R^t(X ∩ D_d). Injectivity of R^t on D_d gives the iff.
- **Lemma 6.**
  - The CRT gives t >= 0 with a+t ≡ 1 (mod d) and b+t ≡ 1 (mod d+1).
  - Then R^t x_a = (1,d) is absent and R^t y_b = (1,d+1) is present in C(B^t λ).
  - B^t λ is a partition (1.1), so by 0.3 the presence of (1,d+1) forces (1,d) to be present. Contradiction. Valid.
- **7.1.** K exists: the D_d are pairwise disjoint and non-empty (0.4) and C(λ) is finite, so not every D_d is contained in C(λ). Also (1,1) ∈ C(λ), so K >= 2.
- **7.2.** Induction. For e = K+1, apply Lemma 6 at d = K. For larger e, the empty D_{e-1} (non-empty as a set) is not contained in C(λ), so Lemma 6 applies at d = e-1.
- **7.3.** By minimality of K, D_1..D_{K-1} ⊆ C(λ); by 7.2 there is nothing beyond D_K. So n = T_{K-1} + |S| with 0 <= |S| <= K-1.
- **7.4.** The intervals (T_{m-1}, T_m] tile N_{>=1}. If |S| >= 1, then T_{K-1} < n < T_K, so k = K and r = |S|. If |S| = 0, then n = T_{K-1} with K-1 >= 1, so k = K-1 and r = k. In both cases (*) holds.
- **7.5.** Column-by-column reading using (*) gives λ_j = (k-j) + eps_j for j <= k, and λ_j = 0 for j > k. Only λ_k can be 0. So λ = λ(eps) with |eps| = r.
- **8.1.** The entries of λ(eps) are positive, except possibly the last. Consecutive differences are 1+eps_j-eps_{j+1} >= 0. The sum is T_{k-1} + r. So λ(eps) is a partition of n.
- **8.2.** eps_j = λ_j − (k−j) recovers eps, so ε ↦ λ(ε) is injective.
- **8.3.**
  - λ(eps) has s = k-1+eps_k parts. For k >= 2 this is >= k-1 >= 1; for k = 1, eps_1 = r = 1.
  - The multiset of parts of B(λ) and of λ(ρ eps) coincide entrywise under j → j+1. Both drop exactly the same zero values: λ_k - 1 = 0 when eps_k = 1, and k-(j+1)+eps_j = 0 only at j = k-1 with eps_{k-1} = 0.
  - A partition is determined by its multiset of parts. Valid.
- **8.4.** ρ^k = id, so B^k λ(eps) = λ(eps) with k >= 1. So λ(eps) is cyclic.
- **Theorem 9.** Combines 7.5 and 8.4; the count C(k,r) follows from 8.2. Valid. The "equivalently" Young-diagram form is the content of (*) and 8.1.
- **10.1.**
  - Every element of a cycle is cyclic.
  - Λ is a bijection W(k,r) → Cyc(n) with BΛ = Λρ.
  - The cycle through Λ(eps) is Λ(orbit of eps).
  - Orbits partition W and Λ is injective, so #cycles = #orbits of Z/k acting via ρ^j. Burnside is valid for non-faithful actions, with |H| = k.
- **10.2.** Burnside's lemma, via double counting and orbit–stabiliser. Correct.
- **10.3.**
  - (ρ^j eps)_i = eps_{i-j}.
  - Fixed words are those constant on the cosets of ⟨j⟩ = gZ/kZ: g cosets, each of size k/g.
  - A fixed word with r ones exists iff (k/g) | r, and then there are C(g, rg/k) of them. Valid.
- **10.4.** #{j in [0,k) : gcd(j,k) = g} = phi(k/g), including j=0 with g=k. Substituting d = k/g gives the stated formula. The check at r = k gives 1.
- **11.** T_k has rank k with r = k. W(k,k) = {1^k} and λ(1^k) = δ_k. Every orbit reaches a cyclic partition (1.2), which must be δ_k. Valid; i >= 0 as the target requires.

**Unjustified, circular or false steps found:** none.

## 3. Numerical sanity

- I reran the subject's `inbox/subject/code/check_c1.py 45`. Result: "ALL OK up to 45", real 19.34 s, integer arithmetic only. Log: `out/cex/log_subject_check_c1_45.txt`.
- My own independent implementation, `out/cex/search.py`, is stdlib only and exact:
  - it enumerates partitions with an iterative generator, and cross-checks p(n) against the Euler pentagonal recurrence;
  - it finds cyclic nodes by colouring the functional graph of B, and cross-checks each against the literal definition (a walk until the first repeat);
  - it compares with both the λ(eps) set and a Young-diagram construction.
- n = 1..50 (all p(n) partitions, up to 204226 at n = 50): all assertions pass. Examples:
  - n = 47: 45 cyclic partitions, 5 cycles (lengths 5, 10×4) = N(10,2) = 5.
  - n = 50: 252 cyclic partitions, 26 cycles = N(10,5).
- Floating point: none in the proof or in either piece of code.

## 4. Equality-case test

- **n = T_k, k = 1..9** (n = 1, 3, 6, 10, 15, 21, 28, 36, 45):
  - the cyclic set is exactly {δ_k};
  - B(δ_k) = δ_k;
  - every partition reaches δ_k (exhaustive).
- **Energy tightness:** for every cyclic partition with n <= 50, U(λ) is already sorted and E(Bλ) = E(λ), as 4.2 requires. On random partitions (40000 total), E(Bλ) = E(λ) holds exactly when U(λ) is sorted, as the equality case of 4.1 states.

## 5. Cross-cell consistency

C1 is the first cell, so there are no verified lower cells. Internally, (ii) at r = k reproduces (i): N(k,k) = 1 and C(k,k) = 1.

## 6. Counterexample search (`out/cex/search.py`)

- **Part A.** Exhaustive over all partitions of every n in [1, 50]. Checks the full claim: cyclic set, the Young-diagram form, |set| = C(k,r), #cycles = N(k,r) = brute-force necklace count, reach-δ_k for triangular n, and 4.2. No counterexample.
- **Part B.** Every k in [1, 14] and every eps in {0,1}^k with |eps| >= 1. Checks:
  - 8.1: λ(eps) is a partition of T_{k-1} + |eps|;
  - 8.2: injectivity;
  - 8.3: B(λ(eps)) = λ(ρ eps);
  - 10.3: the fixed-point count of ρ^j on W(k,r), for every j and r;
  - N(k,r) = necklace count for every r.

  No counterexample.
- **Part C.** Random tests, seeds 7 and 2, 20000 trials each:
  - Lemma 3, including the strict equality case, and the E formula of 0.5, on random sequences of length <= 9 with entries <= 8;
  - 2.1 (R is a bijection C(λ) → C(U λ)), 2.2 and 4.1, on random partitions of n <= 40.

  No counterexample.
- **Part D.** The statement's example values: pass.

Logs: `out/cex/log_search_N50_K14_seed7.txt` (real 7.07 s), `out/cex/log_search_N30_K12_seed2.txt` (real 0.79 s).
