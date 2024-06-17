def f(num: str, x: int, p: int):
    num2: int = 0
    for i, n in enumerate(num[::-1]):
        num2 += (x if n == "x" else int(n)) * p ** i
    return num2


# x1418₁₃ + 1x037₁₄ = 2x209₁₉
for x in range(19):
    if f("x1418", x, 13) + f("1x037", x, 14) == f("2x209", x, 19):
        print(f("2x209", x, 19))
# 323104
