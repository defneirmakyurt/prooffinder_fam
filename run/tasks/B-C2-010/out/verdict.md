```
VERDICT: ACCEPT
STATEMENT MATCH: yes
FIRST PROBLEM: none (editorial only: B7 step (a) uses p+m <= q-1, which the induction supplies but I(m) does not state; add "p+m <= q-1" to I(m))
CHECKLIST:
  G1 PASS — proves D_B(T_k) = k^2-k for every k >= 1 with no exceptions; both bounds; no extra hypotheses
  G2 PASS — every step re-derived below; no "clearly"/"similarly"; B7(a) bookkeeping is supplied by the induction (editorial note)
  G3 PASS — k=1 (A.0, B9), k=2 (B9 hand table, A.2 needs k>=2 and has it), k>=3 general; t<=k covers cyclic starts (t=0)
  G4 PASS — E is preserved by rot and drops by >=1 at slides (0.1(a),(d)); B7 length strictly drops; B2 equality/flip form exact
  G5 PASS — witness orbit tracked symbolically for all k>=2 via S(a,b), CRT gives t* = k^2-k-1 for every k>=2
  G6 PASS — uniqueness of delta_k proved in 0.3 (no B-C1 use); no step cites the target
  G7 PASS — no computation is used in the proof; code is sanity only, stdlib, exact integers, all runs < 30 s
  G8 PASS — Griggs-Ho 1998 Thm 3.7 / Lemmas 3.3-3.6 named as source of the architecture only; nothing is used unproved
  G9 PASS — Conclusion states what is established; Part C labelled sanity only
  S1 PASS — F(k)=k^2-k, UPPER (Part B) for all lambda |- T_k, LOWER (Part A) explicit lambda^(k) with d_B = F(k), all k>=1
  S2 PASS — exhaustive exact enumeration k<=11 (n<=66): D_B(T_k)=k^2-k, witness attains it, only cyclic partition is delta_k
  S3 PASS — k=1,2,3, d_B=0, (1^n), (n) all covered by the general argument; witness orbit symbolic in k
  S4 PASS — d_B = cycle-entry time (A.4, 0.3); s counts all parts (B1); sorted insertion (0.1(d)); uniqueness of delta_k proved (0.3)
  S5 PASS — consistent with C1 (0.3 proves delta_k unique cyclic, d_B = hitting time); C5 at k=2 N/A (not gated), F(2)=2 = D_B(3) computed
  S6 PASS — d_B((2,1,1,1,1)) = 3 reproduced; F(3)=6 >= 3; (2,2,1,1) is the unique maximiser at k=3
EQUALITY CASES: Part S lists none (unknown). Witness lambda^(k)=(k-1,k-1,k-2,...,2,1,1) attains k^2-k for k=1..60 (orbit = S(a_t,b_t) at every step); it is among the maximisers for k<=11 (the maximiser counts are 1,1,1,3,16,65,293,1267,5686,25475,115838). The B7 chain length k-3 is attained for k=4..7 (tight counting in B9).
CROSS-CELL: consistent with C1 (delta_k unique cyclic partition of T_k, proved in 0.3 and confirmed exhaustively k<=11); C5 N/A (not gated).
CEX SEARCH: out/cex/exhaustive.py (all partitions of T_k, k<=11, with cycle detection), lemmas.py ((*), B2 flip form, B6, B7 statement + the proof's p' construction, B8 on all partitions n<=26 with c_1..c_70; 0.3 energy/slide claim, B4, B5, B9 chain on T_k, k<=7), family.py (A.2 (i)-(iii) for all (a,b), k<=30; orbit k<=60), s6.py. No counterexample, 0 violations.
OTHER ISSUES: (1) proof.md is plain text, not LaTeX: typeset it before hand-in. (2) B7(a): add "p+m <= q-1" to the invariant I(m) (base: q >= p+3; the step supplies it). (3) Line 48, "or the B-C1 assumption": delete it, since B-C1 is not an available assumption and 0.3 already proves the fact. (4) sources.md, with the full bibliographic entries, is not in the subject: include the entries in the hand-in.
RAN: see the "Runs" section below.
```

## Runs (all stdlib python3, exact integer arithmetic, timed with /usr/bin/time -p)

- subject dbt.py 8: exhaustive D_B(T_k), k=1..8. COMPLETED, real 0.58 s. Values 0,2,6,12,20,30,42,56. Log: out/cex/rerun_dbt.txt
- subject witness.py 40: witness orbit, k=1..40. COMPLETED, real 1.66 s, 0 failures. Log: out/cex/rerun_witness.txt
- subject gh_lemmas.py 30 80: B5-B8 statements, n<=30, c_1..c_80. COMPLETED, real 2.88 s, 0 violations (4411 B5 cases). Log: out/cex/rerun_gh_lemmas.txt
- out/cex/exhaustive.py 10: all partitions of T_k, k=1..10, with cycle detection. COMPLETED, real 2.98 s, failures 0. Log: out/cex/exhaustive_log.txt
- out/cex/exhaustive.py 11: all partitions of T_k, k=1..11 (2,323,520 partitions at k=11). COMPLETED, real 27.79 s, failures 0. Log: out/cex/exhaustive11_log.txt
- out/cex/lemmas.py 26 70 7: (*), B2, B6, B7, B7-construction, B8 on all n<=26 with c_1..c_70; 0.3, B4, B5, B9 on T_k, k<=7. COMPLETED, real 9.17 s, 0 violations. Log: out/cex/lemmas_log.txt
- out/cex/family.py 30 60: A.2 for k=2..30 (8990 diagram pairs); witness orbit for k=1..60. COMPLETED, real 24.39 s, 0 failures. Log: out/cex/family_log.txt
- out/cex/s6.py: the S6 example and the k=2 table. COMPLETED, real 0.03 s. Log: out/cex/s6_log.txt

## Checklist (with reasons)

Part G
- **G1 PASS.** The claim is D_B(T_k) = k^2 - k for every k >= 1 with no exceptions (k=1 gives 0, k=2 gives 2, both matching exhaustive values). The upper bound is proved for every partition of T_k and the lower bound by an explicit witness for every k. There are no extra hypotheses and the inequality is not weakened.
- **G2 PASS.** Every step is re-derived below. There is no hand-waving. The one implicit piece of bookkeeping (B7(a) needs p+m <= q-1) is supplied by the written induction, since I(m+1) is only produced after (a) has shown p+m <= q-2. It is recommended as an explicit clause in I(m).
- **G3 PASS.** k=1 is treated in A.0 and B9. For k=2 the B9 table is correct: (3)->(2,1), (1,1,1)->(3)->(2,1). A.2 needs k >= 2 (so that a=k excludes a=1), and A only uses it for k >= 2. B9's k >= 3 condition is needed for T_k <= k^2-k and for k < k^2-k, and it is assumed exactly there. Starts with d_B = 0 fall under "t <= k".
- **G4 PASS.** Energy E is preserved by rot, which preserves diagonals (0.1(a)). E drops by at least 1 at a slide (0.1(d): at least one cell moves down one diagonal). The B7 length drops strictly (q'-p' < q-p). B2 is an exact identity, c_{i+1} = c_i + 1 - L_i.
- **G5 PASS.** The witness is defined for all k >= 2, plus (1) for k = 1. A.2 is proved for general (a,b) and k >= 2. A.3's CRT computation t0 = k^2-k-1 holds for every k >= 2 (checked: -1 mod k and 1 mod k+1).
- **G6 PASS.** Uniqueness of the cyclic partition is proved in 0.3 and not assumed. Griggs-Ho is cited only as the source of the architecture, and every lemma is re-proved.
- **G7 PASS.** No proof step depends on computation. Part C is labelled sanity only. The code is stdlib, uses exact integers, and each run takes under 30 s.
- **G8 PASS.** The references are given with lemma and theorem numbers (Griggs-Ho 1998 Prop 3.2, Lemmas 3.3-3.6, Thm 3.7; Igusa 1985; Etienne 1991) and are kept separate from the new write-up. The full bibliography is in sources.md, which is not in the subject; it should be added to the hand-in.
- **G9 PASS.** The Conclusion states what is established. Part C is marked as proving nothing for all k.

Part S
- **S1 PASS.** F(k) = k^2-k with no exceptions. UPPER is B9. LOWER is A.1-A.4 with the explicit lambda^(k).
- **S2 PASS.** Exact exhaustive enumeration was run for k=1..11 (the checklist requires k<=10). Results: D_B(T_k) = k^2-k, d_B(lambda^(k)) = k^2-k, and the only cyclic partition is delta_k. The cycle detection does not assume uniqueness.
- **S3 PASS.** k=1,2,3 are covered. For (1^n) and (n), B1-B9 place no restriction on the shape of lambda. The witness orbit is tracked symbolically (S(a_t,b_t)).
- **S4 PASS.** d_B is the entry time: A.4 shows that no earlier iterate is cyclic, and B uses d_B = the first hitting time of delta_k, via 0.3. B1 counts all parts, 1-parts included. 0.1(d) handles the sorted insertion. Uniqueness of delta_k is proved in 0.3.
- **S5 PASS.** Consistent with C1: 0.3 proves the C1 claim for T_k, and exhaustive checks confirm it for k<=11. C5 is N/A (not gated), and F(2) = 2 = D_B(3) as computed.
- **S6 PASS.** The orbit (2,1,1,1,1)->(5,1)->(4,2)->(3,2,1) was reproduced, so d_B = 3 <= F(3) = 6.

## Per-step re-derivation (reason each step holds)

**0.1 Rotation lemma.**
- (a) (i-1)+(j+1)-1 = i+j-1. Both (1,j) and (j,1) lie on diagonal j. On diagonal w, column j maps to j+1 for j<w, and (1,w) maps to (w,1).
- (b) Row 1 becomes column 1, of height s. Column j minus its bottom cell becomes column j+1, of height lambda_j - 1.
- (c) The column heights s, lambda_1-1, lambda_2-1, ... are weakly decreasing iff s >= lambda_1-1.
- (d) Row i of the sorted diagram has length #{columns of height >= i}. For i <= s, column 1 is counted and the other columns form the initial segment 2..m, so the row is unchanged. For i > s, column 1 is excluded, so the row {2..r_i+1} shifts left by one. The cell (s+1,2) exists because lambda_1-1 > s.

**0.2** B(delta_k) = delta_k by direct computation.

**0.3 Convergence and uniqueness.**
- h >= 1 when S != D_k: diagonals 1..k hold exactly T_k positions, so equal cardinalities give h cells outside and h holes inside.
- Choice of w: W0 >= k+1 and w0 <= k, so w exists. Diagonal w+1 is either W0 or full, so it has a cell.
- With no slide, the positions on each diagonal rotate cyclically, and holes map to holes because rot is a bijection on each diagonal's positions.
- CRT (w and w+1 are coprime) puts the hole at (1,w) and the cell at (w+1,1) at some time tau < w(w+1). Then s <= w-1 because row 1 is an initial segment, and mu_1 >= w+1 > s+1, so a slide occurs.
- E is a non-negative integer and drops by at least 1 at each slide, so only finitely many slides occur. Hence the orbit reaches D_k, which is fixed.
- If mu is cyclic, then mu = B^{mp}(mu) = delta_k.
- Checked numerically for k<=7 (0 violations): the E behaviour, and the claim that a slide occurs within w(w+1) steps.

**A.0** T_1 = 1: the only partition is (1), which is fixed.

**A.1** The witness is weakly decreasing, its sum is (k-1) + T_{k-1} + 1 = T_k, and its diagram is D_k - (k,1) + (1,k+1).

**A.2 The family S(a,b).**
- (i) s counts the row-1 cells. The removed cell (k+1-a,a) is in row 1 iff a=k, and the added cell (k+2-b,b) is in row 1 iff b=k+1. The same count for column 1 gives mu_1.
- (ii) s >= k-1 and mu_1 <= k+1. So s < mu_1-1 forces s = k-1 and mu_1 = k+1, i.e. (a,b) = (k,1), because a=k excludes a=1 when k >= 2. Otherwise 0.1(c) applies, and rot shifts the hole and the extra cell cyclically.
- (iii) rot(S(k,1)) has hole (k,1) and extra cell (k,2). The only cell in rows >= k is (k,2), which slides to (k,1), giving D_k.
- Checked for every Young-diagram pair (a,b) with k<=30.

**A.3 The orbit.**
- a_t and b_t advance cyclically, and the induction keeps "S(a_t,b_t) is a diagram" true.
- a_t = k iff t = -1 (mod k), and b_t = 1 iff t = 1 (mod k+1). Then t0 = k^2-k-1 satisfies both (k = -1 mod k+1, so k^2 = 1), and 0 <= t0 < k(k+1). This value is unique by CRT.
- Every iterate before time k^2-k has a cell on diagonal k+1, so none of them is delta_k.

**A.4** If some B^t with t < k^2-k were cyclic, then it would equal B^{mp}(itself) = delta_k, contradicting A.3. So d_B = k^2-k exactly.

**B1 The c-sequence.**
- Induction on t: subtracting 1 and keeping the positive values commutes with the listing, and the new part is c_t (the number of parts of B^{t-1}).
- (*) follows by counting the positive entries.
- c_u >= 1, so e_{i,i-1} = 1.
- (*) checked on all n<=26, t<=70.

**B2** Each entry of row i+1 is at most the corresponding entry of row i (monotone threshold indicators), and row i+1 has the extra entry e_{i+1,i} = 1. A flip in column u at row i is equivalent to c_u = i-u, and in a lambda-column to lambda_j = i. So c_{i+1} = c_i + 1 - L_i, checked exhaustively.

**B3 Sandwich.** Take p maximal in [i,j) with c_p <= x-1. Then c_{p+1} = x, using B2. Next, j >= p+2 (otherwise c_j = x). Take q minimal > p+1 with c_q != x. Then c_q is in [x, x+1] and not equal to x, so c_q = x+1.

**B4** delta_k is fixed with k parts, so c_u = k for u >= t+1. c_t is a part of delta_k, so c_t <= k, and B2 gives c_t >= k-1. If c_t = k, the parts of mu minus 1 are k-1..1 and one 0, so mu = delta_k, which contradicts minimality.

**B5 Patterns at the end of the orbit.**
- Row t has k entries at columns t-k..t-1, and they sum to at most k-1, so some entry is 0. Take the maximal such i. Since L_t = 0 (because c_{t+1} = c_t + 1), e_{t+1,i+1} = 1. B2 then gives c_i = t-i-1 and c_{i+1} = t-i.
- Case i >= t-k+1: c_i <= k-2, so B3 with x = k-1 applies.
- Case i = t-k: three subcases.
  - Some c_j <= k-2: B3 gives (ii).
  - Some c_j >= k+1: B3 with x = k on [t-k, j] gives (i) with q <= t-1.
  - Otherwise the k-1 ones of row t are exactly the columns [t-k+1, t-1]. Then the parts of mu are c_u-(t-1-u), each at most k-v, with total at most T_k - 1 < T_k. Contradiction.
- Checked on all partitions of T_k with t >= k+1, k<=9, via the subject's gh_lemmas (4411 cases) and my own lemmas.py for k<=7.

**B6** Row p+m has m ones: m-1 from columns p+1..p+m-1, column p is 0, and one more column Z.
- Z a lambda-column: p+m <= n.
- Z = u0 >= 2: L_{p+m-1} = 0 and L_{p+m-2} = 1 (the flip at column p). These give e_{p+m-2,u0-1} = 0, so c_{u0} >= c_{u0-1} + 2, contradicting B2.
- Hence u0 = 1 and c_1 >= p+m-1. Since c_1 <= n, p+m <= n+1.
- The index conditions p+m-2 >= p+1 and p < p+m-2 use m >= 3, which holds because c_p = m-2 >= 1.
- Checked: 1464 instances, 0 violations.

**B7 Shortening a pattern.**
- Row p has x entries at columns p-x..p-1 but only x-1 ones, so some entry is 0. With p' maximal, L_p = 0, and as in B5 this gives c_{p'} = y-1 and c_{p'+1} = y, where y = p-p' is in [2, x].
- Invariant I(m): column p'+m ends at row p+m (since c_{p'+m} = y), so it is a flip there.
- (a) This flip is incompatible with c_q = c_{q-1} + 1, so p+m != q-1. Together with p+m <= q-1 this gives p+m <= q-2. The bound p+m <= q-1 holds for m=1 because q >= p+3, and the step preserves it (editorial note (2)). Then L_{p+m} = 1 and the unique flip is p'+m, which propagates the ones to row p+m+1.
- (b) B2 bounds c_{p'+m+1} in [y, y+1].
- Termination occurs at some m <= q-p-2.
- q' <= p+1 because c_p != c_{p+1}.
- Both the statement and the specific construction were checked: 9354 instances, 0 violations.

**B8** Row p has p-1 > c_p entries, so some entry is 0. With i maximal, two B2 equalities propagate e_{.,i+1} = 1 down to row p+2. This gives c_{i+1} >= p-i+1 and c_i <= p-i-1, contradicting B2. Checked: 13402 instances, 0 violations.

**B9 Assembly.**
- k=1,2: by hand, correct.
- t <= k < k^2-k for k >= 3.
- Case (ii) with q = p+k: the ranges force p = t-k+1. Then B6 with m = k gives t <= T_k <= k^2-k (for k >= 3).
- Otherwise q-p <= k-1 and p >= t-k.
- The B7 chain: x_i stays <= k, the length drops by at least 1 per step and stays >= 2, so there are at most k-3 steps. The chain ends with p_m <= x_m <= k, either directly or by B8.
- Hence p_0 <= k + (k-3)k and t <= p_0 + k <= k^2-k.
- Checked on T_k, k<=7: the maximum chain length k-3 is attained, and 0 violations.

## Numerical sanity and counterexample search

- All arithmetic is exact integer arithmetic. There is no floating point anywhere, in the proof or the code.
- **Statement.** Exhaustive over every partition of T_k, k=1..11, with cycle detection that does not assume uniqueness: D_B(T_k) = k^2-k, and the witness attains it. No partition exceeds k^2-k. There is no cyclic partition other than delta_k.
- **Intermediate claims.** 0 violations of (*), B2 flip form, B4, B5, B6, B7 (statement and construction), B8, B9 chain, or the 0.3 slide/energy claims on the ranges listed in the Runs section.
- **Witness family.** 0 failures for A.2 (k<=30) and A.3 (k<=60).
- These are sanity checks on finite ranges. The all-k claim rests on the written proof, which is complete.
