# Submission: Problem B, Cell 3 (A General Upper Bound) — PARTIAL

Hand-in format required by the cell: a written proof (LaTeX). The LaTeX hand-in is `out/submission.tex`
(compiled: `out/submission.pdf`, 7 pages). This file is the cover note.

## Statement (verbatim)

Definitions (verbatim, problem statement): a partition of n >= 1 is a weakly decreasing sequence of positive
integers with sum n (s piles). B(lambda): the positive numbers among lambda_1 - 1, ..., lambda_s - 1, together with
one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k.

C3 (verbatim): "Now the numbers strictly between two consecutive triangular numbers.
(a) Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.
(b) Determine D_B(T_k - 1) exactly.
(c) Determine also, for that n, which partitions attain the maximum."

## Cell status and claim status

- CELL STATUS: PARTIAL
- CLAIM STATUS (of the established claim): PROVED

Claims established:
1. (b) LOWER half: for every k >= 3, lambda*_k = (k-1,k-2,k-2,k-3,...,2,1,1) is a partition of T_k - 1 with
   d_B(lambda*_k) = k^2-2k-1, hence D_B(T_k - 1) >= k^2-2k-1. Status: PROVED (accepted proof.md sections 0-6,
   gated VALID by two referees).

Remaining gap (exact, from the brief):
- (a) the upper bound d_B <= k^2-2k-1 for every non-triangular n of rank k >= 4;
- the upper half of (b) (so D_B(T_k-1) = k^2-2k-1 is NOT established);
- (c) the maximiser set.
All three OPEN; proofs in progress, not gated.

## Cited vs. ours

- Cited: the Cell 1 classification of cyclic partitions (earlier cell C1 of this problem, gated earlier in this
  run; not re-proved). Form used: for n = T_{k-1} + r, 1 <= r <= k, the cyclic partitions are
  lambda(e) = (k-1+e_1, ..., 1+e_{k-1}, e_k), e in {0,1}^k, sum e = r. Used only in Lemma R2 (proof.md 2.5).
- Ours (team): Lemmas R1-R6 (proof.md sections 0-6): rotation lemma (R1), energy characterisation of cyclicity
  (R2), classification of Phi=1 partitions (R3, R3'), exact d_B formula in case B (R4), maximum over case B (R5),
  lower bound (R6). Accepted artefact proof.md, sha256
  e86838d6c354e239e3201105542c8b83e77e6aa312dfc62488c6a18818c86c7b (verified against accepted/MANIFEST.sha256).

## Proof

`out/submission.tex`, sections 0-6: a faithful LaTeX transcription of accepted proof.md sections 0-6, keeping
the paragraph numbering (0.1-6.1) and the lemma labels R1-R6. Sections 7-9 of proof.md (not gated) are not
included as results. Chain: R1 (1.3) -> R2 (2.5, uses Cell 1) -> R3 (3.4) and R3' (3.5) -> R4 (4.5) -> R5 (5.3,
5.4: lambda*_k is the unique Phi=1 maximiser for T_k - 1) -> R6 (6.1).

## How to verify

Not load-bearing for the proof (it checks the R4 formula, lines "(L)", and the finite-range statements below).

- Command (in `out/submission/code/`, stdlib only): `/usr/bin/time -p python3 check_c3.py 10`
- Actually run on a copy at `out/verify/run/check_c3.py` (byte-identical to the inbox copy). Full output:
  `out/verify/logs/check_c3_K10.txt`.
- Expected/observed output: last line `ALL OK`; exit status 0.
- Measured runtime: real 26.93 s, user 26.66 s, sys 0.14 s (Python 3.14.0). Under the 10-minute limit.

Numerical evidence (NOT proof; finite range only; from that run):

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| T_k - 1 | 2 | 5 | 9 | 14 | 20 | 27 | 35 | 44 | 54 |
| D_B(T_k - 1), computed | 0 | 3 | 7 | 14 | 23 | 34 | 47 | 62 | 79 |
| k^2-2k-1 | -1 | 2 | 7 | 14 | 23 | 34 | 47 | 62 | 79 |

The run also reports D_B(n) <= k^2-2k-1 for every n with T_{k-1} < n < T_k, 4 <= k <= 10 (lines
"k=K: (A) checked ..."). None of this says anything about k >= 11.

LaTeX: `latexmk -pdf -interaction=nonstopmode submission.tex` in `out/` exited 0, produced
`out/submission.pdf` (7 pages); log `out/verify/logs/latexmk.txt` (Latexmk 4.88, pdfTeX TeX Live 2026). Two
small overfull-hbox warnings (5.9 pt, 18.2 pt), no errors, no undefined references.

## Shipped files (`out/submission/`)

- `code/check_c3.py` (sha256 227cc093b9d76106341c49d20444365023c77f74663ef238372cbe5c56d7e303)
- `code/README.md` (sha256 0fc4142c5f0854692f595e005ebb3e1e4e8957c7d22e298e59b011b708fb64ac)
Both byte-identical to `inbox/accepted/code/` (checked with cmp and against MANIFEST.sha256).

## Limitations

- Only the lower half of (b) is established. (a), the upper half of (b), and (c) are OPEN.
- Lemma R2, and everything after it, relies on the cited Cell 1 classification of cyclic partitions.
- proof.md sections 7-9 (the family mu_k / M_k, the partial upper-bound analysis, the maximiser computations,
  and the by-hand small-k values) were not gated and do not appear as results.
- The shipped README reports a 28.71 s runtime from an earlier run; this run measured 26.93 s. The README is
  shipped unchanged (byte-identical).
- proof.md 4.5 cites `out/code/check_c3.py` "for 3 <= k <= 10"; in the LaTeX this became
  `code/check_c3.py`, 3 <= k <= K (the checker runs (L) for k >= 3 and 2 <= r <= k-1). Only the path and range
  wording were changed, no mathematics.
- The "(L) ... max=" value the checker prints is the formula (k+1)(r-2)+2. The checker does not compute it
  independently, so those lines do not check R5.
