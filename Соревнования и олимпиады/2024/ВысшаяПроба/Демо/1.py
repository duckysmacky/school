from functools import reduce

def conv(x: int) -> str:
    num = ""
    while x > 0:
        num += str(x % 9)
        x //= 9
    return num[::-1]

def check(num: str) -> bool:
    if reduce(lambda val, x: val * x, map(int, num)) != 21:
        return False
    if sum(int(x) for x in num if int(x) <= 3) != 9:
        return False
    return True

nums = []
for n in range(1, 10 ** 10):
    num = conv(n)
    if check(num):
        nums.append(num)
print(int(max(nums), 9))