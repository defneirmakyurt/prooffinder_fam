```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none
CHECKLIST:
  G1 PASS — proves (i) and (ii)(a),(b) for every k>=1, 1<=r<=k, exactly as in target.md; no extra hypotheses; i>=0 as in target.
  G2 PASS — no "clearly/obviously/routine/similarly/by symmetry"; every step written out (see per-step notes).
  G3 PASS — k=1 handled explicitly (Thm 9(a),(d), Sec. 8); r=k and r'=0 handled separately in Thm 11; n>=1 used to force e>=1.
  G4 PASS — E only needs to be non-increasing (Lemma 3(a)); equality along a cycle is forced by periodicity (Lemma 6(b)); strictness in Lemma 2 is proved and is the only strictness used.
  G5 PASS — lambda(eps) and B(lambda(eps))=lambda(rho eps) proved for all k>=1, all eps in W(k,r), both cases eps_{k-1}=0/1.
  G6 PASS — no circularity; (i) derived from (ii)(a) + pigeonhole; Burnside proved in 6.3.
  G7 PASS — no step depends on computation; included code is exact integer, stdlib-only, runs in ~5 s.
  G8 PASS — only elementary tools (pigeonhole, Bezout, sorting uniqueness, orbit-stabiliser), declared; nothing problem-specific cited.
  G9 PASS — Sec. 9 states exactly what is established; code labelled sanity-only.
  S1 PASS — both directions of the iff (Thm 11 <= and =>), explicit set C(k,r), count binom(k,r), cycle count N(k,r) proved; (i) both parts.
  S2 PASS — delta_k unique cyclic at T_k; claimed set and count re-derived and matched by my exhaustive enumeration for all n<=50.
  S3 PASS — all k>=1 incl. k=1,2; r=1 and r=k; Cor. 8 applies to any cyclic partition (any number of 1-parts, >k parts, parts >k).
  S4 PASS — s counts all parts (0.2, Lemma 1); sorted insertion handled by mu* (Lemma 3); fixed points counted as cycles; cycles counted via Burnside, not read off; energy used only as a non-increasing quantity, cycles identified by Prop. 7.
  S5 PASS — r=k gives C(k,k)={delta_k}, N(k,k)=1 (6.7, Thm 13); k=1 gives (1), B((1))=(1).
  S6 PASS — example chain verified; exhaustive enumeration n=1..50 matches C(k,r), binom(k,r), N(k,r) and the cycle lengths.
EQUALITY CASES: n=T_k for k=1..9 (n<=45 exhaustive): cyclic set={delta_k}, one fixed point, every partition reaches delta_k. Matches Thm 13.
CROSS-CELL: consistent with S5 (r=k reduces to (i)); no gated lower cells exist.
CEX SEARCH: out/cex/referee_check.py: exhaustive n<=50 (cyclic set, cycle count, cycle lengths); per-partition Lemmas 1,3,4,6(b), Prop 7 for n<=35; Thm 9(d) for all eps, k<=16; N(k,r) vs brute-force orbit count, k<=16; Lemma 2 on 200000 random sequences. No counterexample.
OTHER ISSUES: editorial only: (1) the preamble cites "Step 10.1" and "Step 10.3", which do not exist (should be 6.1, 6.3); (2) the preamble and Sec. 9 cite "out/code/", but the code is in subject/code/; (3) the hand-in asks for LaTeX, while proof.md is Markdown with LaTeX math, so it needs conversion when assembled; (4) 6.5 uses gcd(gj',k)=g*gcd(j',k/g) without stating it, which is an elementary one-liner.
RAN: subject check_c1.py n=1..45 (python3) COMPLETED, real 4.90 s | referee_check.py partA n=1..50, partB n=1..35, partC k=1..16, 200000 random Lemma-2 tests (python3) COMPLETED, real 5.85 s
```

# Referee report B-C1-005 (VERIFY, subject B-C1-001)

## 1. Statement match

Target (ii) for every k>=1, 1<=r<=k, n=T_{k-1}+r:
- (a) an explicit set, with an if-and-only-if proof;
- (b) the exact number of cycles, as a formula in k and r.

Target (i) for n=T_k: every partition reaches delta_k at some i>=0, and delta_k is the only cyclic partition.

The proof's opening statement gives:
- (a) C(k,r) = { (k-1+e_0, ..., 1+e_{k-2}, e_{k-1}) with a final 0 dropped : e in {0,1}^k, sum e = r };
- (b) N(k,r) = (1/k) sum_{d | gcd(k,r)} phi(d) binom(k/d, r/d);
- (i) as stated.

The quantifiers and ranges agree, and so does the cyclic definition (i>=1, so fixed points count). "Distinct cycles" is read as the cycles of the functional graph of B on P(n). That is the natural reading, and the proof states it explicitly. The only difference from the hand-in requirement is format: the file is Markdown with LaTeX math. It needs conversion at assembly, and nothing mathematical changes.

## 2. Per-step verification

- **0.1–0.2**: This is a restatement of the definitions with 0-indexing, and the padding convention λ_a=0 for a>=s. It is consistent with the statement: s counts all parts, 1-parts included.
- **0.3**: |Y(λ)| = Σλ_a = n. Y is injective because the row lengths recover λ, and a partition is its sequence of positive parts.
- **0.4 Young property**: b<λ_a forces a<s. Then a'<=a and weak decrease give λ_{a'} >= λ_a > b >= b'. Correct.
- **0.5–0.6**: D_d has d+1 points, and the diagonals partition Z_{>=0}^2. Σ_{j<d}(j+1) = T_d. T_d is strictly increasing, so the rank is unique. Correct.
- **1.1**: Zero entries contribute a·0 + C(0,2) = 0, so trailing zeros do not change E. Correct.
- **1.2 Lemma 1**: I re-derived it. C(x-1,2) = C(x,2) - (x-1) for x>=1 (at x=1 both sides are 0). The entry μ_{a+1} contributes aλ_a + C(λ_a,2) - a, and μ_0 contributes C(s,2). Since Σ_{a<s} a = C(s,2), E(μ) = E(λ). It was also checked on every partition with n<=35.
- **1.3 Lemma 2**: Swapping an ascent at a, a+1 changes F by y_a - y_{a+1} < 0. The swap process terminates because F strictly decreases over a finite set, and it ends at the unique weakly decreasing arrangement. Strictness follows when x is unsorted (J>=1). Correct, and it was tested on 200000 random sequences.
- **1.4 Lemma 3**: The multiset of μ is the parts of B(λ) plus zeros, because s>=1 is positive. So μ* = (B(λ),0,…,0) and E(μ*) = E(B(λ)).
  - (a) follows from Lemmas 2 and 1.
  - μ_1..μ_s is weakly decreasing, so μ is sorted iff s >= λ_0 - 1.
  - (b) is the contrapositive of the strict part of Lemma 2.
  - (c) holds because a sorted μ equals μ*.

  All correct, and checked exhaustively for n<=35 (including strict decrease whenever s < λ_0 - 1).
- **2.1**: τ and its inverse are written out, and both compositions are checked. It is a bijection.
- **2.2 Lemma 4**: By Lemma 3(c) and padding, ν_0 = s, ν_{a+1} = λ_a - 1 and ν_c = 0 for c>s. Split Y(λ) into column 0 and the rest. τ sends column 0 to row 0 of length s, and it sends (a,b) with b>=1 to (a+1,b-1). The images are exactly the two pieces of Y(ν). Correct, and checked on all 47874 sort-free steps with n<=35.
- **2.3 Lemma 5**: The direct computation holds in both cases a<d and a=d. The τ^t formula follows by induction. Correct.
- **2.4 Lemma 6**: (a) holds by periodicity. For (b), E is non-increasing around a closed orbit of length p, so all steps are equalities; Lemma 3(b) then gives s >= λ_0 - 1 at each time. (c) follows by induction with Lemma 4. Correct. This is the right way to use a monotone energy (trap S4): only equality on cycles is used, not strict decrease off them.
- **3.1 Proposition 7**: I re-derived each part.
  - (1): τ^t is injective, so holes stay holes. Lemma 5 gives both positions.
  - (2): g | (Q-P) >= 1 gives g <= Q-P, so {0..Q-P} contains a full residue system mod g and c* exists. With uP + vQ = g and j = um mod Q, we get jP ≡ m(g - vQ) ≡ gm (mod Q). So t = t_0 + jP puts the hole at p_d(0) and the cell at p_{d'}(c*), and 0 <= c* <= Q-P < Q.
  - (3): d' - c* >= d, so the Young property puts (0,d) in Y, which is a contradiction.

  Every hypothesis is checked (d<d' is what makes Q-P>=1). Correct, and checked on every cyclic partition with n<=35.
- **3.2 Corollary 8**: e exists because D_0..D_n would hold more than n cells. Prop. 7 with d=e kills all cells above e. r' <= e, and n = T_e + r' by disjointness. Correct.
- **4.1**: These are definitions. Only L_{k-1} can be 0, because L_a >= k-1-a >= 1 for a <= k-2.
- **4.2 Theorem 9**:
  - (a): L_a - L_{a+1} = 1 + e_a - e_{a+1} >= 0. The sum is T_{k-1} + r, and the length is k-1+e_{k-1}. It is non-empty, and k=1 is checked.
  - (b): Row a is {b <= k-2-a} plus p_{k-1}(a) when e_a=1. Row k-1 has no lower-diagonal part, and there are no rows >= k.
  - (c): This follows from (b).
  - (d): λ_0 - 1 <= k-1 <= s, so Lemma 3(c) applies. The index bookkeeping μ_a = L(ρe)_a for 1 <= a <= min(s,k-1) is correct (a-1 <= k-2 and a-1 < s). In both cases e_{k-1}=0 and e_{k-1}=1, deleting the zeros gives λ(ρe), including when both trailing entries are 0.

  I re-derived all of it, and (d) was checked for every e in {0,1}^k with sum>=1 and k<=16.
- **4.3 Corollary 10**: ρ^k = id and B^t(λ(e)) = λ(ρ^t e) by induction, using ρe ∈ W(k,r). So B^k fixes λ(e) with k>=1. Correct.
- **5.1 Theorem 11**:
  - (<=) follows from 9(a) and Cor. 10.
  - (=>), case r'>=1: T_e < n < T_{e+1}, so the rank is e+1 = k and r' = r. The cell set is D_0..D_{k-2} plus r points of D_{k-1}, which is Y(λ(e)), and Y is injective.
  - (=>), case r'=0: n>=1 gives e>=1, the rank is e = k, and r = k, so λ = λ(1..1).
  - Count: |C| = |W| = binom(k,r) by 9(c).

  Correct, and exhaustively confirmed for n<=50.
- **5.2**: A restatement of the set. It agrees with 4.1.
- **6.1**: The cycles O(λ) are well defined and partition the cyclic set. The argument with t' = t mod p is correct because p - t' + t ≡ 0 (mod p) and is >= 0.
- **6.2**: Λ is a bijection and B^t∘Λ = Λ∘ρ^t, so O(Λe) = Λ(Ge) and orbits correspond bijectively to cycles. Correct. Cycle lengths match the orbit sizes, which I also checked exhaustively for n<=50.
- **6.3 Burnside**: Double counting plus orbit–stabiliser (the bijection hStab(x) -> hx is named). Correct and standard.
- **6.4**: (=>) Bezout with u reduced mod k gives ρ^{uj} = ρ^g, so e is invariant under shifting by g. Because g | k, the residue class mod g is exhausted. (<=) holds because g | j and g | k. The fixed-word count binom(g, rg/k) when (k/g) | r, and 0 otherwise, is correct.
- **6.5**: j = gj' with gcd(j', k/g) = 1. This uses gcd(gj', gm) = g·gcd(j',m), which is not stated but is elementary. The j'=0 ↔ j'=m substitution gives φ(k/g). Correct.
- **6.6 Theorem 12**: Grouping j by g = gcd(j,k) and then substituting d = k/g gives N(k,r). Correct. It matches a brute-force orbit count for all 1<=r<=k<=16, and the exhaustive cycle count for n<=50.
- **6.7**: Σ_{d|k} φ(d) = k follows from 6.5, so N(k,k) = 1. N = 1 when gcd(k,r) = 1. Correct, and consistent with S5.
- **7.1 Theorem 13**: The rank is k and r = k, so C(k,k) = {λ(1..1)} = {δ_k}; δ_k is cyclic by (<=) of Thm 11. Pigeonhole on M+1 iterates gives a cyclic B^i(λ), and that iterate is δ_k. Correct: this proves both parts of (i), with i>=0.
- **8, 9**: The edge-case summary and the statement of what is established are accurate.

**Unjustified, circular or false steps**: none found. Editorial defects only (see OTHER ISSUES in the verdict block).

## 3. Numerical sanity

- **Subject's code** `inbox/subject/code/check_c1.py`, run as the copy `out/cex/subject_check_c1_copy.py 45`: "ALL OK up to n = 45", real 4.90 s. It uses exact integers, is stdlib-only, and is not load-bearing.
- **Floating point**: none used anywhere.

## 4. Equality / extremal cases

- n = T_k for k=1..9: the unique cyclic partition is δ_k, it is a fixed point, and every partition reaches it within p(n) steps. This was checked exhaustively in referee_check.py partA.
- r=1 and r=k-1 give a single k-cycle, confirmed for n<=50.

## 5. Cross-cell

This is the first cell, so there are no gated lower cells. The internal consistency required by S5 holds: r=k reduces to (i), and k=1 gives (1).

## 6. Counterexample search (`out/cex/referee_check.py`, log `out/cex/referee_run.log`)

- **Part A**: exhaustive over n=1..50 (every k<=10 and r). It computes the functional-graph cycles by colouring and compares them with C(k,r). It checks |C| = binom(k,r) and #cycles against both the formula and a brute-force count of rotation orbits. It compares the cycle-length multiset with the orbit sizes. At r=k, it checks that every partition reaches δ_k. All match.
- **Part B**: n=1..35, 81155 partitions. It checks Lemma 1, Lemma 3(a)(b)(c), Lemma 4 on sort-free steps, strict decrease on the other steps, Lemma 6(b) on cyclic partitions, and Prop. 7 on cyclic partitions. All hold.
- **Part C**: Thm 9(a),(d) for all e with k<=16, and N(k,r) against brute force for k<=16. All hold.
- **Part D**: the statement's example chain holds.
- **Part R**: Lemma 2 on 200000 random sequences (seed 12345) holds.
- **Runtime**: real 5.85 s. Result: no counterexample found.
