D = lambda n, m: n % m == 0

B = range(20, 81)
for a in range(1, 10_000):
    A = range(1, a)
    found = True
    for x in range(1, 10_000):
        if not (x in B) or (not D(x, 17) or (x in A)): continue
        found = False
        break
    if found: break
print(len(A))
# 68
