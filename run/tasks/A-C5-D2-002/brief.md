TASK: A-C5-D2-002      ROLE: referee      REGIME: CLEAN-ROOM
PHASE: 2   MODE: VERIFY   BRANCH: -
SUBJECT: A-C5-D2-001
TIME BOX: 30 minutes
READ ONLY: run/tasks/A-C5-D2-002/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/A-C5-D2-002/out/
TARGET: # Target: A-C5-D2 — the d=2 sub-case of A-C5 ("d+2 Lines in R^d"), carved out as its own lemma

## Exact statement

For every 4 lines ℓ_1,ℓ_2,ℓ_3,ℓ_4 through the origin of R^2 (repetitions/coincident lines
allowed), S(ℓ_1,ℓ_2,ℓ_3,ℓ_4) = Σ_{i<j} θ(ℓ_i,ℓ_j) ≤ 2π, where θ(ℓ,ℓ') = arccos|⟨x,x'⟩| for unit
vectors x,x' spanning ℓ,ℓ'. (This is exactly A-C5's target (C(d+2,2)-2)π/2 specialized to d=2,
N=4: (C(4,2)-2)π/2 = (6-2)π/2 = 2π.)

## Why this is carved out separately

A-C5 as a whole requires this bound for every d≥2. A-C5-001 and A-C5-002 (two independent blind
provers) both fully proved exactly this d=2 case, but A-C5 itself remains PARTIAL (d≥3 open).
Two independent clean-room referees (A-C5-004, A-C5-005) verified A-C5-001's full submission
against the WHOLE cell's target and correctly returned MAJOR (statement match: no) because the
submission does not cover d≥3 — but both explicitly confirmed steps 1-2 and 5 (the d=2 argument)
are fully correct, with no unjustified steps, correct equality cases, and independent
counterexample search finding nothing. This lemma-cell exists so the d=2 result can be judged
against its own, honestly-scoped statement and gated on its own merits, without that gate being
blocked by the (real, separate) fact that A-C5's general-d claim isn't proved.

## Deliverable being gated

`run/tasks/A-C5-D2-001/out/proof.md`, an excerpt (Steps 1, 2 and 5 verbatim, renumbered) of
A-C5-001's full submission — the algebraic reduction S = C(N,2)π/2 − T (steps 1-2) plus the
self-contained d=2 case-split argument (step 5). Steps 3, 4 and 6 of the original (the general-d
weak bound and the d≥3 gap) are omitted here as not relevant to this narrower claim.
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: run the full 7-step protocol and return a verdict
LESSONS: role-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus CHECKLIST / RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v0, statement.md, target.md, checklist-G.md, checklist-S.md, subject/ (proof.md, claims.md, code of A-C5-D2-001)
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
