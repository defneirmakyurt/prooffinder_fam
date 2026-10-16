TASK: H-C1-002      ROLE: checker-builder      REGIME: CLEAN-ROOM
PHASE: 0   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 20 minutes
READ ONLY: run/tasks/H-C1-002/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C1-002/out/
TARGET: H-C1 "U(Q_3) and U(Q_4)" (1 point, checked instantly). Verbatim: "The two smallest interesting cubes: Q_3 has 8 vertices and 12 edges, Q_4 has 16 vertices and 32 edges. Determine U(Q_3) and U(Q_4)." Definitions (labelling, valley, uphill path, U(G), Q_d) exactly as in inbox/statement.md.
Exact target: the integers U(Q_3) and U(Q_4). For each d in {3, 4}, determining U(Q_d) = V means both halves: (a) an explicit labelling of Q_d with exactly V uphill paths, and (b) evidence that every labelling of Q_d has at least V uphill paths.
Hand-in (verbatim): "the values, and for each value an explicit labelling that attains it as a list of the 2^d vertices in increasing label order, written as 0/1 strings."
Artefact format: a text file Q<d>.txt with exactly 2^d lines; line i (1-based) is the 0/1 string of length d of the vertex that gets label i.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/verify.py and out/tests.py are written and every test passes
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md
PYTHON: /Users/raducucu/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

From the statement alone, write out/verify.py: Python standard library only (fractions allowed),
exact arithmetic, reads the artefact format given in TARGET, prints VERIFIED + score,
or the exact reason for failure. Keep it short enough to read line by line.
Also write out/tests.py: hand-computed small cases plus a brute-force cross-check where feasible.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.

CHECKER SPEC (from the problem skill): input is a text file with exactly 2^d non-empty lines, each a 0/1 string of length d; line i (1-based) is the vertex with label i. d is inferred from the line length and must match an optional --d argument. Validation: every line has the same length d >= 1 and only the characters 0/1; exactly 2^d lines; all distinct; trailing whitespace and a final newline are tolerated, anything else is FAILED. Output: 'VERIFIED <count>' (exit 0) or 'FAILED: <reason>' (exit 1). Score: the number of uphill paths from the definitions (valleys, then every strictly increasing adjacent sequence starting at a valley, the single-vertex path included). Exact Python integers. Runtime: Q_9 well under 10 s. Tests: all labellings of Q_1 and Q_2 computed by hand (hand computation in comments), random permutations of {0,1}^d for d = 1..9 plus structured orders (lexicographic, reverse, by Hamming weight, Gray code), and a brute-force cross-check by explicit DFS path enumeration (small d) against the main count.
