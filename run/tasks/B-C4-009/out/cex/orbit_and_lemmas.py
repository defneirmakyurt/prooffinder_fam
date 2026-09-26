"""Referee checks (stdlib only, exact integers).
(a) d_B(lambda^(k)) by theory-free first-repeat detection, k in [5, KA].
(b) symbolic orbit of proof Step 8.2 at EVERY t (diagram-based Q(h;x,y)), k in [5, KB];
    final states B^{t*} = (k,k-1,k-3,...,2), B^{t*+1} = gamma_3.
(c) Lemma 7 formula d_B(Q(h0;x,y)) = (k-h0)+(m-2)(k-1) for ALL closed S(h;x,y), k in [4, KC],
    and uniqueness of the maximiser Q(1;k-1,k) on that level.
(d) random tests of Lemma 2 (energy) and Lemma 5 (identity) on random partitions.
Usage: python3 orbit_and_lemmas.py KA KB KC NRAND"""
import sys, random

def shift(lam):
    s = len(lam)
    new = [p - 1 for p in lam if p > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def dB_direct(lam):
    seen = {}
    x = lam; t = 0
    while x not in seen:
        seen[x] = t; x = shift(x); t += 1
    return seen[x]          # index of first element on the cycle = tail length

def lam_target(k):
    return tuple([k - 2] + list(range(k - 2, 1, -1)) + [2, 1])

def cell(d, r):
    return (r, d + 1 - r)

def to_partition(cells):
    rows = {}
    for (i, j) in cells:
        rows[i] = rows.get(i, 0) + 1
    L = max(rows) if rows else 0
    lam = tuple(rows.get(i, 0) for i in range(1, L + 1))
    closed = all(((i == 1) or ((i - 1, j) in cells)) and ((j == 1) or ((i, j - 1) in cells)) for (i, j) in cells)
    return lam, closed

def S(k, h, x, y):
    cells = {cell(d, r) for d in range(1, k) for r in range(1, d + 1)}
    cells.discard(cell(k - 1, h))
    cells.add(cell(k, x)); cells.add(cell(k, y))
    return cells

def energy(lam):
    return sum(i * a + a * (a + 1) // 2 for i, a in enumerate(lam, 1))

def gamma(k, j):
    mu = list(range(k - 1, 0, -1)) + [0]
    mu[j - 1] += 1
    return tuple(p for p in mu if p > 0)

def rand_partition(n, rng):
    # random composition sorted -> a partition (distribution irrelevant)
    parts = []
    while n > 0:
        p = rng.randint(1, n); parts.append(p); n -= p
    return tuple(sorted(parts, reverse=True))

def main(KA, KB, KC, NR):
    ok = True
    # (a)
    for k in range(5, KA + 1):
        lam = lam_target(k)
        assert sum(lam) == k * (k - 1) // 2 + 1 and len(lam) == k
        assert all(lam[i] >= lam[i + 1] for i in range(len(lam) - 1))
        d = dB_direct(lam)
        if d != (k - 1) * (k - 3):
            ok = False; print("(a) FAIL", k, d)
    print(f"(a) d_B(lambda^(k)) = (k-1)(k-3) by direct first-repeat iteration, k=5..{KA}: {'OK' if ok else 'FAIL'}", flush=True)
    # (b)
    okb = True
    for k in range(5, KB + 1):
        lam = lam_target(k)
        q, cl = to_partition(S(k, 1, k - 1, k))
        assert cl and q == lam, (k, q, lam)          # lambda^(k) = Q(1;k-1,k)
        ts = k * k - 4 * k + 2
        x = lam
        for t in range(ts + 1):
            h = 1 + (t % (k - 1))
            b = 1 + ((t - 1 - 1) % k)                # b in {1..k}, b = t-1 mod k
            bp = b + 1 if b < k else 1
            q, cl = to_partition(S(k, h, b, bp))
            if not (cl and q == x):
                okb = False; print("(b) FAIL", k, t); break
            if energy(x) != energy(gamma(k, 1)) + 1:
                okb = False; print("(b) energy FAIL", k, t); break
            if t < ts:
                x = shift(x)
        if x != tuple([k, k - 1] + list(range(k - 3, 1, -1))):
            okb = False; print("(b) B^t* FAIL", k, x)
        y = shift(x)
        if y != gamma(k, 3):
            okb = False; print("(b) B^{t*+1} FAIL", k, y)
        # gamma_3 cyclic of period k (theory-free)
        z = y
        for _ in range(k):
            z = shift(z)
        if z != y:
            okb = False; print("(b) gamma_3 not cyclic", k)
        # B^{t*} not cyclic (theory-free): its orbit enters gamma-cycle and never returns
        if dB_direct(x) != 1:
            okb = False; print("(b) d_B(B^t*) != 1", k)
    print(f"(b) orbit B^t = Q(1+(t mod k-1); b_t, b_t+) for all 0<=t<=k^2-4k+2, finals, k=5..{KB}: {'OK' if okb else 'FAIL'}", flush=True)
    ok &= okb
    # (c)
    okc = True
    for k in range(4, KC + 1):
        best = -1; argbest = []
        for h in range(1, k):
            for x in range(1, k + 1):
                for y in range(x + 1, k + 1):
                    q, cl = to_partition(S(k, h, x, y))
                    pred_closed = x not in (h, h + 1) and y not in (h, h + 1)
                    if cl != pred_closed:
                        okc = False; print("(c) closedness FAIL", k, h, x, y)
                    if not cl:
                        continue
                    ox, oy = (x - h) % k, (y - h) % k
                    m = min(ox, oy)
                    pred = (k - h) + (m - 2) * (k - 1)
                    d = dB_direct(q)
                    if d != pred:
                        okc = False; print("(c) formula FAIL", k, h, x, y, d, pred)
                    if d > best:
                        best = d; argbest = [(h, x, y)]
                    elif d == best:
                        argbest.append((h, x, y))
        if best != (k - 1) * (k - 3) or argbest != [(1, k - 1, k)]:
            okc = False; print("(c) max FAIL", k, best, argbest)
    print(f"(c) Lemma 6(a) closedness + Lemma 7 formula on all S(h;x,y), unique max Q(1;k-1,k), k=4..{KC}: {'OK' if okc else 'FAIL'}", flush=True)
    ok &= okc
    # (d)
    rng = random.Random(20260926)
    okd = True
    for _ in range(NR):
        n = rng.randint(1, 300)
        lam = rand_partition(n, rng)
        s = len(lam)
        e0, e1 = energy(lam), energy(shift(lam))
        eq = (lam[0] <= s + 1)
        if e1 > e0 or ((e1 == e0) != eq):
            okd = False; print("(d) Lemma2 FAIL", lam)
        # rho(Y) closed iff eq
        Y = {(i, j) for i, a in enumerate(lam, 1) for j in range(1, a + 1)}
        R = {((i + 1, j - 1) if j >= 2 else (1, i)) for (i, j) in Y}
        q, cl = to_partition(R)
        if cl != eq or (cl and q != shift(lam)):
            okd = False; print("(d) rho FAIL", lam)
    for _ in range(NR // 10):
        k = rng.randint(4, 30); n = k * (k - 1) // 2 + 1
        lam = rand_partition(n, rng)
        Y = {(i, j) for i, a in enumerate(lam, 1) for j in range(1, a + 1)}
        c = {}
        for (i, j) in Y:
            c[i + j - 1] = c.get(i + j - 1, 0) + 1
        mdd = {d: d - c.get(d, 0) for d in range(1, k)}
        M = sum(mdd.values())
        rhs = M + sum((d - k) * v for d, v in c.items() if d >= k) + sum((k - 1 - d) * v for d, v in mdd.items())
        if energy(lam) - energy(gamma(k, 1)) != rhs or rhs < 0:
            okd = False; print("(d) Lemma5 FAIL", lam)
    print(f"(d) Lemma 2 (energy drop, equality iff lambda_1<=s+1 iff rho(Y) closed, then Y(B)=rho(Y)) on {NR} random partitions n<=300; Lemma 5 identity on {NR//10} random partitions of T_(k-1)+1, 4<=k<=30: {'OK' if okd else 'FAIL'}", flush=True)
    ok &= okd
    print("ALL OK" if ok else "FAILURE")

if __name__ == "__main__":
    a = [int(v) for v in sys.argv[1:5]]
    main(*a)
