sn = lambda x, y: x + y <= 0

for z in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if not (not sn(x, 5 - z)) or (not sn(x, -8) or sn(x, 4)): continue
        found = False
        break
    if found: break

print(z)
# 13
