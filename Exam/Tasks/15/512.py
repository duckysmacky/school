D = lambda n, m: n % m == 0

B = range(50, 71)
for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if D(x, A) or (not D(x, 23) or not (x in B)): continue
        found = False
        break
    if found: print(A)
# 69
