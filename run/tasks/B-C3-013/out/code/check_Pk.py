#!/usr/bin/env python3
"""Exact check (stdlib, integers) that d_B(P_k) = 2k+1 for k in [KMIN,KMAX],
P_k = (k,k-1,k-1,k-3,k-4,...,3,1), a partition of T_k - 1.
Definitional test: x = B^{2k+1}(P_k) satisfies B^L(x) = x for its period L (found by
iteration, L <= k+1 enforced), and y = B^{2k}(P_k) is not on that cycle, hence not cyclic
(a cyclic y would lie on the cycle through B(y) = x)."""
import sys
from check_Ek import B, Pk
def main():
    KMIN = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    ok = True
    for k in range(KMIN, KMAX + 1):
        p = Pk(k)
        assert sum(p) == k*(k+1)//2 - 1 and all(p[i] >= p[i+1] for i in range(len(p)-1))
        orb = [p]
        for _ in range(2 * k + 1): orb.append(B(orb[-1]))
        x = orb[2 * k + 1]; y = orb[2 * k]
        cyc = [x]; z = B(x)
        while z != x and len(cyc) <= k + 1:
            cyc.append(z); z = B(z)
        good = (z == x) and (y not in cyc)
        ok &= good
        if not good: print("FAIL k=", k)
    print(f"d_B(P_k)=2k+1 for all k in [{KMIN},{KMAX}]:", ok)
if __name__ == "__main__": main()
