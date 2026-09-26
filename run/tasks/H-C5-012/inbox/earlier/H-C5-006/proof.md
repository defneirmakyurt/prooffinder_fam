Statements proved here (partial progress on H-C5; NOT the cell): (I) for every d >= 2, every independent decycling set S of Q_d has |S| = 2^{d-1} - |C| for a binary code C of length d with minimum distance >= 4, hence |S| >= 2^{d-1} - A(d,4); with the cited value A(9,4) = 20, every decycling set of Q_9 with at most 235 vertices contains an edge. (J) For every labelling f of Q_d, with S = S_f = {v : N(v) >= 2}: P(f) >= 2^d + (d-1)|S| + sum_{u in S} max(0, deg_F(u) + 2 down_S(u) - 2) up_S(u); for d = 9 the weight is max(0, 7 - up_S(u) + down_S(u)). Consequences: necessary conditions (J5, J6) for both routes of H-C5. Neither route of the cell is achieved.

Definitions exactly as in inbox/statement.md. Q_d: vertex set {0,1}^d, e_i = i-th unit vector, x + e_i =
x with coordinate i flipped. X / Y = even / odd weight vertices; every edge has one end in X and one in Y.
A decycling set of a graph G is S subset V(G) such that G - S has no cycle; nabla(G) = min |S|.
A(d,4) = maximum size of a binary code of length d with minimum Hamming distance >= 4.
Labelling notation as in H-C5-002 (inbox/earlier/H-C5-002/out/proof.md, "H2" below): N(v) = number of uphill
paths ending at v; lower / upper neighbour of v = neighbour with smaller / larger label.

Credit. The identity (*) and the facts H2-4(a)-(c), H2-5 are from H-C5-002 (Steps 1-7; under review, not
gated); they are restated where used, not re-proved. Lemma I reproduces, by an argument written here, the
"hard" direction of Pike's characterisation (Pike 2003, as stated in Wodlinger's thesis Thm 2.34; Pike's own
proof was NOT accessible, so I cannot say whether it is the same argument). Lemma J is new here (not found in
the sources searched, see sources.md).

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

## What is established / not established
Established: Lemma I (all d >= 2), I8 (modulo the cited A(9,4) = 20), Lemma J, J5, and the conditional J6.
Not established: U(Q_9) >= 2369; a labelling with <= 2399 paths; nabla(Q_9) <= 235; nabla(Q_9) >= 226.
Search (not proof): out/code/fixsize_sa.c at |F| = 277 on Q_9 (RAN lines in the report and out/claims.md)
found no induced forest of 277 vertices.
