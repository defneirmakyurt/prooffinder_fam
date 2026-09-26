# Submission: Problem B, Cell 3 (A General Upper Bound)

Main document: `out/submission.tex` (compiled: `out/submission.pdf`, 10 pages). Source artefact: `inbox/accepted/B-C3-007/` only
(the earlier lower-half proof `accepted/proof.md` is not used).

## Statement (verbatim)
Definitions: a partition of n >= 1 is a weakly decreasing sequence of positive integers with sum n (s piles). B(lambda): the positive
numbers among lambda_1 - 1, ..., lambda_s - 1, together with one extra part equal to s. lambda is cyclic if B^i(lambda) = lambda for some
i >= 1. d_B(lambda) = min{ i >= 0 : B^i(lambda) cyclic }, D_B(n) = max{ d_B(lambda) : lambda a partition of n }.
T_k = k(k+1)/2, delta_k = (k, ..., 1); rank of n = the unique k with T_{k-1} < n <= T_k.

Cell 3: "Now the numbers strictly between two consecutive triangular numbers.
(a) Prove that for every k >= 4 and every non-triangular n with T_{k-1} < n < T_k, D_B(n) <= k^2 - 2k - 1.
(b) Determine D_B(T_k - 1) exactly.
(c) Determine also, for that n, which partitions attain the maximum."

## Status
CELL STATUS: SOLVED
CLAIM STATUS: PROVED

## Answers (as in accepted/B-C3-007/proof.md, header and Steps 5, 7, 9)
- (a) For every k >= 4, every n with T_{k-1} < n < T_k, every lambda |- n: d_B(lambda) <= k^2-2k-1 (Thm 5.1; k = 4 by hand).
- (b) D_B(T_k - 1) = k^2-2k-1 for every k >= 4, attained by lambda*_k = (k-1,k-2,k-2,k-3,...,2,1,1) (7.1, 6.4).
  Small k: k = 1: T_1 - 1 = 0 is not a positive integer (7.2); D_B(2) = 0 (7.3); D_B(5) = 3 (7.4).
- (c) Proved criterion: for every k >= 4 the maximisers are exactly {lambda |- T_k - 1 : B^{k^2-2k-2}(lambda) = nu_k},
  nu_k = (k+1,k-1,k-2,...,3,1) (9.3). k = 2: (2), (1,1); k = 3: (1^5) only (7.3, 7.4, 9.5).

## Cited vs. ours
- Cited (method): J. R. Griggs, C.-C. Ho, "The cycling of partitions and compositions under repeated shifts", Adv. Appl. Math. 21 (1998)
  205-227, DOI 10.1006/aama.1998.0597; preprint https://people.math.sc.edu/griggs/cycling.pdf. Prop. 3.2, Lemmas 3.3-3.6, 4.3, Thm 4.4.
  Every lemma is re-proved in full (proof.md header; sources.md row 1).
- Used as the earlier cell's result: the gated Cell 1 classification of cyclic partitions (proof.md Step 0, "ASSUMPTIONS").
  Per GH Thm 2.1 it is due to J. Brandt, Proc. Amer. Math. Soc. 85 (1982) 483-486 (sources.md; not opened).
- Ours: the pile/row write-up; steps GH leave as "similar"/"imitating" written out; k = 4 of (a) by hand; Step 6 witness proof;
  part (c) (Step 9). The maximiser characterisation was not found in the sources searched by B-C3-007 (sources.md: GH 1998, the
  Mestrovic 2026 survey fetch summary, Drensky 2015 and Harris-Nguyen 2023 abstracts, OEIS search).

## Proof
`out/submission.tex`: the accepted proof.md converted to LaTeX with the same step numbering (Steps 0-10). Editorial changes only:
1. "ASSUMPTIONS" is spelled out as "the Cell 1 result".
2. 4.2, Case B3: the sentence "(those are born after row tau-k... precisely, born pile j is alive only from row j+1 > tau-k)" is
   reworded as "since born pile j is alive only from row j+1 > tau-k"; same content.
3. 9.6: the "[GAP]" label (which referred only to the missing closed-form list) is removed; (c) is stated as a proved criterion
   characterising the maximiser set exactly.
The unedited accepted proof ships as `out/submission/proof.md`.

## How to verify (sanity only, not load-bearing)
Command (from `out/submission/code/`): `/usr/bin/time -p python3 check.py 9`
Expected output: the 34 lines of `out/submission/code/run.txt`, ending `ALL OK`.
Measured re-run: output identical to run.txt apart from timing lines (diff empty: `out/verify/logs/diff_vs_run_txt.txt`);
real 38.62 s, user 33.18 s, sys 0.54 s, Python 3.14.0 (log: `out/verify/logs/check_py_K9.txt`). run.txt records real 16.70 s.
Compile: `latexmk -pdf -interaction=nonstopmode -halt-on-error submission.tex` in `out/`: exit 0, 10 pages, real 0.62 s
(log: `out/verify/logs/latexmk.txt`).

## Limitations
- (c) is a proved criterion (B^{k^2-2k-2}(lambda) = nu_k) that characterises the maximiser set exactly; it is not a closed-form list
  of the maximisers as explicit functions of k (proof.md 9.6; claims.md last row: closed form OPEN). The humans ruled (SCOPE.md, 16:42)
  that the criterion counts as determining the maximisers.
- |E_k| = 1, 6, 34, 175, 831, 3911 (k = 4..9) and the k = 4, 5 lists are numerical evidence only (COMPUTER-VERIFIED, sanity).
- The Cell 1 classification is used as the earlier cell's result.

## Shipped files (`out/submission/`, byte-identical to inbox/accepted/B-C3-007/, sha256 as in MANIFEST.sha256)
- code/check.py a122db26f2892a542e72307f22ee27c767a7742a08e868359ec745049e1e6386
- code/run.txt 726f59e8bb29922f1085c9c259c7287badff335b29dd5942bcba7386ab702c57
- proof.md 52dff0b3361a02fbf632c68ca6f3009d27dfe16d0393058f81fd07c8c429257b
- sources.md 5569690d843e857c697f4973a34a338ed41129239a6b07d1e7308bcbf847c5f2
- claims.md 1ad6a98b552a113bdebb4c289a22c19b35ca3bffdc61644823fa0ac277c8b533
