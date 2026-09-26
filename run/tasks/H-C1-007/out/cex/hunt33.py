"""Referee H-C1-007: hard stochastic hunt for a labelling of Q_4 with <= 33 uphill paths
(and of Q_3 with <= 13).  Stdlib, exact integers.  A negative result is evidence, not proof;
the proof of U(Q_4) >= 34 is the subject's Steps 5-7, checked by hand.

Also checks the closing Remark's number theory for d = 2..40 (outside the cell's range).
"""
import random
import sys
import time


def nbrs_cube(d):
    return [tuple(v ^ (1 << j) for j in range(d)) for v in range(1 << d)]


def score(order, nbr):
    n = len(order)
    lab = [0] * n
    for i, v in enumerate(order, 1):
        lab[v] = i
    N = [0] * n
    tot = 0
    for v in order:
        s = 0
        low = False
        for w in nbr[v]:
            if lab[w] < lab[v]:
                low = True
                s += N[w]
        N[v] = s if low else 1
        tot += N[v]
    return tot


def anneal(d, target, restarts, steps, seed):
    n = 1 << d
    nbr = nbrs_cube(d)
    rng = random.Random(seed)
    best = None
    best_o = None
    evals = 0
    hist = {}
    for r in range(restarts):
        o = list(range(n))
        rng.shuffle(o)
        cur = score(o, nbr)
        evals += 1
        T0, T1 = 3.0, 0.02
        for s in range(steps):
            # temperature schedule uses floats only for the ACCEPTANCE COIN;
            # every reported objective value is an exact integer.
            T = T0 * ((T1 / T0) ** (s / steps))
            i = rng.randrange(n)
            j = rng.randrange(n)
            if i == j:
                continue
            o[i], o[j] = o[j], o[i]
            t = score(o, nbr)
            evals += 1
            hist[t] = hist.get(t, 0) + 1
            if t <= cur or rng.random() < pow(2.718281828459045, -(t - cur) / T):
                cur = t
                if best is None or t < best:
                    best, best_o = t, list(o)
                    if best <= target:
                        return best, best_o, evals, hist
            else:
                o[i], o[j] = o[j], o[i]
    return best, best_o, evals, hist


if __name__ == "__main__":
    for d, target, restarts, steps in [(3, 13, 200, 4000), (4, 33, 400, 12000)]:
        t0 = time.time()
        b, o, evals, hist = anneal(d, target, restarts, steps, seed=20260926 + d)
        el = time.time() - t0
        lo = sorted(hist)[:4]
        print("Q_%d: simulated annealing, %d restarts x %d steps, %d exact evaluations, "
              "%.1fs" % (d, restarts, steps, evals, el))
        print("     best found = %d ; target <= %d %s" % (b, target,
              "REACHED (counterexample!)" if b <= target else "NOT reached"))
        print("     lowest values ever visited: %s" % [(v, hist[v]) for v in lo])
        print("     best labelling: %s"
              % ["".join(str((v >> (d - 1 - j)) & 1) for j in range(d)) for v in o])
        sys.stdout.flush()

    print()
    print("closing Remark (outside the cell): (d-1) | 2^(d-1)(d-2)+1 for d = 2..40")
    ok = [d for d in range(2, 41) if (2 ** (d - 1) * (d - 2) + 1) % (d - 1) == 0]
    print("   d for which the equality condition of Step 6 can hold at all:", ok)
