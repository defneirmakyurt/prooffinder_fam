# stdlib only, exact. Checks proof steps 0.1, 0.3 (energy + slide-within-w(w+1) claim) and A.2 (all a,b).
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
def diagram(l):
    return frozenset((i, j) for j, h in enumerate(l, 1) for i in range(1, h + 1))
def rot(S):
    return frozenset(((i - 1, j + 1) if i >= 2 else (j, 1)) for (i, j) in S)
def E(S): return sum(i + j - 1 for (i, j) in S)
def from_diagram(S):
    # returns partition if S is a Young diagram, else None
    cols = {}
    for (i, j) in S: cols[j] = cols.get(j, 0) + 1
    if not cols: return ()
    s = max(cols)
    lam = tuple(cols.get(j, 0) for j in range(1, s + 1))
    if any(h == 0 for h in lam) or any(lam[j] < lam[j + 1] for j in range(s - 1)): return None
    if diagram(lam) != S: return None
    return lam
NP = int(sys.argv[1]); KD = int(sys.argv[2]); KA = int(sys.argv[3])
bad01 = bad03 = badE = 0; n01 = n03 = 0
# 0.1 on all partitions of n <= NP
for n in range(1, NP + 1):
    for l in partitions(n):
        n01 += 1
        S = diagram(l); R = rot(S); s = len(l)
        if s >= l[0] - 1:
            if diagram(B(l)) != R: bad01 += 1
        else:
            Sl = frozenset(((i, j - 1) if i > s else (i, j)) for (i, j) in R)
            if not (all(j >= 2 for (i, j) in R if i > s) and diagram(B(l)) == Sl and any(i > s for (i, j) in R)):
                bad01 += 1
# 0.3 on all partitions of T_k, k <= KD
for k in range(1, KD + 1):
    n = k * (k + 1) // 2; delta = tuple(range(k, 0, -1)); Dk = diagram(delta)
    for l in partitions(n):
        if l == delta: continue
        n03 += 1
        S = diagram(l)
        W0 = max(i + j - 1 for (i, j) in S)
        holes = [w for w in range(1, W0) if any((w + 1 - j, j) not in S for j in range(1, w + 1))]
        w = max(holes)
        x = l; found = False
        for step in range(w * (w + 1)):
            s = len(x); slide = s < x[0] - 1
            Sx = diagram(x); Sy = diagram(B(x))
            if slide:
                if not E(Sy) < E(Sx): badE += 1
                found = True; break
            else:
                if E(Sy) != E(Sx): badE += 1
            x = B(x)
        if not found: bad03 += 1
# A.2 for 2 <= k <= KA, all a in 1..k, b in 1..k+1 with S(a,b) a Young diagram
badA = 0; nA = 0
for k in range(2, KA + 1):
    D = frozenset((i, j) for i in range(1, k + 1) for j in range(1, k + 1) if i + j - 1 <= k)
    def Sab(a, b): return (D - {(k + 1 - a, a)}) | {(k + 2 - b, b)}
    for a in range(1, k + 1):
        for b in range(1, k + 2):
            mu = from_diagram(Sab(a, b))
            if mu is None: continue
            nA += 1
            s_ok = len(mu) == k - (a == k) + (b == k + 1) and mu[0] == k - (a == 1) + (b == 1)
            nb = B(mu)
            if a == k and b == 1: ok = nb == tuple(range(k, 0, -1))
            else: ok = diagram(nb) == Sab(a % k + 1, b % (k + 1) + 1)
            if not (s_ok and ok): badA += 1
print(f"0.1: partitions n<={NP}: {n01}, violations {bad01}")
print(f"0.3: non-delta partitions of T_k, k<={KD}: {n03}, no slide within w(w+1) steps: {bad03}, energy-rule violations: {badE}")
print(f"A.2: k=2..{KA}, admissible (a,b): {nA}, violations {badA}")
