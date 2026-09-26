# Claims: H-C5-008 (searcher, CONTRARIAN, UPPER route)

Headline: **no labelling with <= 2399 found (SEARCH-FOUND-NOTHING).** The target (<= 2399) was not
reached. Everything below is either a written proof, an exact check of a concrete object, or a
heuristic search that found nothing (labelled as such).

| claim | status | where shown |
|---|---|---|
| Q1. Checker sanity: verify.py gives 2 on Q_1 (0,1) and 5 on Q_2 (00,01,10,11), both hand-computed | CHECKED | runlog R1 |
| Q2. Lemma Q (covering quotients): for a group G of automorphisms of Q_9 with d(v, gv) >= 2 for all v and all g != id, a G-invariant T is an induced forest of Q_9 iff T/G is an induced forest (no cycle, no parallel pair) of the multigraph Q_9/G; and \|T\| = \|G\|.\|T/G\| | PROVED | section 1 below |
| Q3. Counting: every induced forest of Q_9 has <= 287 vertices; so a G-invariant forest with \|T\| >= 277 needs \|G\| in {2,4,8}; \|G\| = 8 forces \|T\| = 280, \|G\| = 4 forces \|T\| in {280, 284} | PROVED | section 2 |
| Q4. Code classes: binary linear codes of dim r <= F_2^9 without weight-1 words, up to coordinate permutation: 8 (r=1), 35 (r=2), 99 (r=3) | CHECKED (exact enumeration of column multisets up to GL(r,2)) | code/quotients.py, runlog R2 |
| Q5. r=3 (translation groups of order 8): no class has a quotient forest of size >= 35 (i.e. no invariant forest of size 280); max is 34 (272) in 9 classes | SOLVER-UNSAT, NOT certified (CaDiCaL via python-sat, no DRAT); the value 34 is attained by verified forests | runlog R3, R4 |
| Q6. r=2 (order 4): 24 of 35 classes solver-UNSAT at 70 (no DRAT), 11 timed out; SA best 68 (272) over all 35 classes | SEARCH-FOUND-NOTHING, not exhaustive | runlog R5, R6 |
| Q7. r=1 (order 2 translations): SA best 137 (274, class weight(a)=4), others <= 136; none reaches 139 | SEARCH-FOUND-NOTHING, not exhaustive | runlog R7, R8 |
| Q8. Free affine involutions v -> sigma(v)+a (sigma with t = 1..3 transpositions): see runlog R10 | SEARCH-FOUND-NOTHING, not exhaustive | runlog R10 |
| Q9. Excess identity: for every labelling of Q_d, #uphill = 2^d + (d-1)\|S\| + X with X = sum_{w in T} (N(w)-1) up(w) + sum_{w in S} (N(w)-2) up(w) >= 0 termwise | PROVED (from the gated Lemma A steps A4, A6) | section 3 |
| Q10. Structure: a labelling of Q_9 with <= 2399 paths and \|S\| = 235 has N = 1 on T, every T-S edge rising into S, and S = M + A2 + R with M local maxima (independent), A2 = vertices with exactly 2 T-neighbours (both lower) and 7 S-neighbours (all higher), \|R\| <= 7, \|A2\| <= 12 | PROVED | section 3 |
| Q11. Best artefact: out/best.txt = out/Q9.txt, a labelling of Q_9 from a verified lifted forest; checker output quoted in runlog | CHECKED (score > 2400: not an improvement) | runlog R9 |

## 1. Lemma Q (covering quotients)

Setting. G is a finite group of automorphisms of Q_9 such that (*) for every g != id and every vertex
v, the Hamming distance d(v, gv) >= 2 (so g fixes no vertex and maps no vertex to a neighbour).
X = Q_9/G is the multigraph whose vertices are the G-orbits [v] and whose edges are the G-orbits of
edges of Q_9, the orbit of {u, w} joining [u] and [w]. For a G-invariant T, X[T/G] is the
sub-multigraph on the orbits contained in T with all edge-orbits joining two of them. "Forest" for a
multigraph means: no loop, no two parallel edges (a 2-cycle), no cycle of length >= 3.

(a) Local structure. Let {u, w} be an edge. [u] != [w]: otherwise w = gu for some g, and g != id
since w != u, so g maps u to a neighbour, contrary to (*). Suppose an edge orbit contains two distinct
edges at u, {u, w1} and {u, w2} = g{u, w1} = {gu, gw1}. Then either gu = u, so g = id by (*) and
w2 = w1, a contradiction; or gw1 = u, so g maps w1 to its neighbour u, contrary to (*) (g != id
since it moves w1). So each edge orbit has at most one edge at u. Every edge orbit incident to [u]
contains an edge {hu, x} for some h in G; applying h^{-1} gives an edge {u, h^{-1}x} of the same
orbit at u. Hence the map (edge at u) -> (its orbit) is a bijection from the 9 edges at u onto the
edge orbits incident to [u] (counted with multiplicity), and orbits have |G| elements each (a vertex
orbit: g v = h v implies h^{-1} g fixes v, so h = g).

(b) Reduced closed walks. A closed walk x_0, e_1, x_1, ..., e_m, x_m = x_0 (m >= 1) in a multigraph
is reduced if e_j != e_{j+1} for all j, indices of edges mod m. Claim: a reduced closed walk
contains a loop, a parallel pair, or a cycle of length >= 3 whose vertices and edges are among those
of the walk. Proof: pick i < j with x_i = x_j and j - i >= 1 minimal. Then x_i, ..., x_{j-1} are
pairwise distinct. If j - i = 1, e_{i+1} is a loop. If j - i = 2, e_{i+1} and e_{i+2} both join
x_i and x_{i+1} and are different edges (reduced), a parallel pair. If j - i >= 3, x_i, ..., x_{j-1}
with edges e_{i+1}, ..., e_j is a cycle of length j - i.

(c) T acyclic => T/G acyclic (contrapositive). Suppose X[T/G] has a cycle or parallel pair:
y_0, h_1, y_1, ..., h_L, y_L = y_0, L >= 2, the h's pairwise distinct edge orbits. Pick u_0 in y_0.
Inductively, given u_s in y_{s mod L}, by (a) the orbit h_{(s mod L)+1} has exactly one edge at u_s,
say {u_s, u_{s+1}}; then u_{s+1} is in y_{(s+1) mod L}. All u_s lie in T (T is G-invariant and every
y is an orbit inside T). The infinite walk u_0, u_1, ... has consecutive edges in different orbits
(consecutive h's are distinct, including h_L, h_1 since L >= 2), so consecutive edges of the walk
are different edges of Q_9 (edges in different orbits are different). As Q_9[T] is finite, some
vertex repeats. Let j be the least index with u_j in {u_0, ..., u_{j-1}}, and u_i = u_j (i < j). Then
u_i, ..., u_{j-1} are pairwise distinct. j - i = 1 would make {u_i, u_{i+1}} a loop: impossible in
Q_9. j - i = 2 would give u_{i+2} = u_i, so the edges {u_i, u_{i+1}} and {u_{i+1}, u_{i+2}} coincide,
contradicting the previous sentence. So j - i >= 3 and u_i, ..., u_{j-1} (closing edge
{u_{j-1}, u_j} = {u_{j-1}, u_i}) is a cycle of Q_9[T].

(d) T/G acyclic => T acyclic (contrapositive). Let v_1, ..., v_m (m >= 3 distinct, v_j ~ v_{j+1},
v_m ~ v_1) be a cycle in Q_9[T]. Its image [v_1], e_1, [v_2], ..., e_m, [v_1] (e_j = orbit of
{v_j, v_{j+1}}, indices mod m) is a closed walk in X[T/G]. The edges e_{j-1}, e_j contain the two
edges {v_{j-1}, v_j} and {v_j, v_{j+1}} at v_j, which are different since v_{j-1} != v_{j+1}
(m >= 3); by (a) different edges at v_j lie in different orbits, so e_{j-1} != e_j: the walk is
reduced. By (b), X[T/G] contains a loop (impossible by (a)), a parallel pair, or a cycle.

So T is an induced forest of Q_9 iff T/G is a forest of X, and |T| = |G| |T/G|. The code
additionally re-checks every lifted T directly in Q_9 (quotients.is_forest_qd), so no reported
object depends on this lemma; the lemma is what makes a quotient search a search over exactly the
G-invariant forests.

Translation groups. For a linear code C with no word of weight 1, G = {v -> v + c}: d(v, v + c) =
wt(c) >= 2, so (*) holds; X is the Cayley multigraph Cay(F_2^9/C, {e_i + C}) (parallel edges exactly
from weight-2 words). Conjugating the translation group by an automorphism v -> sigma(v) + b gives
the translation group of sigma(C); so C-invariant forests up to Aut(Q_9) correspond to codes up to
coordinate permutation. A code with generator columns col_1..col_9 in F_2^r is determined up to
coordinate permutation and change of basis by the multiset of columns up to GL(r,2);
code/quotients.py enumerates all multisets, keeps one canonical representative (the largest image
under GL(r,2)), and keeps those of rank r with no weight-1 word (u != 0 with exactly one j,
u.col_j = 1).

Free involutions. g(v) = sigma(v) + a, sigma a product of t disjoint transpositions, sigma(a) = a.
g^2 = id. For each pair (i j) of sigma, (g(v) + v) restricted to {i, j} is (v_i + v_j + a_i)(e_i+e_j)
(a_i = a_j), weight 0 or 2; on a fixed coordinate it is a_k. So d(v, gv) = f + 2 x(v) where f = weight
of a on the fixed coordinates and x(v) >= 0 can be 0. Hence (*) holds iff f >= 2. Conjugating by the
translation v -> v + b replaces a by a + b + sigma(b), which changes a on the pairs arbitrarily, so a
may be taken 0 on the pairs; permuting coordinates, the classes are (t, f), t = 1..3, 2 <= f <= 9 - 2t
(t = 4 leaves one fixed coordinate, f <= 1). These 12 classes are the ones run in R10.

## 2. Counting bound (Q3)

Let T be an induced forest of Q_9, S = V \ T, s = |S|. Each vertex of T has 9 neighbours, so
9|T| = 2 e(T) + e(T, S) and e(T, S) <= 9 s. Hence 2 e(T) >= 9(512 - s) - 9 s, i.e.
e(T) >= 9(256 - s). A forest has e(T) <= |T| - 1 = 511 - s. So 2304 - 9 s <= 511 - s, 8 s >= 1793,
s >= 225 and |T| <= 287. For a G-invariant forest, |G| divides |T| (Q2); |T| in [277, 287]:
multiples of 16 in that range: none (272, 288); of 8: 280; of 4: 280, 284; of 2: 278..286.
For translation groups |G| = 2^r, so only r = 1, 2, 3 can give a forest of size >= 277, and the
quotient targets are 139 (r=1, 256-vertex quotient), 70 (r=2, 128 vertices), 35 (r=3, 64 vertices).

## 3. Excess identity and structure (Q9, Q10)

Notation as in the gated Lemma A (inbox/gated-lemmaA.md): d >= 1, labelling f, down/up, N(v),
S = {down >= 2}, T = V \ S, V0 = number of valleys, E = d 2^(d-1).
From A4: P := sum_v N(v) = V0 + E + sum_w (N(w) - 1) up(w).
From A6: sum_{w in S} down(w) = E - |T| + V0, so sum_{w in S} up(w) = d|S| - E + |T| - V0.
Therefore P - (d|S| + |T|) = V0 + E + sum_w (N(w)-1) up(w) - d|S| - |T|
  = sum_w (N(w)-1) up(w) - sum_{w in S} up(w)
  = sum_{w in T} (N(w)-1) up(w) + sum_{w in S} (N(w)-2) up(w) =: X,
and d|S| + |T| = 2^d + (d-1)|S|. Every term of X is >= 0: N(w) >= 1 for all w (A3) and N(w) >= down(w)
>= 2 on S (A3). This is Q9.

Q10 (d = 9, P <= 2399, |S| = 235). Then 2^9 + 8 * 235 = 2392, so X <= 7.
(i) A vertex w in T has down(w) <= 1, so up(w) >= 8; if N(w) >= 2 its term is >= 8 > 7. So N = 1 on T.
(ii) If t in T, s in S are adjacent and f(s) < f(t), then N(t) >= N(s) >= 2 by A2, contradicting (i).
So every T-S edge goes up from T into S.
(iii) For s in S, N(s) = sum of N over its down(s) lower neighbours (A2; s is no valley). If
(N(s) - 2) up(s) = 0 and up(s) >= 1 then N(s) = 2, so s has exactly 2 lower neighbours, each with
N = 1, hence each in T (vertices of S have N >= 2); by (ii) all T-neighbours of s are lower, so s has
exactly 2 T-neighbours and its other 7 neighbours are in S and higher. Call these vertices A2. Let M
be the local maxima of S (up = 0) and R the rest of S. Each vertex of R has a term >= 1, so |R| <= 7.
M is independent (of two adjacent vertices one is lower, so not a local maximum).
(iv) Counting as in section 2 with |T| = 277, |S| = 235: 9*277 = 2 e(T) + e(T,S), e(T) = 277 - c
(c = number of trees), 9*235 = 2 e(S) + e(T,S); subtracting, e(S) + c = 88, so e(S) <= 87. The 7
upward S-edges at the vertices of A2 are distinct for distinct vertices (each is identified by its
lower endpoint), so 7|A2| <= e(S) <= 87 and |A2| <= 12.
This narrows any <= 2399 labelling with |S| = 235 to S = M + A2 + R of this shape; it was not used to
drive a search in this run (see stuck.md).
