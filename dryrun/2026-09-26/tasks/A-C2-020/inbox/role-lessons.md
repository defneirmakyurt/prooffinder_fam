version: 2
# Lessons: scribe
<!-- Head-editable lessons layer. Refines the locked core in .claude/agents/scribe.md, never overrides it. ≤ ~30 lines.
     Format: - <lesson> (evidence: <task ids>; added <hh:mm>; version <n>)
     No lesson may weaken verification: gate, referee checklist, exactness, runtime, isolation, status labels, RAN. -->

- Every RAN line must have its output saved as a file under out/ (e.g. out/verify/logs/<name>.txt), the way referees save theirs in out/cex/. The Auditor re-runs RAN lines from a copy and compares outputs with your saved log: a RAN line with no log gives it nothing to compare against, and it will list it as a gap. (evidence: A-C1-008, A-C1-009; added 14:05; version 1; reworded 12:22 v2: the Auditor now has Bash)
- Counts and inventories are citations too, and they are where reports actually fail: "seven tasks", "three referee passes", "the only seed is X". Before writing any count, list the items and count them in the record; before writing "only"/"no other", grep the whole record for counter-examples. (evidence: A-C1-008, A-C1-009; added 14:05; version 1)
- Your inbox/record/ is a snapshot taken when your task was created, so it may not contain your own task's row. Say which copy you mean when you cite it ("the copy shipped to this task"), and cite anything newer to your own brief.md. (evidence: A-C1-008; added 14:05; version 1)
