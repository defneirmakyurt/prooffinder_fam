"""Referee B-C4-008: independent exhaustive check (stdlib only, exact integer arithmetic).
For each k in [KMIN, KMAX], n = T_{k-1}+1:
  - enumerate ALL partitions of n, build B, find cyclic points as points on cycles (no theory),
  - compute d_B for every partition (cycle-ENTRY time), D_B(n), and ALL maximisers,
  - compare D_B with F(k)=(k-1)(k-3) and check lambda^(k) is a maximiser with d_B = F(k),
  - check Lemma 2 (E(B l) <= E(l); equality iff l_1 <= s+1) on every partition,
  - check Lemma 5(a): E >= E_min with equality iff cyclic,
  - check Lemma 5(b)/6(a): level E_min+1 = {closed S(h;x,y)}, closed iff x,y not in {h,h+1},
  - check Lemma 7 formula d_B(Q(h0;x,y)) = (k-h0)+(m-2)(k-1) on every level-(E_min+1) partition.
Usage: python3 exhaustive_check.py KMIN KMAX"""
import sys

def partitions(n):
    # iterative generation of partitions in reverse-lex order
    a = [n]
    while True:
        yield tuple(a)
        # find rightmost part > 1
        rem = 0
        while a and a[-1] == 1:
            a.pop(); rem += 1
        if not a:
            return
        x = a.pop() - 1
        rem += 1
        a.append(x)
        while rem > x:
            a.append(x); rem -= x
        if rem:
            a.append(rem)

def B(lam):
    s = len(lam)
    new = [x - 1 for x in lam if x > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def energy(lam):
    return sum(i * x + x * (x + 1) // 2 for i, x in enumerate(lam, 1))

def cell(d, r):
    return (r, d + 1 - r)

def from_cells(cells):
    rows = {}
    for (i, j) in cells:
        rows[i] = rows.get(i, 0) + 1
    R = max(rows)
    lam = tuple(rows.get(i, 0) for i in range(1, R + 1))
    closed = all(((i == 1) or ((i - 1, j) in cells)) and ((j == 1) or ((i, j - 1) in cells)) for (i, j) in cells)
    return lam, closed

def S_set(k, h, x, y):
    cells = set(cell(d, r) for d in range(1, k) for r in range(1, d + 1))
    cells.remove(cell(k - 1, h))
    cells.add(cell(k, x)); cells.add(cell(k, y))
    return cells

def lam_k(k):
    # row description of proof 8.1 / target: (k-2), then k-2, k-3, ..., 2 (rows 2..k-2), then 2, 1
    return tuple([k - 2] + list(range(k - 2, 1, -1)) + [2, 1])

def run(k):
    n = k * (k - 1) // 2 + 1
    P = list(partitions(n))
    assert len(set(P)) == len(P)
    nxt = {p: B(p) for p in P}
    # cyclic points: points on cycles of functional graph
    color = {}
    cyclic = set()
    for p in P:
        if p in color:
            continue
        path = []; idx = {}
        q = p
        while q not in color and q not in idx:
            idx[q] = len(path); path.append(q); q = nxt[q]
        if q in idx:
            cyclic.update(path[idx[q]:])
        for r in path:
            color[r] = 1
    d = {p: 0 for p in cyclic}
    for p in P:
        st = []; q = p
        while q not in d:
            st.append(q); q = nxt[q]
        v = d[q]
        while st:
            v += 1; d[st.pop()] = v
    D = max(d.values())
    maxim = sorted([p for p in P if d[p] == D], reverse=True)
    F = (k - 1) * (k - 3)
    lk = lam_k(k)
    ok = True
    # Lemma 2
    for p in P:
        e0, e1 = energy(p), energy(nxt[p])
        if e1 > e0: ok = False; print("Lemma2(a) FAIL", p)
        if (e1 == e0) != (p[0] <= len(p) + 1): ok = False; print("Lemma2(b) FAIL", p)
    # Lemma 5(a)
    delta = list(range(k - 1, 0, -1))
    gam = []
    for j in range(k):
        mu = delta + [0]; mu[j] += 1
        gam.append(tuple(x for x in mu if x > 0))
    Emin = energy(gam[0])
    for p in P:
        e = energy(p)
        if e < Emin: ok = False; print("Lemma5(a) FAIL <", p)
        if (e == Emin) != (p in cyclic): ok = False; print("Lemma5(a) FAIL eq", p)
    if set(gam) != cyclic: ok = False; print("cyclic set FAIL")
    # Lemma 5(b)/6(a)/7
    level1 = set(p for p in P if energy(p) == Emin + 1)
    closedS = {}
    for h in range(1, k):
        for x in range(1, k + 1):
            for y in range(x + 1, k + 1):
                lam, cl = from_cells(S_set(k, h, x, y))
                if cl != (x not in (h, h + 1) and y not in (h, h + 1)):
                    ok = False; print("Lemma6(a) FAIL", h, x, y)
                if cl:
                    closedS[lam] = (h, x, y)
    if set(closedS) != level1: ok = False; print("Lemma5(b) FAIL")
    for lam, (h, x, y) in closedS.items():
        ox, oy = (x - h) % k, (y - h) % k
        m = min(ox, oy)
        if d[lam] != (k - h) + (m - 2) * (k - 1):
            ok = False; print("Lemma7 FAIL", lam, h, x, y, d[lam])
    print(f"k={k} n={n} #P={len(P)} D_B={D} F={F} D_B==F:{D == F} "
          f"d_B(lambda^(k)={lk})={d.get(lk)} sum={sum(lk)} #maximisers={len(maxim)} "
          f"maximisers={maxim if len(maxim) <= 12 else (maxim[:3] + ['...'])} lambda^(k)_is_maximiser={lk in maxim} level1_size={len(level1)} lemmas_ok={ok}", flush=True)
    return ok and D == F and d.get(lk) == F

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    allok = True
    for k in range(kmin, kmax + 1):
        allok = run(k) and allok
    print("ALL OK" if allok else "SOME CHECK FAILED")
