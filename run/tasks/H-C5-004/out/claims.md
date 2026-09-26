# Claims: H-C5-004

| claim | status | where shown |
|---|---|---|
| out/Q9.txt (= out/best.txt) is a labelling of Q_9 with 2400 uphill paths (matches the known bound; earns nothing) | CHECKED (checker: VERIFIED 2400) | runlog run 19; built by code/build_labelling.py from the subject's parity forest (run 13) |
| No labelling with <= 2399 found | SEARCH-FOUND-NOTHING (not a lower bound) | runlog runs 3-18 |
| Smallest decycling set of Q_9 found: 236; nothing smaller in any run | SEARCH-FOUND-NOTHING below 236 | runlog runs 9, 11, 12, 16, 17 |
| A 236-set of the non-parity type (e(S)=13) gives at best 2406 with the builder's ordering | CHECKED (VERIFIED 2406 on tmp/lab_s101.txt) | runlog runs 9-10 |
| Parity-balanced forests (both classes >= 60) reached only |F| = 272 (|S| = 240) | SEARCH-FOUND-NOTHING better | runlog runs 14-16 |
| There is no induced forest F of Q_9 with |F| >= 277 that is invariant under g, for g any automorphism conjugate in Aut(Q_9) to: the 9-cycle of coordinates, a 7-cycle, or a 5-cycle of coordinates (no translation part). Also none with |F| >= 276 for the 9-cycle | SEARCH-FOUND-NOTHING in these classes (SAT answered UNSAT; exhaustive over the classes given the encoding, but NO DRAT certificate was produced, so this is not a verification) | runlog runs 3-4; code/sym_forest_sat.py; argument A1 below |
| For the classes "three 3-cycles", "two 3-cycles", and forests of the form (O\Z) u M with 3 <= |Z| <= 8: undecided | TIMED OUT | runlog runs 4, 5, 18 |
| Q_9 = Q_8 x K_2 with half 0 = odd words plus 16 even words at pairwise distance >= 4, half 1 = even words plus 16 odd words at pairwise distance >= 4: every induced forest inside this union has |F| <= 272 | PROVED (argument A2) | below |

## A1. Why a result for one generator covers its conjugacy class, and why the orbit encoding is complete
1. Every map g(x) = P_pi(x) XOR t (P_pi permutes coordinates, t a fixed vector) is an automorphism of Q_9:
   if x and y differ exactly in coordinate i, then P_pi(x) and P_pi(y) differ exactly in coordinate pi(i), and
   XOR with t does not change which coordinates differ.
2. Let sigma be an automorphism, h = sigma g sigma^{-1}. For a vertex set F: h(F) = F iff
   g(sigma^{-1}(F)) = sigma^{-1}(F) (apply sigma^{-1} to both sides of h(F) = F). sigma^{-1} maps induced
   subgraphs isomorphically onto induced subgraphs, so sigma^{-1}(F) is an induced forest iff F is, and it has
   the same size. So "no g-invariant induced forest of size >= K" implies "no h-invariant one".
3. F is g-invariant iff F is a union of orbits of <g>: if F is invariant it contains with x all of
   x, g(x), g^2(x), ...; conversely a union of orbits is mapped to itself. So one boolean per orbit describes
   exactly the invariant sets, and |F| = sum of |orbit| over chosen orbits (the totalizer is fed each orbit
   literal |orbit| times; tested exhaustively on a small instance with repeated literals before use).
4. Each clause added says "not all orbits met by this cycle of Q_9 are chosen". If they all were, every vertex
   of that cycle would be in F and F would contain the cycle. So every clause holds for every g-invariant
   induced forest; UNSAT of the final clause set means none of size >= K exists. SAT answers are re-checked by
   a union-find acyclicity test on the full vertex set.
5. Caveat: the UNSAT answers come from cadical153 via python-sat, with no DRAT proof; they are search results,
   not certified verifications.

## A2. Q_8 x K_2 with perfect-code halves
Write Q_9 = Q_8 x {0,1}. Take F = (O_8 u M1) x {0}  u  (E_8 u M2) x {1}, with M1 a set of 16 even words of
Q_8 at pairwise distance >= 4 and M2 a set of 16 odd words at pairwise distance >= 4. In Q_8 the 16 balls
N(m), m in M1, are pairwise disjoint (a common neighbour would put two words at distance <= 2) and have 8
elements each, so they partition the 128 odd words; likewise N(m), m in M2, partition the even words.
Each half induces 16 disjoint stars (144 vertices, 128 edges). The matching edges between the halves are at
the words in both sets, i.e. at M1 u M2 (32 edges). So G[F] has 288 vertices and 128+128+32 = 288 edges;
its cycle rank equals its number c of components, and at least one vertex per component with a cycle has to
be deleted. Now take m2 in M2 (odd). It lies in exactly one ball N(m1), m1 in M1, so d(m1, m2) = 1; m1 (even)
lies in exactly one ball N(m'), m' in M2, and since m2 is such a word, m' = m2. So the pairs {m1, m2} with
d(m1, m2) = 1 pair M1 with M2 perfectly, and each pair gives the 4-cycle
(m1,0) - (m2,0) - (m2,1) - (m1,1) - (m1,0) (edges: m2 is a leaf of m1's star in half 0; matching at m2; m1
is a leaf of m2's star in half 1; matching at m1). These 16 4-cycles are vertex-disjoint, so at least 16
vertices must be deleted: |F'| <= 288 - 16 = 272 for every induced forest F' inside such an F.
