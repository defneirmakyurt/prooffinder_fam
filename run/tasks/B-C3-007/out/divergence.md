# Divergence: literature route (B-C3-007) vs blind solvers (B-C3-002, B-C3-004)

The two routes are compared here, not merged. No blind proof text is used in out/proof.md.

## Outcomes side by side

| item | B-C3-002 (blind) | B-C3-004 (blind) | B-C3-007 (this, literature) |
|---|---|---|---|
| (a) all k>=4 | GAP for k>=11; CHECKED 4<=k<=10 | PROVED only on the class C_k (between delta_{k-1} and delta_{k+1}); full statement GAP, CHECKED k<=10 | PROVED for every k>=4 (proof.md 5.1), k=4 included by hand |
| (b) lower bound, witness lambda*_k | PROVED k>=3 (energy-1 "case B" dynamics) | PROVED k>=3 (two-ring rotation) | PROVED k>=3 (row-vector rotation, proof.md 6.4) |
| (b) equality | CHECKED k<=10 | CHECKED k<=10 | PROVED k>=4, plus k=2,3 by hand |
| (c) | "maximisers = {B^{k^2-4k-2}(lambda)=mu_k}", mu_k=(k,k-1,k-1,k-3,...,3,1); inclusion PROVED, equality CHECKED 6<=k<=10 | "maximisers = {B^{k^2-2k-2}(lambda)=nu_k}"; inclusion PROVED (Prop. 9.1), equality CHECKED k<=10 | the same set as B-C3-004, both inclusions PROVED for every k>=4 (9.1, 9.2) |
| counts of maximisers | 1,6,34,175,831,3911,18163 (k=4..10) | the same | 1,6,34,175,831,3911 (k=4..9), the same values |

No contradictions. Every value computed in the three runs agrees: D_B(n) for 4<=k<=9, D_B(2)=0, D_B(5)=3, the witness, nu_k, and the maximiser counts.

## Where the approaches differ

1. **Upper bound (a).**
   - Both blind solvers work with the geometry of the Young diagram:
     - B-C3-002 uses the energy (sum of diagonal indices) and the excess Phi.
     - B-C3-004 uses particles and holes on diagonals k-1, k, k+1.
   - Both could only control configurations already close to the cycle (Phi=1, or the class C_k). Both identify the missing piece as a potential coupling "time before entering the near-cycle region" with "phase after entering".
   - The literature route (Griggs-Ho) never looks at diagram geometry. It works only with the sequence c_i of numbers of parts and the "pile/row" bookkeeping (proof.md Step 1).
   - The key tool is the descent lemma 2.1: a plateau pattern (x-1,x,...,x,x+1) at position p forces a strictly shorter plateau pattern about x steps earlier.
   - Iterating the descent lemma charges the whole pre-period to the length of the pattern (2.2: p <= (L-1)X). It covers every partition at once, without splitting the orbit into phases.
   - This is exactly the coupling the blind solvers were missing. Neither blind run used the c_i-sequence idea; it comes from the literature.
2. **Entry into the cycle.**
   - Here the argument uses the minimal time tau at which the orbit is cyclic with c_tau=k-1 and c_{tau+1}=k (4.1), plus the trichotomy of 4.2 (GH Lemma 4.3).
   - The blind runs instead use explicit rotation formulas inside the near-cycle class.
3. **Witness (b).**
   - All three runs compute the orbit of lambda*_k by an explicit rotation: one "hole" set rotating with period k and one extra cell rotating with period k+1, until they collide at time k^2-2k-2.
   - The notation differs: B-C3-002 uses diagonal cells (H,c), B-C3-004 uses (A,P) pairs, and this run uses row vectors ell_i(H,pi) (proof.md 6.1-6.2).
   - The mechanism is the classical array shifting of GH Section 2 (also Akin-Davis and Etienne). GH do not write out this step: Thm 4.4(2) just says "imitating the proof of Theorem 3.1".
   - All three write-outs are independent.
4. **Maximisers (c).**
   - B-C3-004 and this run give the same criterion (depth k^2-2k-2 above nu_k).
   - B-C3-002 gives a different one: depth k^2-4k-2 above mu_k, where B^{2k}(mu_k)=nu_k along the orbit of lambda*_k. Since every orbit through mu_k at that time reaches nu_k at time k^2-2k-2, their set is contained in ours.
   - The two sets agree for 6<=k<=10 (their computation). For k>=11 their equality claim is stronger than what anyone has proved, and it is open here.
   - The proof of the "only these" direction (9.2) is new here: it is not in GH or in the blind runs. It reads off the equality case of the literature bound: tau = k^2-2k forces case (i), then p=tau-k and L=k-2, then R_tau is determined, which pins down B^{tau-1}(lambda) and B^{tau-2}(lambda)=nu_k.
5. **k=4.**
   - GH prove (a) for k=4 only through their computer table (Fig. 1).
   - Both blind runs check k=4 by computer.
   - This run proves k=4 by hand (proof.md 5.1, case (ii) L=k). The only possible exceptions are (9), (2,1^7) and (1^9), and their orbits are written out. The same device gives (c) for k=4 (9.2). New here.

## Provenance of ideas

- **From the literature (GH 1998):** the pile/row diagram; the patterns; the sandwich, descent and counting lemmas; the long-pattern lemma (3.1); the entry lemma (4.2); the witness lambda*_k; the statement of (a) and (b).
- **From the blind runs:** nothing was used in out/proof.md. The blind runs independently found the same witness, the same nu_k (B-C3-004), and the obstruction description. That description matches what GH's descent lemma supplies.
- **New here** (not found in sources.md):
  - a hand proof of (a) and (c) for k=4;
  - the proof of (c) for all k>=4 (9.2);
  - the merged single-lemma form of GH Lemmas 3.5/3.6 (2.1), with its induction written out;
  - the explicit row-vector verification of the witness orbit (6.2-6.4);
  - the recognition criterion 0.4, used to turn GH's "rectangle below c_{t-k-1}" step into a check on conjugate counts (4.2, B3).
