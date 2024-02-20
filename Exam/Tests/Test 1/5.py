def R(N):
    summ = sum([int(x) for x in str(N)])
    n = bin(summ)[2:]
    if n.count("1") % 2 == 0:
        n = f"1{n}00"
    else:
        n = f"10{n}1"
    return int(n, 2)

count = 0

for N in range(100_000_000, 999_999_999):
    if R(N) == 21:
        count += 1

print(count)
# 9
