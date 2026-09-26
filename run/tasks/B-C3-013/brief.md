TASK: B-C3-013      ROLE: prover      REGIME: FRESH
PHASE: WAVE   MODE: -   BRANCH: -
SUBJECT: -
TIME BOX: 40 minutes
READ ONLY: run/tasks/B-C3-013/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-013/out/
TARGET: # Target: B-C3(c), maximiser classification (conditional on the upper bound)

Definitions as in run/B/statement.md. Let k >= 4, n = T_k - 1, M_k = k^2 - 2k - 1.
HYPOTHESIS (H), stated explicitly and not to be proved here: d_B(lambda) <= M_k for every partition lambda of T_k - 1
(this is C3(a)/(b) upper bound, being proved separately).
Prove, under (H) and for every k >= 4 (small k listed separately if the pattern differs):
 1. An EXPLICIT description, as functions of k, of the set E_k = { lambda |- T_k - 1 : d_B(lambda) = M_k }
    (a closed list or a closed-form rule that lets one write every member down directly, not "all preimages under
    B^j of some partition" unless those preimages are then listed explicitly).
 2. Every listed partition has d_B = M_k (this direction needs no hypothesis).
 3. Under (H), no other partition has d_B = M_k.
Exhaustive data to match (from earlier computation, not a proof): |E_k| = 1, 6, 34, 175, 831, 3911, 18163 for k = 4..10.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Gated claim B-C1 (Cell 1). Hypothesis (H) of the target may be assumed ONLY where stated; mark every use.
STOPPING CONDITION: Stop when 1-3 of the target are PROVED for every k>=4, or the same rung fails twice.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line; self-contained.
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

ANGLE: witness-family. Pursue this angle; if you abandon it, say why.
