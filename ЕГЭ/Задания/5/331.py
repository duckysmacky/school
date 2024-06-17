def R(N):
    n = bin(N)[2:]
    if N % 2 != 0:
        n = "".join(["1" if x == "0" else "0" for x in n])
    n = "".join([str(x * 2) for x in n])
    return int(n, 2)


m = 10 ** 10

for N in range(1, 10_000):
    if R(N) > 60:
        m = min(m, N)

print(m)
# 8
