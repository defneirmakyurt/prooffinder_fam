#!/usr/bin/env python3
"""Exhaustive, exact (integer) check for k in [KMIN, KMAX] (default 4..10), n = T_k - 1.
Stdlib only.  For every partition of n it computes d_B by functional-graph analysis
(cyclic = lies on a cycle of the map B; purely definitional, no theorem used).
Checks, for each k:
  (a) max d_B = M_k = k^2-2k-1 and |E_k| (compare 1,6,34,175,831,3911,18163);
  (b) every member of E_k has conjugate inside the box lo_i <= mu_i <= hi_i,
      lo_i = max(0,k+3-2i), hi_i = max(0,2k-1-2i)   (necessary condition only);
  (c) every member of E_k satisfies lambda_1 <= len(lambda)-2 (no B-preimage);
  (d) for k >= 6: B^{M_k-2k-1}(E_k) = {P_k}, P_k = (k,k-1,k-1,k-3,k-4,...,3,1),
      and d_B(P_k) = 2k+1;
  (e) E_k equals the set of depth-(M_k-2k-1) B-ancestors of P_k, generated
      independently by the backward (conjugate) preimage rule of proof.md Step 3.
"""
import sys

def parts(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n - a, a):
            yield (a,) + r

def B(l):
    s = len(l)
    q = [x - 1 for x in l if x > 1] + [s]
    return tuple(sorted(q, reverse=True))

def conj(l):
    return tuple(sum(1 for x in l if x >= j) for j in range(1, (l[0] if l else 0) + 1))

def dvals(n):
    P = list(parts(n)); nxt = {p: B(p) for p in P}
    cyc = set()
    for p in P:
        seen = []; x = p; vis = {}
        while x not in vis and x not in cyc:
            vis[x] = len(seen); seen.append(x); x = nxt[x]
        if x in vis:
            for y in seen[vis[x]:]: cyc.add(y)
    d = {p: 0 for p in cyc}
    for p in P:
        st = []; q = p
        while q not in d:
            st.append(q); q = nxt[q]
        v = d[q]
        while st:
            v += 1; d[st.pop()] = v
    return d

def Pk(k):
    return tuple([k, k - 1, k - 1] + list(range(k - 3, 2, -1)) + [1])

def preimages(nu):
    """All lambda with B(lambda) = nu, via the conjugate rule (proof.md Step 3):
    for each m with m >= nu'_1 - 1, 1 <= m <= len(nu'), nu'_m > nu'_{m+1}:
    lambda' = (m, nu'_1-1, ..., nu'_m-1, nu'_{m+1}, ...)."""
    c = list(conj(nu)); L = len(c); out = []
    for m in range(1, L + 1):
        nxt = c[m] if m < L else 0
        if c[m - 1] > nxt and m >= c[0] - 1:
            mu = [m] + [x - 1 for x in c[:m]] + c[m:]
            mu = [x for x in mu if x > 0]
            out.append(conj(tuple(mu)))
    return out

def ancestors(nu, depth):
    S = {nu}
    for _ in range(depth):
        S = {l for x in S for l in preimages(x)}
    return S

def main():
    KMIN = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    ok = True
    for k in range(KMIN, KMAX + 1):
        n = k * (k + 1) // 2 - 1; M = k * k - 2 * k - 1
        d = dvals(n)
        mx = max(d.values()); E = {p for p in d if d[p] == mx}
        # sanity of preimage rule on all partitions
        pre = {}
        for p in d: pre.setdefault(B(p), set()).add(p)
        pre_ok = all(set(preimages(p)) == pre.get(p, set()) for p in d)
        L = k - 1
        lo = [max(0, k + 3 - 2 * i) for i in range(1, L + 1)]
        hi = [max(0, 2 * k - 1 - 2 * i) for i in range(1, L + 1)]
        def inbox(p):
            c = list(conj(p));
            if len(c) > L: return False
            c += [0] * (L - len(c))
            return all(lo[i] <= c[i] <= hi[i] for i in range(L))
        box_ok = all(inbox(p) for p in E)
        goe_ok = all(p[0] <= len(p) - 2 for p in E)
        line = f"k={k} n={n} maxd={mx} M_k={M} |E_k|={len(E)} preimage_rule_ok={pre_ok} box_ok={box_ok} GoE_ok={goe_ok}"
        ok &= (mx == M) and pre_ok and box_ok and goe_ok
        if k >= 6:
            j = M - 2 * k - 1; P = Pk(k)
            S = set(E)
            for _ in range(j): S = {B(p) for p in S}
            anc = ancestors(P, j)
            merge_ok = (S == {P}) and d[P] == 2 * k + 1
            anc_ok = (anc == E)
            line += f" merge_to_Pk_ok={merge_ok} ancestors_eq_E={anc_ok}"
            ok &= merge_ok and anc_ok
        print(line, flush=True)
    print("ALL OK" if ok else "FAILURE")

if __name__ == "__main__":
    main()
