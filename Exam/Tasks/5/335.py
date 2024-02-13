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

l = []

for N in range(8**3, 8**4):
    if R(N) == 317:
        l.append(N)

print(min(l) + max(l))
# ????
