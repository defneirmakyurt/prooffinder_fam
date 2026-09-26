"""
Independent counterexample search / cross-check for A-C5-D2-002.

Uses mpmath with 50 decimal digits of precision (not exact rational
arithmetic, but far beyond any float rounding at the scale of interest;
used here only as a *search* tool, not as part of any proof).

Checks:
 (a) Direct evaluation of S = sum_{i<j} arccos|cos(phi_i-phi_j)| for many
     random and structured 4-tuples of line-angles phi_i in [0,pi), compared
     against the claimed bound 2*pi.
 (b) Cross-check of the proof's reduction S = F(g1,g2,g3,g4) (the gap
     formula, Step 3 of proof.md) against the direct computation of S from
     raw angles, on random instances -- this tests the correctness of the
     algebraic reduction itself, not just the final case-analysis bound.
 (c) Degenerate/repeated-line configurations (coincident lines, 3 equal +1
     distinct, all 4 equal).
 (d) A local perturbation search around the two claimed equality points to
     make sure 2*pi is a local (and, per grid search, global) maximum, not
     exceeded nearby.
"""
import itertools
import random
import mpmath as mp

mp.mp.dps = 50
PI = mp.pi

def theta_from_angles(p, q):
    # acute angle between lines with direction-angles p,q (any reals)
    return mp.acos(abs(mp.cos(p - q)))

def S_direct(phis):
    tot = mp.mpf(0)
    for i, j in itertools.combinations(range(4), 2):
        tot += theta_from_angles(phis[i], phis[j])
    return tot

def h(x):
    return min(x, PI - x)

def F_from_gaps(g):
    g1, g2, g3, g4 = g
    return h(g1) + h(g2) + h(g3) + h(g4) + h(g1 + g2) + h(g2 + g3)

def gaps_from_angles(phis):
    # representatives in [0, pi)
    reps = sorted((p % PI) for p in phis)
    p1, p2, p3, p4 = reps
    g1 = p2 - p1
    g2 = p3 - p2
    g3 = p4 - p3
    g4 = PI - p4 + p1
    return (g1, g2, g3, g4)

def main():
    rng = random.Random(20260926)
    max_S = mp.mpf('-inf')
    worst = None
    n_trials = 0
    max_reduction_err = mp.mpf(0)
    violations = []

    # (a)+(b) random search, generic + structured (with repeats)
    N = 200000
    for _ in range(N):
        mode = rng.random()
        if mode < 0.5:
            phis = [mp.mpf(rng.uniform(0, float(PI))) for _ in range(4)]
        elif mode < 0.7:
            # force one repeated pair
            phis = [mp.mpf(rng.uniform(0, float(PI))) for _ in range(3)]
            phis.append(phis[rng.randrange(3)])
        elif mode < 0.85:
            # force two repeated pairs (2+2)
            a = mp.mpf(rng.uniform(0, float(PI)))
            b = mp.mpf(rng.uniform(0, float(PI)))
            phis = [a, a, b, b]
        else:
            # 3 equal + 1 distinct, or all 4 equal
            a = mp.mpf(rng.uniform(0, float(PI)))
            if rng.random() < 0.5:
                b = mp.mpf(rng.uniform(0, float(PI)))
                phis = [a, a, a, b]
            else:
                phis = [a, a, a, a]

        n_trials += 1
        S = S_direct(phis)
        g = gaps_from_angles(phis)
        Fv = F_from_gaps(g)
        err = abs(S - Fv)
        if err > max_reduction_err:
            max_reduction_err = err
        if S > max_S:
            max_S = S
            worst = list(phis)
        if S > 2 * PI + mp.mpf('1e-30'):
            violations.append((list(phis), S))

    print(f"(a)/(b) random trials: {n_trials}")
    print(f"max S found = {max_S}  (bound 2*pi = {2*PI})")
    print(f"max |S - F(gaps)| reduction error over all trials = {max_reduction_err}")
    print(f"violations of S <= 2*pi found: {len(violations)}")

    # (c) explicit degenerate configs
    degenerate_configs = {
        "all four coincident": [mp.mpf('0.7')]*4,
        "three coincident + one distinct": [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('1.2')],
        "two pairs coincident, orthogonal": [mp.mpf(0), mp.mpf(0), PI/2, PI/2],
        "two pairs coincident, non-orthogonal": [mp.mpf('0.3'), mp.mpf('0.3'), mp.mpf('1.9'), mp.mpf('1.9')],
    }
    for name, phis in degenerate_configs.items():
        S = S_direct(phis)
        print(f"degenerate case [{name}]: S = {S}  vs 2*pi = {2*PI}  (S<=2pi: {S <= 2*PI + mp.mpf('1e-30')})")

    # (d) local perturbation search near the two claimed equality configs
    print("\n(d) perturbation search near claimed equality configurations")
    base_configs = {
        "doubled orthogonal axes": [mp.mpf(0), mp.mpf(0), PI/2, PI/2],
        "evenly spaced": [k*PI/4 for k in range(4)],
    }
    for name, base in base_configs.items():
        S0 = S_direct(base)
        max_local = S0
        for _ in range(20000):
            eps = [mp.mpf(rng.uniform(-0.05, 0.05)) for _ in range(4)]
            phis = [b + e for b, e in zip(base, eps)]
            S = S_direct(phis)
            if S > max_local:
                max_local = S
        print(f"  {name}: S(base) = {S0} (2*pi={2*PI}), max S in random local perturbation ball = {max_local}")

    # global grid search independent of gap parametrisation, to double check
    # the maximum over a fine deterministic grid of raw angles (not gaps)
    print("\nFine deterministic grid over raw angles (independent of gap reduction)")
    grid_n = 18  # 18^3 combos with phi1 fixed at 0 by rotation-invariance check
    max_grid = mp.mpf('-inf')
    worst_grid = None
    for i in range(grid_n):
        for j in range(grid_n):
            for k in range(grid_n):
                phis = [mp.mpf(0), i*PI/grid_n, j*PI/grid_n, k*PI/grid_n]
                S = S_direct(phis)
                if S > max_grid:
                    max_grid = S
                    worst_grid = phis
    print(f"grid_n={grid_n}, trials={grid_n**3}, max S = {max_grid} (2*pi={2*PI})")
    print(f"achieved near phis = {[str(x) for x in worst_grid]}")

    assert len(violations) == 0
    assert max_S <= 2*PI + mp.mpf('1e-25')
    assert max_grid <= 2*PI + mp.mpf('1e-25')
    assert max_reduction_err < mp.mpf('1e-40')
    print("\nAll counterexample-search checks passed: no violation of S <= 2*pi found; "
          "reduction S = F(gaps) confirmed numerically to ~50 digits on 200000 random instances.")

if __name__ == "__main__":
    main()
