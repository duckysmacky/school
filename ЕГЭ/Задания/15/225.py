for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (not (x & A != 0) or (x & 39 == 7)) or (x & 30 != 6): continue
        found = False
        break
    if found: break
print(A)
# 8
