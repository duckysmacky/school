def f(num: str, base: int):
    x: int = 0
    for i, n in enumerate(num[::-1]):
        x += int(n) * base ** i
    return x


val = str(7 ** 103 - 6 * 7 ** 70 + 3 * 7 ** 57 - 98)
print(str(f(val, 7)).count("6"))
# 9
