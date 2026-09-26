"""Exact exhaustive check (stdlib only, integer arithmetic).
For each k in [KMIN, KMAX]:
  * enumerates ALL partitions of T_k = k(k+1)/2,
  * computes d_B(lambda) = first i with B^i(lambda) = delta_k, and checks along the way that
    the orbit reaches delta_k (so delta_k is the only cyclic partition met; a cycle avoiding
    delta_k would be detected by a visited-set and reported),
  * reports D_B(T_k) = max d_B, compares with k^2 - k,
  * checks the witness lambda^(k) = (k-1,k-1,k-2,...,2,1,1) (k>=2), (1) (k=1) has d_B = k^2-k,
  * checks the two-track lemma: every partition with delta_{k-1} <= lambda <= delta_{k+1} has d_B <= k^2-k.
Usage: python3 check_DB_triangular.py KMIN KMAX
"""
import sys

def partitions(n):
    # iterative generation of partitions of n in reverse-lex order, as tuples
    a = [n]
    while True:
        yield tuple(a)
        # find rightmost part > 1
        i = len(a) - 1
        while i >= 0 and a[i] == 1:
            i -= 1
        if i < 0:
            return
        rem = len(a) - i  # a[i] plus the ones after it
        v = a[i] - 1
        del a[i:]
        rem_total = v + rem  # total to redistribute: (a[i]) + (#ones) = v+1 + (rem-1)
        while rem_total > 0:
            p = min(v, rem_total)
            a.append(p)
            rem_total -= p

def partition_count(n):
    # independent count p(n) by the standard DP over largest allowed part
    c = [1] + [0] * n
    for part in range(1, n + 1):
        for m in range(part, n + 1):
            c[m] += c[m - part]
    return c[n]

def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))

def in_two_track(l, k):
    # delta_{k-1} subset of D(l) subset of delta_{k+1}
    if len(l) < k - 1 or len(l) > k + 1:
        return False
    for i in range(k - 1):
        if l[i] < k - 1 - i:
            return False
    for i, x in enumerate(l):
        if x > k + 1 - i:
            return False
    return True

def main(kmin, kmax):
    ok_all = True
    for k in range(kmin, kmax + 1):
        n = k * (k + 1) // 2
        delta = tuple(range(k, 0, -1))
        assert B(delta) == delta
        memo = {delta: 0}
        best = -1
        count = 0
        two_track_max = -1
        for l in partitions(n):
            assert sum(l) == n and all(l[i] >= l[i + 1] for i in range(len(l) - 1)) and l[-1] >= 1
            count += 1
            path = []
            seen = set()
            x = l
            while x not in memo:
                if x in seen:
                    print("CYCLE AVOIDING delta_k FOUND from", l)
                    return False
                seen.add(x)
                path.append(x)
                x = B(x)
            d = memo[x]
            for y in reversed(path):
                d += 1
                memo[y] = d
            dl = memo[l]
            best = max(best, dl)
            if in_two_track(l, k):
                two_track_max = max(two_track_max, dl)
        assert count == partition_count(n), "enumeration incomplete"
        wit = (1,) if k == 1 else tuple([k - 1] + list(range(k - 1, 0, -1)) + [1])
        assert sum(wit) == n
        dw = memo[wit]
        ok = (best == k * k - k) and (dw == k * k - k) and (two_track_max <= k * k - k)
        ok_all &= ok
        print(f"k={k} T_k={n} #partitions={count} D_B(T_k)={best} k^2-k={k*k-k} "
              f"d_B(witness)={dw} max d_B on two-track region={two_track_max} {'OK' if ok else 'FAIL'}")
        del memo
    print("ALL OK" if ok_all else "SOME FAILURE")
    return ok_all

if __name__ == "__main__":
    kmin = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 9
    sys.exit(0 if main(kmin, kmax) else 1)
