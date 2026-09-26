# Divergence: literature attempt (A-C2-003) vs blind solvers (A-C2-001, A-C2-002)

All three write-ups claim the full cell (all m >= 2) with no computation. I found no contradiction between them.
They are compared here, not merged; proof.md was written independently in a third form.

## Shared skeleton (all three)
- Reformulation: theta_k = pi/2 - phi_k with sin phi_k = |<x_k,x_{k+1}>|, so the target is sum phi_k >= pi/2.
  This is the obvious first move; all three reach it independently.
- Essentially the same trig inequality in different guises:
  - 001 (Step 3): cos^2 psi - sin^2 phi >= cos^2 psi cos^2(psi+phi).
  - 002 (Step 5): sin alpha / cos beta <= sin(alpha+beta).
  - 003 (Step 3): sin phi <= cos psi sin(psi+phi). This is 002's inequality with the roles relabelled, proved by the subtraction formula in one line. 002 expands instead.
  Mathematically all three say the same thing: the angle in the reduced chain is at most the sum of the two merged angles.

## Differences in route
| aspect | A-C2-001 (blind) | A-C2-002 (blind) | A-C2-003 (literature, this task) |
|---|---|---|---|
| object | leading principal minors D_k of the tridiagonal Gram matrix | geometric reduction: project out x_m, induct on m | Gram–Schmidt residual norms t_k = |x_k - P_{k-1} x_k| |
| recursion | D_k = D_{k-1} - a_{k-1}^2 D_{k-2} (Laplace expansion) | new last coefficient c_{m-2}/cos a_{m-1} in x_m^perp | t_{k+1}^2 = 1 - a_k^2/t_k^2 (projection + Pythagoras) |
| how dimension enters | det G = 0 (rank <= m-1) | base case m = 2 in R^1; each step drops one dimension | some t_k = 0 (m vectors in R^(m-1) are dependent) |
| direction | forward in k, contradiction | backward (removes the last vector), direct induction on m | forward in k, contradiction |
| case split | none | |c_{m-1}| = 1, and a_{m-2}+a_{m-1} >= pi/2 vs < pi/2 | none |

Relations: t_k^2 = D_k / D_{k-1} (standard: a product of Gram–Schmidt norms equals a Gram determinant). So 003 is the ratio form of 001's
minor recursion; 001's R4 "D_k >= cos^2 psi_{k-1} D_{k-1}" is exactly 003's "t_k >= cos psi_{k-1}". 002's reduction eliminates
from the other end. Its (m-1)-chain in x_m^perp is the "reverse" Gram–Schmidt (Schur complement on the last index).
The three are one continued-fraction recursion for a Jacobi matrix, run in different coordinates.

## Provenance of ideas
- From the blind runs: the determinant/minor form (001) and the dimension-reducing projection (002). I read both before writing, so 003 is not blind to them.
- From the literature (technique level only, sources not opened): the chain-sequence / continued-fraction view of positive definiteness of tridiagonal (Jacobi) matrices (Wall; Chihara; Szwarc 1998). This suggested writing the recursion in ratio form t_{k+1}^2 = 1 - a_k^2/t_k^2.
- New here relative to both blind proofs (a presentation difference, not a mathematical one): the Gram–Schmidt / projection derivation of the ratio recursion, which avoids cofactor expansions (001) and the case split (002), and the one-line subtraction-formula proof of the trig lemma.
- Found in no source: I could not locate the lemma itself in any source (see sources.md; all fetches blocked). In particular I could not check whether it appears as a step in a published proof of the N = d+1 case (cell A-C3).

## Points a referee should compare
- 001 Step 2's cofactor signs (checked: correct). 003 avoids them.
- 002 Step 4(4c) needs |i - m| >= 3 for i <= m-3 (true) and 4(4d) uses <x_{m-2}, x_m> = 0 (|m-2-m| = 2, true). Its isometry remark lets induction run in x_m^perp. Correct.
- 002's lemma needs sin alpha <= cos beta so that arcsin is defined. It gets this from Cauchy–Schwarz on the reduced chain. 003 needs no arcsin, so this issue does not arise.
- No contradiction found among the three. None depends on computation.
