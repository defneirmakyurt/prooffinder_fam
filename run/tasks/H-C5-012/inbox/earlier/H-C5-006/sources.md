# Sources: H-C5-006 (Phase 3, ANALYST, literature)

Access log (2026-09-26, 13:34-14:15 UTC). This time arxiv.org (abs, html, pdf), jgaa.info, oeis.org,
mathworld.wolfram.com, dspace.library.uvic.ca, api.semanticscholar.org and link.springer.com (abstract page
only) were reachable by curl. PDFs were converted to text with pypdf (installed into the project venv for this
purpose; text dumps are in out/tmp/*.txt). "opened" = I read the quoted passage in the saved text.
Not reachable: ScienceDirect (403), the Elsevier PDF link on F.L. Luccio's page (proxy 502), the full text of
Pike 2003 (Springer paywall; only the abstract is on the page), Utilitas Math. (no online copy found).

Notation: nabla(Q_n) = decycling number = 2^n - (max induced forest of Q_n). The cell reduces to it via
512 + 8 nabla(Q_9) <= U(Q_9) (H-C5-002 proof.md Step 8, under review).

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://jgaa.info/index.php/jgaa/article/download/paper567/2402 (text: out/tmp/hertz.txt) | A. Hertz, *Decycling bipartite graphs*, J. Graph Algorithms Appl. 25(1) (2021) 461-480, Section 3.4 and **Table 4** | Table 4 "Bounds from [25]" ([25] = Pike 2003): n = 9: L(Q_9) = 225, U(Q_9) = 236 (upper bound "from [5]" = Bau survey: 237); CliqueSearch (tabu, restricted to F = one full parity class + a clique of the distance->=4 graph on the other class) reaches UB(Q_9) = 236 in < 1 s but nothing lower. Also: "Most of the largest forests ... contain all vertices of one part"; the general algorithm LargeForest was **not** run on Q_n. Concluding list of improved bounds does not contain Q_9. | 225 <= nabla(Q_9) <= 236: bounds reported as literature values (PROVED in Pike per Hertz); the 236 forest is constructive (COMPUTER-VERIFIED here, see below) | cites only (table values from [25]); algorithm described in full, code not public (no link for hypercube runs) | YES (Sect. 3.4, Table 4, Sect. 4) |
| https://dspace.library.uvic.ca/server/api/core/bitstreams/6920a182-6228-4654-b594-ce68dce6d0c5/content (text: out/tmp/wodlinger.txt) | J. Wodlinger, *Irreversible k-threshold conversion processes on graphs*, PhD thesis, Univ. of Victoria (2018), **Section 2.3.3**, Thm 2.31, Lemmas 2.32-2.33, Thm 2.34, identity (2.4) | Second-hand account of Pike 2003: (i) Thm 2.31 [47,85]: for n >= 7, 2^{n-1} + (n+1-2^{n-1})/(n-1) <= nabla(Q_n) <= 2^{n-1} - 2^{n-1}/(2(n-1)); (ii) Lemma 2.33 (Focardi et al.): O u A acyclic for an even (n,4) code A, full proof given; (iii) Thm 2.34 (Pike): nabla(Q_n) = 2^{n-1} - A(n,4) iff Q_n has an independent minimum decycling set; (iv) identity |S| = 2^{n-1} + (kappa(G-S) + eps(S) - 2^{n-1})/(n-1); (v) "Pike then proves kappa(G-S) + eps(S) >= n+1 ... In the case where every minimum decycling set contains at least one edge, Pike proves that in fact it contains at least n edges." For n = 9, (i) gives nabla(Q_9) >= 225.25, i.e. >= 226, which **disagrees** with Hertz's L(Q_9) = 225 "from [25]" (see KNOWN DISCREPANCY below). Also: k-conversion sets of (k+1)-regular graphs = decycling sets (Dreyer-Roberts, Sect. 2), so nabla(Q_9) = min size of a percolating set for 8-neighbour bootstrap percolation on Q_9. | Thm 2.34, kappa+eps >= n+1: PROVED in Pike per the thesis; Lemma 2.33: PROVED (argument in thesis) | Lemma 2.33 and identity (2.4): argument contained; Thm 2.34 and kappa+eps >= n+1: only outlined ("Pike proves ..."), NOT contained | YES (pp. 31-34) |
| https://link.springer.com/article/10.1007/s00373-003-0529-9 (saved out/tmp/springer_pike.html) | D.A. Pike, *Decycling hypercubes*, Graphs Combin. 19(4) (2003) 547-550 | Abstract only: "Improved bounds are obtained for nabla(Q_n). Further, it is shown that nabla(Q_n) = 2^{n-1} - A(n,4) if and only if Q_n has a minimum decycling set that consists of pairwise non-adjacent vertices." | PROVED (per abstract) | full text not accessible (paywall) | abstract YES; body NO |
| https://arxiv.org/pdf/math/0703544 (text: out/tmp/bau.txt) | S. Bau, *The decycling number of graphs* (survey), arXiv math/0703544 (2007), Section 2: Lemma 2.1, table n <= 8, Thm 2.3 | nabla(Q_n) = 0,1,3,6,14,28,56,112 (n = 1..8) "computed" in Beineke-Vandell [3]; Lemma 2.1: nabla(Q_n) >= 2 nabla(Q_{n-1}) and >= 2^{n-1} - (2^{n-1}-1)/(n-1); Thm 2.3 (from Bau-Beineke-Du-Liu-Vandell [1], Thm 4.1): 225 <= nabla(Q_9) <= 237 | table: COMPUTER-VERIFIED? (code public: n; UNSURE computer or hand); Thm 2.3: PROVED per survey | cites only ("The reader is referred to the elaborate proof ... in [1]") | YES |
| https://arxiv.org/abs/2301.05207 (text: out/tmp/ax_2301.05207.txt) | K. Gunderson, K. Meagher, J. Morris, V.R.T. Pantangi, *Induced forests in some distance-regular graphs*, arXiv 2023 (DAM 2024), Thm 1.4 (spectral bound), Thm 1.5 (edge counting) | Checked for hypercube values: only cites [5,14,27]. Thm 1.4 for Q_9 (k = 9, lambda = -9) gives max forest <= ~313 (weaker than counting); Thm 1.5 gives max forest <= (nk-2c)/(2k-2) = (4608-2c)/16, i.e. nabla(Q_9) >= 225 again | PROVED | yes | YES (Sect. 1) |
| https://arxiv.org/abs/1812.03250 (text: out/tmp/ax_1812.03250.txt) | C.M. Mynhardt, J.L. Wodlinger, *The k-conversion number of regular graphs*, AKCE 2020, Prop. 3.4 | Same edge-counting identity n_S = (n(k-1) + 2 m_S + 2y)/(2k) for (k+1)-regular G; equality iff S independent and G-S a tree. No hypercube values. | PROVED | yes | YES (Sect. 3.2) |
| https://oeis.org/A390382 (saved out/tmp/oeis_A390382.txt) | E.W. Weisstein, OEIS A390382 "Feedback vertex set (decycling) number of the n-hypercube graph" (Jan 2026) | Data 0,0,1,3,6,14,28,56,112 for n = 0..8; keyword "more"; no n = 9 term, no bounds | as data (no proof/code given) | no | YES |
| https://mathworld.wolfram.com/FeedbackVertexSetNumber.html | E.W. Weisstein, *Feedback Vertex Set Number*, MathWorld (updated Sep 2026) | Family table has no hypercube entry beyond general bound nabla <= ... ; nothing on Q_9 | n/a | no | YES |
| https://api.semanticscholar.org (query DOI 10.1007/s00373-003-0529-9) | Semantic Scholar "cited by" list for Pike 2003 (19 citing papers) | used to enumerate citing papers; those with hypercube content opened above (Hertz 2021, Gunderson et al. 2023, Mynhardt-Wodlinger); others are about tori, star graphs, hierarchical cubic networks, Sierpinski graphs, de Bruijn graphs (titles only) | n/a | n/a | list YES; the non-hypercube papers NO |
| https://arxiv.org/html/2606.26761 | D. Ilkovic, *Maximum forest number of general bipartite graphs*, arXiv June 2026 | checked (full-text grep "hypercube", "Q_9", "decycl"): Ore-type degree conditions only, nothing on Q_n | n/a | n/a | YES (grep) |
| (not accessible: ScienceDirect 403, Elsevier CDN 502) | R. Focardi, F.L. Luccio, D. Peleg, *Feedback vertex set in hypercubes*, Inform. Process. Lett. 76 (2000) 1-5 | only via Wodlinger: source of Lemma 2.33 (parity + code construction) and A(n,4) >= 2^{n-2}/(n-1) | PROVED (per thesis) | unknown | NO |
| (not online) | S. Bau, L.W. Beineke, G.-M. Du, Z.-S. Liu, R.C. Vandell, *Decycling cubes and grids*, Utilitas Math. 59 (2001?) / (2000) | only via Bau survey (Thm 2.3) | PROVED per survey | unknown | NO |
| (Wiley, not opened) | L.W. Beineke, R.C. Vandell, *Decycling graphs*, J. Graph Theory 25 (1996) 59-77 | only via Bau survey and Wodlinger: nabla(Q_n) for n <= 8 | UNSURE whether computer or proof | unknown | NO |
| inbox/earlier/H-C5-002/sources.md | earlier literature worker (Phase 1L) | its reading of the Bau survey is confirmed here (same Thm 2.3 text) | as tagged there | - | file read |

## What is known about nabla(Q_9) (the quantity both routes reduce to)
* Upper: nabla(Q_9) <= 236 = 2^8 - A(9,4), A(9,4) = 20. Construction: odd vertices + an even-weight
  distance-4 code of size 20 (Focardi-Luccio-Peleg / Pike via Wodlinger Lemma 2.33; Hertz Table 4).
  Reproduced constructively in H-C5-002 (out/Q9.txt, checker VERIFIED 2400). PROVED.
* Lower: nabla(Q_9) >= 225 (edge counting; Beineke-Vandell Lemma 2.1(2), Bau et al., Hertz Table 4;
  re-proved in H-C5-002 Step 9). PROVED. Possibly >= 226 by Pike's kappa + eps >= n + 1 (as reported by
  Wodlinger; not opened in the primary source; see discrepancy). UNSURE.
* Structural: nabla(Q_n) = 2^{n-1} - A(n,4) iff an independent minimum decycling set exists (Pike, Thm 2.34
  in Wodlinger). PROVED per two secondary sources; argument not seen. Consequence for n = 9: every decycling
  set of size <= 235 has an edge inside it.
* No source found gives nabla(Q_9) exactly, a decycling set of Q_9 of size <= 235, or a lower bound >= 227.

## KNOWN DISCREPANCY
Hertz (2021, Table 4) lists L(Q_9) = 225, L(Q_10) = 456, L(Q_11) = 922, L(Q_12) = 1862, L(Q_13) = 3755 as
"Bounds from [25]" (Pike). These equal the Bau et al. / counting values. Wodlinger's statement of Pike's lower
bound, 2^{n-1} + (n+1-2^{n-1})/(n-1), rounds up to 226, 457, 923, 1863, 3756. One of the two secondary sources
misreports Pike, or Pike's table does not round up. Pike's paper could not be opened. For the cell this is
irrelevant (both are far below 233).

## Not found (sources searched)
No source giving nabla(Q_9), a decycling set of Q_9 of size <= 235, or nabla(Q_9) >= 227.
Queries (WebSearch): "Pike \"Decycling hypercubes\" Graphs and Combinatorics 2003 A(n,4)"; "decycling number
hypercube Q_9 bounds \"feedback vertex set\" hypercube 9-cube"; "\"decycling number\" hypercube Q_9 improved
lower bound 2024 OR 2025 OR 2026"; "\"maximum induced forest\" hypercube exact value n=9 computer search";
"bootstrap percolation hypercube threshold d-1 minimum percolating set decycling number Pike A(d,4)";
"\"k-conversion\" OR \"irreversible threshold\" hypercube Q_n decycling ... independent minimum decycling set";
"\"Decycling and dominating cubes and grids\""; "Pike \"Decycling hypercubes\" pdf \"minimum decycling set\"
\"pairwise non-adjacent\" proof n edges lower bound". OEIS searches: 0,1,3,6,14,28,56,112 (-> A390382 only);
1,2,3,5,10,18,36,72,144 (no hit); "hypercube induced forest" (no relevant hit). Semantic Scholar citing list
of Pike 2003 (19 papers, titles screened). This is not a claim that nothing exists.
No source found that states the uphill-path problem on Q_d or the numbers 2368/2400 (not re-searched here;
see H-C5-002 sources.md).

## Computations whose code is unavailable
* Hertz 2021 CliqueSearch runs on Q_9..Q_13 (code not public for these runs; result 236 is anyway reproduced
  constructively by H-C5-002).
* Beineke-Vandell nabla(Q_n), n <= 8 ("computed"): method/code not seen. (For the cell only the n = 9 case
  matters; n <= 8 values are re-derived in H-C4 via F_5 = 18 plus doubling, per inbox/C4-lemmaA-claims.md.)
* The organisers' lower bound 2368: unpublished; argument unknown. 2368 = 512 + 8*232 (arithmetic only).

## Steps called routine / only outlined in the sources
* Wodlinger: "Pike then proves kappa + eps >= n + 1"; "Pike proves that in fact it contains at least n edges":
  outlined, not written.
* Bau survey: Thm 2.3 "elaborate proof ... in [1]": not written.
