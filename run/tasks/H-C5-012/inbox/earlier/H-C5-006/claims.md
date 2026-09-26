# Claims: H-C5-006 (Phase 3, analyst). The cell is NOT solved.

| claim | status | where proved / source |
|---|---|---|
| Best published bounds: 225 <= nabla(Q_9) <= 236 (lower 225 per Hertz Table 4 "from Pike"; 226 if Wodlinger's statement of Pike's bound is right) | PROVED in the literature (cited; the 236 upper bound also reproduced constructively in H-C5-002, and the 225 lower bound re-proved there) | sources.md (Hertz 2021 Table 4, opened; Wodlinger 2018 Sect. 2.3.3, opened; Pike 2003 abstract only) |
| No source found gives nabla(Q_9) exactly, a decycling set of Q_9 of size <= 235, or nabla(Q_9) >= 227 | not found in the sources listed in sources.md ("Not found") | sources.md |
| Lemma I: for d >= 2, every independent decycling set S of Q_d has components of Q_d - S = isolated vertices and stars K_{1,d}, centres pairwise at distance >= 4, and \|S\| = 2^{d-1} - #centres >= 2^{d-1} - A(d,4) | PROVED (own argument; reproduces the hard direction of Pike 2003 as stated by Wodlinger Thm 2.34; Pike's proof not seen) | proof.md Lemma I, Steps I1-I7; sanity check out/code/check_indep_structure.py (exhaustive d = 2..5, 0 violations) |
| A(9,4) = 20 | CITED, not reproduced (Best-Brouwer-MacWilliams-Odlyzko-Sloane 1978; Brouwer table opened) | sources.md; proof.md I8 [GAP] |
| Plain Delsarte LP bound for even (9,4) codes is 128/5 (dual certificate beta_1 = 3/5, beta_2 = 3/10, beta_3 = 1/10 verified exactly), so LP alone gives only A(9,4) <= 25 | COMPUTER-VERIFIED (code public: y, out/code/lp_A94.py, exact rationals) | proof.md I8 |
| I8: every decycling set of Q_9 with <= 235 vertices contains an edge | PROVED given the cited A(9,4) = 20 | proof.md I8 |
| Lemma J: for any labelling f of Q_d, S = S_f: F-neighbours of S-vertices are lower (J1); N(u) >= deg_F(u) + 2 down_S(u) on S (J2); P(f) >= 2^d + (d-1)\|S\| + sum_{u in S} max(0, deg_F(u) + 2 down_S(u) - 2) up_S(u) (J3) | PROVED (uses the identity (*) and facts 4(c) of H-C5-002, under review) | proof.md Lemma J; sanity check out/code/check_lemmaJ.py (210 labellings, d = 3..9, 0 violations) |
| J4: in a labelling where every S-edge's lower end has zero cost, and S has an edge, some u in S has 1 <= deg_F(u) <= 2 and up_S(u) >= d-2 | PROVED | proof.md J4 |
| J5 (UPPER necessary condition): a labelling of Q_9 with <= 2399 paths has \|S_f\| <= 235, S_f not independent, and sum_{u in S} max(0, 7 - up_S(u) + down_S(u)) up_S(u) <= 1887 - 8\|S_f\| | PROVED (given A(9,4) = 20 for "not independent") | proof.md J5 |
| J6 (LOWER, conditional): nabla(Q_9) >= 232 plus "no labelling with \|S_f\| = 232 has zero extra" would give U(Q_9) >= 2369; nabla(Q_9) >= 233 alone suffices | PROVED (implications only); hypotheses OPEN | proof.md J6, subproblems.md L3-L5 |
| No induced forest of Q_9 with 277 vertices was found by fixed-size penalty SA (3 runs x 3e7 moves; best cycle rank 1) | search result only (proves nothing) | RAN lines below; out/code/fixsize_sa.c |
| The SA sanity run at 276 vertices (seed 11) returned a parity-type forest (S = 236 even vertices, e(S) = 0, 96 components), consistent with Lemma I | COMPUTER-VERIFIED (code public: y; checked with inbox/earlier/H-C5-002/code/check_forest.py) | out/tmp/q9_K276_s11.txt |
| Organisers' 2368 comes from nabla(Q_9) >= 232 | UNSURE (arithmetic 2368 = 512 + 8*232 only) | - |

## RAN (all measured with date-based wall clock; /usr/bin/time is not installed)
* python3 out/code/check_indep_structure.py (d = 2..5, all independent sets) -- COMPLETED, 1.88 s.
* python3 out/code/lp_A94.py -- COMPLETED, 0.13 s.
* python3 out/code/check_lemmaJ.py (d = 3..9, 30 labellings each, seed 20260926) -- COMPLETED, 0.40 s.
* out/tmp/fixsize_sa (gcc -O2 -lm from out/code/fixsize_sa.c) sanity d = 5,6,7,8 at K = 18,36,72,144, seed 1,
  2e6 moves cap, T 2.0 -> 0.05 -- COMPLETED, forests found, 0.007 / 0.67 / 1.73 / 3.61 s.
* fixsize_sa d = 9 K = 277 seed 5, 2e5 moves (timing test) -- COMPLETED, best r = 4, 1.15 s.
* First batch (d = 9: K = 276 seed 11 at 2e7 moves; K = 277 seeds 21, 22, 23 at 6e7 moves) -- killed by me after
  ~4.5 min wall because they would exceed the time box; no output written -- PARTIAL (no result).
* Second batch, 4 jobs in parallel (shared CPU): fixsize_sa 9 276 11 3e7 1.5 0.1 init0 -- COMPLETED, forest found,
  564 s; fixsize_sa 9 277 21 3e7 1.5 0.1 init0 -- COMPLETED, no forest, best r = 1, 623 s; fixsize_sa 9 277 22 3e7
  1.0 0.05 init1 -- COMPLETED, no forest, best r = 1, 593 s; fixsize_sa 9 277 23 3e7 2.0 0.2 init0 -- COMPLETED,
  no forest, best r = 1, 659 s. (Searches only; no claim depends on them.)
* .venv python3 out/code/sym_cegar.py c9 276 120 (C9-invariant forests, 60 orbit variables) -- TIMED OUT at the
  120 s budget, 37 CEGAR iterations, 6731 cycle clauses, 125.5 s; no conclusion.
* python3 inbox/earlier/H-C5-002/code/check_forest.py out/tmp/q9_K276_s11.txt -- COMPLETED, forest, |S| = 236,
  e(S) = 0, all S even, 96 components, 0.06 s.
