# stdlib only, exact integers. Tries to break the intermediate claims of the proof under review.
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
def rank(n):
    k = 1
    while k * (k + 1) // 2 < n: k += 1
    return k
def cseq(l, L):
    c = [None]; x = l
    for _ in range(L):
        c.append(len(x)); x = B(x)
    return c
def patterns(c):
    L = len(c) - 1; out = []
    for p in range(1, L - 1):
        x = c[p] + 1; q = p + 1
        if c[q] != x: continue
        while q <= L and c[q] == x: q += 1
        if q <= L and c[q] == x + 1 and q >= p + 2: out.append((p, q, x))
    return out
N = int(sys.argv[1]); SN = int(sys.argv[2]) if len(sys.argv) > 2 else N
cnt = dict(star=0, B2=0, B4=0, B5=0, B6=0, B7=0, B8=0, B9=0, parts=0)
bad = dict(star=0, B2=0, B4=0, B5=0, B6=0, B7=0, B8=0, B9=0)
for n in range(1, N + 1):
    k = rank(n); L = 2 * n + k * k + 10
    tri = (n == k * (k + 1) // 2); delta = tuple(range(k, 0, -1))
    for lam in partitions(n):
        cnt['parts'] += 1
        c = cseq(lam, L)
        e = lambda i, u: 1 if c[u] >= i - u else 0
        # (*) formula and B2 / flip form
        for t in (range(0, L - 1) if n <= SN else ()):
            v = sum(1 for a in lam if a >= t + 1) + sum(1 for u in range(1, t + 1) if c[u] >= t + 1 - u)
            cnt['star'] += 1
            if v != c[t + 1]: bad['star'] += 1
        for i in (range(1, L - 1) if n <= SN else ()):
            Li = sum(1 for a in lam if a == i) + sum(1 for u in range(1, i) if u + c[u] == i)
            cnt['B2'] += 1
            if not (c[i + 1] <= c[i] + 1 and c[i + 1] == c[i] + 1 - Li): bad['B2'] += 1
        pats = patterns(c)
        for (p, q, x) in pats:
            # B6: pattern (m-2, m-1..m-1, m) at p..p+m  => p+m <= n+1
            m = q - p
            if x == m - 1:
                cnt['B6'] += 1
                if p + m > n + 1: bad['B6'] += 1
            # B8
            if q == p + 2:
                cnt['B8'] += 1
                if p > x: bad['B8'] += 1
            # B7: the proof's explicit construction
            if q >= p + 3 and p >= x + 1:
                cnt['B7'] += 1
                ok = True
                zs = [u for u in range(p - x, p - 1) if e(p, u) == 0]
                if not zs: ok = False
                else:
                    pp = max(zs); y = p - pp
                    if not (2 <= y <= x and c[pp] == y - 1 and c[pp + 1] == y): ok = False
                    else:
                        qq = pp + 1
                        while c[qq] == y: qq += 1
                        if not (c[qq] == y + 1 and 2 <= qq - pp < q - p and p - x <= pp and qq <= p + 1): ok = False
                if not ok: bad['B7'] += 1
        if tri:
            x = lam; t = 0
            while x != delta: x = B(x); t += 1
            if t >= 1:
                cnt['B4'] += 1
                if not (c[t] == k - 1 and all(c[u] == k for u in range(t + 1, L + 1))): bad['B4'] += 1
            if t >= k + 1:
                cnt['B5'] += 1
                i_ = [pq for pq in pats if pq[2] == k and t - k <= pq[0] and pq[1] <= t - 1]
                ii = [pq for pq in pats if pq[2] == k - 1 and t - k + 1 <= pq[0] and pq[1] <= t + 1]
                if not (i_ or ii): bad['B5'] += 1
                # B9 chain as written: start pattern, iterate B7 construction, check bound
                if k >= 3:
                    cnt['B9'] += 1
                    iiq = [pq for pq in ii if pq[1] - pq[0] == k]
                    if iiq:
                        p0 = iiq[0][0]
                        if not (p0 == t - k + 1 and p0 + k <= n + 1 and t <= n): bad['B9'] += 1
                    else:
                        P = (i_ + ii)[0]; p0 = P[0]; pc, qc, xc = P; steps = 0
                        if not (qc - pc <= k - 1 and pc >= t - k): bad['B9'] += 1
                        while qc - pc >= 3 and pc > xc:
                            zs = [u for u in range(pc - xc, pc - 1) if e(pc, u) == 0]
                            pp = max(zs); y = pc - pp; qq = pp + 1
                            while c[qq] == y: qq += 1
                            pc, qc, xc = pp, qq, y; steps += 1
                        if not (pc <= xc <= k and steps <= k - 3 and p0 <= k * k - 2 * k and t <= k * k - k): bad['B9'] += 1
print("n<=%d partitions:%d" % (N, cnt['parts']))
for key in ['star', 'B2', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']:
    print(f"{key}: instances {cnt[key]}, violations {bad[key]}")
