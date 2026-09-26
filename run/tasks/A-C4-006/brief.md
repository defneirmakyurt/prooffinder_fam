TASK: A-C4-006      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/A-C4-006/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C4-006/out/
TARGET: A-C4 "Five Lines in R^3, Six in R^4" (5 points, written proof). Verbatim: "Two concrete instances of the next case, N = d + 2: five lines in three dimensions and six lines in four. In each, the conjectured optimum repeats two of the coordinate axes. Prove that any 5 lines in R^3 satisfy S <= 4 pi, and that any 6 lines in R^4 satisfy S <= 13 pi/2." Exact target: (a) any 5 lines through the origin of R^3 (repetitions allowed) satisfy S <= 4 pi; (b) any 6 lines through the origin of R^4 (repetitions allowed) satisfy S <= 13 pi/2; S = sum over pairs of theta = arccos|<x, x'>| for spanning unit vectors (the acute angle, in [0, pi/2]). Both instances are required. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/submission.md is complete in the hand-in format.
LESSONS: role-lessons.md v2, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v2, problem-lessons.md v0, statement.md, target.md, checklist-G.md, accepted
PYTHON: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
PARTIAL lists the claims established and the exact remaining gap. Add no claim that is not in the accepted artefacts.

CELL STATUS: SOLVED
CLAIM STATUS (do not upgrade): PROVED
