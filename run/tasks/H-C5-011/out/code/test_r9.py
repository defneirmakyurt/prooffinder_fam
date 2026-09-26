#!/usr/bin/env python3
"""test_r9.py -- exploratory (NOT part of the proof; needs python-sat from the venv).
For an induced forest F of Q_9 given as a 512-char 0/1 line (char v = 1 iff vertex v in F), check that F is
an induced forest, and for BOTH parity choices (M = F n E, Z = O \\ F) and (M = F n O, Z = E \\ F) compute
z = |Z|, tau(G_2[M]) exactly (= |M| - alpha, alpha by MaxSAT), and the per-cluster taus
(cluster = component of Z under distance 2), to test R9 (tau <= z + 2) and the stronger tau <= z."""
import sys
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
D, N = 9, 512
wt = lambda x: bin(x).count("1")
def is_forest(F):
    par = list(range(N))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for v in F:
        for i in range(D):
            w = v ^ (1 << i)
            if w > v and w in F:
                a, b = f(v), f(w)
                if a == b: return False
                par[a] = b
    return True
def alpha(verts, edges):
    if not verts: return 0
    idx = {v: k + 1 for k, v in enumerate(verts)}
    w = WCNF()
    for (x, y) in edges: w.append([-idx[x], -idx[y]])
    for v in verts: w.append([idx[v]], weight=1)
    with RC2(w) as r:
        m = r.compute()
    return sum(1 for l in m if l > 0)
def analyse(F, par_M):
    M = [v for v in F if wt(v) % 2 == par_M]
    Z = [v for v in range(N) if wt(v) % 2 != par_M and v not in F]
    Ms = set(M)
    edges = [(x, y) for x in M for y in M if x < y and wt(x ^ y) == 2]
    tau = len(M) - alpha(M, edges)
    # clusters of Z
    Zs = set(Z); seen = set(); cl = []
    for o in Z:
        if o in seen: continue
        comp = [o]; seen.add(o); st = [o]
        while st:
            u = st.pop()
            for i in range(D):
                for j in range(i + 1, D):
                    w = u ^ (1 << i) ^ (1 << j)
                    if w in Zs and w not in seen: seen.add(w); comp.append(w); st.append(w)
        cl.append(comp)
    res = []
    for comp in cl:
        MC = sorted({o ^ (1 << i) for o in comp for i in range(D)} & Ms)
        e = [(x, y) for x in MC for y in MC if x < y and wt(x ^ y) == 2]
        tc = len(MC) - alpha(MC, e)
        res.append((len(comp), len(MC), tc))
    return len(M), len(Z), tau, res
for fn in sys.argv[1:]:
    s = open(fn).read().strip()
    F = {v for v in range(N) if s[v] == '1'}
    print(fn, "|F| =", len(F), "forest:", is_forest(F))
    for pm in (0, 1):
        m, z, tau, res = analyse(F, pm)
        bad = [r for r in res if r[2] > r[0]]
        print("  M parity %d: m=%d z=%d tau=%d  (tau<=z+2: %s, tau<=z: %s); clusters=%d, maxsize=%d, clusters with tau_C>|C|: %s"
              % (pm, m, z, tau, tau <= z + 2, tau <= z, len(res), max([r[0] for r in res] + [0]), bad[:5]))
