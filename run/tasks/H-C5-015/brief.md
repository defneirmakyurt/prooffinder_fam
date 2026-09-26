TASK: H-C5-015      ROLE: scribe      REGIME: RECORD
PHASE: 5   MODE: SUBMISSION   BRANCH: -
SUBJECT: -
TIME BOX: 15 minutes
READ ONLY: run/tasks/H-C5-015/ (this brief + inbox/). Do not open anything else under run/.
WRITE ONLY: run/tasks/H-C5-015/out/
TARGET: H-C5 "Bounds for U(Q_9)" (8 points, judged). Verbatim: "Q_9 has 512 vertices and 2304 edges. The best bounds known to the organisers are 2368 <= U(Q_9) <= 2400; the lower bound is unpublished. Improve either one: prove that U(Q_9) >= 2369, or exhibit a labelling of Q_9 with at most 2399 uphill paths." Definitions exactly as in inbox/statement.md.
Exact target (either route suffices): (UPPER) an explicit labelling of Q_9 with at most 2399 uphill paths, handed in as Q9.txt: exactly 512 lines, line i (1-based) is the 9-character 0/1 string of the vertex that gets label i; or (LOWER) a proof, possibly computer-assisted, that every labelling of Q_9 has at least 2369 uphill paths. Matching 2400 or 2368 earns nothing.
Hand-in (verbatim): "either a labelling of Q_9 in the same format, whose uphill paths will be counted mechanically, or a proof of the lower bound."
STATEMENT RULE: Work from the exact statement in TARGET. Preserve every definition, quantifier, parameter range and hand-in requirement. Never infer the question from a cell's title.
ASSUMPTIONS: none beyond the statement
STOPPING CONDITION: stop when out/submission.md is written
LESSONS: role-lessons.md v1, problem-lessons.md v0
RULES: any computation must be exact or interval arithmetic, code included, runtime < 10 min; state exactly what is established
RETURN: only the report block from your agent instructions, at most 200 words plus RAN lines.
        Full work goes in out/.
INBOX: role-lessons.md v1, problem-lessons.md v0, statement.md, target.md, checklist-G.md, A_lemmaA_gated.md, B_identity_construction_weakLB.md, C_independent_decycling.md, D_restricted_lower_bound.md, Q9.txt
PYTHON: /home/user/bainsahackathon/.venv/bin/python3 (sympy, mpmath, networkx, python-flint, python-sat); plain python3 lacks them.
        Checkers and anything a judge reruns stay stdlib-only unless the brief says otherwise.

Reports introduce no new mathematics. Never upgrade a status given in the brief.
Fill in RAN exactly for every command you ran.

Inbox holds accepted artefacts and the cell's "what to hand in" text.
Produce out/submission.md in exactly that format: statement, cell status, claim status, cited vs. new,
proof or certificate, how to verify (command, expected output, measured runtime), limitations.
PARTIAL lists the claims established and the exact remaining gap. Add no claim that is not in the accepted artefacts.

CELL STATUS: PARTIAL
CLAIM STATUS (do not upgrade): PARTIAL: Lemma A PROVED (gated, cell C4); U(Q_9) <= 2400 COMPUTER-VERIFIED (checker); items C and D and the weak bound in B UNREFEREED
ESTABLISHED: Lemma A (PROVED, gated in cell C4 by two referees): every labelling of Q_d has >= 2^d + (d-1)|S| uphill paths, S = {v : down(v) >= 2}, V minus S an induced forest; hence U(Q_9) >= 512 + 8*nabla(Q_9), nabla = decycling number; U(Q_9) <= 2400 (COMPUTER-VERIFIED: explicit labelling Q9.txt, accepted checker prints VERIFIED 2400; equals the organisers' bound)
REMAINING GAP: Neither threshold is reached: a labelling with <= 2399 paths needs a decycling set of Q_9 with <= 235 vertices (none known; published 225 <= nabla(Q_9) <= 236); U(Q_9) >= 2369 would follow from nabla(Q_9) >= 233 (not proved). Unrefereed partial results: U(Q_9) >= 2312 unconditionally; decycling sets with no inner edge have >= 236 vertices (cites A(9,4) = 20); labellings whose S has <= 3 vertices of one parity have >= 2376 paths (referees pending).

HAND-IN TARGET: a single self-contained Markdown document out/submission.md that a human pastes into a judges' text box for cell C5. Requirements: (1) no internal paths, task ids, 'inbox', 'H2 Step 8'-style cross-references, code file names or run logs; renumber everything into one consistent scheme (Sections 1-5, steps within) and rewrite every cross-reference to point inside the document; (2) proofs copied verbatim from the inbox files except for that renaming and for deleting sentences that only point to code/sanity checks; add NO mathematics and fix nothing; if a step cannot be made self-contained without new mathematics, keep it as is and mark it; (3) put a status line at the top of every section, exactly: Section 1 Lemma A (from A_lemmaA_gated.md sections A and the notation): 'PROVED (refereed by two independent referees)'; Section 2 the 2400 construction (B, Step 10 and what it needs from Part A): 'COMPUTER-VERIFIED: the attached labelling Q9.txt has exactly 2400 uphill paths'; Section 3 the weak unconditional bound U(Q_9) >= 2312 (B, Steps 8-9): 'proof below, not independently refereed'; Section 4 independent decycling sets (C, Lemma I; state that A(9,4) = 20 is cited with its reference): 'proof below, not independently refereed'; Section 5 the restricted lower bound (D): 'proof below, not independently refereed'; (4) open with a 5-line summary: what is claimed, what is not (neither 2399 nor 2369 is reached), and the exact remaining gap as given in this brief; (5) plain Markdown with ASCII math (no LaTeX macros), so it pastes cleanly into a plain text box. Also write out/submission_short.md: the same summary plus section statements only (no proofs), under 40 lines.
