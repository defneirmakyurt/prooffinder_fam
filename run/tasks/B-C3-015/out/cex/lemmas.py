"""Exact stdlib checks of the intermediate lemmas of B-C3-007 on every partition of every n in [1, NMAX].
c_{i+1} = #parts of B^i(lambda), rows computed up to R = d_B + 4k + 5 (k = rank of n) where no new pattern can
start (in the cycle c takes only values k-1,k for non-triangular n and k for triangular n).
Checks: L1.1 pile bijection; L2.1 (p>=x+1 => L>=3 and a descendant pattern exists in the stated window);
C2.2 (p <= (L-1)x); L3.1 (pattern (k'-1;p,k'), k'>=3 => p+k' <= n+1, '=' only for (1^n));
L4.2 (rank k, 1<=r<=k-1, tau>=k+1 => case (i) or (ii)); 5.1 moreover (tau-1 = k^2-2k-1 => (i), or k=4 and (ii) with L=k,p=tau-k+1).
Also 6.2 for random (H,pi) satisfying (S), k=3..14, and lambda*_k orbit for k=3..40 with cyclicity by definition."""
import sys, random
def T(k): return k*(k+1)//2
def rank(n):
    k = 1
    while T(k) < n: k += 1
    return k
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for a in range(min(n, m), 0, -1):
        for r in parts(n-a, a): yield (a,)+r
def B(l): return tuple(sorted([x-1 for x in l if x > 1] + [len(l)], reverse=True))
def dB_def(l):
    seen = {}; x = l; i = 0
    while x not in seen:
        seen[x] = i; x = B(x); i += 1
    return seen[x]  # index of first element of the cycle = entry time
def patterns(c, R):
    # c is 1-indexed list c[1..R]; pattern (x;p,L): c_p=x-1, c_{p+1..p+L-1}=x, c_{p+L}=x+1, x>=2, L>=2
    out = []
    for p in range(1, R):
        x = c[p]+1
        if x < 2: continue
        q = p+1
        while q <= R and c[q] == x: q += 1
        if q <= R and q >= p+2 and c[q] == x+1: out.append((x, p, q-p))
    return out
NMAX = int(sys.argv[1])
bad = []; npat = 0; nlam = 0
for n in range(1, NMAX+1):
    k = rank(n); r = n - T(k-1)
    for lam in parts(n):
        nlam += 1
        d = dB_def(lam)
        R = d + 4*k + 5
        seq = [lam]
        for _ in range(R+1): seq.append(B(seq[-1]))
        c = [None] + [len(seq[i-1]) for i in range(1, R+2)]  # c[i] = #parts of lambda^(i-1)
        # L1.1: piles; original pile m alive rows 1..lam_m; born pile j alive rows j+1..j+c_j
        ends = {('o', m): lam[m] for m in range(len(lam))}
        for j in range(1, R+1): ends[('b', j)] = j + c[j]
        start = {('o', m): 1 for m in range(len(lam))}
        for j in range(1, R+1): start[('b', j)] = j+1
        for i in range(0, R):
            Rrow = [P for P in ends if start[P] <= i+1 <= ends[P]]
            if sorted((ends[P]-i for P in Rrow), reverse=True) != list(seq[i]):
                bad.append(('L1.1', lam, i)); break
        pats = patterns(c, R+1)
        pset = set(pats); npat += len(pats)
        for (x, p, L) in pats:
            if p > (L-1)*x: bad.append(('C2.2', lam, (x, p, L)))
            if p >= x+1:
                if L < 3: bad.append(('L2.1 L>=3', lam, (x, p, L)))
                if not any(2 <= y <= x and p-x <= pp <= p-2 and 2 <= LL <= L-1 for (y, pp, LL) in pats):
                    bad.append(('L2.1 descendant', lam, (x, p, L)))
            kk = x+1
            if kk >= 3 and L == kk:
                if p+kk > n+1 or (p+kk == n+1 and lam != (1,)*n): bad.append(('L3.1', lam, (x, p, L)))
        if 1 <= r <= k-1 and k >= 3:
            # tau
            cyc_idx = d
            tau = None
            for i in range(1, R+1):
                if i-1 >= d and c[i] == k-1 and c[i+1] == k: tau = i; break
            if tau is None: bad.append(('tau missing', lam)); continue
            if d > tau-1: bad.append(('4.1', lam))
            if tau >= k+1:
                ci = any(x == k and tau-k <= p and p+L <= tau-1 for (x, p, L) in pats)
                cii = any(x == k-1 and tau-k+1 <= p and p+L <= tau+1 for (x, p, L) in pats)
                if not (ci or cii): bad.append(('4.2', lam, tau))
                if k >= 4 and tau-1 == k*k-2*k-1:
                    ok5 = ci or (k == 4 and any(x == k-1 and L == k and p == tau-k+1 for (x, p, L) in pats))
                    if not ok5: bad.append(('5.1 moreover', lam))
            if k >= 4 and tau-1 > k*k-2*k-1: bad.append(('5.1', lam, tau))
print(f"lemma checks n=1..{NMAX}: partitions={nlam} patterns={npat} failures={len(bad)}")
for b in bad[:20]: print(b)
# 6.2 random tests
def ell(H, pi, k):
    return [max(k-i, 0) + (1 if (i <= k and i not in H) else 0) + (1 if pi == i else 0) for i in range(1, k+2)]
def Lam(H, pi, k): return tuple(v for v in ell(H, pi, k) if v > 0)
def S(H, pi, k): return not ((pi <= k and pi in H) or (pi >= 2 and (pi-1) in H))
def Hp(H, k): return frozenset([h+1 for h in H if h < k] + ([1] if k in H else []))
random.seed(12345); nt = 0; f62 = 0
for k in range(3, 15):
    for _ in range(3000):
        H = frozenset(h for h in range(1, k+1) if random.random() < random.random())
        pi = random.randint(1, k+1)
        if not S(H, pi, k): continue
        l = ell(H, pi, k)
        if any(l[i] < l[i+1] for i in range(k)): f62 += 1; continue
        nt += 1
        lam = Lam(H, pi, k); b = B(lam)
        if pi == 1 and k in H:
            if b != Lam(Hp(H, k) - {1}, None, k): f62 += 1
        else:
            pp = pi+1 if pi <= k else 1
            if b != Lam(Hp(H, k), pp, k) or not S(Hp(H, k), pp, k): f62 += 1
print(f"6.1/6.2 random tests k=3..14: tested={nt} failures={f62}")
# witness orbit, cyclicity by definition
fw = 0
for k in range(3, 41):
    ls = tuple([k-1, k-2] + list(range(k-2, 0, -1)) + [1])
    nu = tuple([k+1] + list(range(k-1, 2, -1)) + [1])
    assert sum(ls) == T(k)-1
    d = dB_def(ls)
    x = ls
    for _ in range(k*k-2*k-2): x = B(x)
    if d != k*k-2*k-1 or x != nu: fw += 1; print('witness fail', k, d)
print(f"witness lambda*_k, k=3..40: d_B=k^2-2k-1 and B^(k^2-2k-2)=nu_k: failures={fw}")
