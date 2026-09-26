# Sources: H-C2-002

IMPORTANT ACCESS NOTE. In this run WebFetch was blocked by the egress proxy for EVERY domain tried
(researchgate.net, link.springer.com, arxiv.org, export.arxiv.org, ajc.maths.uq.edu.au,
www.math.mun.ca, mathworld.wolfram.com, oeis.org). After the head reported that fetches work
again, I retried arxiv.org (twice), oeis.org, en.wikipedia.org, www.semanticscholar.org: all still
returned EGRESS_BLOCKED in this session. Only the web-search engine worked. Therefore
**no reference below was opened**; everything is from search-engine result titles/summaries, which
are not sources. Nothing in out/proof.md depends on any of them: the lower bound uses only the
self-contained Steps 1-8 and my own exhaustive search.

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/pdf/2509.19303 | B. Bajnok, Report on the 63rd IMO (IMO 2022 P6 = grid version, answer 2n^2-2n+1, lower bound \|E\|+1) | background only: origin of the \|E\|+1 bound (Steps 1-4 of proof.md re-prove the identities used). Opened by the earlier C1 literature agent (inbox/earlier-C1-sources.md), not by me | PROVED (per C1 agent) | yes (per C1 agent) | NO (not by me) |
| https://link.springer.com/article/10.1007/s00373-003-0529-9 | D. A. Pike, "Decycling hypercubes", Graphs and Combinatorics 19 (2003) 547-550 | Search summary: "improved bounds for nabla(Q_n)"; "nabla(Q_n) = 2^(n-1) - A(n,4) if and only if Q_n has a minimum decycling set that consists of pairwise non-adjacent vertices", A(n,4) = max size of a binary code, length n, min distance 4. This is exactly the construction family of proof.md By-product (B) and the equality case of Step 6 | UNSURE (claimed PROVED in the paper; not read) | unknown | NO (egress blocked) |
| (IPL 76 (2000) 1-5; Wikidata Q57832155 https://www.wikidata.org/wiki/Q57832155) | R. Focardi, F. L. Luccio, D. Peleg, "Feedback vertex set in hypercubes", Information Processing Letters 76 (2000) 1-5 | bibliographic existence only (search summary); content (bounds on nabla(Q_n)) not seen | UNSURE | unknown | NO |
| https://www.researchgate.net/publication/245849970_Decycling_cubes_and_grids | S. Bau, L. W. Beineke, Z. Liu, G. Du, R. C. Vandell, "Decycling cubes and grids", Utilitas Mathematica (year not seen) | bibliographic existence only; presumably small values of nabla(Q_n) | UNSURE | unknown | NO (egress blocked) |
| https://ajc.maths.uq.edu.au/pdf/25/ajc-v25-p285.pdf | S. Bau, L. W. Beineke, "The decycling number of graphs", Australas. J. Combin. 25 (2002) 285-298 (survey) | bibliographic existence only | UNSURE | unknown | NO |
| (search-engine summary; no identifiable page) | unattributed: "for n <= 8 exact decycling numbers computed: nabla(Q_7) = 56, nabla(Q_8) = 112; nabla(Q_9) between 224 and 312" | would give U(Q_7) >= 464, U(Q_8) >= 1040 via proof.md Step 6 (matching out/Q7.txt, Q8.txt). NOT used. Note the quoted "312" upper bound for nabla(Q_9) is inconsistent with the explicit independent set of size 2^8 - A(9,4) = 236 (if A(9,4) = 20), so this summary is unreliable | UNSURE | unknown | NO |
| https://dgrozev.wordpress.com/2022/07/16/three-graph-problems-on-imo-2022-problem-6/ | D. Grozev, blog, 2022 | \|E\|+1 bound holds for any graph (per C1 agent) | PROVED (sketch, per C1 agent) | yes (per C1) | NO (not by me) |

## Own computations (these, not the table above, carry the proof)

| artefact | what | status |
|---|---|---|
| out/code/decycle.py 5 13 and out/code/brute13.c | no 13-vertex decycling set in Q_5 => nabla(Q_5) >= 14 (two independent programs) | COMPUTER-VERIFIED (code public: y, in out/code) |
| out/code/decycle.py 6 27 | no 27-vertex decycling set in Q_6 => nabla(Q_6) >= 28 (neighbour cell; single implementation) | COMPUTER-VERIFIED (code: y) |
| out/code/decycle.py 7 55 | nabla(Q_7) >= 56? | TIMED OUT at 590 s, nothing established |
| out/Q5.txt ... out/Q8.txt | labellings with 88, 204, 464, 1040 uphill paths (inbox/checker/verify.py) | COMPUTER-VERIFIED (checker) |

## Not found

Not found, in the sources searched, any statement of U(Q_d) for any d, any paper posing the hypercube
version of IMO 2022 P6, or any link between uphill paths and decycling numbers. Searched (web-search
engine only; fetches all blocked):
"uphill paths hypercube labelling minimum number valleys IMO 2022 Problem 6 generalization";
"\"uphill paths\" \"hypercube\" Nordic square";
"\"uphill paths\" graph labelling minimum \"hypercube\" OR \"n-cube\" \"IMO 2022\" generalization paper";
"decycling number hypercube Q_5 feedback vertex set exact values";
"\"decycling number\" hypercube \"A(n,4)\" pairwise non-adjacent minimum decycling set";
"Pike \"Decycling hypercubes\" Graphs and Combinatorics";
"decycling number of hypercube Q_n values n=5 14, n=6 28 Bau Beineke Focardi Luccio Peleg ...";
"maximum induced forest hypercube Q_n exact values induced forest n-cube";
"\"decycling\" hypercube \"Q_7\" OR \"Q_8\" OR \"Q_9\" exact value ...";
"Focardi Luccio Peleg \"Feedback vertex set in hypercubes\" ...".
OEIS could not be reached (oeis.org blocked). MathOverflow/AoPS not reachable on-site.
This is NOT a claim that the connection U(Q_d) >= 2^d + (d-1) nabla(Q_d) is new.

## Things called routine / computations with unavailable code
- Any published value of nabla(Q_n) for n >= 5 (Bau-Beineke-Liu-Du-Vandell; Pike) was presumably
  obtained by computer; code status unknown (papers not opened). Not relied on.
- The cell statement's "2368 <= U(Q_9)" lower bound is unpublished; unavailable; not used.
