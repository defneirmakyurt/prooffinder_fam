# Board: problem H, updated 15:02, run time 1:54 of 7:00

| Cell | Pts | Tier | Phase | Cell status | Claim status | Robustness | Best so far | Live lineages | Next | Time used |
|------|-----|------|-------|-------------|--------------|------------|-------------|---------------|------|-----------|
| H-C1 | 1 | T0: done in dry run | submitted; gated | SOLVED | PROVED: U(Q3)=14, U(Q4)=34 (LB = H-L1 at d=3,4; labellings checker-verified, pinned) | – | Q3 14, Q4 34 (checker re-scored) | none | none (submitted) | 0:00 (dry run) |
| H-C2 | 2 | T1: 32 vertices, local search feasible; LB via H-L1 | submitted (portal: correct); gated | SOLVED | PROVED 88 (gated H-C4-001 claim C10, d=5; both referees ACCEPT C10) | – | 88 (H-C2-001, H-C2-002, H-C5-002) | excess-DP (H-C2-001), decycling (H-C2-002) | none | 0:35 |
| H-C3 | 3 | T1: 64 vertices; LB via H-L1 | submitted (portal: correct); gated | SOLVED | PROVED 204 (gated H-C4-001 claim C10, d=6; both referees ACCEPT C10) | – | 204 (H-C3-001, H-C2-002, H-C5-002) | forest-peak exhaustive (H-C3-001) | none | 0:35 |
| H-C4 | 5 | T2: two values, Q8 256 vertices; /E/+2 pattern may break | submitted (portal: correct); gated | SOLVED | PROVED 464, 1040 (gate VALID: H-C4-002 + H-C4-003 ACCEPT) | – | Q7 464, Q8 1040 (H-C4-001, H-C2-002, H-C5-002) | induced-forest bound, doubling (H-C4-001) | none | 0:35 |
| H-C5 | 8 | T2: scored construction, beat 2400 | stopped by humans (run ~1:57) | PARTIAL | BEST-FOUND 2400 (= organisers; no improvement); LB unconditional 2312 | – | 2400 (5 lineages) | all stopped | none | 1:17 |
| H-C6 | 13 | T3: open; stretch only | - | NOT ATTEMPTED | OPEN | – | – | none | none (C5 not reached) | 0:00 |
| H-L1 | 0 (lemma for C1-C4) | T1: written sketch exists (dry-run H-C1-006 Remark) | gated | SOLVED | PROVED (gate VALID 13:21: H-L1-002 + H-L1-003 ACCEPT) | – | U(Q_d) >= d*2^(d-1)+2 for all d >= 3 (accepted/proof.md) | edge-count+divisibility | use as gated ASSUMPTION for C2-C5 (non-blind briefs) | 0:14 |

## Partial cells: established / remaining gap

## Awaiting gate
- [14:54] H-C5-007 (PARTIAL: labellings of Q_9 whose S_f has <= 3 vertices of one parity have >= 2376 paths): referees H-C5-013 (VERIFY), H-C5-014 (GATE), judged against its own partial statement.

## Contested cells (tell the humans)

## Lessons (changes since last checkpoint; pending Referee/Checker-builder/Auditor lessons)
- [14:36] Checkpoint 1 (run 1:28): no lesson changes; no pending gate-role lessons. Isolation: run/guard.log absent (0 denials); blindcheck on H-C2-001, H-C3-001, H-C4-001, H-C5-001: 0 real hits (1 false positive: 'SEED in 1..6'). Library: no entries added or imported.

## Decisions for the team
- [13:08] Checker: library entry H-uphill-checker installed as the accepted checker in C2-C6 (dry-run cross-test covers d=1..9, 208 cases, 0 disagreements); no new checker-builders dispatched.
- [13:08] H-L1 dispatched as Phase 1L literature, not an EXPLOIT prover: pp.py requires an EXPLOIT subject in the same cell and the dry-run proof lives outside run/tasks.
- [13:15] Network: the environment's policy blocks arxiv.org, oeis.org, AoPS, evanchen.cc, imo-official.org, wikipedia (HTTP 403 at the proxy). Literature agents see search snippets only; every reference stays unverified. Humans can allow these hosts in the environment's Network access settings. UPDATE: humans opened the network (all six hosts answer 200); running literature agents H-C2-002, H-C5-002 told to retry fetches. H-L1-001's references remain unopened.
- [13:21] H-L1 gated VALID at 13:21 (run 0:14): U(Q_d) >= d*2^(d-1)+2 for every d >= 3. Consequences: C1 SOLVED (14, 34 attained, pinned run/H/C1/accepted/); any labelling with 82 (Q5), 194 (Q6), 450 (Q7), 1026 (Q8) paths proves that value optimal.
- [13:32] L2 lemma cell dropped: H-C4-001's written argument covers d = 5..8 directly, so it goes to referees as is (cheaper, and the text refereed is the text handed in).
- [13:32] C5 reduction (from H-C5-002 1L + H-C4-001 Lemma A, not gated): 512 + 8*nabla(Q_9) <= U(Q_9); a labelling with <= 2399 paths needs a decycling set of Q_9 of size <= 235 (published: 225 <= nabla(Q_9) <= 237, Bau et al. 2000 via survey; Pike 2003 apparently 236, not opened). Upper route = beat the published decycling bound; lower route = nabla(Q_9) >= 233.
- [13:36] Humans submitted C2 = 88, C3 = 204, C4 = 464, 1040; the portal marked all correct (run ~0:40). Portal confirmation is external evidence for the values, not a proof: the lower-bound argument (H-C4-001) still goes through the gate for the record and for C5/C6, which build on it.
- [13:42] Humans asked for speed, proofs only (run ~0:50): Phase 5 reports/audits, triage and cross-verification skipped for C1-C4; gate = two referees per proof. C5 lower route opened: prover H-C5-007 (EXPLOIT on H-C5-002's lower-route notes).
- [14:02] Humans chose option 1 for C5 (run ~1:10): let the running workers (H-C5-001, -003, -004, -005, -006) finish; no new C5 dispatches. Stop C5 if nothing scores <= 2399 or proves >= 2369.
- [14:30] Humans: 'solve C5' (run ~1:20). C5 reopened with wave 3, only approaches not yet tried: CP-SAT exact model with implied subcube constraints (CONTRARIAN, dead ends forbidden), exhaustive cluster enumeration (merged cluster lineages), SAT lower bound with DRAT (FRESH), repair of H-C5-007's R9, and a literature pass for Pike 2003's full text and any non-independent minimum decycling set. Gated Lemma A given as ASSUMPTION. ortools installed in the venv.
- [15:02] Humans: 'stop all' (run ~1:57). Stopped H-C5-008, -009, -010, -011 (wave 3), referees H-C5-013/-014 (H-C5-007 partial proof stays UNREFEREED), scribe H-C5-015. No worker processes left running. C5 hand-in = run/H/handin/C5_partial_plain.txt + Q9_2400.txt.

## Obstacle notes (parked cells)
- [14:01] H-C5 lower route: TRIED: parity split + clique cover (H-C5-007). STALLS AT: R9, tau(G_2[F∩E]) <= z+2 for 4 <= z <= 116. PROVED (unrefereed): forests missing <= 3 vertices of one parity have <= 279 vertices, so such labellings have >= 2376 paths. Unconditional LB still 2312. KNOWN: 225/226 <= nabla(Q_9) <= 236 (Pike 2003, Hertz 2021; H-C5-006).
- [14:04] H-C5 (H-C5-006 analyst): published 225 <= nabla(Q_9) <= 236 (Hertz 2021 Table 4, citing Pike 2003; Pike itself paywalled, unopened). No source gives a decycling set <= 235 or nabla(Q_9) >= 227. Independent decycling sets have size >= 2^(d-1) - A(d,4) = 236 (A(9,4) = 20 cited), so an upper-route S_f must contain an edge. Searches for a 277-vertex induced forest: none found.
- [14:24] H-C5 CLOSED (run 1:17): TRIED: parity/code construction + decycling SA (H-C5-002), FVS SAT+LS (H-C5-001), decycling local search (H-C5-003), symmetric SAT (H-C5-004), recursive product (H-C5-005), lower-route parity split (H-C5-007), literature (H-C5-006). STALLS AT: a decycling set of Q_9 with <= 235 vertices (upper) or nabla(Q_9) >= 233 (lower). NEEDS: improving the published 225 <= nabla(Q_9) <= 236 (Pike 2003; Hertz 2021).
