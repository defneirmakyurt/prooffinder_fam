TASK: H-C5-006      ROLE: literature      REGIME: LITERATURE
PHASE: 3   MODE: ANALYST   BRANCH: -
SUBJECT: -
TIME BOX: 45 minutes
READ ONLY: run/tasks/H-C5-006/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C5-006/out/
TARGET: H-C5 "Bounds for U(Q_9)" (8 points, judged). Verbatim: "Q_9 has 512 vertices and 2304 edges. The best bounds known to the organisers are 2368 <= U(Q_9) <= 2400; the lower bound is unpublished. Improve either one: prove that U(Q_9) >= 2369, or exhibit a labelling of Q_9 with at most 2399 uphill paths." Definitions exactly as in inbox/statement.md.
Exact target (either route suffices): (UPPER) an explicit labelling of Q_9 with at most 2399 uphill paths, handed in as Q9.txt: exactly 512 lines, line i (1-based) is the 9-character 0/1 string of the vertex that gets label i; or (LOWER) a proof, possibly computer-assisted, that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
Hand-in (verbatim): "either a labelling of Q_9 in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound."
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop and report immediately if a source gives (or lets you build) a decycling set of Q_9 with at most 235 vertices, or proves nabla(Q_9) >= 233; otherwise stop at the time box with subproblems.md and why_not.md
LESSONS: role-lessons.md v0, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established; uphill-path conventions: a lone valley counts as an uphill path (k=1); paths are counted as sequences, so different routes to the same endpoint count separately; paths must start at a valley; labels strictly increase and form a bijection onto 1..2^d
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, problem-lessons.md v0, statement.md, target.md, checklist-G.md, earlier/H-C5-002/, earlier/cell/gate, checker, C4-lemmaA-claims.md
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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

FOCUS (network access to arxiv, OEIS, AoPS, Springer pages etc. is now open; earlier agents could not open these). The cell reduces (inbox/earlier/H-C5-002/out/proof.md, and Lemma A in inbox/C4-lemmaA-claims.md, both under review, not gated) to the decycling number nabla(Q_9): 512 + 8*nabla(Q_9) <= U(Q_9) <= 2400. (1) Open the primary sources: D.A. Pike, 'Decycling hypercubes', Graphs Combin. 19 (2003) 547-550 (try Springer, the zbMATH Open / MathSciNet review, Google Scholar versions, the author's pages); Bau, Beineke, Du, Liu, Vandell, 'Decycling cubes and grids', Utilitas Math. (2000); Beineke-Vandell 1996; and every later paper citing them (Google Scholar 'cited by', arXiv full-text search for 'decycling' + 'hypercube', 'feedback vertex set' + 'hypercube', 'maximum induced forest' + 'hypercube'/'Q_9'/'9-cube'), plus OEIS. Record for each exactly what it states about nabla(Q_9) (or the maximum induced forest of Q_9), whether it contains the argument, and the link. (2) If any source gives an explicit decycling set of Q_9 with <= 235 vertices, or a construction that yields one, reconstruct it in code, verify acyclicity of the complement exactly, build a labelling from it and score it with inbox/checker/verify.py (out/Q9.txt). (3) If any source proves nabla(Q_9) >= 233, write out exactly the statement and the argument. (4) Otherwise: subproblems.md (known and citable / known but hard to access / unknown) for both routes, attempt the reachable ones, and why_not.md.
