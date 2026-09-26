#!/usr/bin/env python3
"""S7 cross-cell sanity (not part of the subject's proof): build labellings of Q_5 and Q_6 from an
induced forest T whose complement S is independent (label trees of T in BFS order, then S), write
them in hand-in format to out/cex/Q5_ref.txt, Q6_ref.txt, to be scored by the accepted checker.
Q_5 forest: first pair (T0,T1) of Q_4-forests (sizes sum 18) whose union is a Q_5 forest with independent complement. Q_6: T5 x {0} u (T5 xor a) x {1}, a searched."""
import itertools

def check_and_label(d, T):
    n = 1 << d; Ts = set(T); S = [v for v in range(n) if v not in Ts]; Ss = set(S)
    if any((v ^ (1 << j)) in Ss for v in S for j in range(d)): return None
    e = sum(1 for v in T for j in range(d) if (v >> j) & 1 == 0 and (v ^ (1 << j)) in Ts)
    order = []; seen = set()
    for r in T:
        if r in seen: continue
        seen.add(r); q = [r]; k = 0
        while k < len(q):
            x = q[k]; k += 1
            for j in range(d):
                w = x ^ (1 << j)
                if w in Ts and w not in seen: seen.add(w); q.append(w)
        order += q
    comps = sum(1 for _ in [0])  # placeholder
    # forest test: edges == |T| - #components
    ncomp = 0; seen2 = set()
    for r in T:
        if r in seen2: continue
        ncomp += 1; st = [r]; seen2.add(r)
        while st:
            x = st.pop()
            for j in range(d):
                w = x ^ (1 << j)
                if w in Ts and w not in seen2: seen2.add(w); st.append(w)
    if e != len(T) - ncomp: return None
    return order + S


def _forest4(m):
    vs=[v for v in range(16) if m>>v&1]; e=sum(1 for v in vs for j in range(4) if v>>j&1==0 and m>>(v^(1<<j))&1)
    seen=0; c=0
    for r in vs:
        if seen>>r&1: continue
        c+=1; seen|=1<<r; st=[r]
        while st:
            x=st.pop()
            for j in range(4):
                w=x^(1<<j)
                if m>>w&1 and not seen>>w&1: seen|=1<<w; st.append(w)
    return e==len(vs)-c
def _indep4(m):
    return all(not (m>>(v^(1<<j))&1) for v in range(16) if m>>v&1 for j in range(4))
F4=[m for m in range(1<<16) if _forest4(m) and bin(m).count('1')>=8 and _indep4(0xffff^m)]
T5=None
for m0 in F4:
    for m1 in F4:
        if bin(m0).count('1')+bin(m1).count('1')!=18: continue
        if (0xffff^m0)&(0xffff^m1): continue   # direction-5 edges inside S
        cand=[v for v in range(16) if m0>>v&1]+[v+16 for v in range(16) if m1>>v&1]
        if check_and_label(5,cand): T5=cand; break
    if T5: break
print("Q5 forest with independent complement:", T5)


o5 = check_and_label(5, T5)
assert o5 is not None
open('/home/user/bainsahackathon/run/tasks/H-C4-002/out/cex/Q5_ref.txt', 'w').write(
    ''.join(format(v, '05b') + '\n' for v in o5))
print("Q5: |T|=18, S independent, T forest; predicted count", 32 + 4 * 14)
done = False
for a in range(32):
    T6 = T5 + [(v ^ a) + 32 for v in T5]
    o6 = check_and_label(6, T6)
    if o6:
        open('/home/user/bainsahackathon/run/tasks/H-C4-002/out/cex/Q6_ref.txt', 'w').write(
            ''.join(format(v, '06b') + '\n' for v in o6))
        print("Q6: a=%d gives |T|=36 forest with independent S; predicted count" % a, 64 + 5 * 28)
        done = True; break
if not done: print("Q6: no translate works")
