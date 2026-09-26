TASK: B-C2-013      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/B-C2-013/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C2-013/out/
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
STOPPING CONDITION: Stop when out/submission.tex compiles (latexmk -pdf) and out/submission.md is written.
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, accepted
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
PARTIAL lists the claims established and the exact remaining gap. Add no claim that is not in the accepted artefacts.

CELL STATUS: SOLVED
CLAIM STATUS (do not upgrade): PROVED

Write out/submission.tex: a complete, compilable LaTeX article (amsmath, amssymb, amsthm) with the Cell 2 statement, status (SOLVED, PROVED), the answer D_B(T_k)=k^2-k for every k>=1 with the explicit witness, cited vs ours, the accepted proof converted faithfully to LaTeX with its numbering (0.1-0.3, A.0-A.4, B1-B9), how to verify (the three scripts, run commands, runtimes; not load-bearing), limitations. Cite Griggs and Ho (1998), Thm 3.7 and Lemmas 3.3-3.6 as the source of the upper-bound architecture, with the bibliographic data in the accepted sources.md, and say every lemma is re-proved in full here. Editorial fixes only, no change to mathematics: delete the phrase 'or the B-C1 assumption, which says the same' in Part B; in B7 state the invariant p+m <= q-1 as part of I(m), as the proof's own step (a) already derives; point code paths to the shipped code/ folder. Compile in out/ and report the result.
