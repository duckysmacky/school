def vspr(x, y):
    for i in range(2, x):
        if x % i == 0 and y % i == 0:
            return False
    return True


for A in range(1, 10_000):
    found = True
    for x in range(1, 10_000):
        if (not vspr(x, 360) or vspr(x, A)) and (not vspr(x, A) or vspr(x, 240)): continue
        found = False
        break
    if found: break

print(A)
# 30
