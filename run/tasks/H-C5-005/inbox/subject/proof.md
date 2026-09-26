Statement proved (partial progress on H-C5, NOT the cell): for every d >= 1 and every labelling f of Q_d,
P(f) = 2^d + (d-1)|S_f| + sum_{u in S_f} (N(u)-2) up(u), where N(u) = number of uphill paths ending at u,
S_f = {u : N(u) >= 2}, up(u) = number of neighbours with larger label, and every summand is >= 0; V(Q_d) \ S_f
induces a forest. Consequently U(Q_d) >= 2^d + (d-1) nabla(Q_d) (nabla = decycling number), and for every
even-weight binary code M of length d with minimum distance >= 4, U(Q_d) <= 2^d + (d-1)(2^{d-1} - |M|).
For d = 9: 2^9 + 8 nabla(Q_9) <= U(Q_9) <= 2400, the upper bound realised by out/Q9.txt (checker: VERIFIED 2400).

What this does NOT establish: it does not prove U(Q_9) >= 2369 and does not give a labelling with <= 2399.
It reduces both routes of the cell to the decycling number of Q_9 (Step 8).

Definitions exactly as in inbox/statement.md. Throughout, G = Q_d, n = 2^d, |E| = d 2^{d-1}, f a labelling.
"lower neighbour" of v = neighbour w with f(w) < f(v); "upper neighbour" = neighbour w with f(w) > f(v).
low(v), up(v) = number of lower / upper neighbours; low(v) + up(v) = d.

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

## Part C. Status for d = 9 (what is established)
 * U(Q_9) <= 2400: out/Q9.txt, VERIFIED 2400 (reproduces the organisers' upper bound; earns nothing).
 * U(Q_9) >= 512 + 8 nabla(Q_9) >= 2312: proved above. Published bounds on nabla(Q_9) that I could open:
   225 <= nabla(Q_9) <= 237 (Bau et al. 2000 via Bau's survey). Pike (2003) has improved bounds [not opened].
 * Improving the upper bound to <= 2399 REQUIRES a decycling set of Q_9 of size <= 235 (Step 8). Simulated
   annealing for maximum induced forests of Q_9 (7 runs, see RAN lines) never went below |S| = 236.
 * Improving the lower bound to >= 2369 would FOLLOW from nabla(Q_9) >= 233 (Step 8), or from nabla(Q_9) >= 232
   plus a proof that every decycling set of size 232 forces a positive sum in (*). [GAP: neither done.]

## Part D. Published lower-bound techniques and what they give at d = 9
 * IMO 2022 P6 technique (literature, via inbox/earlier-C1-sources.md): P >= |E| + 1 for every graph (every edge
   ends at least one uphill path; plus a valley). At d = 9: U(Q_9) >= 2305. It is the case S_f = empty of (*)'s
   ingredients: (2) with V >= 1 and N >= 1.
 * Via (5) and the published decycling lower bound nabla(Q_9) >= 225 (Beineke-Vandell Lemma 2.1(2) as quoted by
   Bau; re-proved in Step 9): U(Q_9) >= 2312. Also nabla(Q_n) >= 2 nabla(Q_{n-1}) (Beineke-Vandell Lemma 2.1(1),
   quoted by Bau, not re-proved here) gives nabla(Q_9) >= 224 only.
 * No published lower bound for U(Q_d) itself was found (sources.md, "Not found").

## Part E. How the 2400 construction works (for a worker trying to improve it by 1)
 Q9.txt = [20 stars: code word m, then its 9 odd neighbours] + [76 odd vertices with no code neighbour]
 + [236 even non-code vertices]. Valleys = 20 + 76 = 96, P = |E| + 96 = 2400. Every vertex of the forest part
 has N = 1 and every even non-code vertex is a peak, so the only slack is the number of valleys, i.e. the number
 of forest components. In the language of (*), P = 512 + 8|S| with S = the 236 even non-code vertices. To reach
 2399 one must shrink S to <= 235 (Step 8): keep a forest F with >= 277 vertices. Parity-only S (Z = S n O empty)
 cannot do it because |M| <= A(9,4) = 20; any improvement must remove some odd vertices Z and keep
 |M| - |Z| >= 21 even vertices M in the forest, with O \ Z u M acyclic, and then order S so that the extra term
 sum_{u in S}(N(u)-2)up(u) stays <= 1887 - 8|S|.
