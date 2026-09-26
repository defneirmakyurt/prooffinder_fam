TASK: A-C4-004      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: A-C4-003
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C4-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C4-004/out/
TARGET: Prove BOTH: (a) any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4*pi; (b) any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13*pi/2. Here S = sum over pairs i<j of theta(l_i, l_j), with theta(l, l') = arccos |<x, x'>| for spanning unit vectors (the acute angle, in [0, pi/2]). A computer-assisted step is allowed only with code included, runtime under 10 minutes on a laptop, exact or interval arithmetic (or a proved bound on the numerical error), and a written argument explaining why the computation proves the claim.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/verdict.md is complete with every checklist item answered
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of A-C4-003)
PYTHON: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
