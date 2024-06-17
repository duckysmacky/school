def R(N):
    n = bin(N)[2:]
    if N % 3 == 0:
        n += n[-3:]
    else:
        n += bin((N % 3) * 3)[2:]
    return int(n, 2)

m = -1

for N in range(1, 10_000):
    if R(N) < 170:
        m = max(m, R(N))

print(m)
# 166