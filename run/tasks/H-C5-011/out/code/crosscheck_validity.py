#!/usr/bin/env python3
"""crosscheck_validity.py -- stdlib only; cross-check of cluster_tau.py (not needed for the proof).
For every class representative C of size k <= KMAX (same enumeration as cluster_tau.py), it enumerates the family
of C-valid sets in two independent ways and compares them:
  (1) the incremental component-label test used by cluster_tau.py (exact_tau_star's DFS), and
  (2) a from-scratch test: grow sets in increasing candidate order, and for each set build
      L(C, M') = Q_9[M' u (N_O(M') minus C)] explicitly and test acyclicity with a fresh union-find.
Also recomputes max tau over the family with a brute-force vertex cover (smallest X with every distance-2 pair
met), independent of the alpha routine."""
import sys, itertools
sys.argv = [sys.argv[0]] + sys.argv[1:]
import importlib.util
spec = importlib.util.spec_from_file_location("ct", __file__.replace("crosscheck_validity.py", "cluster_tau.py"))
src = open(spec.origin).read().replace("\nmain()", "\n")
ct = {}
exec(compile(src, spec.origin, "exec"), ct)
D = 9; wt = ct["wt"]; canon = ct["canon"]; DIST2 = ct["DIST2"]; acyclic = ct["acyclic"]

def family_scratch(C):
    Cs = set(C); cand = sorted({o ^ (1 << i) for o in C for i in range(D)}); fam = []
    def local(Mp):
        s = set(Mp)
        for x in Mp:
            for i in range(D):
                w = x ^ (1 << i)
                if w not in Cs: s.add(w)
        return s
    def rec(start, Mp):
        fam.append(tuple(Mp))
        for idx in range(start, len(cand)):
            Mp.append(cand[idx])
            if acyclic(local(Mp)): rec(idx + 1, Mp)
            Mp.pop()
    rec(0, []); return fam

def family_incremental(C):
    Cs = set(C); cand = sorted({o ^ (1 << i) for o in C for i in range(D)})
    onb = {x: [x ^ (1 << i) for i in range(D) if (x ^ (1 << i)) not in Cs] for x in cand}; fam = []
    def rec(start, Mp, olab):
        fam.append(tuple(Mp))
        for idx in range(start, len(cand)):
            x = cand[idx]; seen = set(); ok = True
            for w in onb[x]:
                l = olab.get(w)
                if l is None: continue
                if l in seen: ok = False; break
                seen.add(l)
            if not ok: continue
            L = {olab[w] for w in onb[x] if w in olab}
            n2 = {w: (len(Mp) + 1 if l in L else l) for w, l in olab.items()}
            for w in onb[x]: n2[w] = len(Mp) + 1
            Mp.append(x); rec(idx + 1, Mp, n2); Mp.pop()
    rec(0, [], {}); return fam

def tau_brute(Mp):
    E = [(a, b) for a, b in itertools.combinations(Mp, 2) if wt(a ^ b) == 2]
    for s in range(len(Mp) + 1):
        for X in itertools.combinations(Mp, s):
            Xs = set(X)
            if all(a in Xs or b in Xs for a, b in E): return s

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3
layer = {canon([1]): [1]}
for k in range(1, KMAX + 1):
    if k > 1:
        new = {}
        for rep in layer.values():
            S = set(rep)
            for o in rep:
                for d2 in DIST2:
                    w = o ^ d2
                    if w in S: continue
                    key = canon(rep + [w])
                    if key not in new: new[key] = rep + [w]
        layer = new
    allsame = True; mx = []
    for C in layer.values():
        f1 = family_scratch(C); f2 = family_incremental(C)
        allsame &= (set(f1) == set(f2) and len(f1) == len(f2))
        mx.append(max(tau_brute(list(M)) for M in f1) - k)
    print("k=%d classes=%d families identical: %s  brute-force max tau - k per class: %s" % (k, len(layer), allsame, sorted(mx)))
