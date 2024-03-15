for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (x & 30 != 4) or (not (x & 35 == 1) or (x & A == 0)): continue
        found = False
        break
    if found: print(A)
# 58
