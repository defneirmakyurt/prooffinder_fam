# Divergence: literature (A-C1-003) vs blind runs (A-C1-001, A-C1-002)

Compared, not merged. My proofs (out/proof.md) were written from the literature techniques; no blind step was copied.

## Verdicts
- A-C1-001: claims cell solved, complete proof, no gaps. A-C1-002: same. A-C1-003 (here): same, by two proofs.
- No contradiction anywhere: all three reach exactly the target S <= (pi/2) floor(N^2/4) for all N >= 0, repetitions allowed, and all note sharpness via floor(N/2)/ceil(N/2) copies of two perpendicular lines. Literature agrees: FVZ 2016 Theorem 2.1 is precisely this inequality; Bilyk-Matzke 2018 Section 4 lists it as settled.

## Approaches

| run | core idea | relation to literature |
|---|---|---|
| A-C1-001 (blind) | theta = rho(a-b) = dist(a-b, pi Z); cut indicator g = 1[rho(z) < pi/4] (open quarter-arc centred at the cut direction, period pi); overlap lemma int g(s)g(s-theta) = pi/2 - theta; count k(N-k) | Same as the L2 quadrant-discrepancy / Stolarsky identity for S^1 in Bilyk-Matzke Sec. 4.3: their Q(x) = {y : abs(x.y) > sqrt2/2} is exactly {rho < pi/4}, and sigma(Q(y) cap Q(z)) = 1/2 - (1/pi) arccos abs(y.z) is A-C1-001's overlap lemma (Step 7) after normalisation. Found blind, independently. |
| A-C1-002 (blind) | double the angles (u = 2a) so theta = half the arc distance on the circle of length 2 pi; Crofton identity with half-open semicircles; count k(N-k) | Same Crofton/cut-averaging family (semicircles on the doubled circle = quarter-turn arcs on R/pi Z). Also a variant of Bilyk-Matzke Sec. 4.3. Its integer step (k(N-k) <= N^2/4 plus integrality) is slicker than the parity split in A-C1-001 and here. |
| A-C1-003 Proof A (here) | half-open quarter-turn arc chi = 1[u mod pi in [0, pi/2)], identity via abs(p-q) = p+q-2pq, count k(N-k) | Taken from the literature (Bilyk-Matzke Sec. 4.3). Substantively the same route as both blind runs; differs only in normalisation (half-open arc starting at the cut rather than centred arc or doubled circle). |
| A-C1-003 Proof B (here) | for a perpendicular pair l, l' and any line m, theta(l,m) + theta(l',m) = pi/2; existence of a maximiser; first-order analysis at a maximiser without perpendicular pairs (no coincidences, balanced sides); slide one line at constant S until it becomes perpendicular to or coincident with another; induction N -> N-2 | Idea from FVZ 2016 Section 2 (proof of Theorem 2.1). Not used by either blind run. The maximiser/local-analysis/induction organisation (Steps B3-B6) is new here as a write-up: FVZ instead continuously transform any configuration without decreasing S and leave several steps as "clearly"/"obvious"/"by symmetry" (compactness, choice of side, monotonicity during rotation). Proof B fills those. |

## Where the approaches differ in substance
1. Global vs variational. The cut-averaging proofs (both blind runs, Proof A) are global identities: S = (1/2) int k(t)(N-k(t)) dt, which also gives an exact formula for the deficit (pi/2) floor(N^2/4) - S as an integral of (floor(N^2/4) - k(N-k)), i.e. an L2-discrepancy. Proof B is a variational argument (a maximiser exists, is locally balanced, and can be moved to contain a perpendicular pair) plus induction; it gives no deficit formula.
2. Which fact about d = 2 is used. Cut averaging uses that the "lines" space R/pi Z is a circle whose metric is a Crofton average of cuts (true on S^1, no exact analogue for projective spaces of higher dimension; Bilyk-Matzke use it only for S^1). Proof B uses theta(l,m) + theta(l',m) = pi/2 for l perpendicular to l' in R^2 (from cos^2 + sin^2 = 1). In R^d, d >= 3, sum_i theta(e_i, m) over an orthonormal frame is NOT constant (e.g. d = 3: m = e_1 gives pi, m = (1,1,1)/sqrt3 gives 3 arccos(1/sqrt3) ~ 2.86 < pi), so B1-B2 do not extend verbatim. This is a useful warning for cells 3-6.
3. Equality cases. None of the runs characterise all maximisers; Proof B's Step B4 gives a necessary condition (a maximiser without perpendicular pairs has no coincident lines and each line has equally many lines on each side), consistent with the odd-N extra maximisers (e.g. three lines at pi/3) noted by A-C1-002.

## Checks on the blind write-ups (spot-read, not a full referee pass)
- A-C1-001: Steps 3-8 consistent; Step 7 case split (s - theta in [-pi/2, pi/4) vs (-3pi/4, -pi/2)) covers all s in (-pi/4, pi/4) for theta in [0, pi/2]. Sanity script exact (Fraction). No issue found.
- A-C1-002: Steps 0-13 consistent; Step 9 computes D(s) = 2s on [0, pi] with the doubled circle; Step 12 integrality argument correct. Its sanity script is floating point, but it is declared non-load-bearing, so G7 is not affected. No issue found.
- Both handle N = 0, 1 and repeated lines explicitly.

## Provenance summary
- From the blind runs only: nothing I used.
- From the literature: cut-averaging identity (Bilyk-Matzke Sec. 4.3; also the Crofton idea implicit in both blind runs), perpendicular-pair invariance and the rotation step (FVZ Sec. 2).
- New here (as a write-up): the maximiser-based rigorous form of the FVZ argument (Steps B3-B6), including the first-order balance lemma B4.
