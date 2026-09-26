#!/usr/bin/env python3
"""Sanity checks (stdlib only, exact integers) for proof.md of B-C3-011.  NOT part of the proof.
Usage: python3 check_c3a.py K   (checks ranks 4..K; default K=9)
Part 1 (general lemmas R3,R5,R6,R7) on every partition of every n in [1, NMAX], NMAX = T_K - 1:
  for every sandwich (c_p..c_q) = (x-1,x,..,x,x+1) in c_1..c_W: q-p != x, q-p <= x+1,
  p <= (q-p-1)*x (Descent), and if q-p = x+1 then q <= T_x + 2 (Long-pattern lemma, m = x+1).
Part 2 (non-triangular n of rank k, 4<=k<=K), every partition lambda, t = d_B(lambda):
  End lemma R9, Cycle lemma R8, the case certificate of R10/R11 exactly as in proof.md, and t <= k^2-2k-1.
"""
import sys

def partitions(n):
    out = []
    def rec(rem, mx, pre):
        if rem == 0:
            out.append(tuple(pre)); return
        for f in range(min(rem, mx), 0, -1):
            pre.append(f); rec(rem - f, f, pre); pre.pop()
    rec(n, n, [])
    return out

def B(l):
    new = [x - 1 for x in l if x > 1]
    new.append(len(l)); new.sort(reverse=True)
    return tuple(new)

def T(k): return k * (k + 1) // 2

def is_cyc_nontri(l, k):
    # B-C1 for n = T_{k-1}+r, 1<=r<=k-1: cyclic iff l = (k-1+e_1,...,1+e_{k-1},e_k)
    if len(l) > k: return False
    for i in range(k):
        li = l[i] if i < len(l) else 0
        if not (k - 1 - i <= li <= k - i): return False
    return True

def sandwiches(c, lo, hi):
    """all (p,q,x) with lo<=p<q<=hi, q>=p+2, c_p=x-1, c_{p+1..q-1}=x, c_q=x+1 (c is 1-indexed list)"""
    res = []
    for p in range(lo, hi):
        x = c[p] + 1
        q = p + 1
        while q <= hi and c[q] == x: q += 1
        if q <= hi and q >= p + 2 and c[q] == x + 1:
            res.append((p, q, x))
    return res

def orbit_c(l, W):
    c = [None]; x = l
    for _ in range(W):
        c.append(len(x)); x = B(x)
    return c

def main(K):
    bad = 0
    NMAX = T(K) - 1
    # Part 1
    cnt = 0
    for n in range(1, NMAX + 1):
        W = 3 * n + 10
        for l in partitions(n):
            c = orbit_c(l, W)
            for (p, q, x) in sandwiches(c, 1, W):
                cnt += 1
                L = q - p
                if L == x or L > x + 1 or p > (L - 1) * x: bad += 1; print("P1 FAIL", n, l, p, q, x)
                if L == x + 1 and q > T(x) + 2: bad += 1; print("P7 FAIL", n, l, p, q, x)
    print(f"Part 1: n=1..{NMAX}, {cnt} sandwich patterns checked, failures so far {bad}")
    # Part 2
    for k in range(4, K + 1):
        bound = k * k - 2 * k - 1; Dmax = 0; cases = {}
        for n in range(T(k - 1) + 1, T(k)):
            r = n - T(k - 1)
            for l in partitions(n):
                rows = [None]; x = l; t = 0
                while not is_cyc_nontri(x, k):
                    rows.append(x); x = B(x); t += 1
                for _ in range(k + 2): rows.append(x); x = B(x)
                c = [None] + [len(rw) for rw in rows[1:]]
                Dmax = max(Dmax, t)
                if t > bound: bad += 1; print("BOUND FAIL", k, n, l, t)
                if t == 0: cases['t=0'] = cases.get('t=0', 0) + 1; continue
                # cycle lemma R8
                nu = rows[t + 1]
                e = [(nu[j - 1] if j - 1 < len(nu) else 0) - (k - j) for j in range(1, k + 1)]
                assert sum(e) == r
                for i in range(1, k + 1):
                    if c[t + i] != k - 1 + e[k - i]: bad += 1; print("R8 FAIL", k, l)
                # end lemma R9
                ct = c[t]
                if ct not in (k - 2, k - 1): bad += 1; print("R9 FAIL ct", k, l, ct); continue
                if ct == k - 2:
                    # R10: pattern at p=t, q<=t+k
                    s = [pq for pq in sandwiches(c, t, t + k) if pq[0] == t and pq[2] == k - 1]
                    ok = bool(s) and (lambda L: (L <= k - 2 and t <= (L - 1) * (k - 1)) or (L == k and t + k <= T(k - 1) + 2))(s[0][1] - s[0][0])
                    cases['ct=k-2'] = cases.get('ct=k-2', 0) + 1
                    if not ok: bad += 1; print("R10 FAIL", k, l, t, c[t:t + k + 1])
                    continue
                mu = rows[t]
                if not (mu.count(k + 1) == 1 and all(v <= k - 1 for v in mu if v != k + 1) and c[t + k - 1] == k):
                    bad += 1; print("R9 FAIL mu", k, l, mu)
                if t <= k: cases['ct=k-1,t<=k'] = cases.get('ct=k-1,t<=k', 0) + 1; continue
                caseA = all(u + c[u] >= t for u in range(t - k + 1, t))
                if caseA:
                    u0 = [u for u in range(t - k + 1, t) if u + c[u] == t + k]
                    assert len(u0) == 1; u0 = u0[0]
                    if u0 == t - 1:
                        i = [u for u in range(t - k + 1, t - 1) if c[u] <= k - 1]
                        ok = bool(i)
                        if ok:
                            s = [pq for pq in sandwiches(c, i[-1], t - 1) if pq[2] == k]
                            ok = bool(s) and t <= (s[0][1] - s[0][0] - 1) * k + k - 1
                        cases['A1'] = cases.get('A1', 0) + 1
                    else:
                        b = t - u0
                        ok = (2 <= b <= k - 2) and c[t - k] <= k - 1 and c[u0 - 1] == k + b - 1
                        if ok:
                            s = [pq for pq in sandwiches(c, t - k, u0 - 1) if pq[2] == k]
                            ok = bool(s) and (s[0][1] - s[0][0]) <= k - 3 and t <= (s[0][1] - s[0][0] - 1) * k + k
                        cases['A2'] = cases.get('A2', 0) + 1
                    if not ok: bad += 1; print("R11 A FAIL", k, l, t)
                else:
                    i = max(u for u in range(t - k + 1, t - 1) if u + c[u] < t)
                    ok = c[i] <= k - 2
                    s = [pq for pq in sandwiches(c, i, t + k - 1) if pq[2] == k - 1]
                    ok = ok and bool(s)
                    if ok:
                        p, q, _ = s[0]; L = q - p
                        ok = (t - k + 1 <= p <= t - 1) and ((L <= k - 2 and t <= (L - 1) * (k - 1) + k - 1) or (L == k and t <= q - 1 <= T(k - 1) + 1))
                    cases['B'] = cases.get('B', 0) + 1
                    if not ok: bad += 1; print("R11 B FAIL", k, l, t)
        print(f"k={k}: max d_B over non-triangular n of rank k = {Dmax} (bound {bound}); case counts {cases}")
    print("ALL CHECKS PASSED" if bad == 0 else f"FAILURES: {bad}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 9)
