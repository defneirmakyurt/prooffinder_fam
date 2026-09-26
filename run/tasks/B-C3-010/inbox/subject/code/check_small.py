#!/usr/bin/env python3
"""Exhaustive exact check (stdlib only) for Bulgarian solitaire, ranks k = 2..K.
For every n with T_{k-1} < n < T_k it computes D_B(n) = max_lambda d_B(lambda) by building the
full functional graph of B on partitions of n (cyclic = on a cycle, found by in-degree peeling).
Checks: (1) D_B(n) <= k^2-2k-1 for k >= 4; (2) D_B(T_k-1) = k^2-2k-1 for k >= 4, and prints
D_B(T_k-1) for k = 2, 3; (3) every extremal lambda of T_k-1 satisfies B^{D-1}(lambda) = nu_k,
nu_k = (k+1, k-1, k-2, ..., 3, 1); (4) d_B(lambda*_k) = k^2-2k-1 for
lambda*_k = (k-1, k-2, k-2, k-3, ..., 2, 1, 1).  Usage: python3 check_small.py K
"""
import sys

def partitions(n):
    # iterative generation of partitions of n as weakly decreasing tuples
    out = []
    def rec(rem, mx, pre):
        if rem == 0:
            out.append(tuple(pre)); return
        for f in range(min(rem, mx), 0, -1):
            pre.append(f); rec(rem - f, f, pre); pre.pop()
    rec(n, n, [])
    return out

def B(l):
    s = len(l)
    new = [x - 1 for x in l if x > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def depths(n):
    P = partitions(n)
    nxt = {p: B(p) for p in P}
    indeg = dict.fromkeys(P, 0)
    for p in P:
        indeg[nxt[p]] += 1
    stack = [p for p in P if indeg[p] == 0]
    order = []
    while stack:
        p = stack.pop(); order.append(p)
        q = nxt[p]; indeg[q] -= 1
        if indeg[q] == 0:
            stack.append(q)
    removed = set(order)
    d = {p: 0 for p in P if p not in removed}   # cyclic partitions
    for p in reversed(order):                    # parents after children
        d[p] = d[nxt[p]] + 1
    return d

def T(k): return k * (k + 1) // 2

def lam_star(k):
    return tuple([k - 1, k - 2] + [k - i + 1 for i in range(3, k + 1)] + [1])

def nu(k):
    return tuple([k + 1] + list(range(k - 1, 2, -1)) + [1])

def main(K):
    ok = True
    for k in range(2, K + 1):
        for n in range(T(k - 1) + 1, T(k)):
            d = depths(n)
            D = max(d.values())
            line = f"k={k} n={n} D_B(n)={D}"
            if k >= 4:
                good = D <= k * k - 2 * k - 1
                ok &= good
                line += f" bound={k*k-2*k-1} {'OK' if good else 'VIOLATION'}"
            if n == T(k) - 1:
                ext = [p for p in d if d[p] == D]
                line += f"  [n=T_k-1] #extremal={len(ext)}"
                if k >= 4:
                    eq = (D == k * k - 2 * k - 1); ok &= eq
                    ls = lam_star(k); assert sum(ls) == n
                    st = (d[ls] == D); ok &= st
                    allnu = True
                    for p in ext:
                        x = p
                        for _ in range(D - 1): x = B(x)
                        allnu &= (x == nu(k))
                    ok &= allnu
                    line += f" D==k^2-2k-1:{eq} d(lambda*)==D:{st} all B^(D-1)=nu_k:{allnu}"
            print(line, flush=True)
    print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 9)
