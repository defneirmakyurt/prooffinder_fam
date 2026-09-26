# stdlib only: check Part A (witness orbit) for k = 1..K
import sys
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def diagram(l):
    return {(i, j) for j, h in enumerate(l, 1) for i in range(1, h + 1)}
def S(k, a, b):
    D = {(i, j) for i in range(1, k + 1) for j in range(1, k + 1) if i + j - 1 <= k}
    return (D - {(k + 1 - a, a)}) | {(k + 2 - b, b)}
K = int(sys.argv[1]); bad = 0
for k in range(1, K + 1):
    lam = (1,) if k == 1 else tuple([k - 1] + [k + 1 - j for j in range(2, k + 1)] + [1])
    assert sum(lam) == k * (k + 1) // 2
    delta = tuple(range(k, 0, -1)); x = lam; t = 0
    while x != delta:
        if k >= 2 and diagram(x) != S(k, 1 + t % k, 1 + (t + k) % (k + 1)): bad += 1
        x = B(x); t += 1
    if t != k * k - k: bad += 1
print("k=1..%d checked, failures:" % K, bad)
