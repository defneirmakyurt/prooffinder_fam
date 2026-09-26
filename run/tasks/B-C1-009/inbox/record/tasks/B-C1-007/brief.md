TASK: B-C1-007      ROLE: literature      REGIME: LITERATURE
PHASE: 1L   MODE: SOLVE   BRANCH: -
SUBJECT: -
TIME BOX: 20 minutes
READ ONLY: run/tasks/B-C1-007/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C1-007/out/
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
STOPPING CONDITION: Stop when sources.md maps the known results for this cell (with exact references), your own attempt is written, and divergence.md compares it with the blind results; do not present a citation as the proof of the cell.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/B-C1-001/, earlier/B-C1-002/
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.

Phase 1L. Inbox/earlier/ holds the Phase 1 blind results for this cell.
1. Find the literature for this cell and its neighbours, with links (out/sources.md: link, what was used, status).
2. Attempt the cell using known techniques (out/proof.md, out/claims.md).
3. Compare with the blind solvers: where do approaches differ or contradict? (out/divergence.md).
   Record which ideas came from the blind run, which from literature, and which are new here.
Blind and literature results are compared, never merged.
