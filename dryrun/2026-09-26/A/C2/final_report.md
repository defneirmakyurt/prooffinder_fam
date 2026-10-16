# Final report: cell A-C2 "An Orthogonality Lemma" (task A-C2-018, scribe, Phase 5, MODE REPORT)

Citation convention: every path is relative to `inbox/record/` of this task (the copy of the record shipped to this task), unless it starts with `brief.md` (this task's own brief) or `out/` (this task's own output). Where a file has no numbered steps, the citation gives section names or line numbers. `cell/phases.md` in this snapshot lists tasks A-C2-001 to A-C2-017 only (cell/phases.md, lines 3-19). This task, A-C2-018, is cited through its own brief.md.

---

## 1. OUTCOME

**PROVED.** Cell status: **SOLVED**. Claim status: **PROVED** (brief.md, lines 29-30).

- The only claim that passed the gate is the proof of A-C2-002. Gate decision: "VALID — two referees ACCEPT the same proof version with complete checklists (A-C2-005, A-C2-006); matrix ROBUST; statement checked by head". Next action: "PROVED on board" (cell/gate/A-C2-002.md, lines 6-7).
- The accepted artefacts are `cell/accepted/proof.md` and `cell/accepted/claims.md`, pinned by `cell/accepted/MANIFEST.sha256` (lines 1-2). They are byte-identical to `tasks/A-C2-002/out/proof.md` and `tasks/A-C2-002/out/claims.md` (out/verify/logs/02_manifest_check.txt; out/verify/logs/03_accepted_vs_A-C2-002.txt).
- No step of the accepted proof uses computation (cell/accepted/proof.md, line 3 and section "Remarks", line 83).

## 2. STATEMENT

The exact statement, verbatim from cell/target.md, lines 1-3 (identical to brief.md, lines 7-9):

> A-C2 "An Orthogonality Lemma" (2 points, written proof). Verbatim: "A statement about a chain of vectors, in which each vector may fail to be orthogonal only to its immediate neighbours in the list. Let m >= 2 and let x_1, ..., x_m be unit vectors in R^(m-1) with <x_i, x_j> = 0 whenever |i - j| >= 2. Prove that sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos |<x, y>|."
>
> Exact target: for every integer m >= 2 and all unit vectors x_1, ..., x_m in R^(m-1) (dimension m-1, not m) such that <x_i, x_j> = 0 for all i, j with |i - j| >= 2, the chain sum sum_{i=1}^{m-1} theta(x_i, x_{i+1}) <= (m - 2) pi/2, where theta(x, y) = arccos|<x, y>| in [0, pi/2]. Only consecutive pairs (i, i+1) are summed. Definitions exactly as in inbox/statement.md.
>
> Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.

**Checklist hash:** `sha256(cell/checklist.md) = 8d96a9f43b592c0e795769e6c13c421e3bb87ee04efc9722495887fdc9887c84`. The command is under RAN in section 6 (out/verify/logs/01_checklist_sha256.txt).

## 3. RESULT

**The final proof is `cell/accepted/proof.md`** (sha256 `3e08fea36e4a73353a09efda5019a7491e811a5f8522c7d3c88e6bcb3e9a3ea1`, cell/accepted/MANIFEST.sha256, line 1). It is the proof of A-C2-002. The outline below follows it step by step, with no change to any mathematical step.

- **Notation.** c_i = <x_i, x_{i+1}>, a_i = arcsin|c_i| in [0, pi/2], A(x) = sum_{i=1}^{m-1} a_i. An "m-chain" is a list of m unit vectors in an (m-1)-dimensional inner-product space with <x_i,x_j> = 0 for |i-j| >= 2 (cell/accepted/proof.md, section Notation).
- **Step 1 (reformulation).** arccos t + arcsin t = pi/2 on [0,1], so the chain sum is (m-1) pi/2 - A(x). The target is therefore equivalent to (*) A(x) >= pi/2. An isometry remark transfers (*) to any (m-1)-dimensional inner-product space (cell/accepted/proof.md, Step 1).
- **Step 2 (base case m = 2).** In R^1 the unit vectors are ±1, so |c_1| = 1 and A = pi/2 (cell/accepted/proof.md, Step 2).
- **Step 3 (degenerate case).** If |c_{m-1}| = 1 then a_{m-1} = pi/2 and A >= pi/2 (cell/accepted/proof.md, Step 3).
- **Step 4 (reduction, |c_{m-1}| < 1).** Set y = (x_{m-1} - c x_m)/cos a_{m-1}. Then x_1, ..., x_{m-2}, y is an (m-1)-chain in W = x_m^perp, where dim W = m-2. Its last coefficient has absolute value sin a_{m-2}/cos a_{m-1}, and its angles are a_1, ..., a_{m-3}, a'. The induction hypothesis gives (4e): a_1 + ... + a_{m-3} + a' >= pi/2 (cell/accepted/proof.md, Step 4).
- **Step 5 (trigonometric lemma).** If alpha + beta < pi/2, then arcsin(sin alpha / cos beta) <= alpha + beta. This follows from the identity sin(alpha+beta) cos beta - sin alpha = sin beta cos(alpha+beta) >= 0 (cell/accepted/proof.md, Step 5).
- **Step 6 (inductive step).** If a_{m-2} + a_{m-1} >= pi/2, the claim is immediate. Otherwise a' <= a_{m-2} + a_{m-1} by Step 5, and (4e) gives A >= pi/2 (cell/accepted/proof.md, Step 6).
- **Step 7 (target).** The chain sum is (m-1)pi/2 - A(x) <= (m-2)pi/2 (cell/accepted/proof.md, Step 7).

The claims table lists Steps 1-7 as PROVED (cell/accepted/claims.md, lines 3-9).

**Sharpness.** Sharpness is not part of the target. The accepted proof gives the m = 3 family x_1 = e_1, x_2 = (cos t, sin t), x_3 = e_2 with sum pi/2 (cell/accepted/proof.md, Remarks, line 82). The tuple (e_1, e_1, e_2, ..., e_{m-1}) gives exactly (m-2) pi/2. This was checked exactly for m = 2..11 by A-C2-004 (tasks/A-C2-004/out/verdict.md, S2 and "Numerical checks" item 5) and certified in arb for m = 2..11 by A-C2-006 (tasks/A-C2-006/out/verdict.md, section 4).

## 4. HOW IT WAS REACHED

### 4.1 Task inventory

There are 17 task folders in the record, A-C2-001 to A-C2-017 (out/verify/logs/11_inventory.txt). By role (cell/phases.md, lines 3-19):

- 4 provers: A-C2-001, -002, -010, -011
- 2 literature tasks: A-C2-003, -017
- 8 referees: A-C2-004, -005, -006, -009, -012, -013, -014, -016
- 2 triage tasks: A-C2-007, -008
- 1 breaker: A-C2-015

### 4.2 Timeline

**Phase 1 (12:21), blind provers** (cell/phases.md, lines 3-4)

- **A-C2-001** proved the target with the Gram matrix / leading-minor route:
  - det G = 0 from rank <= m-1;
  - D_k = D_{k-1} - a_{k-1}^2 D_{k-2};
  - a trigonometric lemma;
  - under psi_{m-1} < pi/2, D_k >= cos^2(psi_{k-1}) D_{k-1} > 0, contradicting det G = 0.

  Status claimed: SOLVED (tasks/A-C2-001/out/proof.md, Steps 1-5 and line 3). stuck.md: "none" (tasks/A-C2-001/out/stuck.md, line 1).
- **A-C2-002** proved the target by backward projection (induction on m, removing x_m) plus the lemma arcsin(sin a / cos b) <= a + b (tasks/A-C2-002/out/proof.md, Steps 1-7). stuck.md: "none" (tasks/A-C2-002/out/stuck.md, line 1).

**Phase 1L (12:23), literature task A-C2-003** (cell/phases.md, line 5)

- It wrote a third proof, a forward Gram–Schmidt residual route: t_{k+1}^2 = 1 - a_k^2/t_k^2, some t_k = 0 by dimension, and t_k >= cos psi_{k-1} under the contrary hypothesis (tasks/A-C2-003/out/proof.md, Steps 1-5).
- Every web fetch was blocked (tasks/A-C2-003/out/stuck.md, lines 3-6).

**Phase 2 referees**

| Time | Referee | Subject | Verdict | Citation |
|---|---|---|---|---|
| 12:23 | A-C2-004 | A-C2-001 | ACCEPT | tasks/A-C2-004/out/verdict.md, line 1 |
| 12:23 | A-C2-005 | A-C2-002 | ACCEPT | tasks/A-C2-005/out/verdict.md, line 1 |
| 12:25 | A-C2-006 (GATE) | A-C2-002 | ACCEPT | tasks/A-C2-006/out/verdict.md, line 2 |
| 12:27 | A-C2-009 | A-C2-003 | ACCEPT | tasks/A-C2-009/out/verdict.md, line 1 |

Times: cell/phases.md, lines 6-8 and 11.

**First gate (12:28).** A-C2-002 was ruled VALID with "Matrix: not run". No Phase 2B task existed yet (cell/gate/A-C2-002.pre-2B.md, lines 1-7; brief.md, GATE FACTS, line 32).

**Phase 2A triage (12:27)**

- **A-C2-007** was created but has no output files: only tasks/A-C2-007/brief.md exists, and its out/ directory is empty (out/verify/logs/12_A-C2-007_files.txt).
  - Its INBOX line included obstacles/A-C2-004/ (verdict.md) and obstacles/A-C2-005/ (verdict.md) (tasks/A-C2-007/brief.md, line 17).
  - Per the head, it was never dispatched because that inbox would have shown Part S to a blind triage agent (brief.md, line 32).
- **A-C2-008** rated the five branches (tasks/A-C2-008/out/triage.md, section "Branch ratings"):

  | Branch | Rating |
  |---|---|
  | ALGEBRAIC | HIGH |
  | ANALYSIS | HIGH |
  | DISCRETE | MEDIUM |
  | TOPOLOGICAL | LOW |
  | NUMBER-THEORY | NONE |

  - Under the head's two-branch budget it selected ALGEBRAIC and ANALYSIS as solvers (tasks/A-C2-008/out/selected_branches.txt, lines 1-2; tasks/A-C2-008/brief.md, line 30).
  - Eliminations, in re-admission order (tasks/A-C2-008/out/triage.md, section "Eliminations"):
    1. DISCRETE: dropped only by the budget cap; "Re-admit first".
    2. TOPOLOGICAL: existence of a maximiser only.
    3. NUMBER-THEORY: no arithmetic structure.
  - No task for a re-admitted branch appears in cell/phases.md (lines 3-19).

**Phase 2B (12:28), branch provers** (cell/phases.md, lines 12-13)

- **A-C2-010 (ALGEBRAIC)** proved the target by contradiction with the leading-minor recursion and partial sums alpha_k = theta_1 + ... + theta_k - (k-1) pi/2 (tasks/A-C2-010/out/proof.md, Steps 1-6).
- **A-C2-011 (ANALYSIS)** proved it with a weighted AM-GM splitting of the quadratic form ||sum t_i x_i||^2 >= cos^2(B_{k-1}) t_k^2, which gives linear independence when B_{m-1} < pi/2 (tasks/A-C2-011/out/proof.md, Steps 1-6).
- Both stuck.md files read "none" (tasks/A-C2-010/out/stuck.md, line 1; tasks/A-C2-011/out/stuck.md, line 1).

**Phase 2B-XV cross-verification and further Phase 2**

| Time | Referee | Mode / branch | Subject | Verdict | Citation |
|---|---|---|---|---|---|
| 12:29 | A-C2-012 | CROSS, ALGEBRAIC | A-C2-002 | CONFIRMED | tasks/A-C2-012/out/verdict.md, line 2 |
| 12:29 | A-C2-013 | CROSS, ANALYSIS | A-C2-002 | CONFIRMED | tasks/A-C2-013/out/verdict.md, line 1 |
| 12:32 | A-C2-014 | VERIFY | A-C2-011 | ACCEPT | tasks/A-C2-014/out/verdict.md, line 1 |
| 12:34 | A-C2-016 | CROSS, ALGEBRAIC | A-C2-011 | CONFIRMED | tasks/A-C2-016/out/verdict.md, line 1 |

Times: cell/phases.md, lines 14-16 and 18.

- A-C2-012 read Step 4 as a Schur complement at the last pivot followed by a diagonal rescaling (tasks/A-C2-012/out/verdict.md, TRANSLATION line 5).
- A-C2-013 read A(x) as a potential that is non-increasing under the reduction (tasks/A-C2-013/out/verdict.md, TRANSLATION line 4).
- A-C2-016 read Step 4 as the LDL^T pivot bound p_k >= cos^2(B_{k-1}) (tasks/A-C2-016/out/verdict.md, TRANSLATION line 4).

**Phase 2C (12:32), breaker A-C2-015**

- Verdict: PROOF-ROUTE-FOUND. Its contrapositive attack produced a complete forward Gram–Schmidt proof (tasks/A-C2-015/out/verdict.md, line 1; tasks/A-C2-015/out/proof.md, steps 1-10).
- Local analysis found that the optimum is not strict: at m = 3 the sum is identically pi/2 on the curve a1^2 + a2^2 = 1 (tasks/A-C2-015/out/local_analysis.md, lines 9-11).

**Agreement matrix (12:35).** CLASS: ROBUST (cell/matrix.md, lines 1-18).

| Proof | Own branch | Phase 2 verifier | ALGEBRAIC | ANALYSIS |
|---|---|---|---|---|
| A-C2-002 | - | ACCEPT (A-C2-005) | CONFIRMED (A-C2-012) | CONFIRMED (A-C2-013) |
| A-C2-010 | ALGEBRAIC | pending | (own) | pending |
| A-C2-011 | ANALYSIS | ACCEPT (A-C2-014) | CONFIRMED (A-C2-016) | (own) |

- Disputed steps: "none". Pending: "A-C2-010: Phase 2 verifier, ANALYSIS" (cell/matrix.md, lines 14-18).

**Gate (12:35)**

| Proof | Decision | Citation |
|---|---|---|
| A-C2-002 | VALID | cell/gate/A-C2-002.md, line 6; cell/gate/gate_report.md is byte-identical (out/verify/logs/11_inventory.txt) |
| A-C2-001 | GAP: "1 counted ACCEPT(s) of 2 needed; matrix is ROBUST through other proof(s), but A-C2-001 is not in matrix" | cell/gate/A-C2-001.md, line 6 |
| A-C2-011 | GAP: "1 counted ACCEPT(s) of 2 needed" | cell/gate/A-C2-011.md, line 6 |

- Both GAP reports end with "Next: repair + Phase 2C with this report" (cell/gate/A-C2-001.md, line 7; cell/gate/A-C2-011.md, line 7).
- There is no gate report for A-C2-003, -010, -015 or -017 (out/verify/logs/11_inventory.txt).

**Phase 3 (12:44), literature analyst A-C2-017**

- It split the cell into sub-problems S1-S5 and labelled none of them (c), i.e. unknown (tasks/A-C2-017/out/subproblems.md, lines 9-33).
- It wrote a further reproduction of the forward Gram–Schmidt proof (tasks/A-C2-017/out/proof.md, Steps 1-5).
- No source could be opened (tasks/A-C2-017/out/sources.md, lines 3-7).

**Phase 5.** This task, A-C2-018 (brief.md, lines 1-2).

### 4.3 Literature vs blind divergence

A-C2-003 compared its literature-informed proof with the two blind proofs (tasks/A-C2-003/out/divergence.md).

- **No contradiction** among the three. All share the reformulation to sum phi_k >= pi/2 and "essentially the same trig inequality in different guises" (lines 3-13).
- **Different routes:**
  - A-C2-001: minors D_k, forward, by contradiction.
  - A-C2-002: projection of x_m, backward, direct induction on m.
  - A-C2-003: Gram–Schmidt residuals t_k, forward, by contradiction.

  They are linked by t_k^2 = D_k/D_{k-1} (lines 15-27).
- **Provenance** (lines 29-33):
  - The minor form (001) and the projection (002) came from the blind runs.
  - The chain-sequence / continued-fraction view came from the literature "at technique level only, sources not opened".
  - Neither the lemma itself nor its use in an N = d+1 proof could be located.

### 4.4 Adversary and counterexample searches

No search found a violation. Every near miss is at an equality configuration. (At m = 3 every admissible chain is an equality case: tasks/A-C2-005/out/verdict.md, "Equality cases"; tasks/A-C2-015/out/contrapositive.md, lines 17-18.)

| Task | Script / seed | Range and count | Arithmetic | Result / nearest miss | Citation |
|---|---|---|---|---|---|
| A-C2-004 | out/cex/check.py, `random.seed(20260926)` (line 6) | 60000 attempts, 32942 admissible, m in [2,14] | exact rationals + 256-bit mpmath; 9439 flagged cases re-evaluated at 2048 bits | min slack -1.25e-69; 0 violations; max \|slack\| among flagged 6.3e-609 | tasks/A-C2-004/out/cex/check_log.txt, lines 4-5; tasks/A-C2-004/out/verdict.md, "Numerical checks" item 4 |
| A-C2-005 | out/cex/search.py, `random.seed(12345)` (line 6) | 2800 chains, m = 2..8; local search m = 3..6 | mpmath 50 digits | min margin -1.47e-47 at m = 3; local-search margins ~0, 1.2e-5, 1.1e-3, 1.7e-2 | tasks/A-C2-005/out/cex/log.txt, lines 2-9 |
| A-C2-006 | out/cex/search.py, `random.Random(12345)` (line 39), `random.Random(7)` (line 75) | 32176 exact admissible chains, m = 2..12 | arb balls, 256 bits | 0 certified violations | tasks/A-C2-006/out/cex/log.txt, lines 2-13 |
| A-C2-009 | out/cex/search.py and search_hiprec.py, `random.Random(2026)` (line 13 of each) | 3200 chains, m = 2..9; hill-climb m = 3..6; 19900 in-domain interval boxes | 50 and 100 digits | min slack -5.2e-26 at 50 digits and -3.8e-51 at 100 digits (rounding); hill-climb gaps 0, 1.3e-5, 6.5e-4, 6.3e-3; 0 interval violations in-domain. A first run flagged 200 boxes that lie outside the lemma's domain | tasks/A-C2-009/out/cex/log.txt, lines 3-8; tasks/A-C2-009/out/cex/log_hiprec.txt, lines 1-2; tasks/A-C2-009/out/verdict.md, Step 3 |
| A-C2-012 | out/cex/gram_search.py, `random.seed(12)` (line 23) | 32252 exact Gram chains, m = 3..12 | float arcsin | 0 violations below -1e-12; min -2.2e-15 | tasks/A-C2-012/out/cex/log.txt, lines 1-12 |
| A-C2-013 | out/cex/search.py, seed 7 (argv, line 17) | 11200 instances, m = 2..9 | arb, 200 bits | 0 certified violations; smallest certified lower bound -1.99e-58 at m = 3 | tasks/A-C2-013/out/cex/log_search.txt, lines 1-3 |
| A-C2-014 | out/cex/search.py, `random.seed(12345)` (line 9) | 33000 draws, 20114 admissible, m = 2..12 | mpmath 60 digits | 0 violations; min slack -2.2e-59 at m = 3 | tasks/A-C2-014/out/cex/log.txt, line 1; tasks/A-C2-014/out/verdict.md, sections 3/4/6 |
| A-C2-016 | out/cex/search.py, `random.seed(20260926)` (line 12) | 85820 admissible, m = 3..12 | float | 0 violations; min slack -1.3e-14 | tasks/A-C2-016/out/cex/log.txt, lines 1-2 |
| A-C2-015 (breaker) | out/cex_search/search.py, `random.Random(12345)` for R4 (line 53), `random.Random(777)` for R5 (line 66) | R3 equal weights m = 2..60; R4 random m = 2..12, 20000 each; R5 local search m = 3..10, 200 restarts each | float; wall 469 s | overall min gap -2.1e-8, "rounding at the equality point"; worst case saved exactly as m = 3, x = (1,0), (3/5,4/5), (0,1), margin 0 | tasks/A-C2-015/out/cex_search/log.txt, line 79; tasks/A-C2-015/out/tested.md, lines 2-7; tasks/A-C2-015/out/worst.json |

Arithmetic caveats:
- The A-C2-004 search used high precision with re-evaluation, not interval arithmetic (tasks/A-C2-004/out/verdict.md, item 4).
- The A-C2-012 arcsin sums are floating point, used only as a search (tasks/A-C2-012/out/verdict.md, "Limitation").

### 4.5 Dead ends

- `cell/deadends.md` is empty (0 bytes; out/verify/logs/11_inventory.txt).
- Every prover's stuck.md reads "none": A-C2-001, -002, -010, -011 and -017 (each tasks/<id>/out/stuck.md, line 1). A-C2-003's reads "Proof: none" (tasks/A-C2-003/out/stuck.md, line 1).
- The only recorded stuck point is literature access (tasks/A-C2-003/out/stuck.md, lines 3-6; tasks/A-C2-017/out/sources.md, lines 3-7).
- A-C2-015 recorded two naive routes and where they fail (tasks/A-C2-015/out/minimal_failing.md, lines 6-10):
  1. **Gershgorin route.** It fails at m = 3: a = (1/2, 1/2) has a1 + a2 = 1 but arcsin sum pi/3. That a is not admissible, "but the route cannot see this".
  2. **Angle-triangle-inequality route.** It "bounds in the wrong direction".

## 5. LITERATURE VS OURS

### 5.1 Existing results

The cell's statement, as a stand-alone lemma, was **not found in** the sources and queries listed in tasks/A-C2-003/out/sources.md (lines 18-31) and tasks/A-C2-017/out/sources.md (lines 20-31). Every fetch was blocked, so **no source was opened** and the absence of a match says nothing about prior existence (tasks/A-C2-003/out/sources.md, lines 3-7 and 30-31; tasks/A-C2-017/out/sources.md, lines 3-7 and 28-30). No source is used as a step of any proof.

| Reference | Link | Status (as recorded) | Contains argument? | Citation |
|---|---|---|---|---|
| D. Bilyk, R. W. Matzke, "On the Fejes Tóth problem about the sum of angles between lines", Proc. AMS 147 (2019) | https://arxiv.org/abs/1801.07837 | UNSURE; context only | unknown; not opened | tasks/A-C2-017/out/sources.md, line 11 |
| T. Lim, R. J. McCann, "On Fejes Tóth's conjectured maximizer for the sum of angles between lines", Appl. Math. Optim. (2021) | https://arxiv.org/abs/2007.08698 | UNSURE; context only | unknown; not opened | tasks/A-C2-017/out/sources.md, line 12 |
| F. Fodor, V. Vígh, T. Zarnócz, "On the angle sum of lines", Arch. Math. 106 (2016) 91–100 | https://link.springer.com/article/10.1007/s00013-015-0847-1 | UNSURE; context only | unknown; not opened | tasks/A-C2-017/out/sources.md, line 13 |
| "Maximizing expected powers of the angle between pairs of points in projective space" (authors not seen) | https://arxiv.org/pdf/2007.13052 | UNSURE; not used | unknown; not opened | tasks/A-C2-017/out/sources.md, line 14 |
| "Mathematical exploration and discovery at scale" (2025) | https://arxiv.org/abs/2511.02864 | UNSURE; relevance unknown | unknown; not opened | tasks/A-C2-017/out/sources.md, line 15 |
| R. Szwarc, "Chain sequences, orthogonal polynomials, and Jacobi matrices", J. Approx. Theory (1998) | https://www.sciencedirect.com/science/article/pii/S0021904596931093 | UNSURE; background technique only (Wall–Wetzel chain-sequence criterion, from memory) | unknown; not opened | tasks/A-C2-017/out/sources.md, line 16 |
| T. S. Chihara, "An Introduction to Orthogonal Polynomials", Gordon and Breach (1978), chapter on chain sequences | (book, no link) | UNSURE; background only | unknown; not opened | tasks/A-C2-017/out/sources.md, line 17 |

### 5.2 Our contribution (team artefacts)

| Artefact | Route | Status | Referee record | Citation |
|---|---|---|---|---|
| tasks/A-C2-002/out/proof.md (= cell/accepted/proof.md) | backward projection + trig lemma, induction on m | **PROVED** (gate VALID) | ACCEPT A-C2-005, ACCEPT A-C2-006 (GATE), CONFIRMED A-C2-012, CONFIRMED A-C2-013 | cell/gate/A-C2-002.md, lines 2-6; cell/matrix.md, line 7 |
| tasks/A-C2-001/out/proof.md | Gram minors, contradiction | not gated as valid: gate DECISION GAP (1 of 2 ACCEPTs; not in matrix) | ACCEPT A-C2-004 | cell/gate/A-C2-001.md, lines 2 and 6 |
| tasks/A-C2-011/out/proof.md | weighted AM-GM / quadratic form, linear independence | not gated as valid: gate DECISION GAP (1 of 2 ACCEPTs) | ACCEPT A-C2-014; CONFIRMED A-C2-016 | cell/gate/A-C2-011.md, lines 2 and 6; cell/matrix.md, line 9 |
| tasks/A-C2-003/out/proof.md | forward Gram–Schmidt residuals | one ACCEPT, no gate report | ACCEPT A-C2-009 | tasks/A-C2-009/out/verdict.md, line 1; out/verify/logs/11_inventory.txt |
| tasks/A-C2-010/out/proof.md | minors + partial sums alpha_k | no referee; matrix "pending" | none | cell/matrix.md, lines 8 and 18 |
| tasks/A-C2-015/out/proof.md | forward Gram–Schmidt (contrapositive) | no referee | none | cell/phases.md, lines 3-19 (no referee task has A-C2-015 as subject) |
| tasks/A-C2-017/out/proof.md | forward Gram–Schmidt (analyst reproduction) | no referee | none | cell/phases.md, lines 3-19 (no referee task has A-C2-017 as subject) |

These statuses are reported as the record gives them. Only A-C2-002's proof carries the claim status PROVED (brief.md, line 32).

## 6. REPRODUCIBILITY

**The proof needs no computation.** The accepted proof "uses no computation" and its script is "an optional floating-point sanity check only" (cell/accepted/proof.md, lines 3 and 83). The referees agree: G7 N/A in A-C2-005 (tasks/A-C2-005/out/verdict.md, line 11), and G7 PASS "no computation is load-bearing" in A-C2-006 (tasks/A-C2-006/out/verdict.md, line 12). Both scores also appear in cell/gate/A-C2-002.md, line 5. So no floating-point step in the proof needs an error bound, and the 10-minute limit applies to no step of the proof.

**Software.** Python 3.11.15, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0 (out/verify/logs/05_versions.txt). `/usr/bin/time` is not installed, so runtimes were measured with the bash builtin `time -p`.

**Commands run by this task.** Each was run on a copy under `out/verify/rerun/`, copied byte-identically from the record. Every log is saved under `out/verify/logs/`.

| # | Command | Output | Runtime | Log |
|---|---|---|---|---|
| 1 | `cd inbox/record && sha256sum cell/checklist.md` | `8d96a9f4…9887c84` | <1 s | 01_checklist_sha256.txt |
| 2 | `cd inbox/record/cell/accepted && sha256sum -c MANIFEST.sha256` | proof.md: OK, claims.md: OK | <1 s | 02_manifest_check.txt |
| 3 | `cmp` of the accepted proof.md and claims.md against tasks/A-C2-002/out/ | IDENTICAL | <1 s | 03_accepted_vs_A-C2-002.txt |
| 4 | `sha256sum` of the 7 proof.md files | hashes recorded | <1 s | 04_proof_hashes.txt |
| 5 | version query (python, sympy, mpmath, python-flint) | see Software above | <1 s | 05_versions.txt |
| 6 | `cd out/verify/rerun/A-C2-002/out/code && time -p .venv/bin/python3 sanity_lemma.py` | min 3.077760268865859e-12 over 1e6 float samples (not load-bearing) | real 0.63 s | 06_A-C2-002_sanity_lemma.txt |
| 7 | `cd out/verify/rerun/A-C2-006/out/cex && time -p .venv/bin/python3 search.py` | 32176 exact chains m = 2..12, 0 certified violations (arb 256-bit) | real 4.26 s | 07_A-C2-006_search.txt |
| 8 | `cd out/verify/rerun/A-C2-013/out/cex && time -p .venv/bin/python3 search.py 7` | 11200 instances, 0 certified violations (arb 200-bit) | real 2.10 s | 08_A-C2-013_search.txt |
| 9 | `cd out/verify/rerun/A-C2-012/out/cex && time -p .venv/bin/python3 gram_search.py` | 32252 chains, 0 violations (float arcsin, tolerance 1e-12) | real 2.44 s | 09_A-C2-012_gram_search.txt |
| 10 | diff of runs 6-9 against the saved record logs | NO DIFFERENCE in all four | <1 s | 10_diff_vs_record.txt |
| 11 | inventory (task folders, gate files, verdict files, deadends.md size) | 17 tasks; 5 gate files; 9 verdict.md | <1 s | 11_inventory.txt |
| 12 | `find tasks/A-C2-007 -type f` | brief.md only | <1 s | 12_A-C2-007_files.txt |

- Runs 7 and 8 use rigorous ball arithmetic. Run 6 and the arcsin sums in run 9 are floating point and serve only as searches or sanity checks.
- Run 10 compares against: tasks/A-C2-006/out/cex/log.txt, tasks/A-C2-013/out/cex/log_search.txt, tasks/A-C2-012/out/cex/log.txt and tasks/A-C2-013/out/cex/log_subject_sanity.txt.
- **All reruns took under 5 s, far below the 10-minute limit.**
- The longest recorded run in the whole record is A-C2-015's search, at 469 s wall (tasks/A-C2-015/out/cex_search/runtime.txt, line 1). That is under 10 minutes. This task did not rerun it.

## 7. LIMITATIONS

- **Agent agreement is evidence, not proof.** Two ACCEPTs, two CONFIRMED cross-checks and a ROBUST matrix (cell/gate/A-C2-002.md; cell/matrix.md) do not replace a human reading of cell/accepted/proof.md, Steps 1-7. In particular, humans must still check:
  - the reduction in Step 4, (4a)-(4e), including the use of the induction hypothesis in W through the isometry remark of Step 1;
  - the case split in Step 6.
- **Proofs with incomplete review.** Only A-C2-002's proof passed the gate.
  - A-C2-001 and A-C2-011 each received gate decision GAP, with 1 of 2 ACCEPTs (cell/gate/A-C2-001.md, line 6; cell/gate/A-C2-011.md, line 6).
  - A-C2-003 has one ACCEPT and no gate report.
  - A-C2-010, A-C2-015 and A-C2-017 have no referee (section 5.2).
- **Wording discrepancy.** The head's GATE FACTS say the proofs of A-C2-001 and A-C2-011 "were not gated" (brief.md, line 32). The record does contain gate reports for both, with DECISION GAP (cell/gate/A-C2-001.md; cell/gate/A-C2-011.md). This report gives the record's wording. Neither proof passed the gate.
- **A-C2-007.** It was created but has no output. Its inbox would have included referee verdicts (tasks/A-C2-007/brief.md, line 17; brief.md, line 32).
- **Equality configurations.** Equality configurations other than the known ones are not established. The checklist says "Whether other equality configurations exist: unknown" (cell/checklist.md, line 17), and A-C2-006 agrees (tasks/A-C2-006/out/verdict.md, section 4). This is not needed for the target.
- **Cross-cell item.** S5 relies on cell A-C1 being "gated VALID, final report filed" (cell/checklist.md, line 20). The A-C1 record is not in this task's inbox, so this report cannot confirm it.
- **Literature.** Not a single source was opened (section 5.1). Whether the lemma appears in the literature, for example as a step for N = d+1 lines, is not established (tasks/A-C2-017/out/subproblems.md, lines 35-36).
- **Cosmetic remarks by referees on the accepted proof** (unchanged here, since this report does not edit mathematics):
  - Remarks cites "out/code/sanity_lemma.py" for a file referees saw at subject/code/ (tasks/A-C2-005/out/verdict.md, line 41; tasks/A-C2-006/out/verdict.md, line 46).
  - The "Regime BLIND" line is irrelevant (same citations).
  - The continuity remark in Step 1 is superfluous (tasks/A-C2-012/out/verdict.md, line 26).
  - The second clause of the Step 5 lemma is unused (tasks/A-C2-012/out/verdict.md, line 27).
- **Unresolved disagreements.** None. The matrix lists "Disputed steps: none" (cell/matrix.md, line 15), and every verdict file in the record is ACCEPT, CONFIRMED or PROOF-ROUTE-FOUND (out/verify/logs/11_inventory.txt; section 4.2).

## 8. NEXT STEPS

1. **Human check of the accepted proof** (cell/accepted/proof.md, Steps 1-7), pinned by sha256 `3e08fea3…9e3ea1` (cell/accepted/MANIFEST.sha256, line 1).
2. **Optional backup proofs.** If a second, independent gated proof is wanted:
   - A-C2-001 and A-C2-011 each need one more counted ACCEPT. Their gate reports say "Next: repair + Phase 2C with this report" (cell/gate/A-C2-001.md, line 7; cell/gate/A-C2-011.md, line 7).
   - A-C2-010 is still pending a Phase 2 verifier and the ANALYSIS cross-check (cell/matrix.md, line 18).
3. **Literature provenance.** When web access allows, open the sources in section 5.1, in particular to see whether the lemma is used for N = d+1 lines (cell A-C3) (tasks/A-C2-017/out/subproblems.md, lines 35-36; tasks/A-C2-003/out/stuck.md, lines 3-6).
