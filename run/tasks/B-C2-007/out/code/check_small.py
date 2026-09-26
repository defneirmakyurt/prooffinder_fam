"""Stdlib-only, exact integer computation (evidence only, not a proof step).
(1) For k = 1..K: computes D_B(T_k) = max d_B(lambda) over all partitions of T_k.
(2) For k = 1..K: checks Lemma 3 (containment monotonicity) on all pairs lambda <= mu obtained by
    removing one corner cell (lambda = mu minus a corner), mu a partition of T_k.
(3) For k = 2..K: checks Lemma 6 (the e-vector description of B on the two-track region)
    on every e in {-1,0,1}^{k+1} satisfying the admissibility conditions."""
import sys, itertools
def parts(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for p in range(min(n, maxp), 0, -1):
        for rest in parts(n - p, p):
            yield (p,) + rest
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def contained(a, b):
    return len(a) <= len(b) and all(a[i] <= b[i] for i in range(len(a)))
def from_e(e, k):
    rows = [k + 1 - i + e[i - 1] for i in range(1, k + 2)]
    return tuple(r for r in rows if r > 0)
def admissible(e, k):
    if e[k] == -1 or sum(e) != 0: return False
    return all(not (e[i] == -1 and e[i + 1] == 1) for i in range(k))
def step_e(e, k):
    # Lemma 6 rule
    first = (1 if e[k] == 1 else 0) - (1 if e[k - 1] == -1 else 0)
    new = [first] + list(e[:k - 1]) + [1 if e[k - 1] == 1 else 0]
    if new[0] == -1 and new[1] == 1:
        new[0] = 0; new[1] = 0
    return tuple(new)
K = int(sys.argv[1])
for k in range(1, K + 1):
    n = k * (k + 1) // 2
    dk = tuple(range(k, 0, -1))
    d = {dk: 0}
    P = list(parts(n))
    for l in P:
        path = []
        x = l
        while x not in d:
            path.append(x); x = B(x)
        v = d[x]
        for y in reversed(path):
            v += 1; d[y] = v
    D = max(d[l] for l in P)
    # monotonicity check on corner removals
    bad = 0
    for mu in P:
        for i in range(len(mu)):
            if i == len(mu) - 1 or mu[i] > mu[i + 1]:
                lam = list(mu); lam[i] -= 1
                lam = tuple(x for x in lam if x > 0)
                if not contained(B(lam), B(mu)): bad += 1
    # e-vector lemma
    ebad = 0; ecount = 0
    if k >= 2:
        for e in itertools.product((-1, 0, 1), repeat=k + 1):
            if not admissible(e, k): continue
            ecount += 1
            lam = from_e(e, k)
            if sum(lam) != n or list(lam) != sorted(lam, reverse=True): ebad += 1; continue
            e2 = step_e(e, k)
            if not admissible(e2, k) or from_e(e2, k) != B(lam): ebad += 1
    print(f"k={k} T_k={n} #partitions={len(P)} D_B(T_k)={D} k^2-k={k*k-k} "
          f"monotonicity_failures={bad} twotrack_configs={ecount} lemma6_failures={ebad}")
