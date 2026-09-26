Statement proved (PARTIAL, not the cell): every induced forest F of Q_9 whose complement S = V \ F has at most 3 vertices of even weight, or at most 3 vertices of odd weight, has |F| <= 279; consequently every labelling f of Q_9 for which S_f = {v : v has >= 2 neighbours with smaller label} has at most 3 vertices of one parity has at least 2376 uphill paths. U(Q_9) >= 2369 itself is NOT proved (it would follow from the missing Lemma R9 in Step 11).

Reading of the brief: none ambiguous. Definitions (labelling, valley, uphill path, Q_9) exactly as in
inbox/statement.md. Only Lemma A (inbox/lemmaA-claims.md) is taken as given; everything else is proved here.

## Notation
V = {0,1}^9, E / O = vertices of even / odd Hamming weight (|E| = |O| = 256). e_j = j-th unit vector,
x + y = coordinatewise sum mod 2, d(x,y) = Hamming distance. Every edge of Q_9 joins E and O. For an induced
forest F (a vertex set such that Q_9[F] has no cycle): S = V \ F, M = F n E, Z = S n O = O \ F, m = |M|, z = |Z|.
Then |F| = |M| + |F n O| = m + 256 - z.                                                             (0)
G_2[M] = graph with vertex set M, x ~ x' iff d(x,x') = 2; tau(G_2[M]) = its minimum vertex-cover size.
For o in Z: K_o = N(o) n M (the neighbours of o that lie in M), t_o = |K_o|, D(o) = {j : o + e_j in M}.

## Step 1 (Lemma A, assumed, stated in full as the brief requires)
Lemma A (inbox/lemmaA-claims.md, section A): let d >= 1 and f a labelling of Q_d; down(v) = number of
neighbours w of v with f(w) < f(v); S_f = {v : down(v) >= 2}, T_f = V \ S_f. Then (i) Q_d[T_f] has no cycle,
and (ii) the number of uphill paths of f is at least 2^d + (d-1)|S_f|. Hence U(Q_d) >= 2^d + (d-1)(2^d - F_d),
F_d = the maximum size of an induced forest of Q_d.

## Step 2 (reduction)
If every induced forest of Q_9 has at most 279 vertices, then for every labelling f, |T_f| <= 279 by
Lemma A(i), so |S_f| >= 512 - 279 = 233 and by Lemma A(ii) the number of uphill paths is
>= 512 + 8*233 = 2376 >= 2369. So the cell's LOWER route reduces to F_9 <= 279 (rung R10).

## Step 3 (parity swap)
sigma(x) = x + e_1 is an automorphism of Q_9 (d(sigma x, sigma y) = d(x,y)) and maps E onto O and O onto E.
If F is an induced forest then so is sigma(F) (sigma restricts to an isomorphism Q_9[F] -> Q_9[sigma F]),
|sigma F| = |F|, and O \ sigma(F) = sigma(E \ F), E \ sigma(F) = sigma(O \ F). Hence it suffices to prove
the Theorem of Step 9 under the hypothesis z = |O \ F| <= 3; the case |E \ F| <= 3 follows by applying it
to sigma(F).

## Step 4 (Lemma 1: distance-2 pairs of M are covered by Z)
Let F be an induced forest and x != x' in M with d(x,x') = 2, say x' = x + e_i + e_j (i != j).
Their common neighbours are exactly a = x + e_i and b = x + e_j (a vertex adjacent to both differs from x in
one coordinate and from x' in one coordinate, so it is x + e_i or x + e_j). a != b, both odd, and
x, a, x', b are four distinct vertices with x ~ a ~ x' ~ b ~ x. If a, b were both in F, Q_9[F] would contain
this 4-cycle. So a or b lies in O \ F = Z. Call it o; then x, x' in N(o) n M = K_o.
Consequence: every edge of G_2[M] has both ends in K_o for some o in Z.

## Step 5 (Lemma 2: an o in Z with many M-neighbours forces further Z-vertices)
Let o in Z, t = t_o >= 1. Define the graph H_o on vertex set D(o): {i,j} is an edge iff w_ij := o + e_i + e_j
lies in F. Claim: H_o has no cycle.
Proof. Suppose j_1, ..., j_r (r >= 3, distinct) is a cycle of H_o (j_s ~ j_{s+1} for s < r and j_r ~ j_1).
Put u_s = o + e_{j_s} (in M, since j_s in D(o)) and w_s = o + e_{j_s} + e_{j_{s+1}} (indices mod r; in F since
{j_s, j_{s+1}} is an edge of H_o). u_s and w_s differ exactly in coordinate j_{s+1}, and w_s and u_{s+1} differ
exactly in coordinate j_s, so u_1 w_1 u_2 w_2 ... u_r w_r u_1 is a closed walk in Q_9[F]. Its 2r vertices are
distinct: the u_s are distinct because the j_s are; the w_s are distinct because the r edges
{j_s, j_{s+1}} of a cycle (r >= 3) in a simple graph are distinct 2-sets; u's are even, w's are odd. So it is a
cycle of length 2r in Q_9[F], a contradiction.
A graph without cycles on t >= 1 vertices has at most t - 1 edges, so at least C(t,2) - (t-1) = (t-1)(t-2)/2
of the 2-sets {i,j} in D(o) are non-edges, i.e. have w_ij not in F. w_ij is odd, so w_ij in Z. Distinct 2-sets
give distinct w_ij, and w_ij != o (they differ in two coordinates). Hence
   z >= 1 + (t_o - 1)(t_o - 2)/2   for every o in Z with t_o >= 1.                                  (1)
In particular: z <= 2 implies t_o <= 3 for all o in Z ((t-1)(t-2)/2 <= 1 forces t <= 3); z = 1 implies t_o <= 2;
z = 3 implies t_o <= 3 ((t-1)(t-2)/2 <= 2 forces t <= 3).

## Step 6 (Lemma 3: codes of even words, length 9, distance >= 4, have <= 21 words)
Let C be a nonempty subset of E with no two words at distance 2. Distances between even words are even, so
distinct words of C are at distance 4, 6 or 8. Let N = |C| and a_i = #{(x,y) in C x C : d(x,y) = i}; then
a_0 = N and N^2 = a_0 + a_4 + a_6 + a_8.
(I1) sum_{j=1}^{9} (sum_{x in C} (-1)^{x_j})^2 >= 0. Expanding the square, the left side equals
     sum_{x,y in C} sum_j (-1)^{x_j + y_j} = sum_{x,y} (9 - 2 d(x,y)), because (-1)^{x_j+y_j} = -1 exactly for
     the d(x,y) coordinates where x and y differ. So 9 a_0 + 1 a_4 - 3 a_6 - 7 a_8 >= 0.
(I2) sum_{1<=j<l<=9} (sum_{x in C} (-1)^{x_j + x_l})^2 >= 0. The left side equals
     sum_{x,y} sum_{j<l} eps_j eps_l with eps_j = (-1)^{x_j+y_j}; since (sum_j eps_j)^2 = 9 + 2 sum_{j<l} eps_j eps_l
     and sum_j eps_j = 9 - 2d(x,y), the inner sum is ((9 - 2d)^2 - 9)/2 = 36, -4, 0, 20 for d = 0, 4, 6, 8.
     So 36 a_0 - 4 a_4 + 0 a_6 + 20 a_8 >= 0.
(I3) a_8 <= N: the words at distance 8 from x are x + (11...1) + e_j, j = 1..9; two of them differ exactly in
     two coordinates, so C contains at most one of them; sum over x in C.
Adding (I1) and (I2): 45 N - 3 a_4 - 3 a_6 + 13 a_8 >= 0, i.e. a_4 + a_6 <= 15 N + (13/3) a_8. Then
   N^2 = N + (a_4 + a_6) + a_8 <= N + 15 N + (16/3) a_8 <= 16 N + (16/3) N = (64/3) N    (by I3),
so N <= 64/3 < 22, i.e. N <= 21. (Arithmetic re-checked exactly by code/check_code_bound.py; this is the
Delsarte linear-programming inequality for k = 1, 2, here proved directly. The dual multipliers 1/3, 1/3, 16/3
were found by an exact LP, code/lp_explore.py; the proof does not depend on that search.)

## Step 7 (general inequality, valid for every induced forest)
Let C* be a minimum vertex cover of G_2[M]. M \ C* has no two words at distance 2, so by Step 6
|M \ C*| <= 21 (or M \ C* is empty), i.e. m <= 21 + tau(G_2[M]). With (0):
   |F| <= 277 + tau(G_2[M]) - z.                                                                   (2)
Also, by Step 4, for any choice of one vertex r_o in each nonempty K_o, the set C = union over o in Z of
(K_o \ {r_o}) is a vertex cover of G_2[M] (an edge {x,x'} lies in some K_o, and at most one of x, x' is r_o).
Hence tau(G_2[M]) <= sum_{o in Z, t_o >= 1} (t_o - 1).                                              (3)

## Step 8 (cases z = 0, 1, 2, 3)
Let F be an induced forest with z = |O \ F| <= 3.
 * z = 0: Z is empty, G_2[M] has no edge (Step 4), tau = 0, |F| <= 277 by (2).
 * z = 1: t_o <= 2 by (1), tau <= 1 by (3), |F| <= 277 + 1 - 1 = 277.
 * z = 2: t_o <= 3 for both o by (1), tau <= 2 + 2 = 4 by (3), |F| <= 277 + 4 - 2 = 279.
 * z = 3: t_o <= 3 for all three o by (1).
   - If every t_o <= 2: tau <= 3 by (3), |F| <= 277.
   - Otherwise some o1 in Z has t_{o1} = 3, K_{o1} = {o1 + e_i, o1 + e_j, o1 + e_k}. By Step 5 (t = 3 gives at
     least one non-edge of H_{o1}) one of the three vertices o1 + e_p + e_q ({p,q} in {i,j,k}) lies in Z;
     rename so that o2 := o1 + e_i + e_j in Z. Then a := o1 + e_i = o2 + e_j and b := o1 + e_j = o2 + e_i are
     in M and adjacent to o2, so {a, b} is contained in K_{o1} and in K_{o2}. Let o3 be the third vertex of Z and
     C = {a, b} u (K_{o3} minus one vertex, or empty if K_{o3} is empty); |C| <= 2 + 2 = 4.
     C covers G_2[M]: an edge {x, x'} lies in K_o for some o in Z (Step 4). If o = o1, then x, x' would both lie
     in K_{o1} \ C, which has at most 1 element (K_{o1} \ {a,b} = {o1 + e_k}). If o = o2, K_{o2} has at most 3
     elements (t_{o2} <= 3) and contains a, b, so K_{o2} \ C has at most 1 element. If o = o3, K_{o3} \ C has at
     most 1 element. In each case one of x, x' is in C. So tau <= 4 and |F| <= 277 + 4 - 3 = 278.
In all cases |F| <= 279.

## Step 9 (Theorem)
If F is an induced forest of Q_9 with |O \ F| <= 3 or |E \ F| <= 3, then |F| <= 279.
Proof: the first case is Step 8; the second follows by applying Step 8 to sigma(F) (Step 3).

## Step 10 (Corollary for labellings)
Let f be a labelling of Q_9 and S_f = {v : down(v) >= 2}. If |S_f n E| <= 3 or |S_f n O| <= 3, then f has at
least 2376 uphill paths.
Proof: T_f = V \ S_f is an induced forest (Lemma A(i)), and E \ T_f = S_f n E, O \ T_f = S_f n O. By Step 9,
|T_f| <= 279, so |S_f| >= 233, and Lemma A(ii) gives at least 512 + 8*233 = 2376 uphill paths.
Equivalently: any labelling with at most 2368 uphill paths must have at least 4 vertices of EACH parity with
>= 2 lower neighbours.

## Step 11 (what is missing for the cell) [GAP]
By (2) and Step 2, the cell's bound U(Q_9) >= 2369 (indeed >= 2376) would follow from
   R9 (missing): for every induced forest F of Q_9 with z = |O \ F| <= |E \ F|: tau(G_2[F n E]) <= z + 2.
Step 8 proves R9 for z <= 3 (there tau - z <= 2). For z >= 4 the clique-cover bound (3) is too weak: (1) only
forces t_o <= 4 at z = 4 and allows t_o up to 9 once z >= 29, and then sum_o (t_o - 1) can be far above z + 2
(up to 8z), because the cliques K_o overlap heavily and (3) ignores the overlaps. For large z, tau(G_2[M]) is a
global quantity (when M is most of E it is |M| minus the largest distance-4 code inside M), so a proof of R9
needs either a global counting/LP argument or an exhaustive search; neither was completed.
(Note: under the normalisation z <= |E \ F| and |F| >= 280 one has z <= 116 by (0).)
[GAP: R9 is not proved for 4 <= z <= 116. Hence neither F_9 <= 279 nor U(Q_9) >= 2369 is established here.]

## What is established / not established
 * Established: Steps 3-10 (Lemma 1, Lemma 2, Lemma 3 with N <= 21, inequality (2) for all forests, the
   Theorem for forests missing at most 3 vertices of one parity class, and the labelling Corollary), given
   Lemma A.
 * Not established: U(Q_9) >= 2369. The strongest unconditional lower bound available to this worker remains
   U(Q_9) >= 2312 (subject H-C5-002, Steps 8-9: edge counting, |S_f| >= 225; with Lemma A(ii) the same number:
   an induced forest F has at most |F| - 1 edges and at least 2304 - 9|S| edges, so 8|S| >= 1793, |S| >= 225,
   and 512 + 8*225 = 2312). This is below the organisers' 2368.
