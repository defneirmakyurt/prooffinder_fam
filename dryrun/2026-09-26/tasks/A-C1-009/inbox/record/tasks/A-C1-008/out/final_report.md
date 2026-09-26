# Final report — Cell A-C1 "Lines in the Plane"

Task A-C1-008, Phase 5, REPORT mode.
All citations are paths relative to `inbox/record/` of this task.

---

## 1. OUTCOME

**PROVED.**

- Cell status: **SOLVED** (`cell/gate/gate_report.md`, line "Next: PROVED on board").
- Claim status: **PROVED** for the target claim "S(l_1..l_N) <= (pi/2) floor(N^2/4), all N>=0, repetitions allowed" (`cell/accepted/claims.md`, row "TARGET", citing `proof.md, Steps 11-12`).
- Gate decision: "VALID — two referees ACCEPT the same proof version with complete checklists (A-C1-004, A-C1-006); matrix not run; statement checked by head" (`cell/gate/gate_report.md`, DECISION line).
- The accepted proof declares itself: "Status: **cell A-C1 solved** (complete proof, no [GAP]; no step rests on computation)" (`cell/accepted/proof.md`, line 2).
- Supporting claim statuses in the accepted claims table, all **PROVED** (`cell/accepted/claims.md`, rows 1–12): parametrisation (Step 1), well-definedness of theta (Step 2), the function rho (Step 3), the angle formula (Step 4), the cut function g (Step 5), period integrals (Step 6), the overlap lemma (Step 7), the cut identity (Step 8), the integer bound (Step 9), the pair count (Step 10), the target (Steps 11–12), sharpness (Step 13, marked "not required").

## 2. STATEMENT

Exact statement, as recorded in `cell/target.md`:

> A-C1 "Lines in the Plane" (1 point, written proof). Verbatim: "We begin in the plane (d = 2), where the conjectured optimum splits the N lines as evenly as possible between two perpendicular directions. Let l_1, ..., l_N be lines in R^2. Prove that S(l_1, ..., l_N) <= (pi/2) floor(N^2/4)."
> Exact target: for every N and all lines l_1, ..., l_N through the origin of R^2 (repetitions allowed), S(l_1, ..., l_N) = sum_{1<=i<j<=N} theta(l_i, l_j) <= (pi/2) floor(N^2/4), where theta(l, l') in [0, pi/2] is the acute (non-obtuse) angle between the lines, theta = arccos|<x, x'>| for spanning unit vectors x, x'. Definitions exactly as in inbox/statement.md.
> Hand-in: a complete written proof; a step may rest on computation only with code included, running under 10 minutes, and rigorous (exact or interval arithmetic, or a bound on the numerical error). Say whether the cell is solved or partial.

Checklist hash (sha256 of `cell/checklist.md`):

```
70046abcb09ea7c059d24da3a3dca7d402243db8ec3a4dc3373a26af5d03e5dd
```

Computed with the command recorded under RUN-1 in section 6.

The checklist has a generic Part G (G1–G9) and a referee-only Part S (S1–S6) (`cell/checklist.md`, sections "Part G" and "Part S").

## 3. RESULT

The final proof is `cell/accepted/proof.md` (sha256 `fc29d1e656049f35883f3f162a350a539f04a30e17d51fc558f10bf810edae5e`, pinned in `cell/accepted/MANIFEST.sha256`). It is byte-identical to `tasks/A-C1-001/out/proof.md` (verified under RUN-2, section 6).

Its structure, by step (`cell/accepted/proof.md`, Steps 1–13):

1. **Step 1** — every line through 0 in R^2 is spanned by u(a) = (cos a, sin a) for some a in [0, pi).
2. **Step 2** — theta is independent of the choice of spanning unit vectors, and <u(a), u(b)> = cos(a - b).
3. **Step 3** — rho(z) = min_{k in Z} |z - k pi| is attained, lies in [0, pi/2], is pi-periodic and even, equals |z| on [-pi/2, pi/2] and z + pi on [-pi, -pi/2].
4. **Step 4** — arccos|cos(a - b)| = rho(a - b), so theta(l_a, l_b) = rho(a - b).
5. **Step 5** — the cut function g(z) = 1[rho(z) < pi/4] is pi-periodic, even, and a step function on bounded intervals.
6. **Step 6** — the integral of a pi-periodic function over any period equals int_0^pi; int_0^pi g = pi/2.
7. **Step 7** — overlap lemma: int_{-pi/2}^{pi/2} g(s) g(s - theta) ds = pi/2 - theta for theta in [0, pi/2].
8. **Step 8** — cut identity: int_0^pi |g(t - x) - g(t - y)| dt = 2 rho(x - y) for all real x, y.
9. **Step 9** — k(N - k) <= floor(N^2/4) for all integers N >= 0 and k, proved separately for even and odd N.
10. **Step 10** — for each t, sum_{i<j} |g(t - a_i) - g(t - a_j)| = k(t)(N - k(t)) with k(t) = #{i : g(t - a_i) = 1}.
11. **Step 11** — combining: S = (1/2) int_0^pi k(t)(N - k(t)) dt <= (1/2) pi floor(N^2/4) = (pi/2) floor(N^2/4).
12. **Step 12** — degenerate cases N = 0, 1 (empty sum, both sides 0) and repeated lines.
13. **Step 13** — sharpness (explicitly marked "not required by the cell"): floor(N/2) copies of R u(0) and the rest of R u(pi/2) attain the bound for every N.

The proof states its own scope: "What is established: the full target for every N >= 0 (N = 0, 1 trivially), all lines through the origin of R^2, with repetitions. What is not claimed: characterisation of all equality cases (not asked). No computation is used in the proof" (`cell/accepted/proof.md`, final paragraph).

Two further complete proofs of the same statement exist in the record but were not the accepted artefact:

- `tasks/A-C1-002/out/proof.md`, Steps 0–13: doubling of direction angles (u_i = 2 a_i), a Crofton-type semicircle identity (Step 10), the same counting step (Step 11) and integer bound (Step 12).
- `tasks/A-C1-003/out/proof.md`, Steps B1–B7 (perpendicular-pair invariance, existence of a maximiser, a rotation argument, induction N -> N-2) and Steps A1–A4 (quarter-turn cut averaging).

There is no open lemma: `tasks/A-C1-001/out/stuck.md` reads "none", `tasks/A-C1-002/out/stuck.md` reads "none", and `tasks/A-C1-003/out/stuck.md` reads "none. Both written proofs are complete." `cell/deadends.md` is empty.

## 4. HOW IT WAS REACHED

### Timeline

The phases index (`cell/phases.md`) lists seven tasks:

| Task | Phase | Role | Regime | Mode | Subject | Created |
|---|---|---|---|---|---|---|
| A-C1-001 | 1 | prover | BLIND | - | - | 12:34 |
| A-C1-002 | 1 | prover | BLIND | - | - | 12:34 |
| A-C1-003 | 1L | literature | LITERATURE | SOLVE | - | 12:39 |
| A-C1-004 | 2 | referee | CLEAN-ROOM | VERIFY | A-C1-001 | 12:39 |
| A-C1-005 | 2 | referee | CLEAN-ROOM | VERIFY | A-C1-002 | 12:39 |
| A-C1-006 | GATE | referee | CLEAN-ROOM | GATE | A-C1-001 | 12:43 |
| A-C1-007 | 2 | referee | CLEAN-ROOM | VERIFY | A-C1-003 | 12:46 |

(source: `cell/phases.md`, table rows). The gate report is timestamped 12:47 (`cell/gate/gate_report.md`, header line). No task carried a BRANCH or SUBJECT beyond the referee subjects above (`cell/phases.md`, Branch column all "-").

### Phase 1 — two blind provers

**A-C1-001** was briefed BLIND with the instruction "Derive everything from first principles... if you recognise a known theorem about this problem, do not use it, work the argument out yourself. Cite no papers or authors." (`tasks/A-C1-001/brief.md`, final paragraph). Its plan (`tasks/A-C1-001/out/plan.md`, "Idea") was: "represent each line by a direction angle a in [0, pi); theta becomes the distance rho(a-b) of a-b to pi*Z. Write rho as an average over t of a 'cut' indicator (one open quarter-arc of the circle R/piZ, centred at t), then count cut pairs." The ladder R1–R7 was completed with every rung marked PROVED (`tasks/A-C1-001/out/plan.md`, Ladder). Stuck points: none (`tasks/A-C1-001/out/stuck.md`).

**A-C1-002** was briefed BLIND in parallel. Its plan idea (`tasks/A-C1-002/out/plan.md`, "Idea"): "double the direction angles, so that theta becomes half the arc distance on the circle; write the arc distance as an average over half-open semicircles of 'exactly one of the two points lies in the semicircle' (a Crofton-type identity); for each semicircle the number of separated pairs is k(N-k)." Rungs R1–R8 all PROVED (`tasks/A-C1-002/out/plan.md`, Ladder). Stuck points: none (`tasks/A-C1-002/out/stuck.md`).

### Phase 1L — literature

**A-C1-003** searched the literature and also attempted the cell (`tasks/A-C1-003/brief.md`, "Phase 1L" instructions). Searches run are listed in `tasks/A-C1-003/out/sources.md`, section "Searches run": WebSearch "Fejes Toth sum of angles between lines conjecture planar case proof"; WebSearch "Fodor Vigh Zarnocz 'angle sum of lines' Archiv der Mathematik"; WebSearch "arXiv 2024 2025 Fejes Toth conjecture sum of angles between lines d+1 lines proof"; WebSearch "'sum of angles' lines Fejes Toth 'Mathematical exploration and discovery at scale' AlphaEvolve"; and the StackExchange API for MathOverflow question 173712. The third search returned "nothing newer on the planar case" and the fourth "nothing specific" (same section).

It produced two proofs: Proof B from the Fodor–Vigh–Zárnocz technique, Proof A from the Bilyk–Matzke quadrant/Stolarsky identity (`tasks/A-C1-003/out/proof.md`, header bullets).

### Literature vs blind divergence

`tasks/A-C1-003/out/divergence.md`, section "Verdicts": "A-C1-001: claims cell solved, complete proof, no gaps. A-C1-002: same. A-C1-003 (here): same, by two proofs." and "No contradiction anywhere: all three reach exactly the target S <= (pi/2) floor(N^2/4) for all N >= 0, repetitions allowed, and all note sharpness via floor(N/2)/ceil(N/2) copies of two perpendicular lines."

Approach mapping (`tasks/A-C1-003/out/divergence.md`, table "Approaches"):

- A-C1-001's cut indicator g = 1[rho(z) < pi/4] is "the same as the L2 quadrant-discrepancy / Stolarsky identity for S^1 in Bilyk-Matzke Sec. 4.3: their Q(x) = {y : abs(x.y) > sqrt2/2} is exactly {rho < pi/4} ... Found blind, independently."
- A-C1-002's doubled-circle Crofton identity is "a variant of Bilyk-Matzke Sec. 4.3. Its integer step (k(N-k) <= N^2/4 plus integrality) is slicker than the parity split in A-C1-001 and here."
- A-C1-003's Proof B "Idea from FVZ 2016 Section 2 ... Not used by either blind run."

Substantive differences recorded in the same file, section "Where the approaches differ in substance": (1) global identity vs variational argument — the cut-averaging proofs give an exact deficit formula, Proof B does not; (2) which planar fact is used — cut averaging uses the Crofton property of the circle R/pi Z, Proof B uses theta(l,m) + theta(l',m) = pi/2 for perpendicular l, l', and the same file records that "In R^d, d >= 3, sum_i theta(e_i, m) over an orthonormal frame is NOT constant (e.g. d = 3: m = e_1 gives pi, m = (1,1,1)/sqrt3 gives 3 arccos(1/sqrt3) ~ 2.86 < pi), so B1-B2 do not extend verbatim"; (3) no run characterises all maximisers.

Provenance (`tasks/A-C1-003/out/divergence.md`, "Provenance summary"): "From the blind runs only: nothing I used. From the literature: cut-averaging identity (Bilyk-Matzke Sec. 4.3 ...), perpendicular-pair invariance and the rotation step (FVZ Sec. 2)."

### Phase 2 and the gate — three referee passes

- **A-C1-004** (VERIFY, subject A-C1-001): **ACCEPT**, STATEMENT MATCH yes, FIRST PROBLEM none; all of G1–G9 and S1–S6 PASS except G4 N/A (`tasks/A-C1-004/out/verdict.md`, VERDICT/CHECKLIST block). It re-derived every step (`tasks/A-C1-004/out/verdict.md`, section 2) and concluded "Unjustified, circular or false steps found: **none**."
- **A-C1-005** (VERIFY, subject A-C1-002): **ACCEPT**, STATEMENT MATCH yes, FIRST PROBLEM none; same PASS/N-A pattern (`tasks/A-C1-005/out/verdict.md`, CHECKLIST block).
- **A-C1-006** (GATE, subject A-C1-001): **ACCEPT**, STATEMENT MATCH yes, FIRST PROBLEM none; same PASS/N-A pattern (`tasks/A-C1-006/out/verdict.md`, CHECKLIST block).
- **A-C1-007** (VERIFY, subject A-C1-003): **ACCEPT**, STATEMENT MATCH yes, FIRST PROBLEM none; all G1–G9 and S1–S6 PASS, with G4 PASS rather than N/A because Proof B has an invariant (`tasks/A-C1-007/out/verdict.md`, CHECKLIST block, G4 line: "the invariant in B5 (F_N constant along the rotation a_N -> a_N + e, 0 <= e <= e*) is proved from C = 0 and P = Q; strictness is needed only for d > 0 in B4, which holds").

### Agreement matrix

The matrix was not run: "Matrix: not run" (`cell/gate/gate_report.md`, Matrix line; repeated in `cell/gate/A-C1-001.md`). The head checked the statement word for word: "Statement checked word for word by head: yes" (same line source).

De facto agreement across the record: three independent write-ups (A-C1-001, A-C1-002, A-C1-003 with two proofs) reach the same inequality with the same constant, and four referee passes accept (`tasks/A-C1-003/out/divergence.md`, "Verdicts"; the four verdict files cited above).

### Adversary (counterexample) searches

- **A-C1-004** (`tasks/A-C1-004/out/verdict.md`, section 6 and CEX SEARCH line): exhaustive exact grid of multiples of pi/12 for N <= 8; random rational configurations with N <= 14 including forced repetitions; float hill-climb N = 2..12 with 40 starts each, best points recertified exactly after rational rounding; exact tests of Steps 7, 8, 9, 10, 11; Step 9 exhaustively for N <= 300, k in [-20, N+20]. "Found: no violation of the target and no failure of any intermediate claim." Near misses: in section 3, "The best values approach the bound, and reach it exactly for odd N."
- **A-C1-005** (`tasks/A-C1-005/out/verdict.md`, section 6): exact checks E1–E8 including an exhaustive grid over 863163 multisets on grids m in {2,...,10,12,24,60} with N up to 12 (see the table there); and `hill_interval.py` with 200-bit arb ball arithmetic, N = 2..12, 6 random starts x 6000 steps, 66 final configurations — "36 configurations certified strictly below the bound. 30 overlap the bound to within about 1e-55. These are all odd N, consistent with the open set of maximisers. 0 certified above the bound."
- **A-C1-006** (`tasks/A-C1-006/out/verdict.md`, CEX SEARCH and RAN lines): Step 8 on 3028 exact rational pairs (denominators <= 997), Step 7 on 1003 exact theta, Step 11 on 1000 exact configurations N <= 12, Step 9 for N = 0..300 and k = -100..400, exhaustive exact grid D = 12 for N = 0..7, float ascent N = 2..14 with 30 restarts x 3000 steps rechecked exactly as dyadic rationals — "0 exact violations".
- **A-C1-007** (`tasks/A-C1-007/out/verdict.md`, section 6): exact grids D = 12 (N <= 10), D = 7 (N <= 12), D = 10 (N <= 10), D = 24 (N <= 6); float hill-climbing N = 2..16 with 60 restarts each, "max excess 1.4e-14"; "Result: no counterexample to the statement or to any intermediate claim."

Seeds: the only seed recorded in the record is 12345 for `tasks/A-C1-002/out/code/sanity_check.py` (`tasks/A-C1-002/out/code/README.md`, "Measured" line, and `tasks/A-C1-005/out/verdict.md`, section 3). The other searches do not record a seed in their artefacts.

### Stuck points and dead ends

`cell/deadends.md` is empty (0 bytes). All three stuck files read "none" (`tasks/A-C1-001/out/stuck.md`, `tasks/A-C1-002/out/stuck.md`, `tasks/A-C1-003/out/stuck.md`). No triage decision (branch kept, dropped or re-admitted) appears anywhere in the record: every brief in `cell/phases.md` carries "BRANCH: -".

Non-blocking issues raised by referees, none of which changed the proof:

- A-C1-004, OTHER ISSUES: "proof.md cites the script as out/code/check_cut_identity.py (inbox path subject/code/); the script docstring says 'Step 12' for check 2, the README says Step 11. Neither affects the proof."
- A-C1-005, OTHER ISSUES: "Step 6 uses F(x + 2pi n) = F(x) for integer (possibly negative) n, an unstated one-line induction from 5(b); 'Tools used' lists the cosine subtraction formula while Step 3 uses the addition formula (the same fact)."
- A-C1-006, OTHER ISSUES: "(i) Step 8 uses the reflection substitution s = -r while the Conventions paragraph lists only t = s + c ...; (ii) proof.md refers to out/code/check_cut_identity.py, shipped as subject/code/."
- A-C1-007, OTHER ISSUES: "B4 uses evenness of rho (0.3(b)) silently for pairs (i, n) with i < n; Remark's 'for odd N there are others' fails for N = 1 (non-load-bearing, in the 'not claimed' section); sources.md referenced but not in the inbox".

## 5. LITERATURE VS OURS

### Existing results (from `tasks/A-C1-003/out/sources.md`)

| Reference | Link | What it contains | Status tag in the record | Contains the argument? |
|---|---|---|---|---|
| F. Fodor, V. Vigh, T. Zárnócz, "On the angle sum of lines", Arch. Math. 106 (2016) 91–100, Section 2 "The planar case", Theorem 2.1 | http://www.math.u-szeged.hu/~vigvik/preprints/egyenesekszogei.pdf (published: https://doi.org/10.1007/s00013-015-0847-1) | "Theorem 2.1 is exactly the cell's inequality (k^2 pi/2 for n = 2k, k(k+1) pi/2 for n = 2k+1)" | PROVED | "yes (short; relies on 'a simple compactness argument', 'By symmetry, we may clearly assume', 'The case ... being obvious', and does not spell out why the right/left count stays favourable during the rotation)"; opened as the preprint, journal version paywalled and not opened |
| Same paper, Theorem 1.1 (R^3) and Introduction (Fejes Tóth solved d = 3, n <= 6; recursive bound S(n,d) <= n S(n-1,d)/(n-2)) | same | neighbour context only | PROVED (as stated there) | "yes (Thm 1.1); the Fejes Toth n <= 6 result only cited" |
| D. Bilyk, R. W. Matzke, "On the Fejes Tóth problem about the sum of angles between lines", Proc. AMS 147 (2019) 51–59 (arXiv 2018), Conjecture 1.1, Section 4 and 4.3 | https://arxiv.org/abs/1801.07837 ; https://ar5iv.labs.arxiv.org/html/1801.07837 | Says the S^1 case "has been settled in [9], [10]"; gives alternative proofs (Chebyshev, Fourier, and the L2 quadrant-discrepancy / Stolarsky principle) | PROVED | "yes for S^1 (as summarised; exact wording of the odd-N integrality step not verified by me)"; opened through a fetch summary only |
| F. Petrov, "maximum sum of angles between n lines", MathOverflow 173712 (2014), answer 283104 by D. Bilyk (2017), comments | https://mathoverflow.net/q/173712 | Question states the conjecture for all d; Petrov's comment asserts the d = 2 optimum; Bilyk's answer gives arccos|t| <= pi/2 - (7pi/16) t^2; Petrunin's 2022 comment gives an orthogonality-graph argument for n = d+1 | "d=2: CONJECTURED/asserted in the post; answer: PROVED (short inequality argument, the pointwise inequality only 'proved' by a picture)" | "d=2: no (only asserted); answer: yes, but the key pointwise inequality is justified by a graph only" |
| Y.-H. Lim, R. J. McCann, "On Fejes Tóth's conjectured maximizer for the sum of angles between lines", Appl. Math. Optim. (2021) | https://arxiv.org/abs/2007.08698 | Abstract only; neighbour context | PROVED (as stated in abstract) | not checked; abstract only, fetch summary |
| T. Lim, R. J. McCann, "Maximizing expected powers of the angle between pairs of points in projective space", Probab. Theory Related Fields (2022) | https://arxiv.org/abs/2007.13052 | "only seen as a search-result title; not used" | UNSURE | unknown; not opened |
| L. Fejes Tóth, "Über eine Punktverteilung auf der Kugel", Acta Math. Acad. Sci. Hungar. 10 (1959) 13–19 | (not online) | origin of the conjecture (d = 3); per FVZ intro, solved d = 3 for n <= 6 | "PROVED per FVZ (cited only)" | unknown; not opened |

Nothing newer on the planar case was found in the sources searched (`tasks/A-C1-003/out/sources.md`, "Searches run", third bullet: "nothing newer on the planar case").

### Our contribution

| Artefact | What it is | Status |
|---|---|---|
| `cell/accepted/proof.md` (= `tasks/A-C1-001/out/proof.md`), Steps 1–13 | Self-contained proof of the full target by cut averaging over the circle R/pi Z; written BLIND, with "no citations" (`tasks/A-C1-001/out/plan.md`, "Checklist-G pass", G6) | PROVED (`cell/accepted/claims.md`, TARGET row; `cell/gate/gate_report.md`, DECISION) |
| `cell/accepted/claims.md` | Claim-by-claim table pinning each claim to a step | PROVED for rows 1–12 as tagged in that file |
| `tasks/A-C1-002/out/proof.md`, Steps 0–14 | Independent blind proof via angle doubling and a semicircle Crofton identity | ACCEPT by referee A-C1-005 (`tasks/A-C1-005/out/verdict.md`, VERDICT line); not the accepted artefact |
| `tasks/A-C1-003/out/proof.md`, Steps B1–B7 | Rigorous write-up of the FVZ variational argument; `tasks/A-C1-003/out/divergence.md` records "the maximiser-based rigorous form of the FVZ argument (Steps B3-B6), including the first-order balance lemma B4" as written up there, filling steps FVZ leaves as "clearly"/"obvious"/"by symmetry" | ACCEPT by referee A-C1-007 (`tasks/A-C1-007/out/verdict.md`, VERDICT line); not the accepted artefact |
| `tasks/A-C1-003/out/proof.md`, Steps A1–A4 | Full write-up of the Bilyk–Matzke Section 4.3 route | ACCEPT by referee A-C1-007 (same source) |
| `tasks/A-C1-001/out/code/check_cut_identity.py` | Exact (fractions.Fraction, stdlib) sanity check of Steps 8 and 11 | CHECKED, explicitly non-load-bearing: "The proof in ../proof.md does NOT rest on any computation" (`tasks/A-C1-001/out/code/README.md`, line 3) |

Per the cell's rules, "citing a published result for the statement you are asked to prove does not count" (`tasks/A-C1-001/brief.md`, RULES line); the accepted proof cites nothing (`tasks/A-C1-004/out/verdict.md`, G6 line: "no circularity; the only external inputs are polar coordinates, the cosine subtraction formula and linearity/monotonicity/translation of Riemann integrals of step functions; no citation of the target").

## 6. REPRODUCIBILITY

### Software

- `python3` — Python 3.14.0 (measured, RUN-0 below). The brief's venv interpreter `/Users/raducucu/bainsahackathon/.venv/bin/python3` is also Python 3.14.0 (measured, RUN-0). All scripts rerun below are stdlib-only and were run with plain `python3`.
- `shasum` (macOS, Darwin 25.6.0), `/usr/bin/time -p`.

### Files under `out/`

Byte-identical copies of the record's scripts were placed in `out/verify/` and run there. Verified identical by sha256 (RUN-3):

| `out/verify/` file | source in the record | sha256 |
|---|---|---|
| `check_cut_identity.py` | `tasks/A-C1-001/out/code/check_cut_identity.py` | `4554394cdbb44a1ed7f4a11804b364a34580da2b22b74025269bb679fa98e9ea` |
| `referee_004_check.py` | `tasks/A-C1-004/out/cex/check.py` | `b8f4d5d3bc7ea999314bac07f94f4ceb6f61e6fea68781a3e5bca3042485d34f` |
| `referee_004_s5.py` | `tasks/A-C1-004/out/cex/s5.py` | `30405a37944af413380f644406ce3cfea57bbcac31b14ab912fa85894d4429f3` |
| `referee_006_checks.py` | `tasks/A-C1-006/out/cex/referee_checks.py` | `19e7e185bb734cb9c54cec9aab45b629d9b5d2c70998fa75cad86e3afb67e438` |
| `referee_006_crosscell_s5.py` | `tasks/A-C1-006/out/cex/crosscell_s5.py` | `f057266fd9b0e13f38c710cb46ca93689bf88a525478603ddb1defc7a8d5fa24` |

Logs of the timed runs are in `out/verify/logs/`.

### Runs executed for this report (all measured with `/usr/bin/time -p`)

- **RUN-0** (versions): `/Users/raducucu/bainsahackathon/.venv/bin/python3 -V ; python3 -V` → `Python 3.14.0` twice. COMPLETED.
- **RUN-1** (checklist hash): `shasum -a 256 /Users/raducucu/bainsahackathon/run/tasks/A-C1-008/inbox/record/cell/checklist.md` → `70046abcb09ea7c059d24da3a3dca7d402243db8ec3a4dc3373a26af5d03e5dd`. COMPLETED.
- **RUN-2** (accepted artefacts pinned and identical to A-C1-001's proof): `cd /Users/raducucu/bainsahackathon/run/tasks/A-C1-008/inbox/record/cell/accepted && shasum -a 256 -c MANIFEST.sha256` → `proof.md: OK`, `claims.md: OK`; and `shasum -a 256 inbox/record/cell/accepted/proof.md inbox/record/tasks/A-C1-001/out/proof.md` → both `fc29d1e656049f35883f3f162a350a539f04a30e17d51fc558f10bf810edae5e`. COMPLETED.
- **RUN-3** (script copies byte-identical): `shasum -a 256` on the five files in `out/verify/` and their five sources — all five pairs match (table above). COMPLETED.
- **RUN-4**: `cd /Users/raducucu/bainsahackathon/run/tasks/A-C1-008/out/verify && /usr/bin/time -p python3 check_cut_identity.py 48 7 8`. Range: check1 grid D = 48, 2304 pairs; check2 all multisets of N = 0..7 angles on grid D2 = 8. Output `check1: grid D=48, pairs=2304, failures=0`, `equal = True` for every N = 0..7, `ALL OK`. COMPLETED, real 0.40 s (log `out/verify/logs/check_cut_identity_48_7_8.txt`). Matches `tasks/A-C1-001/out/code/README.md` ("failures=0 ... ALL OK; real 0.41 s").
- **RUN-5**: `/usr/bin/time -p python3 check_cut_identity.py 45 6 9`. Range: check1 grid D = 45, 2025 pairs; check2 N = 0..6 on grid D2 = 9. Output `check1: ... failures=0`, `ALL OK`; for even N the odd grid gives max S strictly below the bound (`N=2: 4/9 < 1/2`, `N=4: 17/9 < 2`, `N=6: 13/3 < 9/2`), as the README predicts ("the grid lacks perpendicular pairs"). COMPLETED, real 0.45 s (log `out/verify/logs/check_cut_identity_45_6_9.txt`). README reports real 0.26 s.
- **RUN-6**: `/usr/bin/time -p python3 referee_004_s5.py`. Range N = 0..10000. Output `S5: N=0..10000, failures = 0`. COMPLETED, real 0.05 s (log `out/verify/logs/referee_004_s5.txt`). `tasks/A-C1-004/out/verdict.md` RAN line reports 0.12 s.
- **RUN-7**: `/usr/bin/time -p python3 referee_006_crosscell_s5.py`. Range N = 0..10000 plus the S6 values N = 2..5 and the Setting example at d = 2, k = 0,1,2. Output `failures = 0`; `N=2..5: balanced split S/pi = 1/2, 1, 2, 3 = bound/pi`. COMPLETED, real 0.03 s (log `out/verify/logs/referee_006_crosscell_s5.txt`). `tasks/A-C1-006/out/verdict.md` RAN line reports 0.03 s.
- **RUN-8**: `/usr/bin/time -p python3 referee_006_checks.py 3000`. Ranges: Step 8 on 3000+28 exact rational (x,y) pairs with denominators <= 997 and |x|,|y| <= 5; Step 7 on 1003 exact rational theta in [0, 1/2] (units of pi); Step 11 on 1000 exact random configurations N <= 12 (30% with forced repeats); Step 9 for N = 0..300, k = -100..400; exhaustive exact grid D = 12 for N = 0..7; float ascent N = 2..12. Output: all `failures=0` / `violations=0`, exhaustive grid `attained=True` for N = 0..7. COMPLETED, real 7.04 s (log `out/verify/logs/referee_006_checks.txt`). `tasks/A-C1-006/out/verdict.md` RAN line reports 4.27 s.
- **RUN-9**: `/usr/bin/time -p python3 referee_004_check.py`. Ranges: Step 4 float sanity on 200000 random (a,b) in [-10,10]^2; Step 7 exact for all theta = k/D, D = 1..60 (960 values); Step 8 exact on 3000 random rational (x,y) in [-3,3]^2 with denominators <= 97; Steps 10–11 exact on 1500 random rational configurations N = 0..14 (30% with a forced repeat); Step 9 for N = 0..300, k = -20..N+20; exhaustive exact grid D = 12 for N = 0..8; float local search N = 2..12 with exact recertification; equality configurations N = 1..30. Output: all `failures = 0`, all `violations = 0`, `exact <= bound: True` for every N in the local search, `eq=True` on the exhaustive grid for N = 0..8. COMPLETED, real 12.44 s (log `out/verify/logs/referee_004_check.txt`). `tasks/A-C1-004/out/verdict.md` RAN line reports 13.36 s.

### Floating point

- No step of the accepted proof uses floating point: "No computation is used in the proof" (`cell/accepted/proof.md`, final paragraph); confirmed by `tasks/A-C1-004/out/verdict.md`, G7 line, and `tasks/A-C1-006/out/verdict.md`, G7 line.
- Floating point appears only in non-load-bearing checks, always with a recorded error bound:
  - RUN-8 log line: `step4 (float sanity only): max |arccos|cos(pi z)| - pi rho(z)| over 3000 z in [-20,20] = 1.260e-13`.
  - RUN-9 log line: `A Step4 float sanity: 200000 random (a,b) in [-10,10]^2, max |arccos|cos(a-b)| - rho(a-b)| = 1.997e-12 (tol 1e-9) OK`.
  - `tasks/A-C1-002/out/code/README.md`, item 3: a midpoint Riemann sum with 20000 nodes, "the error is within the grid resolution (about 2h = 6.3e-4)"; `tasks/A-C1-005/out/verdict.md`, section 3, measured "identity error 6.0e-4 within the Riemann-sum resolution 6.28e-4".
  - Rigorous interval arithmetic where a certificate was wanted: `tasks/A-C1-005/out/cex/hill_interval.py`, "200-bit arb ball arithmetic", results "36 configurations certified strictly below the bound ... 0 certified above the bound" (`tasks/A-C1-005/out/verdict.md`, section 6). I did not rerun this script (it needs python-flint from the venv).
  - Float hill-climb values approaching the bound are documented as noise at equality, not violations: `tasks/A-C1-005/out/verdict.md`, section 3 ("gaps of about -3e-11 for odd N are float noise at equality"); `tasks/A-C1-007/out/verdict.md`, section 6 ("max excess 1.4e-14").

### 10-minute limit

Confirmed. Every run above completed in at most 12.44 s (RUN-9), far under 10 minutes. The longest runtime recorded anywhere in the record is 22.53 s (`tasks/A-C1-005/out/verdict.md`, RAN line for `check_exact.py`), also far under the limit. The accepted proof rests on no computation at all (`cell/accepted/proof.md`, final paragraph), so the 10-minute rule does not bind any proof step.

## 7. LIMITATIONS

- **agent agreement is evidence, not proof.**
- Not established: any characterisation of the equality cases. The accepted proof states "What is not claimed: characterisation of all equality cases (not asked)" (`cell/accepted/proof.md`, final paragraph). The checklist records this as open: "Whether other configurations also attain equality: unknown (not given)" (`cell/checklist.md`, S2).
- Not established: anything for d >= 3, or for cells C2–C6. `tasks/A-C1-002/out/proof.md`, final section: "Not established / not claimed: anything about d >= 3". `tasks/A-C1-003/out/divergence.md`, section "Where the approaches differ in substance", point 2, records that both planar routes fail to extend verbatim to d >= 3.
- **The agreement matrix was not run** (`cell/gate/gate_report.md`, Matrix line). The gate rested on two referee ACCEPTs plus the head's word-for-word statement check (same file, DECISION line).
- **Deviating runtimes.** My reruns did not reproduce the referees' measured times exactly: RUN-8 took 7.04 s against 4.27 s reported (`tasks/A-C1-006/out/verdict.md`, RAN line) and RUN-5 took 0.45 s against 0.26 s (`tasks/A-C1-001/out/code/README.md`). All check outputs (failures, violations, maxima) matched exactly; only wall-clock times differ.
- **Sources read through a summarising tool.** `tasks/A-C1-003/out/sources.md`, header: "'opened (fetch-summary)' = read through the WebFetch tool, which returns a model-extracted summary/quotes of the page, not the raw text; treat exact wording as UNSURE." This applies to Bilyk–Matzke and Lim–McCann. `tasks/A-C1-003/out/stuck.md` flags the same: "the exact wording of Bilyk-Matzke Sec. 4.3 was read through a fetch summary, which affects sources.md attribution only, not the proofs." The Fodor–Vigh–Zárnócz journal version was not opened (paywalled); only the authors' preprint was.
- **Unresolved cosmetic remarks left in the record, not fixed in the accepted artefact** (listed verbatim in section 4): the docstring/README step-number mismatch in `check_cut_identity.py` and the path `out/code/` vs `subject/code/` (A-C1-004, A-C1-006); the unstated integer-n periodicity induction in Step 6 of `tasks/A-C1-002/out/proof.md` and its "subtraction" vs "addition" wording (A-C1-005); the reflection substitution s = -r not listed in the Conventions paragraph of `cell/accepted/proof.md` Step 8 (A-C1-006). Each referee marked these non-blocking, and this report does not change a single mathematical step.
- **`tasks/A-C1-005/out/cex/hill_interval.py` was not rerun here** (it requires python-flint). Its interval-certified results are reported from `tasks/A-C1-005/out/verdict.md`, section 6.
- **What humans must still check:** that Step 8 of `cell/accepted/proof.md` (the cut identity) and Step 7 (the overlap lemma) hold at the breakpoints where g jumps — the referees state these are pointwise statements about indicator values and measure-zero in the integral (`tasks/A-C1-006/out/verdict.md`, G3 line), but this is the one place where the argument's case split is densest; and that "compactness" is not invoked anywhere in the accepted proof (it is not: the accepted route is an integral identity, not a variational argument; the maximiser/compactness route appears only in `tasks/A-C1-003/out/proof.md`, Step B3).

## 8. NEXT STEPS

- The cell is closed. `cell/gate/gate_report.md`, "Next" line: "PROVED on board".
- Neighbour cells remain open. The problem statement (this task's `inbox/statement.md`, outside `inbox/record/`) lists C2 (orthogonality lemma, 2 points), C3 (d+1 lines in R^d, 3 points), C4 (five lines in R^3, six in R^4, 5 points), C5 (d+2 lines in R^d, 8 points) and C6 (the full conjecture, 13 points, marked "Open question"). No artefact in this cell's record addresses them.
- Transferable material recorded for those cells:
  - The warning that the planar routes do not extend: `tasks/A-C1-003/out/divergence.md`, point 2, "In R^d, d >= 3, sum_i theta(e_i, m) over an orthonormal frame is NOT constant ... so B1-B2 do not extend verbatim. This is a useful warning for cells 3-6."
  - Consistency arithmetic linking C1 to C6 at d = 2: binom(N,2) - M(N,2) = floor(N^2/4) (`cell/checklist.md`, S5; verified for N = 0..10000 in RUN-6 and RUN-7).
  - Literature leads for the neighbours, with links and status, in `tasks/A-C1-003/out/sources.md`: FVZ Theorem 1.1 for R^3 and the recursive bound S(n,d) <= n S(n-1,d)/(n-2); Bilyk–Matzke Theorem 1.3 for d >= 2; Petrunin's orthogonality-graph comment on MathOverflow 173712 for n = d+1 (cell C3); Lim–McCann for the alpha-power family.
  - The exact deficit formula that cut averaging gives — "(pi/2) floor(N^2/4) - S as an integral of (floor(N^2/4) - k(N-k)), i.e. an L2-discrepancy" (`tasks/A-C1-003/out/divergence.md`, point 1) — if a higher-dimensional analogue of the cut is ever found.
- If the equality cases are ever wanted: the record already contains observed extra maximisers for odd N (three lines at mutual angles pi/3 for N = 3: `tasks/A-C1-002/out/proof.md`, final section; dyadic configurations found by search for N = 3,5,...,13: `tasks/A-C1-006/out/verdict.md`, EQUALITY CASES line; regular configurations {k pi/N} for odd N = 3..41: `tasks/A-C1-007/out/verdict.md`, EQUALITY CASES line). None of this amounts to a characterisation.
