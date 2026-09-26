#!/usr/bin/env python3
"""Stdlib-only integrity check (no mathematics).

Usage: python3 check_embedded.py <submission.md> <proof.md> [<pinned sha256>]

Extracts the text between the marker lines
    <!-- BEGIN EMBEDDED proof.md -->  ````text
and
    ````  <!-- END EMBEDDED proof.md -->
in submission.md, and checks that it is byte-identical to proof.md
(and, if given, that its sha256 equals the pinned hash).
Exit code 0 iff every check passes.
"""
import hashlib
import sys

BEGIN = "<!-- BEGIN EMBEDDED proof.md -->\n````text\n"
END = "````\n<!-- END EMBEDDED proof.md -->"


def main() -> int:
    sub_path, proof_path = sys.argv[1], sys.argv[2]
    pinned = sys.argv[3] if len(sys.argv) > 3 else None
    with open(sub_path, "rb") as f:
        sub = f.read().decode("utf-8")
    with open(proof_path, "rb") as f:
        proof = f.read()
    if sub.count(BEGIN) != 1 or sub.count(END) != 1:
        print("MARKERS: FAIL (expected exactly one BEGIN and one END marker)")
        return 1
    start = sub.index(BEGIN) + len(BEGIN)
    stop = sub.index(END)
    embedded = sub[start:stop].encode("utf-8")
    h_emb = hashlib.sha256(embedded).hexdigest()
    h_file = hashlib.sha256(proof).hexdigest()
    ok = embedded == proof
    print("embedded proof sha256:", h_emb)
    print("proof.md       sha256:", h_file)
    print("embedded == proof.md:", "OK" if ok else "FAIL")
    if pinned is not None:
        pin_ok = h_emb == pinned
        print("embedded == pinned hash:", "OK" if pin_ok else "FAIL")
        ok = ok and pin_ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
