D = lambda n, m: n % m == 0

c = 0
B = range(160, 181)
for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if not (x in B) or (not D(x, 35) or D(x, A)): continue
        found = False
        break
    if found: c += 1
print(c)
# 6
