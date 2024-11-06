file = open("27-A.txt")
n = int(file.readline())
nums = list(map(int, file.readlines()))

def is_prime(x: int) -> bool:
    if n < 2: return False
    for div in range(2, int(x ** 0.5) + 1):
        if n % div == 0:
            return False
    return True

def check(nums: list) -> bool:
    return len([x for x in nums if is_prime(x)]) % 9 == 0

max_sum = 0
for i in range(n):
    for j in range(n):
        group = nums[i:j + 1]
    if check(group):
        max_sum = max(max_sum, sum(group))

print(max_sum)