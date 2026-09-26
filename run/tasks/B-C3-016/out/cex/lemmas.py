"""Referee B-C3-016: exact checks of the proof's intermediate claims (stdlib only).
L1 (Lemma 2.1): every pattern (x;p,L) with p>=x+1 has L>=3 and a pattern (y;p',L') with 2<=y<=x, p-x<=p'<=p-2, 2<=L'<=L-1.
L2 (Cor 2.2 with X=x): every pattern (x;p,L) has p <= (L-1)x.
L3 (Lemma 3.1): every pattern (x;p,x+1), x>=2, has p+x+1 <= n+1, equality only for (1^n).
  Checked on the c-sequence c_1..c_N (c_i = #parts of B^{i-1}(lam)) with N = d_B + 2k + 6, for ALL partitions of every n in [1, NMAX].
L4 (Lemma 6.2): for 3<=k<=KL, all (H,pi) with (S): B(Lambda(H,pi)) equals the claimed partition.
L5 (Prop 6.4): for 3<=k<=KS, d_B(lambda*_k) (cycle-entry time, computed from the orbit alone, no Cell-1 list) = k^2-2k-1
    and B^{k^2-2k-2}(lambda*_k) = nu_k.
"""
import sys
from itertools import combinations
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n - a, a): yield (a,) + r
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def T(k): return k*(k+1)//2
def rank(n):
    k = 1
    while T(k) < n: k += 1
    return k
def entry(l):
    seen = {}; x = l; i = 0; orbit = []
    while x not in seen:
        seen[x] = i; orbit.append(x); x = B(x); i += 1
    return seen[x], orbit   # cycle-entry index = index of first element that recurs
def patterns(c):  # c is dict/list 1-indexed
    N = len(c) - 1; out = []
    for p in range(1, N):
        x = c[p] + 1
        if x < 2: continue
        q = p + 1
        if q > N or c[q] != x: continue
        while q <= N and c[q] == x: q += 1
        if q <= N and c[q] == x + 1: out.append((x, p, q - p))
    return out
NMAX = int(sys.argv[1]); KL = int(sys.argv[2]); KS = int(sys.argv[3])
bad = []; npat = 0; nlam = 0
for n in range(1, NMAX + 1):
    k = rank(n)
    for lam in parts(n):
        nlam += 1
        d, orb = entry(lam)
        N = d + 2*k + 6
        seq = [lam]
        while len(seq) < N: seq.append(B(seq[-1]))
        c = [None] + [len(s) for s in seq]
        pats = patterns(c); pset = set(pats); npat += len(pats)
        for (x, p, L) in pats:
            if p > (L - 1)*x: bad.append(("L2", lam, x, p, L))
            if p >= x + 1:
                if L < 3: bad.append(("L1-L", lam, x, p, L))
                if not any(2 <= y <= x and p - x <= q <= p - 2 and 2 <= M <= L - 1 for (y, q, M) in pats):
                    bad.append(("L1", lam, x, p, L))
            if L == x + 1:
                if p + x + 1 > n + 1: bad.append(("L3", lam, x, p, L))
                if p + x + 1 == n + 1 and lam != tuple([1]*n): bad.append(("L3eq", lam, x, p, L))
print(f"L1-L3: all partitions of n=1..{NMAX}: {nlam} partitions, {npat} patterns, violations={len(bad)}", bad[:5])
# L4
bad4 = 0; tot4 = 0
for k in range(3, KL + 1):
    for sz in range(0, k + 1):
        for H in combinations(range(1, k + 1), sz):
            H = set(H)
            for pi in range(1, k + 2):
                if pi <= k and pi in H: continue
                if pi >= 2 and (pi - 1) in H: continue
                ell = [max(k - i, 0) + (1 if (i <= k and i not in H) else 0) + (1 if pi == i else 0) for i in range(1, k + 2)]
                Lam = tuple(x for x in ell if x > 0)
                assert list(Lam) == sorted(Lam, reverse=True)
                H1 = {h + 1 for h in H if h < k} | ({1} if k in H else set())
                pip = pi + 1 if pi <= k else 1
                if pi == 1 and k in H:
                    H2 = H1 - {1}
                    tgt = tuple(x for x in [max(k - i, 0) + (1 if (i <= k and i not in H2) else 0) for i in range(1, k + 2)] if x > 0)
                else:
                    ell2 = [max(k - i, 0) + (1 if (i <= k and i not in H1) else 0) + (1 if pip == i else 0) for i in range(1, k + 2)]
                    tgt = tuple(x for x in ell2 if x > 0)
                    # (S) preserved
                    if (pip <= k and pip in H1) or (pip >= 2 and (pip - 1) in H1): bad4 += 1
                tot4 += 1
                if B(Lam) != tgt: bad4 += 1
print(f"L4: k=3..{KL}: {tot4} configurations (H,pi) with (S), violations={bad4}")
# L5
bad5 = []
for k in range(3, KS + 1):
    lstar = tuple([k - 1, k - 2] + list(range(k - 2, 0, -1)) + [1])
    assert sum(lstar) == T(k) - 1
    d, orb = entry(lstar)
    nu = tuple([k + 1] + list(range(k - 1, 2, -1)) + [1])
    m = k*k - 2*k - 2
    ok = (d == k*k - 2*k - 1) and (k == 3 or orb[m] == nu)
    if not ok: bad5.append((k, d))
print(f"L5: k=3..{KS}: lambda*_k cycle-entry = k^2-2k-1 and B^(k^2-2k-2)=nu_k; failures={bad5}")
