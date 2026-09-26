TASK: B-C2-011      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: GATE   MODE: GATE   BRANCH: -
SUBJECT: B-C2-003
TIME BOX: 20 minutes
READ ONLY: run/tasks/B-C2-011/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C2-011/out/
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
STOPPING CONDITION: Stop when every checklist item and every proof step has a verdict with reasons; stop early and report WRONG on a counterexample.
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, tmp of B-C2-003)
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
