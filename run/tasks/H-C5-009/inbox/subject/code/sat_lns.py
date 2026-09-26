#!/usr/bin/env python3
"""sat_lns.py -- large-neighbourhood search for a small decycling set of Q_d, exact SAT sub-solves.
Start: an induced forest F0 (indicator file). Repeat: choose a region R (random subcube of dimension k, or
random Hamming ball of radius r); keep every vertex outside R as in the current solution; ask the SAT solver
(CEGAR with lazy cycle clauses over the vertices of R, as in sat_cegar.py) for a set S_R inside R with
|S_R| <= |S cap R| - 1 such that (V \\ S_outside \\ S_R) is a forest. If found: accept (|S| drops by 1).
If UNSAT or timeout for this region: try another region. Every accepted solution is re-checked to be a
forest. SEARCH tool only: UNSAT / timeouts are not claims.
Usage: sat_lns.py d init.txt out.txt --rounds R --k K --sub-time T --seed s [--ball r]
"""
import sys, time, random, argparse
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

ap = argparse.ArgumentParser()
ap.add_argument('d', type=int); ap.add_argument('init'); ap.add_argument('out')
ap.add_argument('--rounds', type=int, default=20); ap.add_argument('--k', type=int, default=6)
ap.add_argument('--ball', type=int, default=0)
ap.add_argument('--sub-time', type=float, default=20.0); ap.add_argument('--seed', type=int, default=0)
ap.add_argument('--total-time', type=float, default=500.0)
a = ap.parse_args()
d = a.d; n = 1 << d
random.seed(a.seed)
inF = [c == '1' for c in open(a.init).read().strip()]
assert len(inF) == n
nb = lambda v: [v ^ (1 << j) for j in range(d)]

def is_forest(F):
    par = list(range(n))
    def fp(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for v in range(n):
        if F[v]:
            for w in nb(v):
                if w > v and F[w]:
                    x, y = fp(v), fp(w)
                    if x == y: return False
                    par[x] = y
    return True

assert is_forest(inF)

def small_cycles():
    cyc = []
    for v in range(n):
        for i in range(d):
            for j in range(i + 1, d):
                c = [v, v ^ (1 << i), v ^ (1 << i) ^ (1 << j), v ^ (1 << j)]
                if v == min(c): cyc.append(c)
    for v in range(n):
        for i in range(d):
            for j in range(i + 1, d):
                for k in range(j + 1, d):
                    m = (1 << i) | (1 << j) | (1 << k)
                    if v & m: continue
                    cube = [v | (((t >> 0) & 1) << i) | (((t >> 1) & 1) << j) | (((t >> 2) & 1) << k) for t in range(8)]
                    for x in cube:
                        if (x & m) < ((x ^ m) & m):
                            cyc.append([y for y in cube if y != x and y != (x ^ m)])
    return cyc
SMALL = small_cycles()

def find_cycles(F, limit=300):
    par = [-2] * n; nontree = []
    for r in range(n):
        if not F[r] or par[r] != -2: continue
        par[r] = -1; q = [r]; h = 0
        while h < len(q):
            v = q[h]; h += 1
            for w in nb(v):
                if not F[w]: continue
                if par[w] == -2: par[w] = v; q.append(w)
                elif w != par[v] and v < w and par[w] != v: nontree.append((v, w))
    random.shuffle(nontree); out = []
    for (u, w) in nontree[:limit]:
        prev = {u: None}; q = [u]; h = 0; found = False
        while h < len(q) and not found:
            x = q[h]; h += 1
            for y in nb(x):
                if not F[y] or y in prev: continue
                if x == u and y == w: continue
                prev[y] = x
                if y == w: found = True; break
                q.append(y)
        if found:
            c = []; y = w
            while y is not None: c.append(y); y = prev[y]
            out.append(c)
    return out

def region():
    if a.ball:
        c = random.randrange(n)
        return [v for v in range(n) if bin(v ^ c).count('1') <= a.ball]
    free = random.sample(range(d), a.k); fixed = [j for j in range(d) if j not in free]
    val = random.randrange(n)
    mask = sum(1 << j for j in fixed)
    return [v for v in range(n) if (v & mask) == (val & mask)]

t0 = time.time()
curS = n - sum(inF)
print('start |S|=%d' % curS, flush=True)
for rnd_ in range(a.rounds):
    if time.time() - t0 > a.total_time: print('total time reached'); break
    R = region(); idx = {v: i + 1 for i, v in enumerate(R)}
    inR = [False] * n
    for v in R: inR[v] = True
    sR = sum(1 for v in R if not inF[v])
    s = Solver(name='cd15')
    def clause_for(c):
        if any((not inR[v]) and (not inF[v]) for v in c): return None  # fixed S vertex on it: never a cycle
        cl = [idx[v] for v in c if inR[v]]
        return cl
    for c in SMALL:
        cl = clause_for(c)
        if cl is not None:
            if not cl: raise SystemExit('fixed cycle?')
            s.add_clause(cl)
    pool = IDPool(start_from=len(R) + 1)
    for cl in CardEnc.atmost(lits=list(range(1, len(R) + 1)), bound=sR - 1, vpool=pool, encoding=EncType.seqcounter).clauses:
        s.add_clause(cl)
    ts = time.time(); res = None; its = 0
    while time.time() - ts < a.sub_time:
        its += 1
        if not s.solve(): res = 'UNSAT'; break
        m = s.get_model()
        F = list(inF)
        for v in R: F[v] = m[idx[v] - 1] < 0
        cyc = find_cycles(F)
        if not cyc: res = F; break
        for c in cyc:
            cl = clause_for(c)
            s.add_clause(cl)
    s.delete()
    if isinstance(res, list):
        assert is_forest(res)
        inF = res; curS = n - sum(inF)
        open(a.out, 'w').write(''.join('1' if x else '0' for x in inF) + '\n')
        print('round %d |R|=%d: IMPROVED -> |S|=%d (%.1fs)' % (rnd_, len(R), curS, time.time() - t0), flush=True)
    else:
        print('round %d |R|=%d |S cap R|=%d: %s after %d its (%.1fs)' % (rnd_, len(R), sR, res or 'TIMEOUT', its, time.time() - t0), flush=True)
print('final |S|=%d' % curS)
