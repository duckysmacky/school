def f(num: str, x: int, p: int):
    num2: int = 0
    for i, n in enumerate(num[::-1]):
        num2 += (x if n == "x" else int(n)) * p ** i
    return num2


# 3364x₁₁ + x7946₁₂ = 55x87₁₄
for x in range(14):
    if f("3364x", x, 11) + f("x7946", x, 12) == f("55x87", x, 14):
        print(f("55x87", x, 14))
# 207291
