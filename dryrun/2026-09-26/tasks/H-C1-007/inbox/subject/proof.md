# Proof: U(Q_3) = 14 and U(Q_4) = 34.

(First line above is the exact statement proved. All definitions are those of inbox/statement.md:
a labelling of a graph G on n vertices is a bijection f : V(G) -> {1,...,n}; v is a valley if every
neighbour w of v has f(w) > f(v) (an isolated vertex is a valley); an uphill path is a sequence
(v_1,...,v_k), k >= 1, with v_1 a valley, v_i ~ v_{i+1}, and f(v_1) < ... < f(v_k); U(G) is the
minimum over labellings of the number of uphill paths; Q_d has vertex set {0,1}^d with two vertices
adjacent when they differ in exactly one coordinate, so |V(Q_d)| = 2^d and |E(Q_d)| = d*2^{d-1}.)

Throughout, G is a finite simple graph, f a labelling of G, n = |V(G)|, E = E(G).
No result is claimed for any d outside {3,4}.

Notation. For a vertex v put
    up(v)   = #{w : w ~ v and f(w) > f(v)},
    down(v) = #{w : w ~ v and f(w) < f(v)},
    N(v)    = the number of uphill paths (v_1,...,v_k) with v_k = v.
Since f is injective, every neighbour w of v satisfies exactly one of f(w) > f(v), f(w) < f(v);
hence up(v) + down(v) = deg(v). By definition v is a valley iff down(v) = 0.
Let P = P(f) denote the total number of uphill paths of f, and let Val = Val(f) be the set of
valleys. Each uphill path has exactly one last vertex, so P = sum over v in V of N(v).

--------------------------------------------------------------------------------------------------
Step 1. The two degree sums.  sum_{v in V} up(v) = |E| = sum_{v in V} down(v).

Proof. Fix an edge {u,v}. Since f is injective, f(u) != f(v), so exactly one of the two orderings
f(u) < f(v), f(v) < f(u) holds; say f(u) < f(v). Then the edge {u,v} is counted once in up(u)
(because v ~ u and f(v) > f(u)) and in up(w) for no other vertex w: up(w) counts only edges
incident with w, and of the two endpoints of {u,v} only u has the other endpoint larger. So each
edge is counted exactly once in sum_v up(v), giving sum_v up(v) = |E|. The same argument with the
roles of "larger" and "smaller" exchanged counts each edge exactly once at its endpoint with the
larger label, giving sum_v down(v) = |E|.  []

--------------------------------------------------------------------------------------------------
Step 2 (recurrence).  For every vertex v,
    N(v) = [down(v) = 0] + sum over {w : w ~ v, f(w) < f(v)} of N(w),
where [.] is 1 if the condition holds and 0 otherwise.

Proof. Split the uphill paths ending at v by their length k.

k = 1: the only sequence of length 1 ending at v is (v), and by the definition (v) is an uphill path
iff its first vertex v is a valley, i.e. iff down(v) = 0. This contributes [down(v) = 0].

k >= 2: let A be the set of uphill paths of length >= 2 ending at v, and let B be the set of pairs
(w, Q) where w ~ v, f(w) < f(v), and Q is an uphill path ending at w. Define
phi(v_1,...,v_{k-1},v) = (v_{k-1}, (v_1,...,v_{k-1})).

phi maps A into B: if (v_1,...,v_{k-1},v) is an uphill path with k >= 2, then v_1 is a valley,
v_i ~ v_{i+1} for 1 <= i <= k-2 (a subset of the adjacencies assumed), and
f(v_1) < ... < f(v_{k-1}) (a sub-chain of the assumed strict chain); hence (v_1,...,v_{k-1}) is an
uphill path ending at w := v_{k-1}. Also w ~ v (consecutive vertices of the path) and f(w) < f(v)
(the last inequality of the chain). So the image lies in B.

phi is injective: from the pair (w, (v_1,...,v_{k-1})) the original sequence is recovered as
(v_1,...,v_{k-1},v), since v is fixed.

phi is surjective: given (w, (v_1,...,v_{k-1})) in B with v_{k-1} = w, the sequence
(v_1,...,v_{k-1},v) has v_1 a valley, consecutive vertices adjacent (the old adjacencies, plus
v_{k-1} = w ~ v), and strictly increasing labels (the old chain, extended by f(w) < f(v)). So it is
an uphill path, it has length k >= 2, it ends at v, and phi sends it to the given pair.

Hence |A| = |B| = sum over {w ~ v : f(w) < f(v)} of N(w), which is the claim.  []

--------------------------------------------------------------------------------------------------
Step 3.  N(v) >= 1 for every vertex v.

Proof. By strong induction on f(v). Let v be given and assume N(u) >= 1 for every u with
f(u) < f(v). All terms in Step 2 are counts, hence >= 0. If down(v) = 0 then Step 2 gives
N(v) >= [down(v) = 0] = 1. If down(v) >= 1, pick a neighbour w of v with f(w) < f(v); by Step 2 and
non-negativity of the other terms, N(v) >= N(w), and N(w) >= 1 by the induction hypothesis. The
induction starts correctly: the vertex v with f(v) = 1 has every neighbour labelled higher, so
down(v) = 0 and the first case applies, using no hypothesis.  []

--------------------------------------------------------------------------------------------------
Step 4 (exact identity).  P = |Val| + sum over v in V of N(v) * up(v).

Proof. Split all uphill paths by length. Those of length 1 are exactly the sequences (v) with v a
valley, and there are |Val| of them. For length >= 2, map (v_1,...,v_k) to the pair
((v_1,...,v_{k-1}), v_k). By exactly the argument of Step 2 (applied for each choice of last vertex
v_k, and noting that each uphill path of length >= 2 has a unique last vertex), this is a bijection
onto the set of pairs (Q, x) where Q is an uphill path ending at some vertex w and x ~ w with
f(x) > f(w). The number of such pairs is sum over w of N(w) * #{x ~ w : f(x) > f(w)}
= sum over w of N(w) * up(w).  []

--------------------------------------------------------------------------------------------------
Step 5 (general lower bound).  For every finite simple graph G and every labelling f,
    P >= |E| + |Val| >= |E| + 1.

Proof. By Step 3, N(v) >= 1 for every v, and up(v) >= 0, so N(v)*up(v) >= up(v). Summing and using
Step 4 and then Step 1,
    P = |Val| + sum_v N(v)*up(v) >= |Val| + sum_v up(v) = |Val| + |E|.
Finally |Val| >= 1: the vertex v with f(v) = 1 has f(w) > 1 = f(v) for every neighbour w (labels are
distinct and 1 is the least), so v is a valley.  []

(This is the lower-bound step of the official IMO 2022 Problem 6 solution, stated there for the
grid; see out/sources.md, Bajnok arXiv:2509.19303. For Q_3 it gives P >= 13 and for Q_4 P >= 33,
which is one short of the truth in both cases. Steps 6-7 close that gap.)

--------------------------------------------------------------------------------------------------
Step 6 (structure of an equality labelling).  Let G be a finite simple graph with no isolated
vertex and let f be a labelling with P = |E| + 1. Put m = #{v : up(v) = 0}. Then
    |E| = sum over v of down(v) = n - 1 - m + sum over {v : up(v) = 0} of deg(v).

Proof. From the chain of inequalities in Step 5,
    |E| + 1 = P = |Val| + sum_v N(v)*up(v) >= |Val| + sum_v up(v) = |Val| + |E| >= 1 + |E|,
so both inequalities are equalities. Equality in the second gives |Val| = 1; write Val = {v_0}.
Equality in the first gives sum_v (N(v) - 1) * up(v) = 0; every summand is >= 0 by Step 3, so
    (*)  N(v) = 1 for every v with up(v) >= 1.

Let M = {v : up(v) = 0}, so |M| = m, and let R = V \ ({v_0} u M).

(a) v_0 is not in M. Indeed down(v_0) = 0 and deg(v_0) >= 1 (no isolated vertices), so
up(v_0) = deg(v_0) - down(v_0) = deg(v_0) >= 1. Hence {v_0}, M, R is a partition of V, and
|R| = n - 1 - m.

(b) down(v_0) = 0, by definition of valley.

(c) For v in M: up(v) = 0, so down(v) = deg(v).

(d) For v in R: v is not in M, so up(v) >= 1, and (*) gives N(v) = 1. Also v != v_0 and v_0 is the
only valley, so down(v) >= 1 and the term [down(v) = 0] in Step 2 is 0. Therefore
    1 = N(v) = sum over the down(v) neighbours w of v with f(w) < f(v) of N(w),
a sum of down(v) terms each >= 1 by Step 3, with down(v) >= 1. A sum of t >= 1 integers each >= 1
equals 1 only if t = 1. Hence down(v) = 1.

Summing down over the partition and using Step 1:
    |E| = sum_v down(v) = 0 + sum_{v in M} deg(v) + |R|*1 = sum_{v in M} deg(v) + (n - 1 - m).  []

--------------------------------------------------------------------------------------------------
Step 7 (the cube has no equality labelling for d = 3, 4).  For d in {3,4}, no labelling f of Q_d
satisfies P(f) = |E(Q_d)| + 1. Consequently every labelling of Q_d has at least |E(Q_d)| + 2
uphill paths, i.e. U(Q_3) >= 14 and U(Q_4) >= 34.

Proof. Q_d is a finite simple graph in which every vertex has degree exactly d >= 3 >= 1, so it has
no isolated vertex and Step 6 applies. Here n = 2^d and |E| = d * 2^{d-1} (each of the 2^d vertices
has degree d and each edge has two endpoints, so |E| = d*2^d/2). Suppose P = |E| + 1 for some
labelling. With m as in Step 6, deg(v) = d for all v, so Step 6 reads
    d * 2^{d-1} = m*d + 2^d - 1 - m,  i.e.  (d - 1) * m = d * 2^{d-1} - 2^d + 1 = 2^{d-1}(d-2) + 1.
m is a non-negative integer, so (d-1) must divide 2^{d-1}(d-2) + 1.

d = 3: the equation is 2m = 4*1 + 1 = 5. The left side is even and 5 is odd, so there is no integer
solution m. Contradiction.

d = 4: the equation is 3m = 8*2 + 1 = 17. Now 17 = 3*5 + 2 is not a multiple of 3, so there is no
integer solution m. Contradiction.

So in both cases no labelling attains |E| + 1. By Step 5 every labelling has P >= |E| + 1, and
P is an integer, so every labelling has P >= |E| + 2. For d = 3, |E| = 3*4 = 12 and the bound is 14;
for d = 4, |E| = 4*8 = 32 and the bound is 34.  []

--------------------------------------------------------------------------------------------------
Step 8 (matching labellings).  There is a labelling of Q_3 with exactly 14 uphill paths and a
labelling of Q_4 with exactly 34 uphill paths.

Proof. Exhibit them. Writing each vertex as a 0/1 string of length d (leftmost character =
coordinate d-1), in increasing label order:

  out/Q3.txt :  000, 001, 010, 011, 101, 110, 100, 111
  out/Q4.txt :  1010, 0111, 0101, 1011, 1000, 0010, 0001, 0011,
                1101, 1110, 1001, 0100, 0000, 0110, 1111, 1100

Each list is a permutation of {0,1}^d, hence a labelling. The number of uphill paths of each was
computed in two independent ways -- by the recurrence of Step 2, and by explicitly enumerating every
uphill path with a depth-first traversal that starts at each valley and extends to higher-labelled
neighbours -- and both give 14 and 34 respectively (out/code/uphill.py; runs 1 and 4 of
out/runlog.md, exact integer arithmetic, < 0.1 s each). For Q_3 the value 14 is also the minimum
over a complete enumeration of all 8! = 40320 labellings (out/code/q3_exhaustive.py, run 2).

For readers who want the Q_3 witness checked by hand: with the labels 1..8 assigned in the listed
order, N(000)=1 (valley), N(001)=1, N(010)=1, N(011)=N(001)+N(010)=2, N(101)=N(001)=1,
N(110)=N(010)=1, N(100)=N(000)+N(101)+N(110)=3, N(111)=N(011)+N(101)+N(110)=4; the total is
1+1+1+2+1+1+3+4 = 14. (Check of the neighbour lists used: 011 ~ 001,010,111; 101 ~ 001,100,111;
110 ~ 010,100,111; 100 ~ 000,101,110; 111 ~ 011,101,110. In each case only the neighbours with a
smaller label are summed.)  []

--------------------------------------------------------------------------------------------------
Conclusion.  By Step 7, every labelling of Q_3 has at least 14 uphill paths and every labelling of
Q_4 has at least 34; by Step 8 both values are attained. Therefore

        U(Q_3) = 14        and        U(Q_4) = 34.

--------------------------------------------------------------------------------------------------
Remark (NOT part of the cell, recorded only as a by-product; the cell asks for d = 3, 4 only).
Step 6 applies to any regular graph. For Q_d with d >= 2 the equality condition is
(d-1) | 2^{d-1}(d-2) + 1, i.e. (since d - 2 = -1 + (d-1)) 2^{d-1} = 1 mod (d-1). It is classical
that n | 2^n - 1 forces n = 1 (let p be the least prime factor of n > 1; then n is odd, the
multiplicative order of 2 mod p divides both n and p - 1, hence divides gcd(n, p-1) = 1, so p | 1,
a contradiction). With n = d - 1 this says the condition holds only for d = 2. So for every d >= 3,
    U(Q_d) >= d * 2^{d-1} + 2.
I have checked this argument but it is outside the cell's parameter range and is not used above.
