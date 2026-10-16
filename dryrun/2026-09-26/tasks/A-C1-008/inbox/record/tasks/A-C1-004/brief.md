TASK: A-C1-004      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: A-C1-001
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C1-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C1-004/out/
TARGET: A-C1 "Lines in the Plane" (1 point, written proof). Verbatim: "We begin in the plane (d = 2), where the conjectured optimum splits the N lines as evenly as possible between two perpendicular directions. Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4)."
Exact target: for every N and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') in [0, pi/2] is the acute (non-obtuse) angle between the lines, theta = arccos|<x, x'>| for spanning unit vectors x, x'. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/verdict.md holds the full 7-step protocol and the verdict
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; citing a published result for the statement being proved does not count
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of A-C1-001)
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
