# Sub-problems for H-C5 (second analyst pass; builds on inbox/earlier/H-C5-006/subproblems.md, which is not repeated)

Reduction (H-C5-002 Steps 1-8, under review): 512 + 8 nabla(Q_9) <= U(Q_9) <= 2400 = 512 + 8*236.
Identity for Q_9 (every decycling set S, F = V - S, c = #components of Q_9[F], e(S) = #edges of Q_9[S]):
8|S| = 1792 + c + e(S). So |S| = 235 <=> c + e(S) = 88; |S| = 233 <=> c + e(S) = 72; |S| = 236 <=> 96
(out/code/bounds_table.py). Labels: (a) known and citable, (b) known but hard to access, reproduce, (c) unknown.

## Changes to the H-C5-006 table
| id | statement | label (old -> new) | status / where |
|---|---|---|---|
| S2' | A(9,4) <= 28 (packing for even codes) and "max codes can be taken even" | (a)/(b) -> reproduced | out/proof.md P1, P2 (Pike 2003 Lemma 1 opened; packing bound attributed to Pike by Wodlinger) |
| S2 | A(9,4) = 20 | (a) cited, unchanged | not reproduced (plain Delsarte LP gives 25, H-C5-006) |
| U1 | nabla(Q_9) <= 236 | (a); now read in the primary source: Pike 2003 Theorem 1 (p.548, opened) with A(9,4) = 20; Pike's Cor. 1 alone gives 240 | PROVED (and reproduced constructively in H-C5-002 and in out/code/lns_sat.py's start forest) |
| L2 | nabla(Q_9) >= 226 (Pike's kappa + eps >= n + 1) | (b), still not reproduced; discrepancy with Hertz (225) now explained with high probability: Hertz's L column coincides for n = 9..13 with the older bound of [1] (Bau et al.), which Pike p.547 quotes as the bound he improves | UNSURE-attribution; irrelevant to the cell |
| U5 | a decycling set of Q_9 with <= 235 vertices (necessarily with an edge inside) | (c) OPEN; literature pass 2 found no construction for any n of a non-independent set beating 2^{n-1} - A(n,4) | new necessary conditions for a MINIMUM such set: every vertex has <= 7 S-neighbours and closes a cycle (out/proof.md P3); moves between equal-size sets: seed shuffle (P4) |
| U5-LNS | no 277-forest agrees with the standard 276-forest (odd vertices + a 20-word even code) outside any Hamming ball of radius 2 (all 512 centres), resp. radius 3 (centres covered as in RAN) | (c) new search data | COMPUTER-VERIFIED for that single start forest (code public: y, out/code/lns_sat.py); proves nothing about nabla(Q_9) |
| L4 | nabla(Q_9) >= 233 (equivalently c + e(S) >= 72 for every induced forest) | (c) OPEN | no source; see why_not.md |
| X1 | Exact solution of max induced forest of Q_9 by generic ILP | (c) | Melo-Ribeiro 2021 Table 8: branch-and-cut on weighted Q_8/Q_9 not closed in 1 h (gaps 2-6 %); a generic ILP/SAT without heavy symmetry breaking is not expected to prove L4 within the 10-minute rule |
