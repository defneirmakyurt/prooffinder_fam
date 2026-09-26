TASK: B-C3-008      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: B-C3-002
TIME BOX: 20 minutes
READ ONLY: run/tasks/B-C3-008/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-008/out/
TARGET: # Target: B-C3(b), LOWER-BOUND half (gated separately)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, delta_k).

Claim to verify: for every k >= 3, the explicit partition of T_k - 1
  lambda*_k = (k-1, k-2, k-2, k-3, ..., 2, 1, 1)
satisfies d_B(lambda*_k) = k^2 - 2k - 1 exactly; consequently D_B(T_k - 1) >= k^2 - 2k - 1 for every k >= 3.
Requires: lambda*_k is a partition of T_k - 1 (check the part list for every k >= 3, incl. k = 3, 4 where the
pattern is short); the cyclic partitions of T_k - 1 (gated Cell 1: delta_{k-1} plus k-1 of the k cells of the
k-th diagonal) may be used; B^i(lambda*_k) is not cyclic for i < k^2-2k-1 and is cyclic at i = k^2-2k-1, proved for
EVERY k >= 3 symbolically. The upper bound (a) and the maximiser classification (c) are NOT part of this target.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: Stop when every checklist item and every proof step the LOWER-half target depends on has a verdict with reasons; stop early and report WRONG on a counterexample.
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of B-C3-002)
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
