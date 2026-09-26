TASK: B-C3-017      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 12 minutes
READ ONLY: run/tasks/B-C3-017/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-017/out/
TARGET: # Target: B-C3 (A General Upper Bound, 3 points, written proof)

Definitions (verbatim, run/B/statement.md): a partition of n >= 1 is a weakly decreasing sequence of positive
integers with sum n (s piles). B(lambda): the positive numbers among lambda_1 - 1, ..., lambda_s - 1, together with
one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k.

Cell text (verbatim): "Now the numbers strictly between two consecutive triangular numbers.
(a) Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.
(b) Determine D_B(T_k - 1) exactly.
(c) Determine also, for that n, which partitions attain the maximum."

Exact targets:
(a) For every k >= 4, every n with T_{k-1} < n < T_k, and every partition lambda of n: d_B(lambda) <= k^2 - 2k - 1.
(b) A formula F(k) with D_B(T_k - 1) = F(k); state explicitly the k-range proved (the cell states none; cover as
    many k >= 1 as possible and give any small-k values separately). Both halves: upper bound over every partition
    of T_k - 1, and an explicit partition (function of k) attaining F(k), each proved for every k in the range.
(c) The exact set of partitions lambda of T_k - 1 with d_B(lambda) = D_B(T_k - 1), as explicit functions of k,
    with proof that every listed partition attains the maximum and that no other partition does.

Hand-in: a written proof (LaTeX). Computation only if exhaustive over a finite set the argument has reduced the
problem to (code included, < 10 min); small-k tables alone prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when out/submission.tex compiles (latexmk -pdf) and out/submission.md is written. Hard limit 12 minutes.
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

Use ONLY accepted/B-C3-007/ (the full gated proof); ignore accepted/proof.md (an earlier lower-half proof). Write out/submission.tex: a complete, compilable LaTeX article (amsmath, amssymb, amsthm) with the verbatim Cell 3 statement; CELL STATUS SOLVED, CLAIM STATUS PROVED; answers stated up front ((a), (b) with k-range and small-k values, (c)); cited vs ours (the method follows Griggs and Ho 1998 Thm 4.4, with bibliographic data from accepted/B-C3-007/sources.md; every lemma is re-proved in full here; the gated Cell 1 classification of cyclic partitions is used and stated as the earlier cell's result); the accepted proof converted faithfully to LaTeX with its step numbering. Editorial fixes only, no change to mathematics: in (c) call the answer a proved criterion (the maximiser set is characterised exactly, not listed in closed form) and remove the [GAP] label in 9.6, which referred only to the missing closed list; tidy wording in 4.2 without changing its content. How to verify: accepted/B-C3-007/code/check.py (command, expected output, measured runtime; sanity only, not load-bearing). Limitations: (c) is a criterion, not a closed list; sizes of the maximiser sets for small k as numerical evidence only. Compile in out/ and report the result.
