# S3 (containment order / Akin-Davis comparison) and S5 (in-tree / merge point) checks. Exact, stdlib only.
import sys, time
from small_cases import partitions, B, analyse
from functools import lru_cache
t0 = time.time()

def add_cell(lam):
    lam = list(lam); out = set()
    for i in range(len(lam) + 1):
        prev = lam[i-1] if i > 0 else 10**9
        cur = lam[i] if i < len(lam) else 0
        if cur + 1 <= prev:
            m = lam[:] + ([0] if i == len(lam) else [])
            m[i] += 1
            out.add(tuple(x for x in m if x > 0))
    return out

def contained(a, b):
    return len(a) <= len(b) and all(a[i] <= b[i] for i in range(len(a)))

# Akin-Davis monotonicity: a subset b (Young diagrams, any sizes) => B(a) subset B(b); check n<=14 pairs
bad = 0; pairs = 0
allp = [p for n in range(1, 15) for p in partitions(n)]
for a in allp:
    for b in add_cell(a):
        pairs += 1
        if not contained(B(a), B(b)): bad += 1
print(f"S3 Akin-Davis monotonicity on all (a, a+cell), |a|<=14: {pairs} pairs, violations {bad}")

K = int(sys.argv[1]) if len(sys.argv) > 1 else 7
for k in range(4, K+1):
    Tk = k*(k+1)//2
    Dt, _, _, dT = analyse(Tk)
    # min over supersets beta of size T_k: memoised upward closure
    @lru_cache(maxsize=None)
    def mind(lam):
        if sum(lam) == Tk: return dT[lam]
        return min(mind(b) for b in add_cell(lam))
    bound = k*k - 2*k - 1
    for n in range(Tk - (k-1), Tk):
        D, ext, cyc, d = analyse(n)
        worst = max(mind(l) for l in d)          # the relaxation bound max_lam min_beta d(beta)
        viol = sum(1 for l in d if d[l] > mind(l))  # d(lam) <= min_beta d(beta) should hold for all lam
        fails = [l for l in d if mind(l) > bound]
        tight = sum(1 for l in d if d[l] == mind(l))
        print(f"k={k} n={n} D_B={D} bound={bound} max_lam min_beta d(beta)={worst} "
              f"#lam with min_beta d(beta)>bound={len(fails)} viol(d>min)={viol} #lam with d==min={tight}/{len(d)}"
              + (f" e.g. {fails[:2]}" if fails else ""))
    sys.stdout.flush()
    mind.cache_clear()
print("runtime %.2fs" % (time.time()-t0))
