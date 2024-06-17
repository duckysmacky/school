def R(N):
    n = bin(N)[2:]
    if n.count("1") % 4 == 0:
        n = "10" + n
    else:
        n = "11" + n
    if int(n, 2) % 2 != 0:
        n += "0"
    else:
        n += "1"
    return int(n, 2)

m = -1

for N in range(1, 10_000):
    if R(N) <= 250:
        m = max(m, N)

print(m)
# 30