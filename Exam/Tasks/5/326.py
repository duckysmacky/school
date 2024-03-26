# TODO
def R(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = "1" + n + n[-1]
    else:
        n += "0"
        n += n[-1]
    return int(n, 2)


d = {}

for N in range(1, 10_000):
    if R(N) > 100:
        d[R(N)] = N


print(d[min(d.keys())])
# 20