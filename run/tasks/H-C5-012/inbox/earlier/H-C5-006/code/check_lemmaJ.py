#!/usr/bin/env python3
"""check_lemmaJ.py -- H-C5-006, stdlib only. SANITY CHECK (not a proof) of proof.md Lemma J:
for labellings f of Q_d: (J1) no S-vertex has an upper F-neighbour; (J2) N(u) >= deg_F(u) + 2 down_S(u) on S;
(J3) P(f) >= 2^d + (d-1)|S| + sum_S max(0, deg_F + 2 down_S - 2) up_S; plus the identity (*) of H-C5-002.
Test labellings: uniformly random, and 'forest-first' labellings (a random maximal induced forest labelled in BFS
order per tree, then the rest in random order), which have S-edges. Seeded, d = 3..9."""
import random
from collections import deque

def count(d, order):
    n = 1 << d
    lab = [0] * n
    for i, v in enumerate(order):
        lab[v] = i + 1
    N = [0] * n
    for v in order:
        low = [v ^ (1 << j) for j in range(d) if lab[v ^ (1 << j)] < lab[v]]
        N[v] = 1 if not low else sum(N[w] for w in low)
    return lab, N

def forest_first(d, rng):
    n = 1 << d
    inF = [False] * n
    par = list(range(n))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    vs = list(range(n)); rng.shuffle(vs)
    for v in vs:  # greedy maximal induced forest
        roots = [f(v ^ (1 << j)) for j in range(d) if inF[v ^ (1 << j)]]
        if len(roots) == len(set(roots)):
            inF[v] = True
            for r in roots:
                par[r] = v
    order, seen = [], [False] * n
    for r in vs:
        if inF[r] and not seen[r]:
            q = deque([r]); seen[r] = True
            while q:
                v = q.popleft(); order.append(v)
                for j in range(d):
                    w = v ^ (1 << j)
                    if inF[w] and not seen[w]:
                        seen[w] = True; q.append(w)
    rest = [v for v in range(n) if not inF[v]]; rng.shuffle(rest)
    return order + rest

rng = random.Random(20260926)
viol = tests = 0
for d in range(3, 10):
    n = 1 << d
    for t in range(30):
        order = list(range(n)); rng.shuffle(order)
        if t % 2:
            order = forest_first(d, rng)
        lab, N = count(d, order)
        P = sum(N)
        S = [v for v in range(n) if N[v] >= 2]
        inS = [N[v] >= 2 for v in range(n)]
        bound = n + (d - 1) * len(S)
        ident = n + (d - 1) * len(S)
        for u in S:
            nb = [u ^ (1 << j) for j in range(d)]
            degF = sum(1 for w in nb if not inS[w])
            upS = sum(1 for w in nb if inS[w] and lab[w] > lab[u])
            downS = sum(1 for w in nb if inS[w] and lab[w] < lab[u])
            upF = sum(1 for w in nb if not inS[w] and lab[w] > lab[u])
            if upF:  # J1
                viol += 1
            if N[u] < degF + 2 * downS:  # J2
                viol += 1
            bound += max(0, degF + 2 * downS - 2) * upS
            ident += (N[u] - 2) * (upS + upF)
        if P < bound or P != ident:
            viol += 1
        tests += 1
print("labellings tested:", tests, "violations:", viol)
