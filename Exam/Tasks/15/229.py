for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (x & A == 0) or not ((x & 69 == 4) or (x & 118 == 6)): continue
        found = False
        break
    if found: break
print(A)
# 64
