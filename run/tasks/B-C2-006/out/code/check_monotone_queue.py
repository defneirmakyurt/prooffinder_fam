"""Sanity check (stdlib only, exact integers) of two lemmas proved by hand in proof.md:
 (M) lambda subset mu (diagrams)  =>  B(lambda) subset B(mu), for all partitions of sizes <= NMAX;
 (Q) conjugate formula (B lambda)'_j = lambda'_{j+1} + [j <= lambda'_1].
Not relied upon by the proof (both lemmas are proved in writing); it only guards against slips.
Usage: python3 check_monotone_queue.py NMAX
"""
import sys
def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for p in range(min(n, maxp), 0, -1):
        for r in partitions(n - p, p): yield (p,) + r
def B(l):
    s = len(l); return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def conj(l):
    return tuple(sum(1 for x in l if x >= j) for j in range(1, (l[0] if l else 0) + 1))
def sub(a, b):
    return len(a) <= len(b) and all(a[i] <= b[i] for i in range(len(a)))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 14
allp = [p for n in range(1, N + 1) for p in partitions(n)]
imgs = {p: B(p) for p in allp}
cntQ = 0
for p in allp:
    c = conj(p); cb = conj(imgs[p]); L = max(len(cb), len(c)) + 2
    cc = list(c) + [0] * (L + 2)
    pred = [cc[j] + (1 if j <= c[0] else 0) for j in range(1, L + 1)]  # j is 1-based: cc[j] = lambda'_{j+1}
    while pred and pred[-1] == 0: pred.pop()
    assert tuple(pred) == cb, (p, pred, cb); cntQ += 1
cntM = 0
for a in allp:
    for b in allp:
        if sum(a) <= sum(b) and sub(a, b):
            assert sub(imgs[a], imgs[b]), (a, b); cntM += 1
print(f"NMAX={N}: (Q) checked on {cntQ} partitions, (M) checked on {cntM} comparable pairs: OK")
