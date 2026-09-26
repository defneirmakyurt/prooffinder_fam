TASK: H-L1-001      ROLE: literature      REGIME: LITERATURE
PHASE: 1L   MODE: SOLVE   BRANCH: -
SUBJECT: -
TIME BOX: 35 minutes
READ ONLY: run/tasks/H-L1-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-L1-001/out/
TARGET: H-L1 (promoted lemma; not a hand-in cell; the lower-bound half that C1–C4 would rest on).
Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: For every integer d >= 3 and every labelling f of Q_d, the number of uphill paths of f is at least d*2^(d-1) + 2. Equivalently: U(Q_d) >= |E(Q_d)| + 2 for every d >= 3.
Scope: all d >= 3 (not only tested values) and all labellings. d = 1, 2 are not claimed.
Requirements: a self-contained, line-by-line proof. Any general graph inequality used (for example a bound of the form U(G) >= |E(G)| + c) must be proved in full inside the proof, not only cited; any number-theoretic fact used must be proved or cited with an exact reference that states it. Any code used must be exact, included, and run in under 10 minutes.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/proof.md proves the TARGET for every d >= 3 with every step written out, or when the same step fails twice (then report the exact failing step in stuck.md and prove the strongest correct statement you can)
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; an unfinished or time-limited search is not a lower bound: label it SEARCH-FOUND-NOTHING / BEST-FOUND; a value is determined only with both an attaining labelling and a lower bound over all labellings
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier-proof.md, earlier-divergence.md, earlier-sources.md, earlier-gate-report.md
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.

Phase 1L. Inbox/earlier/ holds the Phase 1 blind results for this cell.
1. Find the literature for this cell and its neighbours, with links (out/sources.md: link, what was used, status).
2. Attempt the cell using known techniques (out/proof.md, out/claims.md).
3. Compare with the blind solvers: where do approaches differ or contradict? (out/divergence.md).
   Record which ideas came from the blind run, which from literature, and which are new here.
Blind and literature results are compared, never merged.

PROMOTED LEMMA (no Phase 1 blind results exist for it; inbox/earlier/ is empty by design). inbox/earlier-proof.md is an earlier literature-agent proof, for d = 3 and d = 4 only, of U(Q_3) = 14 and U(Q_4) = 34; its closing Remark sketches how the same argument would give the TARGET for every d >= 3. inbox/earlier-gate-report.md is its gate report (one referee ACCEPT for d = 3, 4; never refereed for general d). inbox/earlier-divergence.md and inbox/earlier-sources.md record which ideas were cited and which were new; two of those sources could not be opened (HTTP 403 / undecodable PDF). Your jobs: (1) open and verify the sources, recording in out/sources.md exactly what each one states and proves, and whether any source already states a lower bound for U(Q_d) or values of U(Q_d); (2) write out/proof.md, a clean, self-contained, line-by-line proof of the TARGET for general d >= 3, ready for two independent referees: prove every general inequality you use in full (a citation alone is not enough), prove or exactly cite every number-theoretic fact, and cover every case of every equality analysis; (3) out/divergence.md: what is cited, what is from the earlier proof, what is new. If the Remark's extension is wrong or incomplete for some d, say exactly where in out/stuck.md.
