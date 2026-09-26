# Audit (re-audit after repair) — final report for cell A-C1 (subject task A-C1-008)

Auditor A-C1-009, Phase 5 AUDIT. Read only: brief.md and inbox/ (final_report.md, statement.md,
target.md, checklist-G.md, record/). No code was executed; every check is a reading of the artefact
named by the report. RAN: none. This file replaces the first-pass audit.

Snapshot note (supplied by the head, confirmed by it, and consistent with everything I can see):
the record folder is snapshotted when a task is created. The copy of `cell/phases.md` in the
reporting task's inbox was taken at 12:46 and has seven task rows; the copy in my inbox was taken at
12:51 and has eight, including the A-C1-008 row. The corrected report's statements about "snapshotted
at 12:46 … lists the first seven" and "`grep -n 'A-C1-008' cell/phases.md` returns nothing" describe
the copy in its own inbox and are judged on that basis. For the same reason my copy of
`tasks/A-C1-008/out/` is the pre-repair one (no `logs/run10_inventory.txt`, old `final_report.md`).

```
AUDIT: PASS
CITATIONS CHECKED: 75
UNSUPPORTED: none
```

All three items from the first pass are now resolved:

1. Task count and timeline — the report now says "Eight tasks produced this cell's record", gives an
   eight-row table, and states which rows come from `cell/phases.md` and which from its own `brief.md`.
   Every one of the eight rows matches my (eight-row) copy of `cell/phases.md` exactly.
2. Seeds — replaced by a seven-row table of script, line and seed. All seven lines and seed values are
   verbatim correct in my copy of the record, and no other script in the record uses `random`
   except two byte-identical working copies of two of them (see row 53).
3. Referee passes — the heading now reads "four referee passes" and the section opens with "Four
   referee tasks ran, all returning ACCEPT", matching the four referee rows in `cell/phases.md` and
   the four ACCEPT verdicts.

No other statement changed. Sections 1, 2, 3, 5, 7 and 8, and RUN-0 to RUN-9 in section 6, are
word-for-word what I audited in the first pass; the only additions are the timeline paragraph and
table, the seeds table with its note, the "four referee passes" sentence, and RUN-10.

## Form checks (section 15, item 4)

| check | result |
|---|---|
| Eight sections present (OUTCOME, STATEMENT, RESULT, HOW IT WAS REACHED, LITERATURE VS OURS, REPRODUCIBILITY, LIMITATIONS, NEXT STEPS) | PASS |
| STATEMENT matches TARGET word for word (all three paragraphs, every range, quantifier, edge case, hand-in clause) | PASS — identical to brief.md TARGET and to inbox/record/cell/target.md, including "for every N", "(repetitions allowed)", "theta(l, l') in [0, pi/2]", "arccos\|<x, x'>\|" and the computation/status hand-in sentence |
| LIMITATIONS contains "agent agreement is evidence, not proof" | PASS (section 7, first bullet) |
| Nothing called "new" | PASS — no occurrence of "new"/"novel"/"first time"; the literature negative reads "Nothing newer on the planar case was found in the sources searched" with the searches listed |
| Literature results and our own in separate lists | PASS — "Existing results (from tasks/A-C1-003/out/sources.md)" and a separate "Our contribution" table |
| PROVED needs a gate report with DECISION: VALID | PASS — cell/gate/gate_report.md, "DECISION: VALID" for proof A-C1-001 |
| COMPUTER-VERIFIED | none claimed; the only code claim is "CHECKED, explicitly non-load-bearing" for check_cut_identity.py, matching cell/accepted/claims.md row 8 |
| SOLVED needs every hand-in claim at an established status | PASS — hand-in is a complete written proof plus a solved/partial statement; cell/accepted/proof.md is complete (no [GAP]), TARGET row PROVED, gate VALID; the scribe's brief sets CELL STATUS: SOLVED / CLAIM STATUS: PROVED and the report upgrades neither |

## Citation-by-citation table

| # | statement in the report | citation | found? | what the artefact actually says |
|---|---|---|---|---|
| 1 | Cell status SOLVED | cell/gate/gate_report.md, "Next: PROVED on board" | yes | Line 7 is exactly "Next: PROVED on board"; DECISION line is VALID. "Solved" itself is in cell/accepted/proof.md line 3 (cited next) and in the scribe's brief. |
| 2 | Claim status PROVED for the target claim | cell/accepted/claims.md, row "TARGET" | yes | "TARGET: S(l_1..l_N) <= (pi/2) floor(N^2/4), all N>=0, repetitions allowed \| PROVED \| proof.md, Steps 11-12" |
| 3 | Gate decision quoted in full | cell/gate/gate_report.md, DECISION line | yes | Verbatim. |
| 4 | "Status: cell A-C1 solved (complete proof, no [GAP]; no step rests on computation)", cited as line 2 | cell/accepted/proof.md | yes | Verbatim, on line 3 (line 2 is blank). Content unchanged. |
| 5 | Twelve claim rows, all PROVED, each pinned to a step | cell/accepted/claims.md, rows 1–12 | yes | 12 rows, every status begins PROVED; row 8 adds "(also exact sanity check … CHECKED, non-load-bearing)", row 12 is "PROVED (not required)". Step numbers all match. |
| 6 | STATEMENT section, three paragraphs | cell/target.md | yes | Identical word for word, and identical to brief.md TARGET. |
| 7 | Checklist sha256 70046abc…e5dd | RUN-1 | no artefact | No hash file or log in my copy of the record; not resolvable without execution (KNOWN GAP). |
| 8 | Part G (G1–G9) generic, Part S (S1–S6) referee-only | cell/checklist.md | yes | Part G lists G1–G9; Part S headed "specific; referees and the gate only, NEVER shown to blind agents", S1–S6. |
| 9 | Accepted proof sha256 fc29d1…dae5d pinned | cell/accepted/MANIFEST.sha256 | yes | Line 1 matches character for character. |
| 10 | Byte-identical to tasks/A-C1-001/out/proof.md | RUN-2 | partly | Both exist; statement line, status line, Conventions and Step 1 identical on inspection, and the two claims.md files are identical; the hash comparison itself is not verifiable here (KNOWN GAP). |
| 11 | Steps 1–4 (parametrisation; theta well defined, <u(a),u(b)> = cos(a−b); rho and its five properties; arccos\|cos(a−b)\| = rho(a−b)) | cell/accepted/proof.md, Steps 1–4 | yes | Matches, incl. (3a)–(3e). |
| 12 | Steps 5–6 (g pi-periodic, even, step function; period integral; int_0^pi g = pi/2) | cell/accepted/proof.md, Steps 5–6 | yes | (5a)–(5c) and Step 6 with its closing line. |
| 13 | Step 7 overlap lemma, theta in [0, pi/2] | cell/accepted/proof.md, Step 7 | yes | Exactly this statement and range. |
| 14 | Step 8 cut identity for all real x, y | cell/accepted/proof.md, Step 8 | yes | "For all real x, y" as claimed. |
| 15 | Step 9 for all integers N >= 0 and k, both parities | cell/accepted/proof.md, Step 9 | yes | Matches, with separate even/odd arguments. |
| 16 | Step 10 pair count k(t)(N − k(t)) | cell/accepted/proof.md, Step 10 | yes | Matches. |
| 17 | Step 11 main inequality | cell/accepted/proof.md, Step 11 | yes | Same constant, same direction. |
| 18 | Step 12 degenerate cases and repetitions | cell/accepted/proof.md, Step 12 | yes | Matches. |
| 19 | Step 13 sharpness, "not required by the cell" | cell/accepted/proof.md, Step 13 | yes | Header and construction as described, for every N. |
| 20 | Scope quote "What is established … No computation is used in the proof" | cell/accepted/proof.md, final paragraph | yes | Verbatim. |
| 21 | Second proof, Steps 0–13, Step 10 identity / Step 11 counting / Step 12 integer bound | tasks/A-C1-002/out/proof.md | yes | Steps 0–14 exist with exactly those roles; Step 14 is the sharpness remark (section 5 cites "Steps 0–14"). Cosmetic internal inconsistency, both readings match the file. |
| 22 | Third write-up, Steps B1–B7 and A1–A4 | tasks/A-C1-003/out/proof.md | yes | B1–B7 and A1–A4 present with the described content. |
| 23 | Three stuck files, no open lemma | tasks/A-C1-001,002,003/out/stuck.md | yes | "none", "none", "none. Both written proofs are complete. …" |
| 24 | cell/deadends.md empty (0 bytes) | cell/deadends.md | yes | Empty. |
| 25 | **"Eight tasks produced this cell's record"**, eight-row timeline table | cell/phases.md + this task's brief.md | yes | My copy of cell/phases.md has exactly eight task rows; the eighth is "\| A-C1-008 \| 5 \| scribe \| RECORD \| REPORT \| - \| - \| 12:51 \|", matching the report's eighth row (phase 5, scribe, RECORD, REPORT, subject -, created 12:51). Corrected item 1 now holds. |
| 26 | **The shipped copy of cell/phases.md "was snapshotted at 12:46 … and lists the first seven"; `grep -n 'A-C1-008'` returns nothing** | RUN-10 | yes, for the artefact it names | This is about the copy in the reporting task's own inbox, not mine. The head confirms that copy has seven rows and mtime 12:46; the report says explicitly which copy it describes and supplies the eighth row from another source. My copy (eight rows, mtime 12:51) is a later snapshot and does not contradict the claim. The RUN-10 log is not in my pre-repair snapshot (KNOWN GAP). |
| 27 | Eighth row taken from this task's brief.md, lines 1–3, quoted | tasks/A-C1-008/brief.md | yes | Lines 1–3 read "TASK: A-C1-008      ROLE: scribe      REGIME: RECORD", "PHASE: 5   MODE: REPORT   BRANCH: -", "SUBJECT: -" — the quote is accurate; the created time 12:51 is corroborated by the A-C1-008 row of my cell/phases.md. |
| 28 | Timeline rows A-C1-001…007 (phase, role, regime, mode, subject, created) | cell/phases.md, table rows | yes | Every value matches: 001/002 prover BLIND 12:34; 003 1L literature LITERATURE SOLVE 12:39; 004 VERIFY A-C1-001 12:39; 005 VERIFY A-C1-002 12:39; 006 GATE A-C1-001 12:43; 007 VERIFY A-C1-003 12:46. |
| 29 | Gate report timestamped 12:47 | cell/gate/gate_report.md, header | yes | "# Gate: A-C1, proof A-C1-001, 12:47" |
| 30 | No BRANCH or SUBJECT beyond the referee subjects | cell/phases.md, Branch column | yes | Branch column "-" in all eight rows; subjects only on 004/005/006/007. |
| 31 | A-C1-001 BLIND instruction quote | tasks/A-C1-001/brief.md, final paragraph | yes | Verbatim (line 35). |
| 32 | A-C1-001 plan "Idea" quote | tasks/A-C1-001/out/plan.md | yes | Verbatim. |
| 33 | Ladder R1–R7, every rung PROVED | tasks/A-C1-001/out/plan.md, Ladder | yes | R1–R7, each "Status: PROVED". |
| 34 | A-C1-002 plan "Idea" quote; rungs R1–R8 all PROVED | tasks/A-C1-002/out/plan.md | yes | Verbatim; R1–R8 each "STATUS: PROVED". |
| 35 | A-C1-003 searched the literature and attempted the cell | tasks/A-C1-003/brief.md, Phase 1L | yes | Brief items 1–3 say exactly that. |
| 36 | Five searches; third "nothing newer on the planar case", fourth "nothing specific" | tasks/A-C1-003/out/sources.md, "Searches run" | yes | Four WebSearches plus the StackExchange API query; both quotes verbatim. |
| 37 | Two proofs: B from FVZ, A from Bilyk–Matzke | tasks/A-C1-003/out/proof.md, header bullets | yes | Bullets say exactly this. |
| 38 | Divergence "Verdicts" quotes | tasks/A-C1-003/out/divergence.md | yes | Both sentences verbatim. |
| 39 | Approach-mapping quotes (001, 002, Proof B) | tasks/A-C1-003/out/divergence.md, "Approaches" | yes | All three verbatim, incl. "Found blind, independently." and "Not used by either blind run." |
| 40 | Three substantive differences incl. the d >= 3 non-constancy example | tasks/A-C1-003/out/divergence.md | yes | Points 1–3 as described; the quoted R^d sentence verbatim. |
| 41 | Provenance quote | tasks/A-C1-003/out/divergence.md, "Provenance summary" | yes | Verbatim; the file's "New here (as a write-up)" is not reproduced as "new" anywhere. |
| 42 | **Heading "four referee passes"; "Four referee tasks ran, all returning ACCEPT"** | cell/phases.md rows A-C1-004…007; the four verdict files | yes | phases.md marks exactly those four rows Role = referee (004 VERIFY, 005 VERIFY, 006 GATE, 007 VERIFY); all four verdict files open "VERDICT: ACCEPT". Corrected item 3 now holds. |
| 43 | A-C1-004 ACCEPT / match yes / no first problem / G4 N/A, rest PASS; "Unjustified, circular or false steps found: none" | tasks/A-C1-004/out/verdict.md | yes | Header block and §2 closing line verbatim. |
| 44 | A-C1-005 same pattern | tasks/A-C1-005/out/verdict.md | yes | G4 N/A, all other items PASS. |
| 45 | A-C1-006 (GATE) same pattern | tasks/A-C1-006/out/verdict.md | yes | Same. |
| 46 | A-C1-007 all PASS with G4 PASS (quoted) | tasks/A-C1-007/out/verdict.md, G4 line | yes | Quoted verbatim. |
| 47 | Matrix not run; head checked the statement word for word | cell/gate/gate_report.md; cell/gate/A-C1-001.md | yes | "Matrix: not run"; "Statement checked word for word by head: yes"; both gate files identical in content. |
| 48 | "four referee passes accept" (Agreement matrix section) | the four verdict files; divergence.md "Verdicts" | yes | All four read ACCEPT. |
| 49 | A-C1-004 search ranges and quotes | tasks/A-C1-004/out/verdict.md, §3, §6, CEX SEARCH | yes | pi/12 grid N <= 8; rationals N <= 14 with repeats; hill-climb N = 2..12, 40 starts, exact recertification; Steps 7–11 exact; Step 9 N <= 300, k in [−20, N+20]; both quotes verbatim. |
| 50 | A-C1-005 E1–E8, 863163 multisets, grids m in {2..10,12,24,60}, N up to 12; hill_interval 200-bit arb, N = 2..12, 6 × 6000, 66 configurations, 36/30/0 | tasks/A-C1-005/out/verdict.md, §6 | yes | Verbatim, incl. "0 certified above the bound." |
| 51 | A-C1-006 ranges and "0 exact violations" | tasks/A-C1-006/out/verdict.md, CEX SEARCH and RAN lines | yes | RAN lines give exactly these ranges. |
| 52 | A-C1-007 grids, hill-climb N = 2..16 / 60 restarts, "max excess 1.4e-14", "no counterexample…" | tasks/A-C1-007/out/verdict.md, §6 | yes | All four grids and both quotes match. |
| 53 | **"Exactly seven scripts in the record use `random`, and every one of them fixes its seed"** | RUN-10 (`grep -l`/`grep -n` over tasks/*/out/code/*.py and tasks/*/out/cex/*.py) | yes | In the record the report describes (tasks A-C1-001…007, the two globs it names) exactly seven .py files contain `random`, and each has a seed line. In my later snapshot the same seven appear, plus two byte-identical working copies of two of them in tasks/A-C1-008/out/verify/ (referee_004_check.py line 12 and referee_006_checks.py line 9, same seeds), which are not separate record scripts; no unseeded use of `random` exists anywhere. The substance — every randomised script fixes its seed — holds in both snapshots. |
| 54 | Seed row: tasks/A-C1-002/out/code/sanity_check.py, line 38, `random.Random(12345)` | the script | yes | Line 38: `    rng = random.Random(12345)` |
| 55 | Seed row: tasks/A-C1-004/out/cex/check.py, line 12, `random.seed(20260926)` | the script | yes | Line 12: `random.seed(20260926)` |
| 56 | Seed row: tasks/A-C1-005/out/cex/check_exact.py, line 62, `random.Random(20260926)` | the script | yes | Line 62: `    rng = random.Random(20260926)` |
| 57 | Seed row: tasks/A-C1-005/out/cex/hill_interval.py, line 32, `random.Random(777)` | the script | yes | Line 32: `    rng = random.Random(777)` |
| 58 | Seed row: tasks/A-C1-006/out/cex/referee_checks.py, line 9, `random.seed(20260926)` | the script | yes | Line 9: `random.seed(20260926)` |
| 59 | Seed row: tasks/A-C1-006/out/cex/ascent_exact_recheck.py, line 5, `random.seed(7)` | the script | yes | Line 5: `random.seed(7)` |
| 60 | Seed row: tasks/A-C1-007/out/cex/cex.py, line 16, `random.seed(20260926)` | the script | yes | Line 16: `random.seed(20260926)` |
| 61 | "One of these seeds is also written out in prose … The remaining six are recorded in the source of the scripts" | tasks/A-C1-002/out/code/README.md "Measured" line; tasks/A-C1-005/out/verdict.md §3 | yes | README line 16: "…on the author's laptop, seed 12345"; A-C1-005 §3 and its RAN line say "seed 12345". A text search of the record's prose files finds no other seed value; the other six appear only in source. |
| 62 | No triage decision; every brief carries "BRANCH: -" | cell/phases.md | yes | Branch column all "-"; the briefs in the record (001, 003, 008) carry "BRANCH: -". |
| 63 | Four OTHER ISSUES blocks quoted, all non-blocking | the four verdict files, OTHER ISSUES lines | yes | All four verbatim; each is labelled "cosmetic only"/"non-blocking" in its verdict. |
| 64 | Literature table, seven rows with link, content, status tag, "contains the argument?" | tasks/A-C1-003/out/sources.md, table | yes | All seven rows match, including the status tags (PROVED / "d=2: CONJECTURED/asserted…" / UNSURE / "PROVED per FVZ (cited only)") and the "opened?" qualifiers. |
| 65 | "Nothing newer on the planar case was found in the sources searched" | tasks/A-C1-003/out/sources.md, "Searches run", third bullet | yes | Bullet ends "-> nothing newer on the planar case". Required "not found in <sources searched>" form. |
| 66 | Our-contribution table (accepted proof PROVED; claims rows; A-C1-002 ACCEPT by 005; A-C1-003 B and A ACCEPT by 007; script CHECKED non-load-bearing, README line 3 quote) | cell/accepted/*, the two verdicts, tasks/A-C1-001/out/code/README.md line 3 | yes | Statuses are exactly those in the cited files; README line 3 verbatim. No status upgraded. |
| 67 | Rules quote and G6 quotes (proof cites nothing) | tasks/A-C1-001/brief.md RULES line; tasks/A-C1-004/out/verdict.md G6; tasks/A-C1-001/out/plan.md G6 | yes | All three verbatim. |
| 68 | RUN-10 (record inventory: 9 lines, 7 task rows, no A-C1-008 match, mtimes 12:46/12:51, brief lines 1–3, 7 random files, 7 seed lines, 4 referee rows), 0.03 s, log out/verify/logs/run10_inventory.txt | RUN-10 | mostly | The checkable content is confirmed: the seven seed lines (rows 54–60) are exact, the brief quote is exact, and cell/phases.md marks exactly four referee rows. The row counts and mtimes concern the reporting task's own inbox copy (head-confirmed); the log file is not in my pre-repair snapshot (KNOWN GAP). |
| 69 | RUN-0…RUN-9 (versions, hashes, five copied scripts, six timed reruns with ranges, outputs, runtimes) | tasks/A-C1-008/out/verify/ and out/verify/logs/ | mostly | Unchanged from the first pass and re-checked: RUN-4 (0.40 s), RUN-5 (0.45 s; 4/9, 17/9, 13/3), RUN-6 (0.05 s), RUN-7 (0.03 s), RUN-8 (7.04 s), RUN-9 (12.44 s) match their logs line by line, including both float-error quotes (1.260e-13, 1.997e-12) and the grid/ascent outcomes. RUN-0/1/2/3 have no log in the record (KNOWN GAP). Comparison runtimes from A-C1-001 README (0.41 s, 0.26 s), A-C1-004 (13.36 s, 0.12 s) and A-C1-006 (4.27 s, 0.03 s) all match. |
| 70 | "The longest runtime recorded anywhere in the record is 22.53 s" | tasks/A-C1-005/out/verdict.md, RAN line | yes | check_exact.py 22.53 s; no larger figure in any RAN line or README (next: 13.36 s, 12.44 s, 6.12 s, 4.50 s, 3.62 s). RUN-10 at 0.03 s does not affect the "at most 12.44 s" sentence. |
| 71 | No float in the accepted proof; float only in non-load-bearing checks, each with an error bound or interval certificate | cell/accepted/proof.md final paragraph; A-C1-004 G7; A-C1-006 G7; A-C1-002 README item 3; A-C1-005 §3, §6; A-C1-007 §6 | yes | Every figure matches: "about 2h = 6.3e-4", "6.0e-4 within the Riemann-sum resolution 6.28e-4", "gaps of about −3e-11 … float noise at equality", "max excess 1.4e-14", "200-bit arb ball arithmetic". |
| 72 | hill_interval.py not rerun (needs python-flint); its results reported from the verdict | tasks/A-C1-005/out/cex/hill_interval.py; §6 | yes | Script present; results quoted from the verdict, not re-asserted. |
| 73 | LIMITATIONS items (equality cases; d >= 3; matrix not run; deviating runtimes; fetch-summary sources; cosmetic remarks) | as cited in section 7 | yes | All quotes verbatim, incl. checklist S2 "Whether other configurations also attain equality: unknown (not given)". |
| 74 | "What humans must still check" — breakpoints of Steps 7 and 8 called pointwise/measure-zero | tasks/A-C1-006/out/verdict.md, G3 line | yes | The expanded G3 in §1 says exactly this; the one-line G3 in the header block does not. Content supported; the citation points at the shorter of two entries with the same label. |
| 75 | NEXT STEPS (cell closed; C2–C6 with point values and C6 "Open question"; transferable material; extra maximisers for odd N) | gate_report.md; inbox/statement.md; checklist S5; divergence points 1–2; sources.md; A-C1-002 proof final section; A-C1-006 and A-C1-007 EQUALITY CASES lines | yes | statement.md gives C2 (2), C3 (3), C4 (5), C5 (8), C6 (13, "Open question"); S5 gives binom(N,2) − M(N,2) = floor(N^2/4); EQUALITY CASES lines give dyadic configurations N = 3,5,…,13 and regular {k pi/N} for odd N = 3..41. |

## Notes that are not failures

- Section 3 calls the A-C1-002 write-up "Steps 0–13" and section 5 "Steps 0–14"; the file has Steps 0–14
  with Step 14 a sharpness remark. Cosmetic inconsistency; both readings match the file.
- Two references are imprecise without changing content: cell/accepted/proof.md "line 2" is line 3, and
  the A-C1-006 "G3 line" content sits in the expanded G3 of §1 rather than the header block.
- Citation 1 attributes "SOLVED" to the gate's "Next: PROVED on board"; the gate records PROVED and
  SOLVED comes from cell/accepted/proof.md line 3 and the scribe's brief. No status is upgraded.
- My copy of `tasks/A-C1-008/out/final_report.md` is the pre-repair version, and my copy of
  `cell/phases.md` is a later snapshot than the reporting task's. Both are snapshot-timing artefacts,
  not report claims.

## Known gaps (not resolvable by reading, no execution available)

- RUN-0 interpreter versions, RUN-1 checklist sha256, RUN-2 `shasum -c` / proof byte-identity,
  RUN-3 five-file hash table, and RUN-10's log `out/verify/logs/run10_inventory.txt` (absent from my
  pre-repair snapshot) and its `wc`/`stat` figures for the reporting task's own inbox copy.
  The accepted proof's hash is corroborated by cell/accepted/MANIFEST.sha256; the A-C1-001 copy matches
  on inspection of its statement, status line, conventions and first step, and its claims.md is
  identical to the accepted one; RUN-10's seven seed lines, brief quote and four referee rows are
  confirmed directly against the record.
