def f(num: str, x: int, p: int):
    num2: int = 0
    for i, n in enumerate(num[::-1]):
        num2 += (x if n == "x" else int(n)) * p ** i
    return num2


# 9009x₁₈ + 2257x₁₈
nums = []
pw = 18
dl = 15
for x in range(pw):
    a = f("9009x", x, pw)
    b = f("2257x", x, pw)
    if (a + b) % dl == 0:
        nums.append((a + b) // dl)

print(min(nums))
# 77888
