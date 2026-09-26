# Theorem (H-L1). For every integer d >= 3 and every labelling f of Q_d, the number of uphill paths of f is at least d*2^(d-1) + 2. Equivalently, U(Q_d) >= |E(Q_d)| + 2 for every d >= 3.

(First line above is the exact statement proved. Nothing is claimed for d = 1, 2; see Remark 3.)

Definitions, exactly as in inbox/statement.md. G is a finite simple graph on n vertices. A labelling
is a bijection f : V(G) -> {1,...,n}. A vertex v is a *valley* if every neighbour w of v has
f(w) > f(v) (an isolated vertex is a valley). An *uphill path* is a sequence (v_1,...,v_k), k >= 1,
with v_1 a valley, v_i adjacent to v_{i+1} for 1 <= i < k, and f(v_1) < f(v_2) < ... < f(v_k); a
valley on its own (k = 1) is an uphill path; paths are sequences, so different sequences are
different paths even if they share endpoints. U(G) is the minimum, over all labellings, of the number
of uphill paths. Q_d has vertex set {0,1}^d, two vertices adjacent iff they differ in exactly one
coordinate.

The proof uses no computation and no citation. Part A proves general facts about an arbitrary
finite simple graph; Part B proves one elementary number-theoretic fact; Part C combines them for Q_d.

---------------------------------------------------------------------------------------------------
## Part A. An arbitrary finite simple graph G with a labelling f

Notation. n = |V(G)|, E = E(G), u ~ v means u and v are adjacent. For a vertex v:

* up(v)   = #{ w : w ~ v, f(w) > f(v) },
* down(v) = #{ w : w ~ v, f(w) < f(v) },
* N(v)    = the number of uphill paths (v_1,...,v_k) with v_k = v,
* [S] = 1 if the statement S is true and 0 if it is false.

Val = Val(f) is the set of valleys, and P = P(f) is the number of uphill paths of f.

**Step 1 (basic facts).**
(a) For every vertex v, up(v) + down(v) = deg(v).
(b) v is a valley if and only if down(v) = 0.
(c) P is a finite non-negative integer, each N(v) is a finite non-negative integer, and
    P = sum over v in V of N(v).

Proof. (a) Let w ~ v. Then w != v (simple graph, no loops), so f(w) != f(v) because f is injective;
hence exactly one of f(w) > f(v), f(w) < f(v) holds. So every one of the deg(v) neighbours is counted
in exactly one of up(v), down(v).
(b) By definition v is a valley iff every neighbour w has f(w) > f(v), i.e. iff no neighbour has
f(w) <= f(v). Since a neighbour w satisfies f(w) != f(v) (see (a)), "f(w) <= f(v)" is the same as
"f(w) < f(v)". So v is a valley iff down(v) = 0. (For an isolated vertex both sides are true: it is a
valley by definition and down(v) = 0.)
(c) In an uphill path the labels f(v_1) < ... < f(v_k) are strictly increasing, so the v_i are
pairwise distinct (if v_i = v_j with i < j, then f(v_i) = f(v_j), contradicting f(v_i) < f(v_j));
hence k <= n. There are finitely many sequences of vertices of
length at most n, so P is finite, and so is each N(v) <= P. Every uphill path has exactly one last
vertex v_k, so the uphill paths are partitioned according to their last vertex, and
P = sum_v N(v).  []

**Step 2 (the two degree sums).** sum_{v in V} up(v) = |E| = sum_{v in V} down(v).

Proof. The quantity sum_v up(v) counts the pairs (v, w) with w ~ v and f(w) > f(v). Every such pair
determines the edge {v, w}. Conversely, fix an edge {a, b}; by Step 1(a) exactly one of f(a) < f(b),
f(b) < f(a) holds, say f(a) < f(b) (otherwise rename). The ordered pairs (v, w) with {v, w} = {a, b}
are (a, b) and (b, a); the first satisfies f(w) > f(v) and the second does not. So each edge
corresponds to exactly one counted pair, and sum_v up(v) = |E|. The same argument with ">" replaced
by "<" (now only the pair (b, a) is counted) gives sum_v down(v) = |E|.  []

**Step 3 (recurrence).** For every vertex v,

    N(v) = [down(v) = 0] + sum over { w : w ~ v, f(w) < f(v) } of N(w).

Proof. Split the uphill paths ending at v by their length k.

k = 1. The only sequence of length 1 ending at v is (v). By definition it is an uphill path iff v is
a valley, i.e. (Step 1(b)) iff down(v) = 0. This contributes [down(v) = 0].

k >= 2. Let A be the set of uphill paths of length >= 2 ending at v, and B the set of pairs (w, Q)
with w ~ v, f(w) < f(v), and Q an uphill path ending at w. Define
phi(v_1,...,v_{k-1}, v) = (v_{k-1}, (v_1,...,v_{k-1})).
* phi(A) is contained in B: the sequence (v_1,...,v_{k-1}) has length k - 1 >= 1, first vertex v_1 a
  valley, consecutive vertices adjacent (these adjacencies are among those of the original path), and
  strictly increasing labels (a sub-chain of the original chain), so it is an uphill path; it ends at
  w := v_{k-1}; w ~ v (they are consecutive in the original path); f(w) < f(v) (last inequality of
  the original chain).
* phi is injective: the image pair (w, (v_1,...,v_{k-1})) determines (v_1,...,v_{k-1}, v), since v
  is fixed.
* phi is onto B: given (w, (v_1,...,v_j)) in B with v_j = w, the sequence (v_1,...,v_j, v) has v_1 a
  valley, consecutive vertices adjacent (the old adjacencies and v_j = w ~ v), and strictly increasing
  labels (the old chain and f(w) < f(v)); it has length j + 1 >= 2 and ends at v, so it lies in A,
  and phi maps it to the given pair.
Hence |A| = |B|, and |B| = sum over the lower neighbours w of v of N(w) (for each such w there are
exactly N(w) choices of Q). Adding the two cases gives the formula.  []

**Step 4 (every vertex ends an uphill path).** N(v) >= 1 for every vertex v.

Proof. Strong induction on the label t = f(v), t = 1, 2, ..., n. Let v have label t and assume
N(u) >= 1 for every u with f(u) < t (for t = 1 this assumption is empty). All terms on the right of
Step 3 are non-negative integers.
* If down(v) = 0, Step 3 gives N(v) >= [down(v) = 0] = 1.
* If down(v) >= 1, choose a neighbour w with f(w) < f(v) = t. Step 3 gives N(v) >= N(w), and
  N(w) >= 1 by the induction hypothesis (f(w) < t).
For t = 1 the second case cannot occur (no label is below 1, so down(v) = 0), so the first case
applies and no hypothesis is used.  []

**Step 5 (exact identity).**

    P = |Val| + sum_{v in V} N(v) * up(v).

Proof. Split the uphill paths by length. Those of length 1 are exactly the sequences (v) with v a
valley: |Val| of them. For those of length >= 2, let C be the set of pairs (Q, x) where Q is an uphill
path, w is the last vertex of Q, x ~ w and f(x) > f(w). The map psi(v_1,...,v_k) = ((v_1,...,v_{k-1}), v_k)
(k >= 2) is a bijection from the set of uphill paths of length >= 2 onto C:
* into C: (v_1,...,v_{k-1}) is an uphill path (same verification as in Step 3), its last vertex is
  v_{k-1}, v_k ~ v_{k-1}, and f(v_k) > f(v_{k-1});
* injective: the pair determines the sequence (append x to Q);
* onto: for (Q, x) in C with Q = (v_1,...,v_j), the sequence (v_1,...,v_j, x) has v_1 a valley,
  consecutive vertices adjacent, strictly increasing labels (f(x) > f(v_j)), length j + 1 >= 2, and
  psi maps it to (Q, x).
Grouping the pairs in C by the last vertex w of Q: there are N(w) choices of Q and up(w) choices of x,
so |C| = sum_w N(w) * up(w).  []

**Step 6 (general lower bound, with the exact excess).**

    P - (|E| + 1) = (|Val| - 1) + sum_{v in V} (N(v) - 1) * up(v),

and both terms on the right are >= 0. In particular P >= |E| + 1 for every finite simple graph with at
least one vertex and every labelling.

Proof. By Step 5 and Step 2,
P = |Val| + sum_v N(v) up(v) = |Val| + sum_v up(v) + sum_v (N(v) - 1) up(v)
  = |Val| + |E| + sum_v (N(v) - 1) up(v);
subtract |E| + 1. Each summand (N(v) - 1) up(v) is a product of two non-negative integers (Step 4 and
the definition of up), so the sum is >= 0. |Val| >= 1: let v* be the vertex with f(v*) = 1 (it exists
because f is onto {1,...,n} and n >= 1); every neighbour w of v* has f(w) != 1, so f(w) > 1 = f(v*),
and v* is a valley.  []

(This bound P >= |E| + 1 is the lower-bound half of the official solution of IMO 2022 Problem 6,
there written for the grid; see out/sources.md. It is re-proved here in full, Steps 1-6.)

**Step 7 (equality structure).** Let G have no isolated vertex, and let f be a labelling with
P = |E| + 1. Let M = { v : up(v) = 0 } and m = |M|. Then

    |E| = (n - 1 - m) + sum_{v in M} deg(v).

Proof. By Step 6, 0 = P - (|E| + 1) is a sum of two non-negative integers, so both are 0:
(i) |Val| = 1; write Val = {v_0};
(ii) sum_v (N(v) - 1) up(v) = 0, and since every summand is >= 0, every summand is 0; so for every v
     with up(v) >= 1 we have N(v) - 1 = 0, i.e. N(v) = 1.
Let R = V \ ({v_0} u M). We determine down(v) on each of the three sets.
* v_0 is not in M: down(v_0) = 0 (Step 1(b)), and deg(v_0) >= 1 (no isolated vertex), so by
  Step 1(a) up(v_0) = deg(v_0) >= 1. Hence {v_0}, M, R are pairwise disjoint with union V, and
  |R| = n - 1 - m.
* down(v_0) = 0 (v_0 is a valley, Step 1(b)).
* For v in M: up(v) = 0, so down(v) = deg(v) by Step 1(a).
* For v in R: v is not in M, so up(v) >= 1 and N(v) = 1 by (ii). Also v != v_0 and v_0 is the only
  valley, so v is not a valley and down(v) >= 1 (Step 1(b)); in particular [down(v) = 0] = 0. Step 3
  gives 1 = N(v) = sum of N(w) over the down(v) lower neighbours w of v. Each of these down(v) terms
  is >= 1 (Step 4), so 1 = N(v) >= down(v) * 1, i.e. down(v) <= 1. Together with down(v) >= 1 this
  gives down(v) = 1.
Summing down(v) over the partition and using Step 2:
|E| = sum_v down(v) = 0 + sum_{v in M} deg(v) + |R| * 1 = sum_{v in M} deg(v) + (n - 1 - m).  []

---------------------------------------------------------------------------------------------------
## Part B. A number-theoretic fact

Facts from elementary arithmetic used below (all integers): the division algorithm (for a >= 0 and
r >= 1 there are q >= 0 and 0 <= s < r with a = qr + s); every integer > 1 has a prime factor (its
least divisor > 1 is prime: a proper factorisation of it would give a smaller divisor > 1); Euclid's
lemma (if a prime p divides ab then p | a or p | b).

**Step 8.** For every integer k >= 2, k does not divide 2^k - 1.

Proof. Suppose k >= 2 and k | 2^k - 1.
(1) k is odd: 2^k - 1 is odd (2^k is even since k >= 1); if k were even, then 2 | k | 2^k - 1, so
    2^k - 1 would be even, a contradiction.
(2) Let p be the least prime factor of k (it exists since k > 1). p divides the odd number k, so p is
    odd; hence p >= 3 and p does not divide 2 (the only prime dividing 2 is 2). By Euclid's lemma and
    induction on i, p does not divide 2^i for any i >= 0.
(3) There is an integer r with 1 <= r <= p - 1 and p | 2^r - 1. Indeed, the p integers
    2^0, 2^1, ..., 2^(p-1) have remainders mod p in {1, ..., p-1} (none is 0, by (2)); this set has
    p - 1 elements, so by the pigeonhole principle two coincide: 2^i and 2^j with 0 <= i < j <= p - 1
    leave the same remainder, so p | 2^j - 2^i = 2^i (2^(j-i) - 1). Since p does not divide 2^i (2),
    Euclid's lemma gives p | 2^(j-i) - 1, and r := j - i satisfies 1 <= r <= p - 1.
    Let r now denote the LEAST positive integer with p | 2^r - 1; by what was just shown, r <= p - 1.
(4) r divides k. Write k = qr + s with q >= 0 and 0 <= s < r. Since p | k | 2^k - 1, we have
    2^k = 1 (mod p). Also 2^r = 1 (mod p) gives 2^(qr) = (2^r)^q = 1 (mod p) (because
    a^q - 1 = (a - 1)(a^(q-1) + ... + a + 1) for q >= 1, and for q = 0 both sides are 1). Then
    2^k - 2^s = 2^s (2^(qr) - 1) is divisible by p, so 2^s = 2^k = 1 (mod p), i.e. p | 2^s - 1. If s >= 1 this contradicts
    the minimality of r (s < r). So s = 0 and r | k.
(5) r = 1. If r >= 2, r has a prime factor q'. Then q' | r | k, so q' is a prime factor of k, and
    q' <= r <= p - 1 < p, contradicting the choice of p as the least prime factor of k.
(6) With r = 1, p | 2^1 - 1 = 1, which is impossible since p >= 2.
All cases lead to a contradiction, so k does not divide 2^k - 1.  []

---------------------------------------------------------------------------------------------------
## Part C. The hypercube

**Step 9 (Q_d is d-regular with d*2^(d-1) edges).** For d >= 1, Q_d has n = 2^d vertices, every
vertex has degree exactly d, and |E(Q_d)| = d * 2^(d-1). In particular Q_d has no isolated vertex.

Proof. |{0,1}^d| = 2^d. For x in {0,1}^d and i in {1,...,d} let x^(i) be x with coordinate i flipped.
The neighbours of x are exactly the vertices differing from x in exactly one coordinate, i.e. exactly
x^(1),...,x^(d); these are pairwise distinct (x^(i) and x^(j), i != j, differ in coordinates i and j).
So deg(x) = d >= 1. Each edge has two endpoints, so sum_x deg(x) = 2|E|, i.e. d * 2^d = 2|E| and
|E| = d * 2^(d-1).  []

**Step 10 (no labelling of Q_d attains |E| + 1, for d >= 3).** Let d >= 3 and let f be any labelling
of Q_d. Then P(f) != d * 2^(d-1) + 1.

Proof. Suppose P(f) = |E| + 1 with |E| = d * 2^(d-1). By Step 9, Q_d has no isolated vertex, so
Step 7 applies; with M, m as there and deg(v) = d for all v (Step 9), it reads
    d * 2^(d-1) = (2^d - 1 - m) + m*d,
i.e.
    (d - 1) * m = d * 2^(d-1) - 2^d + 1 = 2^(d-1) * (d - 2) + 1.            (**)
Now
    2^(d-1) - 1 = 2^(d-1) * (d - 1) - [2^(d-1) * (d - 2) + 1]
                = 2^(d-1) * (d - 1) - (d - 1) * m        (by (**))
                = (d - 1) * (2^(d-1) - m).
(Check of the first line: 2^(d-1)(d-1) - 2^(d-1)(d-2) - 1 = 2^(d-1) - 1.) Since 2^(d-1) - m is an
integer, k := d - 1 divides 2^k - 1. But k = d - 1 >= 2 because d >= 3, contradicting Step 8.  []

**Step 11 (conclusion).** Let d >= 3 and let f be any labelling of Q_d. By Step 6 (Q_d has
2^d >= 1 vertices), P(f) >= |E| + 1 = d*2^(d-1) + 1. By Step 10, P(f) != d*2^(d-1) + 1. Since P(f) is
an integer (Step 1(c)), P(f) >= d*2^(d-1) + 2. As f was arbitrary and U(Q_d) is the minimum of P(f)
over the finitely many (namely (2^d)!) labellings, U(Q_d) >= d*2^(d-1) + 2 = |E(Q_d)| + 2.  []

---------------------------------------------------------------------------------------------------
## What is and is not established

* Established (PROVED here, no computation): U(Q_d) >= d*2^(d-1) + 2 for every integer d >= 3.
* Also proved on the way, for every finite simple graph G and labelling f (Steps 5-7):
  P = |Val| + sum_v N(v) up(v); P >= |E| + |Val| >= |E| + 1; and if G has no isolated vertex and
  P = |E| + 1 then |E| = n - 1 - m + sum_{up(v)=0} deg(v).
* NOT established here: any upper bound, any exact value of U(Q_d), or anything for d = 1, 2.

Remark 1 (sharpness for small d; not used). The bound is attained for d = 3 and d = 4
(U(Q_3) = 14, U(Q_4) = 34: the earlier literature proof inbox/earlier-proof.md Step 8 exhibits
labellings with 14 and 34 uphill paths, re-counted in two ways by out/code/sanity.py check F; check C
re-confirms by exhaustion over all 8! labellings that min P = 14 for Q_3). For d = 9 it gives only U(Q_9) >= 2306, far below the organisers' 2368 quoted in
the statement; the bound is not expected to be sharp for large d.

Remark 2 (why d >= 3 is needed). Step 10 uses d >= 3 only through k = d - 1 >= 2. For d = 2, (**)
reads m = 1 and has a solution; indeed Q_2 (the 4-cycle) has labellings with P = |E| + 1 = 5
(out/code/sanity.py check D finds 16 of the 24). For d = 1, (**) reads 0 = 0.

Remark 3 (scope). The target explicitly excludes d = 1, 2; nothing is claimed there.
