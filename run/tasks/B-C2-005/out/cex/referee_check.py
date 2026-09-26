"""Referee B-C2-005: independent exact checks (stdlib only, integer arithmetic).
Usage: python3 referee_check.py KEXH KWIT KTAU
  A. exhaustive, k=1..KEXH: all partitions of T_k (recursive generator, count checked vs Euler pentagonal recurrence);
     functional graph of B: set of cyclic partitions == {delta_k}; D_B(T_k)=max d_B vs k^2-k; list maximisers (k<=6).
  B. witness, k=1..KWIT: direct simulation of B on lambda^(k); first i with B^i = delta_k is k^2-k and
     every earlier state != delta_k; for k<=40 also: every state lies in R_k with |H|=|C|=1 until the end (Steps 12,15).
  C. Step 12 track rule, k=2..min(KEXH,10): for every lambda in R_k (from exhaustive list or constructed from (H,C)),
     B(lambda) computed directly equals the track-rule prediction.
  D. Step 13, k=2..KTAU: for all (h,i) with i-h not in {0,1}: brute-force tau == k*x0+1-h, <= k^2-k, equality iff (1,k+1);
     for k<=25 also build the partition with H={h}, C={i} and check d_B == tau by simulation.
  E. statement example and traps: B(2,1,1,1,1)=(5,1)->(4,2)->(3,2,1), d_B=3; (n) and (1^n) handled.
"""
import sys

def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))

def parts_rec(n, maxp):
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for rest in parts_rec(n - p, p):
            yield (p,) + rest

def p_euler(n):
    p = [1] + [0] * n
    for m in range(1, n + 1):
        s, j = 0, 1
        while True:
            g1 = j * (3 * j - 1) // 2
            if g1 > m: break
            sign = 1 if j % 2 == 1 else -1
            s += sign * p[m - g1]
            g2 = j * (3 * j + 1) // 2
            if g2 <= m: s += sign * p[m - g2]
            j += 1
        p[m] = s
    return p[n]

def T(k): return k * (k + 1) // 2
def delta(k): return tuple(range(k, 0, -1))
def witness(k): return (1,) if k == 1 else tuple([k - 1] + list(range(k - 1, 0, -1)) + [1])

def diagram(l): return {(i + 1, j + 1) for i, x in enumerate(l) for j in range(x)}
def from_diagram(D):
    rows = {}
    for (i, j) in D: rows[i] = rows.get(i, 0) + 1
    return tuple(rows[i] for i in range(1, len(rows) + 1))

def HC(l, k):
    """return (H,C) if l in R_k else None"""
    D = diagram(l)
    for (i, j) in D:
        if i + j - 1 >= k + 2: return None
    for d in range(1, k):
        for r in range(1, d + 1):
            if (r, d + 1 - r) not in D: return None
    H = frozenset(r for r in range(1, k + 1) if (r, k + 1 - r) not in D)
    C = frozenset(r for r in range(1, k + 2) if (r, k + 2 - r) in D)
    return H, C

def build(k, H, C):
    D = {(i, j) for i in range(1, k + 1) for j in range(1, k + 1) if i + j - 1 <= k}
    for h in H: D.discard((h, k + 1 - h))
    for c in C: D.add((c, k + 2 - c))
    return from_diagram(D)

def track_rule(k, H, C):
    sk = lambda r: r + 1 if r < k else 1
    sk1 = lambda r: r + 1 if r < k + 1 else 1
    H2 = {sk(h) for h in H}; C2 = {sk1(c) for c in C}
    if 1 in H2 and 2 in C2:
        H2.discard(1); C2.discard(2)
    return frozenset(H2), frozenset(C2)

def partA(KEXH, log):
    ok = True
    allparts = {}
    for k in range(1, KEXH + 1):
        n = T(k)
        P = list(parts_rec(n, n))
        assert len(P) == len(set(P)) == p_euler(n), "enumeration incomplete"
        for l in P:
            assert sum(l) == n and all(l[a] >= l[a + 1] for a in range(len(l) - 1)) and l[-1] >= 1
        Pset = set(P)
        succ = {l: B(l) for l in P}
        assert all(succ[l] in Pset for l in P)
        # cyclic nodes: iterate image |P| times -> only cyclic remain
        cur = set(P)
        while True:
            nxt = {succ[x] for x in cur}
            if nxt == cur: break
            cur = nxt
        cyc_ok = (cur == {delta(k)})
        # d_B by memo: 0 on cyclic
        d = {x: 0 for x in cur}
        for l in P:
            path = []
            x = l
            while x not in d:
                path.append(x); x = succ[x]
            v = d[x]
            for y in reversed(path):
                v += 1; d[y] = v
        best = max(d[l] for l in P)
        maxim = sorted(l for l in P if d[l] == best)
        dw = d[witness(k)]
        good = cyc_ok and best == k * k - k and dw == k * k - k and witness(k) in maxim
        ok &= good
        msg = (f"A k={k} T_k={n} p(T_k)={len(P)} cyclic={sorted(cur)} D_B={best} k^2-k={k*k-k} "
               f"d_B(witness)={dw} #maximisers={len(maxim)} {'OK' if good else 'FAIL'}")
        if k <= 6: msg += f" maximisers={maxim}"
        print(msg, file=log)
        # extremal starts named in S3
        print(f"   d_B((n))={d[(n,)]}  d_B((1^n))={d[tuple([1]*n)]}", file=log)
        if k + 1 <= 12: allparts[k] = (P, d)
    return ok, allparts

def partB(KWIT, log):
    ok = True
    for k in range(1, KWIT + 1):
        x = witness(k); dk = delta(k); t = 0
        assert sum(x) == T(k)
        good = True
        while x != dk:
            if k <= 40:
                hc = HC(x, k)
                if hc is None or len(hc[0]) != 1 or len(hc[1]) != 1: good = False; break
            x = B(x); t += 1
            if t > k * k + 5: good = False; break
        good = good and t == k * k - k
        ok &= good
        if not good or k <= 5 or k % 50 == 0:
            print(f"B k={k} first i with B^i(witness)=delta_k : {t}  k^2-k={k*k-k} {'OK' if good else 'FAIL'}", file=log)
    print(f"B witness k=1..{KWIT}: {'ALL OK' if ok else 'FAILURE'}", file=log)
    return ok

def partC(KC, allparts, log):
    ok = True
    from itertools import combinations
    for k in range(2, KC + 1):
        # enumerate R_k from (H,C) with |H|=|C| and Young constraint, cross-check with exhaustive list if present
        Rk = set()
        for m in range(0, k + 1):
            for H in combinations(range(1, k + 1), m):
                for C in combinations(range(1, k + 2), m):
                    if all((c not in H) and (c - 1 not in H) for c in C):
                        Rk.add(build(k, frozenset(H), frozenset(C)))
        if k in allparts:
            P, _ = allparts[k]
            Rk2 = {l for l in P if HC(l, k) is not None}
            if Rk2 != Rk: ok = False; print(f"C k={k} R_k mismatch", file=log)
        cnt = 0
        for l in Rk:
            assert sum(l) == T(k)
            H, C = HC(l, k)
            b = B(l)
            hc = HC(b, k)
            if hc is None or hc != track_rule(k, H, C): ok = False; print(f"C k={k} rule fails at {l}", file=log)
            cnt += 1
        print(f"C k={k} |R_k|={cnt} Step-12 track rule verified on all of R_k", file=log)
    return ok

def partD(KTAU, log):
    ok = True
    for k in range(2, KTAU + 1):
        worst, arg = -1, []
        for h in range(1, k + 1):
            for i in range(1, k + 2):
                if i - h in (0, 1): continue
                tb = next(t for t in range(1, k * (k + 1) + 1) if (h + t - 1) % k == 0 and (i + t - 2) % (k + 1) == 0)
                x0 = (i - h - 1) % (k + 1)
                if tb != k * x0 + 1 - h or tb > k * k - k: ok = False; print(f"D k={k} h={h} i={i} tau={tb} formula={k*x0+1-h}", file=log)
                if tb > worst: worst, arg = tb, [(h, i)]
                elif tb == worst: arg.append((h, i))
                if k <= 25:
                    l = build(k, {h}, {i}); x = l; t = 0
                    while x != delta(k): x = B(x); t += 1
                    if t != tb: ok = False; print(f"D sim k={k} h={h} i={i} d_B={t} tau={tb}", file=log)
        if worst != k * k - k or arg != [(1, k + 1)]: ok = False
        if k <= 6 or k % 10 == 0 or worst != k*k-k:
            print(f"D k={k} max tau={worst} at {arg} (k^2-k={k*k-k})", file=log)
    print(f"D tau formula k=2..{KTAU} (+simulation k<=25): {'ALL OK' if ok else 'FAILURE'}", file=log)
    return ok

def partE(log):
    s = [(2, 1, 1, 1, 1)]
    for _ in range(4): s.append(B(s[-1]))
    good = s == [(2,1,1,1,1), (5,1), (4,2), (3,2,1), (3,2,1)]
    print(f"E statement example orbit {s} {'OK' if good else 'FAIL'}", file=log)
    return good

if __name__ == "__main__":
    KEXH, KWIT, KTAU = (int(a) for a in sys.argv[1:4])
    log = sys.stdout
    okA, allparts = partA(KEXH, log)
    okB = partB(KWIT, log)
    okC = partC(max(2, min(KEXH, 10)), allparts, log)
    okD = partD(KTAU, log)
    okE = partE(log)
    print("SUMMARY", dict(A=okA, B=okB, C=okC, D=okD, E=okE))
    sys.exit(0 if all([okA, okB, okC, okD, okE]) else 1)
