# Code: A-C3-002

`evidence.py` (stdlib only). EVIDENCE ONLY: floating point, no proof step rests on it.

Run: `python3 evidence.py` (about 0.6 s).

It samples random inputs and reports the minimum slack seen for:
- (a) the target in the form T = sum_{i<j} arcsin|<x_i,x_j>| >= pi/2 for d+1 random unit vectors
  in R^d, d = 1..8, 3000 samples per d (some pushed near coordinate axes);
- (b) Lemma L (proof.md Step 2), 20000 samples;
- (c) the Key Lemma (proof.md Step 3), relative slack, 20000 samples.
Slacks of order -1e-16 are rounding (equality cases, e.g. d = 1 and d = 2 at 60 degrees).

Measured run (2026-09-26): completed, real 0.62 s. Output:
(a) min over samples of T - pi/2, by d: {1: 0.0, 2: -0.0, 3: 0.069139, 4: 0.232051, 5: 0.903341, 6: 0.776967, 7: 2.732875, 8: 3.163256}
(b) min slack of Lemma L: -3.3306690738754696e-16
(c) min relative slack of Key Lemma (should be > 0): 1.2968238705113322e-09

`../tmp/probe_M.py` is scratch (float hill-climb on the Perron root of [sin alpha_ij]); not used.
