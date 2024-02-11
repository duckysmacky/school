def eight(x) -> str:
    num = []
    while x > 0:
        num.append(x % 8)
        x = x // 8
    return "".join((map(str, num[::-1])))


def R(N):
    n = eight(N)
    if len(n) < 3:
        return 0
    sum_1 = int(n[0]) + int(n[-1])
    sum_2 = int(n[1]) + int(n[2])
    x = str(min(sum_1, sum_2)) + str(max(sum_1, sum_2))
    return int(x)


mn = 10 ** 10
mx = -1

for N in range(1, 100):
    if R(N) == 317:
        mn = min(mn, N)
        mx = max(mx, N)

print(mn + mx)
# ????
