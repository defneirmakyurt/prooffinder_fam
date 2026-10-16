"""R4: stochastic local search (swap moves, simulated annealing) for low-count labellings of Q_d.
Upper-bound generator only; the reported score comes from inbox/checker/verify.py."""
import math, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uphill import count, to_lines

def anneal(d, seed, iters=200000, T0=3.0, T1=0.05):
    rng = random.Random(seed)
    n = 1 << d
    order = list(range(n)); rng.shuffle(order)
    c = count(d, order); best, barg = c, order[:]
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        i, j = rng.randrange(n), rng.randrange(n)
        if i == j: continue
        order[i], order[j] = order[j], order[i]
        c2 = count(d, order)
        if c2 <= c or rng.random() < math.exp((c - c2) / T):
            c = c2
            if c < best: best, barg = c, order[:]
        else:
            order[i], order[j] = order[j], order[i]
    return best, barg

if __name__ == "__main__":
    d = int(sys.argv[1]); seeds = range(int(sys.argv[2])); out = sys.argv[3] if len(sys.argv) > 3 else None
    iters = int(sys.argv[4]) if len(sys.argv) > 4 else 200000
    gb, ga = None, None
    for s in seeds:
        b, a = anneal(d, s, iters)
        print("seed", s, "best", b, flush=True)
        if gb is None or b < gb: gb, ga = b, a
    print("overall best", gb)
    print(to_lines(d, ga), end="")
    if out: open(out, "w").write(to_lines(d, ga))
