file = open("18.txt")
nums = list(map(int, file.readlines()))

groups = []
i, j = 0, 0
while j < len(nums):
    group = nums[i:j + 1]
    if all(n % 2 != 0 for n in group):
        groups.append(group)
        j += 1
    else:
        j += 1
        i = j

print(len(max(groups, key=len)))