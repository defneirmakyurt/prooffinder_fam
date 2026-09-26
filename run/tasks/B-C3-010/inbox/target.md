# Target: B-C3(c), maximiser classification (conditional on the upper bound)

Definitions as in run/B/statement.md. Let k >= 4, n = T_k - 1, M_k = k^2 - 2k - 1.
HYPOTHESIS (H), stated explicitly and not to be proved here: d_B(lambda) <= M_k for every partition lambda of T_k - 1
(this is C3(a)/(b) upper bound, being proved separately).
Prove, under (H) and for every k >= 4 (small k listed separately if the pattern differs):
 1. An EXPLICIT description, as functions of k, of the set E_k = { lambda |- T_k - 1 : d_B(lambda) = M_k }
    (a closed list or a closed-form rule that lets one write every member down directly, not "all preimages under
    B^j of some partition" unless those preimages are then listed explicitly).
 2. Every listed partition has d_B = M_k (this direction needs no hypothesis).
 3. Under (H), no other partition has d_B = M_k.
Exhaustive data to match (from earlier computation, not a proof): |E_k| = 1, 6, 34, 175, 831, 3911, 18163 for k = 4..10.
