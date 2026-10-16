# Task 4: minimal failing sub-case

Obstacle files (A-C2-001, -002, -010, -011) contain only "none", so no recorded failed argument is available to localise.
Natural naive routes and where they first fail:

1. Gershgorin route: singular I - A forces a row with a_{i-1} + a_i >= 1; one would then want arcsin a_{i-1} + arcsin a_i >= pi/2.
   Fails already at m = 3 (smallest nontrivial case): a = (1/2, 1/2) has a1 + a2 = 1 but arcsin sum = pi/3 < pi/2. (That a is not
   admissible, since det = 1/2 != 0, but the route cannot see this.) The correct m = 3 condition is a1^2 + a2^2 = 1.
2. Angle-triangle-inequality route: angle(x_k, V_{k-1}) <= theta_{k-1} bounds in the wrong direction (upper bound on the residual angle
   in terms of theta, while one needs a lower bound on |u_k| in terms of phi).

Precise sub-lemma that closes the gap (and is proved as step 5 + step 8 of out/proof.md):
  For alpha, phi >= 0 with alpha + phi < pi/2 and any beta in [0, alpha]: sin(phi)/cos(beta) <= sin(alpha + phi).
  (Monotone in beta, and at beta = alpha it is cos(alpha) sin(alpha+phi) - sin(phi) = sin(alpha) cos(alpha+phi) >= 0.)
Combined with the exact chain recursion sin(beta_k) = sin(phi_{k-1})/cos(beta_{k-1}) for the angle beta_k between x_k and span(x_1..x_{k-1}),
it gives beta_k <= phi_1 + ... + phi_{k-1}. The smallest case where this lemma is used non-trivially (alpha > 0) is m = 3, k = 3.
