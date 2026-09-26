TASK: B-C1-008      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/B-C1-008/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C1-008/out/
TARGET: # Target: B-C1 (Cyclic Partitions and Cycles, 1 point, written proof)

Definitions (verbatim from the official statement, run/B/statement.md): a partition of n >= 1 is a weakly
decreasing sequence lambda = (lambda_1, ..., lambda_s) of positive integers with sum n (s piles).
The shift B(lambda) is the partition whose parts are the positive numbers among lambda_1 - 1, ..., lambda_s - 1
together with one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
T_k = k(k+1)/2, delta_k = (k, k-1, ..., 2, 1). The rank of n >= 1 is the unique k with T_{k-1} < n <= T_k.

Cell text (verbatim): "First, the long-run behaviour: which partitions repeat under the shift, and how they
fall into cycles. Let n = T_k. Prove that for every partition lambda of n there is an i with
B^i(lambda) = delta_k, and that delta_k is the only cyclic partition of n. Then let n be arbitrary of rank k,
say n = T_{k-1} + r with 1 <= r <= k: determine all cyclic partitions of n, and determine the number of
distinct cycles of B on the partitions of n. Prove both."

Exact targets (all must be proved, for every k >= 1):

(i)  For every k >= 1 and n = T_k: for every partition lambda of n there is an i >= 0 with B^i(lambda) = delta_k;
     and delta_k is the only cyclic partition of n.

(ii) For every k >= 1 and every r with 1 <= r <= k, n = T_{k-1} + r:
     (a) give an explicit description (as functions of k and r) of the set of ALL cyclic partitions of n,
         and prove that a partition of n is cyclic if and only if it lies in that set;
     (b) give the exact number of distinct cycles of B on the partitions of n (as a formula in k and r),
         and prove it.

Hand-in: a written proof (LaTeX), stating clearly what is established. Computation may be used only if exhaustive
over a finite set the argument has reduced the problem to (code included, < 10 min).
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/submission.md and out/submission.tex are written and out/submission.tex compiles (or, if no LaTeX engine is available, is checked for balanced environments and valid syntax).
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

The humans want the hand-in as LaTeX. Besides out/submission.md, write out/submission.tex: a complete, self-contained, compilable LaTeX article (amsmath, amssymb, amsthm) containing the statement of Cell 1, the status (SOLVED; claim status PROVED), the answer (cyclic partitions and number of cycles), cited vs. ours, the accepted proof converted faithfully from Markdown to LaTeX with its numbering preserved, how to verify (the included script, its run command and measured runtime; state that the proof does not rely on it), and limitations. Change no mathematics: only typesetting. Fix only reference slips that are purely editorial (e.g. the script path is code/check_c1.py). If pdflatex or latexmk is on PATH, compile it in out/ and report the result.
