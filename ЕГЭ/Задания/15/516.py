D = lambda n, m: n % m == 0

B = range(10, 41)
for a in range(1, 10_000):
    A = range(1, a)
    found = True
    for x in range(1, 10_000):
        if (x in A) or (not (x in B) or not D(x, 6)): continue
        found = False
        break
    if found: break
print(len(A))
# 36
