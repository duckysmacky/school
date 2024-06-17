D = lambda n, m: n % m == 0

c = 0
B = range(70, 81)
for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if not (D(x, 12) and (x in B) and not D(x, A)): continue
        found = False
        break
    if found: c += 1
print(c)
# 12
