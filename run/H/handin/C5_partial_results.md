# Uphill paths on the hypercube: C5 partial results (U(Q_9))

STATUS (head, run time 1:40). Nothing here reaches the cell's thresholds (<= 2399 or >= 2369).
Read the status column: only item 1 has passed the gate; items 2-5 are UNREFEREED worker proofs,
copied verbatim below. Referees for item 5 are running now.

| # | Statement | Status | Source (verbatim below) |
|---|---|---|---|
| 1 | Lemma A: every labelling of Q_d has >= 2^d + (d-1)|S| paths, S = {down >= 2}, V \ S an induced forest; hence U(Q_9) >= 512 + 8*nabla(Q_9) (nabla = decycling number = 512 - largest induced forest) | PROVED (gate VALID, cell C4, two referees) | C2-C4_values_and_proof.md, section A |
| 2 | U(Q_9) <= 2400: explicit labelling Q9_2400.txt | COMPUTER-VERIFIED (checker: VERIFIED 2400); equals the organisers' bound, no gain | H-C5-002 Step 10 |
| 3 | nabla(Q_9) >= 225, hence U(Q_9) >= 2312 (unconditional) | UNREFEREED (short counting) | H-C5-002 Steps 8-9 |
| 4 | Every decycling set of Q_d with no edge inside has >= 2^(d-1) - A(d,4) vertices (= 236 at d = 9, citing A(9,4) = 20); so a labelling with <= 2399 paths needs a decycling set of <= 235 vertices that contains an edge | UNREFEREED; A(9,4) = 20 cited, not proved | H-C5-006 Lemma I |
| 5 | Every labelling of Q_9 whose set S_f has at most 3 vertices of one parity class has >= 2376 paths | UNREFEREED; referees running | H-C5-007 proof.md |

Published context (literature agents, sources opened): 225 <= nabla(Q_9) <= 236 (Hertz 2021, Table 4, citing
Pike 2003; Pike's paper itself is paywalled and was not opened). Both C5 routes therefore amount to improving
that bound: <= 2399 needs nabla(Q_9) <= 235; >= 2369 needs e.g. nabla(Q_9) >= 233.

---------------------------------------------------------------------------------------------------
## Items 2-3: verbatim from run/tasks/H-C5-002/out/proof.md (Part A identity, Steps 8-10)

## Part A. An exact identity for the number of uphill paths

Step 1 (recursion). Let N(v) be the number of uphill paths ending at v. A one-vertex sequence (v) is an uphill
path iff v is a valley. A sequence (v_1,...,v_k) with k >= 2 and v_k = v is an uphill path iff v_{k-1} = w is a
lower neighbour of v and (v_1,...,v_{k-1}) is an uphill path ending at w (the conditions "v_1 is a valley",
"consecutive vertices adjacent", "labels strictly increase" for the whole sequence are exactly those for the
prefix plus "w ~ v and f(w) < f(v)"). Distinct sequences are distinct paths. Hence
  N(v) = [v is a valley] + sum over lower neighbours w of v of N(w).                               (1)
A vertex is a valley iff low(v) = 0. (This is the same recursion as inbox/checker/verify.py.)

Step 2 (N >= 1). By induction on f(v): if low(v) = 0 then N(v) = 1 by (1); otherwise v has a lower
neighbour w with N(w) >= 1 (induction, f(w) < f(v)), so N(v) >= 1.

Step 3 (total). Summing (1) over v, with V = number of valleys, P(f) = sum_v N(v):
  P(f) = V + sum over edges {w,v} with f(w)<f(v) of N(w) = V + sum_w N(w) up(w).
Since every edge has exactly one lower endpoint, sum_w up(w) = |E|. So
  P(f) = V + |E| + sum_w (N(w) - 1) up(w).                                                         (2)

Step 4 (the sets T and S). Let T = {v : N(v) = 1}, S = {v : N(v) >= 2}; by Step 2 they partition V(G).
 (a) Every valley is in T (low = 0 gives N = 1).
 (b) If v in T is not a valley, then low(v) = 1 and its unique lower neighbour is in T: by (1),
     1 = N(v) = sum of N(w) over its lower neighbours, each term >= 1 (Step 2) and there is at least one term,
     so there is exactly one term and it equals 1.
 (c) If u in S and w is an upper neighbour of u, then w in S: by (1), N(w) >= N(u) >= 2.

Step 5 (T induces a forest with exactly V components). Let {a,b} be an edge with both ends in T and
f(a) < f(b). Then b is not a valley and a is a lower neighbour of b, so by 4(b) a is THE lower neighbour of b.
Hence the map p: (T minus valleys) -> T, p(b) = unique lower neighbour of b, satisfies: the edges of G[T] are
exactly the pairs {b, p(b)}. So e(G[T]) = |T| - V. Iterating p strictly decreases f, so from every vertex of T
it reaches a vertex where p is undefined, i.e. a valley (4(a)); hence every component of G[T] contains a valley,
so G[T] has at most V components. The cycle rank of a graph (edges - vertices + components) is >= 0, with
equality iff the graph is a forest. For G[T] it is (|T| - V) - |T| + #components = #components - V <= 0, so it is
0: G[T] is a forest with exactly V components, and since each component contains a valley and there are V
valleys, each component contains exactly one valley.

Step 6 (edges inside S). By 4(c), sum_{u in S} up(u) counts every edge with lower endpoint in S, and such an
edge has its upper endpoint in S; conversely every edge inside S is counted once, at its lower endpoint. So
  sum_{u in S} up(u) = e(S)   (number of edges of G[S]).                                           (3)
Counting edges of G: |E| = e(T) + e(T,S) + e(S), and summing degrees over S: d|S| = e(T,S) + 2 e(S). With
e(T) = |T| - V (Step 5) and |T| = n - |S|:
  |E| = n - |S| - V + d|S| - e(S),  i.e.  e(S) = n + (d-1)|S| - V - |E|.                           (4)

Step 7 (identity). By (2), N(w) - 1 = 0 on T, so P(f) = V + |E| + sum_{u in S}(N(u)-1) up(u)
= V + |E| + e(S) + sum_{u in S}(N(u)-2) up(u) by (3), and by (4):
  P(f) = 2^d + (d-1)|S| + sum_{u in S} (N(u) - 2) up(u),   every summand >= 0 (N >= 2 on S).       (*)
Nothing here uses the cube except |V| = 2^d and d-regularity; for any graph G the same computation gives
P(f) = |V(G)| + sum_{u in S}(deg u - 1) + sum_{u in S}(N(u)-2)up(u).
Sanity check (not part of the proof): out/code/check_identity.py tests (*) and Steps 4(c), 5 on 180 random
and near-random labellings, d = 1..9, and on out/Q3.txt..out/Q9.txt: 0 mismatches.

## Part B. Consequences

Step 8 (lower bound via decycling). A decycling set of G is a set whose removal leaves a forest; nabla(G) is the
minimum size. By Step 5, S_f is a decycling set, so |S_f| >= nabla(Q_d), and by (*):
  U(Q_d) >= 2^d + (d-1) nabla(Q_d).                                                                (5)
In particular, for d = 9:
 * any labelling with P(f) <= 2399 has 8|S_f| <= 2399 - 512 = 1887, so |S_f| <= 235: it exhibits a decycling
   set of Q_9 of size <= 235, i.e. it would prove nabla(Q_9) <= 235;
 * any proof of nabla(Q_9) >= 233 gives U(Q_9) >= 512 + 8*233 = 2376 >= 2369 (the LOWER route).
 * The organisers' numbers fit (5) exactly: 2368 = 512 + 8*232 and 2400 = 512 + 8*236. (That their lower bound
   comes from nabla(Q_9) >= 232 is my guess, UNSURE; the statement says the lower bound is unpublished.)

Step 9 (self-contained weak lower bound). If S is a decycling set of Q_d then the forest Q_d - S has at most
n - |S| - 1 edges and at least |E| - d|S| edges, so |E| - d|S| <= n - |S| - 1, i.e.
|S| >= (|E| - n + 1)/(d-1). For d = 9: |S| >= 1793/8, so |S| >= 225, and (5) gives U(Q_9) >= 512 + 1800 = 2312.
(This is the bound of Beineke-Vandell Lemma 2.1(2) as quoted in Bau's survey, see sources.md; proved here.)
It is weaker than the organisers' 2368.

Step 10 (upper bound construction; reproduces 2400). Let E_d / O_d be the even / odd weight vertices. Let M be
a subset of E_d with pairwise Hamming distance >= 4. Put F = O_d u M, S = E_d \ M.
 (a) F induces |M| vertex-disjoint stars plus isolated vertices: each m in M has all d neighbours in O_d
     (subset of F); two words of M at distance >= 4 have no common neighbour (a common neighbour would put
     them at distance <= 2); O_d is independent and M is independent (even-even distance is even, >= 4).
     So the components of G[F] are the stars {m} u N(m) (m in M) and the 2^{d-1} - d|M| odd vertices with no
     neighbour in M.
 (b) Labelling: for each m in M, m then its d neighbours; then the isolated odd vertices; then S.
     A star centre m has no lower neighbour: its neighbours are its own leaves, placed right after it (they are
     not leaves of an earlier star, by disjointness in (a)) -> valley, N = 1. An isolated odd vertex has no
     lower neighbour: its neighbours are even and not in M (else it would be a leaf), so they are in S, placed
     last -> valley, N = 1. A leaf x of centre m: its neighbours are even; the only one in M is m (a second one
     m' would give d(m,m') = 2); the others are in S, placed last. So x has exactly one lower neighbour, m,
     and N(x) = N(m) = 1.
     Each vertex of S is even, so all its neighbours are odd, hence in F, hence lower -> up = 0.
 (c) By (2): P = V + |E| + 0 = |E| + |M| + 2^{d-1} - d|M| = 2^d + (d-1)(2^{d-1} - |M|) (equivalently (*)
     with S_f = S, all summands 0 because up = 0 on S).
 With the codes found by out/code/parity_code_construction.py (sizes 1,2,2,4,8,16,20 for d = 3..9, printed in
 out/tmp/parity_runs.log) this gives 14, 34, 88, 204, 464, 1040, 2400, each confirmed by
 inbox/checker/verify.py on out/Q3.txt ... out/Q9.txt. The code sizes are A(d,4) for d <= 9 per standard tables
 (not needed: the checker verifies the files directly).

Step 11 (small d, conditional). Bau's survey (opened, see sources.md) reports, citing Beineke-Vandell (1996),
nabla(Q_n) = 0,1,3,6,14,28,56,112 for n = 1..8 ("[3] computed nabla(Q_n) exactly"). IF these values are
correct, then (5) and Step 10 give U(Q_d) = 2^d + (d-1) nabla(Q_d) exactly for 3 <= d <= 8:
U(Q_3..Q_8) = 14, 34, 88, 204, 464, 1040. [GAP: the nabla values are cited, not reproduced; the original
computation/proof in Beineke-Vandell was not opened.] Heuristic support only: out/code/mif_sa.c finds induced
forests with |S| = 14, 28, 56, 112 for d = 5..8 and never smaller (search, not proof).

---------------------------------------------------------------------------------------------------
## Item 4: verbatim from run/tasks/H-C5-006/out/proof.md

## Lemma I (independent decycling sets of Q_d)

Let d >= 2, S an independent decycling set of Q_d, F = V \ S (so Q_d[F] is a forest). For v in F let
D(v) = {i : v + e_i in F}, deg_F(v) = |D(v)|.

Step I1 (square rule). If v in F and i != j are in D(v), then v + e_i + e_j in S.
Proof: v, v+e_i, v+e_i+e_j, v+e_j are four distinct vertices (they are v + sum_{t in T} e_t for the four
distinct subsets T of {i,j}); consecutive ones differ in exactly one coordinate (i, j, i) and the last and
first differ in coordinate j. So they form a 4-cycle of Q_d. The first, second and fourth are in F. If the
third were in F, Q_d[F] would contain this cycle, contradicting that Q_d[F] is a forest. So v+e_i+e_j in S.

Step I2 (independence). If s in S then every neighbour of s is in F (S has no edge).

Step I3 (degrees). For every v in F, deg_F(v) is 0, 1 or d.
Proof: suppose 2 <= deg_F(v) <= d-1. Choose i != j in D(v) and l not in D(v) (possible: |D(v)| <= d-1);
l differs from i and j. Then:
  v + e_l in S (l not in D(v));
  v + e_l + e_i and v + e_l + e_j are neighbours of v + e_l, so they are in F (I2);
  v + e_i + e_j in S (I1), so its neighbour v + e_i + e_j + e_l is in F (I2).
Consider the six vertices
  v, v+e_i, v+e_i+e_l, v+e_i+e_j+e_l, v+e_j+e_l, v+e_j.
They are v + sum_{t in T} e_t for the six distinct subsets T = {}, {i}, {i,l}, {i,j,l}, {j,l}, {j} of {i,j,l},
hence distinct. Consecutive ones differ in exactly one coordinate (in order: i, l, j, i, l) and the last and
the first differ in coordinate j. So they form a 6-cycle of Q_d. All six are in F (v by assumption,
v+e_i and v+e_j since i, j in D(v), the other three shown above). This is a cycle in Q_d[F], a contradiction.

Step I4 (centres give stars). Call v in F a centre if deg_F(v) = d. Let v be a centre. For each i, the
neighbour u = v + e_i is in F and its neighbours are v (in F) and u + e_j = v + e_i + e_j for j != i, which
are in S by I1 (i, j in D(v) = all coordinates, and d >= 2 gives at least one j != i). So deg_F(u) = 1.
Hence the component of v in Q_d[F] is exactly {v} u N(v): a star K_{1,d} (every leaf's only F-neighbour is v).

Step I5 (all components). Let K be a component of Q_d[F] with at least two vertices; take an edge {x, y} of
K, y = x + e_i. If deg_F(x) = deg_F(y) = 1, pick l != i (d >= 2). The only F-neighbour of x is y, so
x + e_l is in S; likewise the only F-neighbour of y is x, so y + e_l is in S. But x + e_l and
y + e_l = x + e_l + e_i differ exactly in coordinate i, so they are adjacent: contradiction with independence.
So one of x, y has F-degree >= 2, hence = d by I3: it is a centre, and by I4 K is a star centred there.
Conclusion: every component of Q_d[F] is an isolated vertex or a star K_{1,d} centred at a centre.
Let C be the set of centres.

Step I6 (counting). e(F) := number of edges of Q_d[F] = d|C| by I5 (each star has d edges, isolated vertices
none). Second count: each edge of Q_d has exactly one end in X, so
  e(F) = sum_{x in F n X} deg_F(x) = sum_{x in F n X} (d - |N(x) n S|) = d|F n X| - e(F n X, S n Y),
where N(x) is contained in Y, and e(A,B) = number of edges between A and B. Each of the d edges at a vertex of
S n Y ends in X, and in F by I2, so e(F n X, S n Y) = d|S n Y|. Hence
  e(F) = d(|F n X| - |S n Y|) = d(|F n X| - (2^{d-1} - |F n Y|)) = d(|F| - 2^{d-1}).
Comparing: |F| - 2^{d-1} = |C|, i.e. |S| = 2^d - |F| = 2^{d-1} - |C|.

Step I7 (centres form a distance-4 code). Let c != c' be centres, t = Hamming distance.
  t = 1: c' is a neighbour of c, so deg_F(c') = 1 (I4), but deg_F(c') = d >= 2. Impossible.
  t = 2: c' = c + e_i + e_j is in S by I1. Impossible (c' in F).
  t = 3: c' = c + e_i + e_j + e_l. The vertex c + e_i is in F (a leaf of c), and c + e_i = c' + e_j + e_l,
         which is in S by I1 applied at the centre c' (j, l in D(c')). Impossible.
So t >= 4 and C is a code of length d with minimum distance >= 4 (or |C| <= 1): |C| <= A(d,4) (A(d,4) >= 1).
Therefore |S| = 2^{d-1} - |C| >= 2^{d-1} - A(d,4).                                                     QED (I)

Remarks. (i) Equality is attained: X \ M with M an even-weight code of minimum distance 4 and size A(d,4)
(Focardi-Luccio-Peleg via Wodlinger Lemma 2.33; H2 Step 10 builds it for d = 9 with |M| = 20).
(ii) Sanity check, not part of the proof: out/code/check_indep_structure.py enumerates ALL independent sets of
Q_d for d = 2..5 (7, 35, 743, 254475 sets), finds 6, 10, 26, 114 independent decycling sets, 0 violations of
I3-I7, and minimum sizes 1, 3, 6, 14 = 2^{d-1} - A(d,4).

Step I8 (d = 9). A(9,4) = 20 is CITED, not reproduced: Best, Brouwer, MacWilliams, Odlyzko, Sloane, "Bounds for
binary codes of length less than 25", IEEE Trans. IT 24 (1978) 81-93, via A.E. Brouwer's table (opened, see
sources.md). [GAP: not re-proved. The plain Delsarte LP bound for even (9,4) codes, computed exactly by
out/code/lp_A94.py with a verified dual certificate beta = (3/5, 3/10, 1/10) on k = 1, 2, 3, gives only
|C| <= 128/5, i.e. A(9,4) <= 25 after puncture/extend; the extra inequalities of Best et al. are needed.]
Given A(9,4) = 20: every independent decycling set of Q_9 has >= 256 - 20 = 236 vertices, so
  every decycling set of Q_9 with <= 235 vertices contains at least one edge.                            (I8)
(The puncture/extend remark: a code with minimum distance >= 4 of length 9 and size M gives, by deleting the
last coordinate and appending an overall parity bit, an even-weight code of length 9, size M, minimum
distance >= 4; used only to justify applying the even-code LP to arbitrary codes, i.e. only for the "<= 25".)

## Lemma J (cost of edges inside S_f)

Fix d >= 1 and a labelling f of Q_d. Let S = {v : N(v) >= 2}, F = {v : N(v) = 1} (H2 Step 2: N >= 1, so this
partitions V). For u in S: deg_F(u), up_S(u), down_S(u) = numbers of neighbours of u in F, in S with larger
label, in S with smaller label; deg_F + up_S + down_S = d.
Facts used from H2 (restated): (1) N(v) = [v valley] + sum over lower neighbours w of N(w); a valley has N = 1;
(4c) every upper neighbour of a vertex of S is in S (by (1): N(w) >= N(u) >= 2); (*) P(f) = 2^d + (d-1)|S| +
sum_{u in S} (N(u) - 2) up(u), where up(u) = number of upper neighbours; by (4c) up(u) = up_S(u) for u in S.

Step J1. If u in S and w in F are adjacent, then f(w) < f(u).
Proof: if f(w) > f(u) then u is a lower neighbour of w, so by (1) N(w) >= N(u) >= 2, contradicting w in F.

Step J2. For u in S: N(u) >= deg_F(u) + 2 down_S(u).
Proof: u is not a valley (a valley has N = 1). By (1), N(u) = sum of N(w) over lower neighbours w. By J1 all
deg_F(u) neighbours in F are lower, each with N = 1; the down_S(u) lower neighbours in S have N >= 2 each;
all terms are >= 1 (H2 Step 2). Summing gives the claim.

Step J3. From (*), J2 and N(u) - 2 >= 0 on S:
  P(f) >= 2^d + (d-1)|S| + sum_{u in S} max(0, deg_F(u) + 2 down_S(u) - 2) * up_S(u).
For d = 9, deg_F(u) = 9 - up_S(u) - down_S(u), so the weight is w(u) := max(0, 7 - up_S(u) + down_S(u)).

Step J4 (zero-cost S-edges). The term of u is 0 iff up_S(u) = 0 or N(u) = 2. If up_S(u) >= 1 and N(u) = 2,
then by J2 deg_F(u) + 2 down_S(u) <= 2, so either (a) down_S(u) = 0 and deg_F(u) <= 2, i.e. up_S(u) >= d - 2,
or (b) down_S(u) = 1 and deg_F(u) = 0 (then up_S(u) = d - 1). In a labelling where every term vanishes and
S has an edge, let u be the vertex with the smallest label among those with up_S(u) >= 1. In case (b) its lower
S-neighbour u' has up_S(u') >= 1 (u is above u') and a smaller label: contradiction with minimality; so case
(a): u has deg_F(u) <= 2 and up_S(u) >= d - 2. Also deg_F(u) >= 1 is not forced; if deg_F(u) = 0 and
down_S(u) = 0 then u is a valley, impossible for u in S. So 1 <= deg_F(u) <= 2 and up_S(u) >= d - 2.

Corollary J5 (UPPER route, d = 9). If a labelling f of Q_9 has P(f) <= 2399, then with S = S_f:
  |S| <= 235 (H2 Step 8), S contains an edge (I8, using the cited A(9,4) = 20), and
  sum_{u in S} max(0, 7 - up_S(u) + down_S(u)) * up_S(u) <= 1887 - 8|S|   (J3 with 512 + 8|S| + extra <= 2399).
In particular for |S| = 235 the budget is 7, for 234 it is 15, for 233 it is 23, for 232 it is 31. An S-edge
whose lower end u has up_S(u) = 1 and down_S(u) = 0 costs >= 6; an S-edge costs nothing only if its lower end
has at least 7 upper S-neighbours (by J4: cost 0 with up_S(u) >= 1 forces N(u) = 2, hence case (a) with
up_S(u) >= 7 or case (b) with up_S(u) = 8). So a hand-in for the UPPER route is exactly a decycling set of
size <= 235 (necessarily with edges) whose S-edges are concentrated at vertices of S-degree >= 7, or few.

Corollary J6 (LOWER route, conditional). Suppose one had nabla(Q_9) >= 232 (the organisers' 2368 = 512 + 8*232
suggests they do; UNSURE, unpublished). Then U(Q_9) >= 2368 by H2 Step 8. To reach 2369 it would suffice to
show, in addition, that no labelling has |S_f| = 232 and zero extra cost; by I8 such an S_f has an edge, and
by J4 it would contain a vertex u with 1 <= deg_F(u) <= 2 and up_S(u) >= 7, and every lower end of an
S-edge satisfies (a) or (b) of J4. [NOT done: nabla(Q_9) >= 232 is not available to me; the best published
lower bound found is 225 (or 226, see sources.md discrepancy).]

---------------------------------------------------------------------------------------------------
## Item 5: verbatim from run/tasks/H-C5-007/out/proof.md

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
