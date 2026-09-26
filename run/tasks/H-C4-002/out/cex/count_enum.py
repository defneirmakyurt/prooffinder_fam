#!/usr/bin/env python3
"""Independent re-count (referee): validate artefact format strictly and count uphill paths by
EXPLICIT enumeration of every sequence (DFS from each valley along strictly increasing labels),
not by the N(v) recurrence. Also reports S = {down>=2}, |S|, whether S is independent, whether
T = V\\S induces a forest, and Lemma A bound 2^d+(d-1)|S|. Stdlib, exact ints."""
import sys

def load(fn, d):
    raw = open(fn, 'rb').read()
    txt = raw.decode('ascii')
    lines = txt.split('\n')
    if lines[-1] == '':
        lines = lines[:-1]
    assert len(lines) == 2 ** d, ('line count', len(lines))
    for s in lines:
        assert len(s) == d and set(s) <= set('01'), s
    assert len(set(lines)) == 2 ** d
    return [int(s, 2) for s in lines]  # order[i] gets label i+1

def main():
    for fn, d in zip(sys.argv[1::2], sys.argv[2::2]):
        d = int(d); n = 1 << d
        order = load(fn, d)
        f = {v: i + 1 for i, v in enumerate(order)}
        nb = lambda v: [v ^ (1 << j) for j in range(d)]
        valleys = [v for v in range(n) if all(f[w] > f[v] for w in nb(v))]
        # explicit DFS enumeration of all uphill sequences
        count = 0
        stack = [(v,) for v in valleys]
        while stack:
            p = stack.pop(); count += 1
            last = p[-1]
            for w in nb(last):
                if f[w] > f[last]:
                    stack.append(p + (w,))
        down = {v: sum(1 for w in nb(v) if f[w] < f[v]) for v in range(n)}
        S = {v for v in range(n) if down[v] >= 2}
        indep = all(w not in S for v in S for w in nb(v))
        # forest test on T: edges == |T| - components
        T = [v for v in range(n) if v not in S]
        Tset = set(T)
        edges = sum(1 for v in T for w in nb(v) if w in Tset and w > v)
        seen = set(); comps = 0
        for r in T:
            if r in seen: continue
            comps += 1; seen.add(r); st = [r]
            while st:
                x = st.pop()
                for w in nb(x):
                    if w in Tset and w not in seen:
                        seen.add(w); st.append(w)
        forest = (edges == len(T) - comps)
        print("%s d=%d first=%s last=%s valleys=%d uphill(enumerated)=%d |S|=%d S_independent=%s "
              "T_forest=%s lemmaA_bound=%d" % (fn, d, format(order[0], '0%db' % d), format(order[-1], '0%db' % d),
              len(valleys), count, len(S), indep, forest, n + (d - 1) * len(S)))

main()
