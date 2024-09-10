file = open("files/9-162.txt")
count = 0
for line in file:
    nums = sorted(list(map(int, line.split())), reverse=True)
    if nums[0] - nums[-1] >= 50 and nums[1] * nums[2] <= 1000:
        count += 1
print(count)
