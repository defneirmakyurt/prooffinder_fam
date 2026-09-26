TASK: H-C3-001      ROLE: searcher      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 45 minutes
READ ONLY: run/tasks/H-C3-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C3-001/out/
TARGET: H-C3 "U(Q_6)" (3 points, checked instantly). Verbatim: "Q_6 has 64 vertices and 192 edges. Determine U(Q_6)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integer U(Q_6). Determining U(Q_6) = V means both halves: (a) an explicit labelling of Q_6 with exactly V uphill paths, and (b) a proof (possibly computer-assisted) that every labelling of Q_6 has at least V uphill paths.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: a text file Q6.txt with exactly 64 lines; line i (1-based) is the 0/1 string of length 6 of the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: priority is the upper half: stop searching for better labellings once your best score has not improved across at least 3 independent restarts or methods; then spend the remaining time box on lower-bound evidence; stop at the time box in any case
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

HAND-IN FILES: save your best labelling as out/Q6.txt and an identical copy as out/best.txt; save at least one further labelling with the same best score that is structurally different (a different run, seed or method), as out/Q6_alt1.txt, and record node/state counts and seeds for every run in out/runlog.md.
