# Plan: B-C3-013 (FRESH, angle: witness-family), target B-C3(c) under (H)

Reading adopted: "explicit description" = a rule producing every member of E_k directly.
Witness-family angle: find one explicit partition P_k through which the orbit of every
maximiser passes (a "trunk point"), prove d_B(P_k) exactly, and describe E_k as its
ancestors at a fixed depth; then try to make the ancestor set explicit.

Notation: n = T_k - 1, M_k = k^2-2k-1, j_k = k^2-4k-2 = M_k-(2k+1),
P_k = (k,k-1,k-1,k-3,k-4,...,3,1) (k>=6).

| rung | statement | uses | status |
|---|---|---|---|
| R1 | Conjugate form: (B lambda)'_j = lambda'_{j+1} + [j <= l(lambda)] | defs | PROVED (proof.md Step 2) |
| R2 | Preimage rule: B^{-1}(nu) listed by descents m of nu' with m >= nu'_1-1; nu has no preimage iff nu_1 <= l(nu)-2 | R1 | PROVED (Step 3) + CHECKED k=4..10 on all partitions |
| R3 | d_B(B lambda) = d_B(lambda)-1 for non-cyclic lambda; B^j(lambda)=nu non-cyclic => d_B(lambda)=j+d_B(nu) | defs | PROVED (Step 4) |
| R4 | Y_1=(k,...,2) lies on a k-cycle Y_1->Y_k->...->Y_2->Y_1 | defs | PROVED (Step 5) |
| R5 | d_B(P_k) = 2k+1 for every k>=6 (explicit orbit, 8 families) | R3,R4 | PROVED (Step 6); CHECKED k=6..200 |
| R6 | Direction 2 (no hypothesis): every lambda with B^{j_k}(lambda)=P_k has d_B = M_k | R3,R5 | PROVED (Step 7) |
| R7 | Under (H): every maximiser is a Garden of Eden, and E_k = {lambda : B^{M_k-1}(lambda) not cyclic} | R2,R3,(H) | PROVED (Step 8) |
| R8 | k=4..10: explicit lists of E_k; counts 1,6,34,175,831,3911,18163; E_k = A_k:= B^{-j_k}(P_k) for 6<=k<=10 (unconditional there) | code | CHECKED (Step 9) |
| R9 | Merge claim for all k>=11: under (H), every lambda in E_k has B^{j_k}(lambda)=P_k (Direction 3) | (H) | GAP (open; CHECKED only k<=10 exhaustively) |
| R10 | Closed-form listing of A_k for general k (not "preimages of P_k") | R2 | GAP (only a necessary box condition, CHECKED k<=10; box is strictly larger for k=6,8,9,10) |
| R11 | Target 1-3 for all k>=4 | R6,R8,R9,R10 | GAP (holds for k=4..10 by R8; general k open) |

Stopping: R9/R10 attempted (box rule refuted as exact rule: 1,3,24,167 extra members for k=6,8,9,10);
time box reached. Reported PARTIAL.
