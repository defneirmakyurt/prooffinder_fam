#!/usr/bin/env python3
"""sym_cegar.py -- H-C5-006. Needs python-sat (project venv). SEARCH over induced forests of Q_9 that are
invariant under a group G of coordinate permutations, by SAT with lazily added cycle clauses (CEGAR).
Variables: one per G-orbit of vertices (x_o = 1 iff orbit o is in F). Constraint: sum_o |o| x_o >= K.
Loop: solve; if the model's F induces a cycle in Q_9, add for each found cycle Z the clause OR_{o meets Z} not x_o;
repeat. Result SAT (an acyclic F with |F| >= K is found and re-verified by union-find) or UNSAT (no G-invariant
induced forest with >= K vertices exists: every added clause is a valid consequence of acyclicity, and the
cardinality encoding is exact), or TIMEOUT.
Usage: sym_cegar.py GROUP K timeout_s outfile   GROUP in {c9, c3, c3x3, none}"""
import sys, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType

d, n = 9, 512
def perm_apply(v, p):  # p: list, new coord i gets old coord p[i]
    w = 0
    for i in range(d):
        if v >> p[i] & 1:
            w |= 1 << i
    return w
G = sys.argv[1]; K = int(sys.argv[2]); tmax = float(sys.argv[3]); out = sys.argv[4]
gens = []
if G == "c9":
    gens = [[(i + 1) % 9 for i in range(9)]]
elif G == "c3":
    gens = [[(i + 3) % 9 for i in range(9)]]
elif G == "c3x3":   # coordinates as 3x3 grid (r,c) -> index 3r+c ; shift rows and shift columns
    gens = [[(3 * ((i // 3 + 1) % 3) + i % 3) for i in range(9)], [(3 * (i // 3) + (i % 3 + 1) % 3) for i in range(9)]]
orb = [-1] * n; orbits = []
for v in range(n):
    if orb[v] >= 0: continue
    o = {v}; st = [v]
    while st:
        x = st.pop()
        for p in gens:
            y = perm_apply(x, p)
            if y not in o:
                o.add(y); st.append(y)
    for x in o: orb[x] = len(orbits)
    orbits.append(sorted(o))
m = len(orbits)
var = lambda o: o + 1
lits = [var(orb[v]) for v in range(n)]          # one literal per vertex (orbit literal repeated)
# exact cardinality: introduce per-vertex copies y_v <-> x_orb(v) to avoid duplicate inputs
top = m
ylit = []
cls = []
for v in range(n):
    top += 1; ylit.append(top)
    cls.append([-top, var(orb[v])]); cls.append([top, -var(orb[v])])
card = CardEnc.atleast(lits=ylit, bound=K, top_id=top, encoding=EncType.seqcounter)
s = Cadical153(bootstrap_with=cls + card.clauses)
def add_cycle(cyc):
    s.add_clause(sorted({-var(orb[v]) for v in cyc}))
# initial 4-cycle clauses
nclauses = 0
seen = set()
for v in range(n):
    for i in range(d):
        for j in range(i + 1, d):
            if not (v >> i & 1) and not (v >> j & 1):
                cyc = (v, v | 1 << i, v | 1 << i | 1 << j, v | 1 << j)
                key = frozenset(orb[x] for x in cyc)
                if key not in seen:
                    seen.add(key); add_cycle(cyc); nclauses += 1
def find_cycles(F):
    """return a list of cycles (vertex lists) closing union-find, via BFS tree paths."""
    par = list(range(n))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    adj = {v: [] for v in F}
    bad = []
    for v in sorted(F):
        for i in range(d):
            w = v ^ (1 << i)
            if w > v and w in F:
                a, b = f(v), f(w)
                if a == b:
                    bad.append((v, w))
                else:
                    par[a] = b; adj[v].append(w); adj[w].append(v)
    cycles = []
    for (v, w) in bad[:200]:
        # path v -> w in the spanning forest
        prev = {v: None}; q = [v]
        for x in q:
            if x == w: break
            for y in adj[x]:
                if y not in prev:
                    prev[y] = x; q.append(y)
        path = []; x = w
        while x is not None:
            path.append(x); x = prev[x]
        cycles.append(path)
    return cycles, len(bad)
t0 = time.time(); it = 0; status = "TIMEOUT"
while time.time() - t0 < tmax:
    it += 1
    if not s.solve():
        status = "UNSAT"; break
    model = set(l for l in s.get_model() if 0 < l <= m)
    F = set(v for v in range(n) if var(orb[v]) in model)
    cycles, nb = find_cycles(F)
    if nb == 0:
        status = "SAT"; break
    for c in cycles:
        add_cycle(c); nclauses += 1
print("group=%s orbits=%d K=%d status=%s iterations=%d cycle_clauses=%d time=%.1fs" % (G, m, K, status, it, nclauses, time.time() - t0))
if status == "SAT":
    # independent re-check
    par = list(range(n))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    ok = True
    for v in F:
        for i in range(d):
            w = v ^ (1 << i)
            if w > v and w in F:
                a, b = f(v), f(w)
                if a == b: ok = False
                par[a] = b
    print("recheck forest:", ok, "|F| =", len(F), "|S| =", n - len(F))
    open(out, "w").write("".join("1" if v in F else "0" for v in range(n)) + "\n")
