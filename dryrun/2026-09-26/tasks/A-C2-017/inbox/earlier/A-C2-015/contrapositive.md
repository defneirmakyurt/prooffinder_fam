# Task 1: contrapositive

P: x_1..x_m unit vectors in R^(m-1) with <x_i,x_j>=0 for |i-j|>=2.
Q: sum_{i<m} theta(x_i,x_{i+1}) <= (m-2) pi/2, equivalently (arccos = pi/2 - arcsin) sum_i phi_i >= pi/2 with phi_i = arcsin|<x_i,x_{i+1}>|.

not-Q => not-P. Assume the chain relations hold (in any R^n) and sum phi_i < pi/2. Forced structure:
the Gram-Schmidt residuals u_k of the chain satisfy |u_k| >= cos(phi_1+...+phi_{k-1}) > 0. Reason: because x_k is
orthogonal to x_1..x_{k-2}, the only part of span(x_1..x_{k-1}) that x_k "sees" is the direction u_{k-1}, giving the
exact recursion sin(beta_k) = sin(phi_{k-1}) / cos(beta_{k-1}), where beta_k = angle(x_k, span(x_1..x_{k-1})), beta_1 = 0.
The one-step identity cos(a) sin(a+p) - sin(p) = sin(a) cos(a+p) >= 0 (a,p>=0, a+p<=pi/2) shows beta_k <= phi_1+...+phi_{k-1} by induction.
So all residuals are nonzero, the x_k are linearly independent, and they need m dimensions: not-P (they cannot lie in R^(m-1)).

This is a complete argument; written out as out/proof.md (numbered steps) with out/claims.md.

Hand checks of smallest cases:
- m=2: x_1,x_2 in R^1 => x_2 = +-x_1, a_1 = 1, phi_1 = pi/2. Equality.
- m=3: Gram matrix [[1,c1,0],[c1,1,c2],[0,c2,1]] has det 1 - c1^2 - c2^2, must be 0 (3 vectors in R^2) => a1^2+a2^2 = 1 =>
  arcsin a1 + arcsin a2 = pi/2 exactly (arcsin a2 = arccos a1). Equality on the whole curve.
