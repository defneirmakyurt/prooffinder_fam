version: 1
# Lessons: searcher
<!-- Head-editable lessons layer. Refines the locked core in .claude/agents/searcher.md, never overrides it. ≤ ~30 lines.
     Format: - <lesson> (evidence: <task ids>; added <hh:mm>; version <n>)
     No lesson may weaken verification: gate, referee checklist, exactness, runtime, isolation, status labels, RAN. -->

- When a search establishes an optimum, emit more than one attaining artefact (the first found and a randomised or structurally different one). Two blind searchers that both emit the lexicographically first minimiser produce byte-identical files, which makes independent lineages look like one and destroys the corroboration value of running two. (evidence: H-C1-003, H-C1-004; added 14:05; version 1)
- State the soundness assumption your lower bound rests on as one named claim ("the bound is exhaustive over class X given LB admissibility"), and give the run that rests on the fewest assumptions as the headline: a referee can read one assumption and cannot read a pile. Report the node/state count for every run so a reader can tell two searches apart. (evidence: H-C1-003, H-C1-004; added 14:05; version 1)
