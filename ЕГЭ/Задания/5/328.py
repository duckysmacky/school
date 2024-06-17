def R(N):
    n = bin(N)[2:]
    if N % 5 == 0:
        n = "1" + n + n[-2:]
    else:
        n = bin(N % 5)[2:] + n
    return int(n, 2)

m = -1

for N in range(1, 10_000):
    if R(N) <= 223:
        m = max(m, R(N))

print(m)
# 219