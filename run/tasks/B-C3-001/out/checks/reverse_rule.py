# S5: check the Eriksson-Jonsson reversed move (delete row i, add it as leftmost column; legal iff lambda_i >= N-1,
# N = number of rows after deletion) generates exactly B^{-1}(mu), all mu |- n, n<=22. Exact, stdlib only.
import time
from collections import defaultdict
from small_cases import partitions, B
t0 = time.time()
def rev(mu):
    out = set()
    for i in range(len(mu)):
        rest = list(mu[:i] + mu[i+1:]); c = mu[i]; N = len(rest)
        if c >= N:  # new column of height c needs c >= #remaining rows: parts = rest+1 (N of them) and c-N ones
            lam = tuple(sorted([x + 1 for x in rest] + [1] * (c - N), reverse=True))
            out.add(lam)
    return out
bad = 0; tot = 0
for n in range(1, 23):
    pre = defaultdict(set)
    for l in partitions(n): pre[B(l)].add(l)
    for mu in partitions(n):
        tot += 1
        if rev(mu) != pre[mu]: bad += 1
print(f"reversed-move rule (legal iff mu_i >= #other rows) == B^-1 on {tot} partitions, n<=22: mismatches {bad}")
print("runtime %.2fs" % (time.time()-t0))
