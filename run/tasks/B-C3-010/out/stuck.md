# Stuck point (B-C3-010)

Exact failure: proof.md Step 6, claim (R6): for every mu in D_1 \ {nu_k} = {mu^(v) : 3<=v<=k-1} u {omega_k},
there is no lambda |- T_k-1 with B^{M-1}(lambda) = mu.  By Prop 4.1 (no hypothesis) this is equivalent to target item 3
(E_k = R_k).

Attempt 1 (use (H) directly): (H) only gives B^{-M}(mu) empty for every mu in D_1 (proof.md 5.3), i.e. tree height
<= M-1. (R6) needs height <= M-2 for the k-2 trees other than that of nu_k. No construction was found turning a depth-(M-1)
ancestor of mu != nu_k into a partition of T_k-1 with d_B > M, so (H) gives nothing more.

Attempt 2 (subject's rotating-frame/particle machinery on C_k = {delta_{k-1} <= lambda <= delta_{k+1}}): inside C_k the
tight case of the subject's counting lemma forces the last particle to start at Q=k with hole labels {0,1} surviving, which
is the nu_k route. But members of E_k are not in C_k (k=5: cells on diagonal k+2; k=6: on diagonal k+3) and the time to
enter C_k is up to 14 for k=8; bounding it is exactly the missing part of the general upper bound (H) itself, which the
target does not supply as a structural statement.

What would be needed: a structural (not merely numerical) form of the upper bound: e.g. an entry-time bound for C_k
together with the remaining-time bound, sharp enough that total time M forces entering the nu_k route.  Data
(code/heights_out.txt, k<=9): the second-highest tree over D_1 has height M-2-k, so a proof with slack k+1 exists
numerically.

Target item 1 (closed form): no rule found. The orbit of a member of E_k can join the orbit of lambda*_k as late as time 30
(k=8), so bounded-depth tail modifications of lambda*_k (like alpha_k, beta_k) do not exhaust E_k.
