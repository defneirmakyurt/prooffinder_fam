TASK: H-C4-001      ROLE: searcher      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 60 minutes
READ ONLY: run/tasks/H-C4-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C4-001/out/
TARGET: H-C4 "U(Q_7) and U(Q_8)" (5 points, checked instantly). Verbatim: "Two larger cubes: Q_7 has 128 vertices and 448 edges, Q_8 has 256 vertices and 1024 edges. Determine U(Q_7) and U(Q_8)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integers U(Q_7) and U(Q_8). For each d in {7, 8}, determining U(Q_d) = V means both halves: (a) an explicit labelling of Q_d with exactly V uphill paths, and (b) a proof (possibly computer-assisted) that every labelling of Q_d has at least V uphill paths. Both values are required.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: Q7.txt (128 lines, 7-character 0/1 strings) and Q8.txt (256 lines, 8-character strings); line i (1-based) is the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: priority is the upper half for BOTH d = 7 and d = 8: stop searching for better labellings of a given d once its best score has not improved across at least 3 independent restarts or methods; then spend the remaining time box on lower-bound evidence; stop at the time box in any case
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; artefacts list the vertices in increasing label order (line 1 = label 1), each a d-character 0/1 string with leading zeros; every score you report must be the output of the checker in inbox/checker/ on the exact file you hand in; compute: this machine has 4 cores shared by several workers; run at most one heavy process at a time, cap every invocation at 10 minutes wall time (use timeout), gcc/clang are available for inner loops; an unfinished or time-limited search is not a lower bound: label it SEARCH-FOUND-NOTHING / BEST-FOUND; a value is determined only with both an attaining labelling and a lower bound over all labellings
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, checker, library/H-uphill-checker
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

First write out/plan.md: TARGET as a ladder of numbered rungs (checker sanity, small cases,
reductions, search stages) with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Inbox holds checker/ (use it as your scoring function) and, if EXPLOIT, the lineage's best program and artefact.
Write a program that generates candidates; do not hand-craft objects.
Save: out/best.<ext> (artefact in the cell's required format), out/code/ (code + README.md),
out/runlog.md (method, seeds, restarts, measured runtime, best score per run),
out/claims.md (claim | status | where shown), out/stuck.md.
State whether any search was exhaustive and over exactly which class;
give the soundness argument for every symmetry reduction, written out in full.
A search over finitely many parameter values never proves a statement for all parameters.
A search that found nothing is SEARCH-FOUND-NOTHING, not a verification.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.

Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.

LIBRARY: inbox/library/<entry>/ holds verified material from the shared technique library; its ENTRY.md says what it is and how it was verified. Use it only if it helps. Copy any library file your code needs into out/code/ so the code runs on its own, and name the entry in claims.md for every claim that depends on it. A library lemma is an assumption: state it in full where you use it.

HAND-IN FILES: save your best labellings as out/Q7.txt and out/Q8.txt; for each d save at least one further labelling with the same best score that is structurally different (a different run, seed or method), as out/Q7_alt1.txt and out/Q8_alt1.txt, and record node/state counts and seeds for every run in out/runlog.md.
