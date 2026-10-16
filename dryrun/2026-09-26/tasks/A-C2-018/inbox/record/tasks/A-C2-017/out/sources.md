# Sources: A-C2 (Orthogonality Lemma), analyst task A-C2-017

ACCESS NOTE (measured this task, 2026-09-26): every fetch was refused by the egress proxy. WebFetch gave EGRESS_BLOCKED for
arxiv.org, www.math.utoronto.ca, par.nsf.gov, www.ams.org, en.wikipedia.org, ui.adsabs.harvard.edu, arxiv-vanity.com,
www.sciencedirect.com and experts.umn.edu. curl gave CONNECT 403 for arxiv.org and export.arxiv.org.
So **no source was opened**. Every row is `not opened`. Its content column only repeats a search-result snippet or
background knowledge, and is UNSURE. None of these sources is used as a step in out/proof.md. The proof cites nothing.

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/abs/1801.07837 (journal: https://www.ams.org/journals/proc/2019-147-01/S0002-9939-2018-14263-X/) | D. Bilyk, R. W. Matzke, "On the Fejes Tóth problem about the sum of angles between lines", Proc. AMS 147 (2019) | Context only. Snippet: only the case d = 1 (lines in the plane) of the conjecture is settled; the paper gives upper bounds. No chain lemma seen in the snippet | UNSURE (theorem numbers not seen) | unknown | not opened (blocked) |
| https://arxiv.org/abs/2007.08698 | T. Lim, R. J. McCann, "On Fejes Tóth's conjectured maximizer for the sum of angles between lines", Appl. Math. Optim. (2021) | Context only. Snippet: the conjecture is embedded in an alpha-power family; optimality and uniqueness proved at alpha = infinity | UNSURE | unknown | not opened (blocked) |
| https://link.springer.com/article/10.1007/s00013-015-0847-1 | F. Fodor, V. Vígh, T. Zarnócz, "On the angle sum of lines", Arch. Math. 106 (2016) 91–100 | Context only. Snippet: recursive upper bound on the angle sum; Fejes Tóth's n <= 6 case in R^3 | UNSURE | unknown | not opened (blocked) |
| https://arxiv.org/pdf/2007.13052 | "Maximizing expected powers of the angle between pairs of points in projective space" (authors not seen) | Appeared in searches; neighbour problem (continuous version). Not used | UNSURE | unknown | not opened (blocked) |
| https://arxiv.org/abs/2511.02864 | "Mathematical exploration and discovery at scale" (2025) | Appeared in a search for the Fejes Tóth angle sum. Relevance unknown | UNSURE | unknown | not opened (blocked) |
| https://www.sciencedirect.com/science/article/pii/S0021904596931093 | R. Szwarc, "Chain sequences, orthogonal polynomials, and Jacobi matrices", J. Approx. Theory (1998) | Background technique only. From memory, UNSURE: Wall–Wetzel, a unit-diagonal Jacobi matrix with off-diagonals b_i is positive definite iff (b_i^2) is a chain sequence. The ratio recursion t_{k+1}^2 = 1 - c_k^2/t_k^2 in proof.md is the finite form of this. Not needed: proof.md derives it directly | UNSURE | unknown | not opened (blocked) |
| (book) | T. S. Chihara, "An Introduction to Orthogonal Polynomials", Gordon and Breach (1978), chapter on chain sequences | Background only (same Wall–Wetzel criterion), from memory | UNSURE | unknown | not opened |
| (earlier work) | inbox/earlier/A-C2-003/sources.md | The previous literature pass hit the same blocks and found the same set; this table extends it | n/a | n/a | opened (local) |

## Queries run this task (WebSearch)
1. "Fejes Tóth sum of angles between lines d+1 lines proof" -> Bilyk–Matzke, Lim–McCann, Fodor–Vígh–Zarnócz.
2. "\"sum of angles\" lines Fejes Tóth conjecture \"d+2\" OR \"d+1\" lines proved 2025 2026 arXiv" -> the same papers plus unrelated Fejes Tóth problems (zone conjecture, sausage, six circles). No 2025–26 result on N = d+1 lines was seen.
3. "tridiagonal Gram matrix unit vectors orthogonal non-adjacent sum arcsin off-diagonal at least pi/2 singular" -> nothing relevant.
4. "Jacobi matrix positive definite if sum of arcsin of off-diagonal entries less than pi/2 continued fraction chain sequence" -> chain-sequence background only (Szwarc 1998; Wikipedia "Chain sequence").
5. "\"unit vectors\" \"whenever |i-j| \geq 2\" angles sum lemma lines Fejes Tóth N=d+1 ..." -> the same Fejes Tóth papers only.
6. "mathoverflow sum of angles between d+1 lines in R^d maximum Fejes Toth" -> no MathOverflow thread; the same papers.

Conclusion: the cell's statement as a stand-alone lemma (and the arcsin form "sum arcsin|c_i| < pi/2 implies the
unit-diagonal tridiagonal matrix is positive definite") was **not found in** the sources and queries above. Since nothing
could be opened, this says nothing about novelty. The cell's status rests entirely on the written proofs (PROVED in-team:
A-C2-002, gate VALID; also A-C2-011; and out/proof.md here), not on any citation.
