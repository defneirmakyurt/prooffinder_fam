# Sources: H-L1-001 (literature, Phase 1L)

**Access situation in this run (important).** Every page fetch failed: WebFetch returned
`EGRESS_BLOCKED` for arxiv.org, web.evanchen.cc, dgrozev.wordpress.com, artofproblemsolving.com,
oeis.org, www.imo-official.org and en.wikipedia.org, and a direct `curl` of
https://arxiv.org/pdf/2509.19303 failed with `CONNECT tunnel failed, response 403`. No workaround was
attempted. Only the web-search tool worked, and it returns titles/URLs/snippets, which are **not**
sources. Consequently **no reference below was opened in this run**. Where the earlier literature run
(H-C1-006, inbox/earlier-sources.md) reports having opened a source, that is recorded separately and
marked as second-hand.

**Nothing in out/proof.md depends on any source.** The proof is self-contained (Steps 1-11): the
general bound P >= |E|+1, the equality analysis and the number-theoretic fact are all proved in full.

| link | reference (authors, title, year, theorem/table) | what was used | status | contains argument? | opened? |
|---|---|---|---|---|---|
| https://arxiv.org/pdf/2509.19303 | B. Bajnok, *Report on the 63rd Annual International Mathematical Olympiad*, arXiv:2509.19303 (2025), section on Problem 6 (Nordic square) | Attribution only: the lower-bound argument P >= 2n(n-1)+1 = |E|+1 for the grid and the equality condition "exactly one valley and ... no two adjacent cells are the last two cells of two different uphill paths". Re-proved in general form in proof.md Steps 5-7 | PROVED (for the n x n grid) per the earlier run | YES per the earlier run (full solution) | **NOT opened in this run** (egress 403). Earlier run H-C1-006 reports opening it and reading the Problem 6 section verbatim: second-hand |
| https://dgrozev.wordpress.com/2022/07/16/three-graph-problems-on-imo-2022-problem-6/ | D. Grozev, "Three Graph Problems on IMO 2022?! Problem 6.", blog post, 16 July 2022 | Attribution only: states the |E|+1 bound for an arbitrary simple graph (downhill-walk argument), per the earlier run's quotation | PROVED (informal sketch) per the earlier run | sketch only (termination of the downhill walk not argued, per the earlier run) | **NOT opened in this run** (egress blocked). Earlier run reports opening it via WebFetch: second-hand |
| https://artofproblemsolving.com/wiki/index.php/2022_IMO_Problems/Problem_6 | AoPS Wiki, "2022 IMO Problems/Problem 6" | nothing | UNSURE | unknown | **NOT opened** (egress blocked here; HTTP 403 in the earlier run as well) |
| https://web.evanchen.cc/exams/IMO-2022-notes.pdf | E. Chen, *IMO 2022 Solution Notes* (search result shows a version dated 4 May 2026), Problem 6 | nothing | UNSURE | unknown | **NOT opened** (egress blocked here; undecodable PDF in the earlier run) |
| https://www.imo-official.org/problems/IMO2022SL.pdf | IMO 2022 Shortlist with official solutions | nothing (tried in order to open an official write-up of the |E|+1 bound) | UNSURE | unknown | **NOT opened** (egress blocked) |
| https://www.researchgate.net/publication/395805857_Report_on_the_63rd_Annual_International_Mathematical_Olympiad | ResearchGate copy of Bajnok's report | nothing | UNSURE | unknown | not opened (seen only as a search hit) |
| https://arxiv.org/abs/1502.03146 ; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i2p15 | J. De Silva, T. Molla, F. Pfender, T. Retter, M. Tait, "Increasing paths in edge-ordered graphs: the hypercube and random graphs", Electron. J. Combin. 23(2) (2016) P2.15 | Neighbouring topic only (edge-orderings, longest increasing path, not counting paths from valleys under a vertex labelling). Not used | UNSURE (not opened; description from search snippet) | unknown | not opened |
| https://arxiv.org/pdf/2509.18931 | "Direct Paths in the Temporal Hypercube" (arXiv:2509.18931) | Neighbouring topic only (random edge weights, accessible paths to the antipode). Not used | UNSURE | unknown | not opened (search hit) |

## Number-theoretic fact (Step 8: k >= 2 does not divide 2^k - 1)

Proved in full in proof.md Step 8 using only the division algorithm, existence of a prime factor,
Euclid's lemma and the pigeonhole principle (no Fermat's little theorem needed). No citation is relied
on. The classical argument (least prime factor p, order of 2 mod p divides both k and p-1) is the one
sketched in the Remark of inbox/earlier-proof.md; I did not open any textbook or web source for it
(web-search query `"n divides 2^n - 1" only n = 1 proof smallest prime divisor order` returned only
generic handouts, none opened).

## Does any source state a lower bound for U(Q_d), or values of U(Q_d)?

**Not found** in the sources searched. This is not a claim that the question is new. The only
quantitative information about U(Q_d) that I have is the problem statement itself
(inbox/statement.md: "2368 <= U(Q_9) <= 2400; the lower bound is unpublished"), whose argument and
code are unavailable (flag: computation/argument not available).

Searches run in this session (web-search tool only; snippets, no page opened):
* `uphill paths hypercube labelling minimum number valleys IMO 2022 Problem 6 generalization`
* `"uphill paths" graph labelling "number of edges" lower bound valley arXiv`
* `"uphill paths" "hypercube"`
* `Nordic square generalization arbitrary graph "|E|+1" uphill paths equality one valley characterization`
* `IMO 2022 Problem 6 Nordic square hypercube "2368" OR "2400" uphill paths Q_9`
* `minimum number of uphill paths hypercube Q_d labelling vertices valley increasing paths`
* `mathoverflow minimum number of increasing paths starting at local minima vertex labelling graph hypercube`
* `"Nordic square" graph generalization regular graph "uphill" lower bound improvement "+2"`
* `"n divides 2^n - 1" only n = 1 proof smallest prime divisor order`
None of the returned hits (IMO 2022 P6 write-ups, edge-ordered increasing paths on Q_d, temporal
hypercube, fitness-landscape papers) mentions minimising the number of uphill paths of a vertex
labelling of Q_d. OEIS, MathOverflow and arXiv listing pages could not be fetched (egress blocked); the
earlier run's OEIS search for `5,14,34` and arXiv metadata search for "uphill path" (second-hand, see
inbox/earlier-sources.md) also found nothing relevant.

## Things a source calls routine but does not write down

* (second-hand, from the earlier run) Bajnok's construction lemma ends with "It is not hard to
  verify ...": construction side only, irrelevant here.
* (second-hand) Grozev's downhill walk: termination not argued. proof.md avoids the walk (Step 4 uses
  induction on the label instead).

## Computations whose code is unavailable

* The organisers' unpublished lower bound U(Q_9) >= 2368 (statement). Not used.
