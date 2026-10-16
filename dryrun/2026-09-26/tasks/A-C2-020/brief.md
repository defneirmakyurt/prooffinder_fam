TASK: A-C2-020      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 20 minutes
READ ONLY: run/tasks/A-C2-020/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C2-020/out/
TARGET: A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/submission.md is complete in the hand-in format below.
LESSONS: role-lessons.md v2, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v2, problem-lessons.md v0, statement.md, target.md, checklist-G.md, accepted
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
PARTIAL lists the claims established and the exact remaining gap. Add no claim that is not in the accepted artefacts.

CELL STATUS: SOLVED
CLAIM STATUS (do not upgrade): PROVED

HAND-IN FORMAT (official, verbatim): "For each cell you attempt, hand in a written proof. Computation. You may use a computer to explore. A proof may rely on a computation only if you include the code, it runs in under 10 minutes on a laptop, and it is rigorous: exact or interval arithmetic, or an argument that bounds the numerical error. Status. Say clearly which cells you consider solved and which are partial." The cell is judged by humans reading the proof; it is submitted through a web form with a text field, so out/submission.md must be self-contained plain Markdown with LaTeX math (\( \), \[ \]), readable top to bottom: statement, status line (A-C2 SOLVED; claim PROVED), a note that no published result is cited and no computation is used, then the complete proof from inbox/accepted/proof.md, rewritten only for readability (same steps, same order, nothing added). Keep internal task ids, file paths and agent names out of the text a judge reads; put them in out/provenance.md instead.
