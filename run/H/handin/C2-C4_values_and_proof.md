# Uphill paths on the hypercube: C2, C3, C4 hand-in (values + lower-bound proof)

STATUS (head, run time 0:52): GATED VALID — two clean-room referees (H-C4-002, H-C4-003) ACCEPTed this proof, including the d = 5, 6 instances. Values PROVED.
The proof text below is copied verbatim from worker artefact run/tasks/H-C4-001/out/claims.md
(sections A, C, B, D); only this header and the per-cell summary are the head's.

## Values (portal format)
- C2: `88`   (labelling Q5.txt, checker VERIFIED 88)
- C3: `204`  (labelling Q6.txt, checker VERIFIED 204)
- C4: `464, 1040`  (labellings Q7.txt VERIFIED 464, Q8.txt VERIFIED 1040)
(C1, already submitted: 14, 34.)

## Per-cell use of the proof
- Upper bounds: the labelling files (line i = vertex with label i), counted by the checker.
- Lower bounds: Lemma A with F_5 = 18 (section B) and Lemma C (F_d <= 2F_{d-1}):
  d=5: 2^5 + 4(32-18) = 88; d=6: F_6 <= 36, 2^6 + 5(64-36) = 204;
  d=7: F_7 <= 72, 128 + 6*56 = 464; d=8: F_8 <= 144, 256 + 7*112 = 1040.
  Worker's own statement of the d <= 6 instances: | C10. (by-product, same argument, outside the target) U(Q_d) = 5, 14, 34, 88, 204 for d = 2..6 | upper CHECKED (runlog R0-2..R0-6, checker VERIFIED 5/14/34/88/204); lower PROVED from Lemma A with F_2 = 3, F_3 = 5, F_4 = 10, F_5 = 18 (lb_forest.py, exhaustive) and F_6 <= 2 F_5 = 36 (Lemma C) | runlog R0, LB1 |

## Computation (section B), how to run
`python3 lb_forest.py` (stdlib only, exact; re-run by the head: 0.44 s, output F_4 = 10, F_5 = 18, no forest of
size 19 or 20). Independent cross-check `crosscheck_F5_sat.py` (needs python-sat): m=19 UNSAT, m=18 SAT, 0.28 s.
Code: run/tasks/H-C4-001/out/code/.

## Proof (verbatim from H-C4-001)

Notation. Q_d, labelling f, valley, uphill path exactly as in inbox/statement.md. n = 2^d,
E = d 2^{d-1}. For a vertex v: down(v) = #neighbours w with f(w) < f(v), up(v) = d - down(v).
N(v) = number of uphill paths whose last vertex is v. F_d = maximum number of vertices of a set
T ⊆ V(Q_d) whose induced subgraph Q_d[T] has no cycle (an "induced forest").

## A. Lemma A (lower bound in terms of induced forests)

Let d >= 1 and f any labelling of Q_d. Let S = {v : down(v) >= 2}, T = V \ S = {v : down(v) <= 1}.
Claim: (i) Q_d[T] has no cycle, so |T| <= F_d; (ii) #uphill paths = sum_v N(v) >= 2^d + (d-1)|S|.
Hence #uphill >= 2^d + (d-1)(2^d - F_d), and U(Q_d) >= 2^d + (d-1)(2^d - F_d).

Step A1 (valleys). Q_d with d >= 1 has no isolated vertex. v is a valley iff every neighbour has a
larger label iff down(v) = 0. So the valleys are exactly the vertices with down = 0; all lie in T.
Let V0 = number of valleys.

Step A2 (recurrence). For every v: N(v) = [v is a valley] + sum_{w ~ v, f(w) < f(v)} N(w).
Proof: an uphill path ending at v has k = 1 or k >= 2. With k = 1 it is (v), which is an uphill
path iff v is a valley. With k >= 2, deleting the last vertex v leaves (v_1..v_{k-1}), an uphill
path (v_1 is a valley, consecutive vertices adjacent, labels increasing) ending at w = v_{k-1},
with w ~ v and f(w) < f(v). Conversely, appending v to an uphill path ending at such a w gives an
uphill path ending at v (adjacency and strict increase hold at the new step). These two maps are
mutually inverse, so the paths with k >= 2 ending at v are in bijection with the disjoint union over
lower neighbours w of the uphill paths ending at w.

Step A3 (N(v) >= 1 for all v, and N(v) >= down(v) when down(v) >= 1). Starting at v, repeatedly
move to some neighbour with a smaller label while one exists. Labels strictly decrease, so this
stops after at most n - 1 moves, at a vertex u with no neighbour of smaller label, i.e. (A1) a
valley. Reading the visited vertices backwards gives an uphill path from u to v. So N(v) >= 1 for
all v. If down(v) >= 1 then by A2, N(v) >= sum over the down(v) lower neighbours of N(w) >= down(v).

Step A4 (summation). Summing A2 over v and exchanging the order of summation (each pair (w, v)
with w ~ v, f(w) < f(v) is an edge, counted once, at its lower endpoint w):
   sum_v N(v) = V0 + sum_w N(w) up(w) = V0 + sum_w up(w) + sum_w (N(w) - 1) up(w)
             = V0 + E + sum_w (N(w) - 1) up(w),
since sum_w up(w) = E (every edge has exactly one lower endpoint; labels are distinct).

Step A5 (bounding the excess). For w in T: (N(w) - 1) up(w) >= 0 by A3. For w in S, k = down(w)
satisfies 2 <= k <= d, so by A3 N(w) - 1 >= k - 1 >= 1 and up(w) = d - k >= 0, hence
(N(w) - 1) up(w) >= (k - 1)(d - k) >= d - k. Therefore
   sum_v N(v) >= V0 + E + sum_{w in S} (d - down(w)) = V0 + E + d|S| - sum_{w in S} down(w).

Step A6 (counting down-degrees). sum_{all w} down(w) = E (each edge counted once, at its upper
endpoint). In T, down(w) is 0 for the V0 valleys (A1) and 1 for the other |T| - V0 vertices, so
sum_{w in T} down(w) = |T| - V0 and sum_{w in S} down(w) = E - |T| + V0. Substituting in A5:
   sum_v N(v) >= V0 + E + d|S| - E + |T| - V0 = d|S| + |T| = 2^d + (d - 1)|S|.
This is (ii).

Step A7 (T induces a forest). Suppose Q_d[T] contains a cycle C (a closed walk v_1..v_m v_1 with
m >= 3 distinct vertices, all in T, consecutive ones adjacent). Let v be the vertex of C with the
largest label. Its two neighbours on C are distinct (m >= 3), adjacent to v, and have smaller
labels, so down(v) >= 2, i.e. v in S, contradicting v in T. So Q_d[T] is acyclic and |T| <= F_d,
|S| >= 2^d - F_d. Combining with (ii): #uphill >= 2^d + (d-1)(2^d - F_d) (using d - 1 >= 0). ∎

Numerical sanity check (not part of the proof): code/lemmaA_sanity.py, 1580 seeded random/
semi-sorted labellings for d = 1..7, 0 violations of (i) or (ii); on Q7.txt and Q8.txt the bound
holds with equality (|S| = 56, 112).

## C. Lemma C (doubling)

For d >= 2, F_d <= 2 F_{d-1}. Proof: let T be an induced forest of Q_d with |T| = F_d. For
b in {0,1} let H_b = {x in {0,1}^d : x_d = b}. Two vertices of H_b are adjacent in Q_d iff they
differ in exactly one of the first d-1 coordinates, so the map x -> (x_1..x_{d-1}) is an isomorphism
from Q_d[H_b] onto Q_{d-1}. Q_d[T ∩ H_b] is an induced subgraph of Q_d[T]; any cycle in it would be
a cycle of Q_d[T], so it is acyclic, and its image is an induced forest of Q_{d-1}; hence
|T ∩ H_b| <= F_{d-1}. As H_0, H_1 partition V(Q_d), F_d = |T ∩ H_0| + |T ∩ H_1| <= 2 F_{d-1}. ∎
By induction, F_{5+j} <= 2^j F_5 for j >= 0.

## B. Computation: F_5 = 18 (exhaustive; code/lb_forest.py, stdlib only, exact)

Class searched: ALL 2^16 subsets of V(Q_4) (so F_4 = 10 is exhaustive over all vertex subsets of
Q_4), then ALL ordered pairs (T0, T1) of induced forests of Q_4 with |T0| + |T1| = m, for m = 20, 19
(all pairs), and m = 18 (until the first acyclic pair).
Reduction (written soundness argument): let T be an induced forest of Q_5 with |T| = m. With H_0,
H_1 as in Lemma C (last coordinate), T0 := image of T ∩ H_0 and T1 := image of T ∩ H_1 under the
isomorphism of Lemma C are induced forests of Q_4 (proof of Lemma C), and |T0| + |T1| = m. The
vertex x + 16 b of Q_5 (x in 0..15 the first four coordinates as bits, b the last) is in T iff
x in T_b, so T is recovered as the set with bitmask T0 | (T1 << 16). The program enumerates every
induced forest of Q_4 (step 1 tests every subset), so every such pair (T0, T1) is examined. For each
pair it first applies a necessary condition (an acyclic graph on m vertices has at most m - 1 edges;
the edge count of Q_5[T] is e(T0) + e(T1) + |T0 ∩ T1|, the last term being the edges in direction 5
between x0 and x1 for x in T0 ∩ T1) and, if that passes, tests acyclicity of Q_5[T] directly by
union-find on the Q_5 adjacency (flip one of 5 bits). If no pair with sum m passes, Q_5 has no
induced forest with exactly m vertices. Since deleting a vertex from an induced forest leaves an
induced forest, "no induced forest with 19 vertices" implies none with >= 19. Output: m = 20 and
m = 19 rejected, an acyclic pair found at m = 18. So F_5 = 18 (and F_4 = 10).
Independent cross-check (different method, needs python-sat): code/crosscheck_F5_sat.py; CEGAR over
cycle clauses; m = 19 UNSAT (707 iterations, 786 cycle clauses), m = 18 SAT. Only lb_forest.py is
used in the headline.

## D. Conclusion of the lower halves

F_7 <= 4 F_5 = 72 and F_8 <= 8 F_5 = 144 (Lemma C + B). By Lemma A:
  U(Q_7) >= 2^7 + 6 (128 - 72) = 128 + 336 = 464;
  U(Q_8) >= 2^8 + 7 (256 - 144) = 256 + 784 = 1040.
Together with C1, C2: U(Q_7) = 464, U(Q_8) = 1040. (Equality in Lemma A for Q7.txt / Q8.txt: the
set S of the handed-in labellings has 56 / 112 vertices, is independent, and T = V \ S is an induced
forest; see lemmaA_sanity output.)
