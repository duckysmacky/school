def f(x: int, base: int):
    num = []
    while x > 0:
        num.append(x % base)
        x = x // base
    return "".join((map(str, num[::-1])))


m = 10 ** 10

for i in range(2, 32):
    if len(str(f(70, i))) == 3:
        m = min(m, i)

print(m)
# 5
