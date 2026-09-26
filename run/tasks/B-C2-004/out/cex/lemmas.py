"""Stdlib-only, exact. Sanity checks of intermediate claims (finite ranges; not proofs).
(A) Steps 2-4: D(B(l)) = rho(D(l)) then columns j>s moved up one row; E(B l) = E(l) - sum_{j>s} c_j.
    Tested on ALL partitions of n for n<=30 and 3000 random partitions of n in [31,200] (seeded).
(B) Step 13: tau(h,i) by brute force equals k*x0+1-h, <= k^2-k, equality iff (h,i)=(1,k+1); k=2..60.
(C) Steps 11-14: every lambda in R_k (enumerated via all Young-valid hole/cell row sets) for k=2..9:
    Step 11 constraint holds, |H|=|C|, B keeps R_k, d_B(lambda) = tau(h0,i0) of the last pair and <= k^2-k."""
import random, itertools
def B(l):
    s = len(l); return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def diagram(l): return {(i + 1, j + 1) for i, x in enumerate(l) for j in range(x)}
def rho(c):
    i, j = c; return (i + 1, j - 1) if j >= 2 else (1, i)
def parts(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for p in range(min(n, m), 0, -1):
        for r in parts(n - p, p): yield (p,) + r
def from_diag(D):
    rows = {}
    for (i, j) in D: rows[i] = rows.get(i, 0) + 1
    l = tuple(rows.get(i, 0) for i in range(1, len(rows) + 1))
    assert diagram(l) == D and all(l[q] >= l[q + 1] for q in range(len(l) - 1)), "not a Young diagram"
    return l
def E(l): return sum(i + j - 1 for (i, j) in diagram(l))
def checkA(l):
    s = len(l); R = {rho(c) for c in diagram(l)}
    newD = set()
    for (i, j) in R:
        newD.add((i - 1, j) if j > s else (i, j))
    c = lambda j: sum(1 for x in l if x >= j + 1)
    return newD == diagram(B(l)) and E(B(l)) == E(l) - sum(c(j) for j in range(s + 1, max(l) + 1))
def rand_part(n, rng):
    # random composition sorted -> random partition (distribution irrelevant)
    cuts = sorted(rng.sample(range(1, n), rng.randint(0, min(n - 1, 40)))) if n > 1 else []
    pts = [b - a for a, b in zip([0] + cuts, cuts + [n])]
    return tuple(sorted(pts, reverse=True))
okA = True; cntA = 0
for n in range(1, 31):
    for l in parts(n): okA &= checkA(l); cntA += 1
rng = random.Random(20260926)
for _ in range(3000):
    l = rand_part(rng.randint(31, 200), rng); okA &= checkA(l); cntA += 1
print(f"(A) Steps 2-4 on {cntA} partitions:", "OK" if okA else "FAIL")
def tau_brute(h, i, k):
    t = 1
    while not ((h + t) % k == 1 % k and (i + t) % (k + 1) == 2 % (k + 1)): t += 1
    return t
okB = True
for k in range(2, 61):
    for h in range(1, k + 1):
        for i in range(1, k + 2):
            if i - h in (0, 1): continue
            tb = tau_brute(h, i, k); x0 = (i - h - 1) % (k + 1)
            okB &= (tb == k * x0 + 1 - h) and tb <= k * k - k and ((tb == k * k - k) == ((h, i) == (1, k + 1)))
print("(B) Step 13 formula/bound/equality k=2..60:", "OK" if okB else "FAIL")
okC = True; cntC = 0
for k in range(2, 10):
    delta = tuple(range(k, 0, -1)); base = diagram(tuple(range(k - 1, 0, -1)))
    trk = lambda d, r: (r, d + 1 - r)
    for m in range(0, k + 1):
        for H in itertools.combinations(range(1, k + 1), m):
            for C in itertools.combinations(range(1, k + 2), m):
                D = set(base) | {trk(k, r) for r in range(1, k + 1) if r not in H} | {trk(k + 1, r) for r in C}
                try: l = from_diag(D)
                except AssertionError: continue
                cntC += 1
                okC &= all((i - h) not in (0, 1) for h in H for i in C)
                # simulate, tracking labelled holes/cells by rho
                holes = {h: h for h in H}; cells = {i: i for i in C}  # label -> current row
                x = l; t = 0; last = None
                while x != delta:
                    x = B(x); t += 1
                    Dx = diagram(x)
                    okC &= base <= Dx and all(a + b - 1 <= k + 1 for (a, b) in Dx)
                    holes = {lab: (r % k) + 1 for lab, r in holes.items()}
                    cells = {lab: (r % (k + 1)) + 1 for lab, r in cells.items()}
                    hl = [lab for lab, r in holes.items() if r == 1]; cl = [lab for lab, r in cells.items() if r == 2]
                    if hl and cl:
                        last = (hl[0], cl[0]); del holes[hl[0]]; del cells[cl[0]]
                    Hx = {r for r in range(1, k + 1) if trk(k, r) not in Dx}
                    Cx = {r for r in range(1, k + 2) if trk(k + 1, r) in Dx}
                    okC &= Hx == set(holes.values()) and Cx == set(cells.values())
                okC &= t <= k * k - k
                if last is not None:
                    okC &= t == tau_brute(last[0], last[1], k)
print(f"(C) Steps 10-14 on all {cntC} partitions of R_k, k=2..9:", "OK" if okC else "FAIL")
