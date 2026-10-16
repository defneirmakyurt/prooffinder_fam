TASK: H-C1-005      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: H-C1-004
TIME BOX: 30 minutes
READ ONLY: run/tasks/H-C1-005/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C1-005/out/
TARGET: H-C1 "U(Q_3) and U(Q_4)" (1 point, checked instantly). Verbatim: "The two smallest interesting cubes: Q_3 has 8 vertices and 12 edges, Q_4 has 16 vertices and 32 edges. Determine U(Q_3) and U(Q_4)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integers U(Q_3) and U(Q_4). For each d in {3, 4}, determining U(Q_d) = V means both halves: (a) an explicit labelling of Q_d with exactly V uphill paths, and (b) evidence that every labelling of Q_d has at least V uphill paths.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: a text file Q<d>.txt with exactly 2^d lines; line i (1-based) is the 0/1 string of length d of the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/verdict.md gives a verdict on the lower-bound argument with the 7-step checklist complete
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (claims.md, code of H-C1-004)
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Inbox holds TARGET, inbox/subject/ (proof.md, claims.md, code/), inbox/checklist-G.md and inbox/checklist-S.md.
You do not know who wrote the proof or how confident anyone is. Assume it may be wrong.
Run the 7-step protocol and write out/verdict.md:
1. Checklist pass: every item of Part G and Part S, PASS / FAIL / N/A with one line each.
   A FAIL on tightness, cases covered or statement match blocks ACCEPT.
2. Line-by-line re-derivation; list every unjustified, circular or false step.
   "Clearly / routine / obviously / similarly / by symmetry" are gaps unless written out.
3. Numerical sanity on random and extremal instances; run the code, record runtime; flag floating point inside a proof.
4. Equality-case test at the extremal configurations in Part S.
5. Cross-cell consistency with the verified cells listed in Part S.
6. Your own counterexample search, code in out/cex/.
7. Verdict ACCEPT / MINOR / MAJOR / WRONG. ACCEPT gives, for each step, the reason it holds.
You may write only out/verdict.md and out/cex/. Return the verdict block in section 4.

This subject is a COMPUTATIONAL claim, not a written proof. The object under evaluation is the argument that the computation establishes U(Q_4) >= 34 and U(Q_3) >= 14: the admissibility proof of the lower-bound function LB (claims.md, R5), the claim that the enumerated class is ALL (2^d)! bijections with no symmetry reduction, the exactness of the arithmetic, and the runtime. Re-run the programs yourself. Judge whether the written argument proves what the searched class is and why no labelling outside it needs checking; a search that is only asserted to be exhaustive is not.
