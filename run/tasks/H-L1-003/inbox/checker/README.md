Accepted checker for H-L1: verify.py = library entry H-uphill-checker (sha256 in run/library/H-uphill-checker/MANIFEST.sha256), originally dry-run task H-C1-002 out/verify.py.
Cross-test: H-C1-001 vs H-C1-002, 208 cases (200 generated over d = 1..9 by seed % 9: lex, reverse, weight order, Gray code, random; plus 8 malformed-input fixtures), 0 disagreements: crosstest.log (copied from dryrun/2026-09-26/H/C1/crosstest/).
Usage: python3 verify.py Q<d>.txt [--d D]  ->  VERIFIED <count> | FAILED: <reason>
