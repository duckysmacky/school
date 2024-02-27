def R(N):
    n = oct(N)[2:]
    if len(n) < 3:
        return 0
    sum_1 = int(n[0]) + int(n[-1])
    sum_2 = int(n[1]) + int(n[2])
    x = str(min(sum_1, sum_2)) + str(max(sum_1, sum_2))
    return int(x[::-1])

l = []

for N in range(8**3, 8**4):
    if R(N) == 317:
        l.append(N)

print(min(l) + max(l))
# 5038
