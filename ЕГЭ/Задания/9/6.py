file = open("files/150.txt")
count = 0
for line in file:
    nums = sorted(list(map(int, line.split())))
    if nums[-1] ** 2 > 2 * sum(nums[:2]):
        print(nums)
        count += 1
print(count) # 3200