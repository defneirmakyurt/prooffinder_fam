TASK: H-C1-004      ROLE: searcher      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 30 minutes
READ ONLY: run/tasks/H-C1-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C1-004/out/
TARGET: H-C1 "U(Q_3) and U(Q_4)" (1 point, checked instantly). Verbatim: "The two smallest interesting cubes: Q_3 has 8 vertices and 12 edges, Q_4 has 16 vertices and 32 edges. Determine U(Q_3) and U(Q_4)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integers U(Q_3) and U(Q_4). For each d in {3, 4}, determining U(Q_d) = V means both halves: (a) an explicit labelling of Q_d with exactly V uphill paths, and (b) evidence that every labelling of Q_d has at least V uphill paths.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: a text file Q<d>.txt with exactly 2^d lines; line i (1-based) is the 0/1 string of length d of the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/Q3.txt and out/Q4.txt are scored by the provided checker and, for each d, either the lower-bound search is complete or you have written exactly why it is not; or at the time box
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; C1 is marked on the values alone, but each value needs an explicit attaining labelling; a computer-assisted lower bound must include the code, run under 10 minutes on a laptop, and come with a written explanation of why the computation proves the bound
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, checker
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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

ARTEFACTS FOR THIS CELL: save the two labellings as out/Q3.txt and out/Q4.txt (these are the cell's out/best.<ext> files), each scored with inbox/checker/verify.py.
