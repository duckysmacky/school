D = lambda n, m: n % m == 0

B = range(70, 81)
for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if D(x, A) or (not (x in B) or not D(x, 18)): continue
        found = False
        break
    if found: print(A)
# 72
