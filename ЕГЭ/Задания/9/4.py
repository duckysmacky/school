from math import sqrt

file = open("files/97.txt")
count = 0

def check(a, b, c) -> bool:
    return a == sqrt(b ** 2 + c ** 2) or b == sqrt(a ** 2 + c ** 2) or c == sqrt(a ** 2 + b ** 2)

for line in file:
    nums = list(map(int, line.split()))
    if check(*nums):
        print(nums)
        count += 1
print(count) # 452