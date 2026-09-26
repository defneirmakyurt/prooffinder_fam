# stdlib only. Independent checks of the intermediate claims of proof.md Part 0 and Part B
# on ALL partitions of every n <= N (sequence c_1..c_L), and of B4/B5/B9 on all partitions of T_k, k <= KT.
# Sanity only: finite ranges prove nothing beyond them.
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
def cseq(l, L):
    c = [None]; x = l
    for _ in range(L):
        c.append(len(x)); x = B(x)
    return c
def e(c, i, u):   # e_{i,u} = [c_u >= i-u], u < i
    return 1 if c[u] >= i - u else 0
def pats(c):
    # all (p,q,x): q>=p+2, c_p=x-1, c_{p+1..q-1}=x, c_q=x+1 ; indices 1..L
    L = len(c) - 1; out = []
    for p in range(1, L):
        x = c[p] + 1; q = p + 1
        while q <= L and c[q] == x: q += 1
        if q <= L and q >= p + 2 and c[q] == x + 1: out.append((p, q, x))
    return out
N = int(sys.argv[1]); L = int(sys.argv[2]); KT = int(sys.argv[3])
cnt = dict(star=0, B2=0, B6=0, B7=0, B7c=0, B8=0, slide=0, energy=0)
nb = dict(star=0, B2=0, B6=0, B7=0, B7c=0, B8=0)
def diagonal_energy(l):
    return sum(i + j - 1 for j, h in enumerate(l, 1) for i in range(1, h + 1))
for n in range(1, N + 1):
    for l in partitions(n):
        c = cseq(l, L)
        # (*) : c_{t+1} = #{j: l_j >= t+1} + #{u<=t : c_u >= t+1-u}
        for t in range(0, L):
            v = sum(1 for h in l if h >= t + 1) + sum(1 for u in range(1, t + 1) if c[u] >= t + 1 - u)
            nb['star'] += 1
            if v != c[t + 1]: cnt['star'] += 1
        # B2 flip form: c_{i+1} = c_i + 1 - L_i
        for i in range(1, L):
            Li = sum(1 for h in l if h == i) + sum(1 for u in range(1, i) if u + c[u] == i)
            nb['B2'] += 1
            if c[i + 1] != c[i] + 1 - Li or c[i + 1] > c[i] + 1: cnt['B2'] += 1
        P = pats(c)
        for (p, q, x) in P:
            # B6: pattern (m-2, m-1..m-1, m) at p..p+m  => p+m <= n+1
            m = q - p
            if x == m - 1:
                nb['B6'] += 1
                if p + m > n + 1: cnt['B6'] += 1
            # B8
            if q == p + 2:
                nb['B8'] += 1
                if p > x: cnt['B8'] += 1
            # B7 statement and the proof's specific construction
            if q >= p + 3 and p > x and q < L - 2:
                nb['B7'] += 1
                if not any(x2 <= x and 2 <= q2 - p2 < q - p and p - x <= p2 < q2 <= p + 1 for (p2, q2, x2) in P):
                    cnt['B7'] += 1
                # construction: p' maximal in [p-x, p-2] with e_{p,p'} = 0; y = p - p';
                # pattern starts at p' with value y-1 and ends at first index with c = y+1
                cand = [u for u in range(p - x, p - 1) if e(c, p, u) == 0]
                nb['B7c'] += 1
                if not cand: cnt['B7c'] += 1; continue
                pp = max(cand); y = p - pp
                ok = c[pp] == y - 1 and c[pp + 1] == y
                if ok:
                    qq = pp + 1
                    while c[qq] == y: qq += 1
                    ok = c[qq] == y + 1 and 2 <= qq - pp < q - p and qq <= p + 1 and y <= x
                if not ok: cnt['B7c'] += 1
        # 0.3 energy: B never raises E; slide <=> E drops (only checked where n triangular below)
# Part 0.3 and B4/B5/B9 on T_k
res = []
for k in range(1, KT + 1):
    n = k * (k + 1) // 2; delta = tuple(range(k, 0, -1))
    viol = dict(E=0, slide=0, B4=0, B5=0, B9=0); cases5 = 0; maxchain = 0
    for l in partitions(n):
        # orbit and d_B
        orb = [l]; x = l
        while x != delta:
            x = B(x); orb.append(x)
            if len(orb) > 10 * n * n: raise SystemExit("no convergence")
        t = len(orb) - 1
        # energy / slide checks along orbit
        for idx in range(len(orb) - 1):
            a, b = orb[idx], orb[idx + 1]
            slide = len(a) < a[0] - 1
            Ea, Eb = diagonal_energy(a), diagonal_energy(b)
            if (not slide and Ea != Eb) or (slide and Eb > Ea - 1): viol['E'] += 1
        # 0.3 claim: from any non-delta state a slide happens within w(w+1) steps
        for idx in range(len(orb) - 1):
            a = orb[idx]
            cells = {(i, j) for j, h in enumerate(a, 1) for i in range(1, h + 1)}
            W0 = max(i + j - 1 for (i, j) in cells)
            holes = [w for w in range(1, W0) if any((w + 1 - j, j) not in cells for j in range(1, w + 1))]
            w = max(holes)
            ok = False; y = a
            for st in range(w * (w + 1)):
                if len(y) < y[0] - 1: ok = True; break
                y = B(y)
            if not ok: viol['slide'] += 1
        if t >= 1:
            c = cseq(l, t + 3)
            if not (c[t] == k - 1 and c[t + 1] == k and c[t + 2] == k): viol['B4'] += 1
        if k >= 1 and t >= k + 1:
            cases5 += 1
            c = cseq(l, t + 3); P = pats(c)
            A = [(p, q, x) for (p, q, x) in P if x == k and t - k <= p and q <= t - 1]
            Bb = [(p, q, x) for (p, q, x) in P if x == k - 1 and t - k + 1 <= p and q <= t + 1]
            if not (A or Bb): viol['B5'] += 1; continue
            if k >= 3:
                # B9 chain: follow the proof's assembly on every B5 pattern found
                for (p, q, x) in A + Bb:
                    if x == k - 1 and q == p + k:
                        if not (p == t - k + 1 and p + k <= n + 1): viol['B9'] += 1
                        continue
                    cc = cseq(l, max(t + 3, 3 * n)); PP = pats(cc)
                    pi, qi, xi = p, q, x; steps = 0; p0 = p
                    while qi - pi >= 3 and pi > xi:
                        cand = [(p2, q2, x2) for (p2, q2, x2) in PP if x2 <= xi and 2 <= q2 - p2 < qi - pi and pi - xi <= p2 < q2 <= pi + 1]
                        if not cand: viol['B9'] += 1; break
                        pi, qi, xi = cand[0]; steps += 1
                    if not (pi <= xi and steps <= k - 3 and p0 <= k * k - 2 * k and t <= k * k - k): viol['B9'] += 1
                    maxchain = max(maxchain, steps)
    res.append((k, n, cases5, maxchain, viol))
    print("T_k: k=%d n=%d B5-cases(t>=k+1)=%d max B7-chain steps=%d violations=%s" % (k, n, cases5, maxchain, viol)); sys.stdout.flush()
print("all n<=%d, c_1..c_%d: instances %s" % (N, L, nb))
print("violations", cnt)
