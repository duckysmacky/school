file = open("files/9-170.csv")
count = 0
for line in file:
    nums = sorted(list(map(int, line.split(';'))))
    if len(set(nums)) == len(nums) and sum(nums) / len(nums) >= (nums[2] + nums[3]) / 2:
        print(nums)
        count += 1
print(count)
