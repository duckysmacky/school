def ter(x) -> str:
    num = []
    while x > 0:
        num.append(x % 3)
        x = x // 3
    return "".join((map(str, num[::-1])))


def R(N):
    n = ter(N)
    if N % 3 == 0:
        n += n[-2:]
    else:
        n += ter((N % 3) * 5)
    return int(n, 3)


m = 10 ** 10

for N in range(1, 10_000):
    if R(N) > 133:
        m = min(m, R(N))

print(m)
# 141