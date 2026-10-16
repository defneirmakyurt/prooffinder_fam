# Library entry: H-uphill-checker
KIND: code
WHAT: Exact stdlib uphill-path counter for a labelled hypercube: python3 verify.py Q<d>.txt prints VERIFIED <count>; input is 2^d lines of 0/1 strings in increasing label order.
FROM: run/H/C1/checker/verify.py
EVIDENCE: cross-test H-C1-001 vs H-C1-002: run/H/C1/crosstest/crosstest.log, 208 cases, 0 disagreements
ADDED: 2026-09-26 13:23, run time 0:48
