def f(num: str, x: int, p: int):
    num2: int = 0
    for i, n in enumerate(num[::-1]):
        num2 += (x if n == "x" else int(n)) * p ** i
    return num2


# 9759x₁₇ + 3x108₁₇
nums = []
pw = 17
dl = 11
for x in range(pw):
    a = f("9759x", x, pw)
    b = f("3x108", x, pw)
    if (a + b) % dl == 0:
        nums.append((a + b) // dl)

print(min(nums))
# 95306
