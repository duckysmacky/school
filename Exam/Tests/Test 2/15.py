D = lambda n, m: n % m == 0

for A in range(1000, 100_000):
    found = True
    for x in range(1, 10_000):
        if ((not D(x, A) or D(x, 36) and D(x, 126)) and (A > 1000)): continue
        found = False
        break
    if found: break
        
print(A)
# 1008