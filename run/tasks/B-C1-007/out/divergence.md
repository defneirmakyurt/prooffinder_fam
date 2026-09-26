# Divergence: blind runs (B-C1-001, B-C1-002) vs literature vs this run (B-C1-007)

Compared, not merged: out/proof.md was written from the literature techniques below; no blind proof text was copied.

## 1. Answers: no contradiction
All three runs and all opened sources give the same answers:
- (ii)(a) cyclic partitions of T_{k-1}+r = (k-1+e_1, ..., 1+e_{k-1}, e_k), e in {0,1}^k, |e| = r (final 0 dropped); binom(k,r) of them.
  B-C1-001 (0-based, set C(k,r)), B-C1-002 (1-based), this run (1-based), Drensky Thm 2, Hart-Khan-Khan Thm 1, Mestrovic's statement of Etienne/Brandt.
- (ii)(b) #cycles = (1/k) sum_{d|gcd(k,r)} phi(d) C(k/d, r/d) (binary necklaces): B-C1-001 Thm 12, B-C1-002 10.4, this run Thm 12, Drensky Thm 2, HKK Cor. 9, OEIS A047996.
- (i) delta_k unique cyclic partition of T_k, reached from everywhere: all runs; Brandt (per Mestrovic), Drensky Thm 1, HKK Thm 1.
Convention difference only: the literature writes n = T_k + r, 0 <= r <= k (or T_m <= n < T_{m+1}; HKK Cor. 9 assumes n non-triangular); the target uses r in [1,k]. At r = k the formula gives 1, consistent with (i).
Brute force: blind scripts (n <= 45) and the independent script here (n <= 50) agree.

## 2. Where the approaches differ

| step | B-C1-001 (blind) | B-C1-002 (blind) | literature | this run |
|---|---|---|---|---|
| monotone quantity | E = sum_a (a x_a + C(x_a,2)) (0-based); general sorting lemma by adjacent swaps (bubble sort) | E = sum of levels; general sorting lemma via prefix sums (majorization) | Drensky/Bjorner: potential energy, drop when the new pile is inserted lower ("cradle model"); HKK/Toom: per-cell statement "a checker never moves to a higher diagonal" | E = sum of levels; B = one insertion of s into the sorted tail; explicit drop E(B l) <= E(l) - (p-1) (Lemma 3) |
| key lemma (no hole below a cell) | any two levels d < d' (Prop. 7), via Bezout and a choice 0 <= c* <= d'-d; cell (c*, d'-c*) sits above hole (0,d) | adjacent levels d, d+1, CRT (gcd(d,d+1)=1) | adjacent levels: HKK Lemma 6 (CRT); Drensky: progression 0,(r+2),2(r+2),... (coprime adjacent levels) | adjacent levels, Drensky's progression t0 + j(l+1), j = 0..l-1, no CRT (Lemma 5) |
| shape of cyclic partition | directly from Prop. 7 (min level with a hole, nothing above) | induction on levels via adjacent lemma | HKK: contrapositive, minimal mixed diagonal; Drensky: minimal energy state | induction via adjacent lemma (Prop. 6) |
| converse B(l(e)) = l(rho e) | compare mu = (s, l_0-1, ...) with L(rho e) entrywise | multiset comparison | "beads rotate" (Drensky, HKK), not written in detail | cell set of l(e) (Lemma 7) + R rotates level k (Lemma 2) |
| necklace count | Burnside proved inline | Burnside proved inline | "standard exercise in Polya enumeration" (HKK Cor. 9; Drensky), not written out | Burnside proved inline |
| Brandt's own method | - | - | per Mestrovic: sequences sigma of pile counts, Prop. 2 (sigma_i in {n, n-1}) (NOT opened) | not reproduced |

Most general key lemma: B-C1-001's Prop. 7 (arbitrary d < d') is stronger than the adjacent version used by B-C1-002, the literature and this run; it is not needed for the cell.

## 3. Provenance of ideas
- From the blind runs (independently of the literature): energy + "no sorting on a cycle" (both); CRT on adjacent levels (B-C1-002, coincides with HKK Lemma 6 / Toom); Bezout lemma for non-adjacent levels (B-C1-001; not found in the opened sources: Drensky arXiv:1503.00885, HKK arXiv:1101.1546, Mestrovic arXiv:2607.17194).
- From the literature (used here): cradle-model energy with single insertion, the arithmetic-progression trick, the necklace identification, all attributions.
- New here: nothing is claimed new. The explicit bound E(B l) <= E(l) - (p-1) is not stated in that form in the opened sources, but is implicit in Drensky's cradle-model argument.

## 4. Checks of the blind proofs made while comparing (not a referee report)
- B-C1-001 Prop. 7: verified the choice j = (um) mod Q gives jP = c* - y - t0 (mod Q) and d' - c* >= d; correct.
- B-C1-002 Lemma 6: CRT solution t >= 0 exists (take the least nonnegative residue mod d(d+1)); positions map to (1,d) and (1,d+1); correct.
- No contradiction found with the literature or with this run.
