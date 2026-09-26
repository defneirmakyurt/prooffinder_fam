# Large-neighbourhood exact search for a larger induced forest of Q_9 (UPPER route of H-C5).
# Start: F0 = odd vertices u C, C an even (9,4) code of size 20 (found by SAT below) -> |F0| = 276, |S| = 236.
# For each ball B(v, R) (Hamming radius R): keep F0 outside the ball fixed, let the ball vertices be free,
# and ask a SAT solver (CEGAR: lazy cycle-exclusion clauses) for an induced forest with |F| >= 277.
# UNSAT for a ball = no 277-forest agrees with F0 outside that ball (for this particular F0).
# Search tool only: UNSAT results prove nothing about nabla(Q_9) in general.
import sys, time, random, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType

n = 9; N = 1 << n
nb = [[v ^ (1 << i) for i in range(n)] for v in range(N)]
wt = [bin(v).count('1') for v in range(N)]

def find_code(size=20, seed=0):
    ev = [v for v in range(N) if wt[v] % 2 == 0]
    idx = {v: i + 1 for i, v in enumerate(ev)}
    cl = []
    for a, b in itertools.combinations(ev, 2):
        if wt[a ^ b] == 2:
            cl.append([-idx[a], -idx[b]])
    cl.append([idx[0]])  # symmetry: 0 in code
    top = len(ev)
    card = CardEnc.atleast(lits=list(idx.values()), bound=size, top_id=top, encoding=EncType.seqcounter)
    s = Cadical153(bootstrap_with=cl + card.clauses)
    assert s.solve()
    m = set(l for l in s.get_model() if l > 0)
    return [v for v in ev if idx[v] in m]

def find_cycle(F):
    # return list of vertices of a cycle in Q_n[F], or None
    inF = bytearray(N)
    for v in F: inF[v] = 1
    parent = {}
    for r in F:
        if r in parent: continue
        parent[r] = -1
        stack = [r]
        while stack:
            u = stack.pop()
            for w in nb[u]:
                if not inF[w] or w == parent[u]: continue
                if w in parent:
                    # cycle: path u..lca..w
                    pu = [u]; x = u
                    while parent[x] != -1: x = parent[x]; pu.append(x)
                    pw = [w]; x = w
                    while parent[x] != -1: x = parent[x]; pw.append(x)
                    sw = set(pw)
                    cyc = []
                    for x in pu:
                        cyc.append(x)
                        if x in sw: lca = x; break
                    cyc += pw[:pw.index(lca)][::-1]
                    return cyc
                parent[w] = u
                stack.append(w)
    return None


def short_cycles():
    # all 4-cycles of Q_n, and the 6-cycles through the base vertex of each Q_3 subcube (12 of its 16 6-cycles;
    # the other 4 are caught lazily by CEGAR). Every clause added is a genuine cycle, so UNSAT is sound.
    cyc = []
    for base in range(N):
        for i, j in itertools.combinations(range(n), 2):
            if base & (1 << i) or base & (1 << j): continue
            a, b = 1 << i, 1 << j
            cyc.append([base, base | a, base | a | b, base | b])
    q3 = []
    for p in itertools.permutations(range(1, 8), 5):
        seq = [0] + list(p)
        if seq[1] > seq[5]: continue
        if all(bin(seq[k] ^ seq[(k + 1) % 6]).count('1') == 1 for k in range(6)):
            q3.append(seq)
    for base in range(N):
        for dirs in itertools.combinations(range(n), 3):
            if any(base & (1 << t) for t in dirs): continue
            sub = [base | sum(1 << dirs[t] for t in range(3) if (m >> t) & 1) for m in range(8)]
            for seq in q3:
                cyc.append([sub[m] for m in seq])
    return cyc
SHORT = []

def ball_search(F0, centre, R, tlimit):
    free = [v for v in range(N) if wt[v ^ centre] <= R]
    fs = set(free)
    fixedF = [v for v in F0 if v not in fs]
    need = 277 - len(fixedF)
    var = {v: i + 1 for i, v in enumerate(free)}
    card = CardEnc.atleast(lits=list(var.values()), bound=need, top_id=len(free), encoding=EncType.seqcounter)
    s = Cadical153(bootstrap_with=card.clauses)
    inF0 = set(F0)
    for cy in SHORT:
        if any(v in fs for v in cy) and all((v in fs) or (v in inF0) for v in cy):
            s.add_clause([-var[v] for v in cy if v in fs])
    t0 = time.time(); it = 0
    while True:
        if time.time() - t0 > tlimit: return 'TIMEOUT', it
        if not s.solve(): return 'UNSAT', it
        m = s.get_model()
        chosen = [v for v in free if m[var[v] - 1] > 0]
        F = fixedF + chosen
        cyc = find_cycle(F)
        it += 1
        if cyc is None:
            return ('FOUND', sorted(F)), it
        Fs = set(F)
        while cyc is not None:   # add several cycle cuts per SAT call
            s.add_clause([-var[v] for v in cyc if v in fs])
            Fs.discard(next(v for v in cyc if v in fs))
            cyc = find_cycle(sorted(Fs))

if __name__ == '__main__':
    R = int(sys.argv[1]); ncent = int(sys.argv[2]); tl = float(sys.argv[3]); seed = int(sys.argv[4])
    t0 = time.time()
    SHORT.extend(short_cycles())
    print('short cycles', len(SHORT), flush=True)
    C = find_code()
    assert len(C) == 20 and all(wt[a ^ b] >= 4 for a, b in itertools.combinations(C, 2))
    F0 = [v for v in range(N) if wt[v] % 2 == 1] + C
    assert find_cycle(F0) is None and len(F0) == 276
    print('code found, |F0| = 276 forest verified, %.1fs' % (time.time() - t0), flush=True)
    random.seed(seed)
    cents = list(range(N)); random.shuffle(cents); cents = cents[:ncent]
    stats = {}
    for c in cents:
        res, it = ball_search(F0, c, R, tl)
        key = res if isinstance(res, str) else res[0]
        stats[key] = stats.get(key, 0) + 1
        print("centre", c, key, "iters", it, "t=%.1fs" % (time.time() - t0), flush=True)
        if key == 'FOUND':
            print('FOUND 277-forest at centre', c, flush=True)
            open('found_F.txt', 'w').write('\n'.join(format(v, '09b') for v in res[1]))
            break
    print('R =', R, 'centres tried', sum(stats.values()), stats, 'total %.1fs' % (time.time() - t0))
