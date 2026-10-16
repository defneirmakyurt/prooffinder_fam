# Provenance: A-C2 submission (task A-C2-020, scribe, SUBMISSION mode)

Not for the judge. Internal ids and paths only.

## Source
- Brief: run/tasks/A-C2-020/brief.md. CELL STATUS: SOLVED. CLAIM STATUS: PROVED (copied, not upgraded).
- Statement: inbox/statement.md, Cell 2 (copied verbatim into submission.md, LaTeX converted to \( \) / \[ \]).
- Proof: inbox/accepted/proof.md (sha256 3e08fea36e4a73353a09efda5019a7491e811a5f8522c7d3c88e6bcb3e9a3ea1).
- Claims table: inbox/accepted/claims.md (sha256 a584a63da39544a1180b69a1b88c34e8ad3876e53ce4ebbbf3229a1e35b5e1f3).
- Both hashes match inbox/accepted/MANIFEST.sha256.

## Mapping submission.md -> proof.md
Notation -> Notation; Step 1..7 -> Step 1..7 (same steps, same order, same labels (4a)-(4e));
"Remarks on edge cases" -> proof.md "Remarks", first bullet.

## Editorial changes (readability only)
- ASCII math rewritten as LaTeX; long sentences split.
- Omitted from the judge text: the "Regime BLIND" line (internal); the reference to the optional floating-point
  sanity script (out/code/sanity_lemma.py, not shipped in accepted/, not part of the proof); the "KNOWN GAPS: none found" line.
- Omitted: the sharpness remark in proof.md Remarks ("m=3, x_1=e_1, x_2=(cos t, sin t), x_3=e_2 ... gives theta sum = pi/2").
  It is marked "not required" in proof.md and does not state the range of t (the identity theta(e_1, x_2) = t needs
  t in [0, pi/2]); rather than add that range, the remark was dropped. It is not a claim of the cell.

## Shipped files (out/submission/, byte-identical to inbox/accepted/)
proof.md, claims.md, MANIFEST.sha256.

## RAN
- `cd out/submission && time sha256sum -c MANIFEST.sha256` -> "proof.md: OK", "claims.md: OK"; real 0m0.002s.
  Log: out/verify/logs/manifest_check.txt. (/usr/bin/time is not installed; bash `time` builtin used.)
