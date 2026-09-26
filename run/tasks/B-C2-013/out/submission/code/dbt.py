# stdlib only: exhaustive D_B(T_k) for small k, list maximisers
import sys
def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for a in range(min(n, m), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest
def B(l):
    s = len(l)
    return tuple(sorted([x - 1 for x in l if x > 1] + [s], reverse=True))
def run(k):
    n = k*(k+1)//2
    delta = tuple(range(k, 0, -1))
    best = -1; arg = []
    for l in partitions(n):
        d = 0; x = l
        while x != delta:
            x = B(x); d += 1
        if d > best: best, arg = d, [l]
        elif d == best: arg.append(l)
    return best, arg
K = int(sys.argv[1])
for k in range(1, K+1):
    b, a = run(k)
    print(k, "T_k=", k*(k+1)//2, "D_B=", b, "k^2-k=", k*k-k, "#max=", len(a), a[:6])
