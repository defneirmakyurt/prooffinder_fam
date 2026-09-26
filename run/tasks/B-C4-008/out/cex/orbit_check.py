"""Referee B-C4-008: theory-free check of d_B(lambda^(k)) (stdlib only, exact integers).
d_B is computed as the cycle-ENTRY time of the rho-shaped orbit: iterate B, record the first index of
each state; at the first repeated state q (first seen at index p) we have d_B = p. No lemma of the proof used.
Also: (1) lambda^(k) built two ways (proof 8.1 row description; target list pattern) must agree and sum to T_{k-1}+1;
(2) the proof's claimed B^{t*}(lambda^(k)) = (k,k-1,k-3,...,2) and B^{t*+1} = gamma_3 = delta_{k-1}+e_3, t* = k^2-4k+2;
(3) the proof's formula B^t = Q(h_t; b_t, b_t+) for 0<=t<=t*, h_t = 1+(t mod (k-1)), b_t = t-1 mod k in {1..k}.
Usage: python3 orbit_check.py KMIN KMAX"""
import sys

def B(lam):
    s = len(lam)
    new = [x - 1 for x in lam if x > 1]
    new.append(s)
    new.sort(reverse=True)
    return tuple(new)

def dB_theory_free(lam):
    seen = {}
    q = lam; i = 0
    while q not in seen:
        seen[q] = i
        q = B(q); i += 1
    return seen[q], i - seen[q]      # (cycle entry time, cycle length)

def lam_rows(k):   # proof 8.1: row1=k-2, rows i=k-i (2<=i<=k-2), row k-1 = 2, row k = 1
    rows = [k - 2] + [k - i for i in range(2, k - 1)] + [2, 1]
    return tuple(rows)

def lam_target(k): # target: (k-2, k-2, k-3, k-4, ..., 3, 2, 2, 1): k-2, then run k-2 down to 2, then 2, 1
    return tuple([k - 2] + list(range(k - 2, 1, -1)) + [2, 1])

def Q(k, h, x, y):  # partition with diagram (delta_{k-1} minus <k-1,h>) + <k,x> + <k,y>, via row lengths
    rows = [k - i for i in range(1, k)] + [0]      # rows 1..k
    r = h; rows[r - 1] -= 1                         # <k-1,h> = (h, k-h)
    for z in (x, y):
        rows[z - 1] += 1                            # <k,z> = (z, k+1-z)
    # validity: must be weakly decreasing and each added cell's column equals new row length
    assert all(rows[a] >= rows[a + 1] for a in range(len(rows) - 1)), (k, h, x, y, rows)
    return tuple(v for v in rows if v > 0)

def check(k):
    n = k * (k - 1) // 2 + 1
    a, b = lam_rows(k), lam_target(k)
    assert a == b and sum(a) == n and len(a) == k and all(a[i] >= a[i + 1] for i in range(k - 1)), k
    d, L = dB_theory_free(a)
    F = (k - 1) * (k - 3)
    tstar = k * k - 4 * k + 2
    mu = a
    for t in range(tstar + 1):
        h = 1 + (t % (k - 1))
        bt = 1 + ((t - 2) % k)
        bp = bt + 1 if bt < k else 1
        assert mu == Q(k, h, bt, bp), (k, t)
        if t < tstar:
            mu = B(mu)
    assert mu == tuple([k, k - 1] + list(range(k - 3, 1, -1))), (k, mu)
    g3 = list(range(k - 1, 0, -1)); g3[2] += 1
    assert B(mu) == tuple(g3)
    return d, L, F

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    bad = 0
    for k in range(kmin, kmax + 1):
        d, L, F = check(k)
        if d != F or L != k:
            bad += 1
            print(f"MISMATCH k={k}: d_B={d} cycle_len={L} F={F}")
        elif k <= 12 or k % 25 == 0:
            print(f"k={k}: d_B(lambda^(k))={d} = (k-1)(k-3)={F}; cycle length {L} = k", flush=True)
    print(f"k={kmin}..{kmax}: {'ALL MATCH' if bad == 0 else str(bad) + ' MISMATCHES'}")
