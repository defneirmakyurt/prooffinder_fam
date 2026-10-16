"""Counterexample search for A-C2 (pure stdlib floating point; exploration only, confirms nothing).
Admissible chain <=> unit-diagonal tridiagonal Gram G (off-diag c_i) PSD of rank <= m-1.
Flipping x_i -> -x_i flips signs, so WLOG G = I - tA(w), A path adjacency with weights w_i>=0.
PSD & singular <=> t = 1/lambda_max(A(w)).  lambda_max found by bisection with LDL pivots
(I - tA PD iff all pivots r_1=1, r_{k+1}=1-(t w_k)^2/r_k are > 0).
Objective gap(w) = sum arcsin(t w_i) - pi/2 ; target <=> gap >= 0.
"""
import math, random

def pd(t, w):
    r = 1.0
    for x in w:
        r = 1.0 - (t*x)**2 / r
        if r <= 0: return False
    return True

def tstar(w):
    lo, hi = 0.0, 1.0/max(w)   # t*max(w)<=1 is necessary for PSD
    if pd(hi, w): return hi    # cannot happen unless all but a 1x1... kept for safety
    for _ in range(200):
        mid = (lo+hi)/2
        if pd(mid, w): lo = mid
        else: hi = mid
    return lo

def gap(w):
    w = [abs(x) for x in w]
    if max(w) == 0: return 10.0
    t = tstar(w)
    return sum(math.asin(min(1.0, t*x)) for x in w) - math.pi/2, [t*x for x in w]

def g(w): return gap(w)[0]

def local(w, rng, iters=3000):
    f = g(w); step = 0.3
    for _ in range(iters):
        v = [max(0.0, x + step*rng.gauss(0,1)) for x in w]
        if max(v)==0: continue
        fv = g(v)
        if fv < f: f, w = fv, v
        else: step *= 0.995
        if step < 1e-9: break
    return f, w

log = open('log.txt', 'w')
def P(*s):
    print(*s); print(*s, file=log); log.flush()

best = (1e9, None)
for m in range(2, 61):                       # R3
    f, a = gap([1.0]*(m-1))
    P(f"R3 equal m={m} a={a[0]:.10f} gap={f:.12f}")
rng = random.Random(12345)                   # R4
for m in range(2, 13):
    mn, arg = 1e9, None
    for _ in range(20000):
        k = rng.randrange(3)
        if k == 0: w = [rng.random() for _ in range(m-1)]
        elif k == 1: w = [rng.random()**6 for _ in range(m-1)]
        else: w = [rng.random() if rng.random() < 0.4 else 0.0 for _ in range(m-1)]
        if max(w) == 0: continue
        f, a = gap(w)
        if f < mn: mn, arg = f, a
    P(f"R4 random m={m} n=20000 min gap={mn:.3e} at a={[round(x,6) for x in arg]}")
    if mn < best[0]: best = (mn, ('R4', m, arg))
rng = random.Random(777)                     # R5
for m in range(3, 11):
    mn, arg = 1e9, None
    for _ in range(200):
        f, w = local([rng.random() for _ in range(m-1)], rng)
        if f < mn: mn, arg = f, gap(w)[1]
    P(f"R5 localopt m={m} restarts=200 min gap={mn:.3e} at a={[round(x,6) for x in arg]}")
    if mn < best[0]: best = (mn, ('R5', m, arg))
P("OVERALL min gap (float):", best)
