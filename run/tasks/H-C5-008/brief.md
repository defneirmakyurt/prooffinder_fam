TASK: H-C5-008      ROLE: searcher      REGIME: CONTRARIAN
PHASE: WAVE   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 75 minutes
READ ONLY: run/tasks/H-C5-008/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C5-008/out/
TARGET: H-C5 "Bounds for U(Q_9)" (8 points, judged). Verbatim: "Q_9 has 512 vertices and 2304 edges. The best bounds known to the organisers are 2368 <= U(Q_9) <= 2400; the lower bound is unpublished. Improve either one: prove that U(Q_9) >= 2369, or exhibit a labelling of Q_9 with at most 2399 uphill paths." Definitions exactly as in inbox/statement.md.
Exact target (either route suffices): (UPPER) an explicit labelling of Q_9 with at most 2399 uphill paths, handed in as Q9.txt: exactly 512 lines, line i (1-based) is the 9-character 0/1 string of the vertex that gets label i; or (LOWER) a proof, possibly computer-assisted, that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
Hand-in (verbatim): "either a labelling of Q_9 in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound."
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Lemma A (gated VALID, cell C4, two referee ACCEPTs): for every d >= 1 and every labelling f of Q_d, with S = {v : down(v) >= 2}, the set V \ S induces a forest of Q_d and f has at least 2^d + (d-1)|S| uphill paths; also F_5 = 18 and F_d <= 2F_{d-1} (F_d = largest induced forest of Q_d). Full statements and proofs: inbox/gated-lemmaA.md (sections A-D; its 'Construction principle' section is not gated).
STOPPING CONDITION: stop as soon as the checker reports at most 2399 on a Q_9 labelling you saved (save it immediately as out/Q9.txt and report); otherwise stop at the time box, reporting per run the largest induced forest (smallest decycling set) and best checker score reached
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d; artefacts list the vertices in increasing label order (line 1 = label 1), each a 9-character 0/1 string with leading zeros; every score you report must be the output of the checker in inbox/checker/ on the exact file you hand in; compute: this machine has 4 cores shared by several workers; run at most one heavy process at a time (CP-SAT: at most 2 search workers), cap every invocation at 10 minutes wall time (use timeout)
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, checker, gated-lemmaA.md
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

FORBIDDEN APPROACHES (already tried, do not use):
- [parity split, clique cover] lower route: clique-cover bound for tau(G_2[F∩E]) closes only z <= 3 missing vertices of one parity; general forest bound F_9 <= 279 open (R9) (H-C5-007)
- [feedback-vertex-set reduction] upper route: SAT (12 symmetry groups, K=235: UNSAT or timeout, no DRAT) and local search on (independent / non-independent) FVS never below |S|=236; best 2400 (H-C5-001)
- [multiway-cut SA, clusters] upper route: multiway-cut SA (9 runs d=9) and symmetric penalty SA never below |S|=236; no net-2 cluster with <= 6 words (exhaustive up to symmetry); best 2400 (H-C5-003)
- [cluster-value decomposition search] upper route: recursive-product / near-parity SAT-CEGAR, 10 symmetric classes, SAT-LNS regions and SA never below |S|=236; best 2400 (H-C5-005)
- [SAT-LNS symmetric forests] upper route: SAT on forests invariant under 9/7/5-cycles of coordinates UNSAT (no DRAT), 3-cycle classes timed out; SA/LNS plateau at |S|=236; Q_8xK_2 with perfect-code halves caps at 272 vertices; best 2400 (H-C5-004)
- [parity/code construction] upper route: S inside one parity class (even words minus a distance-4 code) gives |S| = 256 - |code| >= 236 (A(9,4) = 20); SA on induced forests of Q_9 (7 runs) and labelling-level SA seeded at 2400 never below 236 / 2400 (H-C5-002)
- [fixed-size forest SA] upper route: fixed-size penalty SA for a 277-vertex induced forest of Q_9 (3 runs x 3e7 moves) and C9-symmetric CEGAR (timed out) found none; lower route: counting, halving, subcube averaging, spectral and 4-cycle bounds stop at nabla(Q_9) >= 225 (H-C5-006)

ROUTE: UPPER only. By the gated Lemma A, a labelling with <= 2399 paths needs |S| <= 235, i.e. an induced forest of Q_9 with >= 277 vertices; and every decycling set S with no edge inside it has >= 236 vertices (dead-end list), so the forest you need must leave at least one edge inside S. Save the best labelling as out/Q9.txt; record per run the model, solver parameters, seed, bound reached and runtime in out/runlog.md.
