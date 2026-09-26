# Sources for A-C2 (Orthogonality Lemma)

ACCESS NOTE: every fetch failed. WebFetch returned EGRESS_BLOCKED for arxiv.org, ar5iv.labs.arxiv.org, www.math.utoronto.ca,
publicatio.bibl.u-szeged.hu, link.springer.com, www.semanticscholar.org. Bash curl got CONNECT 403 from the proxy for every host
tried (export.arxiv.org, mathoverflow.net, oeis.org, zbmath.org, api.crossref.org, api.openalex.org, scholar.google.com, ...).
Only WebSearch result snippets were seen. A snippet is not a source, so every row below is `not opened` and the "what it says"
column is only what the search snippet suggested (UNSURE until opened). No row is used as a step of the proof in proof.md.

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/abs/1801.07837 | D. Bilyk, R. W. Matzke, "On the Fejes Tóth problem about the sum of angles between lines", Proc. AMS (2019); arXiv 2018 | Context only: snippet says the conjecture is settled only for d = 1 (plane) and gives new upper bounds. Whether it contains a chain / orthogonality lemma: UNSURE | UNSURE (theorem numbers not seen) | unknown | not opened (blocked) |
| https://arxiv.org/abs/2007.08698 | T. Lim, R. J. McCann, "On Fejes Tóth's conjectured maximizer for the sum of angles between lines", Appl. Math. Optim. (2021) | Context only: snippet says optimality and uniqueness proved in the limiting case alpha = infinity of a Riesz-type family | UNSURE | unknown | not opened (blocked) |
| https://link.springer.com/article/10.1007/s00013-015-0847-1 | F. Fodor, V. Vígh, T. Zarnócz, "On the angle sum of lines", Arch. Math. 106 (2016) 91–100 | Context only: snippet says Fejes Tóth's recursive bound S(n,d) <= n S(n-1,d)/(n-2) extended to all d; Fejes Tóth solved n <= 6 in R^3 | UNSURE | unknown | not opened (blocked) |
| http://www.math.uni.wroc.pl/~szwarc/pdf/chain.pdf (also https://www.sciencedirect.com/science/article/pii/S0021904596931093) | R. Szwarc, "Chain sequences, orthogonal polynomials, and Jacobi matrices", J. Approx. Theory (1998) | Background technique only: chain sequences (Wall) and positive definiteness of Jacobi (tridiagonal) matrices, i.e. the recursion t_{k+1}^2 = 1 - a_k^2/t_k^2 behind proof.md Step 1. proof.md re-derives what it needs and cites nothing | UNSURE (as to exact statements) | unknown | not opened (not attempted after blanket blocks; host likely blocked) |
| (book, no link) | T. S. Chihara, "An Introduction to Orthogonal Polynomials" (1978), chapter on chain sequences | Background only (Wall–Wetzel criterion for positive definite Jacobi matrices, per snippet) | UNSURE | unknown | not opened |
| https://arxiv.org/abs/2511.02864 | "Mathematical exploration and discovery at scale" (2025) | Appeared in a search for Fejes Tóth angle sums. Relevance UNKNOWN; not checked | UNSURE | unknown | not opened (blocked) |

## Searches run (WebSearch), and what they found
1. "Fejes Tóth sum of angles between lines d+1 lines proof arXiv": Bilyk–Matzke, Lim–McCann only.
2. "unit vectors x_i orthogonal whenever |i-j|>=2 sum of angles consecutive at most (m-2)pi/2 lemma": nothing relevant.
3. "\"sum of angles\" lines \"d+1 lines\" Fejes Tóth conjecture proved 2024 OR 2025": nothing new beyond 1–2.
4. "Fejes Tóth angle sum conjecture N = d+1 lines resolved orthogonality lemma chain tridiagonal Gram": nothing new.
5. "\"sum of angles between lines\" arXiv 2025": Pinelis arXiv 2508.04759 (three vectors, unrelated); nothing on this lemma.
6. "Fejes Tóth sum of angles conjecture \"d+1\" lines proof new 2026": nothing.
7. "Fodor Vígh Zarnócz angle sum of lines Fejes Tóth": Arch. Math. 2016 paper.
8. "\"Fejes Tóth\" \"sum of angles\" \"N = d + 1\" OR \"d+1 lines\" ... orthogonal consecutive vectors": nothing new.
9. "tridiagonal Gram matrix singular unit diagonal off-diagonal sin phi_i sum phi_i >= pi/2 lemma": nothing relevant.
10. "chain sequence Wall positive definite Jacobi matrix ... Chihara": Szwarc 1998; Wall–Wetzel criterion (snippet).

Conclusion: the statement of cell A-C2, as a stand-alone lemma, was not found in the sources and queries listed above.
This does not mean it is new: the sources could not be opened. Status of the cell statement itself: PROVED here (proof.md), not by citation.
