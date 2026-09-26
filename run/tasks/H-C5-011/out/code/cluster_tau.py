#!/usr/bin/env python3
"""cluster_tau.py -- stdlib only, exact (integers / bitmasks).  Used by proof.md Steps 13-15.

For every cluster size k = 1..KMAX it enumerates, up to the automorphisms of Q_9 that preserve parity,
ALL sets C of odd vertices of Q_9 that are connected in the distance-2 graph and have |C| = k
("clusters"), and for each computes
    tau*(C) = max { tau(G_2[M']) : M' subset of N_E(C), Q_9[M' u (N_O(M') \\ C)] acyclic }
where N_E(C) = even vertices adjacent to C, N_O(M') = odd vertices adjacent to M', G_2 = distance-2 graph and
tau = vertex-cover number.  It prints, per k, the number of classes and max over classes of tau*(C) - k.

Enumeration: start from C = {o0}, o0 = 1 (weight 1).  Every connected k-set containing a given vertex is
obtained from a connected (k-1)-subset (remove a non-cut vertex of a spanning tree: a leaf) plus one
distance-2 neighbour of it, so extending every class representative of size k-1 by every distance-2
neighbour of every element, and taking canonical forms, yields every class of size k.
Canonical form of C: min over o in C and over orderings of the k rows of the matrix whose rows are the
vectors c XOR o (c in C), with columns then sorted -- i.e. min over (o, row order) of the column-sorted
matrix.  Two clusters are equivalent under x -> pi(x) XOR v (pi a coordinate permutation, v even) iff their
canonical forms agree (see README).

tau*(C) <= k is certified by tau_star(C, k): depth-first search over valid M' in increasing candidate order
(validity is closed under subsets), incremental component labels for the acyclicity test, and two pruning
bounds (tau + #addable later candidates; clique-cover bound with the local Lemma-2 cap); proof.md Step 12(c).
tau(G_2[M']) = |M'| - alpha(G_2[M']) with alpha computed by exhaustive branching.
The canonical key and the enumeration are described in proof.md Step 12(a),(b).
"""
import sys, itertools
D = 9
FULL = (1 << D) - 1
def wt(x): return bin(x).count("1")
DIST2 = [(1 << i) | (1 << j) for i in range(D) for j in range(i + 1, D)]

def canon(C):
    """Key with the property: equal keys => equivalent sets (README, proof Step 12(b)).  Minimum over o in C and
    over the row orderings allowed below of the column-sorted matrix with rows c XOR o.  Allowed orderings: rows
    sorted by the permutation-invariant (weight, sorted distances to the other rows); rows with equal invariant
    are permuted in all ways.  Any choice of allowed orderings keeps 'equal keys => equivalent'; a
    non-canonical choice can only create duplicate classes (more work), never lose one."""
    C = list(C); best = None
    for o in C:
        rows0 = [c ^ o for c in C]
        inv = {r: (wt(r), tuple(sorted(wt(r ^ s) for s in rows0 if s != r))) for r in rows0}
        groups = {}
        for r in rows0: groups.setdefault(inv[r], []).append(r)
        glist = [groups[g] for g in sorted(groups)]
        for combo in itertools.product(*[list(itertools.permutations(g)) for g in glist]):
            perm = [r for grp in combo for r in grp]
            key = tuple(sorted(tuple((r >> b) & 1 for r in perm) for b in range(D)))
            if best is None or key < best: best = key
    return best

def acyclic(verts):
    vs = list(verts); par = {v: v for v in vs}; S = set(vs)
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for v in vs:
        for i in range(D):
            w = v ^ (1 << i)
            if w > v and w in S:
                a, b = f(v), f(w)
                if a == b: return False
                par[a] = b
    return True

def alpha(vs, adj):
    # exhaustive max independent set on small graph; vs list, adj dict of bitmasks over indices
    n = len(vs)
    best = 0
    def rec(cand, size):
        nonlocal best
        if cand == 0:
            if size > best: best = size
            return
        if size + bin(cand).count("1") <= best: return
        i = (cand & -cand).bit_length() - 1
        rec(cand & ~(1 << i) & ~adj[i], size + 1)
        rec(cand & ~(1 << i), size)
    rec((1 << n) - 1, 0)
    return best

def tau(Mp):
    vs = list(Mp); n = len(vs)
    adj = [0] * n
    for a in range(n):
        for b in range(n):
            if a != b and wt(vs[a] ^ vs[b]) == 2: adj[a] |= 1 << b
    return n - alpha(vs, adj)

def tau_star(C, thr):
    """Returns (flag, witness): flag False iff some valid M' has tau(G_2[M']) > thr (witness returned);
    flag True certifies tau*(C) <= thr.  Branch and bound, see README for the two pruning bounds.
    State: olab maps every odd vertex of N_O(Mp) minus C to the label of its component in
    Q_9[Mp u (N_O(Mp) minus C)]; x (even, not in Mp) can be added without creating a cycle iff its
    odd neighbours outside C that are already present carry pairwise distinct labels (every edge at x
    goes to an odd vertex; x's other odd neighbours outside C are new leaves)."""
    Cs = set(C)
    cand = sorted({o ^ (1 << i) for o in C for i in range(D)})
    onb = {x: [x ^ (1 << i) for i in range(D) if (x ^ (1 << i)) not in Cs] for x in cand}
    kn = {o: [o ^ (1 << i) for i in range(D)] for o in C}
    # cap[o] = largest t with (t-1)(t-2)/2 <= #{o' in C : d(o,o') = 2}  (local Lemma 2, proof Step 12(c))
    cap = {}
    for o in C:
        c2 = sum(1 for p in C if wt(o ^ p) == 2)
        cap[o] = max(t for t in range(1, D + 1) if (t - 1) * (t - 2) // 2 <= c2)
    bad = [None]
    def addable(x, olab):
        seen = set()
        for w in onb[x]:
            l = olab.get(w)
            if l is None: continue
            if l in seen: return False
            seen.add(l)
        return True
    def add(x, olab, newid):
        L = {olab[w] for w in onb[x] if w in olab}
        n2 = {w: (newid if l in L else l) for w, l in olab.items()}
        for w in onb[x]: n2[w] = newid
        return n2
    def rec(start, Mp, olab, t):
        if bad[0] is not None: return
        later = [idx for idx in range(start, len(cand)) if addable(cand[idx], olab)]
        if t > thr: bad[0] = list(Mp); return
        if t + len(later) <= thr: return
        pool = set(Mp) | {cand[idx] for idx in later}
        cc = 0
        for o in C:
            s = min(cap[o], sum(1 for y in kn[o] if y in pool))
            if s > 1: cc += s - 1
        if cc <= thr: return
        for idx in later:
            x = cand[idx]
            Mp.append(x)
            t2 = tau(Mp)
            rec(idx + 1, Mp, add(x, olab, len(Mp)), t2)
            Mp.pop()
    rec(0, [], {}, 0)
    return bad[0] is None, bad[0]

def exact_tau_star(C):
    """Cross-check only: max of tau(G_2[M']) over ALL C-valid M' (no pruning; same validity test)."""
    Cs = set(C)
    cand = sorted({o ^ (1 << i) for o in C for i in range(D)})
    onb = {x: [x ^ (1 << i) for i in range(D) if (x ^ (1 << i)) not in Cs] for x in cand}
    best = [0]
    def rec(start, Mp, olab):
        t = tau(Mp)
        if t > best[0]: best[0] = t
        for idx in range(start, len(cand)):
            x = cand[idx]
            seen = set(); ok = True
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
    rec(0, [], {})
    return best[0]

PROG = False
def main():
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    # self-test: threshold k + OFF (OFF < 0 must find violations; OFF = 99: exact unpruned cross-check)
    OFF = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    global PROG
    PROG = 'prog' in sys.argv[3:]   # third argument 'prog': per-class progress on stderr
    o0 = 1
    layer = {canon([o0]): [o0]}
    worst_overall = []
    for k in range(1, KMAX + 1):
        if k > 1:
            new = {}
            for rep in layer.values():
                S = set(rep)
                for o in rep:
                    for d2 in DIST2:
                        w = o ^ d2
                        if w in S: continue
                        C2 = rep + [w]
                        key = canon(C2)
                        if key not in new: new[key] = C2
            layer = new
        if OFF == 99:   # cross-check mode: exact tau*(C) - k histogram, no pruning
            hist = {}
            for C in layer.values():
                d = exact_tau_star(C) - k; hist[d] = hist.get(d, 0) + 1
            print("k=%d classes=%d  EXACT histogram of tau*(C)-k: %s" % (k, len(layer), dict(sorted(hist.items()))), flush=True)
            continue
        cnt = 0; nviol = 0; wit = None
        for key, C in layer.items():
            ok, Mp = tau_star(C, k + OFF)
            cnt += 1
            if not ok:
                nviol += 1; wit = (C, Mp)
            if PROG: print("   k=%d class %d/%d done, violation so far: %d" % (k, cnt, len(layer), nviol), file=sys.stderr, flush=True)
        print("k=%d classes=%d  clusters with tau*(C) > k%+d: %d %s" % (k, cnt, OFF, nviol, "" if wit is None else "witness C=%s M'=%s" % wit), flush=True)
main()
