TASK: H-L1-003      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: GATE   MODE: GATE   BRANCH: -
SUBJECT: H-L1-001
TIME BOX: 30 minutes
READ ONLY: run/tasks/H-L1-003/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-L1-003/out/
TARGET: H-L1 (promoted lemma; not a hand-in cell; the lower-bound half that C1–C4 would rest on).
Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: For every integer d >= 3 and every labelling f of Q_d, the number of uphill paths of f is at least d*2^(d-1) + 2. Equivalently: U(Q_d) >= |E(Q_d)| + 2 for every d >= 3.
Scope: all d >= 3 (not only tested values) and all labellings. d = 1, 2 are not claimed.
Requirements: a self-contained, line-by-line proof. Any general graph inequality used (for example a bound of the form U(G) >= |E(G)| + c) must be proved in full inside the proof, not only cited; any number-theoretic fact used must be proved or cited with an exact reference that states it. Any code used must be exact, included, and run in under 10 minutes.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when every checklist item and every proof step has a verdict with reasons
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of H-L1-001), checker
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
