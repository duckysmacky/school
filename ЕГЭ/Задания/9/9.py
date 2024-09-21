from itertools import permutations

file = open("files/162.txt")
count = 0

def check(nums: list) -> bool:
    for pairs in permutations(nums):
        for i in range(len(pairs)):
            left, right = pairs[:i], pairs[i:]
            if sum(left) == sum(right):
                return True
    return False

for line in file:
    nums = sorted(list(map(int, line.split())))
    if check(nums) and max(nums) - min(nums) < sum(nums[1:3]) - max(nums):
        print(nums)
        count += 1
print(count) # 15