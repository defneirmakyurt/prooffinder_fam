# Lessons changelog

One entry per lessons edit (role files, pending files, run/<P>/lessons.md). Each edit is committed to git.

```
## <hh:mm> <role or problem P> v<old> → v<new>
- Change: <added / sharpened / merged / reverted: text>
- Evidence: <task ids>
- Result after next wave: <pending | improved: ... | no change → reverted | worse → reverted: why>
```

## 14:05 scribe v0 → v1
- Change: added three lessons — save a log for every RAN line (the Auditor has no Bash); treat counts and inventories as citations and verify them against the record before writing them; say which snapshot of `record/` you mean when citing it.
- Evidence: A-C1-008, A-C1-009
- Result after next wave: pending (dry run ended at this cell)

## 14:05 searcher v0 → v1
- Change: added two lessons — emit more than one attaining artefact when a search establishes an optimum; name the single soundness assumption a lower bound rests on and report node/state counts so two searches can be told apart.
- Evidence: H-C1-003, H-C1-004
- Result after next wave: pending (dry run ended at this cell)

## 12:22 scribe v1 → v2
- Change: sharpened the first lesson's reason: it said "the Auditor has no Bash", which the first dry run's own fix (Auditor given Bash, re-runs RAN lines) made false. The instruction (save a log for every RAN line) is unchanged; the reason now says the log is what the Auditor compares its re-run against.
- Evidence: A-C1-009 (the change that gave the Auditor Bash); second dry run (A-C2) read-through
- Result after next wave: pending (A-C2 Phase 5)

## 12:59 pending auditor v0 → v1 (awaits human approval; not copied into any inbox)
- Change: added one lesson: quotes must be verbatim; a wrong role, count or inventory is UNSUPPORTED; no "non-blocking wording" category.
- Evidence: A-C2-019 (PASS with four wording notes), A-C1-009 (FAIL on count/inventory errors)
- Result after next wave: pending approval
