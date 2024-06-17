def f(num: str, x: int, p: int):
    num2: int = 0
    for i, n in enumerate(num[::-1]):
        num2 += (x if n == "x" else int(n)) * p ** i
    return num2


# 55x36₁₉ + x2724₁₉
nums = []
pw = 19
dl = 11
for x in range(pw):
    a = f("55x36", x, pw)
    b = f("x2724", x, pw)
    if (a + b) % dl == 0:
        nums.append((a + b) // dl)

print(min(nums))
# 135122
