TASK: H-C5-004      ROLE: searcher      REGIME: EXPLOIT
PHASE: WAVE   MODE: -   BRANCH: -
SUBJECT: H-C5-002
TIME BOX: 60 minutes
READ ONLY: run/tasks/H-C5-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C5-004/out/
TARGET: H-C5 "Bounds for U(Q_9)" (8 points, judged). Verbatim: "Q_9 has 512 vertices and 2304 edges. The best bounds known to the organisers are 2368 <= U(Q_9) <= 2400; the lower bound is unpublished. Improve either one: prove that U(Q_9) >= 2369, or exhibit a labelling of Q_9 with at most 2399 uphill paths." Definitions exactly as in inbox/statement.md.
Exact target (either route suffices): (UPPER) an explicit labelling of Q_9 with at most 2399 uphill paths, handed in as Q9.txt: exactly 512 lines, line i (1-based) is the 9-character 0/1 string of the vertex that gets label i; or (LOWER) a proof, possibly computer-assisted, that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
Hand-in (verbatim): "either a labelling of Q_9 in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound."
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop as soon as the checker reports at most 2399 on a Q_9 labelling you saved (save it immediately as out/Q9.txt and report); otherwise stop at the time box, reporting the smallest decycling set size and the best checker score reached per run
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; artefacts list the vertices in increasing label order (line 1 = label 1), each a 9-character 0/1 string with leading zeros; every score you report must be the output of the checker in inbox/checker/ on the exact file you hand in; compute: this machine has 4 cores shared by several workers; run at most one heavy process at a time, cap every invocation at 10 minutes wall time (use timeout), gcc/clang are available
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, subject/ (proof.md, claims.md, code, Q9.txt of H-C5-002), checker, lineage-stuck.md, lineage-sources.md
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

Inbox holds the current best proof and its gate report or critique. Repair the listed problems first. If the approach cannot be repaired, say so and why.

ROUTE: UPPER only (a labelling of Q_9 with at most 2399 uphill paths). inbox/subject/ is this lineage's best (a labelling with 2400, its proof.md with the reduction, claims.md, code/); inbox/lineage-stuck.md is its record of where it stopped (dead ends and an observation about the structure of near-optimal decycling sets); inbox/lineage-sources.md is its literature map (references mostly unopened). The reduction in the subject's proof.md is NOT yet refereed: treat it as a search guide; the only score that counts is the checker's on your Q9 file. Save the best labelling as out/Q9.txt, and per run record method, seeds, moves, the smallest decycling set size and the checker score in out/runlog.md. A search that finds nothing is SEARCH-FOUND-NOTHING for the class searched, never a lower bound.
