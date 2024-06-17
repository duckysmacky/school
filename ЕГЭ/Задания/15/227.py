for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (not (x & A != 0) or (x & 55 == 33)) or (x & 112 != 16): continue
        found = False
        break
    if found: break
print(A)
# 32
