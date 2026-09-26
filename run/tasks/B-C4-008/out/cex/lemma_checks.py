"""Referee B-C4-008: checks of intermediate claims beyond the exhaustive range (stdlib only, exact integers).
(A) Lemma 7: for k in [4, K7], every (h, x<y) with S(h;x,y) closed: theory-free cycle-entry time of Q(h;x,y)
    equals (k-h)+(m-2)(k-1), m = min offsets; max over the level equals (k-1)(k-3), attained only at Q(1;k-1,k).
(B) Lemma 1/2 on random partitions of n = T_{k-1}+1 for k in [5, KR] (seeded): rho(Y) row list, energy
    identity E(r) = E(lambda), E(B lambda) <= E(lambda), equality iff lambda_1 <= s+1, and Y(B)=rho(Y) then.
Usage: python3 lemma_checks.py K7 KR NRAND"""
import sys, random

def B(lam):
    s = len(lam)
    new = [x - 1 for x in lam if x > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def cycle_entry(lam):
    seen = {}; q = lam; i = 0
    while q not in seen:
        seen[q] = i; q = B(q); i += 1
    return seen[q]

def Erows(a):
    return sum(i * x + x * (x + 1) // 2 for i, x in enumerate(a, 1))

def Ecells(cells):
    return sum(i + j for (i, j) in cells)

def Y(lam):
    return {(i, j) for i, x in enumerate(lam, 1) for j in range(1, x + 1)}

def rho(c):
    i, j = c
    return (i + 1, j - 1) if j >= 2 else (1, i)

def Qrows(k, h, x, y):
    # build the cell set explicitly and test closedness directly (no row-length shortcut)
    cells = {(r, d + 1 - r) for d in range(1, k) for r in range(1, d + 1)}
    cells.remove((h, k - h))                 # <k-1,h>
    cells.add((x, k + 1 - x)); cells.add((y, k + 1 - y))   # <k,x>, <k,y>
    ok = all((i == 1 or (i - 1, j) in cells) and (j == 1 or (i, j - 1) in cells) for (i, j) in cells)
    rows = [sum(1 for (i, j) in cells if i == r) for r in range(1, k + 1)]
    return (tuple(v for v in rows if v > 0) if ok else None)

def lemma7(K7):
    allok = True
    for k in range(4, K7 + 1):
        best = -1; argbest = []
        for h in range(1, k):
            for x in range(1, k + 1):
                for y in range(x + 1, k + 1):
                    closed_pred = x not in (h, h + 1) and y not in (h, h + 1)
                    q = Qrows(k, h, x, y)
                    # Qrows returns None iff the cell set is not closed (checked directly)
                    if (q is not None) != closed_pred:
                        allok = False; print("closedness mismatch", k, h, x, y)
                    if q is None:
                        continue
                    m = min((x - h) % k, (y - h) % k)
                    f = (k - h) + (m - 2) * (k - 1)
                    d = cycle_entry(q)
                    if d != f:
                        allok = False; print("Lemma7 formula FAIL", k, h, x, y, d, f)
                    if d > best:
                        best, argbest = d, [(h, x, y)]
                    elif d == best:
                        argbest.append((h, x, y))
        ok = best == (k - 1) * (k - 3) and argbest == [(1, k - 1, k)]
        allok = allok and ok
        print(f"k={k}: level E_min+1 max d_B={best}, (k-1)(k-3)={(k-1)*(k-3)}, argmax={argbest}, ok={ok}", flush=True)
    return allok

def rand_partition(n, rng):
    # random partition via random composition then sort (not uniform; fine for sanity)
    parts = []
    r = n
    while r > 0:
        p = rng.randint(1, r)
        parts.append(p); r -= p
    return tuple(sorted(parts, reverse=True))

def lemma12(KR, NR):
    rng = random.Random(20260926)
    allok = True; cnt = 0
    for k in range(5, KR + 1):
        n = k * (k - 1) // 2 + 1
        for _ in range(NR):
            lam = rand_partition(n, rng)
            if rng.random() < 0.3:   # bias toward long partitions too
                lam = tuple(sorted([1] * rng.randint(0, n // 2) + list(rand_partition(n - 0, rng)), reverse=True))
                # rebalance sum to n
                while sum(lam) > n:
                    lam = lam[:-1]
                lam = tuple(sorted(list(lam) + [1] * (n - sum(lam)), reverse=True))
            assert sum(lam) == n
            s = len(lam)
            Yl = Y(lam)
            R = {rho(c) for c in Yl}
            rlist = [s] + [x - 1 for x in lam]
            if R != {(i, j) for i, x in enumerate(rlist, 1) for j in range(1, x + 1)}:
                allok = False; print("Lemma1 FAIL", lam)
            if Ecells(R) != Ecells(Yl) or Erows(lam) != Ecells(Yl):
                allok = False; print("energy identity FAIL", lam)
            b = B(lam)
            eq = Erows(b) == Erows(lam)
            if Erows(b) > Erows(lam) or eq != (lam[0] <= s + 1):
                allok = False; print("Lemma2 FAIL", lam)
            if eq and Y(b) != R:
                allok = False; print("Lemma2(c) FAIL", lam)
            cnt += 1
    print(f"Lemma1/2 random checks: {cnt} partitions, k=5..{KR}, ok={allok}")
    return allok

if __name__ == "__main__":
    K7, KR, NR = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    a = lemma7(K7)
    b = lemma12(KR, NR)
    print("ALL OK" if a and b else "SOME CHECK FAILED")
