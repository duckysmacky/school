for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (x & 25 != 1) or (not (x & 34 == 2) or (x & A == 0)): continue
        found = False
        break
    if found: break
print(A)
# 8
