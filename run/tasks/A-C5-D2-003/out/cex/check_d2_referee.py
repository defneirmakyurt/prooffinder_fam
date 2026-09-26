"""
Independent referee sanity check for A-C5-D2 (4 lines through the origin of R^2, S <= 2*pi).

Uses mpmath at 50 decimal digits of precision (not exact rational, but far beyond any
floating-point rounding concern for this purpose; used only as a numerical sanity check,
not as a substitute for the written proof).

Three things are checked:
 (1) Direct computation of S from 4 random line-angles (via arccos|cos(phi_i-phi_j)|)
     agrees with the proof's gap-based formula F(g1,g2,g3,g4), for many random and
     degenerate (repeated-line) configurations.
 (2) Random search (large sample) plus a fine grid search for any configuration with
     S > 2*pi (a counterexample to the target statement).
 (3) The two claimed equality configurations (doubled orthogonal axes; four evenly spaced
     lines) reproduce S = 2*pi exactly (to working precision), and a local perturbation
     search around them does not find S > 2*pi.
"""
import mpmath as mp
import random

mp.mp.dps = 50

def theta(phi_i, phi_j):
    # acute angle between lines at angles phi_i, phi_j (any reals, since arccos|cos(.)| is
    # automatically pi-periodic and reflection symmetric)
    return mp.acos(abs(mp.cos(phi_i - phi_j)))

def S_direct(phis):
    n = len(phis)
    total = mp.mpf(0)
    for i in range(n):
        for j in range(i+1, n):
            total += theta(phis[i], phis[j])
    return total

def h(x):
    return min(x, mp.pi - x)

def F_from_gaps(g):
    g1, g2, g3, g4 = g
    return h(g1) + h(g2) + h(g3) + h(g4) + h(g1+g2) + h(g2+g3)

def gaps_from_phis(phis):
    # representatives of phi mod pi in [0, pi)
    reps = sorted([ph % mp.pi for ph in phis])
    p1, p2, p3, p4 = reps
    g1 = p2 - p1
    g2 = p3 - p2
    g3 = p4 - p3
    g4 = mp.pi - p4 + p1
    return (g1, g2, g3, g4)

random.seed(42)
two_pi = 2 * mp.pi

max_S = mp.mpf(0)
worst = None
mismatches = 0
N_RANDOM = 20000

# (1)+(2) random search, including degenerate (repeated-angle) configurations
for trial in range(N_RANDOM):
    if trial % 5 == 0:
        # force some repeats / degenerate configs
        base = [mp.mpf(random.uniform(0, 1)) * mp.pi for _ in range(2)]
        phis = [random.choice(base) for _ in range(4)]
    else:
        phis = [mp.mpf(random.uniform(0, 1)) * mp.pi for _ in range(4)]

    S1 = S_direct(phis)
    g = gaps_from_phis(phis)
    S2 = F_from_gaps(g)

    if abs(S1 - S2) > mp.mpf('1e-30'):
        mismatches += 1

    if S1 > max_S:
        max_S = S1
        worst = phis[:]

    if S1 > two_pi + mp.mpf('1e-25'):
        print("COUNTEREXAMPLE FOUND:", phis, S1)

print(f"Random search: {N_RANDOM} trials (incl. degenerate/repeated-line cases)")
print(f"  mismatches between S_direct and F(gaps): {mismatches}")
print(f"  max S found = {max_S}  (bound 2*pi = {two_pi})")
print(f"  max S - 2*pi = {max_S - two_pi}")

# (3) equality configurations
doubled = [mp.mpf(0), mp.mpf(0), mp.pi/2, mp.pi/2]
evenly = [mp.mpf(0), mp.pi/4, mp.pi/2, 3*mp.pi/4]

S_doubled = S_direct(doubled)
S_evenly = S_direct(evenly)
print(f"S(doubled orthogonal axes) = {S_doubled}   (expect 2*pi = {two_pi})")
print(f"S(evenly spaced)           = {S_evenly}   (expect 2*pi = {two_pi})")
print(f"  diff doubled: {S_doubled - two_pi}")
print(f"  diff evenly:  {S_evenly - two_pi}")

# local perturbation search around the two equality configs, to check they are local maxima
def perturb_search(base, trials=20000, eps=mp.mpf('0.05')):
    m = mp.mpf(0)
    for _ in range(trials):
        cand = [p + (mp.mpf(random.uniform(-1,1)) * eps) for p in base]
        s = S_direct(cand)
        if s > m:
            m = s
    return m

m1 = perturb_search(doubled)
m2 = perturb_search(evenly)
print(f"Local perturbation max near doubled-axes: {m1}  (2*pi={two_pi}, exceeds? {m1 > two_pi + mp.mpf('1e-20')})")
print(f"Local perturbation max near evenly-spaced: {m2}  (2*pi={two_pi}, exceeds? {m2 > two_pi + mp.mpf('1e-20')})")

# fine deterministic grid search over rational multiples of pi (denom=40) as an extra check
print("Running fine grid search over compositions of pi (denominator 40)...")
denom = 40
max_grid = mp.mpf(0)
worst_grid = None
count = 0
for c1 in range(denom+1):
    for c2 in range(denom+1-c1):
        for c3 in range(denom+1-c1-c2):
            c4 = denom - c1 - c2 - c3
            g = (mp.pi*c1/denom, mp.pi*c2/denom, mp.pi*c3/denom, mp.pi*c4/denom)
            val = F_from_gaps(g)
            count += 1
            if val > max_grid:
                max_grid = val
                worst_grid = g
print(f"Grid search: {count} compositions checked, max F = {max_grid} (2*pi={two_pi})")
print(f"  achieved at g = {worst_grid}")

print("DONE")
