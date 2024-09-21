file = open("files/107.txt")
count = 0
for line in file:
    nums = list(map(int, line.split()))
    if sum(nums) == 180:
        print(nums)
        count += 1
print(count) # 2374