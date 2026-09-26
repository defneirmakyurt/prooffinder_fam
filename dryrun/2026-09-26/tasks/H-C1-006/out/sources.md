# Sources: H-C1-006

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/pdf/2509.19303 | Bela Bajnok, *Report on the 63rd Annual International Mathematical Olympiad*, arXiv:2509.19303 (2025; also Amer. Math. Monthly-style report). Section "Problem 6 (22; 2; 3; 19; 7; 22; 80; 434; 0.68); proposed by Serbia", statement + "Solution" + "Lemma" | The exact IMO 2022 P6 statement (Nordic square, valley, uphill path -- identical definitions to inbox/statement.md restricted to the grid); the answer 2n^2-2n+1; the lower-bound argument "at least one valley ... 2n(n-1) pairs of adjacent cells ... at least 2n(n-1)+1"; and the equality condition "exactly one valley and ... no two adjacent cells are the last two cells of two different uphill paths". This is the |E|+1 bound and the equality analysis that out/proof.md Steps 5-6 re-prove and then push further | PROVED | YES -- the full solution, both bounds, with the construction lemma proved | YES. Fetched the PDF, decompressed the content streams locally and read the Problem 6 section verbatim (out/tmp/bajnok_clean.txt) |
| https://dgrozev.wordpress.com/2022/07/16/three-graph-problems-on-imo-2022-problem-6/ | Dimitar Grozev, "Three Graph Problems on IMO 2022?! Problem 6.", blog post, 2022 | Confirms the lower bound is a general-graph statement: "Fix a directed edge and start walking downward until reach a root ... the number of up-paths that consist of at least an edge is at least the number of edges. Further, there is at least one root ... Therefore the number of up-paths are at least |E|+1", and "This is true for any simple graph" | PROVED (informal write-up of a correct argument) | YES for the lower bound (sketch level: the downhill walk is not argued to terminate, and termination is immediate only because labels strictly decrease) | YES (via WebFetch; the quoted passage was returned from the page) |
| https://artofproblemsolving.com/wiki/index.php/2022_IMO_Problems/Problem_6 | AoPS Wiki, "2022 IMO Problems/Problem 6" | Would be a second write-up of the same solution | PROVED (per search snippets: answer 2n^2-2n+1, lower bound 1+|E|) | unknown | **NO -- HTTP 403 Forbidden on fetch.** Only search snippets seen. Not relied on for anything |
| https://web.evanchen.cc/exams/IMO-2022-notes.pdf | Evan Chen, *IMO 2022 Solution Notes*, Problem 6 | Would be a second independent write-up | UNSURE (not read) | unknown | **NO** -- the PDF downloaded but its text is stored with subsetted font encodings that I could not decode with the tools available offline (no pdftotext/mutool/pypdf in the environment). Not relied on for anything |
| https://oeis.org/search?q=2,5,14,34 and https://oeis.org/search?q=5,14,34 | OEIS | Searched for the sequence U(Q_d) = ... , 5, 14, 34, ... (U(Q_2)=5 is a sanity value, not part of the cell) | not found | n/a | YES (search pages fetched) -- hits returned (A080934, A122881, A265226, A374699, A182738, A228660, A023515, A094584, A083332, A284415, A384651) are about Catalan paths, compositions, primes etc.; **none** concerns uphill paths, valleys, hypercube labellings or IMO 2022 |
| http://export.arxiv.org/api/query?search_query=all:%22uphill%20path%22 | arXiv API metadata search, phrase "uphill path", 40 results requested | Looking for any paper on minimising uphill paths of a vertex labelling | not found | n/a | YES -- the only hit is Ochs & Desai, *The competition between simple and complex evolutionary trajectories in asexual populations* (2014), about fitness landscapes, unrelated |

## Not found

I did **not** find, in any source, a determination of U(Q_d) for any d, nor any paper or post that
poses the hypercube version of IMO 2022 Problem 6. Sources searched and queries used:

* Web search (Anthropic web_search): "IMO 2022 Problem 6 uphill paths valley minimum number solution";
  "\"uphill paths\" hypercube labelling minimum valley graph";
  "arXiv generalization IMO 2022 Problem 6 uphill paths arbitrary graphs minimum number of uphill paths";
  "\"Nordic square\" generalization graph \"number of uphill paths\" hypercube open problem";
  "\"uphill paths\" minimum labelling graph \"n-cube\" OR \"hypercube\" generalization IMO 2022 P6 AoPS";
  "mathoverflow OR math.stackexchange minimum number of uphill paths general graph \"|E|+1\" valleys labelling".
* arXiv metadata full search for the phrase "uphill path" (API, 40 results).
* OEIS, queries `5,14,34` and `2,5,14,34`.
* DuckDuckGo HTML endpoint -- **blocked by a CAPTCHA**, returned nothing.
* Google web search endpoint -- **blocked by a consent redirect**, returned nothing.
* MathOverflow / math.stackexchange were only reached through the web-search engine above, not
  searched on-site; this is a gap.

So: "not found in the sources searched" (web search, arXiv metadata search, OEIS, one blog, the IMO
report). This is **not** a claim that the hypercube question is new or unstudied.

## Things a source calls routine but does not write down

* Bajnok's Lemma (the tree/marking construction) ends "It is not hard to verify that this
  construction works" for the m = 6q juxtaposition and the row-deletion cases. Not written down
  there. This affects only the grid construction, which is **not used** anywhere in out/proof.md.
* Grozev's blog states the downhill walk "start walking downward until reach a root" without arguing
  termination. Irrelevant here: out/proof.md Step 5 proves the same bound by a different route
  (Steps 1-4) with no walk.

## Computations whose code is unavailable

* None relied on. The cell's own statement reports bounds 2368 <= U(Q_9) <= 2400 with the lower
  bound "unpublished" -- by definition its code and argument are unavailable to me; I use neither.
