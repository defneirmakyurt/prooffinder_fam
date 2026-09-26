# Claims: H-C1-003

| claim | status | where shown |
|---|---|---|
| The provided checker agrees with hand computation on Q_2 (identity order, 5), Q_2 (00,01,11,10, 5) and Q_3 (identity order, 16) | CHECKED | runlog.md run 1; hand computation in runlog.md |
| For any labelling, N(v) = [v is a valley] + sum over neighbours w with f(w)<f(v) of N(w), and the score is sum_v N(v) | PROVED | claims.md "Recurrence" below; cross-checked against explicit DFS enumeration of all uphill paths (run 8) |
| U(Q_3) <= 14, attained by out/Q3.txt | CHECKED | `verify.py out/Q3.txt --d 3` -> `VERIFIED 14` (run 9) |
| U(Q_3) >= 14, i.e. every one of the 8! = 40320 labellings of Q_3 has >= 14 uphill paths | CHECKED (exhaustive over ALL 8! labellings, no symmetry reduction) | out/code/brute_q3.py, run 2 |
| U(Q_3) = 14 | CHECKED | the two lines above |
| U(Q_4) <= 34, attained by out/Q4.txt | CHECKED | `verify.py out/Q4.txt --d 4` -> `VERIFIED 34` (run 9) |
| U(Q_4) >= 34, i.e. no labelling of Q_4 has <= 33 uphill paths | CHECKED (exhaustive over ALL 16! labellings, no symmetry reduction, via two independent exact searches) | out/code/dp_lower.py run 6 (`4 33 --no-fix`) and out/code/bb_lower.py run 7 (`4 33 --no-fix`) |
| U(Q_4) = 34 | CHECKED | the two lines above |
| U(Q_2) = 5 (sanity only, not part of the target) | CHECKED | out/code/bb_lower.py at T=4 (none) and T=5 (found), run 5 |
| Running dp_lower.py at d=4, T=33 with LB pruning entirely disabled also finds nothing | GAP | TIMED OUT after 10 min (run 4); not established |

## Recurrence (R2), written out

Fix a labelling f of a graph G. For a vertex v let N(v) be the number of uphill paths whose
last vertex is v. The uphill paths are partitioned by their last vertex, so the score is
sum_v N(v).

An uphill path ending at v with k = 1 is exactly the one-term sequence (v), and it is an uphill
path iff v is a valley; so there are [v is a valley] of them. An uphill path
(v_1,...,v_k) with k >= 2 and v_k = v has v_{k-1} a neighbour w of v with f(w) < f(v), and
(v_1,...,v_{k-1}) is again an uphill path (same valley start, same adjacency, same strict
increase), ending at w. Conversely, appending v to an uphill path ending at any neighbour w
with f(w) < f(v) gives an uphill path ending at v. This is a bijection, so

    N(v) = [v is a valley] + sum over {w ~ v : f(w) < f(v)} of N(w).

All terms on the right have smaller label, so processing vertices in increasing label order
computes every N(v) with exact integer arithmetic. This is the checker's rule and mine.

Two consequences used below, for every vertex x:
  (i) N(x) >= 1. Induction on f(x): if x is a valley N(x) = 1; otherwise x has a neighbour w
      with f(w) < f(x), and N(x) >= N(w) >= 1 by induction (all N-values are >= 0).
  (ii) N(x) >= sum over any subset of lower neighbours of N, since all N-values are >= 0.

## Lower-bound function LB(S, N) (R6), written out

Both searches build a labelling by choosing the vertices in increasing label order. After k
steps the placed set is S (these carry labels 1..k) and N(w) is known and final for every
w in S: by the recurrence N(w) only uses neighbours with smaller label, all of which are in S.

Let v be unplaced, and put A(v) = sum over {w in S : w ~ v} of N(w). Every w in S gets a
smaller label than v, so all of these w are lower neighbours of v, and by (ii) N(v) >= A(v).
By (i), N(v) >= 1. Hence N(v) >= max(1, A(v)) for every unplaced v, whatever the completion.

Now sum the recurrence over the unplaced vertices. For unplaced v, its lower neighbours split
into the ones in S (total contribution A(v)) and the unplaced ones with smaller label:

    sum_{v unplaced} N(v)
      = sum_{v unplaced} [v valley] + sum_{v unplaced} A(v)
        + sum_{v unplaced} sum_{u unplaced, u ~ v, f(u) < f(v)} N(u).

In the last double sum each edge {u,v} with both endpoints unplaced occurs exactly once,
contributing N of whichever endpoint has the smaller label (the labels are distinct, so
exactly one of the two orders holds). That endpoint is u or v, and N of it is >= max(1,A(u))
or >= max(1,A(v)) respectively, hence >= min( max(1,A(u)), max(1,A(v)) ) in either case.
Dropping the valley term (>= 0) gives, for EVERY completion of the partial labelling,

    sum_{v unplaced} N(v)  >=  LB(S,N) := sum_{v unplaced} A(v)
                               + sum_{edges {u,v} with u,v both unplaced} min(max(1,A(u)), max(1,A(v))).

Since the final score is (running total over S) + sum_{v unplaced} N(v), a partial labelling
with running_total + LB(S,N) > T cannot be completed to a labelling of score <= T. Discarding
it is therefore sound: no labelling of score <= T is lost.

## State merging in dp_lower.py (R7), written out

Call a placed vertex a boundary vertex if it has at least one unplaced neighbour. Claim: the
set of achievable values of sum_{v unplaced} N(v) depends on the partial labelling only through
(S, N restricted to the boundary of S).

Indeed, fix S and a completion, i.e. a linear order of the unplaced vertices. Compute the N of
the unplaced vertices in that order by the recurrence. Each such N(v) is
[v has no lower neighbour] + sum over lower neighbours w of N(w); a lower neighbour w is either
unplaced (then N(w) was already computed inside this completion) or lies in S, and in that case
w has the unplaced neighbour v, so w is a boundary vertex. The same holds for the valley test:
v is a valley iff it has no neighbour in S and no earlier unplaced neighbour, and "has a
neighbour in S" is decided by S alone. So the whole computation reads only S, the completion
order, and N on the boundary of S. Two partial labellings with the same (S, N|boundary)
therefore admit exactly the same multiset of future costs.

Consequently, among all partial labellings with the same (S, N|boundary), only the one with the
smallest running total can matter for "is there a completion with total <= T": if a larger-total
one completes to <= T, so does the smallest-total one. dp_lower.py keeps exactly that minimum,
so the merge is lossless for the decision question and for the minimum.

Because this merging is the only non-obvious ingredient of dp_lower.py, out/code/bb_lower.py
repeats the d=4, T=33 search as a plain depth-first branch and bound with NO merging at all
(and no symmetry fix). It also reports "none", so the Q_4 lower bound does not rest on the
merging argument.

## Symmetry (R3), written out, and why it is not needed

For u in {0,1}^d the map sigma_u(v) = v XOR u is a bijection of {0,1}^d, and v XOR w =
sigma_u(v) XOR sigma_u(w), so v and w differ in exactly one coordinate iff sigma_u(v) and
sigma_u(w) do: sigma_u is an automorphism of Q_d. Given a labelling f with f(u) = 1, the
labelling g = f o sigma_u satisfies g(0...0) = f(u) = 1, and (v_1,...,v_k) is an uphill path
for g iff (sigma_u(v_1),...,sigma_u(v_k)) is one for f, so g and f have equally many uphill
paths. Hence min over labellings with label 1 at 0...0 equals min over all labellings.

This reduction is implemented (default) but the reported Q_4 lower-bound runs use --no-fix,
i.e. all 16 choices of the vertex with label 1, so the claim does not depend on it.
