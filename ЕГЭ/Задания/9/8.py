file = open("files/169.txt")
count = 0
for line in file:
    nums = list(map(int, line.split()))
    avg = (min(nums) + max(nums)) / 2
    if avg % 1 != 0: continue
    if nums.count(int(avg)) > 0:
        print(nums, avg)
        count += 1
print(count) # 76