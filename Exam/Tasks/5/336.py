def R(N):
    if N % 2 == 0:
        N /= 2
    else:
        N -= 1
    if N % 6 == 0:
        N /= 6
    else:
        N -= 1
    if N % 15 == 0:
        N /= 15
    else:
        N -= 1
    return N


m = 10 ** 10

for N in range(1, 10_000):
    if "c" in hex(N)[2:] and R(N) == 523:
        m = min(m, N)

print(m)
# 3145