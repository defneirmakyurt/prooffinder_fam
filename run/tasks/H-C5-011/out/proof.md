Statement proved (PARTIAL, not the cell): every induced forest F of Q_9 with |O \ F| <= 5 or |E \ F| <= 5 has |F| <= 277 (more precisely: if z = |O \ F| <= 5 then tau(G_2[F n E]) <= z, which is rung R9 for z <= 5); consequently every labelling f of Q_9 whose set S_f = {v : v has >= 2 neighbours with smaller label} contains at most 5 vertices of one parity has at least 2392 uphill paths. U(Q_9) >= 2369 is NOT proved: R9 remains open for 6 <= z <= 116.

Reading of the brief: none ambiguous. Definitions (labelling, valley, uphill path, Q_9) exactly as in
inbox/statement.md. Only Lemma A (inbox/gated-lemmaA.md) is assumed; every other step is proved here, or is a
finite exact computation (Step 12) whose reduction is written out in Steps 10-12. Steps 2-7 re-prove, in
self-contained form, the parts of the subject H-C5-007 that are re-used; Steps 8-15 are new.

## Notation
V = {0,1}^9; E / O = vertices of even / odd Hamming weight, |E| = |O| = 256. e_j = j-th unit vector,
x + y = coordinatewise sum mod 2, d(x,y) = Hamming distance, N(x) = set of the 9 neighbours of x.
Every edge of Q_9 joins E and O, and d(x,y) is even iff x, y have the same parity.
An induced forest is a set F of vertices such that Q_9[F] has no cycle.
For an induced forest F: M = F n E, P = F n O, Z = O \ F, z = |Z|, m = |M|. Then
   |F| = m + (256 - z).                                                                         (0)
G_2[X] (X a set of vertices of one parity) = graph on X with x ~ x' iff d(x,x') = 2;
tau(G) = minimum size of a vertex cover of G (a set meeting every edge), alpha(G) = maximum size of an
independent set. For every graph G on n vertices, tau(G) = n - alpha(G) (the complement of an independent set is
a vertex cover and conversely).
For o in Z: K_o = N(o) n M, t_o = |K_o|.

## Step 1 (Lemma A, assumed; statement as in inbox/gated-lemmaA.md)
For a labelling f of Q_d let down(v) = number of neighbours w of v with f(w) < f(v), S_f = {v : down(v) >= 2},
T_f = V \ S_f. Then (i) Q_d[T_f] has no cycle and (ii) the number of uphill paths of f is >= 2^d + (d-1)|S_f|.

## Step 2 (parity swap)
sigma(x) = x + e_1 satisfies d(sigma x, sigma y) = d(x, y), so it is an automorphism of Q_9; it maps E onto O and
O onto E. If F is an induced forest, sigma restricts to an isomorphism Q_9[F] -> Q_9[sigma F], so sigma(F) is an
induced forest with |sigma F| = |F|, and O \ sigma(F) = sigma(E \ F).

## Step 3 (Lemma 1: distance-2 pairs of M have a common neighbour in Z)
Let F be an induced forest, x != x' in M, d(x,x') = 2, x' = x + e_i + e_j (i != j). A common neighbour of x and x'
differs from x in one coordinate and from x' in one coordinate, so it is a = x + e_i or b = x + e_j. a != b, both
are odd, and x, a, x', b are four distinct vertices with x ~ a ~ x' ~ b ~ x. If a and b were both in F, this
4-cycle would lie in Q_9[F]. So a or b lies in O \ F = Z; call it o. Then x, x' are in N(o) n M = K_o.

## Step 4 (Lemma 3: even-weight codes of length 9 with minimum distance >= 4 have <= 21 words)
Let C be a nonempty subset of E with no two words at distance 2. Distinct words of C are at distance 4, 6 or 8.
Let N = |C| and a_i = #{(x,y) in C x C : d(x,y) = i}; a_0 = N and N^2 = a_0 + a_4 + a_6 + a_8.
(I1) 0 <= sum_{j=1}^{9} (sum_{x in C} (-1)^{x_j})^2 = sum_{x,y in C} sum_j (-1)^{x_j + y_j}
     = sum_{x,y} (9 - 2 d(x,y)) (the term is -1 exactly at the d(x,y) coordinates where x, y differ),
     so 9 a_0 + a_4 - 3 a_6 - 7 a_8 >= 0.
(I2) 0 <= sum_{1<=j<l<=9} (sum_{x in C} (-1)^{x_j + x_l})^2 = sum_{x,y} sum_{j<l} eps_j eps_l with
     eps_j = (-1)^{x_j + y_j}. Since (sum_j eps_j)^2 = 9 + 2 sum_{j<l} eps_j eps_l and sum_j eps_j = 9 - 2 d(x,y),
     the inner sum is ((9 - 2d)^2 - 9)/2 = 36, -4, 0, 20 for d = 0, 4, 6, 8. So 36 a_0 - 4 a_4 + 20 a_8 >= 0.
(I3) a_8 <= N: the words at distance 8 from x are x + (1,...,1) + e_j (j = 1..9); two of them are at distance 2,
     so C contains at most one of them; sum over x in C.
(I1) + (I2): 45 N - 3 a_4 - 3 a_6 + 13 a_8 >= 0, i.e. a_4 + a_6 <= 15 N + (13/3) a_8. Then
     N^2 = N + (a_4 + a_6) + a_8 <= 16 N + (16/3) a_8 <= 16 N + (16/3) N = (64/3) N by (I3),
so N <= 64/3 < 22, i.e. N <= 21. (Arithmetic re-checked by code/check_code_bound.py, copied unchanged from the
subject; see RAN.)

## Step 5 (inequality (2), valid for every induced forest of Q_9)
Let F be an induced forest and X a minimum vertex cover of G_2[M]. M \ X has no two words at distance 2, so by
Step 4 |M \ X| <= 21 (trivially if M \ X is empty). Hence m <= 21 + tau(G_2[M]) and, by (0),
   |F| <= 277 + tau(G_2[M]) - z.                                                                   (2)

## Step 6 (reduction of the cell to F_9 <= 279; unchanged from the subject)
If every induced forest of Q_9 has <= 279 vertices then for every labelling f, |T_f| <= 279 by Step 1(i), so
|S_f| >= 233 and by Step 1(ii) f has >= 512 + 8*233 = 2376 >= 2369 uphill paths.

## Step 7 (the missing rung R9, as in the lineage)
R9: for every induced forest F of Q_9 with z = |O \ F| <= |E \ F|: tau(G_2[F n E]) <= z + 2.
By (2), R9 implies F_9 <= 279 (Step 2 handles |E \ F| < |O \ F|). If |F| >= 280 and z <= |E \ F| then by (0)
280 <= |F| = 512 - z - |E \ F| <= 512 - 2z, so z <= 116; hence only 0 <= z <= 116 matters.

## Step 8 (definition: clusters)
Fix an induced forest F. Let Gamma_Z be the graph on Z in which o ~ o' iff d(o,o') = 2. A cluster is the vertex
set of a connected component of Gamma_Z. Clusters partition Z. For a cluster C put M_C = M n N(C) (the vertices of
M adjacent to at least one vertex of C) and N_E(C) = E n N(C).

## Step 9 (every edge of G_2[M] lies inside one M_C)
Let {x, x'} be an edge of G_2[M]. By Step 3 there is o in Z with x, x' in N(o). o lies in some cluster C, and then
x, x' are in M n N(C) = M_C. Consequently, if X_C is a vertex cover of G_2[M_C] for each cluster C, then the union
of the X_C meets every edge of G_2[M] (each edge has both ends in some M_C and is then met by X_C). Hence
   tau(G_2[M]) <= sum over clusters C of tau(G_2[M_C]).                                           (4)

## Step 10 (local validity of M_C)
For a set C of odd vertices call a set M' of even vertices C-valid if M' is contained in N_E(C) and the graph
L(C, M') := Q_9[M' u (N_O(M') \ C)] has no cycle, where N_O(M') = odd vertices adjacent to some vertex of M'.
Claim: for every cluster C of an induced forest F, M_C is C-valid.
Proof. M_C is contained in N_E(C) by definition. Let w be in N_O(M_C) \ C: w is adjacent to some x in M_C, and x is
adjacent to some o in C. Then w and o are odd and d(w, o) <= 2, so d(w, o) is 0 or 2. If w were in Z, then either
w = o (in C) or d(w, o) = 2, i.e. w ~ o in Gamma_Z, so w would lie in the same component as o, i.e. in C. Since
w is not in C, w is not in Z; w is odd, so w is in O \ Z = P, a subset of F. Also M_C is a subset of M, a subset of F.
So L(C, M_C) is an induced subgraph of Q_9[F]; a cycle in it would be a cycle in Q_9[F]. So it has no cycle.

Define tau*(C) = max { tau(G_2[M']) : M' C-valid } (the empty set is C-valid, so the max exists; N_E(C) is
finite). By the Claim, tau(G_2[M_C]) <= tau*(C) for every cluster C of every induced forest.       (5)

## Step 11 (invariance of tau* under the parity-preserving automorphisms)
Let g(x) = pi(x) + v with pi a permutation of the 9 coordinates and v in E. g preserves Hamming distance, so it
is an automorphism of Q_9; weight(g(x)) = weight(pi x) + weight(v) mod 2 = weight(x) mod 2, so g maps O onto O and
E onto E. Hence g(N_E(C)) = N_E(gC), g(N_O(M') \ C) = N_O(gM') \ gC, g restricts to an isomorphism
L(C, M') -> L(gC, gM') and to an isomorphism G_2[M'] -> G_2[gM']. So M' is C-valid iff gM' is gC-valid, with the
same tau, and tau*(gC) = tau*(C). Also g maps sets connected in the distance-2 graph on O to such sets.
Call two sets of odd vertices equivalent if one is the image of the other under such a g.

## Step 12 (computation, CHECKED: tau*(C) <= |C| for every set C of <= 5 odd vertices connected in the distance-2 graph)
Program: code/cluster_tau.py (stdlib Python, exact integer/bitmask arithmetic). Command and output under RAN.
What it does, and why it covers every such C:
 (a) Enumeration. Layer 1 = {{o0}}, o0 = e_1. Every single odd vertex o is equivalent to {o0} via g(x) = x + o + o0
     (o + o0 is even). Layer k is obtained from layer k-1 by adding to each kept representative R every odd w at
     distance 2 from some element of R and not in R, and keeping, for each key value, the first generated set with that
     key. Coverage, by induction on k, of the statement IH(k): every connected k-set is equivalent to a kept
     representative of layer k. IH(1) holds as just said. Let C be a connected k-set (k >= 2). A spanning tree of the
     connected graph (C, distance 2) has a leaf l; C' = C \ {l} is connected, so by IH(k-1) h(C') = R for a kept
     representative R of layer k-1 and some h of the form in Step 11. h preserves distances, so h(l) is odd, not in R,
     and at distance 2 from an element of R; hence h(C) = R u {h(l)} is generated at step k. The kept representative
     R' of the key of h(C) has the same key as h(C), so by (b) R' is equivalent to h(C), hence to C. This proves IH(k).
 (b) Key. key(C) = min, over o in C and over a set of orderings (c_1,...,c_k) of C chosen by the program (all
     orderings compatible with sorting the rows c + o by the invariant (weight of c + o, sorted list of distances to the
     other rows); rows with equal invariant are permuted in every way), of the sorted list of the 9 columns of the
     k x 9 0/1 matrix with rows c_i + o. Whatever orderings are used: if key(C) = key(C'), the two minimising matrices
     have the same multiset of columns, so some coordinate permutation pi maps the rows of the first (in order) onto
     the rows of the second: {c' + o' : c' in C'} = pi({c + o : c in C}), i.e. C' = pi(C) + (pi(o) + o'), and
     pi(o) + o' is even (both odd). So equal keys imply equivalence. (The converse is not needed: a non-canonical key can
     only keep two equivalent representatives, which costs time but loses nothing.)
 (c) Evaluation. For each kept representative C of size k the program decides whether some C-valid M' has
     tau(G_2[M']) > k, by depth-first search over subsets of the candidate list N_E(C) in increasing index order:
     - C-validity is closed under subsets (if M'' is contained in M', L(C, M'') is an induced subgraph of L(C, M')),
       so every C-valid set is a node of the search tree (all its prefixes are C-valid) unless an ancestor is pruned.
     - Acyclicity test when adding x to a C-valid M': the new vertices of L are x and those odd neighbours of x outside
       C that are not yet present; the latter are adjacent to no vertex of M' (otherwise they would be present), so they
       are leaves at x; x is even, so all its edges go to odd vertices. Hence a cycle appears iff two present odd
       neighbours of x outside C lie in the same component of the old L. The program keeps a component label for every
       odd vertex of L and applies exactly this test; after adding x, it relabels the merged components.
     - tau(G_2[M']) = |M'| - alpha(G_2[M']), alpha computed by exhaustive include/exclude branching.
     - Pruning (only when it is certain that no C-valid superset in this subtree has tau > k). Let "later" = the
       candidates after the current index that are individually addable to the current M'. Every C-valid superset
       of M' in the subtree is contained in M' u later (each of its extra elements x makes M' u {x} C-valid by
       closure under subsets). Bound 1: tau(G_2[M' u R]) <= tau(G_2[M']) + |R| (add R to a cover). Bound 2: for a
       C-valid M'', every edge {y, y'} of G_2[M''] has a common neighbour in C (its two common neighbours are odd; if
       neither were in C, both would be in N_O(M'') \ C and y, a, y', b would be a 4-cycle in L(C, M'')), so taking,
       for each o in C, all but one element of N(o) n M'' gives a cover: tau(G_2[M'']) <= sum_{o in C}
       (|N(o) n M''| - 1)^+. Moreover |N(o) n M''| <= |N(o) n (M' u later)| and |N(o) n M''| <= cap(o), where cap(o)
       is the largest t <= 9 with (t-1)(t-2)/2 <= c2(o) := #{o' in C : d(o,o') = 2}. Proof of the cap (Lemma 2 of the
       subject, localised): let D = {i : o + e_i in M''}, t = |D|, and H the graph on D with {i,j} an edge iff
       o + e_i + e_j is not in C. If H had a cycle j_1 ... j_r (r >= 3), then u_s = o + e_{j_s} (in M'') and
       w_s = o + e_{j_s} + e_{j_{s+1}} (indices mod r; odd, not in C, adjacent to u_s, so in N_O(M'') \ C) would form the
       closed walk u_1 w_1 u_2 w_2 ... u_r w_r u_1 in L(C, M''); its 2r vertices are distinct (the u_s because the j_s
       are distinct, the w_s because the r edges of a cycle are distinct 2-sets, u's even and w's odd), so it is a
       cycle: impossible. So H is acyclic, has <= t - 1 edges, and at least C(t,2) - (t-1) = (t-1)(t-2)/2 pairs {i,j}
       of D give distinct vertices o + e_i + e_j of C at distance 2 from o; hence (t-1)(t-2)/2 <= c2(o).
       Bound 2 is sum_{o in C} (min(cap(o), |N(o) n (M' u later)|) - 1)^+. The subtree is skipped iff bound 1 or
       bound 2 is <= k.
     Output for k = 1..5: "clusters with tau*(C) > k+0: 0" for every k, i.e. tau*(C) <= |C| for every class.
 (d) Self-tests (not needed for the proof): with threshold k - 1 (second argument -1) the program finds C-valid
     sets with tau = k for 1, 1, 2, 5 of the 1, 1, 2, 8 classes of sizes 1..4; the exact unpruned evaluator (second
     argument 99) gives the histogram of tau*(C) - k: {0:1}, {0:1}, {0:2}, {-1:3, 0:5} for k = 1..4, consistent with
     both pruned runs; code/crosscheck_validity.py rebuilds, for k <= 3, the whole C-valid family with a from-scratch
     union-find on the explicit graph L(C, M'), finds it identical to the family produced by the incremental test,
     and recomputes max tau by brute-force minimum vertex cover (max tau - k = 0 for all classes).
By Step 11 and (a), (b), every connected set C of <= 5 odd vertices is equivalent to a checked representative,
so tau*(C) <= |C| for all of them.

## Step 13 (Theorem: R9, indeed tau <= z, for z <= 5)
Let F be an induced forest of Q_9 with z = |O \ F| <= 5. Every cluster C of F has |C| <= z <= 5 and is connected in
the distance-2 graph, so by (5) and Step 12, tau(G_2[M_C]) <= tau*(C) <= |C|. By (4) and because the clusters
partition Z, tau(G_2[M]) <= sum_C |C| = z. By (2), |F| <= 277 + z - z = 277.
If instead |E \ F| <= 5, apply this to sigma(F) (Step 2): |O \ sigma F| = |E \ F| <= 5, so |F| = |sigma F| <= 277.
(For z = 0 there are no clusters, the sum is empty, tau(G_2[M]) = 0 by Step 3.)

## Step 14 (Corollary for labellings)
Let f be a labelling of Q_9 with |S_f n E| <= 5 or |S_f n O| <= 5. T_f is an induced forest (Step 1(i)) with
E \ T_f = S_f n E and O \ T_f = S_f n O, so |T_f| <= 277 by Step 13, |S_f| >= 235, and by Step 1(ii) f has at least
512 + 8*235 = 2392 uphill paths. Equivalently: a labelling with at most 2391 (in particular at most 2368) uphill
paths has at least 6 vertices of each parity with >= 2 lower neighbours.

## Step 15 (what is missing for the cell) [GAP]
R9 is open for 6 <= z <= 116. Remarks on the gap:
 * The statement "tau(G_2[M]) <= z for every induced forest" (which Step 13 proves for z <= 5) would give F_9 <= 277
   via (2). It cannot be improved in general: let C0 be a largest set of odd words pairwise at distance >= 4 and
   F = E u C0 (a union of stars and isolated vertices, hence an induced forest). Then M = E, z = 256 - |C0|, and
   tau(G_2[E]) = 256 - alpha(G_2[E]) = 256 - |C0| (sigma maps odd codes to even codes and back), so tau = z.
 * Extending Step 12 to clusters of size k costs k! * k per canonical key and a branch-and-bound per class; clusters
   of size up to 116 cannot be enumerated this way. A proof for large z needs a global argument (e.g. that every
   cluster satisfies tau*(C) <= |C|, which the computation supports for |C| <= 5, proved uniformly in |C|).
 * Heuristic search (code/sa_forest.c, simulated annealing, exploratory only, NOT evidence in the proof) found induced
   forests of size 276 but none larger in 3 runs of 2.5e7 moves; all three have one parity class missing 0 or 1 vertex
   (covered by Step 13), so no forest found has a large cluster to test the conjecture tau*(C) <= |C| on.
 * The cluster size-6 layer (python3 code/cluster_tau.py 6) did not finish within 10 minutes (TIMED OUT).

## What is established / not established
 * Established (given Lemma A): Steps 2-14; in particular R9 (even tau <= z) for z <= 5, and |F| <= 277 for every
   induced forest missing at most 5 vertices of one parity; the labelling corollary (>= 2392 paths when S_f has
   <= 5 vertices of one parity). This strengthens the subject's z <= 3 case from 279 to 277 and extends it to z <= 5.
 * Not established: R9 for 6 <= z <= 116; F_9 <= 279; U(Q_9) >= 2369. The strongest unconditional lower bound
   available here remains U(Q_9) >= 2312 (edge counting, as in the subject).

## Computations (all stdlib Python, exact; run from out/code/)
 * python3 cluster_tau.py 5 -> k=1..5: classes 1, 1, 2, 8, 31; "clusters with tau*(C) > k+0: 0" for every k.
   COMPLETED, real 2m32.5s (user 1m43s). This is the only computation Step 12 rests on.
 * python3 cluster_tau.py 4 -1 -> violations 1, 1, 2, 5 (self-test). COMPLETED, 1.9 s.
 * python3 cluster_tau.py 4 99 -> exact histograms {0:1}, {0:1}, {0:2}, {-1:3, 0:5}. COMPLETED, 11.3 s.
 * python3 crosscheck_validity.py 3 -> families identical, brute-force max tau - k = 0. COMPLETED, 2.7 s.
 * python3 check_code_bound.py -> ALL OK. COMPLETED, 0.24 s.
 * python3 cluster_tau.py 6 0 prog -> k <= 5 as above, then 19 of 268 size-6 keys checked (0 violations) when the
   run was stopped after about 3.7 minutes (projected > 1 hour). PARTIAL; not used.
 * sa_forest (C, exploratory): seeds 2, 3, 4, 2.5e7 moves each, best 276 each, about 92 s each. Not used.
