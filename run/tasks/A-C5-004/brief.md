TASK: A-C5-004      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: A-C5-001
TIME BOX: 30 minutes
READ ONLY: run/tasks/A-C5-004/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C5-004/out/
TARGET: # Target: A-C5 — "d+2 Lines in R^d" (8 pts)

## Exact statement (verbatim cell text)

The case N=d+2 in every dimension, with the same conjectured optimum: the d coordinate axes,
two of them repeated. Prove that for every d≥2, any d+2 lines in R^d satisfy

    S ≤ (C(d+2,2) - 2) * π/2

where C(n,2) = n(n-1)/2, S(ℓ_1,...,ℓ_{d+2}) = Σ_{i<j} θ(ℓ_i,ℓ_j), θ(ℓ,ℓ') = arccos|⟨x,x'⟩| ∈ [0,π/2]
for unit vectors x,x' spanning ℓ,ℓ', and repetitions among the ℓ_i are allowed.

## Parameter range

- d ≥ 2 (all integers), N = d+2 lines (with repetition allowed).
- No restriction on the lines beyond "N=d+2 lines through the origin of R^d".

## Deliverable

A complete, general (every d≥2) written proof, or an honest PARTIAL result (e.g. proved for a
family of d, or for A-C4's two concrete instances only) with the exact remaining gap stated.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: run the full 7-step protocol and return a verdict
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of A-C5-001)
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
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
