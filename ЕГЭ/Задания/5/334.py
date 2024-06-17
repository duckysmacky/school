def ter(x) -> str:
    num = []
    while x > 0:
        num.append(x % 3)
        x = x // 3
    return "".join((map(str, num[::-1])))

def R(N):
    n = ter(N)
    if N % 3 == 0:
        n = "1" + n + "02"
    else:
        n += ter((N % 3) * 4)
    return int(n, 3)

m = -1

for N in range(1, 10_000):
    if R(N) < 199:
        m = max(m, N)

print(m)
# 20