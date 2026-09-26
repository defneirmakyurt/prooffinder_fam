# Divergence: H-C2-002 (EARLY 1L)

The Phase 1 blind searcher for C2 was still running, so inbox/earlier/ was empty. Per the brief,
this compares against inbox/earlier-C1-proof.md (earlier literature agent, U(Q_3)=14, U(Q_4)=34).
Compared, not merged: nothing of that proof is copied; shared elementary identities (degree sums,
the N(v) recurrence, P = s + sum N up) are standard (IMO 2022 P6 official solution) and are
re-proved in my proof.md Steps 1-4.

## Where the approaches differ
| point | earlier C1 proof | this run (C2) |
|---|---|---|
| lower-bound engine | P >= \|E\| + 1 (every edge starts a path), then equality analysis: equality forces 1 valley, down(v) = 1 off peaks, so (d-1) m = 2^(d-1)(d-2) + 1; divisibility fails for d = 3, 4 => P >= \|E\| + 2 | P >= n + (d-1)\|D_f\| with D_f = {down >= 2} a decycling set (Step 5-6), so U(Q_d) >= 2^d + (d-1) nabla(Q_d). Reduces the lower bound to a decycling-number bound |
| strength at d = 5 | the C1 method gives only U(Q_5) >= 82 (4m = 49 has no solution) | 84 by hand (Step 7), 88 with nabla(Q_5) >= 14 (computer, Step 8) -- tight |
| strength at d = 3, 4 | tight (14, 34) | also tight: 8 + 2*3 = 14, 16 + 3*6 = 34 (uses nabla(Q_3) = 3, nabla(Q_4) = 6, both re-found by decycle.py) |
| constructions | Q_3, Q_4 labellings found by search, no general pattern | explicit family: F = odd vertices + an even distance-4 code S (stars + isolated points), D = rest of the even side (peaks); P = (d+1)2^(d-1) - (d-1)\|S\|: d = 3 (\|S\| = 1) gives 16 - 2 = 14; d = 4 (\|S\| = 2) gives 40 - 6 = 34; d = 5..8 gives 88, 204, 464, 1040 |
| C1 closing Remark (U(Q_d) >= d 2^(d-1) + 2 for all d >= 3; flagged as not established) | argued via (d-1) \| 2^(d-1)(d-2)+1 impossible for d >= 3 | Not adjudicated here. Consistency only: by Step 7, (d-1)\|D\| >= (d-2)2^(d-1) + 1 with equality iff c = 1, e(D) = 0; the same divisibility condition appears, so Step 6 + that number-theoretic fact would give the same conclusion. No contradiction between the two. |

## Contradictions
None found. Both give 14 and 34 for d = 3, 4 (my d = 3, 4 values are only checks, via nabla(Q_3) = 3,
nabla(Q_4) = 6 from decycle.py, not a separate claim of this cell).

## Provenance of ideas
- From the blind run: none (no blind C2 output existed at writing time).
- From the earlier C1 literature proof / IMO 2022 literature: the identities P = s + sum N(v) up(v)
  and sum up = \|E\|; the idea of analysing the slack in P >= \|E\| + 1.
- From the decycling literature (Pike 2003; Focardi-Luccio-Peleg 2000; Bau-Beineke et al.; NOT
  opened, search summaries only): the notion of decycling number of Q_n and the fact that
  independent decycling sets come from distance-4 codes (nabla(Q_n) = 2^(n-1) - A(n,4) iff an
  independent minimum decycling set exists).
- New here (not found in the sources searched, see sources.md): the inequality
  P(f) >= n + (d-1)\|D_f\| linking uphill paths to decycling sets for d-regular graphs; the matching
  construction (By-product A) giving U(G) = n + (d-1) nabla(G) when an independent minimum decycling
  set exists; the exhaustive nabla(Q_5) >= 14, nabla(Q_6) >= 28 searches with the edge-identity cut.
