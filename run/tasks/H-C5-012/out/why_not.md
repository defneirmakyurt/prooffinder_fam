# Why H-C5 is not solved here (H-C5-012, second analyst pass)

The obstruction is unchanged from inbox/earlier/H-C5-006/why_not.md (credited; not repeated): both routes of
the cell reduce to the decycling number nabla(Q_9), via 512 + 8 nabla(Q_9) <= U(Q_9) <= 2400.
* UPPER (<= 2399) needs a decycling set of size <= 235. Because of Pike's characterisation (H-C5-006 Lemma I,
  using A(9,4) = 20), such a set must contain an edge.
* LOWER (>= 2369) needs, e.g., nabla(Q_9) >= 233. The best published bound is 225 or 226.

## What this pass adds to the obstruction analysis
1. Primary source. Pike 2003 pp. 547-548 (now opened) prove the upper bound only through independent sets
   (Theorem 1, via codes). The two pages seen contain no non-independent construction and nothing specific to
   n = 9. Pages 549-550 remain unseen.
2. No such example is known for any n. No source gives a hypercube Q_n with a non-independent minimum decycling
   set, or with nabla(Q_n) < 2^{n-1} - A(n,4). For n <= 8 the exact values equal the code bound. For 9 <= n <= 13
   the best known upper bounds equal the code bound (Hertz Table 4, found by a search that is limited to
   independent sets). So there is no known pattern to transfer to n = 9.
3. Why the easy "doubling" route to UPPER fails (it is covered by Lemma I). Split Q_9 into two Q_8 halves. Take an
   optimal parity set in one half (even words minus the extended Hamming code H) and the opposite-parity set in
   the other half. The result is a set of Q_9 vertices that all have the same parity, so it is independent, and
   Lemma I puts it at >= 236. With S0 = even_8 minus H fixed in one half, every odd word of Q_8 is at distance 1
   from H. So no odd word can be added as a star centre in the other half, and the best independent completion
   has size 240 (proof: proof.md P5). The 236-sets split unevenly across the halves, with both halves non-optimal.
4. Local exact search fails around the standard 236-set. Take F0 = (odd vertices) u (a 20-word even code). For
   every Hamming ball of radius 2 or 3, re-optimising the ball exactly (SAT, all 4- and 6-cycles plus lazy
   cycle cuts) cannot give 277 vertices: all 512 balls UNSAT for R = 2 and R = 3. Radius 4 (half the cube) was
   run for the centres listed in claims.md. So an improvement, if one exists, is not a local modification of
   this 236-set. Either it changes > 130 vertices, or it starts from a different near-optimal structure.
   (Identity: going from 236 to 235 means reducing c + e(S) from 96 to 88. With e(S) >= 1, at least 9
   components must be merged.)
5. Generic exact optimisation is out of reach. Branch-and-cut ILP (Melo-Ribeiro 2021, Table 8) does not close
   weighted Q_8 or Q_9 in 1 h (gaps 2-6 %). Without heavy symmetry reduction, a generic ILP or SAT proof of
   nabla(Q_9) >= 233 is not plausible under the 10-minute rule.
6. The known local structure is too weak. Francis-Mynhardt-Wodlinger (P3/P4) give only degree <= 7 inside a
   minimum S, plus seed shuffles. This neither excludes nor produces a 235-set.

## What the next person needs to start
* Read Pike 2003 pp. 549-550, which need library access (DOI 10.1007/s00373-003-0529-9, Zbl 1032.05071). Check
  three things: (i) the exact lower bound for n = 9 (226 expected); (ii) the proof that a minimum decycling set
  containing an edge contains >= n edges. If that holds for Q_9, a 235-set that is minimum has >= 9 internal
  edges and c <= 79; this is a strong constraint for UPPER searches. (iii) Whether Pike tabulates n = 9..13.
* UPPER: start searches from structures that are NOT the parity + code set. Examples: forests with few large
  trees (c small). Or decycling sets built from the Q_4 x Q_5 or Q_3^3 product structure. Or group-invariant
  forests for subgroups of Aut(Q_9) with <= ~40 orbits (exhaustive over orbit unions is then feasible).
  out/code/lns_sat.py already has a working exact neighbourhood re-optimiser (short-cycle clauses + CEGAR) that
  can take any start forest.
* LOWER: see H-C5-006 why_not.md item 3 (classify near-optimal Q_8 forests up to symmetry and glue them).
  Nothing in the literature does this.
