def B(l):
    s=len(l); return tuple(sorted([x-1 for x in l if x>1]+[s],reverse=True))
x=(2,1,1,1,1); seq=[x]
for _ in range(4): x=B(x); seq.append(x)
print(seq)
