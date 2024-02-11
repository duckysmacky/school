def R(N):
    n = bin(N)[2:]
    if N % 3 == 0:
        n += "010"
    else:
        n += bin(5 * (N % 3))[2:]
    return int(n, 2)

r = {}

for N in range(1, 10_000):
    if R(N) > 300:
        r[R(N)] = N

print(r[min(r.keys())])
# 37