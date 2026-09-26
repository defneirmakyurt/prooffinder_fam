# Translation checks for the space cards. Exact integer arithmetic, stdlib only.
import sys, time
from small_cases import partitions, B, analyse

def d_direct(lam):
    """exact d_B by simulation: first index whose state lies on the eventual cycle"""
    seen = {}; seq = []; x = lam; i = 0
    while x not in seen:
        seen[x] = i; seq.append(x); x = B(x); i += 1
    return seen[x]  # first state of cycle = index where the cycle starts

# ---- S1: Griggs-Ho / Etienne diagonal array: cell (i,j), 0-indexed row i (part index), column j (height)
def cells(lam):  # cell (a,b): a = part index, b = level inside part; diagonal a+b
    return {(a, b) for a, p in enumerate(lam) for b in range(p)}
def array_shift(lam):
    # Step 1: rotate every diagonal: cell (a,b) with b>=1 -> (a+1, b-1); cell (a,0) -> (0, a)
    C = cells(lam)
    new = set()
    for (a, b) in C:
        new.add((a+1, b-1) if b >= 1 else (0, a))
    # Step 2 (left shift): columns = parts; collect column sizes, drop empty ones, re-sort
    cols = {}
    for (a, b) in new: cols[a] = cols.get(a, 0) + 1
    return tuple(sorted(cols.values(), reverse=True)), new
def energy(lam):
    return sum(a + b for (a, b) in cells(lam))

# ---- S2: Griggs-Ho sequence seq_B = (c_1, c_2, ...), c_i = #parts of B^{i-1}(lam)
def seqB(lam, L):
    out = []; x = lam
    for _ in range(L): out.append(len(x)); x = B(x)
    return out
def recover_from_seq(c, n):
    # conjugate: lam'_{i+1} = c_{i+1} - #{m<=i : c_m >= i-m+1}  (0-indexed below)
    conj = []
    for i in range(len(c)):
        v = c[i] - sum(1 for m in range(i) if c[m] >= i - m)
        if v <= 0: break
        conj.append(v)
    # conjugate back
    if not conj: return ()
    return tuple(sum(1 for v in conj if v > j) for j in range(conj[0]))

if __name__ == "__main__":
    t0 = time.time()
    N = 22
    ok1 = ok2 = ok3 = True; cnt = 0
    for n in range(1, N+1):
        for lam in partitions(n):
            cnt += 1
            b, _ = array_shift(lam)
            if b != B(lam): ok1 = False; print("S1 FAIL", lam)
            if energy(B(lam)) > energy(lam): ok3 = False; print("energy increase", lam)
            c = seqB(lam, n + 2)
            if recover_from_seq(c, n) != lam: ok2 = False; print("S2 FAIL", lam, c)
    print(f"S1 array-shift == B on all {cnt} partitions n<=%d: {ok1}" % N)
    print(f"S1 energy (sum of diagonal indices) non-increasing, n<=%d: {ok3}" % N)
    print(f"S2 seq_B determines lambda (recovery formula) n<=%d: {ok2}" % N)
    # Griggs-Ho Prop 3.2(1),(2) on n<=22
    bad = 0
    for n in range(3, N+1):
        k = 1
        while k*(k+1)//2 < n: k += 1
        r = n - (k-1)*k//2
        for lam in partitions(n):
            c = seqB(lam, 3*n)
            if any(c[i+1] > c[i] + 1 for i in range(len(c)-1)): bad += 1
            if any(sum(c[i:i+k]) > k*(k-1) + r for i in range(len(c)-k)): bad += 1
    print("S2 Prop 3.2(1),(2) violations n in [3,%d]:" % N, bad)
    # Griggs-Ho explicit extremizer for T_k - 1
    for k in range(4, 16):
        lam = tuple([k-1, k-2] + [k-i+1 for i in range(3, k+1)] + [1])
        assert sum(lam) == k*(k+1)//2 - 1
        print(f"k={k} GH lambda={lam} d_B={d_direct(lam)} k^2-2k-1={k*k-2*k-1}")
    print("runtime %.2fs" % (time.time()-t0))
