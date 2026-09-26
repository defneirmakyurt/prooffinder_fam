#!/usr/bin/env python3
"""Independent exhaustive check (stdlib only, exact). For every non-triangular n with rank 2..K:
  - enumerate all partitions, compute d_B by memoised orbit walking (cycle entry time, independent of Cell 1);
  - check the brute-force cyclic set equals the Cell-1 set (S5) and equals {Phi = 0} (proof 2.5);
  - check proof 1.4 on every partition: E(B l) <= E(l), equality iff l_1 <= s+1;
  - report D_B(n); check D_B(n) <= k^2-2k-1 for k >= 4 (S2 (a), finite range);
  - at n = T_k-1: report D_B, #maximisers, lambda*_k's d_B, Phi=1 maximisers.
"""
import sys
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for p in range(min(n, m), 0, -1):
        for r in parts(n-p, p): yield (p,) + r
def B(l):
    s = len(l); return tuple(sorted([x-1 for x in l if x > 1] + [s], reverse=True))
T = lambda k: k*(k+1)//2
def E(l): return sum(i*p + p*(p-1)//2 for i, p in enumerate(l))
def cell1(l, k):
    rows = list(l) + [0]*(k+1-len(l))
    if any(rows[k:]): return False
    return all(rows[i]-(k-1-i) in (0, 1) for i in range(k))
def main(K):
    ok = True
    for k in range(2, K+1):
        for n in range(T(k-1)+1, T(k)):
            P = list(parts(n)); nxt = {p: B(p) for p in P}
            # cyclic set by brute force: p cyclic iff walking from p returns to p within |P| steps
            cyc = set()
            for p in P:
                if p in cyc: continue
                seen = {p: 0}; x = nxt[p]; i = 1
                while x not in seen: seen[x] = i; x = nxt[x]; i += 1
                # x is first repeat -> x lies on a cycle
                y = x
                while True:
                    cyc.add(y); y = nxt[y]
                    if y == x: break
            d = {}
            for p in P:
                path = []; x = p
                while x not in d and x not in cyc: path.append(x); x = nxt[x]
                v = 0 if x in cyc else d[x]
                if x in cyc: d[x] = 0
                for y in reversed(path): v += 1; d[y] = v
            Emin = sum(n - T(j) for j in range(1, k))
            for p in P:
                c1 = cell1(p, k); phi0 = (E(p) == Emin)
                if (p in cyc) != c1 or c1 != phi0: print("FAIL cyclic", n, p); ok = False
                if E(p) < Emin: print("FAIL Emin", n, p); ok = False
                eq = E(nxt[p]) == E(p)
                if E(nxt[p]) > E(p) or eq != (p[0] <= len(p)+1): print("FAIL energy", n, p); ok = False
            D = max(d.values()); F = k*k-2*k-1
            if k >= 4 and D > F: print("FAIL (a)", k, n, D); ok = False
            if n == T(k)-1:
                mx = [p for p in P if d[p] == D]
                lam = tuple([k-1, k-2] + [k-i for i in range(2, k)] + [1])
                phi1 = [p for p in mx if E(p) == Emin+1]
                print(f"k={k} n={n} D_B={D} F={F} #max={len(mx)} d(lambda*)={d.get(lam)} Phi1-maximisers={phi1 if len(phi1)<3 else len(phi1)}"
                      + (f" maximisers={mx}" if k <= 4 else ""))
        print(f"k={k}: rank-{k} non-triangular n in ({T(k-1)},{T(k)}) done")
    print("ALL OK" if ok else "FAILURES", f"ranks 2..{K}")
main(int(sys.argv[1]))
