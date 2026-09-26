# Space cards: B-C3-001

### S1 diag-array
SPACE: A2 dynamical space + A1 configuration space (Etienne / Griggs-Ho (0,1)-array with diagonals)
BRANCH: DISCRETE
FIDELITY: EQUIVALENT — lambda <-> set of cells (part a, level b); B = rotate every diagonal a+b=w cyclically (Step 1) then left-shift columns (Step 2); bijective encoding, both directions exact.
FEEDS: proof, construction, obstruction
CHECK: PASSED array-shift == B on all 4507 partitions n<=22; energy E=sum of diagonal indices non-increasing on the same set (checks/translations.py)
TIGHT: n/a
TOOLS: (i) Step 1 preserves diagonals, Step 2 strictly lowers E ("drop"); cyclic <=> no drop ever (GH Thm 2.1) -> for n=T_k-1 the cyclic set is delta_k minus one rim cell, so d_B(lambda) = first time the array is "full on diagonals <= k-1, k-1 ones on diagonal k". (ii) Energy E(lambda)-E(cyclic) bounds the number of drops; for n=T_k-1 all extremizers make their last drop at step D-1 and the Griggs-Ho extremizer makes exactly ONE drop (CHECKED k=4..9), so the extremal transient is a drop-free rotation of length D-1 followed by one drop: the bound in (a)/(b) is a statement about how long a drop-free rotation can last before a forced drop. (iii) For (c) the array is where an explicit description of E_k would be written (GH Thm 3.8 did this for T_k, only necessary conditions). Breaks: tracking many drops by hand is messy; E alone gives only O(n^{3/2})-type counts.
KNOWN: GH Thm 2.1 (Brandt's characterisation) PROVED with this array; GH Thm 3.1 and 4.4(2) constructions "by repeatedly applying the shifting process" (sketched) [https://people.math.sc.edu/griggs/cycling.pdf]; GH Thm 3.8 array conditions for T_k extremizers PROVED necessary, converse COMPUTER-VERIFIED k=4..7 and false at k=8. Etienne 1991 uses the same array (cited in GH and arXiv:2607.17194; not opened).
UNEXPLORED: an array characterisation of E_k (n=T_k-1) analogous to GH Thm 3.8 — not found in GH, EJ, S26, Pham, HN. The single-drop structure of the GH extremizer and the merge point mu_k=(k,k-1,k-1,k-3,...,3,1) (CHECKED k=6..9) not found in those sources.
COST: medium — the construction half of (b) is a direct array computation; (c) needs an equality-case analysis.
PAYOFF: high — carries the construction for (b), and is the natural language for the set in (c).
ANGLE: Encode lambda |- T_k-1 as the Etienne/Griggs-Ho (0,1)-array; B is diagonal rotation plus a left-shift that lowers the energy. First write the orbit of lambda_k=(k-1,k-2,k-2,...,1,1) explicitly (one drop, at step k^2-2k-2), then study which arrays sit at depth k^2-2k-1 via the merge point mu_k.
FIRST TASK: prover: For every k>=4, d_B((k-1,k-2,k-2,k-3,...,2,1,1)) = k^2-2k-1, with B^j written explicitly in array form at j = multiples of k and at the single drop | assumes: GH Thm 2.1 (cyclic = delta_{k-1}+0/1 rim) | output: LaTeX lemma + table of B^{jk}(lambda_k) | stop: proof written or a k where the pattern breaks (check k=4..15 against checks/translations.py).

Translation (full): cell (a,b), 0<=b<lambda_{a+1}, diagonal w=a+b+1. Step 1: (a,b)->(a+1,b-1) for b>=1, (a,0)->(0,a). Step 2: columns (parts) re-sorted, empty ones dropped; a cell moves to a lower diagonal iff Step 2 moves it. Check details: translations.py compares array_shift(lambda) with B(lambda) for all lambda |- n, n<=22 (4507 cases), and E(B(lambda))<=E(lambda).

### S2 seqB-diagram
SPACE: A5/B4 bookkeeping matrix: Griggs-Ho sequence seq_B(lambda)=<c_1,c_2,...>, c_i = #parts of B^{i-1}(lambda), and diagram_B(lambda)
BRANCH: DISCRETE
FIDELITY: EQUIVALENT — lambda -> c is injective (conjugate recovered by lambda'_{i+1} = c_{i+1} - #{m<=i : c_m >= i-m+1}); B acts as left shift of c; B^i(lambda) is the "rectangle below c_i".
FEEDS: proof, bound
CHECK: PASSED recovery formula reconstructs lambda from c on all partitions n<=22; GH Prop 3.2(1) c_{i+1}<=c_i+1 and (2) k-window sums <= k(k-1)+r hold on all lambda, n in [3,22] (checks/translations.py)
TIGHT: n/a
TOOLS: (i) Prop 3.2 (window-sum double count; Sandwich Property) forces patterns (x-1,x,...,x,x+1) in c before the cycle; (ii) Lemmas 3.4-3.6 bound the index p of such a pattern (p<=x, p+k<=n+1, and a descent to smaller patterns), giving "at most k^2-3k-1 terms before c_p" and hence d_B <= k^2-2k-1 for 1<=r<k (GH Thm 4.4(1)). (iii) For (c): equality d_B=k^2-2k-1 forces equality in the chain of Lemmas 3.5/3.6, which pins c_1..c_{D}; since c determines lambda, a full description of the equality sequences IS a description of E_k. Breaks: GH handle k=4 by computer table (Fig. 1) and the chain's equality case is not analysed there.
KNOWN: GH Thm 3.7 (D_B(T_k)=k^2-k) and Thm 4.4(1) (the cell's (a)) PROVED in this space with arguments, k=4 COMPUTER-VERIFIED (Fig. 1) [https://people.math.sc.edu/griggs/cycling.pdf]. GH Thm 3.8 extracted T_k extremizer conditions from the equality case of the same chain (necessary only).
UNEXPLORED: equality-case analysis of GH's chain for r=k-1 (giving (c)) — not found in GH, EJ, S26, Pham, HN, HJ-abstract.
COST: medium — (a) exists in the literature as a route (must be written in full, with k=4 by exhaustive check of 67 partitions); (c) equality case is new work.
PAYOFF: high — delivers (a) and the upper half of (b); likely the most direct route to "no other partition" in (c).
ANGLE: Work with seq_B and diagram_B exactly as Griggs-Ho Sections 3-4 (preprint linked). Reprove Thm 4.4(1) self-contained (the cell needs a written proof; cite nothing as the proof), then run the equality case: d_B=k^2-2k-1 forces which (p,q,x) pattern chain, hence which c_1..c_D.
FIRST TASK: prover: For k>=5 and lambda |- T_k-1 with d_B(lambda)=k^2-2k-1, determine the forced values of seq_B(lambda) (from equality in GH Lemmas 3.3(2), 3.5, 3.6, 4.3) | assumes: GH Prop 3.2, Lemmas 3.3-3.6, 4.3 (re-proved) | output: the forced pattern positions and the induced constraints on lambda; compare with E_k lists from checks/merge.py, k=5..9 | stop: constraints written and checked on k=5..9, or an extremizer in E_k violating the claimed forced pattern.

Translation (full): c_1 = s; c_{i+1} = #{j : lambda_j > i} + #{m<=i : c_m > i-m}. diagram_B: column j of lambda has lambda_j ones on top; the row labelled c_i has c_i ones. B^i(lambda) = column lengths of the rectangle below c_i. Check details: recover_from_seq in translations.py; Prop 3.2 checked over windows up to 3n terms.

### S3 containment-order
SPACE: A3 order/lattice space: Young's lattice (containment of diagrams across different n), Akin-Davis comparison
BRANCH: DISCRETE
FIDELITY: RELAXATION — alpha subset lambda subset beta, |alpha|=T_{k-1}, |beta|=T_k => delta_{k-1} subset B^j(lambda) subset delta_k for j>=max(d(alpha),d(beta)), which is the cyclic form; so d_B(lambda) <= max(min_alpha d(alpha), min_beta d(beta)) (upper bound on the max, one-sided); for n=T_k-1 simply d_B(lambda) <= min_{beta=lambda+cell} d_B(beta).
FEEDS: bound
CHECK: PASSED monotonicity lambda subset mu => B(lambda) subset B(mu) on all 1770 pairs (a, a+cell), |a|<=14; d_B(lambda) <= min_beta d_B(beta) on every lambda |- T_k-1, k=4..7 (checks/order_tree.py)
TIGHT: NO — at n=T_k-1 the relaxed value max_lambda min_beta d(beta) equals k^2-k for k=5,6,7 (20,30,42 vs truth 14,23,34); explicit objects: (3,3,3,3,1,1) |- 14 (d_B=8, every one-cell extension of it has d_B=20), (4,4,4,2,2,1,1,1,1) |- 20, (4,4,4,4,4,2,1,1,1,1,1) |- 27. Also fails at n=T_k-2 (k=6,7).
TOOLS: Akin-Davis monotonicity reduces non-triangular n to the triangular D_B(T_k)=k^2-k (GH Thm 4.2) — delivers only D_B(n)<=k^2-k; cannot give (a) or (b). Useful as a lemma: sandwiching localises the cycle and proves "B^j(lambda) subset delta_k => cyclic" at n=T_k-1.
KNOWN: GH Thm 4.1 (Akin-Davis 1985 Thm 3(c)) and Thm 4.2 (Igusa/Etienne bound k^2-k) PROVED [https://people.math.sc.edu/griggs/cycling.pdf]; GH note Igusa derived it this way.
UNEXPLORED: using the order with a SET of supersets beta simultaneously (min over beta at each time j, not only at the end) — not found in GH, S26; the explicit obstruction above shows the one-shot version cannot work.
COST: low — the lemma is two lines.
PAYOFF: low — only k^2-k; kept as the reason the proof must use more than comparison with T_k.
ANGLE: Young's-lattice comparison (GH Thm 4.1) localises the cycle but loses exactly the k+1 steps the cell is about; use it only as a lemma (cyclicity test at T_k-1), not as the bound.
FIRST TASK: breaker: exhibit for every k>=5 an explicit lambda |- T_k-1 all of whose one-cell extensions have d_B = k^2-k | assumes: nothing | output: family + proof sketch, checked k=5..9 | stop: family found or k where none exists.

Translation (full): order lambda <= mu iff lambda_i <= mu_i for all i. Check details: order_tree.py (min over supersets memoised by add_cell).

### S4 CRT-timing
SPACE: A7 arithmetic space: per-diagonal rotation groups Z/w, CRT on Z/w x Z/(w+1), necklaces (Brandt; Pham; Harris-Nguyen)
BRANCH: NUMBER-THEORY
FIDELITY: RELAXATION — between drops the dynamics is EXACTLY the rotation (a) -> (a+1 mod w) on each diagonal w (equivalent step); the time to the next drop is bounded by a CRT waiting time on diagonals (w,w+1) (bounding step => upper bound on d_B, one-sided).
FEEDS: bound, construction
CHECK: PASSED drop-free steps are pure diagonal rotation (S1 check, n<=22); the GH extremizer lambda_k has a single drop at step D-1, k=4..9, and every extremizer's last drop is at step D-1 (checks/ext_drops.py)
TIGHT: NO — summing waiting times over drops is far from tight: k=5, n=14 has lambda with 9 drops and max gap 14 (product bound 126 vs D=14) (checks/obstruct_gaps.py); tight only on the single-drop extremizer lambda_k.
TOOLS: gcd(w,w+1)=1 => a 0 on diagonal w and a 1 on diagonal w+1 meet at the drop position within w^2-w-1 steps (GH proof of Thm 2.1: Frobenius number of {w,w+1}); for n=T_k-1 the final cycle is the single necklace class with k-1 black beads out of k (Brandt count (1/k) sum_{d|gcd(k,r)} phi(d) C(k/d,r/d) = 1). Delivers: the exact length of the last drop-free stretch (the dominant term of k^2-2k-1 for lambda_k) and an explicit construction. Breaks: multi-drop orbits; no control of how early drops shape the last stretch.
KNOWN: GH Thm 2.1 proof uses the coprimality bound w^2-w-1 PROVED; cycle count and necklace parametrisation (Brandt 1982, cited in GH; Pham thesis and arXiv:2308.05321 PROVED for orbit-size/level generating functions in limit families).
UNEXPLORED: using the CRT waiting time on diagonals (k-1,k) and (k,k+1) as the main counting device for the max depth at T_k-1 — not found in GH, EJ, S26, Pham, HN.
COST: medium — clean for single-drop orbits; multi-drop needs an amortisation (combine with S1 energy).
PAYOFF: medium — likely gives the exact value of the final stretch and the construction; alone it does not bound multi-drop orbits.
ANGLE: Between drops, B is a product of cyclic rotations Z/w on diagonals; a drop at the diagonal boundary (w,w+1) is a CRT event. For n=T_k-1 look at diagonals k-1,k,k+1 only and compute the latest possible first-meeting time; start with the single-drop orbit of lambda_k.
FIRST TASK: prover: For lambda |- T_k-1 whose transient has exactly one drop, d_B(lambda) <= k^2-2k-1, with equality iff ... (determine) | assumes: S1 array translation | output: lemma + list of single-drop extremizers, compared with checks/ext_drops.py k=4..9 | stop: lemma proved or counterexample.

Translation (full): diagonal w holds w cells indexed by position a in Z/w; Step 1 maps a -> a+1 mod w; a drop occurs at time t iff after Step 1 some column of the array has a gap, i.e. (GH) a 0 at (1,w) and a 1 at (w+1,1) on consecutive diagonals. Check details: translations.py (rotation == B on drop-free steps is part of the array check), ext_drops.py (drop profiles of all extremizers).

### S5 reverse-tree
SPACE: A4 graph space: the functional graph of B / reversed game tree (Eriksson-Jonsson reversed moves; Garden of Eden leaves, Hopkins-Jones)
BRANCH: COMPUTATIONAL
FIDELITY: EQUIVALENT — B^{-1}(mu) = {delete row i of mu, add it as first column : mu_i >= #other rows}; E_k = nodes at maximal height in the in-tree of the cycle.
FEEDS: construction, proof (for (c)), disproof of candidate descriptions
CHECK: PASSED reversed rule == B^{-1} on all 4507 partitions n<=22 (checks/reverse_rule.py); E_k = B^{-L_k}(mu_k), L_k=k^2-4k-2, mu_k=(k,k-1,k-1,k-3,...,3,1), d(mu_k)=2k+1, k=6..9 (checks/merge.py)
TIGHT: n/a
TOOLS: (i) E_k is exactly the set of length-L_k legal reversed-move words from mu_k — so (c) reduces to (1) proving every depth-D node passes through mu_k and (2) describing legal words of length L_k from mu_k explicitly; (ii) the contraction profile |B^j(E_k)| (e.g. k=9: 3911,3911,2815,...,2) shows long 2-element plateaus, i.e. two branches that stay distinct for ~k steps: the explicit set is a tree with few branchings near mu_k and bushy near the leaves; (iii) exhaustive enumeration up to k=10-11 feasible for conjecture testing. Breaks: the leaf layer is large (|E_k| = 1,6,34,175,831,3911); an "explicit function of k" description must be structural (array conditions or word language), not a list.
KNOWN: EJ reversed game and level counts near the root for triangular n (F_{2m}, PROVED) [https://www.fq.math.ca/Papers1/55-3/ErikssonJonsson03112017.pdf]; HJ Garden of Eden enumeration (PROVED, abstract). Nothing on E_k found.
UNEXPLORED: the merge point mu_k and the description E_k = B^{-L_k}(mu_k) — not found in GH, EJ, S26, Pham, HN, HJ-abstract; |E_k| not in OEIS.
COST: low (computation) / high (turning it into an explicit proved description).
PAYOFF: high — the only card that directly targets (c); also a strong test harness for S1/S2 claims.
ANGLE: Treat E_k as the set of legal reversed-move words of length k^2-4k-2 starting at mu_k=(k,k-1,k-1,k-3,...,3,1). Enumerate for k<=11, find the word language / array conditions, then hand the conjectured description to S1/S2 for proof.
FIRST TASK: searcher: for k=5..11 compute E_k (via reversed words from mu_k and independently by forward depth), test candidate explicit descriptions (array conditions a la GH Thm 3.8; word language) | assumes: nothing | output: conjectured explicit E_k with exact agreement table | stop: a description matching all k<=11 or 10 min runtime.

Translation (full): the in-forest of B on P(T_k-1) has one cycle (length k); depth = d_B. Check details: reverse_rule.py compares rev(mu) with the true preimage set for every mu, n<=22; merge.py computes E_k, the first common image, and B^{-L}(mu) by forward iteration over all partitions.

### S6 carolina-analogue
SPACE: C3 analogue: Carolina solitaire on compositions (ordered piles), GH Sec. 5
BRANCH: DISCRETE
FIDELITY: ANALOGY — different map (compositions, new pile placed first); results specialise back only through a projection composition -> partition that commutes with the shift, which GH do not claim (not established here).
FEEDS: obstruction (insight only)
CHECK: NOT RUN — no exact specialisation to d_B identified in the time box.
TIGHT: n/a
TOOLS: the same array/sequence machinery gives D_C(T_k)=k^2-1 and D_C(n)<=k^2-k-2 (non-triangular, k>=4): a second instance where the non-triangular bound drops by exactly k+1 from the triangular value, suggesting the drop mechanism in (a) is a general feature of the window-sum argument.
KNOWN: GH Sec. 5 PROVED D_C(T_k)=k^2-1, D_C(n)<=k^2-k-2, lower bounds CONJECTURED sharp [https://people.math.sc.edu/griggs/cycling.pdf].
UNEXPLORED: extremizers of Carolina solitaire at T_k-1 — not found in GH.
COST: medium.
PAYOFF: low.
ANGLE: Compare the Carolina proof of k^2-k-2 with the Bulgarian k^2-2k-1 proof: both lose k+1 from the triangular case; identify the shared step.
FIRST TASK: searcher: tabulate D_C(T_k-1) and its extremizers for k<=6 and compare with E_k | assumes: GH Carolina definition | output: table | stop: table done.

Translation (full): compositions c=(c_1..c_r); shift: subtract 1 from each, prepend r, drop zeros. Check details: not run.
