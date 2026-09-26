# B-C2 submission: D_B at triangular n

Hand-in format required by the cell: a written proof (LaTeX), stating clearly what is established.
The hand-in is `out/submission.tex` (compiled: `out/submission.pdf`, 9 pages); a copy of both, the shipped code and
the pinned accepted artefacts are in `out/submission/`. This file is the cover sheet.

## Statement (verbatim, from the brief's TARGET)

Definitions (verbatim from the official statement): a partition of n >= 1 is a weakly decreasing sequence
lambda = (lambda_1, ..., lambda_s) of positive integers with sum n (s piles). The shift B(lambda) is the partition whose
parts are the positive numbers among lambda_1 - 1, ..., lambda_s - 1 together with one extra part equal to s.
lambda is cyclic if B^i(lambda) = lambda for some i >= 1.
d_B(lambda) = min{ i >= 0 : B^i(lambda) is cyclic },  D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, k-1, ..., 2, 1).

Cell text (verbatim): "Next, how long the process can take to reach a cycle, starting with the triangular
numbers. Determine D_B(T_k) for every k, with proof of both bounds."

Exact target: explicit F(k) (small-k exceptions stated exactly) with D_B(T_k) = F(k) for every k >= 1; UPPER bound
d_B(lambda) <= F(k) for every partition lambda of T_k, every k >= 1; LOWER bound: explicit lambda^(k) with
d_B(lambda^(k)) = F(k) for every k >= 1; any fact about which partitions of T_k are cyclic proved in the submission.

## Status

- CELL STATUS: SOLVED
- CLAIM STATUS: PROVED

Answer: D_B(T_k) = k^2 - k for every k >= 1, no exceptions (k=1 gives 0, k=2 gives 2).
Witness: lambda^(1) = (1); for k >= 2, lambda^(k) = (k-1, k-1, k-2, ..., 2, 1, 1), with d_B(lambda^(k)) = k^2 - k
(accepted/proof.md, Part A).

## Cited vs. ours

Cited (existing results; source: accepted/sources.md):
- J. R. Griggs, C.-C. Ho, The cycling of partitions and compositions under repeated shifts, Adv. Appl. Math. 21 (1998)
  205-227 (https://www.sciencedirect.com/science/article/pii/S0196885898905978; preprint
  https://people.math.sc.edu/griggs/cycling.pdf). Thm 3.7 (D_B(T_k) = k^2-k) and its Prop 3.2, Lemmas 3.3-3.6 are the
  source of the upper-bound architecture; Thm 3.1 has the same witness; Thm 2.1 idea used in 0.3. Opened by the team.
- K. Igusa, Math. Mag. 58 (1985) 259-271; G. Etienne, J. Combin. Theory Ser. A 58 (1991) 181-197; H.-J. Bentz,
  Ars Combin. 23 (1987) 151-170: proofs of the same value per Griggs-Ho; not opened.
- R. Mestrovic, arXiv:2607.17194 (2026), survey confirming the attribution (no proof).

Ours: the full written proof in accepted/proof.md (Parts 0, A, B): every lemma used from Griggs-Ho is re-proved in full
(Lemma 3.5's "continue this process" written as the induction I(m) in B7), the orbit of the witness is written out
(Part A), and the cyclic-partition facts for T_k are proved (0.3). The result itself is the literature's; no citation
is used as a proof step.

## Proof

`out/submission.tex` / `.pdf`, Section 4: a faithful LaTeX conversion of accepted/proof.md with its numbering
(0.1-0.3, A.0-A.4, B1-B9). Editorial changes requested by the brief, no change to the mathematics:
1. Part B, first line: deleted "or the B-C1 assumption, which says the same" (0.3 proves the needed fact). Likewise the
   opening statement's "so the B-C1 assumption is not needed" is rendered as "so no result of Cell 1 is assumed".
2. B7: the invariant I(m) now states "p+m <= q-1" as its first clause (I(1): from q >= p+3; I(m+1): from step (a),
   which derives p+m <= q-2).
3. Part C code paths (out/tmp/...) now point to the shipped `code/` folder; Part C became the "How to verify" section.
4. Minor typographic changes (e.g. B9 "(x = k or k-1 <= k)" typeset as "(x = k or k-1; x <= k)"; B2 inequality displayed).

## How to verify

Proof check: read Section 4 of submission.pdf (no step depends on computation).
Sanity scripts (stdlib-only; not load-bearing), run from `out/submission/` with
`/Users/radu.cucu/Developer/bainsahackathon/.venv/bin/python3` (Python 3.14.0, macOS Darwin 23.4.0), timed with
`/usr/bin/time -p`; logs in `out/verify/logs/`:

| command | expected output | measured real time | log |
|---|---|---|---|
| `python3 code/witness.py 40` | `k=1..40 checked, failures: 0` | 1.91 s | witness_40.txt |
| `python3 code/dbt.py 8` | 8 lines, D_B = 0,2,6,12,20,30,42,56 = k^2-k; #max = 1,1,1,3,16,65,293,1267 | 0.64 s | dbt_8.txt |
| `python3 code/gh_lemmas.py 30 80` | `partitions checked 28628 n<= 30 seq length 80 violations L3.6: 0 L3.5: 0` / `L3.4 violations: 0  L3.3(2): cases 4411 violations 0` | 3.84 s | gh_lemmas_30_80.txt |
| `latexmk -pdf -interaction=nonstopmode submission.tex` (in out/) | exit 0, `Output written on submission.pdf (9 pages, ...)`, no overfull/undefined warnings | 0.66 s | latexmk.txt |

Integrity: sha256 of code/*.py and accepted/{proof,claims,sources}.md match inbox/accepted/MANIFEST.sha256
(out/verify/logs/sha256.txt). All arithmetic exact integer; total well under 10 minutes.

## Limitations

- Both bounds proved for every k >= 1 as the cell requires; nothing claimed beyond n = T_k (no classification of all
  maximisers for general k, nothing about non-triangular n).
- The correctness rests on the written argument; the most delicate step is B7 (index bookkeeping), flagged by the
  prover as the referee focus. The scripts are finite-range sanity checks only.
- Igusa, Etienne, Bentz, Brandt, Hobby-Knuth were not opened; their content is as reported in Griggs-Ho / the survey.
- Wording flag (not changed): accepted/sources.md says of Griggs-Ho Lemma 3.5 "(informal induction, not re-derived
  here)", while proof.md B7 and claims.md say it is re-derived as I(m). The proof text (B7) is what the submission uses;
  the sources.md phrase appears to refer to Griggs-Ho's own text but reads ambiguously.
