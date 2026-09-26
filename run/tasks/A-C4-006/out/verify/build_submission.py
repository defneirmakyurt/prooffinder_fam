#!/usr/bin/env python3
"""Assemble out/submission.md from the template by inserting verbatim extracts
(no text of the extracts is altered). Stdlib only.

Usage: python3 build_submission.py <task_dir> <T1> <T2> <PYNOTE>
"""
import sys
from pathlib import Path

task = Path(sys.argv[1])
t1, t2, pynote = sys.argv[2], sys.argv[3], sys.argv[4]
inbox = task / "inbox"
out = task / "out"

stmt_lines = (inbox / "statement.md").read_bytes().decode("utf-8").split("\n")


def lines(a: int, b: int) -> str:
    """1-based inclusive line range of statement.md, joined verbatim."""
    return "\n".join(stmt_lines[a - 1 : b])


cell = lines(159, 173)
defs = lines(41, 62)
general = lines(87, 90)
handin = lines(93, 107)
target_text = (inbox / "target.md").read_bytes().decode("utf-8").rstrip("\n")
assert "\n" not in target_text, "target.md expected to be a single line"

claims_lines = (out / "submission" / "claims.md").read_bytes().decode("utf-8").split("\n")
claims_table = "\n".join(l for l in claims_lines[2:] if l.strip())  # table rows, verbatim

proof = (out / "submission" / "proof.md").read_bytes().decode("utf-8")
assert proof.endswith("\n")

tpl = (out / "verify" / "submission_template.md").read_bytes().decode("utf-8")
repl = {
    "@@CELL@@": cell,
    "@@DEFS@@": defs,
    "@@GENERAL@@": general,
    "@@HANDIN@@": handin,
    "@@TARGET@@": target_text,
    "@@CLAIMS@@": claims_table,
    "@@T1@@": t1,
    "@@T2@@": t2,
    "@@PYNOTE@@": pynote,
}
for k, v in repl.items():
    assert tpl.count(k) == 1, k
    tpl = tpl.replace(k, v)
# proof last, so that nothing inside the proof is ever treated as a placeholder
assert tpl.count("@@PROOF@@") == 1
tpl = tpl.replace("@@PROOF@@", proof)
assert "@@" not in tpl.replace(proof, ""), "unfilled placeholder"
(out / "submission.md").write_bytes(tpl.encode("utf-8"))
print("wrote", out / "submission.md", len(tpl.encode("utf-8")), "bytes")
