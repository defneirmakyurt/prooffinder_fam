# U(Q_5) = 88: argument (both halves)

Notation. Q_5: vertex set {0,1}^5 (encoded as integers 0..31 via binary), v ~ w iff they differ in
exactly one coordinate; n = 32, every vertex has degree 5, E = 80 edges. A labelling f is a bijection
V -> {1..32}. For a labelling, N(v) := number of uphill paths ending at v (last vertex v_k = v),
T(f) := total number of uphill paths = sum_v N(v) (every uphill path has exactly one last vertex).
up(v) := #{w ~ v : f(w) > f(v)}, low(v) := #{w ~ v : f(w) < f(v)}; up(v) + low(v) = 5.

## Upper half: T = 88 is attained
out/Q5.txt (and the different labelling out/Q5_alt1.txt) are scored by the provided checker
inbox/checker/verify.py: `VERIFIED 88` for both. Nothing else is claimed for this half.

## Lower half: every labelling of Q_5 has T >= 88

**Lemma 1 (recursion).** N(v) = [v is a valley] + sum over w ~ v with f(w) < f(v) of N(w).
Proof. Split the uphill paths ending at v by length k. k = 1: the only sequence is (v); by definition it
is an uphill path iff v is a valley; this gives the term [v is a valley]. k >= 2: the path is
(v_1,...,v_{k-1}, v) and w := v_{k-1} is a neighbour of v with f(w) < f(v); the prefix (v_1..v_{k-1})
starts at the valley v_1, has consecutive vertices adjacent and strictly increasing labels, so it is an
uphill path ending at w. Conversely, for any neighbour w of v with f(w) < f(v) and any uphill path P
ending at w, appending v gives a sequence starting at a valley, with consecutive vertices adjacent and
labels strictly increasing (the last step since f(w) < f(v)), i.e. an uphill path ending at v of length
>= 2. These two maps are mutually inverse, so the k >= 2 paths ending at v are counted by
sum_{w ~ v, f(w) < f(v)} N(w). QED

**Lemma 2 (N >= 1).** N(v) >= 1 for every v. Proof by induction on f(v). If v is a valley, N(v) >= 1 by
Lemma 1. Otherwise some neighbour w has f(w) < f(v) (not a valley means some neighbour has smaller or equal
label, and labels are distinct so smaller), and by induction N(w) >= 1, so N(v) >= N(w) >= 1 by Lemma 1
(all terms are nonnegative). The base case f(v) = 1: v has no neighbour with smaller label, so it is a
valley. QED

**Lemma 3 (excess identity).** Let V be the number of valleys. Then
T = E + X, where X := sum_v cost(v),  cost(v) := [v valley] + (N(v) - 1) * up(v)  (>= 0 by Lemma 2).
Proof. Sum Lemma 1 over v: T = V + sum over ordered pairs (w, v) with w ~ v and f(w) < f(v) of N(w).
Group the pairs by w: for fixed w the number of such v is up(w). So T = V + sum_w N(w) up(w)
= V + sum_w up(w) + sum_w (N(w) - 1) up(w). Each edge {w, v} has exactly one endpoint with the smaller
label (labels are distinct), so sum_w up(w) = E. QED

So U(Q_5) >= 88 is equivalent to: X >= 8 for every labelling of Q_5.

**Sequential form.** Let v_i := f^{-1}(i), S_i := {v_1..v_i}. For w = v_{i+1}:
its lower neighbours are exactly its neighbours in S_i; w is a valley iff it has no neighbour in S_i;
up(w) = number of neighbours outside S_i (w is not its own neighbour); N(w) = [valley] + sum of N(u) over
neighbours u in S_i. Hence cost(v_{i+1}) is determined by S_i, the N-values of neighbours of w in S_i,
and w.

**State.** sigma_i : V -> {0,...,15}, sigma_i(v) = 0 if v not in S_i; = 15 if v in S_i and all its
neighbours are in S_i; = N(v) otherwise ("boundary" vertex).
(a) (sigma_{i+1}, cost(v_{i+1})) is a function of (sigma_i, v_{i+1}): S_i = {v : sigma_i(v) != 0}; each
neighbour u of w = v_{i+1} lying in S_i has the unplaced neighbour w, so it is a boundary vertex and
sigma_i(u) = N(u) (never 15); this gives valley status, N(w), up(w), cost(w). The new state: w gets 15 if
all its neighbours are in S_i, else N(w); each neighbour u of w in S_i gets 15 if all neighbours of u are
now placed; every other vertex keeps its code (its set of placed neighbours did not change).
(b) Hence X(f) = sum of step costs along the walk sigma_0 -> sigma_1 -> ... -> sigma_32 driven by the
order, and every order is a legal walk. Define rem(sigma) := min, over all ways to place the remaining
vertices one at a time, of the sum of the remaining step costs; by (a) it depends only on sigma.
(c) 4-bit encoding. The program never stores a state whose accumulated cost exceeds LIMIT. A boundary
vertex v has up(v) >= 1 at its placement, so its own cost is >= N(v) - 1; thus a stored boundary value
satisfies N(v) <= LIMIT + 1 = 8 <= 14, distinct from 0 and 15. Nothing is truncated.

**Lemma 4 (non-valley with N >= 2 and up >= 1 costs >= 3 in Q_5).** Let x be a non-valley with
N(x) >= 2 and up(x) = r >= 1. Then low(x) = 5 - r >= 1 (non-valley), so r <= 4. By Lemma 1 and Lemma 2,
N(x) >= low(x) = 5 - r, and N(x) >= 2 by hypothesis, so cost(x) = (N(x)-1) r >= (max(2, 5-r) - 1) r.
For r = 1, 2, 3, 4 this is 3, 4, 3, 4 respectively; the minimum is CB = 3. QED

**Heuristic h (used only in the HEUR=1 runs).** In state sigma, let F := unplaced w whose placed
neighbours have N-sum >= 2. In every completion each w in F is placed after those neighbours, so it is
not a valley and, by Lemma 1 and Lemma 2 (all other terms >= 0), N(w) >= that sum >= 2. Take any matching
M in the subgraph of Q_5 induced on F (the program builds a greedy one). For each edge {x,y} of M the
endpoint placed first, say x, has y unplaced at that moment, so up(x) >= 1 and cost(x) >= 3 by Lemma 4.
The chosen endpoints are distinct (edges of M are disjoint) and are all still unplaced, and all costs are
>= 0, so rem(sigma) >= 3|M| =: h(sigma).

**Symmetry (used only in the SYM=1 runs).** Aut contains the 3840 maps g(v) = pi(v) XOR a (pi a
permutation of the 5 coordinates, a in {0,1}^5); each is a bijection of V, and v ~ w iff g(v) ~ g(w)
(pi keeps the number of differing coordinates, XOR by a keeps it too).
(i) For any labelling f and any such g, f o g^{-1} has the same T: a sequence (v_1..v_k) is an uphill path
for f iff (g v_1..g v_k) is an uphill path for f o g^{-1}, because adjacency is preserved, labels are
equal ((f o g^{-1})(g v) = f(v)), and v is a valley for f iff g v is a valley for f o g^{-1} (its neighbours
map bijectively onto the neighbours of g v, with equal labels). This map of sequences is a bijection.
(ii) Define (g.sigma)(g v) := sigma(v). The rule in (a) uses only adjacency and codes, so if placing w in
sigma gives sigma' with step cost c, then placing g w in g.sigma gives g.sigma' with the same cost c.
Applying this step by step, the completions of sigma and of g.sigma correspond bijectively with equal
costs, so rem(g.sigma) = rem(sigma).
Translations alone (pi = identity) are used in every run: with a := f^{-1}(1), g(v) = v XOR a maps the
label-1 vertex to 0, so by (i) min X over all labellings = min X over labellings with f(0) = 1 = 1 + rem of
the state "vertex 0 placed, N = 1" (vertex 0 is then a valley: cost 1). This is the program's layer 1.
In SYM=1 runs, each new state is replaced before storage by the element of its orbit that is smallest
in a fixed total order (first the 32-bit placed mask as an unsigned integer, then the code vector
lexicographically); a minimum over the whole orbit is the same for all members of the orbit. By (ii)
this replacement does not change rem.

**Correctness of the layered DP (the decision "is min X <= LIMIT?").** Layer i holds states with |S| = i,
each with a recorded cost that is the step-cost total of some actual placement sequence reaching that
state (or, with SYM=1, reaching a state in its orbit). A child sigma' of a state with recorded cost c and
step cost s is discarded iff c + s > LIMIT or (HEUR=1 and) c + s + h(sigma') > LIMIT.
Let X* be the minimum of X over labellings and suppose X* <= LIMIT.
Invariant: every layer i contains a state tau with recorded cost c(tau) + rem(tau) <= X*.
- i = 1: the single state has c = 1 and 1 + rem = X* (translation argument above).
- i -> i+1: take tau as in the invariant and an optimal completion of tau; its first step places some w,
  giving sigma' with step cost s and s + rem(sigma') = rem(tau). Then c(tau) + s + rem(sigma') <= X* <=
  LIMIT, and h(sigma') <= rem(sigma') (Lemma 4 argument), so sigma' is not discarded; it (or its orbit
  representative, same rem) is stored with recorded cost <= c(tau) + s (the table keeps the minimum).
So if some layer i <= 32 is empty, then X* > LIMIT. The program, run with LIMIT = 7, reports an empty
layer in every Q_5 run (layer 27 with the heuristic, layer 30 without; runlog.md), hence X >= 8 for
every labelling, i.e. T >= 88.

## Conclusion
Every labelling of Q_5 has at least 88 uphill paths, and out/Q5.txt has exactly 88 (checker).
Hence U(Q_5) = 88. The lower bound is a computer-assisted proof; it is exhaustive over all 32!
labellings of Q_5 through the reduction above (no parameter other than d = 5 is covered).
Two completed runs of the final code each give "layer empty" for LIMIT = 7 and their extra assumptions
are disjoint: `./lbdp 5 7 0 1` (translations + heuristic h; 2m40s, 18,696,829 states) and
`./lbdp 5 7 1 0` (full orbit merging, no heuristic; 1m16s, 1,567,313 states). See runlog.md.
