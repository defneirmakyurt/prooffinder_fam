TASK: H-C4-002      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: H-C4-001
TIME BOX: 35 minutes
READ ONLY: run/tasks/H-C4-002/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C4-002/out/
TARGET: H-C4 "U(Q_7) and U(Q_8)" (5 points, checked instantly). Verbatim: "Two larger cubes: Q_7 has 128 vertices and 448 edges, Q_8 has 256 vertices and 1024 edges. Determine U(Q_7) and U(Q_8)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integers U(Q_7) and U(Q_8). For each d in {7, 8}, determining U(Q_d) = V means both halves: (a) an explicit labelling of Q_d with exactly V uphill paths, and (b) a proof (possibly computer-assisted) that every labelling of Q_d has at least V uphill paths. Both values are required.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: Q7.txt (128 lines, 7-character 0/1 strings) and Q8.txt (256 lines, 8-character strings); line i (1-based) is the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when every checklist item and every step of sections A, B, C, D has a verdict with reasons
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (claims.md, code, Q7.txt, Q8.txt of H-C4-001), checker
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

SCOPE: in addition to the TARGET (d = 7, 8), also check the subject's claim C10 for d = 5 and d = 6 only (U(Q_5) >= 88 and U(Q_6) >= 204 from the same Lemma A, Lemma C and the exhaustive F_5 computation), and report it as a separate line in your verdict: 'C10 (d=5,6): ACCEPT/MINOR/MAJOR/WRONG — reason'. The d = 2..4 parts of C10 need not be checked.
