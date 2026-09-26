TASK: B-C2-001      ROLE: prover      REGIME: BLIND
PHASE: 1   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 30 minutes
READ ONLY: run/tasks/B-C2-001/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C2-001/out/
TARGET: # Target: B-C2 (D_B at Triangular n, 2 points, written proof)

Definitions (verbatim from the official statement, run/B/statement.md): a partition of n >= 1 is a weakly
decreasing sequence lambda = (lambda_1, ..., lambda_s) of positive integers with sum n (s piles).
The shift B(lambda) is the partition whose parts are the positive numbers among lambda_1 - 1, ..., lambda_s - 1
together with one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) is cyclic },  D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, k-1, ..., 2, 1).

Cell text (verbatim): "Next, how long the process can take to reach a cycle, starting with the triangular
numbers. Determine D_B(T_k) for every k, with proof of both bounds."

Exact target (exact extremal value; the two halves are gated separately):
- Give an explicit formula F(k) (with any small-k exceptions stated separately and exactly) such that
  D_B(T_k) = F(k) for EVERY k >= 1.
- UPPER bound: prove d_B(lambda) <= F(k) for every partition lambda of T_k, for every k >= 1.
- LOWER bound: give an explicit partition lambda^(k) of T_k, as a function of k, and prove d_B(lambda^(k)) = F(k)
  (in particular >= F(k)) for every k >= 1.
- Any fact about which partitions of T_k are cyclic must itself be proved in the submission (no gated
  lower-cell results are available as assumptions yet).

Hand-in: a written proof (LaTeX), stating clearly what is established. Computation may be used only if exhaustive
over a finite set the argument has reduced the problem to (code included, < 10 min); small-k tables alone
prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when the formula, the upper bound for every partition and the explicit witness are all PROVED for every k, or when the same rung fails twice; report GAP rungs honestly.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line, so it can be typeset directly.
RETURN: only the report block from your agent instructions, at most 200 words plus LADDER / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

First write out/plan.md: TARGET as a ladder of numbered rungs (lemmas, special cases, reductions)
with dependencies. Work through it in order, marking each rung
PROVED / CHECKED / GAP / REFUTED / NOT STARTED.
Write out/proof.md. First line: the exact statement you prove, no more.
Then numbered steps; each justified by a definition, an earlier step, or a named lemma with exact reference.
"Clearly", "routine", "obviously", "similarly" and "by symmetry" may not replace an argument. Write the step out.
Mark anything you are not sure of [GAP].
Also write out/claims.md (claim | status | where proved), out/stuck.md (exact point of failure, or "none"),
and out/code/README.md (how to run any code) if you wrote code.
Check inbox/checklist-G.md item by item before you finish.
Numerics may guide you; any step resting on computation must include code in out/code/,
exact or interval arithmetic, runtime < 10 min.
If you executed code, fill in RAN exactly: what ran, parameter range, COMPLETED / TIMED OUT / PARTIAL, measured runtime.

Derive everything from first principles. Standard textbook tools are fine; results specific to this problem or its literature are not: if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors.
