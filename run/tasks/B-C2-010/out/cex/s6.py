# stdlib only: S6 statement example and the k=2 hand table of B9
def B(l):
    return tuple(sorted([x - 1 for x in l if x > 1] + [len(l)], reverse=True))
x = (2, 1, 1, 1, 1); orb = [x]
while x != (3, 2, 1): x = B(x); orb.append(x)
print("orbit of (2,1,1,1,1):", orb, "d_B =", len(orb) - 1)
for l in [(3,), (2, 1), (1, 1, 1)]:
    print(l, "->", B(l))
