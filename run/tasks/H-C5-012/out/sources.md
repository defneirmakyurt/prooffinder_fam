# Sources: H-C5-012 (Phase 3, ANALYST, literature; second analyst pass)

Access log (2026-09-26, 14:30-15:10 UTC). Reachable: link.springer.com abstract pages, **page-one.springer.com
(Springer "preview" PDF = first two pages of an article)**, www.math.mun.ca (by curl; WebFetch blocked),
jgaa.info, ajc.maths.uq.edu.au, arxiv.org, dspace.library.uvic.ca, api.semanticscholar.org, api.zbmath.org.
Not reachable / no full text: Springer full PDF of Pike 2003 (HTTP 303 to login), ResearchGate (403),
doi.org (egress blocked), toc.ui.ac.ir (connection reset), scholar.archive.org (rate-limited), CORE API (429),
Unpaywall (requires a real e-mail; not used). PDFs converted with pypdf; text dumps in out/tmp/.
"opened" = I read the quoted passage in the saved text. The first pass (inbox/earlier/H-C5-006/sources.md)
is not repeated; rows below are new, or re-opened by me where a claim here depends on them.

Notation: nabla(Q_n) = decycling number = 2^n - (max induced forest). Cell reduction (H-C5-002, under review):
512 + 8 nabla(Q_9) <= U(Q_9) <= 2400.

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://page-one.springer.com/pdf/preview/10.1007/s00373-003-0529-9 (text: out/tmp/pageone.txt) | D.A. Pike, *Decycling hypercubes*, Graphs Combin. 19 (2003) 547-550, **pp. 547-548 only** (Abstract, Sect. 1, Sect. 2: Lemma 1, Lemma 2, Theorem 1, Corollary 1) | p.547: prior bounds quoted as 2^{n-1} - (2^{n-1}-1)/(n-1) <= nabla(Q_n) <= nabla(Q_{n-1}) + 2^{n-2} (from [1] = Bau-Beineke-Du-Liu-Vandell) and nabla(Q_n) <= 2^{n-1} - 2^{n-1}/(2(n-1)) ([5] = Focardi-Luccio-Peleg); "In this paper we narrow the bounds". p.548: **Lemma 1** (a max (n,4) code can be taken all even weight; proof given: flip last coordinate of the odd-weight words), **Lemma 2** (A even (n,4) code, S = even vertices not in A is decycling; proof only by reference to "the proof of Lemma 4 of [5]"), **Theorem 1** nabla(Q_n) <= 2^{n-1} - A(n,4), **Corollary 1** n = 2^r - x, 0 <= x < 2^{r-1} => nabla(Q_n) <= 2^{n-1} - 2^{n-r-1} (for n = 9: r = 4, gives only 240). Nothing on p.547-548 is specific to n = 9; no non-independent construction. | Lemma 1, Thm 1, Cor 1: PROVED | Lemma 1, Thm 1, Cor 1: yes; Lemma 2: cites [5] | pp. 547-548 YES; **pp. 549-550 NO** (paywall) |
| https://www.math.mun.ca/~dapike/publications/ (saved out/tmp/pike_pubs.html) | D.A. Pike, publication list | entry "Decycling hypercubes" has **no** online-access link (other papers of the same years do); guessed file names 404 | n/a | n/a | YES |
| https://dspace.library.uvic.ca/server/api/core/bitstreams/6920a182-6228-4654-b594-ce68dce6d0c5/content (text: out/tmp/wod.txt, pp. 31-33) | J. Wodlinger, PhD thesis, U. Victoria 2018, Sect. 2.3.3, Thm 2.31, (2.3), Thm 2.34, (2.4) | re-opened to pin down what Pike's missing pp. 549-550 contain: (i) Pike proves A(n,4) <= 2^{n-1}/n ((2.3), attributed to [85] = Pike); (ii) Thm 2.31 lower bound 2^{n-1} + (n+1-2^{n-1})/(n-1) for n >= 7 (attributed to [47,85]); (iii) Thm 2.34 (iff independent minimum decycling set); (iv) identity (2.4); (v) "Pike then proves kappa(G-S)+eps(S) >= n+1 ... In the case where every minimum decycling set contains at least one edge, Pike proves that in fact it contains at least n edges." | PROVED per thesis (secondary) | outlines only for (ii), (iii), (v); (iv) derived | YES |
| https://jgaa.info/index.php/jgaa/article/download/paper567/2402 (text: out/tmp/hertz.txt) | A. Hertz, *Decycling bipartite graphs*, JGAA 25(1) (2021), Sect. 3.4, **Table 4**, Sect. 4 | re-opened: Table 4 L(Q_n) = 225, 456, 922, 1862, 3755 (n = 9..13) "from [25]"; U = 236, 472, 952, 1904, 3840; text says U(Q_n) = 2^{n-1} - 2^{n-r-1} (Pike's Cor. 1), which does NOT match the tabulated U for n = 9 (formula 240, table 236) -> the description and the table are inconsistent. CliqueSearch restricted to F = Y u clique of H_n (independent S only). Sect. 4: "easy to construct bipartite graphs with no decycling set of minimum size fully contained in X or Y" (Fig. 8, a small ad-hoc graph, not a hypercube). | as in H-C5-006 | cites table values | YES |
| out/code/bounds_table.py (my computation, exact rationals) | - | Hertz's L column equals, for **all five** n = 9..13, the ceiling of the pre-Pike bound 2^{n-1} - (2^{n-1}-1)/(n-1) of [1] (225, 456, 922, 1862, 3755), and is exactly 1 below the ceiling of Wodlinger's statement of Pike's bound (226, 457, 923, 1863, 3756). Pike p.547 says [1]'s bound is the one he improves. => Hertz's "L from [25]" is very probably the [1] bound, mislabelled; Pike's bound for n = 9 is very probably 226. | COMPUTER-VERIFIED (code public: y) for the arithmetic; the attribution conclusion is UNSURE (pp. 549-550 unseen) | - | - |
| https://ajc.maths.uq.edu.au/pdf/74/ajc_v74_p288.pdf (text: out/tmp/ajc74.txt) | M.D. Francis, C.M. Mynhardt, J.L. Wodlinger, *Subgraph-avoiding minimum decycling sets and k-conversion sets in graphs*, Australas. J. Combin. 74(2) (2019) 288-304, **Thm 1.1, Thm 1.2 (Version 2), Lemma 3.1** | For r-regular G != K_{r+1}, r >= 3: some minimum decycling set S has G[S] with no (r-2)-regular subgraph; every minimum decycling set has Delta(G[S]) <= r-2 (stated p.293); Lemma 3.1 "seed shuffle": if x in S has exactly r-2 neighbours in S and v is one of its two outside neighbours, S - x + v is again decycling (same size). For Q_9: a minimum decycling set has every vertex with <= 7 S-neighbours, and one can be chosen with no 7-regular subgraph in Q_9[S]. No hypercube values (cites Pike only in the introduction). | PROVED | yes (Lemma 3.1 proof in full; Thm 1.2 proof in Sect. 3) | YES (pp. 288-293, 300-302) |
| https://arxiv.org/abs/2102.09194 (text: out/tmp/ax_2102.09194.txt) | R.A. Melo, C.C. Ribeiro, *Maximum weighted induced forests and trees: new formulations and a computational comparative review*, arXiv 2021 (ITOR), Sect. 4.1-4.2, **Table 8** (large hypercube instances) | Branch-and-cut / compact ILP formulations (CYC, FLOW, MTZ, TCYC, DCUT; 3600 s limit, warm start) on vertex-**weighted** Q_n instances of Carrabs et al. (2011): H 7 partly solved, **H 8 and H 9: 0 of 5 instances solved to optimality** by the cycle-elimination formulations, final gaps about 2-6 % (e.g. CYC gap 5.5 % on H 9 10 25). | COMPUTER-VERIFIED (code public: UNSURE, not seen) | method yes | YES (Sect. 4, Table 8 rows H 7-9) |
| https://arxiv.org/abs/2501.06902 (text: out/tmp/ax_2501.06902.txt) | A. Ghalavand, S. Klavzar, N. Yang, *On decycling and forest numbers of Cartesian products of trees*, arXiv 2025 (Bull. Malays. Math. Sci. Soc.) | products of TWO trees only; T x K_2 prisms (nabla = matching number); nabla(G1 x G2) >= alpha'(G1) alpha'(G2). Nothing on Q_n for n >= 3 beyond citations of Beineke-Vandell, Focardi et al., Pike-Zou. | PROVED | yes | YES (abstract, intro grep) |
| https://arxiv.org/abs/2501.05145 | *On maximum induced forests of the balanced bipartite graphs*, arXiv 2025 | only cites Beineke-Vandell and Focardi-Luccio for hypercubes | n/a | n/a | YES (grep) |
| https://arxiv.org/abs/2604.15534 ; https://arxiv.org/abs/2411.19734 | J.A. Noel, *Optimal and near-optimal constructions for bootstrap percolation in hypercubes* (2026); G. Berczi, A.Z. Wagner, *A note on small percolating sets on hypercubes via generative AI* (2024) | checked because nabla(Q_9) = m(Q_9; 8) (8-neighbour bootstrap, Dreyer-Roberts equivalence, restated in Francis et al. p.289). Both treat r = 4, 5 only (tables for d = 9 are for r = 4, 5); nothing for r = d-1. | n/a | n/a | YES (abstract + grep) |
| https://ajc.maths.uq.edu.au/pdf/35/ajc_v35_p031.pdf (decoded: out/tmp/ajc35_dec.txt) | J.A. Ellis-Monaghan, D.A. Pike, Y. Zou, *Decycling of Fibonacci cubes*, AJC 35 (2006) 31-40 | intro only cites [3,6,11] for hypercubes; no hypercube values | n/a | no | YES (intro) |
| https://api.zbmath.org (search "decycling hypercube", "feedback vertex set hypercube", "induced forest hypercube") | zbMATH Open | Pike 2003 = Zbl 1032.05071, review text **unavailable** ("conflicting licenses"). Found C. Vandell, *Recycling decycling*, Congr. Numer. 188 (2007) 3-10 (Zbl 1138.05041): review says it studies largest independent MINIMAL decycling sets in products of cycles and "certain hypercubes" | Vandell 2007: UNSURE (not online) | unknown | review YES; paper NO |
| https://api.semanticscholar.org (citations of DOI 10.1007/s00373-003-0529-9) | 19 citing works (2003-2023) | none newer than Gunderson et al. 2023; hypercube-relevant ones opened (Hertz; Mynhardt-Wodlinger AKCE; Francis-Mynhardt-Wodlinger AJC; Gunderson et al. by H-C5-006) | n/a | n/a | list YES |
| (not accessible) | C.M. Mynhardt, J.L. Wodlinger, *A lower bound on the k-conversion number of graphs of maximum degree k+1*, Trans. Comb. 8(3) (2019) | host unreachable; for regular graphs this is the counting bound (same identity), so at most 225 for Q_9 [reasoning, UNSURE] | UNSURE | - | NO |
| (not online) | C. Vandell, *Recycling decycling*, Congr. Numer. 188 (2007); S. Bau et al., *Decycling cubes and grids*, Util. Math. 59 (2001) | - | UNSURE | - | NO |

## What this pass changes about "what is known" for nabla(Q_9)
* Pike 2003 pp. 547-548 (opened for the first time): the 236 upper bound is Theorem 1 with A(9,4) = 20 (A(9,4) itself is not
  computed in the paper's first two pages); Corollary 1 alone gives 240 for n = 9. PROVED. No non-independent construction.
* Pike's lower bound for n = 9: very probably 226 (Wodlinger's formula); Hertz's 225 matches the older [1] bound at all
  n = 9..13 (bounds_table.py). UNSURE until pp. 549-550 are read. Irrelevant to the cell's thresholds (233 / 235).
* No source (any n) exhibits a non-independent minimum decycling set of Q_n, or any n with nabla(Q_n) < 2^{n-1} - A(n,4).
  For n <= 8 the exact values equal 2^{n-1} - A(n,4) (independent sets achieve them); for 9 <= n <= 13 the best known
  upper bounds equal 2^{n-1} - A(n,4) (Hertz Table 4).
* No bound on nabla(Q_9) newer than Hertz 2021 found (lower 225/226, upper 236).
* Exact ILP (branch-and-cut) was run on weighted Q_8, Q_9 by Melo-Ribeiro and could not close them in 1 h (gaps 2-6 %).

## Not found (sources and queries)
Searched: WebSearch queries "Pike \"Decycling hypercubes\" pdf"; "\"decycling number\" hypercube \"A(n,4)\" independent
minimum decycling set non-independent"; "maximum induced forest hypercube Q_9 SAT solver OR \"integer programming\" feedback
vertex set exact"; "\"feedback vertex set\" hypercube \"Q_9\" OR \"9-cube\" OR \"n = 9\" decycling 236 OR 235 OR 232";
"Zou thesis decycling Memorial University ..."; "bootstrap percolation hypercube minimum percolating set threshold \"d-1\" ...";
"\"decycling number\" hypercube lower bound improved 2024 OR 2025 OR 2026 arXiv"; "\"Recycling decycling\" Vandell ...";
"\"feedback number\" hypercube Xu ..."; "\"induced forest\" hypercube \"largest\" ... \"Q_9\" ... 276 OR 277";
"\"A new formula for the decycling number of regular graphs\""; "\"The forest number in several classes of regular graphs\"";
"\"Subgraph-avoiding minimum decycling sets ...\""; zbMATH API (3 queries above); Semantic Scholar citation list; Pike's
home page. Result: no decycling set of Q_9 with <= 235 vertices, no proof of nabla(Q_9) >= 227, no non-independent minimum
decycling set of any Q_n, no SAT/ILP determination of the forest number of Q_9. This is not a claim that none exists.

## Computations whose code is unavailable / steps only outlined
* Melo-Ribeiro Table 8 (hypercube B&C runs): code not seen.
* Pike pp. 549-550 (lower bound, iff theorem, "at least n edges"): only outlined by Wodlinger; not reproduced here.
* Pike Lemma 2 proof: by reference to Focardi et al. Lemma 4 (a full proof is in Wodlinger Lemma 2.33 and in
  H-C5-006 Lemma I).
