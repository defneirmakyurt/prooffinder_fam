#!/usr/bin/env python3
"""Referee check (H-C5-014): exact integer tests of the subject's intermediate claims on random
induced forests of Q_9 (and Q_d, d=4..8 for the dimension-free lemmas).
Tests, for each generated induced forest F (acyclicity verified by union-find):
  L1  every pair x,x' in M=F∩E at distance 2 has a common neighbour in Z=O\F        (Step 4)
  L2  for each o in Z with t_o>=1: H_o acyclic, and z >= 1 + (t_o-1)(t_o-2)/2       (Step 5)
  C3  tau(G_2[M]) <= sum_o (t_o-1)^+  (tau exact via RC2 MaxSAT, only d=9)           (Step 7 (3))
  C2  |F| <= 277 + tau - z  (d=9)                                                   (Step 7 (2))
  TH  if z<=3 or |E\F|<=3 then |F| <= 279 (d=9)                                     (Step 9)
Also Lemma 3 inequalities I1,I2,I3 and N<=21 on random distance>=4 even codes of length 9.
Forests are generated with a bias towards small z (Z first chosen, then M grown greedily),
and also fully random greedy forests.  Seeded, deterministic."""
import random, sys
from itertools import combinations
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF

def pc(x): return bin(x).count("1")

def is_forest(d, F):
    par = {v: v for v in F}
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for v in F:
        for j in range(d):
            w = v ^ (1 << j)
            if w in F and v < w:
                a, b = find(v), find(w)
                if a == b: return False
                par[a] = b
    return True

def grow(d, F, cand, rng):
    """greedily add vertices of cand (random order) keeping F an induced forest"""
    par = {}
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    F = set(F)
    for v in F: par[v] = v
    for v in F:
        for j in range(d):
            w = v ^ (1 << j)
            if w in F and v < w:
                a, b = find(v), find(w)
                assert a != b
                par[a] = b
    c = list(cand); rng.shuffle(c)
    for x in c:
        if x in F: continue
        roots = [find(x ^ (1 << j)) for j in range(d) if (x ^ (1 << j)) in F]
        if len(roots) == len(set(roots)):
            F.add(x); par[x] = x
            for r in roots: par[r] = x
    return F

def tau_exact(edges):
    if not edges: return 0
    vs = sorted({v for e in edges for v in e}); idx = {v: i + 1 for i, v in enumerate(vs)}
    w = WCNF()
    for a, b in edges: w.append([idx[a], idx[b]])
    for v in vs: w.append([-idx[v]], weight=1)
    with RC2(w) as r:
        m = r.compute()
        return sum(1 for l in m if l > 0)

def check_forest(d, F, stats, full):
    assert is_forest(d, F)
    V = range(1 << d)
    E = [v for v in V if pc(v) % 2 == 0]; O = [v for v in V if pc(v) % 2 == 1]
    M = [x for x in E if x in F]; Z = [o for o in O if o not in F]; z = len(Z); Ms = set(M); Zs = set(Z)
    # L1
    g2 = []
    for x, y in combinations(M, 2):
        if pc(x ^ y) == 2:
            i, j = [k for k in range(d) if (x ^ y) >> k & 1]
            a, b = x ^ (1 << i), x ^ (1 << j)
            if not (a in Zs or b in Zs): stats['L1fail'] += 1
            g2.append((x, y))
    # L2
    sumt = 0
    for o in Z:
        D = [j for j in range(d) if (o ^ (1 << j)) in Ms]
        t = len(D)
        if t >= 1:
            sumt += t - 1
            Hedges = [(i, j) for i, j in combinations(D, 2) if (o ^ (1 << i) ^ (1 << j)) in F]
            # acyclic check on H_o
            par = {j: j for j in D}
            def fd(a):
                while par[a] != a: a = par[a]
                return a
            cyc = False
            for i, j in Hedges:
                a, b = fd(i), fd(j)
                if a == b: cyc = True
                else: par[a] = b
            if cyc: stats['L2acyc_fail'] += 1
            if not (z >= 1 + (t - 1) * (t - 2) // 2): stats['L2ineq_fail'] += 1
            stats['maxt'] = max(stats['maxt'], t)
    if full:
        tau = tau_exact(g2)
        if tau > sumt: stats['C3fail'] += 1
        if len(F) > 277 + tau - z: stats['C2fail'] += 1
        stats['maxslack2'] = max(stats['maxslack2'], len(F) - (277 + tau - z))
    ze = len([x for x in E if x not in F])
    if (z <= 3 or ze <= 3):
        stats['TH_tested'] += 1
        stats['TH_maxF'] = max(stats['TH_maxF'], len(F))
        if len(F) > 279: stats['THfail'] += 1
    stats['n'] += 1

def lemma3_random(rng, trials):
    E = [v for v in range(512) if pc(v) % 2 == 0]
    bad = 0; best = 0
    for _ in range(trials):
        c = E[:]; rng.shuffle(c); C = []
        for x in c:
            if all(pc(x ^ y) >= 4 for y in C): C.append(x)
            if len(C) >= rng.randint(1, 25): break
        N = len(C); a = {0: 0, 4: 0, 6: 0, 8: 0}
        for x in C:
            for y in C: a[pc(x ^ y)] += 1
        I1 = 9 * a[0] + a[4] - 3 * a[6] - 7 * a[8]
        I2 = 36 * a[0] - 4 * a[4] + 20 * a[8]
        # direct evaluation of the squared sums
        s1 = sum(sum((-1) ** (x >> j & 1) for x in C) ** 2 for j in range(9))
        s2 = sum(sum((-1) ** ((x >> j & 1) + (x >> l & 1)) for x in C) ** 2 for j in range(9) for l in range(j + 1, 9))
        if not (I1 == s1 >= 0 and I2 == s2 >= 0 and a[8] <= N and N <= 21 and N * N == sum(a.values())): bad += 1
        best = max(best, N)
    return bad, best

if __name__ == "__main__":
    rng = random.Random(20260926)
    stats = dict(n=0, L1fail=0, L2acyc_fail=0, L2ineq_fail=0, C3fail=0, C2fail=0, THfail=0, TH_tested=0,
                 TH_maxF=0, maxt=0, maxslack2=-10**9)
    # d = 9 forests biased to small z
    for trial in range(300):
        d = 9
        O = [v for v in range(512) if pc(v) % 2 == 1]
        E = [v for v in range(512) if pc(v) % 2 == 0]
        z = rng.choice([0, 1, 2, 3, 3, 3, 4, 5, 8, 16, 40])
        if rng.random() < 0.5 and z >= 2:
            # clustered Z: around a random odd o1
            o1 = rng.choice(O); Z = {o1}
            while len(Z) < z:
                i, j = rng.sample(range(9), 2); Z.add(rng.choice(list(Z)) ^ (1 << i) ^ (1 << j))
        else:
            Z = set(rng.sample(O, z))
        F = set(O) - Z
        if not is_forest(d, F): continue
        F = grow(d, F, E, rng)
        check_forest(d, F, stats, full=True)
        if rng.random() < 0.3:
            # parity-swapped copy
            G = {v ^ 1 for v in F}
            check_forest(d, G, stats, full=True)
    # fully random greedy forests, d = 4..9 (L1, L2 only; C2/C3 also for d=9)
    for trial in range(300):
        d = rng.choice([4, 5, 6, 7, 8, 9])
        F = grow(d, set(), range(1 << d), rng)
        if d == 9: check_forest(d, F, stats, full=True)
        else:
            # dimension-free lemmas only
            st2 = dict(stats); check_forest(d, F, st2, full=False)
            for k in ('L1fail', 'L2acyc_fail', 'L2ineq_fail', 'n', 'maxt'): stats[k] = st2[k]
    print("forest tests:", stats)
    bad, best = lemma3_random(rng, 3000)
    print("Lemma 3 random codes: 3000 codes, violations =", bad, " largest random code =", best)
