#!/usr/bin/env python3
"""Referee checks of Lemma A's intermediate claims (stdlib, exact integers).
Part 1: ALL 8! = 40320 labellings of Q_3: checks A2 (DP recurrence == explicit enumeration of
        sequences), A3 (N(v) >= 1 and N(v) >= down(v)), A4 identity, A6 identity, (i) T = {down<=1}
        induces a forest, (ii) count >= 2^d + (d-1)|S|; and min count (= U(Q_3)).
Part 2: seeded random labellings of Q_4..Q_8 (uniform and weight-sorted with noise): same checks
        except explicit enumeration only for d <= 6.
"""
import itertools, random, time

def analyse(d, order, enumerate_paths):
    n = 1 << d; E = d << (d - 1)
    f = [0] * n
    for i, v in enumerate(order, 1): f[v] = i
    down = [sum(1 for j in range(d) if f[v ^ (1 << j)] < f[v]) for v in range(n)]
    up = [d - down[v] for v in range(n)]
    N = [0] * n
    for v in order:
        N[v] = (1 if down[v] == 0 else 0) + sum(N[v ^ (1 << j)] for j in range(d) if f[v ^ (1 << j)] < f[v])
    tot = sum(N)
    errs = []
    if enumerate_paths:
        cnt = 0; st = [v for v in range(n) if all(f[v ^ (1 << j)] > f[v] for j in range(d))]
        while st:
            v = st.pop(); cnt += 1
            st.extend(v ^ (1 << j) for j in range(d) if f[v ^ (1 << j)] > f[v])
        if cnt != tot: errs.append("A2: DP %d != enumeration %d" % (tot, cnt))
    V0 = sum(1 for v in range(n) if down[v] == 0)
    for v in range(n):
        if N[v] < 1 or N[v] < down[v]: errs.append("A3 fails at %d" % v)
    if tot != V0 + E + sum((N[w] - 1) * up[w] for w in range(n)): errs.append("A4 identity fails")
    S = [v for v in range(n) if down[v] >= 2]; T = [v for v in range(n) if down[v] <= 1]
    if sum(down[w] for w in S) != E - len(T) + V0: errs.append("A6 identity fails")
    # (i) forest test: edges == vertices - components
    Ts = set(T)
    e = sum(1 for v in T for j in range(d) if (v ^ (1 << j)) in Ts) // 2
    seen = set(); comps = 0
    for r in T:
        if r in seen: continue
        comps += 1; seen.add(r); st = [r]
        while st:
            v = st.pop()
            for j in range(d):
                w = v ^ (1 << j)
                if w in Ts and w not in seen: seen.add(w); st.append(w)
    if e != len(T) - comps: errs.append("(i) T not a forest")
    bound = n + (d - 1) * len(S)
    if tot < bound: errs.append("(ii) count %d < bound %d" % (tot, bound))
    return tot, bound, len(S), errs

t0 = time.time()
d = 3; mn = None; nerr = 0; neq = 0
for perm in itertools.permutations(range(8)):
    tot, bound, s, errs = analyse(3, perm, True)
    nerr += len(errs)
    if tot == bound: neq += 1
    mn = tot if mn is None else min(mn, tot)
print("Part 1: Q_3, all 40320 labellings: violations=%d, min count=%d, #labellings with equality in (ii)=%d (%.1fs)"
      % (nerr, mn, neq, time.time() - t0))
rng = random.Random(4242)
for d in range(4, 9):
    t1 = time.time(); trials = 300 if d <= 6 else 60; nerr = 0; mn = None
    for _ in range(trials):
        order = list(range(1 << d)); rng.shuffle(order)
        if rng.random() < 0.6:
            noise = rng.choice([0.5, 1.5, 3.0])
            order.sort(key=lambda v: bin(v).count("1") + rng.random() * noise)
        tot, bound, s, errs = analyse(d, order, d <= 6)
        nerr += len(errs); mn = tot if mn is None else min(mn, tot)
        for x in errs: print("  VIOLATION d=%d: %s" % (d, x))
    print("Part 2: d=%d, %d random labellings: violations=%d, min count seen=%d (%.1fs)" % (d, trials, nerr, mn, time.time() - t1))
print("total elapsed %.1fs" % (time.time() - t0))
