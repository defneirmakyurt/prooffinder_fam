AUDIT: PASS
CITATIONS CHECKED: 128
UNSUPPORTED: none

Subject: inbox/final_report.md (A-C2-018, scribe, Phase 5). Paths in the report are relative to inbox/record/; `brief.md` = inbox/record/tasks/A-C2-018/brief.md; `out/...` = inbox/record/tasks/A-C2-018/out/....
My re-run logs are in out/logs/ (01-14). Scratch copies are in out/tmp/.

## Non-blocking observations (the cited artefacts still support the content; wording only)
1. §4.5 says "Every prover's stuck.md reads 'none': A-C2-001, -002, -010, -011 and -017". Each listed stuck.md does read "none", but A-C2-017 is a literature analyst, not a prover (cell/phases.md line 19). The report's own §4.1 gets this right.
2. §6 puts "uses no computation" in quotation marks. cell/accepted/proof.md actually says "no computation used" (line 3) and "No computation is used in the proof" (line 83). The meaning is the same, but the quote is not verbatim.
3. §4.1 / §6 run 11 say "17 task folders". My snapshot has 18, because it also includes A-C2-018 itself. Leaving A-C2-018 out gives 17 (A-C2-001..017), which matches the report and A-C2-018's log 11.
4. §4.2 says the out/ of A-C2-007 is "empty". Log 12 shows no files, and log 11 and my log 11 show that the out/ directory exists but is empty. This is consistent. The head's brief line 32 says "it has no out/", and the report reproduces the record correctly.

## Form checks (out/logs/13_form_checks.txt)
| check | result |
|---|---|
| eight sections present | yes: OUTCOME, STATEMENT, RESULT, HOW IT WAS REACHED, LITERATURE VS OURS, REPRODUCIBILITY, LIMITATIONS, NEXT STEPS |
| STATEMENT = TARGET word for word | yes: the report's lines 19/21/23 match brief.md TARGET lines 7-9, cell/target.md lines 1-3 and inbox/target.md under diff |
| LIMITATIONS contains "agent agreement is evidence, not proof" | yes (line 269) |
| nothing called "new"/"novel" | yes: no occurrence. §5.1 uses "not found in" plus the sources |
| literature and team results in separate lists | yes: §5.1 (existing results) and §5.2 (team artefacts) |
| status PROVED backed by a gate VALID | yes: cell/gate/A-C2-002.md line 6 is DECISION: VALID, and cell/accepted/ pins that proof (MANIFEST OK) |
| cell SOLVED backed | yes: the hand-in is a complete written proof, claims.md Steps 1-7 are all PROVED, and no step relies on computation |

## Re-runs (outputs compared; runtimes are my own measurements)
| report RAN # | what I ran (on a copy in out/tmp/) | output vs report | my runtime | log |
|---|---|---|---|---|
| 1 | sha256sum cell/checklist.md | 8d96a9f4...9887c84, matches | <1 s | out/logs/01_checklist_sha256.txt |
| 2 | sha256sum -c MANIFEST.sha256 | proof.md OK, claims.md OK | <1 s | out/logs/02_manifest_check.txt |
| 3 | cmp accepted vs A-C2-002 | IDENTICAL | <1 s | out/logs/03_accepted_vs_A-C2-002.txt |
| 4 | sha256sum of the 7 proof.md files | same 7 hashes as A-C2-018 log 04; there are exactly 7 proof.md files in the record | <1 s | out/logs/04_proof_hashes.txt |
| 5 | version query | python 3.11.15, sympy 1.14.0, mpmath 1.3.0, python-flint 0.9.0 | <1 s | out/logs/05_versions.txt |
| 6 | sanity_lemma.py (A-C2-002) | min 3.077760268865859e-12, matches | real 0.73 s | out/logs/06_sanity_lemma.txt |
| 7 | A-C2-006 search.py | 32176 chains, 0 certified violations, identical to record log | real 4.38 s | out/logs/07_A-C2-006_search.txt |
| 8 | A-C2-013 search.py 7 | 11200 instances, 0 violations, -1.987e-58, matches | real 2.04 s | out/logs/08_A-C2-013_search.txt |
| 9 | A-C2-012 gram_search.py | 32252 chains, 0 violations (gap < -1e-12), matches | real 2.49 s | out/logs/09_A-C2-012_gram_search.txt |
| 10 | diff vs record logs | identical apart from one blank line before bash `time` output in the record logs; identical to A-C2-018 logs 06-09 | <1 s | out/logs/10_diff_vs_record.txt |
| 11 | inventory | 18 folders incl. A-C2-018 (17 without it); 5 gate files; gate_report.md == A-C2-002.md; 9 verdict.md; deadends 0 bytes | <1 s | out/logs/11_inventory.txt |
| 12 | find tasks/A-C2-007 | brief.md only (plus an empty out/) | <1 s | out/logs/11_inventory.txt |
| - | grep of every runtime recorded in the record | the maximum is 469.25 s (A-C2-015); no other run exceeds 27.3 s | <1 s | out/logs/14_runtimes_grep.txt |
All my reruns took under 5 s, which supports "All reruns took under 5 s".

## Citation table
| statement | citation | found? | what the artefact actually says |
|---|---|---|---|
| phases.md lists only 001-017 | cell/phases.md 3-19 | yes | rows A-C2-001..017 |
| Cell SOLVED, claim PROVED | brief.md 29-30 | yes | "CELL STATUS: SOLVED", "CLAIM STATUS (do not upgrade): PROVED" |
| only gated claim = A-C2-002, quoted decision/next | cell/gate/A-C2-002.md 6-7 | yes | verbatim; other gate files are GAP (001, 011) |
| accepted artefacts pinned | cell/accepted/MANIFEST.sha256 1-2 | yes | two hashes; my sha256 -c gives OK |
| accepted = A-C2-002 byte-identical | out/verify/logs/02, 03 | yes | OK / IDENTICAL; re-run reproduces this |
| no computation in accepted proof | cell/accepted/proof.md 3, 83 | yes | "no computation used"; "No computation is used in the proof" (quote not verbatim, see obs. 2) |
| STATEMENT verbatim | cell/target.md 1-3; brief.md 7-9 | yes | identical under diff |
| checklist hash 8d96... | out/verify/logs/01 | yes | same hash; reproduced |
| final proof hash 3e08... | MANIFEST line 1 | yes | matches |
| Notation c_i, a_i, A, m-chain | proof.md Notation | yes | lines 8-10 |
| Step 1 reformulation + isometry | proof.md Step 1 | yes | lines 13-21 |
| Step 2 base case | proof.md Step 2 | yes | lines 26-27 |
| Step 3 degenerate | proof.md Step 3 | yes | lines 30-31 |
| Step 4 reduction, coefficient, (4e) | proof.md Step 4 | yes | lines 34-53 |
| Step 5 lemma and identity | proof.md Step 5 | yes | lines 56-66. The report omits the hypotheses beta<pi/2 and sin alpha<=cos beta, but both follow from alpha,beta>=0, alpha+beta<pi/2 |
| Step 6 case split | proof.md Step 6 | yes | lines 69-74 |
| Step 7 target | proof.md Step 7 | yes | line 77 |
| claims Steps 1-7 PROVED | cell/accepted/claims.md 3-9 | yes | 7 rows PROVED |
| m=3 sharpness family | proof.md Remarks 82 | yes | verbatim content |
| S2 tuple exact m=2..11 (004) | A-C2-004 verdict S2, item 5 | yes | line 15; line 46 "Equality tuple exact check m=2..11: OK"; check_log line 6 |
| S2 tuple arb m=2..11 (006) | A-C2-006 verdict §4 | yes | line 53, radius <= 1.4e-75, 256 bits; log lines 14-23 |
| 17 task folders | out/verify/logs/11 | yes | 17 (see obs. 3) |
| role counts 4/2/8/2/1 | cell/phases.md 3-19 | yes | recounted: prover 001,002,010,011; literature 003,017; referee 004,005,006,009,012,013,014,016; triage 007,008; breaker 015 |
| Phase 1 at 12:21 | phases.md 3-4 | yes | 12:21 |
| A-C2-001 route and SOLVED claim | A-C2-001 proof.md Steps 1-5, line 3 | yes | Steps 1-5 headers; line 3 "SOLVED"; D_k recursion line 33 |
| A-C2-001 stuck none | A-C2-001 stuck.md 1 | yes | "none" |
| A-C2-002 route Steps 1-7 | A-C2-002 proof.md | yes | identical to the accepted proof |
| A-C2-002 stuck none | stuck.md 1 | yes | "none" |
| Phase 1L 12:23 | phases.md 5 | yes | 12:23 |
| A-C2-003 GS route Steps 1-5 | A-C2-003 proof.md | yes | Steps 1-5; t_{k+1}^2 = 1 - a_k^2/t_k^2 (line 25) |
| every fetch blocked (003) | A-C2-003 stuck.md 3-6 | yes | EGRESS_BLOCKED / CONNECT 403 |
| 004 ACCEPT | 004 verdict 1 | yes | "VERDICT: ACCEPT" |
| 005 ACCEPT | 005 verdict 1 | yes | yes |
| 006 ACCEPT | 006 verdict 2 | yes | line 1 is ``` ; line 2 VERDICT: ACCEPT |
| 009 ACCEPT | 009 verdict 1 | yes | yes |
| Phase 2 times | phases.md 6-8, 11 | yes | 12:23, 12:23, 12:25, 12:27 |
| first gate 12:28 VALID, matrix not run | gate/A-C2-002.pre-2B.md 1-7 | yes | verbatim |
| no Phase 2B task yet | brief.md 32 | yes | "taken before any Phase 2B task existed" (the head's statement) |
| Phase 2A 12:27 | phases.md 9-10 | yes | 12:27 |
| A-C2-007 no output | out/verify/logs/12 | yes | only brief.md; reproduced |
| 007 INBOX includes 004/005 verdicts | A-C2-007 brief.md 17 | yes | verbatim |
| 007 never dispatched (Part S) | brief.md 32 | yes | head's statement |
| A-C2-008 ratings | A-C2-008 triage.md "Branch ratings" | yes | ALG HIGH, ANA HIGH, DISC MEDIUM, TOP LOW, NT NONE |
| selected ALG+ANA | selected_branches.txt 1-2; 008 brief.md 30 | yes | both solver; line 30 is the BUDGET line |
| eliminations order and reasons | triage.md "Eliminations" | yes | lines 92-95, "Re-admit first" |
| no re-admitted-branch task | phases.md 3-19 | yes | Branch column shows only ALGEBRAIC/ANALYSIS |
| Phase 2B 12:28 | phases.md 12-13 | yes | yes |
| 010 route, Steps 1-6 | A-C2-010 proof.md | yes | Steps 1-6; alpha_k = theta_1+...+theta_k-(k-1)pi/2 (line 6) |
| 011 route, Steps 1-6 | A-C2-011 proof.md | yes | Steps 1-6; line 27 quadratic-form bound |
| 010/011 stuck none | stuck.md 1 each | yes | "none" |
| 012 CONFIRMED | 012 verdict 2 | yes | "CROSS VERDICT: CONFIRMED" |
| 013 CONFIRMED | 013 verdict 1 | yes | yes |
| 014 ACCEPT | 014 verdict 1 | yes | yes |
| 016 CONFIRMED | 016 verdict 1 | yes | yes |
| 2B-XV times | phases.md 14-16, 18 | yes | 12:29, 12:29, 12:32, 12:34 |
| 012 Schur complement reading | 012 verdict line 5 | yes | "Schur complement ... diagonal congruence rescaling" |
| 013 potential reading | 013 verdict line 4 | yes | "potential function ... never raises the potential" |
| 016 LDL^T pivot reading | 016 verdict line 4 | yes | "p_k >= cos^2(B_{k-1})" |
| Phase 2C 12:32 | phases.md 17 | yes | yes |
| 015 PROOF-ROUTE-FOUND | 015 verdict 1 | yes | yes |
| 015 proof steps 1-10 | 015 proof.md | yes | numbered 1-10 |
| m=3 flat optimum | 015 local_analysis.md 9-11 | yes | "identically pi/2 on the whole singular curve" |
| matrix ROBUST, table | cell/matrix.md 1-18 | yes | identical table, CLASS: ROBUST |
| disputed none / pending 010 | matrix.md 14-18 | yes | yes |
| gate table 002 VALID | gate/A-C2-002.md 6 | yes | yes |
| gate_report.md byte-identical | out/verify/logs/11 | yes | cmp OK; reproduced |
| 001 GAP quote | gate/A-C2-001.md 6 | yes | verbatim |
| 011 GAP quote | gate/A-C2-011.md 6 | yes | verbatim |
| GAP next action | gate 001/011 line 7 | yes | "Next: repair + Phase 2C with this report" |
| no gate report for 003/010/015/017 | out/verify/logs/11 | yes | the gate files are 001, 002, 002.pre-2B, 011, gate_report |
| Phase 3 12:44 | phases.md 19 | yes | yes |
| 017 S1-S5, none labelled (c) | 017 subproblems.md 9-33 | yes | line 33 "No sub-problem is labelled (c)" |
| 017 GS reproduction Steps 1-5 | 017 proof.md | yes | Steps 1-5 |
| 017 no source opened | 017 sources.md 3-7 | yes | "no source was opened" |
| Phase 5 = A-C2-018 | brief.md 1-2 | yes | yes |
| divergence: no contradiction, shared trig | 003 divergence.md 3-13 | yes | yes |
| routes and t_k^2 = D_k/D_{k-1} | divergence.md 15-27 | yes | yes |
| provenance | divergence.md 29-33 | yes | yes ("could not locate ... could not check") |
| m=3 every chain equality | 005 verdict "Equality cases"; 015 contrapositive.md 17-18 | yes | line 48; lines 17-18 |
| 004 search row (seed line 6; 60000/32942; min -1.25e-69; 9439; 6.3e-609) | 004 check.py 6; check_log 4-5; verdict item 4 | yes | all match |
| 005 row (seed 12345 line 6; 2800, m=2..8; -1.47e-47; margins) | 005 search.py 6; log 2-9 | yes | all match |
| 006 row (Random(12345) l.39, Random(7) l.75; 32176; 256 bits) | 006 search.py; log 2-13 | yes | all match; flint prec 256 (line 8) |
| 009 row (Random(2026) l.13; 3200; -5.2e-26, -3.8e-51; gaps; 19900 boxes; 200 off-domain) | 009 log 3-8; log_hiprec 1-2; verdict Step 3 | yes | all match (verdict line 44) |
| 012 row (seed(12) l.23; 32252; min -2.2e-15; tolerance 1e-12) | 012 gram_search.py; log 1-12 | yes | all match; re-run reproduces this |
| 013 row (seed 7 argv l.17; 11200; 200 bits; -1.99e-58) | 013 search.py; log_search 1-3 | yes | all match; re-run reproduces this |
| 014 row (seed 12345 l.9; 33000/20114; 60 digits; -2.2e-59) | 014 search.py; log 1; verdict §3/4/6 | yes | all match (dps 60, line 8) |
| 016 row (seed 20260926 l.12; 85820; -1.3e-14) | 016 search.py; log 1-2 | yes | all match |
| 015 row (R3/R4/R5 ranges; seeds l.53/66; 469 s; -2.1e-8; worst.json) | 015 log 79; tested.md 2-7; worst.json | yes | all match |
| 004 caveat not interval | 004 verdict item 4 | yes | "not interval arithmetic" |
| 012 caveat float | 012 verdict "Limitation" | yes | line 71 |
| deadends.md 0 bytes | out/verify/logs/11 | yes | 0; reproduced |
| stuck.md "none" (001, 002, 010, 011, 017) | each stuck.md 1 | yes | all "none" (017 mislabelled as a prover, obs. 1) |
| 003 "Proof: none" | 003 stuck.md 1 | yes | "Proof: none (attempt complete)." |
| only stuck point = literature access | 003 stuck.md 3-6; 017 sources.md 3-7 | yes | I grepped every stuck.md and every "stuck" mention: no other stall is recorded |
| Gershgorin / triangle routes | 015 minimal_failing.md 6-10 | yes | verbatim quotes |
| not found in sources/queries | 003 sources.md 18-31; 017 sources.md 20-31 | yes | "not found in the sources and queries" |
| no source opened, says nothing on prior existence | 003 sources 3-7, 30-31; 017 sources 3-7, 28-30 | yes | yes |
| 7 literature rows (Bilyk-Matzke ... Chihara) | 017 sources.md 11-17 | yes | each row UNSURE, not opened, same links |
| 5.2 row 002 PROVED | gate/A-C2-002.md 2-6; matrix 7 | yes | yes |
| 5.2 row 001 GAP | gate/A-C2-001.md 2, 6 | yes | yes |
| 5.2 row 011 GAP | gate/A-C2-011.md 2, 6; matrix 9 | yes | yes |
| 5.2 row 003 one ACCEPT, no gate | 009 verdict 1; logs/11 | yes | yes |
| 5.2 row 010 no referee | matrix 8, 18 | yes | "pending" |
| 5.2 rows 015/017 no referee | phases.md 3-19 | yes | subjects are only 001, 002, 003, 011 |
| only 002 is PROVED | brief.md 32 | yes | yes |
| proof needs no computation | proof.md 3, 83 | yes | yes (obs. 2) |
| G7 N/A in 005 | 005 verdict 11 | yes | yes |
| G7 PASS in 006 | 006 verdict 12 | yes | yes |
| both scores in gate | gate/A-C2-002.md 5 | yes | yes |
| software versions | out/verify/logs/05 | yes | reproduced |
| /usr/bin/time absent, time -p used | logs 06-09 headers | yes | stated in headers (environment claim, consistent with the logs) |
| RAN 1-12 outputs | logs 01-12 | yes | all reproduced (see re-run table) |
| reruns byte-identical copies | out/verify/rerun/ | yes | cmp: all 4 scripts and 3 accepted files are identical to the record |
| run 10 comparison files | logs/10 | yes | the same four files |
| all reruns < 5 s | logs 06-09 | yes | 0.63-4.26 s; mine 0.73-4.38 s |
| longest recorded run = 469 s | 015 cex_search/runtime.txt 1 | yes | "wall 469.250737958 s"; my grep of all runtimes gives max 469 s, next 27.3 s |
| agreement caveat, ACCEPTs / ROBUST | gate/A-C2-002.md; matrix.md | yes | yes |
| GAP 1 of 2 for 001, 011 | gate files line 6 | yes | yes |
| wording discrepancy "not gated" | brief.md 32; gate/A-C2-001.md; gate/A-C2-011.md | yes | the brief says "not gated", but gate files with DECISION GAP exist; the report states the record's wording correctly |
| 007 limitation | 007 brief.md 17; brief.md 32 | yes | yes |
| equality configurations unknown | checklist.md 17; 006 verdict §4 | yes | verbatim; line 56 |
| S5 relies on A-C1 | checklist.md 20 | yes | verbatim; the report flags that it cannot check this |
| literature N=d+1 open | 017 subproblems.md 35-36 | yes | yes |
| cosmetic: code path, Regime BLIND | 005 verdict 41; 006 verdict 46 | yes | yes |
| cosmetic: continuity, 2nd clause | 012 verdict 26, 27 | yes | yes |
| disputed steps none | matrix.md 15 | yes | yes |
| every verdict ACCEPT/CONFIRMED/PROOF-ROUTE-FOUND | logs/11; §4.2 | yes | my log 11 lists the verdict line of all 9 files; none is other |
| next steps: hash, GAP next, 010 pending, sources | MANIFEST 1; gate 7; matrix 18; subproblems 35-36; 003 stuck 3-6 | yes | yes |
