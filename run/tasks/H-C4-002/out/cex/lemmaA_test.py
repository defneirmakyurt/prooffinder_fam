#!/usr/bin/env python3
"""Referee's test of Lemma A and its intermediate claims (stdlib, exact ints).
(1) exhaustive over ALL labellings of Q_2 (24) and Q_3 (40320): count by recurrence AND by explicit
    enumeration; check A2-A7 facts: N(v)>=1, N(v)>=down(v) if down>=1, identity
    sum N = V0 + E + sum (N-1)*up, count >= 2^d+(d-1)|S|, T = {down<=1} acyclic; report min count.
(2) structured labellings (lex, reverse lex, weight order, Gray code) for d=1..9.
(3) adversarial local search (random transpositions, accept if slack count-bound does not increase)
    for d=4..7 from random starts, looking for slack < 0."""
import itertools, random, sys, time

def analyse(d, order, enum=False):
    n = 1 << d; E = d * (n >> 1)
    f = [0] * n
    for i, v in enumerate(order): f[v] = i + 1
    N = [0] * n; V0 = 0
    down = [0] * n
    for v in order:
        low = [v ^ (1 << j) for j in range(d) if f[v ^ (1 << j)] < f[v]]
        down[v] = len(low)
        val = 1 if not low else 0
        V0 += val
        N[v] = val + sum(N[w] for w in low)
    tot = sum(N)
    assert all(x >= 1 for x in N), "N>=1 fails"
    assert all(N[v] >= down[v] for v in range(n)), "N>=down fails"
    assert tot == V0 + E + sum((N[w] - 1) * (d - down[w]) for w in range(n)), "A4 identity fails"
    S = [v for v in range(n) if down[v] >= 2]
    inS = [0] * n
    for v in S: inS[v] = 1
    # T acyclic: edges = |T| - comps
    T = [v for v in range(n) if not inS[v]]
    e = sum(1 for v in T for j in range(d) if (v >> j) & 1 == 0 and not inS[v ^ (1 << j)])
    seen = [0] * n; comps = 0
    for r in T:
        if seen[r]: continue
        comps += 1; seen[r] = 1; st = [r]
        while st:
            x = st.pop()
            for j in range(d):
                w = x ^ (1 << j)
                if not inS[w] and not seen[w]: seen[w] = 1; st.append(w)
    assert e == len(T) - comps, "T not a forest"
    bound = n + (d - 1) * len(S)
    assert tot >= bound, ("Lemma A violated", d, order, tot, bound)
    if enum:
        cnt = 0; st = [(v,) for v in range(n) if down[v] == 0]
        while st:
            p = st.pop(); cnt += 1
            for j in range(d):
                w = p[-1] ^ (1 << j)
                if f[w] > f[p[-1]]: st.append(p + (w,))
        assert cnt == tot, "enumeration != recurrence"
    return tot, bound

t0 = time.time()
for d in (1, 2, 3):
    n = 1 << d; mn = None; mnslack = None; k = 0
    for order in itertools.permutations(range(n)):
        tot, b = analyse(d, list(order), enum=True); k += 1
        mn = tot if mn is None else min(mn, tot)
        mnslack = tot - b if mnslack is None else min(mnslack, tot - b)
    print("d=%d exhaustive: %d labellings, all checks pass, min count=%d, min slack=%d" % (d, k, mn, mnslack))

def gray(i): return i ^ (i >> 1)
for d in range(1, 10):
    n = 1 << d
    orders = {"lex": list(range(n)), "revlex": list(range(n))[::-1],
              "weight": sorted(range(n), key=lambda v: (bin(v).count('1'), v)),
              "gray": [gray(i) for i in range(n)]}
    res = {k: analyse(d, o) for k, o in orders.items()}
    print("d=%d structured (count,bound):" % d, res)

rng = random.Random(7)
worst = {}
for d in (4, 5, 6, 7):
    n = 1 << d; w = None
    for start in range(20 if d <= 5 else 6):
        order = list(range(n)); rng.shuffle(order)
        tot, b = analyse(d, order); slack = tot - b
        for it in range(3000 if d <= 5 else 800):
            i, j = rng.randrange(n), rng.randrange(n)
            order[i], order[j] = order[j], order[i]
            t2, b2 = analyse(d, order)
            if t2 - b2 <= slack: slack = t2 - b2
            else: order[i], order[j] = order[j], order[i]
        w = slack if w is None else min(w, slack)
    worst[d] = w
print("adversarial local search, min slack (count - bound) found per d:", worst)
print("elapsed %.1f s" % (time.time() - t0))
