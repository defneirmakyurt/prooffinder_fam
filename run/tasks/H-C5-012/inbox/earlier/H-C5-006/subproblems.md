# Sub-problems for H-C5 (U(Q_9): prove >= 2369 or exhibit <= 2399)

Reduction used (H-C5-002 proof.md Steps 1-8, under review; restated in out/proof.md): for every labelling f,
S_f = {N >= 2} is a decycling set and P(f) = 512 + 8|S_f| + sum_{u in S_f}(N(u)-2)up(u) with all terms >= 0.
Hence 512 + 8 nabla(Q_9) <= U(Q_9) <= 2400. Labels: (a) known and citable, (b) known but hard to access, so
reproduced (or to be reproduced), (c) unknown.

## Shared
| id | statement (precise) | label | status / where |
|---|---|---|---|
| S0 | For every labelling f of Q_d: P(f) = 2^d + (d-1)\|S_f\| + sum_{u in S_f}(N(u)-2)up(u), S_f decycling, every summand >= 0 | new in H-C5-002 (not found in literature) | PROVED there (under review); used here |
| S1 | nabla(Q_n) = 0,1,3,6,14,28,56,112 for n = 1..8 | (a) Beineke-Vandell 1996 (via Bau survey, OEIS A390382); also re-derived in H-C4 (F_5 = 18 exhaustive + doubling) | not needed for H-C5 |
| S2 | A(9,4) = 20 | (a) Best-Brouwer-MacWilliams-Odlyzko-Sloane 1978; Brouwer's table (opened) | CITED; plain Delsarte LP gives only 25 (out/code/lp_A94.py). Reproducing it = (b), not done |

## UPPER route (a labelling with <= 2399 uphill paths)
| id | statement | label | status |
|---|---|---|---|
| U1 | nabla(Q_9) <= 236 (parity + 20-word code) | (a) Focardi-Luccio-Peleg 2000 / Pike 2003 (Hertz 2021 Table 4) | reproduced constructively: H-C5-002 out/Q9.txt, VERIFIED 2400 |
| U2 | Necessary: a labelling with P <= 2399 has \|S_f\| <= 235 | new (H-C5-002 Step 8) | PROVED there |
| U3 | Every independent decycling set of Q_d has size >= 2^{d-1} - A(d,4); for d = 9: >= 236, so any decycling set of size <= 235 has an edge | (b) Pike 2003 (paywalled; only the statement is visible via Wodlinger's thesis Thm 2.34) | REPRODUCED here with own proof: out/proof.md Lemma I + I8 (I8 uses S2, cited) |
| U4 | Necessary (cost of S-edges): P <= 2399 requires sum_{u in S} max(0, 7 - up_S(u) + down_S(u)) up_S(u) <= 1887 - 8\|S\| | new here | PROVED: out/proof.md J3, J5 |
| U5 | EXISTENCE: an induced forest of Q_9 with >= 277 vertices (decycling set <= 235), necessarily with an edge inside S (U3), i.e. nabla(Q_9) <= 235 | (c) OPEN: best known 236 (Pike 2003 / Hertz 2021 Table 4); equivalent (Pike) to "Q_9 has NO independent minimum decycling set" | not found; searches failed (RAN lines; H-C5-002 SA; Hertz CliqueSearch restricted to independent sets) |
| U6 | Given a U5 set S, an order of S with extra cost <= 1887 - 8\|S\| (U4) | (c) | only relevant once U5 is found; by J4, zero-cost S-edges need their lower end to have >= 7 upper S-neighbours |

## LOWER route (every labelling has >= 2369 uphill paths)
| id | statement | label | status |
|---|---|---|---|
| L1 | nabla(Q_9) >= 225 (edge counting) | (a) Beineke-Vandell Lemma 2.1(2); Gunderson et al. Thm 1.5; Mynhardt-Wodlinger Prop 3.4 | PROVED (H-C5-002 Step 9) -> U(Q_9) >= 2312 |
| L2 | nabla(Q_9) >= 226 via kappa(F) + eps(S) >= n + 1 | (b) Pike 2003 as reported by Wodlinger (Thm 2.31 and outline); Hertz's Table 4 says 225 "from [25]": discrepancy | NOT reproduced; irrelevant for the cell (-> 2320) |
| L3 | nabla(Q_9) >= 232 (would give U(Q_9) >= 2368, the organisers' bound) | (c) for me: organisers call their bound unpublished; no published nabla bound above 226 found | not attempted beyond the obstruction analysis in why_not.md |
| L4 | nabla(Q_9) >= 233 (would give U(Q_9) >= 2376 >= 2369: SOLVES the lower route) | (c) OPEN (gap 225/226 .. 236 in all sources found) | not proved |
| L5 | Alternative to L4: nabla(Q_9) >= 232 AND no labelling with \|S_f\| = 232 has zero extra cost. By I8 + J4 such a labelling has an S-edge and a vertex u in S with 1 <= deg_F(u) <= 2, up_S(u) >= 7 | (c) | reduction proved (out/proof.md J6); both parts open |
| L6 | Equivalent counting form of L4: every induced forest F of Q_9 has c(F) + e(S) >= 72, where c = #components and S = V \ F (identity 8\|S\| = 1792 + c + e(S)) | (c) | identity PROVED (H-C5-002 Step 6 / Pike identity (2.4)); inequality open |
