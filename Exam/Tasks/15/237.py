D = range(133, 178)
B = range(144, 191)

for i in range(1, 100):
    for j in range(1, 500):
        A = range(i, j)
        found = True
        for x in range(1, 10_000):
            if not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D)): continue
            found = False
            break
        if found: break
print(j - i)
# 45


for a in range(0, 100):
    for b in range(a, 100):
        k = 0
        for i in range(1, 200):
            x = i / 2
            if not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D)):
                k = k + 1
                continue

        if k == 199:
            mn = min(mn, b - a)
