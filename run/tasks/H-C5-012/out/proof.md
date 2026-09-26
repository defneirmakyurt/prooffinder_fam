Statements proved here (partial; NOT the cell H-C5): (P1) every binary code of length d with minimum distance >= 4 can be turned into one of the same size with all words of even weight; (P2) an even-weight code of length d with minimum distance >= 4 has at most 2^{d-1}/d words, so A(9,4) <= 28; (P3) in a minimum decycling set S of a d-regular graph G, every vertex of S has at least two neighbours in F = V - S, and two of them lie in the same component of G[F]; in particular for Q_9 every vertex of a minimum decycling set has at most 7 neighbours in S; (P4) (seed shuffle) if x in S has exactly d-2 neighbours in S and v is one of its two F-neighbours, S - x + v is a decycling set of the same size. Neither route of H-C5 (U(Q_9) >= 2369, or a labelling with <= 2399 uphill paths) is achieved.

Definitions exactly as in inbox/statement.md; decycling set / nabla / A(d,4) as in inbox/earlier/H-C5-006/proof.md.

Credit. P1 is Pike 2003 Lemma 1 (p.548, opened; his proof is reproduced in my words with the parity step written
out). P2 is the bound attributed to Pike by Wodlinger (thesis (2.3)); Pike's own proof (p.549-550) was not seen;
the argument below is mine (standard sphere-packing). P3, P4 are from Francis-Mynhardt-Wodlinger 2019 (AJC 74,
p.293 statement "G[S] has maximum degree at most r-2" and Lemma 3.1, opened); proofs written out here.
Nothing here is claimed new.

## P1 (even-weight maximum codes; Pike Lemma 1)
Let A be a code of length d >= 1 with minimum distance >= 4. Let A0, A1 be its words of even / odd weight.
Step 1. For words u, w: wt(u + w) = wt(u) + wt(w) - 2|supp(u) n supp(w)|, so d(u,w) = wt(u+w) has the parity of
wt(u) + wt(w). Hence for w0 in A0, w1 in A1, d(w0, w1) is odd; since it is >= 4, it is >= 5.
Step 2. Let A1' = {w + e_d : w in A1} (flip coordinate d). Words of A1' have even weight (weight changes by exactly 1).
Distances inside A1' equal distances inside A1 (translation by e_d is an isometry), so they are >= 4.
For w0 in A0, w1 in A1: d(w0, w1 + e_d) >= d(w0, w1) - 1 >= 4 (triangle inequality, d(w1, w1 + e_d) = 1).
Also w0 != w1 + e_d, because that distance is >= 4 > 0.
Step 3. So A0 u A1' is a code of |A0| + |A1| = |A| even-weight words with minimum distance >= 4. []

## P2 (packing bound for even codes)
Let A be an even-weight code of length d >= 1 with minimum distance >= 4, and N(a) the set of the d neighbours of a
in Q_d (all of odd weight). If a != b in A and N(a) n N(b) contains some x, then d(a,b) <= d(a,x) + d(x,b) = 2 < 4,
impossible. So the |A| sets N(a) are pairwise disjoint subsets of the 2^{d-1} odd-weight words, and d|A| <= 2^{d-1}.
For d = 9: |A| <= 256/9 < 29, so A(9,4) <= 28 (using P1 to pass from arbitrary codes to even ones). []
(This is far from A(9,4) = 20, which remains CITED; see inbox/earlier/H-C5-006/proof.md I8.)

## P3 (local structure of minimum decycling sets; Francis-Mynhardt-Wodlinger p.293)
Let G be finite, S a minimum decycling set, F = V - S, x in S.
Claim: x has two neighbours in F lying in the same component of G[F].
Proof. Suppose not. Then the F-neighbours of x lie in pairwise distinct components of the forest G[F]
(possibly there are 0 or 1 of them). Consider G[F u {x}]. Any cycle in it must use x (G[F] has none), so it has the
form x, y1, ..., yk, x with k >= 2, y1 != yk both F-neighbours of x, and y1 ... yk a path in G[F]. Then y1 and yk
are in the same component of G[F], contradicting the assumption. So G[F u {x}] is a forest and S - {x} is a
decycling set of size |S| - 1, contradicting minimality. []
Corollary. For d-regular G, deg_S(x) <= d - 2 for every x in a minimum decycling set S. For Q_9: <= 7.
Consequence for the UPPER search (H-C5-006 U5): if nabla(Q_9) <= 235, a minimum decycling set S (|S| = nabla) is
not independent (H-C5-006 I8, uses A(9,4) = 20), has every vertex with <= 7 S-neighbours, and each of its vertices
has two F-neighbours joined by a path in F (so every S-vertex "closes a cycle").

## P4 (seed shuffle; Francis-Mynhardt-Wodlinger Lemma 3.1)
G d-regular, S decycling, x in S with exactly d - 2 neighbours in S; its two F-neighbours are v, v'.
Let S' = S - {x} u {v}, F' = V - S' = (F - {v}) u {x}. In G[F'], x has exactly one neighbour (v' ; v is now in S'),
so x has degree <= 1 in G[F'] and lies on no cycle of G[F']. Every cycle of G[F'] avoiding x lies in G[F - {v}],
a subgraph of the forest G[F]. So G[F'] is a forest and |S'| = |S|. []
Use: P4 lets a search move between decycling sets of equal size; it does not change |S|.

## What is NOT done here
* Pike's lower bound kappa + eps >= n + 1 and "a minimum decycling set containing an edge contains >= n edges"
  (Wodlinger's outline of Pike pp. 549-550): not reproduced. Irrelevant for the cell thresholds (it gives 226).
* The organisers' 2368 (presumably nabla(Q_9) >= 232): not reproduced; no source found.
* nabla(Q_9) <= 235 (U5) and nabla(Q_9) >= 233 (L4): open in every source found.

## P5 (an optimal parity half forces 240 for independent sets; supports why_not.md item 3)
Write vertices of Q_9 as (p, t), p in {0,1}^8, t in {0,1}; H = extended Hamming [8,4,4] code (16 even words,
every odd word of length 8 at distance exactly 1 from exactly one word of H, since the 16 neighbourhoods of size 8
are disjoint by P2's argument and 16 * 8 = 128). Let S be an INDEPENDENT decycling set of Q_9 with
S n {t = 0} = S0 := {(p,0) : p even, p not in H}. Then |S| = 240.
Proof. By H-C5-006 Lemma I (I3-I6), every vertex of F = V - S has F-degree 0, 1 or 9, and |S| = 256 - |C| where
C = set of F-vertices of F-degree 9.
(i) Every (p,0) with p odd is in F: it has 8 neighbours (q,0), q even, and exactly one of them has q in H, so 7 are
in S0; if (p,0) were in S, S would contain an edge.
(ii) For h in H, (h,0) is in F and its 8 neighbours (p,0) (p odd) are in F by (i), so deg_F((h,0)) >= 8; as it must
be 0, 1 or 9, it is 9: (h,0) is in C and (h,1) is in F.
(iii) No other vertex is in C. A vertex (q,0), q even not in H, is in S. A vertex (p,0), p odd, has at most one
F-neighbour (h_p,0) among its 8 even-position neighbours in H0 (the other 7 are in S0), so its F-degree is <= 2 < 9.
A vertex (x,1) in C would be at distance >= 4 from every (h,0) in C (centres are at distance >= 4, Lemma I I7 /
star disjointness): d((x,1),(h,0)) = d(x,h) + 1, so d(x,h) >= 3 for all h in H. But every odd x is at distance 1
from H, and every even x is at distance <= 2 from H (x + e_1 is odd, at distance 1 from some h, so d(x,h) <= 2).
Contradiction. Hence C = {(h,0) : h in H}, |C| = 16, |S| = 240. []
