#!/usr/bin/env python3
"""Independent check of the lower-bound witness (stdlib only, exact integers).
For k in [3, K]:
  * builds lambda*_k from the proof's row formula (rows: k-1, k-2, then k-i for 2<=i<=k-1, then 1),
    checks it is weakly decreasing, positive, and sums to T_k - 1;
  * computes d_B(lambda*_k) WITHOUT Cell 1: iterate B, record first occurrence; first repeat x_j = x_i
    gives tail length i = d_B (cycle-entry time);
  * checks d_B == k^2-2k-1;
  * checks, for every t <= F, that B^t(lambda*) == Lambda({t, t+1} mod k, (k+t) mod (k+1)) for t < F
    (proof's 4.1/4.2 orbit), has Phi = 1, and is non-cyclic by the Cell-1 test; and B^F is Cell-1 cyclic.
"""
import sys
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
T = lambda k: k*(k+1)//2
def energy(l):
    return sum(i*p + p*(p-1)//2 for i, p in enumerate(l))
def emin(n, k):
    return sum(n - T(d) for d in range(1, k))  # nu_d = n - T_d for d<=k-1, 0 beyond
def Lam(H, c, k):
    rows = []
    for i in range(k+1):
        L = (k-1-i if i <= k-2 else 0) + (1 if (i <= k-1 and i not in H) else 0) + (1 if i == c else 0)
        rows.append(L)
    return tuple(x for x in rows if x > 0)
def cell1_cyclic(l, k):
    # n = T_{k-1}+r ; cyclic iff l = (k-1+e1, ..., 1+e_{k-1}, e_k), e in {0,1}^k
    rows = list(l) + [0]*(k+1-len(l))
    if len(rows) > k: 
        if any(rows[k:]): return False
    return all(rows[i] - (k-1-i) in (0, 1) for i in range(k))
def main(K):
    ok = True
    for k in range(3, K+1):
        n = T(k) - 1; F = k*k - 2*k - 1
        lam = tuple([k-1, k-2] + [k-i for i in range(2, k)] + [1])
        assert all(lam[i] >= lam[i+1] > 0 for i in range(len(lam)-1)) and sum(lam) == n, k
        assert lam == Lam({0, 1}, k, k), (k, lam)
        seen = {}; x = lam; j = 0
        while x not in seen:
            seen[x] = j; x = B(x); j += 1
        d = seen[x]
        if d != F: print("FAIL d", k, d, F); ok = False
        x = lam
        for t in range(F+1):
            if t < F:
                exp = Lam({t % k, (t+1) % k}, (k+t) % (k+1), k)
                if x != exp: print("FAIL orbit", k, t); ok = False
                if energy(x) - emin(n, k) != 1: print("FAIL Phi", k, t); ok = False
                if cell1_cyclic(x, k): print("FAIL cyclic early", k, t); ok = False
            else:
                if not cell1_cyclic(x, k): print("FAIL not cyclic at F", k); ok = False
                if energy(x) - emin(n, k) != 0: print("FAIL Phi0", k); ok = False
            x = B(x)
        if k <= 6 or k % 25 == 0: print(f"k={k} lambda*={lam} d_B={d} F={F}")
    print("ALL OK" if ok else "FAILURES", f"k=3..{K}")
main(int(sys.argv[1]))
