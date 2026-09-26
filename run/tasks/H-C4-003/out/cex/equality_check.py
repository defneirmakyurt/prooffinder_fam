#!/usr/bin/env python3
"""Referee: equality structure of the artefacts and the subject's F_5 witness (stdlib, exact)."""
import sys
def forest(Tset, d):
    e = sum(1 for v in Tset for j in range(d) if (v ^ (1 << j)) in Tset) // 2
    seen = set(); c = 0
    for r in Tset:
        if r in seen: continue
        c += 1; seen.add(r); st = [r]
        while st:
            v = st.pop()
            for j in range(d):
                w = v ^ (1 << j)
                if w in Tset and w not in seen: seen.add(w); st.append(w)
    return e == len(Tset) - c, e, c
for fn in sys.argv[1:]:
    rows = open(fn).read().split(); d = len(rows[0]); n = 1 << d
    f = {int(r, 2): i for i, r in enumerate(rows, 1)}
    down = {v: sum(1 for j in range(d) if f[v ^ (1 << j)] < f[v]) for v in range(n)}
    S = {v for v in range(n) if down[v] >= 2}; T = set(range(n)) - S
    indep = all((v ^ (1 << j)) not in S for v in S for j in range(d))
    ok, e, c = forest(T, d)
    print("%s: |S|=%d (2^d-|S|=%d), S independent=%s, down-degrees on S=%s, T forest=%s (e=%d, comps=%d), LemmaA bound=%d"
          % (fn.split('/')[-1], len(S), n - len(S), indep, sorted(set(down[v] for v in S)), ok, e, c, n + (d - 1) * len(S)))
T0 = 0b1011011101001; T1 = 0b1110100110010111
W = {x for x in range(16) if T0 >> x & 1} | {x + 16 for x in range(16) if T1 >> x & 1}
print("subject F_5 witness: size=%d, induced forest=%s" % (len(W), forest(W, 5)[0]))
