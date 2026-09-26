TASK: B-C4-011      ROLE: literature      REGIME: LITERATURE
PHASE: 1L   MODE: SOLVE   BRANCH: -
SUBJECT: -
TIME BOX: 45 minutes
READ ONLY: run/tasks/B-C4-011/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C4-011/out/
TARGET: UPPER half of B-C4: for EVERY k >= 5 and EVERY partition lambda of n = T_{k-1} + 1, d_B(lambda) <= (k-1)(k-3). (The matching lower bound, d_B(lambda^(k)) = (k-1)(k-3) for lambda^(k) = (k-2, k-2, k-3, ..., 3, 2, 2, 1), is handled separately.) Definitions exactly as in inbox/statement.md.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when sources.md, proof.md (or a precise account of what is and is not available), claims.md and divergence.md are written
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/B-C4-005/, earlier/B-C4-006/, earlier/B-C4-007/
PYTHON: /Users/defneirmakyurt/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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

Three blind lineages already prove the lower bound with the same witness and all stall on this upper bound for partitions above the two lowest diagonal-energy levels. Find the literature on D_B(T_{k-1}+1) and on upper bounds for Bulgarian solitaire transients near triangular numbers; if an argument exists, re-derive it IN FULL for this target (citing a published result for the statement itself does not count). Write divergence.md comparing with the blind results.
