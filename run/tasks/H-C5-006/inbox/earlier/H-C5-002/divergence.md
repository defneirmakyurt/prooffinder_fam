# Divergence: H-C5-002 (Phase 1L, EARLY)

inbox/earlier/ does not exist for this task (brief: "the Phase 1 blind searcher for this cell is still
running"). So there is NO blind result to compare against; nothing below is taken from a blind run.
The only earlier-phase file read is inbox/earlier-C1-sources.md (a literature worker, H-C1-006), which gives
the IMO 2022 P6 bound P >= |E| + 1 for any graph.

## Origin of each idea used here
| idea | origin |
|---|---|
| P >= |E| + 1 (one path per edge, plus a valley) | literature (IMO 2022 P6 solutions, via inbox/earlier-C1-sources.md) |
| Recursion N(v) = [valley] + sum of lower N(w) | inbox/checker/verify.py docstring (and standard) |
| Exact identity P = 2^d + (d-1)|S| + sum_{S}(N-2)up with S = {N >= 2}, and "V \ S is a forest with one component per valley", "S is closed upwards" | new here (derived in this task; not found in the sources searched) |
| Link to the decycling number: U(Q_d) >= 2^d + (d-1) nabla(Q_d) | new here (same derivation); decycling number itself is literature (Beineke-Vandell 1996; Bau survey 2007) |
| Parity-class-minus-distance-4-code construction (forest = odd vertices + code words, i.e. disjoint stars) | the forest/decycling side is literature (Pike 2003 abstract: nabla(Q_n) = 2^{n-1} - A(n,4) iff an independent minimum decycling set exists [not opened]; Bau survey Thm 2.2 on stars S(x) in one partite class [opened]); its use as a labelling (stars first, then the even non-code vertices as peaks) and the count 2^d + (d-1)(2^{d-1} - |M|) are new here |
| Values nabla(Q_n), n <= 8, and 225 <= nabla(Q_9) <= 237 | literature (Bau survey, citing Beineke-Vandell and Bau-Beineke-Du-Liu-Vandell) |
| Reading 2368 = 512 + 8*232 and 2400 = 512 + 8*236 | new here (arithmetic; the interpretation that the organisers used nabla(Q_9) >= 232 is a guess) |
| SA for maximum induced forests; observation that optimal-size decycling sets of Q_9 found by SA are of type 234 + 2 (not independent) | new here (computation) |

## Points a later comparison should check (when blind results arrive)
* If a blind solver reports a Q_9 labelling with <= 2399 paths, the checker count is authoritative; by
  proof.md Step 8 it would also give a decycling set of size <= 235 (S = {N >= 2}), which would be worth
  recording separately.
* If a blind solver reports exact values for C1-C4 other than 14, 34, 88, 204, 464, 1040, one of: the checker,
  their labelling, or the cited nabla(Q_n) table is wrong; my lower bound (5) plus the cited table rules out
  anything smaller.
* If a blind solver has a lower-bound argument for Q_9 beyond 2312, compare it with (5): any argument
  bounding |S_f| is a decycling-number bound in disguise.
