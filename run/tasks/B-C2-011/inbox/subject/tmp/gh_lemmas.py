# stdlib only. Sanity check (NOT a proof) of Griggs-Ho Lemmas 3.5, 3.6 and of the
# witness orbit claim, on all partitions of n <= N, sequences c_1..c_L.
import sys
def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for a in range(min(n, m), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def seq(l, L):
    c = []; x = l
    for _ in range(L):
        c.append(len(x)); x = B(x)
    return [None] + c   # 1-indexed
def patterns(c):
    # all (p,q,x) with q>=p+2, c_p=x-1, c_{p+1..q-1}=x, c_q=x+1
    L = len(c) - 1; out = []
    for p in range(1, L - 1):
        x = c[p] + 1
        q = p + 1
        if c[q] != x: continue
        while q <= L and c[q] == x: q += 1
        if q <= L and c[q] == x + 1 and q >= p + 2:
            out.append((p, q, x))
    return out
N = int(sys.argv[1]); L = int(sys.argv[2])
bad36 = bad35 = checked = 0
for n in range(1, N + 1):
    for l in partitions(n):
        c = seq(l, L); pats = patterns(c); checked += 1
        S = set(pats)
        for (p, q, x) in pats:
            if q == p + 2 and p > x: bad36 += 1
            if q >= p + 3 and p > x:
                ok = any(x2 <= x and 2 <= q2 - p2 < q - p and p - x <= p2 < q2 <= p + 1
                         for (p2, q2, x2) in pats)
                if not ok: bad35 += 1
print("partitions checked", checked, "n<=", N, "seq length", L, "violations L3.6:", bad36, "L3.5:", bad35)
# --- Lemma 3.4 (B6): pattern (m-2, m-1,...,m-1, m) at c_p..c_{p+m} => p+m <= n+1
bad34 = 0
for n in range(1, N + 1):
    for l in partitions(n):
        c = seq(l, L)
        for (p, q, x) in patterns(c):
            m = q - p            # pattern length m+1 with values x-1=m-2, x=m-1, x+1=m
            if x == m - 1 and p + m > n + 1: bad34 += 1
# --- Lemma 3.3(2) (B5): n=T_k, t=d_B>=k+1 => (i) or (ii)
bad33 = 0; cnt33 = 0
for k in range(1, 10):
    n = k*(k+1)//2
    if n > N: break
    delta = tuple(range(k, 0, -1))
    for l in partitions(n):
        t = 0; x = l
        while x != delta: x = B(x); t += 1
        if t < k + 1: continue
        cnt33 += 1
        c = seq(l, t + 3)
        pats = patterns(c)
        ok = any(xx == k and t - k <= p and q <= t - 1 for (p, q, xx) in pats) or \
             any(xx == k - 1 and t - k + 1 <= p and q <= t + 1 for (p, q, xx) in pats)
        if not ok: bad33 += 1
print("L3.4 violations:", bad34, " L3.3(2): cases", cnt33, "violations", bad33)
