TASK: H-C5-010      ROLE: searcher      REGIME: FRESH
PHASE: WAVE   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 75 minutes
READ ONLY: run/tasks/H-C5-010/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C5-010/out/
TARGET: H-C5 "Bounds for U(Q_9)" (8 points, judged). Verbatim: "Q_9 has 512 vertices and 2304 edges. The best bounds known to the organisers are 2368 <= U(Q_9) <= 2400; the lower bound is unpublished. Improve either one: prove that U(Q_9) >= 2369, or exhibit a labelling of Q_9 with at most 2399 uphill paths." Definitions exactly as in inbox/statement.md.
Exact target (either route suffices): (UPPER) an explicit labelling of Q_9 with at most 2399 uphill paths, handed in as Q9.txt: exactly 512 lines, line i (1-based) is the 9-character 0/1 string of the vertex that gets label i; or (LOWER) a proof, possibly computer-assisted, that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
Hand-in (verbatim): "either a labelling of Q_9 in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound."
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Lemma A (gated VALID, cell C4): for every d >= 1 and every labelling f of Q_d, with S = {v : down(v) >= 2}, V \ S induces a forest and f has >= 2^d + (d-1)|S| uphill paths; F_5 = 18 (exhaustive) and F_d <= 2F_{d-1}, where F_d = largest induced forest of Q_d. Statements and proofs: inbox/gated-lemmaA.md (sections A-D). Consequence you may use: if every induced forest of Q_9 has at most 279 vertices, then U(Q_9) >= 512 + 8*233 = 2376 >= 2369.
STOPPING CONDITION: stop when the Q_9 threshold 279 is proved with a certificate and a written reduction, or at the time box, reporting the smallest threshold proved (with certificate status) and where the solver stalled
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; compute: this machine has 4 cores shared by several workers; run at most one heavy process at a time, cap every invocation at 10 minutes wall time (use timeout); the FINAL certifying computation must run in under 10 minutes on a laptop; a SAT/ILP 'UNSAT' is a lower bound only with (a) a written reduction proving every valid object satisfies every constraint you add (implied constraints, symmetry breaking, cycle clauses), and (b) a checkable certificate (DRAT/LRAT proof checked by a checker, or an independently re-runnable exact computation); without both it is SEARCH-FOUND-NOTHING
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, checker, gated-lemmaA.md, gated-lb_forest.py
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

ANGLE: sat-ilp-lower + exhaustive-symbreak: a computer-assisted proof that every induced forest of Q_9 has at most 279 vertices. Encode 'Q_9 has an induced forest T with |T| >= 280' for a SAT solver (python-sat in the venv has CaDiCaL/Kissat/Glucose; some support proof logging) with VALID implied constraints: every subcube Q_k (k = 5..8, all positions) holds at most F_k vertices of T (F_5 = 18, F_6 <= 36, F_7 <= 72, F_8 <= 144), all 4-cycle clauses, lazy clauses for longer cycles (CEGAR), and sound symmetry breaking under Aut(Q_9) (order 2^9 * 9!). First validate the pipeline on small cases where the answer is known (F_6 <= 36, F_7 <= 72, F_8 <= 144), then push the Q_9 threshold down from 288 toward 279, recording the smallest threshold proved and the runtime of each step. Pursue this angle; if you abandon it, say why.

ROUTE: LOWER only. Hand-in if successful: out/proof.md (the reduction: why the constraints are valid, why the symmetry breaking is sound, why UNSAT proves the bound, and the chain to U(Q_9) >= 2369 via the gated Lemma A), out/code/ (encoder, solver driver, certificate check), out/runlog.md with exact commands and runtimes.
