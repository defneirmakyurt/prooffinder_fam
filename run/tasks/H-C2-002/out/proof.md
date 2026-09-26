# Proof: U(Q_5) = 88.

(Exact statement proved: every labelling of Q_5 has at least 88 uphill paths, and the labelling in
out/Q5.txt has exactly 88. Definitions exactly as in inbox/statement.md: a labelling of a graph G on
n vertices is a bijection f : V(G) -> {1,...,n}; v is a valley if every neighbour w of v has
f(w) > f(v); an uphill path is a sequence (v_1,...,v_k), k >= 1, with v_1 a valley, v_i ~ v_{i+1},
f(v_1) < ... < f(v_k); a lone valley counts (k = 1); U(G) is the minimum number of uphill paths over
all labellings; Q_d has vertex set {0,1}^d, adjacency = differ in exactly one coordinate.)

The lower bound is computer-assisted in exactly one place (Step 8: Q_5 has no 13-vertex decycling
set), with the reduction to the set searched written out. Steps 1-7 hold for every d-regular graph.

Notation. G is a finite simple d-regular graph on n vertices with edge set E, f a labelling.
For v put up(v) = #{w ~ v : f(w) > f(v)}, down(v) = #{w ~ v : f(w) < f(v)}. Labels are distinct, so
every neighbour is counted in exactly one of them: up(v) + down(v) = d. v is a valley iff down(v) = 0.
A *peak* is a vertex with up(v) = 0 (equivalently down(v) = d). N(v) = number of uphill paths whose
last vertex is v; P = P(f) = total number of uphill paths = sum_v N(v) (each path has one last vertex).
s = number of valleys.

---------------------------------------------------------------------------------------------------
Step 1. sum_v up(v) = |E| = sum_v down(v).

Each edge {u,v} has f(u) != f(v); if f(u) < f(v) the edge is counted in up(u) and in no other up(.)
(only its two endpoints can count it, and v does not since its other endpoint u is smaller). So each
edge contributes exactly 1 to sum up. Symmetrically each edge contributes exactly 1 to sum down,
namely at its larger endpoint.  []

Step 2. N(v) = [down(v) = 0] + sum_{w ~ v, f(w) < f(v)} N(w).

Length-1 paths ending at v: only (v), which is uphill iff v is a valley. Length >= 2: the map
(v_1,...,v_{k-1},v) -> (w = v_{k-1}, (v_1,...,v_{k-1})) is a bijection from uphill paths of length
>= 2 ending at v onto pairs (w, Q) with w ~ v, f(w) < f(v), Q an uphill path ending at w: deleting the
last vertex keeps "starts at a valley", adjacency and the increasing chain; conversely appending v to
Q ending at w with w ~ v, f(w) < f(v) extends the adjacency and the strict chain and keeps the
starting valley; the two maps are mutually inverse since v is fixed.  []

Step 3. N(v) >= 1 for all v; and if down(v) = k >= 1 then N(v) >= k.

Strong induction on f(v). If down(v) = 0, N(v) >= 1 by Step 2. If down(v) = k >= 1, Step 2 gives
N(v) = sum of the k values N(w) over the lower neighbours w, each >= 1 by induction (f(w) < f(v)),
so N(v) >= k >= 1. The vertex with label 1 has down = 0, so the induction starts.  []

Step 4. P = s + sum_v N(v) * up(v).

Length-1 uphill paths are the s valleys. A path of length >= 2 is determined by (its prefix Q
without the last vertex, the last vertex x), where Q is an uphill path ending at some w and x ~ w with
f(x) > f(w); this is a bijection by the argument of Step 2. The number of such pairs is
sum_w N(w) * up(w).  []

Step 5 (key lemma, any labelling). D_f := {v : down(v) >= 2} is a decycling set, i.e. the subgraph
induced by V \ D_f = {v : down(v) <= 1} has no cycle.

Suppose C = (c_1,...,c_m), m >= 3, is a cycle all of whose vertices have down <= 1. Let c_j be the
vertex of C with the largest label (labels are distinct). Its two cycle-neighbours c_{j-1}, c_{j+1}
(indices mod m) are distinct (m >= 3), are neighbours of c_j in G, and have smaller labels. So
down(c_j) >= 2, contradicting c_j not in D_f.  []

Step 6 (lower bound for d-regular G, d >= 2). P(f) >= n + (d-1) * |D_f| >= n + (d-1) * nabla(G),
where nabla(G) is the decycling number (least size of a decycling set).

Partition V into Val (down = 0, s vertices), T (down = 1), D' (2 <= down <= d-1) and M (peaks,
down = d). Then D_f = D' u M.
(a) By Step 4 and Step 1,
      P = s + sum_v up(v) + sum_v (N(v)-1) up(v) = s + |E| + sum_v (N(v)-1) up(v).
    Every term (N(v)-1)up(v) is >= 0 (Step 3). For v in D' with down(v) = k_v, Step 3 gives
    N(v) >= k_v and up(v) = d - k_v, so the term is >= (k_v - 1)(d - k_v). Dropping the other
    (non-negative) terms:   P >= |E| + s + sum_{v in D'} (k_v - 1)(d - k_v).
(b) By Step 1, |E| = sum_v down(v) = |T| + sum_{D'} k_v + d|M|, and n = s + |T| + |D'| + |M|.
    Eliminating |T|:   s = n - |E| + (d-1)|M| + sum_{v in D'} (k_v - 1).
(c) Substituting (b) into (a):
      P >= n + (d-1)|M| + sum_{v in D'} (k_v - 1)(d + 1 - k_v).
    For 2 <= k <= d-1:  (k-1)(d+1-k) - (d-1) = (k-1)(d-k) + (k-1) - (d-1) = (k-1)(d-k) - (d-k)
    = (k-2)(d-k) >= 0.  Hence each v in D' contributes >= d-1, and
      P >= n + (d-1)(|M| + |D'|) = n + (d-1)|D_f|.
(d) By Step 5, |D_f| >= nabla(G).  []

(Checks: Q_3, nabla = 3: bound 8 + 2*3 = 14; Q_4, nabla = 6: bound 16 + 3*6 = 34 -- the values of
the earlier cell. Numerical sanity check of Steps 5-6 on 3000 random labellings of Q_3..Q_6:
code/sanity.py, 0 violations. This check is not part of the proof.)

Step 7 (edge identity). Let G be d-regular on n vertices, D a decycling set, F = V \ D non-empty,
and c >= 1 the number of components of the forest G[F]; e(D) = #edges with both ends in D. Then
      (d-1)|D| = |E| - n + c + e(D).
Proof: a forest on |F| vertices with c components has |F| - c edges. Edges between D and F number
d|D| - 2e(D) (degree sum over D). So |E| = (|F| - c) + e(D) + (d|D| - 2e(D)) = n - |D| - c
+ d|D| - e(D), which rearranges to the claim.  []
For Q_5 (|E| = 80, n = 32): 4|D| = 48 + c + e(D) >= 49, so every decycling set has >= 13 vertices.
With Step 6 this already gives, by hand, U(Q_5) >= 32 + 4*13 = 84.

Step 8 (computer-assisted). Q_5 has no decycling set of 13 vertices; hence nabla(Q_5) >= 14.

Reduction to the search actually performed by out/code/decycle.py (python3 decycle.py 5 13):
 (i)  If some decycling set D has |D| <= 13 then one has exactly 13 vertices: add any vertices;
      an induced subgraph of a forest is a forest. So it suffices to exclude |D| = 13.
 (ii) x -> x XOR a is an automorphism of Q_5 for every a, mapping decycling sets to decycling sets.
      If D is a 13-vertex decycling set and a in D, then D XOR a contains vertex 0. So assume 0 in D.
 (iii) For |D| = 13, Step 7 gives c + e(D) = 52 - 48 = 4 with c >= 1 (F has 19 >= 1 vertices),
      so e(D) <= 3. Branches whose partial D already spans more than 3 edges are cut. (e(D) only
      grows as vertices are added, so the cut loses no solution.)
 (iv) The search decides the vertices 0,1,...,31 (integer = 0/1 string read in binary) in order,
      each into D or F. When v enters F, the program looks at its already-decided F-neighbours;
      adding v closes a cycle in G[F] iff two of them are already in the same component of the
      current forest (a new cycle through v must use two distinct edges at v into one component;
      conversely two such neighbours give a cycle). Components are tracked exactly by union-find
      with rollback. Branches that close a cycle are cut (a forest stays a forest under the later
      additions only if no cycle is ever closed, and a cycle once present persists as an induced
      subgraph because vertices are never removed from F). Branches with |D| > 13 or with too few
      remaining vertices to reach |D| = 13 are cut.
 So the search visits every set D with |D| = 13, 0 in D, e(D) <= 3 and G[V \ D] acyclic, and the
 program reports none: "d=5 k=13 edge_prune=True: NONE (search nodes 12742)", 0.042 s.
 Cross-check without cut (iii): "d=5 k=13 edge_prune=False: NONE (search nodes 3907075)", 5.4 s.
 Independent second implementation (out/code/brute13.c, C): enumerates ALL C(31,12) = 141120525
 13-subsets containing vertex 0 (only reduction (ii) used; no cut (iii), no union-find) and tests
 "#edges(F) = |F| - #components(F)" by bitmask BFS: "k=13 subsets checked=141120525 decycling
 found=0", 2.4 s. Control: with k = 14 it finds 945 decycling 14-sets containing 0 (3.5 s).
 Controls: the same program reports NONE for (d,k) = (3,2), (4,5) and FOUND for (3,3), (4,6),
 (5,14), each found set confirmed by an independent edge/component count (is_decycling), matching
 nabla(Q_3) = 3, nabla(Q_4) = 6 (and a 14-set for Q_5, e.g. the set D of Step 9).  []

Step 9 (lower bound for Q_5). By Steps 6 and 8, every labelling f of Q_5 has
      P(f) >= 32 + 4 * |D_f| >= 32 + 4 * 14 = 88.

Step 10 (matching labelling). out/Q5.txt (produced by code/construct.py 5) lists, in label order:
  labels 1-6   : 00000, 00001, 00010, 00100, 01000, 10000
  labels 7-12  : 01111, 01110, 01101, 01011, 00111, 11111
  labels 13-18 : 10011, 10101, 10110, 11001, 11010, 11100
  labels 19-32 : 00011, 00101, 00110, 01001, 01010, 01100, 10001, 10010, 10100, 10111, 11000,
                 11011, 11101, 11110
Structure: S = {00000, 01111} (even weight, Hamming distance 4). F = S u {odd-weight vertices}
(18 vertices, labels 1-18); D = even-weight vertices not in S (14 vertices, labels 19-32).
Hand count. Every edge of Q_5 joins an odd and an even vertex.
 - 00000 and 01111 (labels 1, 7): all their neighbours are odd and have larger labels (the five
   neighbours of 00000 are labels 2-6, those of 01111 are labels 8-12). Valleys, N = 1.
 - Labels 2-6 (neighbours of 00000) and 8-12 (neighbours of 01111): each is at distance 1 from one
   element of S and distance >= 3 from the other (00000 and 01111 differ in 4 coordinates), so its
   only even neighbour with smaller label is that element of S; all its other neighbours are even
   vertices of D (labels >= 19). down = 1, N = 1.
 - Labels 13-18: the six weight-3 vertices whose first (leftmost) coordinate is 1. None is adjacent
   to 00000 (its neighbours have weight 1) or to 01111 (its neighbours are 11111 and the four
   weight-3 vertices with first coordinate 0). So all five neighbours are even and not in S, i.e.
   have labels >= 19. Valleys, N = 1.
 - Bookkeeping: the 16 odd vertices are the 5 of weight 1 (labels 2-6), the 10 of weight 3 (four at
   labels 8-11, six at 13-18) and 11111 (label 12); so every odd vertex is covered above.
 - Labels 19-32: even vertices, all five neighbours odd, hence labels <= 18. Peaks with down = 5
   and N = sum of five N-values, each 1, so N = 5.
 Total P = 18 * 1 + 14 * 5 = 88. The accepted checker agrees: inbox/checker/verify.py out/Q5.txt
 --d 5 -> "VERIFIED 88". (The count equals the Step 6 bound: n + (d-1)|D| = 32 + 4*14, with D
 independent.)  []

Conclusion. U(Q_5) = 88.

---------------------------------------------------------------------------------------------------
By-products (NOT part of the cell; recorded for the team).
(A) General matching construction. If a d-regular graph G has an INDEPENDENT decycling set D, then
labelling each tree of the forest G[V \ D] in BFS order from a root (trees one after another), and
then D in any order, gives P = n + (d-1)|D|: each F-vertex has exactly one smaller neighbour (its
BFS parent) or none (root), so N = 1; each D-vertex has all d neighbours in F, so N = d; total
(n - |D|) + d|D|. Hence, with Step 6: if some minimum decycling set of a d-regular G is independent,
U(G) = n + (d-1) nabla(G).
(B) For Q_d the construction with D = (even vertices) minus S, S an even-weight code of minimum
distance 4, gives P = (d+1)2^(d-1) - (d-1)|S|: checker counts 88, 204, 464, 1040 for d = 5..8
(|S| = 2, 4, 8, 16; out/Q5.txt..Q8.txt), and for d = 9 with |S| = 20 it would give 2400, the
organisers' stated upper bound (not built here).
(C) Same method, d = 6: decycle.py 6 27 -> NONE (8.2 s), so nabla(Q_6) >= 28 and, by Step 6,
U(Q_6) >= 64 + 5*28 = 204, matched by out/Q6.txt (VERIFIED 204). Reduction identical to Step 8
with e(D) <= 5*27 - 4*32 - 1 = 6. This is a neighbour cell; recorded, not claimed here.
(D) For d = 7, 8 the bound of Step 6 would match out/Q7.txt, Q8.txt (464, 1040) iff
nabla(Q_7) >= 56 and nabla(Q_8) >= 112. A web-search summary asserts nabla(Q_7) = 56,
nabla(Q_8) = 112, but I could not open any source (sources.md: UNSURE). NOT established here.
