def f(num: str, base: int):
    x: int = 0
    for i, n in enumerate(num[::-1]):
        x += int(n) * base ** i
    return x


val = str(6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 77)
print(str(f(val, 6)).count("5"))
# 23
