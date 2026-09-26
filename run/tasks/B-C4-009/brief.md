TASK: B-C4-009      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: GATE   MODE: GATE   BRANCH: -
SUBJECT: B-C4-007
TIME BOX: 25 minutes
READ ONLY: run/tasks/B-C4-009/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C4-009/out/
TARGET: LOWER half of B-C4 (the target says the halves are gated separately): for EVERY k >= 5, the explicit partition lambda^(k) = (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1) of n = T_{k-1} + 1 satisfies d_B(lambda^(k)) = (k-1)(k-3), with its orbit tracked symbolically in k; hence D_B(T_{k-1} + 1) >= (k-1)(k-3) for every k >= 5. Definitions exactly as in inbox/statement.md.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/verdict.md is complete with every checklist item answered
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of B-C4-007)
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

This gate is for the LOWER half only. Judge whether the proof establishes the TARGET above (lambda^(k) is a partition of T_{k-1}+1 and d_B(lambda^(k)) = (k-1)(k-3) exactly, for every k >= 5). Checklist items that concern only the UPPER half are N/A for this verdict (say so in one line each); the upper half will be gated separately. Any other claim in the proof (partial upper bounds) is outside this target: note problems with it under OTHER ISSUES, but they do not decide this verdict.
