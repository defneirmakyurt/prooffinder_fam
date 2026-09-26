TASK: B-C3-012      ROLE: literature      REGIME: LITERATURE
PHASE: 3   MODE: ANALYST   BRANCH: -
SUBJECT: -
TIME BOX: 40 minutes
READ ONLY: run/tasks/B-C3-012/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/B-C3-012/out/
TARGET: # Target: B-C3(a) and the UPPER half of B-C3(b)

Definitions as in run/B/statement.md (partition, shift B, cyclic, d_B, D_B, T_k, rank).
(a) For every k >= 4, every non-triangular n with T_{k-1} < n < T_k, and every partition lambda of n:
    d_B(lambda) <= k^2 - 2k - 1.
(b-upper) In particular D_B(T_k - 1) <= k^2 - 2k - 1 for every k >= 4 (n = T_k - 1 is non-triangular of rank k).
    (Lower half D_B(T_k-1) >= k^2-2k-1 is already proved; with (a) this gives D_B(T_k-1) = k^2-2k-1.)
A complete, self-contained, line-by-line written proof valid for every k >= 4; finite checks prove nothing for all k.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: Gated claims: B-C1 (Cell 1: for n = T_{k-1}+r the cyclic partitions are (k-1+e_1,...,1+e_{k-1},e_k), e in {0,1}^k, sum e = r). B-C2 (Cell 2, proved and verified: D_B(T_k) = k^2-k; its accepted proof is in inbox/gated_B-C2_proof.md where provided).
STOPPING CONDITION: Priority: a complete, self-contained, line-by-line written proof of (a) for every k>=4 (e.g. reconstructing Griggs-Ho 1998 Thm 4.4 / Etienne 1991 / Igusa 1985 in full, every lemma re-proved). A citation alone does not count. Stop when written, or state precisely what cannot be completed.
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; Write the final proof in proof.md using LaTeX math notation ($...$), line by line; self-contained.
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/B-C3-002/, earlier/B-C3-003/, earlier/B-C3-004/, earlier/cell/gate
PYTHON: /Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

You have web search and fetch. Tag every result PROVED / COMPUTER-VERIFIED / CONJECTURED, and say whether the
source contains the argument or only cites it. Flag computations whose code is unavailable and steps called
"routine" but not written down. Every claim carries a source link or a pointer to an artefact, plus a status tag.
Never present a citation as a proof of the cell itself. Never call anything new: write "not found in <sources searched>".
Your output never reaches blind agents.

Phase 3. Inbox/earlier/ holds everything for this cell (proofs, verdicts, matrix, no_natural_route, adversary).
1. Map what is known: PROVED vs COMPUTER-VERIFIED vs CONJECTURED, with links; flag inaccessible results.
2. Reduce the cell to critical sub-problems: (a) known and citable, (b) known but hard to access, so reproduce it,
   (c) unknown (out/subproblems.md).
3. Attempt (b) and (c), crediting earlier work (out/proof.md, out/claims.md).
4. If the cell cannot be solved: out/why_not.md — where the obstruction is, which approaches fail and why
   (with counterexamples if any), why each failing branch fails, and what the next person needs to start.
