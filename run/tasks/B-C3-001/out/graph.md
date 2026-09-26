# Graph: B-C3 (target) and spaces/neighbours

Nodes: TGT(a) bound k^2-2k-1 for T_{k-1}<n<T_k, k>=4; TGT(b) D_B(T_k-1); TGT(c) extremizer set E_k;
C1 (cyclic partitions, Brandt); C2 (D_B(T_k)=k^2-k); C4/C5 (n=T_{k-1}+1, +2); GH Conj 4.7 (all n); S1..S6.

Edges
- C1 => used by all: Brandt's cyclic characterisation (GH Thm 2.1, PROVED, argument in [GH]) is the cyclicity test in S1-S5.
- C2 + S3 => D_B(n)<=k^2-k (GH Thm 4.2, PROVED). Bounds flow C2 -> TGT only as k^2-k; S3 TIGHT NO (explicit objects in
  spaces.md), so C2+S3 cannot prove TGT(a). Load-bearing property of the C2 route (Lemma 3.3: the tail <k-1,k,k,...>) is
  replaced for non-triangular n by GH Lemma 4.3 (periodicity c_{t+i}=c_{t+i+k}); the target has it (CHECKED consistency:
  Prop 3.2 holds on all n<=22).
- TGT(a) at n=T_k-1 => upper half of TGT(b) for k>=4. TGT(b) lower half <= S1/S4 construction lambda_k (CHECKED k=4..15).
- S2 => TGT(a): GH Thm 4.4(1) (PROVED, k=4 via computer table; argument present). A counterexample to TGT(a) would kill S2's
  chain; none exists for n<=44 (CHECKED k<=9 at T_k-1; all non-triangular n<=30).
- S2 (equality case) => TGT(c) "no other partition" direction; S5 => TGT(c) "every listed partition attains" direction
  (E_k = B^{-L_k}(mu_k), CHECKED k=6..9). Pairing for (c): S2 (necessary conditions) + S5 (sufficiency via mu_k).
- S4 (single-drop) => part of TGT(c): the GH extremizer is single-drop; multi-drop extremizers exist (k>=5), so S4 alone
  cannot classify E_k (obstruction: E_5 contains lambda with 3 drops, e.g. drop pattern (1,2,13)).
- TGT(c) method => C4/C5: C5 asks where "the Cell 3 argument" stops, so the S2 route is the one the board expects to reuse.
- S6 (Carolina) ~ TGT(a): ANALOGY only; both lose k+1 from the triangular value (GH Sec. 5).
- GH Conj 4.7 (CONJECTURED, checked n<=36 in [GH]): at r=k-1 its lower bound (r-2)k+r = k^2-2k-1 agrees with TGT(b).

Pairing rule for (b): bound side S2 (EQUIVALENT, GH chain) + construction side S1/S4 (lambda_k). They agree on k=4..9
(D_B computed exhaustively) -> exact value k^2-2k-1 for k>=4 is reachable; k=2,3 separate (0 and 3).

NEIGHBOUR QUESTION: Does Etienne (JCTA 58, 1991) Thm 5.1 or Igusa (Math. Mag. 58, 1985) characterise max-depth partitions
for non-triangular n, in particular n=T_k-1? (not opened; paywalled / not parseable in time box)
NEIGHBOUR QUESTION: Is there any published characterisation of the extremizers of D_B(T_k) or D_B(T_k-1) beyond GH Thm 3.8
(e.g. in Hopkins, "30 years of Bulgarian solitaire", College Math. J. 43 (2012))?
