file = open("17.txt")
nums = list(map(int, file.readlines()))
groups = []

def check(nums: list) -> bool:
    return any(n % 12 == 0 for n in nums) and all(n % 3 == 0 for n in nums)

def avg(nums: list) -> float:
    return sum(nums) / len(nums)

for i in range(len(nums) - 2):
    group = nums[i:i + 3]
    if check(group):
        groups.append(group)

print(len(groups), avg(min(groups, key=avg)))