# Sources: H-C5-002 (Phase 1L, literature)

Access note: from 13:09 to ~13:20 every WebFetch/curl to arxiv.org, oeis.org, springer, wikipedia, AJC, MUN,
Ljubljana etc. was blocked by the egress proxy; after the head's process note, curl to arxiv.org (HTML
versions) and www.math.mun.ca worked; WebFetch to arxiv.org was still blocked; link.springer.com returned a
JavaScript challenge page (content not accessible). No PDF text extractor is installed, so only arXiv HTML
renderings could be read. "opened" below means I read the relevant passage in a locally saved copy
(out/tmp/...html.txt).

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/html/math/0703544v1 (saved: out/tmp/https___arxiv.org_html_math_0703544v1.html.txt, Section 2 "Cubes") | S. Bau, *The decycling number of graphs* (survey), arXiv math/0703544, 2007. Lemma 2.1 (quoting Beineke-Vandell Lemma 2.1), table "For n <= 8, [3] computed nabla(Q_n) exactly", table of bounds for Q_9..Q_13, Theorem 2.3 (quoting Bau-Beineke-Du-Liu-Vandell Thm 4.1) | (i) nabla(Q_n) = 0,1,3,6,14,28,56,112 for n = 1..8 -> with my identity gives U(Q_d) = 14,34,88,204,464,1040 for d=3..8 (conditional, proof.md Step 11); (ii) Lemma 2.1(2): nabla(Q_n) >= 2^{n-1} - (2^{n-1}-1)/(n-1) (= my Step 9); (iii) Theorem 2.3(1): 225 <= nabla(Q_9) <= 237 | small-n values: reported as COMPUTED ("computed ... exactly") -> COMPUTER-VERIFIED? (code public: n, UNSURE whether computer or hand); Lemma 2.1(2): PROVED (easy counting, reproduced in proof.md Step 9); 225 <= nabla(Q_9) <= 237: PROVED per survey | survey only cites; "The reader is referred to the elaborate proof ... in [1]" -- argument NOT in the survey | YES (survey passage); the primary sources NOT opened |
| (cited inside Bau's survey) | L.W. Beineke, R.C. Vandell, *Decycling graphs*, J. Graph Theory 25 (1996) 59-77, Lemma 2.1 and the n <= 8 table | as above | COMPUTER-VERIFIED or PROVED -- UNSURE which | unknown | NO |
| (cited inside Bau's survey) | S. Bau, L.W. Beineke, G.-M. Du, Z.-S. Liu, R.C. Vandell, *Decycling cubes and grids*, Utilitas Math. (2000) 10-18, Thm 4.1: 225 <= nabla(Q_9) <= 237 | bounds on nabla(Q_9) | PROVED (per survey) | unknown | NO |
| https://link.springer.com/article/10.1007/s00373-003-0529-9 | D.A. Pike, *Decycling hypercubes*, Graphs Combin. 19 (2003) 547-550 (bibliographic data confirmed on Pike's publication page https://www.math.mun.ca/~dapike/publications/, opened, entry "D.A. Pike. Decycling hypercubes, Graphs and Combinatorics 19 (2003) 547-550", no online copy) | Abstract as returned by web search snippets only: "Improved bounds are obtained for nabla(Q_n) ... nabla(Q_n) = 2^{n-1} - A(n,4) [snippet renders it '2 n -1-A(n,4)'] if and only if Q_n has a minimum decycling set that consists of pairwise non-adjacent vertices". Consistent with my construction (proof.md Step 10), which gives 2^{n-1} - A(n,4) with an independent set | UNSURE (not opened; exact formula rendering uncertain; which "improved bounds" for Q_9 is unknown to me) | unknown | NO (Springer page is a JS challenge; only search snippets) |
| (not found online) | R. Focardi, F.L. Luccio, D. Peleg, *Feedback vertex set in hypercubes*, Inform. Process. Lett. 76 (2000) 1-5 | bibliographic data only (cited in arXiv 2501.05145 and 2501.06902 reference lists, opened) | UNSURE (content not read) | unknown | NO |
| https://arxiv.org/html/2501.06902 (saved out/tmp/ax_2501.06902.html.txt) | A. Ghalavand, S. Klavzar et al., *On decycling and forest numbers of Cartesian products of trees*, 2025, Section 1 | checked for newer hypercube values: none given (only cites Beineke-Vandell, Focardi-Luccio-Peleg) | n/a | n/a | YES (intro + references) |
| https://arxiv.org/html/2501.05145 (saved out/tmp/ax_2501.05145.html.txt) | *On maximum induced forests of the balanced bipartite graphs*, 2025, Section 1 | same check: no Q_9 value | n/a | n/a | YES (intro) |
| https://arxiv.org/html/1810.04252 (saved out/tmp/ax_1810.04252.html.txt) | *Cycle intersection graphs and minimum decycling sets of even graphs*, 2018, Section 1 | same check: "Improving the bound on the decycling number of hypercubes was continued in [2] and [13]" -- no values | n/a | n/a | YES (intro) |
| https://arxiv.org/html/2310.18163 (saved) | *A collection of open problems in celebration of Imre Leader's 60th birthday*, 2023 | checked because a web search listed it for "uphill paths hypercube": it contains NO uphill-path / valley / Nordic-square / decycling problem (grep for uphill, valley, nordic, decycl, induced forest, IMO: no hits besides unrelated hypercube problems) | n/a | n/a | YES (full text grep) |
| inbox/earlier-C1-sources.md | earlier literature worker H-C1-006 | IMO 2022 P6 sources (Bajnok report, Grozev blog) for the |E|+1 bound; its "not found" list | as tagged there | as tagged there | I read that file only; did not re-open its sources |
| standard coding-theory tables (e.g. MacWilliams-Sloane; Brouwer's table) | A(n,4) = 1,2,2,4,8,16,20 for n = 3..9 | only to explain why the code sizes found by search are the best possible for this construction; NOT needed for any claim (the checker verifies the files) | PROVED (classical) | n/a | NO |

## Not found (sources searched)
No source found that poses or studies the uphill-path problem on the hypercube, or the numbers 2368 / 2400.
Searched: web search (Anthropic) with queries "uphill paths hypercube labelling minimum number valleys IMO 2022
Problem 6 generalization", "\"uphill paths\" hypercube Q_d minimum", "Nordic square hypercube \"uphill\"
labelling open problem 2368 2400", "\"Nordic square\" hypercube generalization \"uphill paths\" d-dimensional",
"artofproblemsolving IMO 2022 P6 \"hypercube\" uphill paths higher dimensions", "mathoverflow IMO 2022 problem 6
uphill paths general graph minimum hypercube"; plus the arXiv HTML texts above. OEIS, AoPS, MathOverflow could
not be opened (blocked) during the window I searched them. This is NOT a claim that the problem is new.

No source found giving nabla(Q_9) exactly or a bound better than 225 <= nabla(Q_9) <= 237 in a text I could
open. Queries: "decycling number hypercube Q_9 known values maximum induced forest hypercube table",
"\"decycling number\" \"Q_9\" OR \"Q9\" hypercube bounds", "decycling number of the 9-cube 236 OR 233 OR 232
hypercube \"decycling\" lower bound improved", "Pike \"Decycling hypercubes\" ...". Pike (2003) is the likely
place for improved Q_9 bounds but was not accessible.

## Computations whose code is unavailable
* Beineke-Vandell's determination of nabla(Q_n) for n <= 8 (the survey says "computed"): code not available,
  method not seen. Used only for the conditional Step 11 of proof.md.
* The organisers' lower bound 2368 is "unpublished": argument and code unavailable. My observation
  2368 = 2^9 + 8*232 is arithmetic, and the guess that it comes from nabla(Q_9) >= 232 is UNSURE.

## Steps called routine but not written down in the sources
* Bau's survey: "The reader is referred to the elaborate proof of this theorem in [1]" (225 <= nabla(Q_9) <= 237):
  not written in the survey. I use only the lower bound 225, which I prove myself (proof.md Step 9).
