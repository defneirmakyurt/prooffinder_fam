TASK: A-C2-017      ROLE: literature      REGIME: LITERATURE
PHASE: 3   MODE: ANALYST   BRANCH: -
SUBJECT: -
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C2-017/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C2-017/out/
TARGET: A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when sources.md, subproblems.md (each sub-problem labelled (a), (b) or (c)) and, for any (b)/(c) attempted, proof.md/claims.md/stuck.md are written; write why_not.md only if you judge the cell not solvable now. Do not spend more than the time box on sources you cannot open.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/A-C2-001/, earlier/A-C2-002/, earlier/A-C2-003/, earlier/A-C2-004/, earlier/A-C2-005/, earlier/A-C2-006/, earlier/A-C2-008/, earlier/A-C2-009/, earlier/A-C2-010/, earlier/A-C2-011/, earlier/A-C2-012/, earlier/A-C2-013/, earlier/A-C2-014/, earlier/A-C2-015/, earlier/A-C2-016/, earlier/cell/matrix.md, earlier/cell/gate
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.

Phase 3. Inbox/earlier/ holds everything for this cell (proofs, verdicts, matrix, no_natural_route, adversary).
1. Map what is known: PROVED vs COMPUTER-VERIFIED vs CONJECTURED, with links; flag inaccessible results.
2. Reduce the cell to critical sub-problems: (a) known and citable, (b) known but hard to access, so reproduce it,
   (c) unknown (out/subproblems.md).
3. Attempt (b) and (c), crediting earlier work (out/proof.md, out/claims.md).
4. If the cell cannot be solved: out/why_not.md — where the obstruction is, which approaches fail and why
   (with counterexamples if any), why each failing branch fails, and what the next person needs to start.
