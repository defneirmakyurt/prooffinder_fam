TASK: H-C2-002      ROLE: literature      REGIME: LITERATURE
PHASE: 1L   MODE: SOLVE   BRANCH: -
SUBJECT: -
TIME BOX: 40 minutes
READ ONLY: run/tasks/H-C2-002/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C2-002/out/
TARGET: H-C2 "U(Q_5)" (2 points, checked instantly). Verbatim: "Q_5 has 32 vertices and 80 edges. Determine U(Q_5)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integer U(Q_5). Determining U(Q_5) = V means both halves: (a) an explicit labelling of Q_5 with exactly V uphill paths, and (b) a proof (possibly computer-assisted) that every labelling of Q_5 has at least V uphill paths.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: a text file Q5.txt with exactly 32 lines; line i (1-based) is the 0/1 string of length 5 of the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when you have a labelling of Q_5 scored by the checker plus your literature map, or at the time box
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; artefacts list the vertices in increasing label order (line 1 = label 1), each a d-character 0/1 string with leading zeros; every score you report must be the output of inbox/checker/verify.py on the exact file you hand in; compute: this machine has 4 cores shared by several workers; run at most one heavy process at a time, cap every invocation at 10 minutes wall time (use timeout)
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, checker, earlier-C1-proof.md, earlier-C1-sources.md
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

EARLY 1L: the Phase 1 blind searcher for this cell is still running, so inbox/earlier/ is empty; write divergence.md against inbox/earlier-C1-proof.md (an earlier literature-agent proof of U(Q_3) = 14, U(Q_4) = 34 whose closing Remark claims U(Q_d) >= d*2^(d-1)+2 for all d >= 3; that general claim is under separate review and is NOT established). Focus: (1) the literature on uphill paths in graphs and specifically on the hypercube: any stated values, bounds or constructions of U(Q_d) for d = 5..9, with where each is proved (sources.md, status-tagged); (2) a construction, found with known techniques and code, of a labelling of Q_5 with as few uphill paths as possible, handed in as out/Q5.txt (line i = vertex with label i) with the checker's count, and any general-d construction pattern you find (with its checker counts for d = 5..8 as out/Q<d>.txt if you build them); (3) lower-bound status for d = 5.
