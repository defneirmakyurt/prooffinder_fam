TASK: A-C2-015      ROLE: breaker      REGIME: BLIND
PHASE: 2C   MODE: ADVERSARY   BRANCH: -
SUBJECT: -
TIME BOX: 25 minutes
READ ONLY: run/tasks/A-C2-015/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C2-015/out/
TARGET: A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when the four ADVERSARY files and out/verdict.md are written; stop at once and report if a violation is confirmed in exact or interval arithmetic.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, obstacles/A-C2-001/ (stuck.md), obstacles/A-C2-002/ (stuck.md), obstacles/A-C2-010/ (stuck.md), obstacles/A-C2-011/ (stuck.md)
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

First write out/plan.md: the attack as a ladder of numbered rungs (sub-claims or families to test)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED (tested, no violation) / GAP / REFUTED / NOT STARTED.
Try to refute TARGET: structured candidates first (symmetric, perturbations of the conjectured optimum,
repetitions, equal values, smallest cases), then randomised and optimisation-based search with many restarts.
Save the worst case with exact values in out/worst.<ext> and a script that reproduces it.
If nothing breaks it, list exactly what you tested (families, sizes, instance counts, seeds).
"Survived" is evidence, not proof. A small positive gap is not a counterexample.
Fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.

Phase 2C. Inbox/obstacles/ holds stuck.md / verdict.md files of failed attempts (never their proofs).
Four separate tasks, each with its own output file:
1. out/contrapositive.md — write the claim as P => Q; try to prove not-Q => not-P directly
   (assume the bound fails and derive forced structure). A complete argument here is a proof: write it
   also as out/proof.md + out/claims.md so it can be verified.
2. out/cex_search/ — counterexample search assuming the claim is false (code, seeds, logs, near misses with gaps).
   Confirm any violation in exact or interval arithmetic.
3. out/local_analysis.md — is the conjectured optimum a strict local optimum (second-order perturbation)?
   A perturbation that beats it is a disproof; otherwise this is evidence only.
4. out/minimal_failing.md — the smallest sub-case where the known arguments fail, as a precise sub-lemma.
out/verdict.md: PROOF-ROUTE-FOUND | COUNTEREXAMPLE-CANDIDATE | LOCALLY-OPTIMAL-EVIDENCE | STUCK.

Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.

Checker note: any code that confirms a violation may use mpmath or python-flint interval/ball arithmetic (an exception to the stdlib-only default for this cell); floating point alone confirms nothing.
