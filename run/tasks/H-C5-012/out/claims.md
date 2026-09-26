# Claims: H-C5-012 (Phase 3, analyst, second pass). The cell is NOT solved.

| claim | status | where proved / source |
|---|---|---|
| Pike 2003 pp. 547-548 contain: Lemma 1 (max (n,4) codes can be taken even), Lemma 2 (even vertices minus an even (n,4) code = decycling set; by reference to Focardi et al.), Theorem 1 (nabla(Q_n) <= 2^{n-1} - A(n,4)), Corollary 1 (n = 2^r - x: nabla <= 2^{n-1} - 2^{n-r-1}; for n = 9 this is 240) | PROVED in the source (opened) | sources.md row 1; out/tmp/pageone.txt |
| Pike pp. 549-550 (lower bound, iff theorem, A(n,4) <= 2^{n-1}/n, "at least n edges") could not be accessed; their content is known only via Wodlinger 2018 Sect. 2.3.3 | UNSURE (secondary only) | sources.md rows 2-3 |
| Hertz 2021 Table 4's L(Q_n) column (225, 456, 922, 1862, 3755 for n = 9..13) equals the ceiling of the pre-Pike bound 2^{n-1} - (2^{n-1}-1)/(n-1) at all five n, and is 1 below Wodlinger's statement of Pike's bound (226, 457, 923, 1863, 3756) | arithmetic COMPUTER-VERIFIED (exact rationals; code public: y); interpretation "Hertz mislabelled [1]'s bound as Pike's" UNSURE | out/code/bounds_table.py |
| Hertz's text formula U(Q_n) = 2^{n-1} - 2^{n-r-1} (Pike Cor. 1) gives 240 for n = 9, but his Table 4 lists 236 (= 2^8 - A(9,4)); the table, not the text formula, is the best bound | PROVED (arithmetic) | sources.md (Hertz row) |
| P1: every (d,4) code can be made even-weight without losing words | PROVED (own write-up of Pike Lemma 1) | proof.md P1 |
| P2: even (d,4) codes have <= 2^{d-1}/d words; A(9,4) <= 28 | PROVED | proof.md P2 |
| P3: every vertex x of a minimum decycling set S has two F-neighbours in one component of G[F]; for d-regular G, deg_S(x) <= d-2 (Q_9: <= 7) | PROVED (write-up of Francis-Mynhardt-Wodlinger 2019, p.293) | proof.md P3 |
| P4: seed shuffle preserves decycling and size | PROVED (write-up of Francis-Mynhardt-Wodlinger Lemma 3.1) | proof.md P4 |
| No source found (any n) with a non-independent minimum decycling set of Q_n, or with nabla(Q_n) < 2^{n-1} - A(n,4); none with a bound on nabla(Q_9) newer than Hertz 2021; no SAT/ILP determination of the forest number of Q_9 | not found in the sources listed in sources.md ("Not found") | sources.md |
| Exact ILP branch-and-cut on vertex-weighted Q_8, Q_9 (Melo-Ribeiro 2021) did not close any instance in 1 h (gaps 2-6 %) | COMPUTER-VERIFIED by the authors (code public: UNSURE) | sources.md, arXiv 2102.09194 Table 8 |
| With F0 = odd vertices u C (C an even (9,4) code of size 20 found by SAT; |F0| = 276, forest checked), for EVERY centre v of Q_9 there is no induced forest of size >= 277 that agrees with F0 outside the Hamming ball B(v,2) | COMPUTER-VERIFIED (code public: y; exact SAT, UNSAT for all 512 balls) | out/code/lns_sat.py, RAN below |
| Same for radius-3 balls (130 free vertices): UNSAT for all 512 centres | COMPUTER-VERIFIED (code public: y) | out/code/lns_sat.py, out/tmp/lns_R3.log |
| Radius-4 balls (256 free vertices): UNSAT for centres 315, 401, 455, 373, 344 (vertex v encoded as the integer with bit i = coordinate i; centre order = random.shuffle with seed 1); 8 further centres TIMED OUT at 20 s each; the other 499 centres not tried | PARTIAL (COMPUTER-VERIFIED for the 5 UNSAT centres only) | out/tmp/lns_R4.log |
| These LNS results say only that this particular 236-set is not improvable by changing <= 46 (resp. <= 130) vertices inside one ball; they say nothing about nabla(Q_9) | - | - |

## RAN (wall clock measured with `date +%s.%N`; /usr/bin/time is not installed in this sandbox)
* python3 out/code/bounds_table.py (n = 5..13) -- COMPLETED, 0.07 s.
* .venv python3 out/code/lns_sat.py 2 20 10 1 (first version, lazy cycle cuts only; R = 2, 20 random centres) -- COMPLETED, all UNSAT, 0.40 s.
* .venv python3 out/code/lns_sat.py 3 512 20 1 (first version; R = 3) -- TIMED OUT at the 300 s shell limit, no summary printed (progress output not yet added); no result used.
* .venv python3 out/code/lns_sat.py 3 512 30 1 (first version with progress) -- killed by me after the first centre (TIMEOUT at 33 s, 447 CEGAR iterations); superseded.
* .venv python3 out/code/lns_sat.py 2 512 10 1 (final version: all 4- and 6-cycles pre-added + multi-cut CEGAR; R = 2, all 512 centres) -- COMPLETED, 512/512 UNSAT, 27.9 s.
* .venv python3 out/code/lns_sat.py 3 512 15 1 (final version; R = 3, all 512 centres, 15 s per ball) -- COMPLETED, 512/512 UNSAT, 99.3 s.
* .venv python3 out/code/lns_sat.py 4 512 20 1 (final version; R = 4, 20 s per ball, 330 s shell cap) -- TIMED OUT at 330 s: 13 centres done (5 UNSAT, 8 TIMEOUT, 0 FOUND), 499 not reached; 330.0 s.
* Note: the pre-added short cycles are all 4-cycles plus 12 of the 16 6-cycles of each Q_3 subcube (69,120 clauses); the remaining cycles are added lazily. Every added clause excludes a genuine cycle, so UNSAT answers are sound.
