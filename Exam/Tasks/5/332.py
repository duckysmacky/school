def R(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += "0"
    else:
        n += "1"
    if n[:-1].count("1") % 2 == 0:
        n += "0"
    else:
        n += "1"
    return int(n, 2)


m = 10 ** 10

for N in range(1, 10_000):
    if R(N) > 2023:
        m = min(m, R(N))

print(m)
# 2025