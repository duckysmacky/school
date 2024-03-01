def f(num: str, base: int):
    x: int = 0
    for i, n in enumerate(num[::-1]):
        x += int(n) * base ** i
    return x


val = str(6 ** 333 - 5 * 6 ** 215 + 3 * 6 ** 144 - 85)
print(str(f(val, 6)).count("5"))
# 23
