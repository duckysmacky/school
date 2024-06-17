Del = lambda n, m: n % m == 0

a = []
for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if not Del(x, A) or (Del(x, 6) or Del(x, 15)): continue
        found = False
        break
    if found: break


print(A)
# 6