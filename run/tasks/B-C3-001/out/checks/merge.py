# Extremizers of T_k - 1: counts, contraction profile |{B^j(ext)}|, merge point mu_k vs guessed formula,
# and whether ext == {lam : B^L(lam) = mu_k}. Exact, stdlib only.
import sys, time
from small_cases import analyse, B
t0 = time.time()
K = int(sys.argv[1]) if len(sys.argv) > 1 else 9
for k in range(5, K+1):
    n = k*(k+1)//2 - 1
    D, ext, cyc, d = analyse(n)
    prof = []; imgs = set(ext); j = 0
    while len(imgs) > 1:
        prof.append(len(imgs)); imgs = {B(x) for x in imgs}; j += 1
    mu = next(iter(imgs)); L = j
    guess = tuple([k, k-1, k-1] + list(range(k-3, 2, -1)) + [1]) if k >= 6 else None
    # all lam with B^L(lam) = mu
    pre = []
    for lam in d:
        x = lam
        for _ in range(L): x = B(x)
        if x == mu: pre.append(lam)
    GH = tuple([k-1, k-2] + [k-i+1 for i in range(3, k+1)] + [1])
    print(f"k={k} n={n} D={D} #ext={len(ext)} merge after L={L} at mu={mu} d(mu)={d[mu]} guess_match={mu==guess} "
          f"#B^-L(mu)={len(pre)} equal_to_ext={set(pre)==set(ext)} GH_in_ext={GH in set(ext)}")
    print("   contraction profile |B^j(ext)|, j=0..L-1:", prof)
    # orbit of mu down to cycle: parts counts
    x = mu; orb = []
    for _ in range(d[mu] + 1): orb.append(x); x = B(x)
    print("   orbit of mu to cycle entry:", orb[:4], "...", orb[-2:])
    sys.stdout.flush()
print("runtime %.2fs" % (time.time()-t0))
