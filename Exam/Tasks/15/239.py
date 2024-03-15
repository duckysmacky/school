D = range(155, 178)
B = range(111, 131)

for a in range(1, 10_000):
    A = range(1, a)
    found = True
    for x in range(1, 10_000):
        if not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D)): continue
        found = False
        break
    if found: break
print(len(A))
# 177
