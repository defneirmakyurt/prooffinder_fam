# stdlib only. Checks proof.md A.2 (i)-(iii) for every (a,b) with S(a,b) a Young diagram, k = 2..K,
# and the witness orbit (A.3): diagram(B^t(lambda^(k))) = S(a_t,b_t) for t < k^2-k, B^{k^2-k} = delta_k, k=1..K2.
import sys
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
def S(k, a, b):
    D = {(i, j) for i in range(1, k + 1) for j in range(1, k + 1) if i + j - 1 <= k}
    return (D - {(k + 1 - a, a)}) | {(k + 2 - b, b)}
def to_partition(cells):
    # returns partition if cells form a Young diagram (columns = parts), else None
    cols = {}
    for (i, j) in cells: cols.setdefault(j, []).append(i)
    J = sorted(cols)
    if J != list(range(1, len(J) + 1)): return None
    h = []
    for j in J:
        r = sorted(cols[j])
        if r != list(range(1, len(r) + 1)): return None
        h.append(len(r))
    if any(h[i] < h[i + 1] for i in range(len(h) - 1)): return None
    return tuple(h)
def diagram(l):
    return {(i, j) for j, h in enumerate(l, 1) for i in range(1, h + 1)}
K = int(sys.argv[1]); K2 = int(sys.argv[2]); bad = 0; diag_pairs = 0
for k in range(2, K + 1):
    delta = tuple(range(k, 0, -1))
    for a in range(1, k + 1):
        for b in range(1, k + 2):
            mu = to_partition(S(k, a, b))
            if mu is None: continue
            diag_pairs += 1
            s = len(mu); m1 = mu[0]
            if s != k - (a == k) + (b == k + 1) or m1 != k - (a == 1) + (b == 1): bad += 1
            nu = B(mu)
            if not (a == k and b == 1):
                if diagram(nu) != S(k, a % k + 1, b % (k + 1) + 1): bad += 1
            else:
                if nu != delta: bad += 1
for k in range(1, K2 + 1):
    lam = (1,) if k == 1 else tuple([k - 1] + [k + 1 - j for j in range(2, k + 1)] + [1])
    delta = tuple(range(k, 0, -1)); x = lam
    for t in range(k * k - k):
        if x == delta: bad += 1
        if diagram(x) != S(k, 1 + t % k, 1 + (t + k) % (k + 1)): bad += 1
        x = B(x)
    if x != delta: bad += 1
print("A.2 checked for k=2..%d (%d Young-diagram pairs (a,b)); witness orbit k=1..%d; failures: %d" % (K, diag_pairs, K2, bad))
