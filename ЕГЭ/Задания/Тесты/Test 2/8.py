from itertools import product

key = "012345"
nums = list(product(key, repeat=5))
c = 0

def check(num: str):
    if num[0] == "0": return False
    for i in range(len(num) - 1):
        if ((int(num[i]) % 2 == 0) == (int(num[i + 1]) % 2 == 0)): return False
    return True

for num in nums:
    if check(num): c += 1

print(c)
# 405