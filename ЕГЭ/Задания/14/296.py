def f(num: str, base: int):
    x: int = 0
    for i, n in enumerate(num[::-1]):
        x += int(n) * base ** i
    return x


val = str(4 ** 103 + 3 * 4 ** 444 - 2 * 4 ** 44 + 67)
print(str(f(val, 4)).count("3"))
# 13
