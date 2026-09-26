#!/usr/bin/env python3
"""
affquot.py -- covering quotients of Q_9 by free groups of affine automorphisms v -> sigma(v) ^ a
(sigma a coordinate permutation, a in F_2^9).  Stdlib only (runs ./qls2 as a subprocess).

A group G of automorphisms acting so that (i) no g != id fixes a vertex and (ii) no g maps a vertex
to a neighbour gives a covering map Q_9 -> Q_9/G onto a 9-regular multigraph without loops; then
a G-invariant set T is an induced forest of Q_9 iff T/G is an induced forest (no parallel pair, no
cycle) of Q_9/G (proof in out/claims.md, Lemma Q).  Every lifted forest is also re-checked directly.

Usage: affquot.py involutions ITERS SEED        -- all free involution classes (t, f), t >= 1
       affquot.py one T F ITERS SEED            -- one involution class (t, f)
       affquot.py random NGROUPS ITERS SEED     -- random free affine groups of order 2, 4 or 8
"""
import sys, random, subprocess, time, os
import quotients as Q

D = 9
V = 1 << D


def apply_map(perm, a, v):
    """sigma(v) ^ a where bit i of v moves to bit perm[i]."""
    w = 0
    for i in range(D):
        if (v >> i) & 1:
            w |= 1 << perm[i]
    return w ^ a


def as_vertex_perm(perm, a):
    return tuple(apply_map(perm, a, v) for v in range(V))


def closure(gens):
    ident = tuple(range(V))
    G = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                gh = tuple(h[g[v]] for v in range(V))
                if gh not in G:
                    G.add(gh)
                    new.append(gh)
                    if len(G) > 64:
                        return None
        frontier = new
    return G


def admissible(G):
    ident = tuple(range(V))
    for g in G:
        if g == ident:
            continue
        for v in range(V):
            x = v ^ g[v]
            if x == 0 or (x & (x - 1)) == 0:     # fixed point, or maps v to a neighbour
                return False
    return True


def quotient_graph(G):
    orb = [-1] * V
    reps = []
    for v in range(V):
        if orb[v] < 0:
            for g in G:
                orb[g[v]] = len(reps)
            reps.append(v)
    adj = [[orb[v ^ (1 << i)] for i in range(D)] for v in reps]
    return orb, reps, adj


def run(G, tag, iters, seed):
    orb, reps, adj = quotient_graph(G)
    gfile = "../tmp/aq_%s.graph" % tag
    with open(gfile, "w") as fh:
        fh.write("%d\n" % len(reps))
        for row in adj:
            fh.write("%d " % len(row) + " ".join(map(str, row)) + "\n")
    ffile = "../tmp/aq_%s_s%s.F" % (tag, seed)
    out = subprocess.run(["./qls2", gfile, str(seed), str(iters), "0.6", "0.05", ffile],
                         capture_output=True, text=True).stdout.strip()
    F = set(int(l) for l in open(ffile) if l.strip())
    T = [v for v in range(V) if orb[v] in F]
    ok = Q.is_forest_qd(T)
    fn = "../tmp/aqlift_%s_s%s_%d.txt" % (tag, seed, len(T))
    with open(fn, "w") as fh:
        fh.write("\n".join(format(x, "09b") for x in sorted(T)) + "\n")
    return len(reps), len(F), len(T), ok, out


def involution(t, f):
    perm = list(range(D))
    for p in range(t):
        perm[2 * p], perm[2 * p + 1] = 2 * p + 1, 2 * p
    a = 0
    for j in range(2 * t, 2 * t + f):
        a |= 1 << j
    return perm, a


def main():
    mode = sys.argv[1]
    if mode == "involutions":
        iters, seed = int(sys.argv[2]), int(sys.argv[3])
        for t in (1, 2, 3):
            for f in range(2, D - 2 * t + 1):
                perm, a = involution(t, f)
                G = closure([as_vertex_perm(perm, a)])
                assert len(G) == 2 and admissible(G)
                t0 = time.time()
                res = run(G, "inv_t%d_f%d" % (t, f), iters, seed)
                print("involution t=%d f=%d |G|=2 quotient_n=%d |F|=%d |T|=%d lift_forest=%s (%s) %.1fs"
                      % (t, f, res[0], res[1], res[2], res[3], res[4], time.time() - t0), flush=True)
    elif mode == "one":
        t, f, iters, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
        perm, a = involution(t, f)
        G = closure([as_vertex_perm(perm, a)])
        assert len(G) == 2 and admissible(G)
        t0 = time.time()
        res = run(G, "inv_t%d_f%d" % (t, f), iters, seed)
        print("involution t=%d f=%d seed=%d iters=%d quotient_n=%d |F|=%d |T|=%d lift_forest=%s (%s) %.1fs"
              % (t, f, seed, iters, res[0], res[1], res[2], res[3], res[4], time.time() - t0), flush=True)
    elif mode == "random":
        ng, iters, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        rng = random.Random(seed)
        done = 0
        tries = 0
        seen = set()
        while done < ng and tries < 5000:
            tries += 1
            gens = []
            for _ in range(rng.choice((1, 2))):
                perm = list(range(D))
                # random permutation with cycle type from small cycles (order 2 or 4)
                idx = list(range(D)); rng.shuffle(idx)
                pos = 0
                while pos < D:
                    L = rng.choice((1, 1, 2, 2, 4))
                    cyc = idx[pos:pos + L]
                    for q in range(len(cyc)):
                        perm[cyc[q]] = cyc[(q + 1) % len(cyc)]
                    pos += L
                a = rng.randrange(V)
                gens.append(as_vertex_perm(perm, a))
            G = closure(gens)
            if G is None or len(G) not in (2, 4, 8) or not admissible(G):
                continue
            orb, reps, adj = quotient_graph(G)
            inv = (len(G), tuple(sorted(tuple(sorted(r)) for r in adj))[:0], sum(len(set(r)) for r in adj))
            key = (len(G), sum(len(set(r)) for r in adj),
                   tuple(sorted(len(set(orb[v ^ (1 << i) ^ (1 << j)] for i in range(D) for j in range(i + 1, D)))
                                for v in reps[:8])))
            if key in seen:
                continue
            seen.add(key)
            done += 1
            t0 = time.time()
            res = run(G, "rnd%d_%d" % (seed, done), iters, seed)
            print("random group #%d |G|=%d quotient_n=%d |F|=%d |T|=%d lift_forest=%s (%s) %.1fs"
                  % (done, len(G), res[0], res[1], res[2], res[3], res[4], time.time() - t0), flush=True)


if __name__ == "__main__":
    main()
