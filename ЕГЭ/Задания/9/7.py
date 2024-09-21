file = open("files/107_9.txt")
count = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if (nums[0] + nums[-1]) ** 2 > sum(map(lambda x: x ** 2, nums[1:4])):
        print(nums)
        count += 1
print(count) # 2640